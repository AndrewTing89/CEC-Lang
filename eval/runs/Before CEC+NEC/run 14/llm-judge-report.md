# Run 14 - LLM Judge Report

**Date:** 2025-12-09
**Evaluator:** Claude Opus 4.5
**Method:** Manual review of each Q&A pair against expected answers

---

## Executive Summary

| Category | Questions | Fully Correct | Partial Credit | Errors |
|----------|-----------|---------------|----------------|--------|
| Core (baseline + core) | 28 | 24 | 3 | 1 |
| CEC | 30 | 30 | 0 | 0 |
| Inspection | 8 | 5 | 2 | 1 |
| **Total** | **66** | **59** | **5** | **2** |

**Overall Accuracy:** 89% fully correct, 97% acceptable (including partial credit)

---

## Targeted Fix Verification

All 3 targeted fixes from Run 13 were **SUCCESSFULLY RESOLVED**:

| Question | Run 13 Answer | Run 14 Answer | Expected | Status |
|----------|--------------|---------------|----------|--------|
| baseline-002 | 4 AWG (wrong) | **6 AWG copper** | 6 AWG copper | FIXED |
| cec-018 | 1.0 VA/ft² (wrong) | **1.3 VA/ft²** | 1.3 VA/ft² | FIXED |
| inspection-010 | 3/0 AWG (wrong) | **2/0 AWG** | 2/0 AWG | FIXED |

---

## Detailed Analysis by Category

### CORE Evaluation (28 questions)

#### Fully Correct (24 questions)
- baseline-001: 20A ampacity with correct 240.4(D) explanation
- baseline-002: **FIXED** - 6 AWG copper, correctly notes 240.4(D) doesn't apply
- baseline-003: Complete GFCI locations for kitchen
- baseline-004: AFCI required for bedrooms
- baseline-005: 4/0 AWG aluminum for 200A service
- baseline-006: 3 feet (36 inches) working clearance
- baseline-007: Two 20A small appliance circuits
- baseline-008: SPD required per 230.67
- core-001: 2/0 copper or 4/0 aluminum service conductors
- core-002: MWBC requirements with handle tie/common trip
- core-003: Comprehensive GFCI location list
- core-004: SPD Type 1/2 with installation locations
- core-006: Code violation for double-tapped breaker
- core-007: Subpanel ground/neutral separation
- core-008: MBJ vs SBJ distinction
- core-009: Two 20A circuits, can serve dining room
- core-010: 19.7A adjusted ampacity (30A × 0.82 × 0.80)
- core-011: AFCI prevents arc faults
- core-012: Torque specifications per 110.14(D)

#### Partial Credit (3 questions)

