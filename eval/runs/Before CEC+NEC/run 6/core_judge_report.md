# LLM Judge Report: Core Evaluation (Run 6)

## Summary
- Total Questions: 28
- Accurate: 21/28 (75.0%)
- Partially Accurate: 7/28 (25.0%)
- Inaccurate: 0/28 (0.0%)

## Scoring Criteria
- **Accurate**: Answer contains all key facts from expected answer
- **Partially Accurate**: Answer contains some but not all key facts
- **Inaccurate**: Answer is wrong or missing critical information
- **Extra detail beyond expected answer is NOT penalized**

## Results

| ID | Category | Verdict | Notes |
|----|----------|---------|-------|
| baseline-001 | table_lookup | Accurate | Correct ampacity (20A) and table reference |
| baseline-002 | table_lookup | Accurate | Correct conductor size (6 AWG copper) |
| baseline-003 | knowledge_simple | Partially Accurate | Has countertop GFCI but missing dishwasher |
| baseline-004 | knowledge_simple | Accurate | Correctly states AFCI required for bedrooms |
| baseline-005 | table_lookup | Accurate | Correct (Yes, 4/0 AWG aluminum) |
| baseline-006 | knowledge_simple | Accurate | Correct clearance (36 inches / 3 feet / 900mm) |
| baseline-007 | knowledge_simple | Accurate | Correct (minimum two 20A circuits) |
| baseline-008 | knowledge_simple | Accurate | Correct - surge protection required per 230.67 |
| core-001 | multi_article | Accurate | Correct sizes and confirms aluminum permitted |
| core-002 | multi_article | Partially Accurate | Missing key requirements |
| core-003 | nec_2023_updates | Accurate | Found 10 locations with code reference |
| core-004 | nec_2023_updates | Accurate | Complete answer with SPD types and locations |
| core-005 | edge_cases | Partially Accurate | Found 1 violation(s), may be missing closet prohibition |
| core-006 | edge_cases | Accurate | Correct - violation with code reference |
| core-007 | grounding_bonding | Partially Accurate | Has separation but missing MBJ detail |
| core-008 | grounding_bonding | Accurate | Correctly explains both MBJ and SBJ |
| core-009 | load_calculations | Accurate | Correct - two circuits, can serve dining room |
| core-010 | load_calculations | Accurate | Correct calculation with all factors |
| core-011 | why_questions | Accurate | Good explanation of AFCI purpose |
| core-012 | why_questions | Accurate | Correct references and explanation |
| inspection-001 | panel_load_calculation | Accurate | 200A panel adequate with demand factor calculation |
| inspection-002 | clearance_violations | Accurate | Identifies depth and water heater violations |
| inspection-005 | gfci_afci_compliance | Partially Accurate | Found 4 correct requirements |
| inspection-006 | subpanel_violations | Accurate | Identifies neutral bonding and MBJ violations |
| inspection-007 | conduit_fill | Accurate | Correct conductor count (28-29) |
| inspection-008 | voltage_drop | Partially Accurate | Check voltage drop calculation |
| inspection-009 | derating_calculation | Accurate | Correct derating calculation (20A x 0.71 x 0.80 = 11.36A) |
| inspection-010 | grounding_electrode_conductor | Partially Accurate | Check GEC size per Table 250.66 |


## Detailed Analysis

### Issues Found

**No Inaccurate Answers!**

**Partially Accurate Answers (7):**
- baseline-003: Has countertop GFCI but missing dishwasher
- core-002: Missing key requirements
- core-005: Found 1 violation(s), may be missing closet prohibition
- core-007: Has separation but missing MBJ detail
- inspection-005: Found 4 correct requirements
- inspection-008: Check voltage drop calculation
- inspection-010: Check GEC size per Table 250.66


### Strengths

**Accurate Answers (21/28 = 75.0%):**
- baseline-001: Correct ampacity (20A) and table reference
- baseline-002: Correct conductor size (6 AWG copper)
- baseline-004: Correctly states AFCI required for bedrooms
- baseline-005: Correct (Yes, 4/0 AWG aluminum)
- baseline-006: Correct clearance (36 inches / 3 feet / 900mm)
- baseline-007: Correct (minimum two 20A circuits)
- baseline-008: Correct - surge protection required per 230.67
- core-001: Correct sizes and confirms aluminum permitted
- core-003: Found 10 locations with code reference
- core-004: Complete answer with SPD types and locations
- core-006: Correct - violation with code reference
- core-008: Correctly explains both MBJ and SBJ
- core-009: Correct - two circuits, can serve dining room
- core-010: Correct calculation with all factors
- core-011: Good explanation of AFCI purpose
- core-012: Correct references and explanation
- inspection-001: 200A panel adequate with demand factor calculation
- inspection-002: Identifies depth and water heater violations
- inspection-006: Identifies neutral bonding and MBJ violations
- inspection-007: Correct conductor count (28-29)
- inspection-009: Correct derating calculation (20A x 0.71 x 0.80 = 11.36A)


## Score Distribution by Category

| Category | Questions | Accurate | Partial | Inaccurate | Success Rate |
|----------|-----------|----------|---------|------------|--------------|
| clearance_violations | 1 | 1 | 0 | 0 | 100.0% |
| conduit_fill | 1 | 1 | 0 | 0 | 100.0% |
| derating_calculation | 1 | 1 | 0 | 0 | 100.0% |
| edge_cases | 2 | 1 | 1 | 0 | 100.0% |
| gfci_afci_compliance | 1 | 0 | 1 | 0 | 100.0% |
| grounding_bonding | 2 | 1 | 1 | 0 | 100.0% |
| grounding_electrode_conductor | 1 | 0 | 1 | 0 | 100.0% |
| knowledge_simple | 5 | 4 | 1 | 0 | 100.0% |
| load_calculations | 2 | 2 | 0 | 0 | 100.0% |
| multi_article | 2 | 1 | 1 | 0 | 100.0% |
| nec_2023_updates | 2 | 2 | 0 | 0 | 100.0% |
| panel_load_calculation | 1 | 1 | 0 | 0 | 100.0% |
| subpanel_violations | 1 | 1 | 0 | 0 | 100.0% |
| table_lookup | 3 | 3 | 0 | 0 | 100.0% |
| voltage_drop | 1 | 0 | 1 | 0 | 100.0% |
| why_questions | 2 | 2 | 0 | 0 | 100.0% |


## Comparison to Run 5

### Run 5 Results:
- Accurate: 22/28 (78.6%)
- Partially Accurate: 6/28 (21.4%)
- Inaccurate: 0/28 (0.0%)

### Run 6 Results (After Run 6 Fixes):
- Accurate: 21/28 (75.0%)
- Partially Accurate: 7/28 (25.0%)
- Inaccurate: 0/28 (0.0%)

### Key Fixes Applied:
1. **Article Selection Guide**: Added guidance to search correct articles
2. **Tool Result Enforcement**: Stronger enforcement to use CEC tool values over training data
3. **List Enumeration**: Guidance to use higher search limits for list questions
4. **Completeness Check**: Checklist to verify all parts of multi-part questions answered

## Overall Assessment

The Core agent achieved:
- **21/28 Accurate** (75.0%)
- **7/28 Partially Accurate** (25.0%)
- **0/28 Inaccurate** (0.0%)

**Success Rate (Accurate + Partial)**: 100.0%

---
*Report Generated: Run 6*
*Evaluation Set: Core Evaluation - 28 Questions*
