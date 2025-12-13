# CEC-051 Root Cause Analysis: Office Lighting Load Inconsistency

## Problem Summary

**Question**: "Calculate the general lighting load for a 5,000 square foot office building."

**Expected Answer**: 5,000 × 1.3 VA/ft² = 6,500 VA
**Wrong Answer** (5/5 runs): 5,000 × 14 VA/ft² = 70,000 VA

**Error Rate**: 100% incorrect (5 out of 5 test runs failed)

## Root Cause: Ambiguous Column Formatting in Table Output

### What the Tool Returns

When the agent calls `cec_lookup_table("220.12")`, the tool returns this formatted text:

```
Type Of Occupancy: Office | Volt Amperes/M²: 14 | Volt Amperes/Ft²: 1.3 | Footnote: d
```

### The Underlying Data (Correct)

The JSON data structure is correct:
```json
{
  "type_of_occupancy": "Office",
  "volt_amperes_per_m2": 14,    // ← This is VA per SQUARE METER
  "volt_amperes_per_ft2": 1.3,  // ← This is VA per SQUARE FOOT
  "footnote": "d"
}
```

### The Formatting Bug (Source of Confusion)

The tool formatting code (`core/tools.py` lines 748-751) converts field names like this:

```python
key_formatted = key.replace('_', ' ').replace('m2', 'm²').replace('ft2', 'ft²')
key_formatted = key_formatted.replace(' per ', '/').title()
```

This produces:
- `volt_amperes_per_m2` → `Volt Amperes/M²`
- `volt_amperes_per_ft2` → `Volt Amperes/Ft²`

**The problem**: The LLM interprets this ambiguously:
- It sees **two numbers next to each other**: `14` and `1.3`
- The column headers don't clearly indicate which unit system to use
- The LLM sometimes interprets "14" as the value for square feet (wrong!)

## Why This Happens

### Observed Agent Behavior (5 Test Runs)

From the console output of the investigation:

**Run 1**: Used 14 VA/ft² → 70,000 VA ❌
**Run 2**: Used 14 VA/ft² → 70,000 VA ❌
**Run 3**: Used 14 VA/ft² → 70,000 VA ❌
**Run 4**: Used 14 VA/ft² → 70,000 VA ❌ (also mentioned 1.3 in text but calculated with 14)
**Run 5**: Used 14 VA/ft² → 70,000 VA ❌

### Why the LLM Picks the Wrong Value

1. **Visual Proximity**: The number "14" appears first in the output
2. **Metric Blindness**: The LLM doesn't always distinguish m² vs ft² carefully
3. **No Unit Enforcement**: The tool doesn't validate that the user asked for imperial units
4. **Column Order**: Metric (m²) column appears before imperial (ft²) column

### Example of LLM Reasoning (from Run 4)

```
For office occupancy:
- 14 volt-amperes per square foot (Table 220.12)
- Note in parentheses: (1.3 VA/ft²)
```

The agent saw BOTH values but chose to use "14" in the calculation!

## Why Reflection Doesn't Catch It

From the traces:
- **Reflection used**: Yes (all 5 runs)
- **Reflection approved**: Yes (all 5 runs)
- **Why it failed**: Reflection sees the same ambiguous tool output and agrees with the wrong interpretation

The reflection step checks "Does this answer make sense?" but it doesn't re-validate the units. Since 70,000 VA is a plausible (if very high) lighting load, reflection approves it.

## Proof: Tool Output Inspection

Running `test_table_output.py` confirms the exact formatting:

```
Headers: Type of Occupancy | Unit Load (Volt-amperes/m²) | Unit Load (Volt-amperes/ft²)

Type Of Occupancy: Office | Volt Amperes/M²: 14 | Volt Amperes/Ft²: 1.3 | Footnote: d
```

**The headers are correct** (they show m² and ft²), but the **LLM doesn't reliably match the header labels to the row values**.

## Contributing Factors

1. **No Unit Context**: The tool doesn't know the user asked for "square foot" calculation
2. **No Validation**: No check that returned value matches expected unit system
3. **Ambiguous Parsing**: The LLM must parse a pipe-delimited string instead of structured JSON
4. **Large Number Bias**: "14" looks more significant than "1.3", biasing selection
5. **Metric-First Ordering**: The metric value appears first (left-to-right reading bias)

## Comparison with Other Tables

This bug is **unique to Table 220.12** because:
- It's the only table with BOTH metric and imperial columns side-by-side
- Other tables (310.16, 250.122) only show imperial values or have clearly separated sections
- The 10x magnitude difference (14 vs 1.3) makes errors catastrophic

## Impact Assessment

**Severity**: CRITICAL
**Frequency**: 100% error rate on this question type
**Scope**: Any question involving Table 220.12 lighting loads
**Affected Questions**: cec-051, and any variants asking for lighting loads

## Recommended Fixes

### Option 1: Improve Column Header Clarity (Quick Fix)

Change the formatting to make units explicit:

```python
# Before:
Type Of Occupancy: Office | Volt Amperes/M²: 14 | Volt Amperes/Ft²: 1.3

# After:
Type Of Occupancy: Office | Volt-Amperes per SQUARE METER: 14 VA/m² | Volt-Amperes per SQUARE FOOT: 1.3 VA/ft²
```

### Option 2: Add Unit Context to Tool (Better Fix)

Modify `cec_lookup_table()` to:
1. Detect when user question mentions "square feet" vs "square meter"
2. Highlight the matching column in the output
3. Add a warning note about unit system

### Option 3: Create Specialized Tool (Best Fix)

Create `cec_lookup_lighting_load(occupancy_type: str, unit_system: str)`:
- Automatically selects correct column based on `unit_system` parameter
- Returns single value (no ambiguity)
- Forces agent to specify imperial vs metric upfront

### Option 4: Post-Processing Validation

Add a validation layer that:
- Checks if user mentioned "square feet" in question
- Verifies the final answer used the imperial column
- Raises error if agent picked wrong unit system

## Test to Verify Fix

After implementing fix, re-run:
```python
question = "Calculate the general lighting load for a 5,000 square foot office building."
# Expected: 5,000 × 1.3 = 6,500 VA
# Should get 5/5 correct after fix
```

## Related Issues

This may also affect:
- Other Table 220.12 occupancy types (retail, hospital, etc.)
- Any calculation where imperial vs metric distinction matters
- Questions that don't specify unit system (agent must infer from context)

---

**Date**: 2025-12-12
**Investigator**: Claude Code
**Test Runs**: 5 iterations, 0% success rate
**Status**: ROOT CAUSE IDENTIFIED - Awaiting fix implementation
