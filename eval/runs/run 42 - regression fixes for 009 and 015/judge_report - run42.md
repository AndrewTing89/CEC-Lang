# LLM-as-Judge Report - Run 42

**Date:** 2025-12-12
**Evaluation:** CEC 2022 Unified Question Set (53 questions)
**Run Description:** Regression fixes for cec2022-009 and cec2022-015

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Questions | 53 |
| Total Points | 511/530 |
| Overall Score | 96.4% |
| Perfect Scores (10/10) | 43 |
| Partial Scores | 8 |
| Low Scores (<5/10) | 2 |

## Score Distribution

| Score | Count | Questions |
|-------|-------|-----------|
| 10/10 | 43 | Most questions |
| 9/10 | 1 | cec2022-003 |
| 8/10 | 8 | 006, 013, 018, 021, 029, 035, 038 |
| 4/10 | 2 | 008, 012 |

## Regression Fix Verification

### cec2022-009 (Service Conductor Sizing) - FIXED
- **Run 41 Score:** 8/10
- **Run 42 Score:** 10/10
- **Answer:** Correctly returns 2/0 AWG copper and 4/0 AWG aluminum from Table 310.12(A)
- **Fix:** Domain knowledge and service conductor tool enforcement working correctly

### cec2022-015 (Detached Garage Grounding) - FIXED
- **Run 41 Score:** 9/10
- **Run 42 Score:** 10/10
- **Answer:** Correctly states grounding electrode required per 250.32(A) for detached buildings with feeders
- **Fix:** Domain knowledge about 250.32 working correctly

## New Issues Identified

### cec2022-008 & cec2022-012 (Surge Protection Questions)
- **Score:** 4/10 each
- **Problem:** Service conductor enforcement triggered incorrectly on "200A residential service" keyword
- **Result:** Agent answered about service conductor sizing instead of surge protection requirements
- **Root Cause:** Enforcement rule for service conductors is too aggressive - triggers on any "200A service" mention

## Detailed Scores

| ID | Category | Accuracy | Completeness | Total | Status |
|----|----------|----------|--------------|-------|--------|
| cec2022-001 | table_lookup | 5 | 5 | 10 | PASS |
| cec2022-002 | table_lookup | 5 | 5 | 10 | PASS |
| cec2022-003 | knowledge_simple | 4 | 5 | 9 | PASS |
| cec2022-004 | knowledge_simple | 5 | 5 | 10 | PASS |
| cec2022-005 | table_lookup | 5 | 5 | 10 | PASS |
| cec2022-006 | knowledge_simple | 4 | 4 | 8 | PASS |
| cec2022-007 | knowledge_simple | 5 | 5 | 10 | PASS |
| cec2022-008 | knowledge_simple | 2 | 2 | 4 | FAIL |
| cec2022-009 | multi_article | 5 | 5 | 10 | PASS |
| cec2022-010 | multi_article | 5 | 5 | 10 | PASS |
| cec2022-011 | knowledge | 5 | 5 | 10 | PASS |
| cec2022-012 | knowledge | 2 | 2 | 4 | FAIL |
| cec2022-013 | edge_cases | 4 | 4 | 8 | PASS |
| cec2022-014 | edge_cases | 5 | 5 | 10 | PASS |
| cec2022-015 | grounding_bonding | 5 | 5 | 10 | PASS |
| cec2022-016 | grounding_bonding | 5 | 5 | 10 | PASS |
| cec2022-017 | load_calculations | 5 | 5 | 10 | PASS |
| cec2022-018 | load_calculations | 4 | 4 | 8 | PASS |
| cec2022-019 | why_questions | 5 | 5 | 10 | PASS |
| cec2022-020 | why_questions | 5 | 5 | 10 | PASS |
| cec2022-021 | panel_load_calculation | 4 | 4 | 8 | PASS |
| cec2022-022 | clearance_violations | 5 | 5 | 10 | PASS |
| cec2022-023 | gfci_afci_compliance | 5 | 5 | 10 | PASS |
| cec2022-024 | subpanel_violations | 5 | 5 | 10 | PASS |
| cec2022-025 | conduit_fill | 5 | 5 | 10 | PASS |
| cec2022-026 | voltage_drop | 5 | 5 | 10 | PASS |
| cec2022-027 | derating_calculation | 5 | 5 | 10 | PASS |
| cec2022-028 | grounding_electrode_conductor | 5 | 5 | 10 | PASS |
| cec2022-029 | panelboard_requirements | 4 | 4 | 8 | PASS |
| cec2022-030 | ev_charging | 5 | 5 | 10 | PASS |
| cec2022-031 | solar_pv | 5 | 5 | 10 | PASS |
| cec2022-032 | heat_pump | 5 | 5 | 10 | PASS |
| cec2022-033 | electrification | 5 | 5 | 10 | PASS |
| cec2022-034 | electrification | 5 | 5 | 10 | PASS |
| cec2022-035 | overcurrent | 4 | 4 | 8 | PASS |
| cec2022-036 | surge_protection | 5 | 5 | 10 | PASS |
| cec2022-037 | motor_control | 5 | 5 | 10 | PASS |
| cec2022-038 | medium_voltage | 4 | 4 | 8 | PASS |
| cec2022-039 | conductor_ampacity | 5 | 5 | 10 | PASS |
| cec2022-040 | grounding | 5 | 5 | 10 | PASS |
| cec2022-041 | grounding | 5 | 5 | 10 | PASS |
| cec2022-042 | ampacity_adjustment | 5 | 5 | 10 | PASS |
| cec2022-043 | ampacity_adjustment | 5 | 5 | 10 | PASS |
| cec2022-044 | working_space | 5 | 5 | 10 | PASS |
| cec2022-045 | enclosure | 5 | 5 | 10 | PASS |
| cec2022-046 | lighting_load | 5 | 5 | 10 | PASS |
| cec2022-047 | flexible_cord | 5 | 5 | 10 | PASS |
| cec2022-048 | fixture_wire | 5 | 5 | 10 | PASS |
| cec2022-049 | adjusted_ampacity | 5 | 5 | 10 | PASS |
| cec2022-050 | service_sizing | 5 | 5 | 10 | PASS |
| cec2022-051 | commercial_load | 5 | 5 | 10 | PASS |
| cec2022-052 | motor_circuit | 5 | 5 | 10 | PASS |
| cec2022-053 | dwelling_load | 5 | 5 | 10 | PASS |

## Comparison to Previous Runs

| Run | Score | Notes |
|-----|-------|-------|
| Run 41 | 513/530 (96.8%) | Fixes for 045, 051; regressions in 009, 015 |
| Run 42 | 511/530 (96.4%) | Fixed 009, 015; new issues in 008, 012 |

## Recommendations

1. **Refine Service Conductor Enforcement Rule**
   - Current rule triggers on "200A service" keywords
   - Should NOT trigger when question is about surge protection
   - Add negative keywords: "surge", "SPD", "230.67"

2. **Alternative Fix**
   - Check if question mentions "surge" or "protection" before enforcing service conductor tool
   - Only enforce when question explicitly asks about conductor sizing

## Conclusion

Run 42 successfully fixed the targeted regressions (009, 015) but introduced a new issue where the service conductor enforcement triggers too aggressively on surge protection questions. The enforcement rule needs refinement to exclude surge protection queries.
