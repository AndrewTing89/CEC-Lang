# Post-Judge Analysis & Fixes Applied

## Summary

After reviewing the judge reports from Run 3, we identified **7 critical failure patterns** causing the 60%+ error rate. The following fixes were implemented to address these issues.

---

## Failure Patterns Identified

### Pattern 1: Table Lookup Errors (3 critical failures)
- `baseline-002`: Expected 6 AWG copper for 60A → Agent said 4 AWG
- `baseline-005`: Expected 4/0 AWG aluminum for 200A → Agent said 250 kcmil
- `inspection-010`: Expected 2/0 AWG GEC for 1000 kcmil → Agent said 1/0 AWG

**Root Cause:** Agent was using forward lookup tools (size → ampacity) for reverse lookup questions (ampacity → size), leading to guessing.

### Pattern 2: Missing Critical Safety Violations (2 failures)
- `core-005`: Missed panels PROHIBITED in clothes closets (240.24(D))
- `core-005`: Missed storage violation in working space (110.26(B))

**Root Cause:** Agent stopped after finding one issue instead of searching all violation categories.

### Pattern 3: Incomplete List Enumeration (8+ partial)
- `cec-001`: Listed 4 appliances, missed EV charging (5th item)
- `cec-017`: Listed some enclosures, missed Type 3, 3R, 3S

**Root Cause:** Search limit too low; no verification of completeness.

### Pattern 4: Exception Misapplication (2 failures)
- `inspection-005`: Incorrectly claimed dishwasher exempt from GFCI

**Root Cause:** Found exceptions but didn't verify they apply to the scenario.

### Pattern 5: Wrong Derating Factors (1 failure)
- `inspection-009`: Used 0.70 bundling factor instead of 0.80 for 6 conductors

**Root Cause:** Confusion between conductor count ranges.

### Pattern 6: Code Edition Confusion (2 failures)
- `core-004`: Asked about NEC 2023 → Agent answered with CEC 2022

**Root Cause:** Defaulted to CEC when NEC was explicitly requested.

---

## Fixes Implemented

### Fix 1: New Reverse Table Lookup Tools
Added two new tools:
- `cec_lookup_conductor_size(required_ampacity, temperature_rating, conductor_type)`
- `nec_lookup_conductor_size(required_ampacity, temperature_rating, conductor_type)`

These tools find the MINIMUM conductor size that meets a required ampacity, eliminating guesswork.

**Files Modified:**
- `core/cec_table_tools.py` - Added `cec_lookup_conductor_size_for_ampacity()`
- `core/nec_table_tools.py` - Added `nec_lookup_conductor_size_for_ampacity()`
- `core/tools.py` - Registered new tools

### Fix 2: System Prompt Updates
Added 6 new critical sections to the system prompt:

1. **CONDUCTOR SIZING: FORWARD vs REVERSE LOOKUPS** - Explains when to use each tool type
2. **INSPECTION/COMPLIANCE QUESTION PROTOCOL** - Mandatory 5-category violation scan
3. **LIST ENUMERATION QUESTIONS** - Requirements for exhaustive retrieval
4. **EXCEPTION APPLICABILITY VERIFICATION** - Must verify exception conditions match scenario
5. **DERATING CALCULATIONS** - Explicit bundling factor values and common errors
6. **CODE EDITION AWARENESS** - How to identify and use correct code

**File Modified:**
- `core/agent.py` - Updated SYSTEM_PROMPT (~160 lines added)

---

## Expected Improvements

| Pattern | Previous Result | Expected After Fix |
|---------|-----------------|-------------------|
| Table lookups | 3 critical errors | Should be correct with new tools |
| Missing violations | 2 failures | Multi-angle scan should catch all |
| Incomplete lists | 8+ partial | Higher limit + verification |
| Exception misapplication | 2 failures | Condition verification |
| Derating factors | 1 failure | Explicit guidance |
| Code edition | 2 failures | Edition awareness check |

---

## Test Plan

Run 4 will test:
- All 28 core evaluation questions
- All 30 CEC evaluation questions

Compare results to Run 3 to measure improvement.
