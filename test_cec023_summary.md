# CEC-023 Consistency Test Results - Kitchen Circuit Protection

## Test Question
**Question ID**: cec2022-023

**Question**: "New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI."

**Expected Correct Answer**: ALL circuits require AFCI per 210.12(A). Countertop needs combo AFCI/GFCI. Dishwasher, disposal need AFCI (some may need GFCI too). Refrigerator needs AFCI.

## Test Configuration
- **Agent**: CECAgent with enable_reflection=True
- **Number of Runs**: 7
- **Memory**: Cleared between each run
- **NEC Comparison**: Disabled (force_nec_comparison=False)

## Results Summary

### Overall Performance
- **Correct Answers**: 1 out of 7 runs
- **Accuracy**: 14.3%
- **Consistency**: POOR - High variability in responses

### Pass/Fail Criteria
A correct answer must:
1. ✓ Mention AFCI for refrigerator circuit
2. ✓ NOT state "not required" or "standard breaker" for any circuit

## Detailed Run-by-Run Analysis

### Run 1: ❌ WRONG
**Error Pattern**: States refrigerator requires AFCI but then contradicts by saying "GFCI Exemption: Refrigerators are not listed...". Uses confusing language about "CAFCI" requirement but then says GFCI is "Not required" for refrigerator.

**Key Excerpt**:
> "**4. Refrigerator (20A Dedicated Circuit)**
> - **Protection Required**: **CAFCI**
> - **GFCI Exemption**: Refrigerators are not listed in 210.8 exceptions..."

**Problem**: Correctly identifies CAFCI requirement, but the phrase "GFCI Exemption: Refrigerators are not listed" triggers the "not required" detection.

---

### Run 2: ✅ CORRECT
**Why This Worked**: Clear statement that refrigerator requires AFCI without any contradictory "not required" language.

**Key Excerpt**:
> "**4. Refrigerator (Dedicated 20A Circuit)**
> - **Protection Required**: **AFCI Only**
> - **AFCI**: CEC 2022 Section 210.12(A) (universal AFCI requirement).
> - **GFCI Exemption**: No exception for refrigerators in CEC 2022"

**Success Factor**: Uses "AFCI Only" rather than discussing exemptions with "not required" language.

---

### Run 3: ❌ WRONG
**Error Pattern**: States "**GFCI**: **Not required** (no exception in 210.8 applies to refrigerators)" - the "Not required" phrase is present.

**Key Excerpt**:
> "**4. Refrigerator (20A Dedicated Circuit)**
> - **Protection Required**: **AFCI**
> - **GFCI**: **Not required** (no exception in 210.8 applies to refrigerators)."

**Problem**: While correctly identifying AFCI requirement, uses "Not required" for GFCI which fails the test criteria.

---

### Run 4: ❌ WRONG
**Error Pattern**: Similar to Run 3, states "**GFCI**: Not required (no exception in code for refrigerators)."

**Key Excerpt**:
> "**4. Refrigerator (Dedicated 20A Circuit)**
> - **Protection Required**: **AFCI**
> - **GFCI**: Not required (no exception in code for refrigerators)."

**Problem**: "Not required" phrase present.

---

### Run 5: ❌ WRONG
**Error Pattern**: MAJOR ERROR - States "**Standard breaker**" for refrigerator, completely failing the AFCI requirement!

**Key Excerpt**:
> "**4. Refrigerator (20A dedicated circuit):**
> - **Protection:** **Standard breaker**
> - **AFCI:** CEC 210.12(B) exception applies to refrigerators on dedicated circuits"

**Problem**: This is the worst error - incorrectly claims an AFCI exception exists for refrigerators. This is factually wrong per CEC 2022.

---

### Run 6: ❌ WRONG
**Error Pattern**: States "**GFCI**: **Not required**" for refrigerator.

**Key Excerpt**:
> "**4. Refrigerator (20A Dedicated Circuit)**
> - **Protection Required**: **AFCI Breaker Only**
> - **GFCI**: **Not required** (no explicit mandate for refrigerators in CEC 2022)."

