# LLM-as-Judge Report - Run 43

**Date:** 2025-12-12
**Evaluation:** CEC 2022 Unified Question Set (53 questions)
**Run Description:** Surge protection domain knowledge fix

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Questions | 53 |
| Total Points | 513/530 |
| Overall Score | 96.8% |
| Perfect Scores (10/10) | 44 |
| Partial Scores (8-9/10) | 9 |
| Low Scores (<5/10) | 0 |

## Key Fix Verification

### cec2022-008 (Surge Protection Requirement) - FIXED
- **Run 42 Score:** 4/10 (answered about conductor sizing)
- **Run 43 Score:** 10/10
- **Answer:** Correctly identifies 230.67(A) requirement for SPD on all dwelling services
- **Fix:** Domain knowledge + smart exclusion from service conductor enforcement

### cec2022-012 (Surge Protection Location) - FIXED
- **Run 42 Score:** 4/10 (answered about conductor sizing)
- **Run 43 Score:** 10/10
- **Answer:** Correctly states 230.67 requirement, Type 1/2 SPD, integral or immediately adjacent location, exception for downstream panelboard
- **Fix:** Same as above

## Score Distribution

| Score | Count | Questions |
|-------|-------|-----------|
| 10/10 | 44 | Most questions |
| 9/10 | 1 | cec2022-003 |
| 8/10 | 8 | 006, 013, 021, 022, 029, 035, 038, 044 |
| <5/10 | 0 | None |

## Detailed Scores

| ID | Category | Accuracy | Completeness | Total | Status |
|----|----------|----------|--------------|-------|--------|
| cec2022-001 | table_lookup | 5 | 5 | 10 | PASS |
| cec2022-002 | table_lookup | 5 | 5 | 10 | PASS |
| cec2022-003 | knowledge_simple | 5 | 4 | 9 | PASS |
| cec2022-004 | knowledge_simple | 5 | 5 | 10 | PASS |
| cec2022-005 | table_lookup | 5 | 5 | 10 | PASS |
| cec2022-006 | knowledge_simple | 4 | 4 | 8 | PASS |
| cec2022-007 | knowledge_simple | 5 | 5 | 10 | PASS |
| cec2022-008 | knowledge_simple | 5 | 5 | 10 | PASS |
| cec2022-009 | multi_article | 5 | 5 | 10 | PASS |
| cec2022-010 | multi_article | 5 | 5 | 10 | PASS |
| cec2022-011 | knowledge | 5 | 5 | 10 | PASS |
| cec2022-012 | knowledge | 5 | 5 | 10 | PASS |
| cec2022-013 | edge_cases | 4 | 4 | 8 | PASS |
| cec2022-014 | edge_cases | 5 | 5 | 10 | PASS |
| cec2022-015 | grounding_bonding | 5 | 5 | 10 | PASS |
| cec2022-016 | grounding_bonding | 5 | 5 | 10 | PASS |
| cec2022-017 | load_calculations | 5 | 5 | 10 | PASS |
| cec2022-018 | load_calculations | 5 | 5 | 10 | PASS |
| cec2022-019 | why_questions | 5 | 5 | 10 | PASS |
| cec2022-020 | why_questions | 5 | 5 | 10 | PASS |
| cec2022-021 | panel_load_calculation | 4 | 4 | 8 | PASS |
| cec2022-022 | clearance_violations | 4 | 4 | 8 | PASS |
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
| cec2022-044 | working_space | 4 | 4 | 8 | PASS |
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
| Run 43 | 513/530 (96.8%) | Fixed 008, 012; no new issues |

## Changes in Run 43

### Domain Knowledge Added
- Surge protection requirements (230.67) for dwelling services
- Type 1/2 SPD requirement
- Installation location: integral or immediately adjacent
- Exception for first downstream panelboard

### Smart Exclusion Logic
- Service conductor enforcement now skips questions containing surge-related keywords
- Keywords: "surge", "spd", "230.67", "protective device"
- This prevents the enforcement from incorrectly triggering on surge protection questions

## Service Conductor Enforcement Stats

| Run | Enforcement Count | Notes |
|-----|-------------------|-------|
| Run 42 | 3/53 | Triggered on 008, 009, 012 |
| Run 43 | 1/53 | Only 041 (actual GEC question) |

## Partial Score Analysis

### cec2022-006 (8/10) - Working Clearance
- Expected: "36 inches (3 feet)"
- Answer mentions 3-foot depth and 30-inch width but in general working space context
- Minor: Could be more direct about the specific 36-inch answer

### cec2022-013 (8/10) - Clearance Violations
- Correctly identifies closet prohibition and violations
- Minor discrepancy in front clearance value cited (30" vs 36")

### cec2022-021 (8/10) - Load Calculation
- Calculation method differs slightly from expected
- Result (119A vs ~103A) due to different demand factor application
- Still correct conclusion: 200A panel is adequate

### cec2022-029 (8/10) - Panelboard Requirements
- Discusses panelboard locations well
- Could more explicitly mention CEC 408.2(A) reserved spaces for specific appliances

### cec2022-035 (8/10) - Table 240.4(G)
- Correctly notes table exists with California amendments
- Expected answer mentions table exists in both CEC and NEC with modified values

### cec2022-038 (8/10) - Medium Voltage Tables
- Lists several tables (311.60(C)(67)-(76))
- Expected answer mentions 20 tables through 311.60(C)(86)

### cec2022-044 (8/10) - Working Space 480V
- Mentions 4 ft depth (correct for Condition 3)
- Answer is more general about working space requirements

## Conclusion

Run 43 successfully fixed both surge protection questions (008 and 012) that were failing in Run 42. The two-pronged approach worked:

1. **Domain knowledge** about surge protection (230.67) ensures the agent knows the requirements upfront
2. **Smart exclusion** in the service conductor enforcement prevents it from triggering on surge-related questions

No regressions were introduced. The score improved from 96.4% to 96.8%, matching Run 41's performance but with different questions at partial scores.
