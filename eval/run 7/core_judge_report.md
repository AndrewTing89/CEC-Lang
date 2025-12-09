# LLM Judge Report: Core Evaluation (Run 7 - Multi-Run)

## Summary
- Total Questions: 28
- Accurate: 22/28 (78.6%)
- Partially Accurate: 6/28 (21.4%)
- Inaccurate: 0/28 (0.0%)
- Runs per Question: 3
- Aggregation Method: Majority Voting

## Scoring Criteria
- **Accurate**: Answer contains all key facts from expected answer
- **Partially Accurate**: Answer contains some but not all key facts
- **Inaccurate**: Answer is wrong or missing critical information
- **Extra detail beyond expected answer is NOT penalized**

## Results

| ID | Category | Verdict | Consistency | Notes |
|----|----------|---------|-----------|-------|
| baseline-001 | table_lookup | Accurate | 100% | Correct ampacity (20A) and table reference |
| baseline-002 | table_lookup | Accurate | 100% | Correct conductor size (6 AWG copper) |
| baseline-003 | knowledge_simple | Partially Accurate | 100% | Has countertop GFCI but missing dishwasher |
| baseline-004 | knowledge_simple | Accurate | 100% | Correctly states AFCI required for bedrooms |
| baseline-005 | table_lookup | Accurate | 100% | Correct (Yes, 4/0 AWG aluminum) |
| baseline-006 | knowledge_simple | Accurate | 100% | Correct clearance (36 inches / 3 feet / 900mm) |
| baseline-007 | knowledge_simple | Accurate | 100% | Correct (minimum two 20A circuits) |
| baseline-008 | knowledge_simple | Accurate | 100% | Correct - surge protection required per 230.67 |
| core-001 | multi_article | Partially Accurate | 100% | Has some correct sizes |
| core-002 | multi_article | Accurate | 100% | Correct breaker requirements |
| core-003 | nec_2023_updates | Accurate | 100% | Found 11 locations with code reference |
| core-004 | nec_2023_updates | Accurate | 100% | Complete answer with SPD types and locations |
| core-005 | edge_cases | Accurate | 100% | Identifies closet prohibition and other violations |
| core-006 | edge_cases | Accurate | 100% | Correctly identifies as violation |
| core-007 | grounding_bonding | Partially Accurate | 100% | Has separation but missing MBJ detail |
| core-008 | grounding_bonding | Accurate | 100% | Correctly explains both MBJ and SBJ |
| core-009 | load_calculations | Accurate | 100% | Correct - two circuits, can serve dining room |
| core-010 | load_calculations | Partially Accurate | 100% | Has one factor, may be missing the other |
| core-011 | why_questions | Accurate | 100% | Good explanation of AFCI purpose |
| core-012 | why_questions | Accurate | 100% | Correct references and explanation |
| inspection-001 | panel_load_calculation | Accurate | 100% | 200A panel adequate with demand factor calculation |
| inspection-002 | clearance_violations | Accurate | 100% | Identifies depth and water heater violations |
| inspection-005 | gfci_afci_compliance | Partially Accurate | 100% | Found 4 correct requirements |
| inspection-006 | subpanel_violations | Partially Accurate | 100% | Identifies some violations |
| inspection-007 | conduit_fill | Accurate | 100% | Correct conductor count with table references |
| inspection-008 | voltage_drop | Accurate | 100% | Correct voltage drop calculation and conclusion |
| inspection-009 | derating_calculation | Accurate | 100% | Correct derating calculation (20A x 0.71 x 0.80 = 11.36A) |
| inspection-010 | grounding_electrode_conductor | Accurate | 100% | Correct GEC size (2/0 AWG copper) |


## Detailed Analysis

### Issues Found

**No Inaccurate Answers!**

**Partially Accurate Answers (6):**
- baseline-003: Has countertop GFCI but missing dishwasher (Consistency: 100%)
- core-001: Has some correct sizes (Consistency: 100%)
- core-007: Has separation but missing MBJ detail (Consistency: 100%)
- core-010: Has one factor, may be missing the other (Consistency: 100%)
- inspection-005: Found 4 correct requirements (Consistency: 100%)
- inspection-006: Identifies some violations (Consistency: 100%)


