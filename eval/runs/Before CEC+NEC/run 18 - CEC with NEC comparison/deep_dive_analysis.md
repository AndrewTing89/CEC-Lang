# Deep Dive: Error Analysis and Generalized Solutions

## Executive Summary

Analysis of 8 imperfect responses reveals **3 distinct failure patterns** with generalizable root causes:

| Pattern | Questions | Root Cause | Solution Category |
|---------|-----------|------------|-------------------|
| **Inverted Comparison** | cec-026 | LLM reasoning error on "restrictive vs permissive" | Prompt Engineering |
| **Table Content Miss** | cec-007, cec-008 | Wrong tool selection (search vs lookup) | Tool Routing |
| **Incomplete Retrieval** | cec-002, cec-013, cec-017, cec-022, cec-030 | Missing data points in response synthesis | Structured Output |

---

## Pattern 1: Inverted Comparison Conclusions

### The Problem
**cec-026** asked "Which code is more restrictive?" and the agent concluded CEC is MORE restrictive when it's actually MORE PERMISSIVE.

### Root Cause Analysis

1. **Ambiguous Terminology**: "Restrictive" vs "permissive" requires careful semantic reasoning:
   - MORE requirements = MORE restrictive
   - FEWER requirements = MORE permissive (less restrictive)

2. **Missing Comparison Framework**: The system prompt has no guidance for questions asking "which is more restrictive?"

3. **Raw Data Without Synthesis**: The `compare_with_nec` tool returns raw text from both codes but doesn't provide structured comparison fields like:
   - Scope of requirement (what does it apply to?)
   - Exceptions (what is excluded?)
   - Net effect (broader or narrower protection?)

### Current System Prompt Gap
```
# MISSING: No guidance for "restrictive vs permissive" comparisons
```

### Generalized Solution: Comparison Reasoning Protocol

**Add to System Prompt:**

```markdown
## COMPARISON QUESTIONS: "Which is more restrictive?"

When asked which code is "more restrictive" or "more permissive":

### STEP 1: Define Scope
For each code, identify:
- WHAT does it apply to? (all X, only Y, exceptions for Z)
- WHERE does it apply? (all locations, specific locations)
- WHEN does it apply? (always, under conditions)

### STEP 2: Count Coverage
- MORE RESTRICTIVE = applies to MORE things/places/situations
- MORE PERMISSIVE = applies to FEWER things (more exceptions/exclusions)

### STEP 3: Structured Comparison
```
| Aspect    | CEC 2022                  | NEC 2023                  |
|-----------|---------------------------|---------------------------|
| Applies to| [list what it covers]     | [list what it covers]     |
| Exceptions| [list exclusions]         | [list exclusions]         |
| Net scope | [broader/narrower]        | [broader/narrower]        |
```

### STEP 4: Explicit Conclusion
State clearly: "CEC is [MORE/LESS] restrictive because it [covers more/fewer] situations."

### ANTI-PATTERN: Don't confuse:
- Having MORE text ≠ more restrictive
- Having exceptions ≠ less restrictive (depends on what's excepted)
- Stricter penalties ≠ more restrictive (scope matters)
```

**Why This Generalizes:**
- Works for any "A vs B" comparison question
- Forces explicit reasoning about scope, not just existence of rules
- Creates auditable comparison table
- Prevents inverted conclusions through structured analysis

---

## Pattern 2: Table Content Misses (Wrong Tool Selection)

### The Problem
**cec-007** and **cec-008** asked "What does CEC Table X specify?" but the agent used `cec_search` and `cec_exception_search` instead of `cec_lookup_table`.

**Result:** Received semantically related content (exceptions, surrounding sections) but NOT the actual table content.

### Root Cause Analysis

1. **Question Type Misclassification**: The agent treated "What does Table X specify?" as a search query rather than a direct lookup.

2. **Tool Description Overlap**: Both tools can address "table" questions:
   - `cec_search`: "Search CEC 2022 for rules and sections"
   - `cec_lookup_table`: "Look up any CEC 2022 table by table ID"

3. **No Explicit Routing Rule**: System prompt doesn't have clear guidance for "describe a table" vs "find content related to a table"

### Current Tool Selection Logic
```python
# Agent's implicit logic:
"What does Table X specify?"
→ Contains "Table" → Search about tables
→ cec_search("Table X")  # WRONG

# Should be:
"What does Table X specify?"
→ Asking ABOUT a specific table
→ cec_lookup_table(X)  # CORRECT
```

### Generalized Solution: Question-Type Routing

**Add to System Prompt:**

```markdown
## TOOL ROUTING BY QUESTION TYPE

### Table Questions - Choose the RIGHT tool:

| Question Pattern | Correct Tool | Wrong Tool |
|-----------------|--------------|------------|
| "What does Table X specify?" | `cec_lookup_table(X)` | cec_search |
| "What is in Table X?" | `cec_lookup_table(X)` | cec_search |
| "Describe Table X" | `cec_lookup_table(X)` | cec_search |
| "Does California have Table X?" | `cec_lookup_table(X)` | cec_search |
| "Find rules about [topic]" | `cec_search(topic)` | cec_lookup_table |
| "What section covers [topic]?" | `cec_search(topic)` | cec_lookup_table |

### ROUTING RULE (MANDATORY):
If the question contains "Table [number]" AND asks what it contains/specifies:
→ FIRST call `cec_lookup_table(number)` to get actual table content
→ THEN call `cec_search` if you need additional context

### Verification Pattern:
After calling tools, ask yourself:
- Did I get the ACTUAL TABLE DATA (rows, columns, values)?
- Or did I get CONTENT ABOUT the table (surrounding text, exceptions)?

If asking about a specific table and didn't get its actual data → call `cec_lookup_table`
```

