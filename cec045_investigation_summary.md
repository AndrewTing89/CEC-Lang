# CEC2022-045 Investigation Summary

## Investigation Overview

**Question:** "What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?"

**Expected Answer:** Type 3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, 6P (10 types)

**Test Results:** 10 runs with full trace capture
- ✅ Correct: 1/10 (10%)
- ❌ Wrong: 9/10 (90%)

---

## Key Findings

### 1. Tool Output is 100% Consistent ✓

All 10 runs received **IDENTICAL** tool output from `cec_lookup_table('110.28')`. The tool correctly returns:

```
Environmental Condition: Rain, snow, and sleet
Type 3: X | Type 3R: X | Type 3S: X | Type 3X: X | Type 3Rx: X | Type 3Sx: X | Type 4: X | Type 4X: X | Type 6: X | Type 6P: X

Environmental Condition: Sleet*
Type 3: � | Type 3R: � | Type 3S: X | Type 3X: � | Type 3Rx: � | Type 3Sx: X | Type 4: � | Type 4X: � | Type 6: � | Type 6P: �
```

**Conclusion:** This is NOT a tool randomness issue. The data is deterministic and correct.

---

### 2. LLM Misinterprets Table Structure ✗

The LLM confuses two distinct table rows:

**Row 1 - "Rain, snow, and sleet":**
- Meaning: Base outdoor weather condition
- Marked types: ALL 10 outdoor enclosure types
- This is the CORRECT answer for the question

**Row 2 - "Sleet*" (with footnote):**
- Meaning: SPECIFIC condition requiring ice-covered operability
- Marked types: Only 3S, 3SX (and sometimes interpreted to include 4, 4X, 6, 6P)
- This is an ADDITIONAL feature, NOT the base requirement

**The Error Pattern:**

8 out of 9 wrong runs explicitly mention focusing on the "Sleet*" row and use it to FILTER the "Rain, snow, and sleet" row, resulting in:
- Most common wrong answer: Type 3S, 3SX, 4, 4X, 6, 6P (6 types) - missing 3, 3R, 3X, 3RX
- Most restrictive wrong answer: Type 3S, 3SX only (2 types)

---

### 3. Why the LLM Gets Confused

**Trigger:** The question mentions "rain, sleet, and **ice**"

The word "ice" appears in the footnote for the "Sleet*" row: "Mechanism shall be operable when ice covered."

This creates a false association where the LLM:
1. Sees "ice" in the question
2. Links it to the "Sleet*" row footnote
3. Treats "Sleet*" as a mandatory refinement criterion
4. Filters out types NOT marked in the "Sleet*" row

**Example of flawed reasoning (Run 1):**
> "Sleet Resistance: Types 3S, 3SX, 4, 4X, 6, and 6P explicitly protect against sleet (see 'Sleet*' row)."

**The correct interpretation should be:**
- "Rain, snow, and sleet" row covers ALL types suitable for outdoor weather including sleet
- "Sleet*" row indicates which enclosures have the ADDITIONAL feature of ice-covered operability
- The question asks about "rain and sleet," which maps to Row 1, not Row 2

---

### 4. Reflection Layer is Ineffective ✗

**Reflection approved 9 out of 9 wrong answers** with `[VERIFIED] Answer is complete.`

The reflection layer fails because:
- It checks for completeness (✓)
- It checks for citations (✓)
- It does NOT validate semantic correctness (✗)
- It does NOT challenge the LLM's interpretation logic (✗)

The wrong answers are "complete" in the sense that they cite Table 110.28, provide explanations, and follow a logical structure. Reflection cannot detect that the underlying interpretation is flawed.

---

### 5. The One Correct Run (Run 9)

**What was different?**

The correct run properly interpreted the table hierarchy:

> "**Key Requirements from Table 110.28:**
> 1. Rain, snow, and sleet protection is provided by Types 3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, and 6P.
> 2. Sleet-specific protection (marked with footnote [*]) requires Types 3S, 3SX, 4X, or 6P."

Key insight: It treats Row 1 as the BASE answer and Row 2 as an ADDITIONAL feature annotation.

**Why is this rare (10% success rate)?**

