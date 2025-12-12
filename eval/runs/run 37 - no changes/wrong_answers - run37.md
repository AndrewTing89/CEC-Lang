# Wrong Answers - run37

**Model:** CEC Lang Agent (Gemini 2.5 Pro)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 96.0% (509/530)

---

## Executive Summary
**Questions with Errors:** 6 of 53
**Perfect Scores:** 47

| Question | Score | Issue Type |
|----------|-------|------------|
| cec2022-023 | 5/10 | **Critical Error** - AFCI requirement missed |
| cec2022-038 | 8/10 | Minor - Table count not provided |
| cec2022-045 | 8/10 | Minor - Enclosure types incomplete |
| cec2022-001 | 9/10 | Minor - Ampacity vs OCP nuance |
| cec2022-021 | 9/10 | Minor - Calculation methodology |

---

## Detailed Error Analysis

### 1. cec2022-023 (Score: 5/10) - **CRITICAL**
**Question:** New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide code references.

**Agent Answer:**
- Countertop: GFCI per 210.8(A)(6)
- Dishwasher: GFCI per 422.5(B)(3)
- Disposal: GFCI per 422.5(B)(3)
- Refrigerator: Standard Breaker (exempt from GFCI)
- **"None of these circuits require AFCI protection (210.12 applies only to bedroom circuits)."**

**Expected Answer:** Per CEC 2022: (1) Countertop receptacles: GFCI required per 210.8(A)(6), **AFCI required per 210.12(A)**. Use combination AFCI/GFCI. (2) Dishwasher: GFCI per 422.5, **AFCI required per 210.12(A)**. (3) Disposal: GFCI per 210.8(A)(6), **AFCI required per 210.12(A)**. (4) Refrigerator: **AFCI required per 210.12(A)**. **All 120V dwelling circuits require AFCI per 210.12(A).**

**Accuracy:** 2/5 - GFCI requirements correct, but **completely wrong about AFCI**
**Completeness:** 3/5 - Missing entire AFCI requirement

**Specific Errors:**
1. **CRITICAL ERROR**: Agent states "AFCI applies only to bedroom circuits" - this is FALSE for CEC 2022
2. CEC 2022 Section 210.12(A) requires AFCI for ALL 120V, 15A and 20A branch circuits in dwelling units, including kitchens
3. The 2017/2020 NEC expanded AFCI to cover essentially all dwelling areas, and CEC 2022 adopts this
4. This is a safety-critical error that could result in non-compliant installations

**Root Cause Analysis:**
The agent appears to have outdated information or is confusing earlier code editions. Earlier NEC editions (pre-2014) limited AFCI primarily to bedrooms. Modern codes (NEC 2017+, CEC 2022) require AFCI for virtually all dwelling unit 120V circuits.

**Impact:** High - Could result in inspector rejections and fire safety concerns

---

### 2. cec2022-038 (Score: 8/10)
**Question:** What medium voltage cable tables exist that are California-specific?

**Agent Answer:** Lists several MV cable ampacity tables in 311.60(C) series including 311.60(C)(67)-(70), 311.60(C)(75)-(76), etc. with details about applications and conditions.

**Expected Answer:** CEC has **20 medium voltage tables** in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only.

**Accuracy:** 4/5 - Correctly identifies the table series
**Completeness:** 4/5 - Missing specific count

**Specific Errors:**
1. Did not state the total count of 20 tables
2. The range 67-86 = 20 tables (86-67+1=20), not enumerated
3. Response is informative but doesn't directly answer "how many tables"

**Impact:** Low - The answer is substantively correct, just lacks the specific enumeration

---

### 3. cec2022-045 (Score: 8/10)
**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?

**Agent Answer:** Type 3S, 3SX, 4, 4X, 6, 6P per Table 110.28

**Expected Answer:** Type 3, 3R, 3S, 4, 4X, 6, or 6P per Table 110.28

**Accuracy:** 4/5 - Most types correct
**Completeness:** 4/5 - Missing some valid types

**Specific Errors:**
1. Missing Type 3 (rainproof, dusttight)
2. Missing Type 3R (rainproof, ice-resistant)
3. Added Type 3SX (valid but not commonly listed)

**Impact:** Low - The answer includes the most common appropriate types, but inspectors may accept other valid options

---

### 4. cec2022-001 (Score: 9/10)
**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Agent Answer:** Base ampacity of **25 amperes** per Table 310.16. Notes that 240.4(D) limits overcurrent protection to **20A maximum**.

**Expected Answer:** 20 amperes

**Accuracy:** 4/5 - Technically more accurate but may cause confusion
**Completeness:** 5/5 - Very thorough

**Specific Errors:**
1. Expected answer says "20 amperes" which is actually the OCP limit, not the ampacity
2. Table 310.16 clearly shows 25A for 12 AWG at 75°C
3. Agent is technically correct but the question may have intended the practical answer
4. The distinction between "ampacity" (25A from table) and "practical current limit" (20A from 240.4(D)) is important

**Impact:** Very low - Agent's answer is technically more accurate, just presents more information than expected

---

### 5. cec2022-021 (Score: 9/10)
**Question:** Residential panel inspection: 200A main breaker. Calculate service load per Article 220.

**Agent Answer:** Calculated total load of **120.21A**, 200A panel adequate.

**Expected Answer:** Calculated **103.2A**, 200A service adequate with 48% safety margin.

**Accuracy:** 4/5 - Different methodology, same conclusion
**Completeness:** 5/5 - Complete step-by-step calculation

**Specific Errors:**
1. Agent calculated 120.21A vs expected 103.2A (17A difference)
2. Both conclude 200A is adequate - same final answer
3. Difference appears to be in demand factor application:
   - Agent applied 1.25× continuous load factor to AC
   - Expected answer may have used different Article 220 tables
4. Both approaches are defensible under Article 220

**Impact:** None - Same conclusion reached, just different calculation methodology

---

## Summary by Category

### Critical Errors (Requires Fix)
| ID | Issue | Recommended Action |
|----|-------|-------------------|
| cec2022-023 | AFCI scope incorrect | Update agent knowledge about CEC 2022 210.12(A) AFCI requirements |

### Minor Errors (Low Priority)
| ID | Issue | Notes |
|----|-------|-------|
| cec2022-038 | Table count missing | Consider adding enumeration to MV table responses |
| cec2022-045 | Enclosure list incomplete | Minor omission, not critical |
| cec2022-001 | Ampacity vs OCP | Agent is technically correct |
| cec2022-021 | Calculation variance | Both methods valid |

---

## Comparison with Previous Runs

### Persistent Issues
- **cec2022-023** (AFCI for kitchens): This error has appeared in multiple runs. The agent consistently misunderstands the scope of CEC 2022 AFCI requirements.

### Resolved Issues from Run 36
- **cec2022-035** (Table 240.4(G)): Expected answer was corrected - table exists in both CEC and NEC
- **cec2022-038** (MV tables): Expected answer was corrected - 20 tables, not 18

### New Issues in Run 37
- None - same error patterns as Run 36

---

## Recommended Fixes

### Priority 1: AFCI Knowledge Update
The agent needs updated knowledge about CEC 2022 Section 210.12(A):
- AFCI is required for **all** 120V, 15A and 20A branch circuits in dwelling units
- This includes kitchens, not just bedrooms
- The only exception is dedicated equipment circuits (certain HVAC, etc.)

### Priority 2: Expected Answer Review
Consider reviewing these expected answers:
- cec2022-001: Expected says "20A" but that's OCP limit, not ampacity (25A)
- cec2022-021: Different calculation methods are acceptable under Article 220
