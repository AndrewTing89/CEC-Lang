# Solutions Analysis - Run 38

**Date:** 2025-12-12
**Wrong/Partial Answers Analyzed:** 2 (critical issues only)
**Overall Score:** 97.7% (518/530)

## Executive Summary

Two issues required deep investigation:

| Issue | Score | Root Cause | Fix Priority |
|-------|-------|------------|--------------|
| cec2022-023 | 7/10 | **SEARCH_FAILURE** - Agent only searched GFCI, never AFCI | **HIGH** |
| cec2022-051 | 3/10 | **INTERPRETATION + UNIT_ERROR** - Agent picked metric instead of imperial | **HIGH** |

**Key Finding for cec2022-023:** Despite adding DOMAIN KNOWLEDGE guidance, the agent **still only searched for GFCI** - the prompt guidance is NOT being followed. The agent then hallucinated non-existent AFCI exceptions.

---

## Issue Analysis

### Issue 1: cec2022-023 - AFCI Kitchen Circuits (CRITICAL)

**Score:** 7/10 (up from 5/10 in Run 37)
**Root Cause Category:** SEARCH_FAILURE + INTERPRETATION

**Investigation:**
- Tools called: `cec_search` (only 1 call)
- Search query: `"210.8 kitchen receptacles GFCI"` (GFCI only, no AFCI)
- Agent iterations: 3 (no additional tool calls after iteration 1)

**Findings:**

1. **Agent NEVER Searched for AFCI**
   - Despite DOMAIN KNOWLEDGE saying "search for ALL THREE together"
   - Only tool call: `cec_search("210.8 kitchen receptacles GFCI")`
   - No search for "AFCI", "210.12", or "arc-fault"

2. **Agent Hallucinated Non-Existent Exceptions**
   From agent's answer:
   - Dishwasher: "AFCI Not required (not listed in 210.12(A) exceptions)"
   - Disposal: "AFCI Not required"
   - Refrigerator: "AFCI Not required (CEC 210.12(A) exceptions include circuits for refrigerators, freezers, etc.)"

   **These exceptions DO NOT EXIST** in CEC 2022 Section 210.12(A).

3. **What CEC 2022 Section 210.12(A) Actually Says:**
   ```
   All 120-volt, single-phase, 15- and 20-ampere branch circuits supplying
   outlets or devices installed in dwelling unit kitchens, family rooms,
   dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms,
   recreation rooms, closets, hallways, laundry areas, or similar rooms or
   areas shall be protected by [AFCI]
   ```

   **Only exception:** Fire alarm systems (Section 760.41/760.121) - NO appliance exceptions.

4. **Why Countertop Was Correct But Others Wrong:**
   - Countertop: GFCI search returned info + agent applied AFCI from general knowledge
   - Dedicated circuits: Agent assumed (incorrectly) these have exceptions without verifying

5. **DOMAIN KNOWLEDGE Not Being Enforced:**
   The prompt guidance exists but there's no enforcement. The specialized tool enforcement in `agent.py` line 664 was disabled:
   ```python
   # Specialized tool enforcement removed in favor of smart table injection
   ```

**Evidence:**
```python
# From evaluation results - tool calls trace
Iteration 1: cec_search("210.8 kitchen receptacles GFCI")  # Only GFCI!
Iteration 2: No tools called
Iteration 3: No tools called (answer generated)
```

**Proposed Fix:**

**Option A: Add Protection Type Coverage Enforcement (core/agent.py)**

```python
def _check_protection_type_coverage(self, question: str, all_tool_calls: list) -> tuple:
    """Verify all protection types mentioned in question were searched."""
    q_lower = question.lower()

    # Detect if this is a dwelling unit circuit protection question
    dwelling_keywords = ['kitchen', 'bedroom', 'dwelling', 'residential', 'living']
    protection_keywords = ['gfci', 'afci', 'cafci', 'protection required', 'breaker']

    is_dwelling_protection = (
        any(kw in q_lower for kw in dwelling_keywords) and
        any(kw in q_lower for kw in protection_keywords)
    )

    if not is_dwelling_protection:
        return (True, None)

    # For dwelling circuit protection questions, BOTH GFCI and AFCI must be searched
    search_queries = []
    for tc in all_tool_calls:
        if 'search' in tc.get('tool', '').lower():
            search_queries.append(str(tc.get('input', {})).lower())

    gfci_searched = any('gfci' in q or '210.8' in q for q in search_queries)
    afci_searched = any('afci' in q or '210.12' in q for q in search_queries)

    if gfci_searched and not afci_searched:
        return (False, "missing_search:afci")
    if afci_searched and not gfci_searched:
        return (False, "missing_search:gfci")

    return (True, None)
```

**Option B: Strengthen DOMAIN KNOWLEDGE Prompt**

Make the guidance more explicit:
```markdown
### Circuit Protection (DWELLING UNITS)
**MANDATORY FOR ALL DWELLING CIRCUIT PROTECTION QUESTIONS:**
1. Search for GFCI requirements (Section 210.8)
2. Search for AFCI requirements (Section 210.12)
3. Search for CAFCI if mentioned

**CEC 2022 Section 210.12(A) REQUIRES AFCI for ALL 120V dwelling circuits:**
- Kitchens, bedrooms, living rooms, hallways, closets, laundry, etc.
- NO exceptions for refrigerators, dishwashers, or other appliances
- The ONLY exception is fire alarm systems (760.41/760.121)

If you cannot find an explicit exception in search results, AFCI IS REQUIRED.
```

