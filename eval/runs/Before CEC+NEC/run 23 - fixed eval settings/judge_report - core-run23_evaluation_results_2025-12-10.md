# Judge Report - core-run23_evaluation_results_2025-12-10

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | CEC Agent (qwen/qwen3-32b) |
| **Source File** | core-run23_evaluation_results_2025-12-10.md |
| **Judge** | Claude Code (Opus) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-10 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 27 (baseline-001 missing from parser) |
| **Total Score** | **215/270** |
| **Percentage** | **79.6%** |
| **Perfect Scores (10/10)** | 14 |
| **Imperfect Scores (<10)** | 13 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 14 |
| High (8-9/10) | 6 |
| Medium (5-7/10) | 4 |
| Low (0-4/10) | 3 |

---

## All Evaluations
| ID | Accuracy | Completeness | Total | Notes |
|----|----------|--------------|-------|-------|
| baseline-002 | 5/5 | 5/5 | **10/10** | Correct: 6 AWG copper |
| baseline-003 | 5/5 | 4/5 | **9/10** | Missing dishwasher GFCI mention |
| baseline-004 | 5/5 | 5/5 | **10/10** | Correct AFCI requirements |
| baseline-005 | 1/5 | 2/5 | **3/10** | WRONG: Says 2/0 aluminum, should be 4/0 |
| baseline-006 | 5/5 | 5/5 | **10/10** | Correct: 3 feet (36 inches) |
| baseline-007 | 5/5 | 5/5 | **10/10** | Correct: 2 circuits |
| baseline-008 | 5/5 | 5/5 | **10/10** | Correct: SPD required per 230.67 |
| core-001 | 1/5 | 2/5 | **3/10** | WRONG: AC load calculation error (48,000 VA instead of 4,600 VA) |
| core-002 | 5/5 | 4/5 | **9/10** | Missing explicit 210.4(D) grouping mention |
| core-003 | 5/5 | 4/5 | **9/10** | Comprehensive but missing "unfinished basements" specifically |
| core-004 | 5/5 | 5/5 | **10/10** | Correct SPD requirements and installation |
| core-005 | 2/5 | 2/5 | **4/10** | WRONG: Says 30" depth (should be 36"), missing 240.24(D) closet prohibition |
| core-006 | 5/5 | 5/5 | **10/10** | Correct violation per 110.14(A)/408.41 |
| core-007 | 4/5 | 4/5 | **8/10** | Good but incorrectly says GE not required (250.32 may require it) |
| core-008 | 5/5 | 5/5 | **10/10** | Excellent MBJ vs SBJ explanation |
| core-009 | 3/5 | 4/5 | **7/10** | WRONG: "6 feet" limitation is incorrect for dining room |
| core-010 | 2/5 | 3/5 | **5/10** | WRONG: Temp factor 0.71 (should be 0.82 for 90°C conductor) |
| core-011 | 5/5 | 5/5 | **10/10** | Correct AFCI explanation |
| core-012 | 5/5 | 5/5 | **10/10** | Correct torque requirements per 110.14(D) |
| inspection-001 | 4/5 | 4/5 | **8/10** | Good calculation, slightly different result (124.8A vs 103.2A expected) |
| inspection-002 | 2/5 | 2/5 | **4/10** | WRONG: Says 30" depth (should be 36"), wrong height interpretation |
| inspection-005 | 3/5 | 4/5 | **7/10** | Over-protective (says all need combo AFCI/GFCI) |
| inspection-006 | 5/5 | 5/5 | **10/10** | Correct bonding violations identified |
| inspection-007 | 1/5 | 1/5 | **2/10** | WRONG: 15 conductors (should be 28-29), used wrong table values |
| inspection-008 | 5/5 | 5/5 | **10/10** | Correct: 2.84V, 2.37% |
| inspection-009 | 1/5 | 1/5 | **2/10** | WRONG: Factors 0.58/0.50 (should be 0.71/0.80), result 5.8A (should be 11.36A) |
| inspection-010 | 5/5 | 5/5 | **10/10** | Correct: 2/0 AWG copper GEC |

---

## Comparison to Previous Runs

| Run | Score | Perfect | Key Changes |
|-----|-------|---------|-------------|
| Run 21 | 254/280 (90.7%) | 22 | force_nec_comparison=False, OLD tools |
| Run 22 | 209/280 (74.6%) | 14 | force_nec_comparison=True, NEW tools |
| Run 23 | 215/270 (79.6%) | 14 | force_nec_comparison=False, NEW tools |

**Observation:** Run 23 is slightly better than Run 22 (+5 points), but still significantly worse than Run 21 (-39 points from 27 questions). The tool refactoring appears to have introduced regressions independent of the NEC comparison setting.

---

## Critical Issues Identified

### 1. Working Space Depth Systematic Error
Model inconsistently reports 30" instead of 36":
- baseline-006: Correctly says 3 feet ✓
- core-005: Wrong - says 30 inches ✗
- inspection-002: Wrong - says 30 inches ✗

### 2. Table Lookup Still Failing
- inspection-007: Used `nec_generic_table_raw` instead of specialized conduit fill calculator
- Got wrong values: 0.0437 in² per conductor (should be 0.0211)
- Result: 15 conductors instead of 28-29

### 3. Ampacity Adjustment Factors Still Wrong
- core-010: Used 0.71 temp factor for 90°C conductor (should be 0.82)
- inspection-009: Used 0.58/0.50 factors (should be 0.71/0.80)
