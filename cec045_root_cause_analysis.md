# Root Cause Analysis: CEC2022-045 Inconsistency

## Question
"What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?"

## Expected Answer
Full list of 10 enclosure types: Type 3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, 6P

## Test Results
- **Total runs**: 10
- **Correct**: 1/10 (10%)
- **Wrong**: 9/10 (90%)
- **Accuracy**: 10% (unacceptably low)

---

## Key Finding: Tool Output is Consistent

**All runs received IDENTICAL tool output** from `cec_lookup_table`. This proves the inconsistency is NOT caused by tool variability.

### Exact Tool Output Shows Both Rows:

**Row 1 - "Rain, snow, and sleet":**
```
Rain, snow, and sleet | Type 3: X | Type 3R: X | Type 3S: X | Type 3X: X | Type 3Rx: X | Type 3Sx: X | Type 4: X | Type 4X: X | Type 6: X | Type 6P: X
```

**Row 2 - "Sleet*" (with footnote):**
```
Sleet* | Type 3: � | Type 3R: � | Type 3S: X | Type 3X: � | Type 3Rx: � | Type 3Sx: X | Type 4: � | Type 4X: � | Type 6: � | Type 6P: �
```

---

## Root Cause: LLM Misinterpretation of Table Structure

The LLM is **confusing two distinct environmental conditions** in Table 110.28:

1. **"Rain, snow, and sleet"** - A general outdoor weather condition protected by ALL outdoor enclosures
2. **"Sleet*"** - A SPECIFIC condition requiring ice-covered operability (footnote: "Mechanism shall be operable when ice covered")

### The Misinterpretation Pattern

The LLM incorrectly treats the question about "rain, sleet, and ice" as requiring BOTH conditions simultaneously:
- ✓ "Rain, snow, and sleet" protection (Row 1) → All types (3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, 6P)
- ✗ "Sleet*" with ice-covered operability (Row 2) → Only types (3S, 3SX)

Then it takes the **intersection** of these two rows, giving only the types marked "X" in BOTH rows, which yields a partial answer.

### Evidence from Wrong Runs

**8 out of 9 wrong runs** explicitly mention focusing on the "Sleet*" row:

**Run 1 reasoning:**
> "Sleet Resistance: Types 3S, 3SX, 4, 4X, 6, and 6P explicitly protect against sleet (see "Sleet*" row)."

**Run 2 reasoning:**
> "**Type 3S** and **3SX** are explicitly marked for sleet resistance (see "Sleet*" row in the table).
> **Type 4**, **4X**, **6**, and **6P** are not explicitly marked for sleet but are included in the broader "rain, snow, and sleet" category."

The LLM sees BOTH rows but incorrectly prioritizes the "Sleet*" row as a stricter requirement, filtering out Type 3, 3R, 3X, 3RX from the answer.

---

## Why the Correct Answer is Rare (1/10 Success)

### The One Correct Run (Run 9)

The correct run properly interpreted the table hierarchy:

> "**Key Requirements from Table 110.28:**
> 1. **Rain, snow, and sleet protection** is provided by Types 3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, and 6P.
> 2. **Sleet-specific protection** (marked with footnote [*]) requires Types **3S**, **3SX**, **4X**, or **6P**.
> 3. **Ice-covered operability** is explicitly required (footnote [*]) for all outdoor enclosures."

**Key insight**: The correct interpretation treats the "Sleet*" row as an ADDITIONAL feature for SOME enclosures, not a mandatory filter for the base question about "rain, sleet."

---

## Why Reflection Fails to Catch This Error

**Reflection approved 9/9 wrong answers** with `[VERIFIED] Answer is complete.`

The reflection layer cannot catch this error because:

1. **The answer is internally consistent** - The LLM's logic is valid IF you accept its interpretation that "sleet" in the question maps to the "Sleet*" row
2. **The reflection prompt doesn't challenge interpretation** - It only checks for completeness and citation, not semantic correctness
3. **No ground truth comparison** - Reflection doesn't have access to the expected answer to verify against

---

## Analysis of LLM Confusion

### Why is the LLM confused?

1. **Ambiguous question wording**: The question asks about "rain, sleet, and ice"
   - Row 1 says: "Rain, snow, and sleet"
   - Row 2 says: "Sleet*" (with ice-covered operability footnote)

2. **The word "ice" triggers the footnote**: The question mentions "ice", which appears in the footnote for "Sleet*" row, creating a false association

3. **LLM tries to be "precise"**: The LLM sees "Sleet*" as more specific than "Rain, snow, and sleet" and incorrectly treats it as a refinement criterion

### The Correct Interpretation

Per the NEC/CEC table structure:
- **"Rain, snow, and sleet"** is the base outdoor weather condition
- **"Sleet*"** refers to a SPECIFIC use case where the mechanism must remain operable while covered in ice (e.g., outdoor disconnect switches in freezing climates)

For a general question about "rain, sleet, and ice," the answer should be ALL enclosures marked "X" in the "Rain, snow, and sleet" row (the base condition), which is the full list of 10 types.

---

## Statistical Confidence

With only 1/10 correct (10% accuracy), this question has **90% failure rate** under current agent configuration:
- LLM: qwen/qwen3-32b (via Groq)
- Temperature: Default (likely 0.0-0.3 based on deterministic tool output)
- Reflection: Enabled (but ineffective for this error type)

---

## Recommended Fixes

### Option 1: Improve Question Clarity
Rewrite the question to avoid the "ice" keyword that triggers false association:
> "What type of enclosure is suitable for outdoor use with rain and sleet per Table 110.28?"

### Option 2: Improve Tool Output Formatting
Restructure the table output to make the hierarchy clearer:
```
=== Base Outdoor Weather Conditions ===
Rain, snow, and sleet: Types 3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, 6P

=== Additional Specific Conditions ===
Sleet* (mechanism operable when ice covered): Types 3S, 3SX only
```

### Option 3: Add Explicit System Prompt Guidance
Add to the agent system prompt:
> "When interpreting Table 110.28, the 'Rain, snow, and sleet' row lists the BASE enclosures suitable for general outdoor weather. The 'Sleet*' row with footnote indicates ADDITIONAL ice-operability features for specific enclosures. Do not filter the base answer by the specific condition unless explicitly required."

### Option 4: Add Post-Processing Validation
Add a validation check after table lookups:
- If the question mentions Table 110.28 and "rain, sleet"
- AND the answer excludes Type 3 or 3R
- THEN flag for review or force re-evaluation

---

## Conclusion

The inconsistency in CEC2022-045 is caused by **LLM semantic confusion** between two similar but distinct table rows, not by tool randomness. The agent receives correct, deterministic tool data but interprets it incorrectly 90% of the time. The reflection layer fails to catch this because the wrong answer is internally consistent with the flawed interpretation.

This is a **prompt engineering and table interpretation problem**, not a tool or retrieval problem.