**Generalization:** This fix prevents hallucination of exceptions for any code section where the agent doesn't actually verify the exception exists.

---

### Issue 2: cec2022-051 - Office Lighting Load Unit Error

**Score:** 3/10
**Root Cause Category:** INTERPRETATION + UNIT_ERROR

**Investigation:**
- Tools called: `cec_lookup_table` (Table 220.12)
- Data checked: `data/CEC_2022/cec_tables_unified.json` - Table 220.12

**Findings:**

1. **Data Is Correct**
   Table 220.12 in JSON correctly has BOTH units:
   ```json
   {
     "type_of_occupancy": "Office",
     "volt_amperes_per_m2": 14,
     "volt_amperes_per_ft2": 1.3,
     "footnote": "d"
   }
   ```

2. **Tool Output Shows Both Values**
   The `cec_lookup_table` function outputs:
   ```
   Type Of Occupancy: Office | Volt Amperes/M²: 14 | Volt Amperes/Ft²: 1.3 | Footnote: d
   ```

3. **Agent Picked Wrong Column**
   - Question asks for "5,000 square foot" → should use VA/ft² (1.3)
   - Agent used 14 (the VA/m² value) but labeled it as "VA/sq ft"
   - Result: 70,000 VA instead of 6,500 VA (off by 10x)

4. **Why This Happened:**
   - Both values appear in same row
   - Metric value (14) appears before imperial (1.3)
   - Agent may have "first value bias"
   - Column names not distinct enough when parsed

**Evidence:**
```json
// From cec_tables_unified.json
"Table 220.12": {
  "rows": [
    {
      "type_of_occupancy": "Office",
      "volt_amperes_per_m2": 14,
      "volt_amperes_per_ft2": 1.3
    }
  ]
}
```

Agent's wrong output:
```
Unit load for office: 14 VA/sq ft (from CEC Table 220.12)
5,000 × 14 = 70,000 VA
```

**Proposed Fix:**

**Option A: Enhanced Tool Output Formatting (core/tools.py)**

Modify `cec_lookup_table` to format dual-unit tables more clearly:

```python
# In cec_lookup_table, around line 730, add special handling for dual-unit tables
def format_dual_unit_row(row: dict) -> str:
    """Format rows that have both metric and imperial units."""
    output_lines = []

    # Check for dual-unit columns
    has_dual_units = ('volt_amperes_per_m2' in row and 'volt_amperes_per_ft2' in row)

    if has_dual_units:
        occupancy = row.get('type_of_occupancy', 'Unknown')
        output_lines.append(f"\n{occupancy}:")
        output_lines.append(f"  • FOR METRIC (m²): {row['volt_amperes_per_m2']} VA/m²")
        output_lines.append(f"  • FOR IMPERIAL (sq ft): {row['volt_amperes_per_ft2']} VA/ft²")
        if row.get('footnote'):
            output_lines.append(f"  • Footnote: {row['footnote']}")
        return '\n'.join(output_lines)
    else:
        # Return None to use default formatting
        return None
```

**Option B: Add DOMAIN KNOWLEDGE About Unit Selection**

```markdown
### Table Dual Units (220.12, etc.)
Some tables have BOTH metric (VA/m²) and imperial (VA/ft²) values.
- When question mentions "square foot" or "sq ft" → use VA/ft² column
- When question mentions "square meter" or "m²" → use VA/m² column
- ALWAYS verify the unit in your answer matches the unit in the question
```

**Generalization:** This fix helps ALL tables that have dual metric/imperial units, not just Table 220.12.

---

## Summary of Fixes

| Issue | Category | File(s) | Fix Type | Priority |
|-------|----------|---------|----------|----------|
| cec2022-023 | SEARCH_FAILURE | `core/agent.py` | Enforcement Code OR Prompt | **HIGH** |
| cec2022-051 | UNIT_ERROR | `core/tools.py` OR `core/agent.py` | Output Formatting OR Prompt | **HIGH** |

---

## Implementation Order

1. **cec2022-023 - AFCI Enforcement (HIGH PRIORITY)**
   - Why first: Safety-critical error - agent confidently states incorrect exceptions
   - Impact: All dwelling circuit protection questions
   - Recommendation: Add enforcement code to force AFCI search when GFCI is searched in dwelling context

2. **cec2022-051 - Dual Unit Handling**
   - Why second: Wrong by factor of 10x - significant calculation error
   - Impact: All tables with dual units (Table 220.12 at minimum)
   - Recommendation: Enhanced tool output formatting to clearly distinguish units

---

## Key Takeaways

1. **DOMAIN KNOWLEDGE is not enough** - The agent ignores prompt guidance when not enforced
2. **Agent hallucinates exceptions** - When it doesn't search, it invents plausible-sounding exceptions
3. **Dual-unit tables need special handling** - First-value bias causes unit confusion
4. **Countertop fix was accidental** - Agent got it right for wrong reasons (general knowledge, not search)

---

## Recommended Approach

For cec2022-023, I recommend **Option A (Enforcement Code)** because:
- Prompt guidance alone proved insufficient (agent ignored it)
- Code enforcement guarantees the behavior
- Can provide specific feedback to agent when AFCI search is missing

For cec2022-051, I recommend **Option A (Output Formatting)** because:
- Makes the unit distinction visually obvious
- Works at the tool level so agent can't miss it
- Generalizes to any dual-unit table
