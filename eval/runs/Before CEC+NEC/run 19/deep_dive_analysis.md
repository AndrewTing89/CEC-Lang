# Deep Dive: Why Prompt Fixes Changed Behavior But Not Answers

## Executive Summary

The Run 19 prompt fixes successfully changed **agent behavior** (using correct tools) but failed to fix **answer content** because:

1. **Table Questions (cec-007, cec-008):** The tools return correct content, but the **enforcement loop forces exception searches** that return weakly-related content, which then **dominates the agent's answer synthesis**

2. **Comparison Question (cec-026):** The tools return **similar-looking text** from both codes, and the **critical scope difference is buried** in the results - the agent can't identify subtle semantic distinctions

---

## Deep Dive 1: Table Content Questions (cec-007, cec-008)

### What the Tools Actually Return

**cec-007: "What does CEC Table 240.4(G) specify?"**

| Tool | Output Quality | Key Content |
|------|---------------|-------------|
| `cec_lookup_table` | EXCELLENT | "CEC 2022 Table 240.4(G) - Specific Conductor Applications... Headers: Conductor \| Article \| Section... Air-conditioning, Capacitor, Control circuits, Welders, Fire alarm, Motor-operated appliances..." |
| `compare_with_nec` | Good | Structured comparison showing CEC vs NEC table entries |
| `cec_exception_search` | POOR (0.50 relevance) | Returns Section 230.90 exceptions about service conductor protection - **not related to Table 240.4(G)** |

**cec-008: "What does CEC Table 242.3 specify?"**

| Tool | Output Quality | Key Content |
|------|---------------|-------------|
| `cec_lookup_table` | EXCELLENT | "CEC 2022 Table 242.3 - Other Articles... **This is a California-specific NEW table (N marker) not found in the base NEC**... Lists equipment types: Class I locations, Class II locations..." |
| `compare_with_nec` | Good | Shows CEC table exists, NEC doesn't have equivalent |
| `cec_exception_search` | POOR (0.24 relevance) | Returns Section 370.23 about Cablebus overcurrent - **not related to surge protection** |

### The Problem: Enforcement Loop + Answer Synthesis

```
┌─────────────────────────────────────────────────────────────────┐
│  AGENT ITERATION FLOW FOR cec-007                               │
├─────────────────────────────────────────────────────────────────┤
│  Iteration 1: cec_lookup_table("240.4(G)")                      │
│       → Returns PERFECT table content                           │
│                                                                 │
│  Iteration 2: Agent ready to answer                             │
│       → ENFORCEMENT: "Missing exception. Forcing search."       │
│                                                                 │
│  Iteration 3: cec_exception_search("240.4(G)")                  │
│       → Returns UNRELATED exceptions (230.90 service OCP)       │
│                                                                 │
│  Iteration 4-5: compare_with_nec, then answer                   │
│       → Agent synthesizes ALL tool outputs                      │
│       → Exception content DOMINATES final answer                │
└─────────────────────────────────────────────────────────────────┘
```

### Root Cause Analysis

**1. Mandatory Exception Search Creates Noise**

The enforcement loop at `agent.py:680-690` forces exception search on EVERY question:
```python
if not any("exception" in tc.get("tool", "") for tc in tool_calls):
    # Force exception search
```

For table content questions, this is counterproductive because:
- The question asks "What does Table X specify?" (descriptive)
- Exception search returns "What exceptions affect Table X?" (tangential)
- Low relevance scores (0.24-0.50) indicate poor matches

**2. Answer Synthesis Prioritizes Exceptions**

The system prompt emphasizes exceptions heavily:
- "MANDATORY: Every answer requires checking for exceptions"
- "Exception search → Find exceptions"
- "MORE RESTRICTIVE rule wins"

This causes the LLM to treat exception content as MORE important than table content, even when the question is about table description.

**3. Tool Output Ordering**

The agent receives tools in this order:
1. Table content (relevant)
2. NEC comparison (relevant)
3. Exception search (irrelevant for this question type)

The exception search comes LAST, and recency bias may cause the LLM to weight it more heavily in answer synthesis.

### Evidence: Actual Agent Answer vs Tool Output

**What cec_lookup_table returned:**
```
CEC 2022 Table 240.4(G) - Specific Conductor Applications
Description: Cross-reference table for overcurrent protection requirements
of specific conductor types. Lists conductor applications and directs users
to the applicable NEC articles...

Headers: Conductor | Article | Section
- Air-conditioning and refrigeration equipment circuit conductors → 440
- Capacitor circuit conductors → 460
- Control and instrumentation circuit conductors (Type ITC) → 727
- Electric welder circuit conductors → 630
- Fire alarm system circuit conductors → 760
- Motor-operated appliance circuit conductors → 422
- Motor and motor-control circuit conductors → 430
...
```

**What the agent answered:**
```
## CEC Table 240.4(G) Exceptions Analysis (CEC 2022)

### Key Exceptions Affecting Table 240.4(G):
1. **Motor Circuit Overcurrent Protection**
   - **Exception 230.90(A) No. 1**:
     *Allows motor circuits to comply with 430.52...*
2. **Service Conductor Overload Protection**
   - **Exception 230.90(A) No. 3**:
     *Permits overcurrent devices exceeding service conductor ampacity...*
...
```

The agent had the correct table content but wrote about exceptions instead.

---

## Deep Dive 2: Comparison Question (cec-026)

### What the Tools Actually Return

**cec-026: "Compare kitchen GFCI requirements. Which code is more restrictive?"**

| Tool | Content | Key Issue |
|------|---------|-----------|
| `cec_search` | 210.52(A) general receptacle spacing, 210.8 GFCI rules | Doesn't explicitly state "countertop only" |
| `compare_with_nec` | Both codes' 210.8 text side-by-side | **Both texts look nearly identical** |
| `cec_exception_search` | Full 210.8 text with exceptions | Key scope difference buried in dense text |

