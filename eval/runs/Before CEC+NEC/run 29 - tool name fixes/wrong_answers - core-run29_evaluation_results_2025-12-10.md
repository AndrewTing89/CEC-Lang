# Wrong Answers - core-run29_evaluation_results_2025-12-10

**Model:** CEC Lang Agent (qwen/qwen3-32b)
**Judge:** Claude Code (Opus)
**Overall Score:** 89.3% (241/270)

---

## Executive Summary
**Questions with Errors:** 13 of 27
**Perfect Scores:** 14

---

## Detailed Error Analysis

### 1. inspection-010 (Score: 3/10) - CRITICAL ERROR
**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.
**Accuracy:** 2/5 - Response is essentially blank/empty with no answer provided
**Completeness:** 1/5 - No relevant information provided
**Specific Errors:**
- Agent hit max iterations (15) without producing an answer
- Tool `cec_lookup_grounding_conductor` was called 6 times without resolving the query
- Expected answer: 2/0 AWG copper GEC per Table 250.66 for 1000 kcmil service conductors
- Note: Table 250.66 shows "Over 600 kcmil through 1100 kcmil" requires 2/0 AWG copper GEC

---

### 2. inspection-002 (Score: 7/10)
**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.
**Accuracy:** 3/5 - Some violations identified correctly, some incorrect
**Completeness:** 4/5 - Most violations covered but with errors
**Specific Errors:**
- INCORRECT: Claims 54 inches width required - actual requirement is 30 inches or equipment width, whichever is greater (30" is likely compliant)
- INCORRECT: Claims headroom violation at 5 feet - the 5 ft refers to mounting height, not working space headroom (need more info to determine headroom compliance)
- CORRECT: 28" depth is a violation (36" required)
- CORRECT: Water heater obstruction is a violation

---

### 3. inspection-005 (Score: 7/10)
**Question:** Kitchen installation circuit protection requirements for countertops, dishwasher, disposal, refrigerator
**Accuracy:** 3/5 - Most correct but refrigerator answer is wrong
**Completeness:** 4/5 - Good coverage but error affects completeness
**Specific Errors:**
- INCORRECT: States refrigerator only needs AFCI (no GFCI)
- NEC 2023 Section 210.8(A)(5) expanded to require GFCI for ALL kitchen receptacles
- This includes refrigerator circuits - they now need GFCI+AFCI (combination breaker)
- The exception for dedicated appliance circuits was removed in NEC 2023

---

### 4. inspection-001 (Score: 8/10)
**Question:** Residential panel service load calculation
**Accuracy:** 4/5 - Correct methodology (optional method) but different from expected (standard method)
**Completeness:** 4/5 - Complete calculation using optional method
**Specific Errors:**
- Used Optional Method (220.82) instead of Standard Method (220.42)
- Both are valid per NEC, but expected answer used standard method with Table 220.42 demand factors
- Standard method calculation: 6675 + 8000 + 5500 + 4600 = 24,775 VA = 103.2A
- Optional method result: 84.3A
- Final conclusion (200A adequate) is correct for both methods

---

### 5. core-005 (Score: 8/10)
**Question:** Panel in closet with 24 inches clearance and water heater 18 inches to the side
**Accuracy:** 4/5 - Identifies main violations but adds incorrect detail
**Completeness:** 4/5 - Missing clothes closet prohibition
**Specific Errors:**
- INCORRECT: Claims 42" depth required for 240V (Condition 2) - should be 36" for Condition 1 or 2 at 120/240V residential
- MISSING: Doesn't mention panels are prohibited in clothes closets per 240.24(D)
- CORRECT: Identifies depth and obstruction violations

---

### 6. baseline-003 (Score: 8/10)
**Question:** GFCI requirements in residential kitchen
**Accuracy:** 4/5 - Correct for countertops and sink distance, missing dishwasher
**Completeness:** 4/5 - Good coverage but incomplete
**Specific Errors:**
- MISSING: Does not mention dishwasher GFCI requirement
- Expected answer includes: "Additionally, dishwashers require GFCI protection"

---

### 7. core-002 (Score: 9/10)
**Question:** Multiwire branch circuit requirements
**Accuracy:** 5/5 - Correctly identifies 2-pole breaker requirement
**Completeness:** 4/5 - Missing some details
**Specific Errors:**
- MISSING: Handle tie option not explicitly mentioned (expected: "handle tie OR common trip breaker")
- MISSING: Conductor grouping requirement per 210.4(D) not explicitly stated

---

### 8. core-003 (Score: 9/10)
**Question:** GFCI locations in residential dwelling per NEC 2023
**Accuracy:** 5/5 - Lists correct locations
**Completeness:** 4/5 - Missing one location
**Specific Errors:**
- MISSING: "Unfinished basements" not explicitly listed as distinct location

---

### 9. core-012 (Score: 9/10)
**Question:** Torque specifications importance
**Accuracy:** 5/5 - Correctly explains importance
**Completeness:** 4/5 - Missing table reference
**Specific Errors:**
- MISSING: Table 110.14(D) not explicitly mentioned (expected answer mentions both 110.14(D) and Table 110.14(D))

---

### 10-13. Minor Deductions (8-9/10 scores)
The remaining questions with imperfect scores had minor omissions but no significant errors.

---

## Problem Areas Summary

1. **Critical Issue - Max Iterations Without Answer (inspection-010):** Agent got stuck in a loop calling the same tool repeatedly without producing an answer for the parallel conductor GEC sizing question.

2. **NEC 2023 Updates (inspection-005):** Incorrect on refrigerator GFCI requirement - NEC 2023 expanded 210.8(A)(5) to cover ALL kitchen receptacles.

3. **Working Space Requirements (inspection-002, core-005):** Inconsistent/incorrect application of Table 110.26(A)(1) requirements.

4. **Calculation Method Variation (inspection-001):** Used optional method vs expected standard method - both valid but different approaches.

5. **Minor Omissions:** Several answers missing specific details like handle ties, basements, dishwasher GFCI, etc.
