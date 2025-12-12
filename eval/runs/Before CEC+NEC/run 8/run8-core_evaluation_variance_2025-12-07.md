# Multi-Run Variance Analysis Report

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 28 |
| Runs per Question | 3 |
| High Consistency (100%) | 28 |
| Medium Consistency (50-99%) | 0 |
| Low Consistency (<50%) | 0 |

## Consistency Distribution

### High Consistency Questions (28)

These questions returned the same status across all 3 runs - confident baseline.

| ID | Category | Status | Avg Duration |
|----|----------|--------|--------------|
| baseline-001 | table_lookup | PASS | 17.1s |
| baseline-002 | table_lookup | PASS | 12.3s |
| baseline-003 | knowledge_simple | PASS | 10.0s |
| baseline-004 | knowledge_simple | PASS | 9.3s |
| baseline-005 | table_lookup | PASS | 13.7s |
| baseline-006 | knowledge_simple | PASS | 10.1s |
| baseline-007 | knowledge_simple | PASS | 8.4s |
| baseline-008 | knowledge_simple | PASS | 13.0s |
| core-001 | multi_article | PASS | 18.5s |
| core-002 | multi_article | PASS | 13.1s |
| core-003 | nec_2023_updates | PASS | 28.3s |
| core-004 | nec_2023_updates | PASS | 11.5s |
| core-005 | edge_cases | PASS | 18.7s |
| core-006 | edge_cases | PASS | 9.6s |
| core-007 | grounding_bonding | PASS | 11.5s |
| core-008 | grounding_bonding | PASS | 12.2s |
| core-009 | load_calculations | PASS | 11.8s |
| core-010 | load_calculations | PASS | 14.6s |
| core-011 | why_questions | PASS | 19.7s |
| core-012 | why_questions | PASS | 11.4s |
| inspection-001 | panel_load_calculation | PASS | 31.7s |
| inspection-002 | clearance_violations | PASS | 16.7s |
| inspection-005 | gfci_afci_compliance | PASS | 19.1s |
| inspection-006 | subpanel_violations | PASS | 11.4s |
| inspection-007 | conduit_fill | PASS | 17.4s |
| inspection-008 | voltage_drop | PASS | 23.3s |
| inspection-009 | derating_calculation | PASS | 13.1s |
| inspection-010 | grounding_electrode_conductor | PASS | 17.6s |


### Medium Consistency Questions (0)

These questions had some variance - majority voting applied.

| ID | Category | Majority Status | Breakdown | Notes |
|----|----------|-----------------|-----------|-------|


### Low Consistency Questions (0)

These questions are highly unstable - needs investigation.

| ID | Category | Majority Status | Breakdown | Notes |
|----|----------|-----------------|-----------|-------|


## Overall Statistics

| Metric | Value |
|--------|-------|
| Pass Rate (Aggregated) | 28/28 (100.0%) |
| Average Consistency | 100.0% |
| Questions with 100% Consistency | 28/28 (100.0%) |

## Recommendations

No questions showed critically low consistency.


---
*Report Generated: 2025-12-07 16:50*
*Runs per Question: 3*
