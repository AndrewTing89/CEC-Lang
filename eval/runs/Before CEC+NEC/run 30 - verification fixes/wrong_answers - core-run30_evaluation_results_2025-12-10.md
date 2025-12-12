# Wrong Answers - core-run30_evaluation_results_2025-12-10

**Model:** CEC Lang Agent (qwen/qwen3-32b)
**Judge:** Claude Code (Opus)
**Overall Score:** 93.7% (253/270)

---

## Executive Summary
**Questions with Errors:** 7 of 27
**Perfect Scores:** 20

---

## Detailed Error Analysis

### 1. inspection-001 (Score: 5/10) - CRITICAL ERROR
**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized.

**Agent Answer:** Calculated general load 13,500 VA (correct), applied a combined 100%/40% demand factor to total load, arrived at 14,640 VA ÷ 240V = **61A**.

**Expected Answer:** Apply Table 220.42 demand factors to general lighting/receptacle load separately: first 3000 VA at 100%, remaining at 35%. Then add appliance loads. Final calculated load: **103.2A**.

**Accuracy:** 2/5 - Wrong methodology yields significantly wrong result (61A vs 103.2A)
**Completeness:** 3/5 - Shows work but wrong approach

**Specific Errors:**
- Applied 100%/40% demand factor to combined total instead of Table 220.42 factors (100%/35%) to general lighting load only
- Result differs by 42A from expected calculation
- While both conclude 200A is adequate, the reasoning is incorrect

---

### 2. core-002 (Score: 7/10)
**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Agent Answer:** Requires 2-pole circuit breaker for simultaneous disconnection. States: "Single-pole breakers with handle ties are *not* permitted for MWBCs."

**Expected Answer:** Requires either a **handle tie or common trip breaker** to simultaneously disconnect all ungrounded conductors per 210.4(B).

**Accuracy:** 3/5 - Incorrect statement about handle ties
**Completeness:** 4/5 - Otherwise comprehensive

**Specific Errors:**
- INCORRECT: Agent claims handle ties are not permitted for MWBCs
- NEC 210.4(B) explicitly allows handle ties as an alternative to common trip breakers
- This is a factual error that could mislead electricians

---

### 3. core-005 (Score: 7/10)
**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Agent Answer:** Does not meet requirements due to insufficient depth (24" < 36" required). Discusses Condition 1 vs 2 considerations.

**Expected Answer:** No, violates: (1) 36" depth; (2) panels prohibited in clothes closets per 240.24(D); (3) 30" width requirement; (4) no storage in working space per 110.26(B).

**Accuracy:** 4/5 - Correctly identifies depth violation but misses other violations
**Completeness:** 3/5 - Missing several important violations

**Specific Errors:**
- Missing: 240.24(D) clothes closet prohibition (if this is a clothes closet)
- Missing: 110.26(B) storage in working space prohibition
- Only focused on depth clearance, didn't fully analyze water heater obstruction issue

---

### 4. inspection-005 (Score: 7/10)
**Question:** Kitchen installation with countertop receptacles, dishwasher, disposal, and refrigerator circuits. Specify required protection (GFCI, AFCI, or combination).

**Agent Answer:** Countertop: AFCI/GFCI. Dishwasher: AFCI/GFCI. Disposal: AFCI/GFCI. **Refrigerator: AFCI only** (claims GFCI exception under 210.8(A) Exception No. 2).

**Expected Answer:** All circuits including refrigerator need AFCI/GFCI combo per NEC 2023 210.8(A)(5) which covers **ALL kitchen receptacles**.

**Accuracy:** 3/5 - Incorrect on refrigerator GFCI requirement
**Completeness:** 4/5 - Otherwise comprehensive

**Specific Errors:**
- INCORRECT: NEC 2023 expanded 210.8(A)(5) to require GFCI for ALL kitchen receptacles
- The refrigerator exemption the agent cites does NOT apply in NEC 2023
- Refrigerator circuits in kitchens now require GFCI protection

---

### 5. baseline-003 (Score: 8/10)
**Question:** Where is GFCI protection required in a residential kitchen?

**Agent Answer:** GFCI required for countertop receptacles per 210.8(A)(6), receptacles within 6 ft of sink.

**Expected Answer:** All receptacles serving kitchen countertop surfaces AND dishwashers require GFCI protection.

**Accuracy:** 4/5 - Correct on countertops, missing dishwasher
**Completeness:** 4/5 - Missing dishwasher requirement

**Specific Errors:**
- Missing explicit mention of dishwasher GFCI requirement

---

### 6. core-003 (Score: 9/10)
**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Agent Answer:** Lists: bathrooms, garages, outdoors, crawl spaces, kitchens, areas with sinks (6ft), bathtubs/showers, laundry areas, damp/wet locations, boathouses.

**Expected Answer:** Includes all of the above plus "unfinished basements" as a specific category.

**Accuracy:** 5/5 - All listed locations correct
**Completeness:** 4/5 - Missing unfinished basements

**Specific Errors:**
- Missing explicit mention of "unfinished basements" as a GFCI-required location

---

## Problem Areas Summary

1. **NEC Article 220 Load Calculations (inspection-001):** Agent used incorrect demand factor methodology. This is a complex calculation that requires careful application of Table 220.42 demand factors to specific load categories, not a blanket percentage to total load.

2. **2023 NEC GFCI Expansion (inspection-005, baseline-003):** Agent doesn't fully account for NEC 2023 changes that expanded GFCI requirements to ALL kitchen receptacles including dedicated appliance circuits like refrigerators.

3. **MWBC Handle Tie Requirements (core-002):** Agent incorrectly stated handle ties are not permitted. This is a factual error - NEC 210.4(B) explicitly allows handle ties as an acceptable method.

4. **Clothes Closet Prohibition (core-005):** Agent missed the 240.24(D) prohibition on overcurrent devices in clothes closets. This is a frequently tested inspection topic.

---

## Recommendations

1. **Load Calculation Training:** Enhance prompts or tools to properly apply Table 220.42 demand factors to general lighting/receptacle loads separately from appliance loads.

2. **NEC 2023 Updates:** Ensure knowledge base reflects NEC 2023 changes, particularly the expanded GFCI requirements in 210.8(A)(5) for kitchen receptacles.

3. **MWBC Requirements:** Correct the erroneous information about handle ties - they ARE permitted per 210.4(B).

4. **Panel Location Rules:** Add 240.24(D) clothes closet prohibition to the knowledge retrieval for panel installation questions.

---

## Comparison to Run 29

| Metric | Run 29 | Run 30 | Change |
|--------|--------|--------|--------|
| Score | 89.3% | 93.7% | +4.4% |
| Perfect Scores | ~17 | 20 | +3 |
| Calculation Errors | Higher | Lower | Improved |

**Key Improvements:**
- Calculation questions (core-010, inspection-009) now consistently correct due to verification fixes
- Conduit fill (inspection-007) now correct after hallucination retry
- GEC sizing (inspection-010) now correct

**Remaining Issues:**
- Load calculation methodology (inspection-001) still uses wrong approach
- NEC 2023 GFCI expansion not fully captured
- Some factual errors persist (handle tie statement)
