# Wrong Answers - core-run22_evaluation_results_2025-12-10

**Model:** CEC Agent (qwen/qwen3-32b)
**Judge:** Claude Code (Opus)
**Overall Score:** 74.6% (209/280)

---

## Executive Summary
**Questions with Errors:** 14 of 28
**Perfect Scores:** 14
**Critical Failures (0/10):** 2 (answered wrong question entirely)

---

## Critical Errors (0-4/10)

### 1. inspection-001 (Score: 0/10)
**Question:** Residential panel inspection: 200A main breaker. Calculate service load per NEC Article 220.
**Accuracy:** 0/5 - COMPLETELY WRONG TOPIC
**Completeness:** 0/5 - Does not address question
**Specific Errors:**
- Model answered about TORQUE SPECIFICATIONS instead of load calculation
- Expected: Detailed Article 220 calculation showing ~103.2A load
- Did not perform any load calculation
- This appears to be a model confusion/hallucination issue

---

### 2. inspection-006 (Score: 0/10)
**Question:** Subpanel bonding violations - identify all violations
**Accuracy:** 0/5 - COMPLETELY WRONG TOPIC
**Completeness:** 0/5 - Does not address question
**Specific Errors:**
- Model answered about SERVICE LOAD CALCULATION instead of bonding violations
- Expected: Identify neutral bonded to enclosure (violation), MBJ in subpanel (violation)
- Did not identify any bonding issues
- Another model confusion/hallucination issue

---

### 3. core-007 (Score: 2/10)
**Question:** How should grounding and bonding be configured in garage subpanel?
**Accuracy:** 1/5 - Answered different question
**Completeness:** 1/5 - Wrong topic
**Specific Errors:**
- Model answered about GEC SIZING instead of bonding configuration
- Expected: Grounds/neutrals SEPARATED, no MBJ in subpanel, neutral isolated from enclosure
- Did not explain correct subpanel bonding configuration

---

### 4. inspection-005 (Score: 4/10)
**Question:** Kitchen circuit protection types (GFCI, AFCI, combination)
**Accuracy:** 2/5 - Multiple errors
**Completeness:** 2/5 - Missing key requirements
**Specific Errors:**
- WRONG: Says dishwasher is EXEMPT from GFCI - NEC 2023 210.8(D) REQUIRES GFCI for dishwashers
- WRONG: Says garbage disposal is EXEMPT - 2023 NEC requires GFCI if cord-connected
- MISSING: AFCI requirements per 210.12(A) for all kitchen circuits
- Expected: Combination AFCI/GFCI for countertops and dishwasher

---

### 5. inspection-008 (Score: 4/10)
**Question:** Voltage drop calculation
**Accuracy:** 2/5 - Wrong calculation result
**Completeness:** 2/5 - Wrong conclusion
**Specific Errors:**
- Model calculated 4.36V (3.63%) - WRONG
- Correct: VD = (2 x 50 x 1.29 x 22) / 1000 = 2.84V (2.37%)
- Model concluded "exceeds 3% limit" - should be "meets 3% limit"
- Appears to have used wrong resistance value (1.98 instead of 1.29)

---

## Medium Errors (5-7/10)

### 6. baseline-006 (Score: 5/10)
**Question:** Minimum working clearance depth for 120/240V panel
**Accuracy:** 2/5 - Wrong value
**Completeness:** 3/5 - Has reference but wrong value
**Specific Errors:**
- Model says 30 inches - WRONG
- Correct answer: 36 inches (3 feet) per Table 110.26(A)(1)
- Both 0-150V and 151-600V Condition 1 require 36 inches

---

### 7. core-004 (Score: 5/10)
**Question:** Surge protection required and installation location
**Accuracy:** 2/5 - Major factual error
**Completeness:** 3/5 - Partial info
**Specific Errors:**
- WRONG: States "NEC 2023: No Mandatory Requirement"
- CORRECT: NEC 2023 Section 230.67 DOES require SPD for dwelling units
- This requirement was added in 2020 NEC and retained in 2023

---

### 8. core-005 (Score: 5/10)
**Question:** Panel in closet with violations
**Accuracy:** 2/5 - Wrong values, missing violations
**Completeness:** 3/5 - Incomplete
**Specific Errors:**
- Says 30 inches depth required - WRONG (36 inches)
- Missing: Panels prohibited in CLOTHES CLOSETS per 240.24(D)
- Missing: Storage prohibition in working space per 110.26(B)
- Question specified "closet" which triggers 240.24(D)

---

### 9. inspection-002 (Score: 5/10)
**Question:** Garage panel working space violations
**Accuracy:** 2/5 - Wrong values
**Completeness:** 3/5 - Partial identification
**Specific Errors:**
- Says 30 inches required - WRONG (36 inches per 110.26(A)(1))
- Incorrectly identifies panel height as violation (5 feet is mounting height, not working space height)
- Working space HEIGHT requirement is 6.5 feet FROM FLOOR, not panel mounting height
- Water heater obstruction correctly identified

---

### 10. core-010 (Score: 7/10)
**Question:** Adjusted ampacity at 50C with 6 conductors
**Accuracy:** 3/5 - Wrong starting value
**Completeness:** 4/5 - Method correct
**Specific Errors:**
- Base ampacity: Model says 35A - WRONG
- Correct: 30A for 12 AWG THHN at 90C per Table 310.16
- Factors correct (0.82, 0.80)
- Final result 23.1A should be ~19.68A

---

## Minor Errors (8-9/10)

### 11. baseline-003 (Score: 9/10)
**Question:** GFCI in kitchen
**Specific Errors:**
- Missing specific mention of dishwasher GFCI requirement

---

### 12. core-001 (Score: 8/10)
**Question:** 200A service conductor sizing
**Specific Errors:**
- States 4/0 copper or 250 kcmil aluminum (oversized)
- Minimum per Table 310.12: 2/0 copper OR 4/0 aluminum

---

### 13. core-002 (Score: 9/10)
**Question:** Multiwire branch circuit requirements
**Specific Errors:**
- Missing explicit mention of grouping per 210.4(D)

---

### 14. core-003 (Score: 9/10)
**Question:** GFCI locations list
**Specific Errors:**
- Says "indoor damp/wet locations" vs specifically "unfinished basements"

---

## Questions FIXED by Tool Refactoring

### inspection-007 (NOW 10/10)
**Previous Issue:** Used `nec_lookup_table("4")` which returned Table 400.4 (wrong)
**Now:** Uses `nec_conduit_fill_calculator` - gets correct 28 conductors

### inspection-009 (NOW 10/10)
**Previous Issue:** Hallucinated factors (0.58, 0.50) instead of looking them up
**Now:** Gets correct factors (0.71, 0.80) and result (11.36A)

---

## Root Cause Analysis

### Critical Model Failures (0/10 scores)
- **inspection-001 and inspection-006**: Model answered completely different questions
- Possible causes: context confusion, question parsing failure, model hallucination
- These need investigation - the model received the right question but generated unrelated answers

### Systematic Errors
1. **Working space depth**: Model consistently says 30" instead of 36" (affects baseline-006, core-005, inspection-002)
2. **NEC 2023 SPD requirement**: Model incorrectly states NEC doesn't require surge protection
3. **2023 NEC kitchen GFCI**: Model has outdated info about dishwasher GFCI exemption (removed in 2023 NEC)

### Improvements Observed
- Conduit fill calculation: FIXED by `nec_conduit_fill_calculator`
- Ampacity adjustment: FIXED - now gets correct factors
