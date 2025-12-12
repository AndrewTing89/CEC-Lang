# CEC Lang Agent - Improvement Recommendations

Based on deep analysis of 14 questions with less-than-perfect scores, we've identified 5 root cause categories and propose generic, non-hard-coded solutions.

---

## Root Cause Categories

### 1. Table Lookup Logic Errors (CRITICAL)
**Examples:** core-010, cec-020, inspection-010
**Impact:** Can cause FAIL scores (5/10 or below)

### 2. Incomplete Enumeration
**Examples:** baseline-003, core-003, core-005, cec-017
**Impact:** Partial credit (8/10)

### 3. Methodology Differences (Not always wrong)
**Examples:** inspection-001, cec-022
**Impact:** Different but valid interpretations

### 4. Missing "Big Picture" Context
**Examples:** cec-007, cec-028, cec-030
**Impact:** Technically correct but misses policy implications

### 5. Exception Misapplication
**Examples:** inspection-005
**Impact:** Wrong conclusions from invented exceptions

---

## Proposed Generic Solutions

### Solution 1: Conductor Ampacity Decision Tree

**Problem:** Agent confuses insulation rating column with termination temperature column

**Implementation:** Add explicit reasoning chain to system prompt or tool:

```python
# Add to knowledge_tools.py or as part of table_lookup tool

AMPACITY_REASONING_PROMPT = """
When calculating conductor ampacity with temperature correction:

1. IDENTIFY the conductor insulation type (THHN, TW, THWN, etc.)
2. LOOKUP the insulation temperature rating:
   - THHN/THWN-2: 90°C
   - TW: 60°C
   - THW/THWN: 75°C
3. SELECT Table 310.16 column matching INSULATION rating (not termination)
4. APPLY temperature correction factor from Table 310.15(B)(1)
   using the SAME temperature column as the base ampacity
5. APPLY bundling adjustment from Table 310.15(C)(1)
6. VERIFY final ampacity doesn't exceed termination rating limits

CRITICAL: Start with the insulation column, then derate.
Do NOT start with 75°C just because terminations are 75°C rated.
```

**Why this works:**
- Forces explicit reasoning about column selection
- Prevents the common termination vs insulation confusion
- No hard-coded values - just a decision process

---

### Solution 2: Exhaustive Enumeration Pattern

**Problem:** Agent finds "enough" answers and stops looking

**Implementation:** Modify the agent's search behavior for list-type questions:

```python
# Add to agent system prompt for enumeration questions

ENUMERATION_PROMPT = """
When a question asks "where is X required" or "list all locations/types":

1. SEARCH for the primary code section
2. READ the ENTIRE section, not just the first match
3. COUNT the items: "Section 210.8(A) lists 11 locations..."
4. ENUMERATE each item explicitly: (1), (2), (3)...
5. CROSS-REFERENCE related sections:
   - For GFCI: Also check 210.8(B), 210.8(D), 422.5
   - For panels: Also check 240.24, 408.x
   - For enclosures: Check the full table, all rows
6. VERIFY completeness: "I found X items total"
```

**Alternative Implementation:** Create a `list_all_items` tool that:
- Takes a code section reference
- Returns ALL enumerated items (not just top matches)
- Forces agent to work through the complete list

---

### Solution 3: Table Lookup Verification Tool

**Problem:** Agent misreads table values or hallucinates them

**Implementation:** Enhance table_lookup tool with verification:

```python
def table_lookup_with_verification(table_ref: str, row_key: str, column_key: str) -> dict:
    """
    Returns:
    {
        "table": "310.16",
        "row": "12 AWG",
        "column": "90°C",
        "value": "30A",
        "adjacent_values": {  # For sanity check
            "above": "10 AWG → 40A",
            "below": "14 AWG → 25A",
            "left": "75°C → 25A",
            "right": "—"
        },
        "footnotes": ["See 240.4(D) for OCP limits"]
    }
    """
```

**Verification prompt:**
```
Before using this table value, verify:
- Is 30A between the adjacent row values (25A for 14 AWG, 40A for 10 AWG)? YES
- Does this match your understanding of conductor sizing progression? YES
- Are there any footnotes that modify this value?
```

---

### Solution 4: Policy vs Technical Distinction

**Problem:** Agent answers "how to do X" when asked "why does CA require X"

**Implementation:** Add context-detection to system prompt:

```python
COMPARISON_PROMPT = """
When comparing CEC to NEC or asked about California-specific requirements:

FIRST determine the question type:
A) "What are the technical differences?" → Detail installation rules
B) "Why does CA have different rules?" → Explain policy/mandate reasons
C) "What makes this CA-specific?" → Highlight what NEC lacks

For Type B/C questions, ALWAYS address:
1. Does California MANDATE this? (Title 24, CALGreen)
2. Does NEC only provide installation rules (if you choose to install)?
3. What is the POLICY goal? (decarbonization, safety, etc.)

Lead with policy differences, then detail technical differences.
```

**Alternative:** Add metadata to questions to flag "policy comparison" vs "technical comparison"

---

### Solution 5: Exception Verification Loop

**Problem:** Agent claims exceptions exist without verifying text

**Implementation:** Add exception verification chain:

```python
EXCEPTION_VERIFICATION_PROMPT = """
Before claiming an exception applies:

1. QUOTE the exact exception text from the code
2. LIST each condition in the exception
3. VERIFY each condition is met:
   - Condition 1: [text] → Met? YES/NO because [reason]
   - Condition 2: [text] → Met? YES/NO because [reason]
4. If ANY condition is not met, the exception does NOT apply
5. If you cannot find the exception text, state:
   "I could not verify this exception exists. Applying base rule."

NEVER claim an exception based on memory or summary.
Always verify with actual code text.
"""
```

**Tool enhancement:** Add an `exception_lookup(base_rule)` tool that:
- Returns ALL exceptions for a given rule
- Includes the exact exception text
- Prevents hallucinated exceptions

---

## Implementation Priority

### HIGH Priority (Causes FAILs)
1. **Conductor Ampacity Decision Tree** - Prevents core-010 type errors
2. **Table Lookup Verification** - Prevents cec-020 type errors
3. **Exception Verification Loop** - Prevents inspection-005 type errors

### MEDIUM Priority (Improves Scores)
4. **Exhaustive Enumeration Pattern** - Improves completeness
5. **Policy vs Technical Distinction** - Better comparison answers

---

## No Hard-Coding Required

All solutions are:
- **Process-based:** They define HOW to reason, not WHAT the answer is
- **Generic:** Apply to any table lookup, any enumeration, any exception
- **Prompt-driven:** Can be implemented via system prompt modifications
- **Tool-enhanced:** Can be supported by smarter tool design

The goal is to make the agent's reasoning more systematic and verifiable,
not to pre-program specific answers.

---

## Estimated Impact

| Solution | Questions Fixed | Estimated Score Gain |
|----------|-----------------|---------------------|
| Ampacity Decision Tree | core-010, cec-021 | +5 points |
| Table Verification | cec-020, inspection-010 | +8 points |
| Exception Verification | inspection-005 | +3 points |
| Exhaustive Enumeration | 4 questions | +8 points |
| Policy Distinction | 3 questions | +6 points |
| **Total** | **12 questions** | **+30 points** |

This would improve average score from 9.1/10 to approximately 9.6/10.
