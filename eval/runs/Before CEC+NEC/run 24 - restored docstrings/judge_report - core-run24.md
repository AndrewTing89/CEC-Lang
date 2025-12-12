# LLM-as-Judge Report - Core Run 24

**Date:** 2025-12-10
**Changes:** Restored tool docstrings + 4 tools added to table_lookup_tools
**Evaluator:** Claude Opus 4.5

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 (baseline-001 missing) |
| Total Score | **193/270** |
| Percentage | **71.5%** |
| Perfect Scores (10/10) | 14 |
| Critical Failures (0-4/10) | 4 |

## Comparison to Previous Runs

| Run | Score | Notes |
|-----|-------|-------|
| Run 21 | 254/280 (90.7%) | Baseline (old tools) |
| Run 22 | 209/280 (74.6%) | New tools + force_nec=True |
| Run 23 | 215/270 (79.6%) | New tools + force_nec=False |
| **Run 24** | **193/270 (71.5%)** | Docstrings restored - **REGRESSED** |

## Critical Issues Found

### 1. inspection-006: WRONG QUESTION ANSWERED (0/10)
- **Question:** Subpanel bonding violations in detached garage
- **Answer Given:** "Required Protection for Kitchen Circuits" (inspection-005 topic!)
- **Root Cause:** Model confused the questions, possibly due to search context pollution

### 2. inspection-007: Wrong Table Values (2/10)
- **Expected:** 40% fill = 0.610 in², 10 AWG THHN = 0.0211 in² → 28-29 conductors
- **Got:** Total area 1.526 in², conductor 0.0437 in² → 13 conductors
- **Tool Used:** `nec_generic_table_raw` (should use `nec_conduit_fill_calculator`)

### 3. inspection-009: Wrong Correction Factors (2/10)
- **Expected:** Temp=0.71, Bundling=0.80 → 11.36A
- **Got:** Temp=0.58, Bundling=0.50 → 5.8A
- **Tool Used:** `cec_search` only (should use ampacity tools)

### 4. baseline-005: Wrong Aluminum Size (3/10)
- **Expected:** 4/0 AWG aluminum for 200A
- **Got:** 2/0 AWG aluminum (incorrect)

## Score Breakdown by Question

### Perfect Scores (10/10) - 14 questions
- baseline-002, baseline-004, baseline-006, baseline-007, baseline-008
- core-001, core-006, core-007, core-009, core-011, core-012
- inspection-010

### High Scores (8-9/10) - 5 questions
- baseline-003 (8): Missing dishwasher GFCI
- core-002 (9): Minor wording difference
- core-003 (9): Listed most GFCI locations
- inspection-001 (9): Slight calculation variation
- inspection-005 (8): Protection details mostly correct

### Medium Scores (5-7/10) - 4 questions
- core-004 (7): Wrong claim about NEC not requiring SPD
- core-008 (5): Wrong System Bonding Jumper definition
- core-010 (7): Wrong temp correction factor (0.71 vs 0.82)
- inspection-002 (5): Wrong depth (30" vs 36")
- inspection-008 (5): Wrong resistance value used

### Critical Failures (0-4/10) - 4 questions
- baseline-005 (3): Wrong aluminum size (2/0 vs 4/0)
- core-005 (4): Wrong depth (30" vs 36"), missing closet prohibition
- inspection-006 (0): **ANSWERED WRONG QUESTION**
- inspection-007 (2): Wrong conduit fill values
- inspection-009 (2): Wrong temperature/bundling factors

## Tool Selection Analysis

| Question | Tool(s) Used | Correct? |
|----------|--------------|----------|
| baseline-002 | `cec_lookup_conductor_size` | ✓ |
| baseline-006 | `cec_lookup_working_space` | ✓ |
| core-010 | `cec_base_ampacity` | ✓ (NEW!) |
| inspection-008 | `cec_lookup_conductor_resistance` + `cec_search` | ✓ (NEW!) |
| inspection-010 | `nec_lookup_grounding_conductor` | ✓ |
| inspection-007 | `nec_generic_table_raw` | ❌ (should be `nec_conduit_fill_calculator`) |
| inspection-009 | `cec_search` | ❌ (should use ampacity tools) |

**Tool routing improved** for core-010 and inspection-008, but inspection-007 and inspection-009 still use wrong tools.

## Conclusions

1. **Docstring restoration did NOT fix tool routing** - inspection-007 and inspection-009 still use generic tools
2. **Critical regression:** inspection-006 answered completely wrong question (0/10)
3. **Score dropped** from 79.6% (Run 23) to 71.5% (Run 24)
4. **Tool improvements:** core-010 and inspection-008 now use specialized tools

## Recommendations

1. Investigate why inspection-006 answered wrong question (context pollution?)
2. Verify `nec_conduit_fill_calculator` docstring has proper "conduit fill" triggers
3. Consider adding explicit routing in SYSTEM_PROMPT for these problematic questions
4. Check if memory/context between questions is causing confusion
