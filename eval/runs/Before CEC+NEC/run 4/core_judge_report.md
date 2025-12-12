# LLM Judge Report: Core Evaluation (Run 4)

## Summary
- Total Questions: 28
- Accurate: 17/28 (60.7%)
- Partially Accurate: 9/28 (32.1%)
- Inaccurate: 2/28 (7.1%)

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
| baseline-003 | knowledge_simple | Partially Accurate | Incomplete kitchen GFCI requirements |
| baseline-004 | knowledge_simple | Inaccurate | Does not clearly state AFCI is required |
| baseline-005 | table_lookup | Inaccurate | Wrong size (250 kcmil instead of 4/0 AWG) |
| baseline-006 | knowledge_simple | Accurate | Correct clearance (36 inches / 3 feet) |
| baseline-007 | knowledge_simple | Accurate | Correct (minimum two 20A circuits) |
| baseline-008 | knowledge_simple | Partially Accurate | Incomplete answer |
| core-001 | multi_article | Partially Accurate | Check conductor sizes |
| core-002 | multi_article | Partially Accurate | Missing key requirements |
| core-003 | nec_2023_updates | Accurate | Found 9 locations with code reference |
| core-004 | nec_2023_updates | Accurate | Complete answer with SPD types and locations |
| core-005 | edge_cases | Accurate | Identifies closet prohibition and other violations |
| core-006 | edge_cases | Accurate | Correct - violation with code reference |
| core-007 | grounding_bonding | Partially Accurate | Has separation but missing MBJ detail |
| core-008 | grounding_bonding | Partially Accurate | Incomplete comparison |
| core-009 | load_calculations | Accurate | Correct - two circuits, can serve dining room |
| core-010 | load_calculations | Accurate | Correct calculation with all factors |
| core-011 | why_questions | Accurate | Explains arc fault fire prevention |
| core-012 | why_questions | Accurate | Correct references and explanation |
| inspection-001 | panel_load_calculation | Accurate | 200A panel adequate with demand factor calculation |
| inspection-002 | clearance_violations | Accurate | Identifies depth and water heater violations |
| inspection-005 | gfci_afci_compliance | Partially Accurate | Found 4 correct requirements |
| inspection-006 | subpanel_violations | Partially Accurate | Identifies some violations |
| inspection-007 | conduit_fill | Accurate | Correct conductor count with table references |
| inspection-008 | voltage_drop | Accurate | Correct voltage drop calculation and conclusion |
| inspection-009 | derating_calculation | Accurate | Correct derating calculation (20A × 0.71 × 0.80 = 11.36A) |
| inspection-010 | grounding_electrode_conductor | Partially Accurate | Check GEC size per Table 250.66 |


## Detailed Analysis

### Issues Found

**Inaccurate Answers (2):**
- baseline-004 (knowledge_simple): Does not clearly state AFCI is required
- baseline-005 (table_lookup): Wrong size (250 kcmil instead of 4/0 AWG)

**Partially Accurate Answers (9):**
- baseline-003: Incomplete kitchen GFCI requirements
- baseline-008: Incomplete answer
- core-001: Check conductor sizes
- core-002: Missing key requirements
- core-007: Has separation but missing MBJ detail
- core-008: Incomplete comparison
- inspection-005: Found 4 correct requirements
- inspection-006: Identifies some violations
- inspection-010: Check GEC size per Table 250.66


### Strengths

**Accurate Answers (17/28 = 60.7%):**
- baseline-001: Correct ampacity (20A) and table reference
- baseline-002: Correct conductor size (6 AWG copper)
- baseline-006: Correct clearance (36 inches / 3 feet)
- baseline-007: Correct (minimum two 20A circuits)
- core-003: Found 9 locations with code reference
- core-004: Complete answer with SPD types and locations
- core-005: Identifies closet prohibition and other violations
- core-006: Correct - violation with code reference
- core-009: Correct - two circuits, can serve dining room
- core-010: Correct calculation with all factors
- core-011: Explains arc fault fire prevention
- core-012: Correct references and explanation
- inspection-001: 200A panel adequate with demand factor calculation
- inspection-002: Identifies depth and water heater violations
- inspection-007: Correct conductor count with table references
- inspection-008: Correct voltage drop calculation and conclusion
- inspection-009: Correct derating calculation (20A × 0.71 × 0.80 = 11.36A)


## Score Distribution by Category

| Category | Questions | Accurate | Partial | Inaccurate | Success Rate |
|----------|-----------|----------|---------|------------|--------------|
| clearance_violations | 1 | 1 | 0 | 0 | 100.0% |
| conduit_fill | 1 | 1 | 0 | 0 | 100.0% |
| derating_calculation | 1 | 1 | 0 | 0 | 100.0% |
| edge_cases | 2 | 2 | 0 | 0 | 100.0% |
| gfci_afci_compliance | 1 | 0 | 1 | 0 | 100.0% |
| grounding_bonding | 2 | 0 | 2 | 0 | 100.0% |
| grounding_electrode_conductor | 1 | 0 | 1 | 0 | 100.0% |
| knowledge_simple | 5 | 2 | 2 | 1 | 80.0% |
| load_calculations | 2 | 2 | 0 | 0 | 100.0% |
| multi_article | 2 | 0 | 2 | 0 | 100.0% |
| nec_2023_updates | 2 | 2 | 0 | 0 | 100.0% |
| panel_load_calculation | 1 | 1 | 0 | 0 | 100.0% |
| subpanel_violations | 1 | 0 | 1 | 0 | 100.0% |
| table_lookup | 3 | 2 | 0 | 1 | 66.7% |
| voltage_drop | 1 | 1 | 0 | 0 | 100.0% |
| why_questions | 2 | 2 | 0 | 0 | 100.0% |


## Comparison to Run 3

### Run 3 Results (Before Fixes):
- Accurate: 11/28 (39.3%)
- Partially Accurate: 10/28 (35.7%)
- Inaccurate: 7/28 (25.0%)

### Run 4 Results (After Fixes):
- Accurate: 17/28 (60.7%)
- Partially Accurate: 9/28 (32.1%)
- Inaccurate: 2/28 (7.1%)

### Key Improvements Expected:
1. **Table Lookup Errors**: New reverse lookup tools should fix baseline-002, baseline-005, inspection-010
2. **Missing Violations**: Multi-angle scan should catch closet prohibition in core-005
3. **Derating Calculation**: Explicit guidance should fix inspection-009 (0.80 factor for 6 conductors)
4. **Exception Misapplication**: Verification rules should fix inspection-005

## Overall Assessment

The Core agent achieved:
- **17/28 Accurate** (60.7%)
- **9/28 Partially Accurate** (32.1%)
- **2/28 Inaccurate** (7.1%)

**Success Rate (Accurate + Partial)**: 92.9%

---
*Report Generated: Run 4*
*Evaluation Set: Core Evaluation - 28 Questions*
