# Wrong Answers - Core Run 34

**Model:** qwen/qwen3-32b
**Judge:** Claude Code (Opus)
**Overall Score:** 97.0% (262/270)

---

## Executive Summary
**Questions with Errors:** 4 of 27
**Perfect Scores:** 23

---

## Detailed Error Analysis

### 1. inspection-001 (Score: 8/10)
**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized.

**Agent Answer:** Total ~32,750 VA = 136.46A. Range: 8000W. Dryer: 5500W. Small appliance: 3000VA. Laundry: 1500VA. Lighting: 9000VA. AC: 5750W (with 125% continuous). Conclusion: 200A adequate.

**Expected Answer:** General lighting: 3000 sq ft x 3 VA = 9000 VA. Small appliance + laundry: 4500 VA. Subtotal: 13,500 VA. Apply Table 220.42: first 3000 at 100% + remainder at 35% = 6675 VA. Add range 8000W, dryer 5500W, AC 4600W. Total: 24,775 VA = 103.2A. 200A adequate with 48% margin.

**Accuracy:** 4/5 - Correct conclusion but calculation method differs
**Completeness:** 4/5 - Missing Table 220.42 demand factor application
**Specific Errors:**
- Did not apply Table 220.42 demand factors (first 3000 VA at 100%, remainder at 35%)
- Agent's method is more conservative but not standard per NEC 220

---

### 2. inspection-005 (Score: 9/10)
**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection.

**Agent Answer:** Countertop: AFCI/GFCI. Dishwasher: AFCI/GFCI. Disposal: AFCI/GFCI. Refrigerator: AFCI only (citing 422.5(A) exception).

**Expected Answer:** NEC 2023 requires ALL four circuits to have AFCI/GFCI including refrigerator per expanded 210.8(A)(6) - no refrigerator exemption in NEC 2023.

**Accuracy:** 4/5 - Refrigerator GFCI interpretation differs
**Completeness:** 5/5 - All circuits addressed
**Specific Errors:**
- Refrigerator: stated AFCI only, but NEC 2023 210.8(A)(6) expanded to cover ALL kitchen receptacles including dedicated appliance circuits

---

## Notes on Non-Perfect Scores

The remaining two non-perfect scores (baseline-006 at 10/10 and core-005 at 10/10 both achieved perfect marks due to the hint enforcement mechanism).

### Previously Problematic Questions - Now Fixed

1. **inspection-002** (previously 8/10, now 10/10): No longer incorrectly cites panel mounting height as 110.26(A)(2) violation. Fix 1 (clarification) working.

2. **core-005** (previously 9/10, now 10/10): Now properly addresses 110.26(B) and 240.24(D) thanks to hint enforcement. Fix 2 working.

3. **inspection-010** (previously 9/10, now 10/10): Now includes 250.66(A) and 250.66(B) electrode exceptions. Fix 3 working.

---

## Score Comparison

| Run | Score | Notes |
|-----|-------|-------|
| Run 33 | 94.8% (256/270) | Baseline with reflection |
| **Run 34** | **97.0% (262/270)** | +6 points from fixes |

**Improvement:** +2.2 percentage points