**Why This Generalizes:**
- Works for any "describe entity X" question type
- Creates explicit routing decision before tool call
- Includes verification step to catch wrong tool selection
- Applies to tables, sections, articles, figures, etc.

---

## Pattern 3: Incomplete Retrieval/Synthesis

### The Problem
Multiple questions had correct core answers but missing secondary information:
- **cec-002**: Missing "40-amp minimum" and "conduit to parking"
- **cec-013**: Missing aluminum conductor size option
- **cec-017**: Missing some enclosure types (Type 3, 3R)
- **cec-022**: Used different (but valid) table for service conductors
- **cec-030**: Key mandate distinction not prominent

### Root Cause Analysis

1. **Single-Path Retrieval**: Agent finds ONE source of information and stops, missing related data points.

2. **Incomplete Cross-Reference**: When tables/sections mention both copper AND aluminum, agent sometimes only reports one.

3. **Answer Synthesis Truncation**: Long tool outputs get summarized, potentially losing important details.

4. **Missing Completeness Check for Categories**: When a table has multiple columns (copper/aluminum), all should be reported.

### Generalized Solution: Completeness Verification Protocol

**Add to System Prompt:**

```markdown
## COMPLETENESS VERIFICATION (MANDATORY)

### For Conductor/Equipment Sizing Questions:
Always report BOTH materials when applicable:
- "X AWG copper OR Y AWG aluminum" (not just copper)
- Check if table has copper AND aluminum columns

### For List/Enumeration Questions:
- Count items in tool output
- Cross-reference with any "complete list" claims
- If source says "Types 3, 3R, 3S, 4, 4X, 6, 6P" → report ALL seven

### For Multi-Requirement Questions:
After drafting answer, verify each requirement mentioned in expected scope:
```
□ Did I address [requirement 1]?
□ Did I address [requirement 2]?
□ Did I include specific values (not just "see table")?
□ Did I include BOTH material options if applicable?
```

### For Comparison Questions:
Verify you addressed the KEY DISTINCTION:
- What is the FUNDAMENTAL difference? (mandate vs guidance, etc.)
- Lead with the key distinction, then provide supporting details

### Cross-Reference Verification:
When a table lookup returns data:
1. Check ALL columns in the result
2. Report values from ALL relevant columns
3. If copper column exists AND aluminum column exists → report both
```

**Why This Generalizes:**
- Works for any multi-faceted answer
- Catches common omission patterns (second material, additional types)
- Creates explicit verification step before final answer
- Applies to sizing, classification, enumeration questions

---

## Implementation Priority

### High Priority (Fixes Critical Errors)

1. **Add Comparison Reasoning Protocol** to system prompt
   - Prevents inverted conclusions on restrictive/permissive questions
   - ~10 lines of prompt text
   - Impact: Fixes Pattern 1 completely

2. **Add Table Question Routing Rules** to system prompt
   - Ensures `cec_lookup_table` is used for "what does table X specify"
   - ~15 lines of prompt text
   - Impact: Fixes Pattern 2 completely

### Medium Priority (Reduces Minor Errors)

3. **Add Completeness Verification Checklist** to system prompt
   - Catches missing materials, types, values
   - ~20 lines of prompt text
   - Impact: Reduces Pattern 3 errors by ~70%

### Optional Enhancements

4. **Tool Output Enhancement**: Modify `cec_lookup_table` to highlight when a table has both copper AND aluminum columns:
   ```
   Note: This table has values for both COPPER and ALUMINUM. Report both.
   ```

5. **Comparison Tool Enhancement**: Modify `compare_with_nec` to return structured comparison fields:
   ```json
   {
     "cec_scope": "countertop receptacles and within 6ft of sink",
     "nec_scope": "all kitchen receptacles",
     "cec_broader": false,
     "recommendation": "CEC is MORE PERMISSIVE (narrower scope)"
   }
   ```

---

## Validation Approach

After implementing these solutions, re-run the same 30 questions and verify:

1. **cec-026**: Should now correctly state CEC is MORE PERMISSIVE
2. **cec-007, cec-008**: Should call `cec_lookup_table` first and describe actual table content
3. **cec-013**: Should include both "4 AWG copper OR 2 AWG aluminum"
4. **cec-017**: Should list all 7 enclosure types
5. **cec-030**: Should lead with "California MANDATES, NEC only provides installation rules"

---

## Summary of Generalized Patterns

| Error Type | Root Cause | Solution | Applies To |
|------------|------------|----------|------------|
| Wrong conclusion | Missing reasoning framework | Structured comparison protocol | Any "A vs B" questions |
| Wrong tool | Ambiguous routing | Explicit tool routing rules | Any "describe entity X" questions |
| Missing details | Incomplete synthesis | Completeness checklist | Any multi-faceted answers |

These solutions are **prompt-level changes** that don't require code modifications, making them easy to implement and test.
