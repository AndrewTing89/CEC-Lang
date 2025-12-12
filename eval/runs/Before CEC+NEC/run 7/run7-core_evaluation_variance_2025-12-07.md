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
| baseline-001 | table_lookup | PASS | 11.0s |
| baseline-002 | table_lookup | PASS | 21.7s |
| baseline-003 | knowledge_simple | PASS | 11.1s |
| baseline-004 | knowledge_simple | PASS | 8.9s |
| baseline-005 | table_lookup | PASS | 11.0s |
| baseline-006 | knowledge_simple | PASS | 10.8s |
| baseline-007 | knowledge_simple | PASS | 10.0s |
| baseline-008 | knowledge_simple | PASS | 10.9s |
| core-001 | multi_article | PASS | 15.3s |
| core-002 | multi_article | PASS | 23.8s |
| core-003 | nec_2023_updates | PASS | 16.1s |
| core-004 | nec_2023_updates | PASS | 21.4s |
| core-005 | edge_cases | PASS | 13.8s |
| core-006 | edge_cases | PASS | 9.4s |
| core-007 | grounding_bonding | PASS | 13.4s |
| core-008 | grounding_bonding | PASS | 10.4s |
| core-009 | load_calculations | PASS | 10.1s |
| core-010 | load_calculations | PASS | 23.0s |
| core-011 | why_questions | PASS | 17.2s |
| core-012 | why_questions | PASS | 10.4s |
| inspection-001 | panel_load_calculation | PASS | 21.2s |
| inspection-002 | clearance_violations | PASS | 17.6s |
| inspection-005 | gfci_afci_compliance | PASS | 15.9s |
| inspection-006 | subpanel_violations | PASS | 11.9s |
| inspection-007 | conduit_fill | PASS | 17.8s |
| inspection-008 | voltage_drop | PASS | 26.5s |
| inspection-009 | derating_calculation | PASS | 12.5s |
| inspection-010 | grounding_electrode_conductor | PASS | 15.7s |


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
*Report Generated: 2025-12-07 15:37*
*Runs per Question: 3*
