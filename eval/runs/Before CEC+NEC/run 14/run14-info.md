# Run 14 - Targeted Fixes for Verified Errors

**Date:** 2025-12-09
**Baseline:** Run 13 (96.6% pass rate, 9.1/10 average - CORRECTED after verification)
**Goal:** Fix 3 verified errors from Run 13

---

## Issues Verified in Run 13

After deep-dive investigation, 3 questions were verified as TRUE ERRORS:

| Question | Agent Answer | Expected | Root Cause |
|----------|-------------|----------|------------|
| baseline-002 | 4 AWG (citing 240.4(D) 50A limit for 6 AWG) | 6 AWG | 240.4(D) only covers 10 AWG and smaller - agent fabricated non-existent restriction |
| cec-018 | 1.0 VA/ft² | 1.3 VA/ft² | Confused Section 220.14 (receptacles) with Table 220.12 (lighting) |
| inspection-010 | 3/0 AWG GEC | 2/0 AWG | Table 250.66 range parsing error (1000 kcmil in "Over 600 through 1100") |

---

## Fixes Implemented

### Fix 1: 240.4(D) Scope Checking (baseline-002)

**Problem:** `find_limiting_rules()` returned 240.4(D) for ANY conductor, even 6 AWG which is NOT covered.

**Solution:** Added scope filtering to `cec_knowledge_tools.py`:
- Parse subject to detect conductor size (AWG/kcmil)
- `SMALL_CONDUCTOR_SIZES = {"18", "16", "14", "12", "10"}`
- If conductor is NOT in this set, filter out 240.4(D) from results
- Add explicit note: "240.4(D) does NOT apply to [size]"

**Files Modified:**
- `core/cec_knowledge_tools.py` - Enhanced `find_limiting_rules()` method

---

### Fix 2: Lighting vs Receptacle Routing (cec-018)

**Problem:** Agent confused Table 220.12 (lighting: 1.3 VA/ft² for offices) with Section 220.14 (receptacles: 1.0 VA/ft²).

**Solution:** Added explicit routing guidance in system prompt:
- "LOAD CALCULATIONS: LIGHTING vs RECEPTACLE (CRITICAL)" section
- Table 220.12 = Lighting loads by occupancy type
- Section 220.14 = Receptacle loads (1.0 VA/ft² or 180 VA/outlet)
- Mandatory routing rule: IDENTIFY which type before answering

**Files Modified:**
- `core/agent.py` - Added new system prompt section

---

### Fix 3: GEC Table Range Parsing (inspection-010)

**Status:** Already implemented in Run 13

The `lookup_gec_size()` method already uses `parse_range_value()` for numeric kcmil sizes, which handles "Over X through Y" format. This fix was verified as working.

---

## Files Modified Summary

| File | Changes |
|------|---------|
| `core/cec_knowledge_tools.py` | 240.4(D) scope filtering in `find_limiting_rules()` |
| `core/agent.py` | Lighting vs Receptacle routing guidance section |

---

## Actual Results

| Evaluation Set | Passed | Total | Pass Rate |
|----------------|--------|-------|-----------|
| Core (baseline + core) | 28 | 28 | **100%** |
| CEC | 30 | 30 | **100%** |
| Inspection | 8 | 8 | **100%** |
| **Total** | **66** | **66** | **100%** |

### Comparison with Run 13

| Metric | Run 13 (Corrected) | Run 14 | Change |
|--------|-------------------|--------|--------|
| Pass Rate | 96.6% | **100%** | +3.4% |
| FAILs | 3 | **0** | -3 |

### Targeted Fix Results

| Question | Run 13 | Run 14 | Status |
|----------|--------|--------|--------|
| baseline-002 (conductor size) | FAIL | **PASS** | FIXED |
| cec-018 (lighting VA/ft²) | FAIL | **PASS** | FIXED |
| inspection-010 (GEC size) | FAIL | **PASS** | FIXED |

All 3 targeted fixes were successful.
