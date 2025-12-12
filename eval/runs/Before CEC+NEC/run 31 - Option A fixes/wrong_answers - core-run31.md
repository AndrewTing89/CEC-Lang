# Wrong Answers - core-run31_evaluation_results_2025-12-11.md

**Model:** qwen/qwen3-32b
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 91.5% (247/270)

---

## Executive Summary
**Questions with Errors:** 12 of 27
**Perfect Scores:** 15

---

## Detailed Error Analysis

### 1. inspection-001 (Score: 7/10)
**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC. Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized.

**Agent Answer:** Total 32,500 VA / 240V = 135.4A. Used range demand factor 0.67 (8000VA), dryer 5250VA, AC 5750VA (with 1.25 multiplier).

**Expected Answer:** General lighting: 9000 VA. Small appliance: 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA. Dryer: 5500 VA. AC: 4600 VA. Total: 24,775 VA = 103.2A.

**Accuracy:** 3/5 - Final conclusion correct but methodology differs significantly
**Completeness:** 4/5 - Shows work but wrong demand factor approach
**Specific Errors:**
- Did NOT apply Table 220.42 demand factors (first 3000VA at 100%, remainder at 35%)
- Used incorrect dryer demand calculation (5250VA vs 5500VA)
- Applied 1.25 continuous load multiplier to AC (not always required for load calc)
- Total calculated load 135.4A vs expected 103.2A

---

### 2. core-002 (Score: 8/10)
**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Agent Answer:** Requires 2-pole breaker or single-pole breakers with listed handle tie per 210.4(B). Neutral must be grouped per 210.4(D).

**Expected Answer:** Handle tie OR common trip breaker per 210.4(B). Common trip required if both line-to-line and line-to-neutral loads. Handle ties SHALL be permitted per 240.15(B)(1). Neutral must be continuous and not switched.

**Accuracy:** 4/5 - Correct overall but missing key detail
**Completeness:** 4/5 - Missing important distinction
**Specific Errors:**
- Does not explicitly reference 240.15(B)(1) which permits handle ties
- Missing distinction that common trip is required when circuit has BOTH line-to-line and line-to-neutral loads
- Does not mention neutral must be continuous and not switched

---

### 3. baseline-003 (Score: 9/10)
**Question:** Where is GFCI protection required in a residential kitchen?

**Agent Answer:** All 125V-250V receptacles serving countertop surfaces per 210.8(A)(6).

**Expected Answer:** All receptacles serving countertop surfaces AND dishwasher.

**Accuracy:** 5/5 - Countertop requirement correct
**Completeness:** 4/5 - Missing dishwasher
**Specific Errors:**
- Does not mention dishwasher GFCI requirement per NEC 2023

---

### 4. inspection-002 (Score: 8/10)
**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side...

**Agent Answer:** Violations: depth 28" vs 42" required (Condition 2), height 5' vs 6.5' required, water heater obstruction.

**Expected Answer:** Violations: (1) depth 28" vs 36" required per 110.26(A)(1), (2) water heater in working space prohibited per 110.26(B). Width 30" meets minimum.

**Accuracy:** 4/5 - Identified violations but wrong depth requirement
**Completeness:** 4/5 - Some inaccuracies
**Specific Errors:**
- Applied 42" (Condition 2) instead of 36" (Condition 1) for residential 120/240V panel
- Height violation may be overstated (5' panel mounting height doesn't necessarily violate code)

---

### 5. inspection-005 (Score: 8/10)
**Question:** New residential construction, 2023 NEC. Kitchen installation... specify required protection for each circuit.

**Agent Answer:** Countertops: AFCI/GFCI. Dishwasher: GFCI+AFCI. Disposal: GFCI+AFCI. Refrigerator: AFCI only (no GFCI).

**Expected Answer:** ALL circuits require combination AFCI/GFCI per 2023 NEC, including refrigerator.

**Accuracy:** 4/5 - Incorrectly exempts refrigerator from GFCI
**Completeness:** 4/5 - Missing refrigerator GFCI
**Specific Errors:**
- NEC 2023 expanded 210.8(A)(5) to cover ALL kitchen receptacles including dedicated appliance circuits like refrigerator
- Refrigerator MUST have GFCI protection in 2023 NEC

---

### 6. inspection-008 (Score: 8/10)
**Question:** Calculate voltage drop... Show your work.

**Agent Answer:** 2.37% voltage drop meets NEC recommendations. Does not show full formula.

**Expected Answer:** VD = (2 x L x R x I) / 1000 = (2 x 50 x 1.29 x 22) / 1000 = 2.84V. Percentage: 2.84V / 120V = 2.37%.

**Accuracy:** 4/5 - Correct final answer
**Completeness:** 4/5 - Missing step-by-step calculation
**Specific Errors:**
- Question specifically asks to "show your work" with formula
- Does not show VD formula or intermediate calculation

---

### 7. inspection-007 (Score: 9/10)
**Question:** Maximum 10 AWG THHN conductors in 1-1/4" RMC... Show calculation.

**Agent Answer:** 0.61 sq in / 0.0211 sq in = 28.91, max 28 conductors.

**Expected Answer:** 28.91 conductors. Per Chapter 9 Note 7, when decimal is 0.8 or larger, round up. 29 conductors maximum.

**Accuracy:** 5/5 - Calculation correct
**Completeness:** 4/5 - Missing Note 7 rounding rule
**Specific Errors:**
- Does not mention Chapter 9 Note 7 which allows rounding up to 29 when decimal >= 0.8
- Conservative answer (28) is acceptable but incomplete explanation

---

## Summary of Error Patterns

### Pattern 1: Demand Factor Application (inspection-001)
The agent uses alternative demand factor approaches instead of the specific Table 220.42 method requested.

### Pattern 2: 2023 NEC Expansion (inspection-005)
Missing awareness that 2023 NEC expanded GFCI to ALL kitchen receptacles including dedicated circuits.

### Pattern 3: Show Work Requests (inspection-008)
When asked to "show your work," agent sometimes provides conclusion without full formula/steps.

### Pattern 4: Specialized Code Details (core-002)
Missing nuanced requirements like 240.15(B)(1) handle tie permission and common trip vs handle tie distinction.

---

## Recommendations

1. **Table 220.42 Training**: Ensure agent knows to apply first 3000VA at 100%, remainder at 35% for dwelling unit lighting/receptacle loads.

2. **2023 NEC Updates**: Update knowledge about expanded GFCI coverage in kitchens (all receptacles, not just countertop).

3. **Show Work Responses**: When "show your work" is requested, always include formula and step-by-step calculation.

4. **Handle Tie vs Common Trip**: Clarify when handle ties are permitted (240.15(B)(1)) vs when common trip is required.
