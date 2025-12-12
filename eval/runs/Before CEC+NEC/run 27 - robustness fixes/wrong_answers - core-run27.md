# Wrong Answers - core-run27

**Model:** CEC Lang Agent (qwen/qwen3-32b)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 90.7% (245/270)

---

## Executive Summary
**Questions with Errors:** 6 of 27
**Perfect Scores:** 21

---

## Detailed Error Analysis (6 questions)

### 1. core-005 (Score: 3/10) - CRITICAL ERROR

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected Answer:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 110.26(B).

**Model Answer:** "The installation **meets NEC requirements**... Required Working Space Depth: **300 mm (12 inches)** per NEC Table 110.26(A)(1) for Condition 2."

**Accuracy:** 1/5 - Completely wrong conclusion
**Completeness:** 2/5 - Missed multiple violations

**Specific Errors:**
- Used incorrect depth requirement (12" instead of 36")
- Misinterpreted voltage condition - residential panels are 120/240V which requires 36" minimum
- Stated "300mm (12 inches)" but Table 110.26(A)(1) requires 900mm (36") for 0-150V systems
- Failed to identify clothes closet prohibition per 240.24(D)
- Failed to identify water heater as obstruction in working space

**Root Cause:** The `nec_lookup_working_space` tool returned data for the wrong condition or the model misinterpreted the lookup results. The model used "Condition 2" for a 120V system but the standard residential panel is 120/240V.

---

### 2. inspection-001 (Score: 7/10)

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected Answer:** General lighting: 9000 VA. Apply Table 220.42 demand: first 3000 VA at 100% = 3000 VA, remaining at 35% = 3675 VA. Subtotal: 6675 VA. Range: 8000 VA. Dryer: 5500 VA. AC: 4600 VA. Total: 24,775 VA = 103.2A. 200A adequate.

**Model Answer:** General load calculated as 9,600 VA with different demand application. Total: 27,400 VA = 114.17A. Conclusion: 200A adequate.

**Accuracy:** 3/5 - Correct conclusion but calculation differs
**Completeness:** 4/5 - Shows work but wrong methodology

**Specific Errors:**
- Did not correctly apply Table 220.42 demand factors
- Added small appliance (3000 VA) and laundry (1500 VA) to subtotal before applying demand factors to general lighting only
- Result is 114.17A vs expected 103.2A (~10% difference)
- Final answer correct (200A is adequate) but methodology was imprecise

**Root Cause:** The model used a simplified calculation method rather than strictly following Article 220 Part III demand factor tables.

---

### 3. inspection-005 (Score: 7/10)

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected Answer:** Per NEC 2023, ALL circuits require GFCI+AFCI because 210.8(A)(5) was expanded to cover ALL kitchen receptacles including dedicated appliance circuits.

**Model Answer:** Countertop, dishwasher, disposal: GFCI+AFCI. **Refrigerator: Standard breaker only** (claims GFCI Exception per 210.8(A)(4) Exception No. 2 and AFCI exception per 210.12(B)).

**Accuracy:** 3/5 - Wrong on refrigerator circuit
**Completeness:** 4/5 - Covers all circuits but incorrect on one

**Specific Errors:**
- Claims refrigerator is exempt from GFCI per "210.8(A)(4) Exception No. 2" - this exception is for garage receptacles, not kitchen
- Claims refrigerator is exempt from AFCI per "210.12(B)" - this section doesn't provide a blanket refrigerator exemption
- NEC 2023 Section 210.8(A)(5) "Kitchens" requires GFCI for ALL receptacles including dedicated appliance circuits
- The referenced exceptions do not apply to kitchen refrigerators

**Root Cause:** The model incorrectly applied exceptions meant for other locations (garage) to the kitchen context. The NEC search may have returned exception language without proper context filtering.

---

### 4. baseline-003 (Score: 9/10)

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected Answer:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**Model Answer:** "GFCI protection is required for all 125-250V receptacles installed to serve countertop surfaces in residential kitchens" per 210.8(A)(6).

**Accuracy:** 4/5 - Missing dishwasher mention
**Completeness:** 5/5 - Thorough on countertops

**Specific Errors:**
- Did not explicitly mention dishwasher GFCI requirement
- Expected answer specifically calls out dishwasher protection

**Root Cause:** Minor omission - the answer focused on countertop surfaces per 210.8(A)(6) but didn't extend to the dishwasher requirement.

---

### 5. core-007 (Score: 9/10)

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected Answer:** Grounds and neutrals must be SEPARATED. NO main bonding jumper in subpanel. Neutral bar must be isolated. Equipment grounding conductor must be bonded to enclosure. A grounding electrode may be required per 250.32 for detached buildings.

**Model Answer:** Covers separation correctly. States "subpanel **does not require a local grounding electrode**" - this is potentially incorrect.

**Accuracy:** 4/5 - Questionable on grounding electrode requirement
**Completeness:** 5/5 - Very thorough

**Specific Errors:**
- Stated grounding electrode "not required" but per 250.32(A), grounding electrodes are often required for detached structures
- The expected answer correctly notes a grounding electrode "may be required" per 250.32

**Root Cause:** Oversimplified the grounding electrode requirement. The code allows certain exceptions but a blanket "not required" statement is incorrect.

---

### 6. Missing Question: baseline-001

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected Answer:** 20 amperes

**Model Response:** NOT EVALUATED (question was not included in the evaluation run)

**Impact:** This is a baseline question that should have been included. The evaluation ran 27 questions instead of the expected 28.

---

## Summary of Error Categories

| Category | Count | Impact |
|----------|-------|--------|
| **Wrong table/condition interpretation** | 1 | Critical (core-005) |
| **Incorrect exception application** | 1 | Significant (inspection-005) |
| **Calculation methodology** | 1 | Moderate (inspection-001) |
| **Minor omission** | 2 | Minor (baseline-003, core-007) |
| **Missing question** | 1 | N/A (baseline-001) |

---

## Recommendations

1. **core-005 FIX (Critical):** Review `nec_lookup_working_space` tool to ensure correct voltage categorization. 120/240V panels should return 36" (900mm) requirement, not 12" (300mm). The tool may be confusing "Condition 1/2/3" with voltage categories.

2. **inspection-005 FIX:** Update NEC 2023 knowledge base to reflect expanded 210.8(A)(5) "Kitchens" coverage. Remove outdated exception references that don't apply to kitchen refrigerators.

3. **inspection-001 FIX:** Add explicit Article 220 calculation guidance to ensure demand factors are applied correctly per Table 220.42.

4. **baseline-001 FIX:** Investigate why this question was missing from the evaluation run.

---

## Comparison with Run 26

| Metric | Run 26 | Run 27 | Change |
|--------|--------|--------|--------|
| Total Score | 257/270 (95.2%) | 245/270 (90.7%) | -4.5% |
| Perfect Scores | 22 | 21 | -1 |
| Critical Errors | 0 | 1 | +1 |

**Note:** Run 27 shows a regression from Run 26, primarily due to the critical error on core-005 (working space requirements). The robustness fixes may have inadvertently changed behavior for this question type.

---

*Report Generated: 2025-12-10*
*Judge: Claude Code (Opus 4.5) - LLM-as-Judge Method*
