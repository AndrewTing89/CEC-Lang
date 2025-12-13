# CEC-051 Visual Analysis: What the LLM Sees

## The Tool Output (Actual)

When the agent calls `cec_lookup_table("220.12")`, it receives this text string:

```
CEC 2022 Table 220.12 - General Lighting Loads by Non-Dwelling Occupancy
Section: Article 220
Description: Provides unit lighting load values in volt-amperes per square meter
and per square foot for calculating general lighting loads in non-dwelling occupancies...

Headers: Type of Occupancy | Unit Load (Volt-amperes/m²) | Unit Load (Volt-amperes/ft²)

Type Of Occupancy: Office | Volt Amperes/M²: 14 | Volt Amperes/Ft²: 1.3 | Footnote: d
```

## The Ambiguity Problem

### What the LLM Should Read:
```
Office Building:
  - Metric:    14 VA/m²   ← For use with square METERS
  - Imperial:  1.3 VA/ft² ← For use with square FEET ✓
```

### What the LLM Actually Reads:
```
Office Building has values: 14 and 1.3
User asked for: "5,000 square foot office"
Which value to use? 🤔
  Option A: 14  ← Appears first, larger number
  Option B: 1.3 ← Appears second, smaller number
```

## Why the LLM Picks 14 (Wrong Choice)

### Cognitive Bias Factors:

1. **Left-to-Right Reading Bias**
   ```
   Volt Amperes/M²: 14 | Volt Amperes/Ft²: 1.3
   ↑ Seen first          ↑ Seen second
   ```

2. **Magnitude Salience**
   ```
   14   ← Larger, more "significant" number
   1.3  ← Smaller, looks like a decimal/factor
   ```

3. **Label Ambiguity**
   ```
   "Volt Amperes/M²" vs "Volt Amperes/Ft²"
   ↑ M² and Ft² look similar at a glance
   ↑ Both say "Volt Amperes/"
   ```

4. **Unit Confusion**
   ```
   User said: "5,000 square foot"
   LLM thinks: "I need a value for square feet"
   LLM sees: "Volt Amperes/M²: 14"
   LLM misreads "M²" as "per square" (wrong unit!)
   ```

## Actual LLM Reasoning (from Traces)

### Run 1 Output:
```
- Unit load for office: 14 VA/ft² (from Table 220.12)
- Total lighting load:
  5,000 ft² × 14 VA/ft² = 70,000 VA
```
**Error**: Used metric value (14 VA/m²) as if it were imperial (14 VA/ft²)

### Run 4 Output (Most Revealing):
```
For office occupancies, Table 220.12 specifies:
- 14 volt-amperes per square foot (1.3 VA/ft²)
```
**Error**: Correctly saw "1.3 VA/ft²" but STILL used "14" in calculation!
This shows the LLM:
1. Recognized both values
2. Even noted the correct one in parentheses
3. But defaulted to using "14" in the math

## Side-by-Side Comparison

| What LLM Sees | What LLM Should Interpret | What LLM Actually Does |
|---------------|---------------------------|------------------------|
| `Volt Amperes/M²: 14` | 14 VA per square METER (metric) | Uses 14 for square feet ❌ |
| `Volt Amperes/Ft²: 1.3` | 1.3 VA per square FOOT (imperial) ✓ | Ignores this value |

## The Unit Mismatch Cascade

```
Question: "5,000 square foot office"
           ↓
Tool Returns: "M²: 14 | Ft²: 1.3"
           ↓
LLM Parses: "14 and 1.3 are available"
           ↓
LLM Selects: "14" (wrong - this is for m², not ft²!)
           ↓
LLM Calculates: 5,000 ft² × 14 VA/ft² = 70,000 VA
           ↓
Reality Check: Should be 5,000 ft² × 1.3 VA/ft² = 6,500 VA
           ↓
Error Magnitude: 10.77× too high (off by factor of ~11)
```

## Why This is Hard to Detect

### The Wrong Answer Looks Plausible:

```
70,000 VA for 5,000 ft² office
= 14 watts per square foot
= Seems reasonable for office lighting
```

In reality:
- Modern office lighting: 0.5-1.5 W/ft² (LED)
- Code minimum (CEC Table 220.12): 1.3 VA/ft²
- 14 W/ft² would be: Old-school fluorescent + high-intensity task lighting
- Still within realm of "possible but excessive"

**This is why reflection doesn't catch it** - the wrong answer isn't obviously absurd.

## Visual Pattern Recognition Failure

The LLM must visually parse this structure:

```
Label 1: Value 1 | Label 2: Value 2
```

But it struggles with:
```
Volt Amperes/M²: 14 | Volt Amperes/Ft²: 1.3
^^^^^^^^^^^^^^^       ^^^^^^^^^^^^^^^^
   8 chars               8 chars
   Very similar looking!
```

The labels are **too visually similar** for reliable pattern matching.

## Proposed Fix: Enhanced Formatting

### Current (Ambiguous):
```
Type Of Occupancy: Office | Volt Amperes/M²: 14 | Volt Amperes/Ft²: 1.3
```

### Proposed (Explicit):
```
Occupancy: Office
  • METRIC (square meters):    14 VA/m²
  • IMPERIAL (square feet):    1.3 VA/ft²  ← USE THIS FOR SQUARE FEET
  • Note: User asked for "square foot" - use IMPERIAL value
```

### Alternative Fix: Structured Output
```
Office Lighting Load:
  For 5,000 square feet → Use 1.3 VA/ft²
  For 5,000 square meters → Use 14 VA/m²
  (Selected based on user question)
```

## Impact of Visual Clarity

| Formatting Style | Correct Rate | Why |
|------------------|--------------|-----|
| Current (pipe-delimited) | 0/5 (0%) | Labels too similar |
| Bulleted with labels | Estimated 80%+ | Clear visual separation |
| Question-aware selection | Estimated 95%+ | Pre-filtered, no choice needed |

## Conclusion

The root cause is a **human factors problem**:
- The tool returns correct data
- But the formatting creates visual ambiguity
- The LLM's pattern recognition fails to reliably distinguish m² vs ft²
- No safeguards prevent unit system mismatch

**Fix Priority**: CRITICAL - 100% failure rate on affected questions

---

**Test Date**: 2025-12-12
**Sample Size**: 5 runs, 0% success
**Error Type**: Systematic (not random) - always picks wrong column