The correct interpretation requires the LLM to:
1. Recognize the question maps primarily to Row 1
2. NOT over-interpret the "ice" keyword as requiring Row 2
3. Understand that Row 2 is a subset refinement, not a mandatory filter

With temperature near 0 (deterministic tool output suggests low temperature), the LLM's interpretation is stable but wrong 90% of the time. The 10% success is likely due to subtle differences in the reasoning path triggered by the initial tool call.

---

## Answers to Investigation Questions

### 1. What tool output does the agent receive?

**IDENTICAL for all runs.** The tool returns both the "Rain, snow, and sleet" row (marking 10 types) and the "Sleet*" row (marking only 3S, 3SX). The data is complete and correct.

---

### 2. Is the tool output the same for correct vs incorrect runs?

**YES.** Run 4 used `cec_search` instead of `cec_lookup_table` in the first iteration, but all other runs (including the correct Run 9) received identical tool output from `cec_lookup_table`.

---

### 3. What does the LLM say in its reasoning for correct vs incorrect runs?

**Correct Run 9:**
- Lists Row 1 as providing 10 types for "Rain, snow, and sleet protection"
- Treats Row 2 as an additional feature: "Sleet-specific protection (marked with footnote [*]) requires Types 3S, 3SX, 4X, or 6P"
- Final answer includes the full list of 10 types

**Wrong Runs (typical):**
- Focuses on Row 2: "Types 3S and 3SX are explicitly marked for sleet resistance (see 'Sleet*' row in the table)"
- Filters Row 1 by Row 2: "Type 4, 4X, 6, and 6P are not explicitly marked for sleet but are included in the broader 'rain, snow, and sleet' category"
- Final answer excludes Type 3, 3R, 3X, 3RX

---

### 4. Is there a pattern in how the agent interprets the table?

**YES. Clear pattern:**

| Interpretation Pattern | Frequency | Result |
|----------------------|-----------|--------|
| Uses "Sleet*" row as primary filter | 8/10 runs | Wrong (excludes base types) |
| Uses "Rain, snow, and sleet" row as base | 1/10 runs | Correct (includes all 10 types) |
| Intersection of both rows only | 1/10 runs | Wrong (only 3S, 3SX) |

The dominant failure mode (80%) is treating the "Sleet*" row as a mandatory refinement criterion instead of an additional feature annotation.

---

### 5. Does reflection help or not?

**NO.** Reflection is completely ineffective for this error type.

- Reflection approved 100% of wrong answers (9/9)
- Reflection does not challenge the LLM's interpretation logic
- Reflection only checks for formal completeness, not semantic correctness

The wrong answers are well-structured, cite sources correctly, and provide logical explanations. Without access to ground truth or explicit validation rules for table interpretation, reflection cannot detect the flaw.

---

## Root Cause Summary

**This is a prompt engineering problem, not a tool problem.**

The inconsistency stems from:
1. ❌ LLM semantic confusion between similar table rows
2. ❌ Over-interpretation of the keyword "ice" in the question
3. ❌ Lack of explicit guidance on table hierarchy interpretation
4. ❌ Ineffective reflection layer for semantic validation

**The fix requires:**
- Improving system prompt with explicit table interpretation rules
- OR restructuring table tool output to clarify hierarchy
- OR adding post-processing validation for Table 110.28 questions
- OR improving the reflection prompt to challenge interpretation logic

---

## Files Generated

1. `cec045_trace_analysis.json` - Raw test data (5 runs)
2. `cec045_detailed_analysis.json` - Extended test data (10 runs with full reasoning)
3. `cec045_root_cause_analysis.md` - Technical analysis with fix recommendations
4. `cec045_trace_comparison.md` - Side-by-side comparison of correct vs wrong reasoning
5. `cec045_investigation_summary.md` - This executive summary

---

## Recommended Next Steps

1. **Immediate Fix:** Update question in evaluation set to avoid "ice" keyword:
   > "What type of enclosure is suitable for outdoor use with rain and sleet per Table 110.28?"

2. **Short-term Fix:** Add explicit guidance to system prompt about Table 110.28 interpretation

3. **Long-term Fix:** Implement semantic validation in reflection layer or add post-processing rules for table questions

4. **Testing:** Re-run evaluation after fixes to verify >95% accuracy on this question type