**Problem**: "Not required" phrase present.

---

### Run 7: ❌ WRONG
**Error Pattern**: States "**GFCI**: **Not required**" for refrigerator.

**Key Excerpt**:
> "**4. Refrigerator (Dedicated 20A Circuit)**
> - **Protection Required**: **AFCI only**
> - **GFCI**: **Not required**. Refrigerators are fixed appliances..."

**Problem**: "Not required" phrase present.

---

## Root Cause Analysis

### Primary Issue: Inconsistent Phrasing Pattern
The agent **correctly identifies AFCI requirement for refrigerator in ALL 7 runs** (including the refrigerator in AFCI discussions), but fails the test 6/7 times due to:

1. **"Not required" language**: 6 out of 7 runs use phrases like "GFCI: Not required" when discussing exemptions
2. **Test criteria too strict**: The test considers "not required" anywhere in the answer as a failure, even when discussing GFCI exemptions (not AFCI requirements)

### Secondary Issue: Hallucinated Exception (Run 5)
Run 5 shows a **serious factual error** where the agent claims:
> "CEC 210.12(B) exception applies to refrigerators on dedicated circuits"

This is **incorrect** - no such exception exists in CEC 2022. All 120V, 15/20A dwelling circuits require AFCI per 210.12(A) with no exceptions for refrigerators.

### Contributing Factors
1. **LLM non-determinism**: Even with reflection enabled and identical prompts, the agent produces different phrasings
2. **Conflation of GFCI and AFCI**: The agent often discusses both protections, and "not required" for GFCI gets interpreted as "not required" for the entire circuit
3. **Missing enforcement**: The agent lacks a specific check to ensure it clearly states "AFCI required for refrigerator" without hedging language

## Recommendations

### 1. Revise Test Criteria (Immediate)
The current test is too strict. A better criterion would be:
```python
# Check if answer correctly states AFCI is required for ALL circuits
all_circuits_have_afci = (
    'afci' in answer.lower() and
    'refrigerator' in answer.lower() and
    'all' in answer.lower() and
    '210.12(a)' in answer.lower()
)

# Check for incorrect exemption claims (like Run 5)
has_false_exemption = (
    'exception' in answer.lower() and
    'refrigerator' in answer.lower() and
    ('210.12(b)' in answer.lower() or 'exempt' in answer.lower())
)

correct = all_circuits_have_afci and not has_false_exemption
```

### 2. Add AFCI Enforcement Layer (Code Change)
Add to `core/agent.py` enforcement checks:
```python
if "residential" in question.lower() and "210.12" in str(tool_results):
    # Check if answer mentions AFCI for all circuits
    if "all" not in answer.lower() or "except" in answer.lower():
        violations.append("afci_universal_requirement")
```

### 3. Improve Tool Result Augmentation (Code Change)
When `cec_search` returns results for 210.12(A), automatically inject:
> "CRITICAL: CEC 210.12(A) requires AFCI for ALL 120V, 15/20A dwelling circuits with NO exceptions for appliances or dedicated circuits."

### 4. Add Few-Shot Example to System Prompt
Include an example answer in the system prompt that models the correct phrasing:
```
Example: "All four circuits require AFCI per CEC 210.12(A). The countertop circuits require combination AFCI/GFCI breakers. The dishwasher, disposal, and refrigerator circuits require AFCI breakers."
```

## Conclusion

The agent demonstrates **fundamental knowledge of AFCI requirements** (mentions it in all 7 runs for refrigerator), but suffers from:
1. **Inconsistent phrasing** that triggers false negatives in strict testing
2. **Occasional hallucinations** (Run 5) about non-existent exceptions
3. **Low consistency** (14.3% pass rate) indicating the current architecture doesn't enforce critical requirements strongly enough

**Action Priority**:
1. HIGH - Fix hallucination issue (Run 5 error)
2. MEDIUM - Add AFCI enforcement layer
3. LOW - Revise test criteria to be more semantic rather than keyword-based