### Strengths

**Accurate Answers (22/28 = 78.6%):**
- baseline-001: Correct ampacity (20A) and table reference
- baseline-002: Correct conductor size (6 AWG copper)
- baseline-004: Correctly states AFCI required for bedrooms
- baseline-005: Correct (Yes, 4/0 AWG aluminum)
- baseline-006: Correct clearance (36 inches / 3 feet / 900mm)
- baseline-007: Correct (minimum two 20A circuits)
- baseline-008: Correct - surge protection required per 230.67
- core-002: Correct breaker requirements
- core-003: Found 11 locations with code reference
- core-004: Complete answer with SPD types and locations
- core-005: Identifies closet prohibition and other violations
- core-006: Correctly identifies as violation
- core-008: Correctly explains both MBJ and SBJ
- core-009: Correct - two circuits, can serve dining room
- core-011: Good explanation of AFCI purpose
- core-012: Correct references and explanation
- inspection-001: 200A panel adequate with demand factor calculation
- inspection-002: Identifies depth and water heater violations
- inspection-007: Correct conductor count with table references
- inspection-008: Correct voltage drop calculation and conclusion
- inspection-009: Correct derating calculation (20A x 0.71 x 0.80 = 11.36A)
- inspection-010: Correct GEC size (2/0 AWG copper)


## Score Distribution by Category

| Category | Questions | Accurate | Partial | Inaccurate | Success Rate |
|----------|-----------|----------|---------|------------|--------------|
| clearance_violations | 1 | 1 | 0 | 0 | 100.0% |
| conduit_fill | 1 | 1 | 0 | 0 | 100.0% |
| derating_calculation | 1 | 1 | 0 | 0 | 100.0% |
| edge_cases | 2 | 2 | 0 | 0 | 100.0% |
| gfci_afci_compliance | 1 | 0 | 1 | 0 | 100.0% |
| grounding_bonding | 2 | 1 | 1 | 0 | 100.0% |
| grounding_electrode_conductor | 1 | 1 | 0 | 0 | 100.0% |
| knowledge_simple | 5 | 4 | 1 | 0 | 100.0% |
| load_calculations | 2 | 1 | 1 | 0 | 100.0% |
| multi_article | 2 | 1 | 1 | 0 | 100.0% |
| nec_2023_updates | 2 | 2 | 0 | 0 | 100.0% |
| panel_load_calculation | 1 | 1 | 0 | 0 | 100.0% |
| subpanel_violations | 1 | 0 | 1 | 0 | 100.0% |
| table_lookup | 3 | 3 | 0 | 0 | 100.0% |
| voltage_drop | 1 | 1 | 0 | 0 | 100.0% |
| why_questions | 2 | 2 | 0 | 0 | 100.0% |


## Consistency Analysis

| Consistency Level | Count | Percentage |
|-------------------|-------|------------|
| High (100%) | 28 | 100.0% |
| Medium (50-99%) | 0 | 0.0% |
| Low (<50%) | 0 | 0.0% |



## Comparison to Run 6

### Run 6 Results:
- Accurate: 21/28 (75.0%)
- Partially Accurate: 7/28 (25.0%)
- Inaccurate: 0/28 (0.0%)

### Run 7 Results (Multi-Run Averaged):
- Accurate: 22/28 (78.6%)
- Partially Accurate: 6/28 (21.4%)
- Inaccurate: 0/28 (0.0%)

## Overall Assessment

The Core agent achieved:
- **22/28 Accurate** (78.6%)
- **6/28 Partially Accurate** (21.4%)
- **0/28 Inaccurate** (0.0%)

**Success Rate (Accurate + Partial)**: 100.0%

---
*Report Generated: Run 7 (Multi-Run Evaluation)*
*Evaluation Set: Core Evaluation - 28 Questions*