### The Critical Difference That's Hidden

**Expected Answer:**
> CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI.
> - CEC: Limits GFCI to receptacles serving **countertop surfaces** and within 6 feet of sink
> - NEC: Requires GFCI for **ALL kitchen receptacles**

**What the tools return:**

CEC 210.8(A)(6):
```
"...receptacles installed to serve countertop surfaces in kitchens..."
```

NEC 210.8(A)(6):
```
"...all kitchen receptacles..."  (paraphrased - the actual NEC text is similar)
```

The problem: Both return similar-looking text about "kitchen" and "GFCI". The SCOPE DISTINCTION ("countertop surfaces" vs "all") is present but not highlighted.

### Root Cause Analysis

**1. No Explicit Scope Extraction**

The `compare_with_nec` tool returns raw text, not semantic analysis:
```python
# What the tool does:
return f"""
CEC: {cec_text}
NEC: {nec_text}
"""

# What it should do for comparison questions:
return f"""
CEC Scope: countertop surfaces only
NEC Scope: all kitchen receptacles
Restrictiveness: NEC is more restrictive (broader scope)
"""
```

**2. Prompt Reasoning Not Applied Correctly**

The prompt fix added:
```
### Comparison Questions ("Which is more restrictive?")
1. Define scope for each code:
   - WHAT does it apply to? (all X, only Y, exceptions for Z)
2. Determine restrictiveness:
   - MORE RESTRICTIVE = applies to MORE things/places/situations
```

But the agent's actual reasoning:
```
### **Restrictiveness Analysis**
1. **Scope of Application**
   - Both codes apply GFCI protection to **all kitchen countertop receptacles**.

### **Conclusion**
- **Equally Restrictive:** Both CEC 2022 and NEC 2023 have **identical requirements**
```

The agent interpreted CEC's "countertop surfaces" as equivalent to NEC's kitchen requirements, missing that NEC covers MORE than just countertops.

**3. Missing Ground Truth in Tool Output**

Neither search explicitly returns:
- "NEC covers ALL kitchen receptacles, not just countertops"
- "CEC has narrower scope than NEC"

The agent has to INFER this from subtle wording differences, which it fails to do.

---

## Proposed Solutions

### Solution 1: Question-Type Detection + Answer Template

Add to system prompt:
```markdown
### Answer Format by Question Type

**"What does Table X specify?" questions:**
FIRST: Describe the table content (columns, rows, purpose)
THEN: Note any exceptions that modify its application
DO NOT lead with exceptions - the question asks about TABLE CONTENT

**"Which is more restrictive?" questions:**
FIRST: State EXPLICITLY what each code covers
  - "CEC covers: [list specific scope]"
  - "NEC covers: [list specific scope]"
THEN: Compare scopes quantitatively
  - "CEC applies to X situations, NEC applies to Y situations"
FINALLY: State conclusion with reasoning
  - "[Code] is more [restrictive/permissive] because it covers [more/fewer] situations"
```

### Solution 2: Conditional Exception Enforcement

Modify enforcement loop to skip mandatory exception search for table content questions:

```python
# In agent.py enforcement check
question_lower = question.lower()
is_table_content_question = (
    "what does table" in question_lower or
    "table" in question_lower and "specify" in question_lower
)

if is_table_content_question:
    # Skip mandatory exception search for descriptive table questions
    pass
else:
    # Normal enforcement
    if not any("exception" in tc.get("tool", "") for tc in tool_calls):
        force_exception_search()
```

### Solution 3: Enhanced compare_with_nec Output

Modify the comparison tool to output scope analysis:

```python
def compare_with_nec(section, query):
    cec_text = get_cec_section(section)
    nec_text = get_nec_section(section)

    # Add scope extraction
    cec_scope = extract_scope(cec_text)  # "countertop surfaces"
    nec_scope = extract_scope(nec_text)  # "all kitchen receptacles"

    return f"""
    ## Scope Comparison
    - CEC applies to: {cec_scope}
    - NEC applies to: {nec_scope}
    - Broader scope: {'NEC' if is_broader(nec_scope, cec_scope) else 'CEC'}

    ## Full Text Comparison
    ...
    """
```

### Solution 4: Answer Synthesis Priority Instructions

Add to system prompt:
```markdown
### Answer Synthesis Priority

When combining multiple tool outputs, prioritize by QUESTION TYPE:

| Question Type | Priority Order |
|---------------|----------------|
| "What does Table X specify?" | 1. cec_lookup_table 2. compare_with_nec 3. cec_exception_search |
| "What size/ampacity/rating?" | 1. lookup tools 2. exceptions 3. search |
| "Which is more restrictive?" | 1. compare_with_nec (scope) 2. search 3. exceptions |

DO NOT let low-relevance exception results dominate answers about table content.
```

---

## Conclusion

The prompt fixes successfully changed tool usage behavior but failed to fix answer content because:

| Issue | Root Cause | Fix Type |
|-------|------------|----------|
| Table questions answered with exceptions | Mandatory exception search + synthesis priority | Conditional enforcement + priority instructions |
| Wrong comparison conclusion | Tool output doesn't highlight scope differences | Enhanced tool output + explicit scope extraction |
| Recency bias in synthesis | Exceptions searched last, weighted heavily | Priority instructions by question type |

**Recommended Next Steps:**
1. Implement Solution 1 (answer templates by question type) - lowest code change
2. Test Solution 4 (synthesis priority) - prompt-only change
3. Consider Solution 2 (conditional enforcement) if prompt changes insufficient