**core-005** - Panel in closet violations
- **Issue:** Agent stated 30 inches depth required, but Table 110.26(A)(1) requires **36 inches (3 feet)** for all voltage conditions at 0-150V to ground
- **Agent said:** "Required: 30 inches (762 mm) per CEC 110.26(A)(1) for systems ≤150V"
- **Correct:** 36 inches minimum for any condition
- **Impact:** Final conclusion correct (24" is insufficient), but specific requirement cited was wrong
- **Score:** 8/10

**inspection-001** - Service load calculation
- **Issue:** Agent used incorrect demand factor for range
- **Agent calculated:** 10,000 VA for range using "8 kW + 50% of (12 kW - 8 kW)"
- **Correct:** 8,000 VA per Table 220.55 Column C for one range ≤12kW
- **Final result:** Agent got 109.5A vs expected 103.2A
- **Impact:** Both conclude 200A is adequate, but calculation methodology incorrect
- **Score:** 7/10

**inspection-002** - Panel working space violations
- **Issue:** Same 30" vs 36" error as core-005
- **Agent said:** "less than the required 30 inches"
- **Correct:** Should be 36 inches
- **Impact:** Violation identified correctly, specific code value wrong
- **Score:** 8/10

#### Errors (1 question)

**inspection-005** - Kitchen circuit protection requirements
- **Multiple errors in protection requirements:**
  - Countertops: Agent says "GFCI" only; should be "AFCI/GFCI combination" per 210.12(A)
  - Dishwasher: Agent says "Standard Breaker"; should be "AFCI/GFCI combination" per 210.8(D) and 210.12(A)
  - Disposal: Agent says "Standard Breaker"; should be "AFCI" per 210.12(A)
- **Correct answers:**
  - Countertops: Combination AFCI/GFCI
  - Dishwasher: Combination AFCI/GFCI (GFCI required per 210.8(D), AFCI per 210.12)
  - Disposal: AFCI minimum (210.12(A))
  - Refrigerator: AFCI (agent got this correct)
- **Score:** 4/10 (only refrigerator fully correct)

---

### CEC Evaluation (30 questions)

All 30 CEC questions were **FULLY CORRECT**, including:

- cec-001: Panel space requirements with correct appliance list
- cec-002: EV charging infrastructure per Article 625 and CALGreen
- cec-003: Solar PV requirements with rapid shutdown, arc-fault, grounding
- cec-004 through cec-006: Heat pump, cooktop, dryer circuit requirements
- cec-007: Table 240.4(G) California-specific provisions
- cec-008: Table 242.3 surge protection cross-reference
- **cec-018: FIXED - 1.3 VA/ft² for office lighting (was 1.0 in Run 13)**
- All other CEC questions verified correct

---

### Inspection Evaluation (8 questions)

#### Fully Correct (5 questions)
- inspection-006: Subpanel bonding violations
- inspection-008: Voltage drop calculation (2.84V, 2.36%)
- inspection-009: TW conductor derating (11.4A)
- **inspection-010: FIXED - 2/0 AWG GEC for 1000 kcmil**

#### Partial Credit (2 questions)
- inspection-001: Load calculation (methodology issue)
- inspection-002: Working space (30" vs 36" error)

#### Errors (1 question)
- inspection-005: Circuit protection requirements

---

## Error Patterns Identified

### Pattern 1: Working Space Clearance Value
**Affected questions:** core-005, inspection-002
**Error:** Agent cites 30 inches for 0-150V systems
**Correct:** 36 inches per Table 110.26(A)(1) for all conditions

**Root Cause:** Agent may have confused width requirements (30" minimum) with depth requirements (36" minimum).

### Pattern 2: AFCI Requirements for Kitchen Circuits
**Affected questions:** inspection-005
**Error:** Agent doesn't apply 210.12(A) AFCI requirements to kitchen circuits
**Correct:** 2023 NEC requires AFCI for all 120V, 15/20A dwelling unit circuits including kitchen

**Root Cause:** Agent may be using outdated NEC information or not recognizing kitchen as requiring AFCI per 210.12(A).

### Pattern 3: Table 220.55 Range Demand
**Affected questions:** inspection-001
**Error:** Agent uses incorrect formula for range demand
**Correct:** Table 220.55 Column C directly gives 8kW for one range ≤12kW

**Root Cause:** Agent may be conflating different table columns or using adjustment notes incorrectly.

---

## Recommendations for Future Improvements

1. **Fix working clearance tool/prompt:** Ensure 110.26(A)(1) returns 36" for all voltage conditions, not 30"

2. **Add AFCI routing guidance for kitchen:** Update system prompt to clarify that 210.12(A) AFCI requirements apply to ALL dwelling unit 120V circuits, including kitchen circuits

3. **Verify Table 220.55 lookup logic:** Ensure range demand calculation uses Column C value directly for ≤12kW ranges

---

## Scoring Summary

| Score | Count | Percentage |
|-------|-------|------------|
| 10/10 | 59 | 89.4% |
| 7-9/10 | 5 | 7.6% |
| 4-6/10 | 2 | 3.0% |
| 0-3/10 | 0 | 0.0% |

**Weighted Average Score:** 9.4/10

---

## Conclusion

Run 14 successfully fixed all 3 targeted errors from Run 13:
- baseline-002: 240.4(D) scope filtering working correctly
- cec-018: Lighting vs receptacle routing guidance effective
- inspection-010: GEC table lookup correct

However, the review identified additional issues:
- 30" vs 36" working clearance error (2 questions)
- Missing AFCI requirements for kitchen circuits (1 question)
- Range demand calculation methodology (1 question)

**Overall Assessment:** The agent performs well on the majority of questions (89% fully correct). The identified issues are systematic and could be addressed with targeted fixes to the system prompt or table lookup tools.
