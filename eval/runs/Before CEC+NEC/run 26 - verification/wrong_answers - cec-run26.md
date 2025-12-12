# Wrong Answers - CEC Run 26

**Model:** CEC Lang Agent (qwen/qwen3-32b)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 90.7% (263/290)

---

## Executive Summary
**Questions with Errors:** 7 of 29
**Perfect Scores:** 22

---

## Detailed Error Analysis (7 questions)

### 1. cec-023 (Score: 4/10) - CRITICAL ERROR

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected Answer:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot. General lighting load = 5,000 sq ft × 1.3 VA/sq ft = 6,500 VA (6.5 kVA).

**Model Answer:** "5,000 sq ft × 3.5 VA/sq ft = 17,500 VA"

**Accuracy:** 1/5 - Used completely wrong table value
**Completeness:** 3/5 - Showed calculation method but wrong value

**Specific Errors:**
- Used outdated 3.5 VA/sq ft value (from pre-2020 codes)
- CEC 2022 Table 220.12 clearly shows 1.3 VA/sq ft for offices
- Final answer is 2.7× too high (17,500 vs 6,500)

**Root Cause:** The cec_search tool returned incorrect or outdated information for Table 220.12 office values.

---

### 2. cec-022 (Score: 8/10)

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected Answer:** Service conductors: 3/0 AWG copper minimum. EGC: 6 AWG copper. GEC: 4 AWG copper.

**Model Answer:** Service: 2/0 AWG copper, EGC: 6 AWG copper, GEC: 4 AWG copper

**Accuracy:** 3/5 - Service conductor undersized
**Completeness:** 5/5 - All components addressed

**Specific Errors:**
- Service conductor: 2/0 AWG (175A at 75°C) instead of 3/0 AWG (200A at 75°C)
- 2/0 AWG is insufficient for a 200A service

**Root Cause:** The cec_lookup_conductor_size tool returned 2/0 based on Table 310.12(A) but this table is for dwelling services with specific conditions.

---

### 3. cec-030 (Score: 7/10)

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected Answer:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements. The key difference is California requires solar installation; NEC only covers how to install it safely.

**Model Answer:** [Detailed technical comparison of specific code sections]

**Accuracy:** 3/5 - Missed the key distinction
**Completeness:** 4/5 - Very detailed but missed central point

**Specific Errors:**
- Failed to clearly state California MANDATES solar installation
- Focused on technical differences instead of the fundamental mandate vs guidance distinction
- Expected answer's key point: CA requires, NEC only covers how

---

### 4. cec-003 (Score: 9/10)

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected Answer:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47.

**Model Answer:** [Covers rapid shutdown 690.56, ground-fault 690.41, grounding 690.43/690.47]

**Accuracy:** 4/5 - Minor code citation difference
**Completeness:** 5/5 - Very thorough

**Specific Errors:**
- Cited 690.56 (labeling) for rapid shutdown instead of 690.12 (rapid shutdown timing requirements)
- Missing explicit mention of arc-fault protection (690.11)

---

### 5. cec-029 (Score: 9/10)

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected Answer:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, etc. The requirements are largely similar.

**Model Answer:** [Detailed comparison claiming CEC extends to closets/hallways/laundry while NEC excludes those]

**Accuracy:** 4/5 - Questionable claim about NEC exclusions
**Completeness:** 5/5 - Very detailed

**Specific Errors:**
- Claim that NEC "excludes hallways/laundry areas from mandatory AFCI coverage" is questionable
- Both codes should have similar coverage for these areas

---

### 6. cec-017 (Score: 9/10)

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected Answer:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures

**Model Answer:** [Lists Type 3, 3S, 3SX, 3X, 4, 4X, 6, 6P; notes 3R is NOT suitable]

**Accuracy:** 4/5 - Includes extra types, excludes 3R
**Completeness:** 5/5 - Comprehensive

**Specific Errors:**
- States Type 3R is "not suitable for sleet/ice" but expected answer includes 3R
- Includes non-standard types (3SX, 3X)

---

### 7. cec-005 (Score: 9/10)

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected Answer:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits.

**Model Answer:** [Emphasizes 422.3(A) and Energy Code 150.0(u) over 408.2]

**Accuracy:** 4/5 - Correct concept, different emphasis
**Completeness:** 5/5 - Complete

**Specific Errors:**
- Primary reference should be 408.2 (panelboard requirements)
- 422.3(A) links to the requirement but is not the primary source

---

## Summary of Error Categories

| Category | Count | Impact |
|----------|-------|--------|
| **Wrong table value** | 1 | Critical (cec-023) |
| **Undersized conductor** | 1 | Significant (cec-022) |
| **Missed key comparison point** | 1 | Moderate (cec-030) |
| **Minor code citation** | 3 | Minor |
| **Enclosure type interpretation** | 1 | Minor |

---

## Recommendations

1. **cec-023 FIX (Critical):** Update Table 220.12 data or search indexing to reflect current 1.3 VA/sq ft for offices
2. **cec-022 FIX:** Review conductor sizing logic for 200A services - should use Table 310.16 (3/0 = 200A) not Table 310.12(A)
3. **cec-030 FIX:** Add comparison template that highlights mandate vs guidance distinction for CA vs NEC questions

---

*Report Generated: CEC Run 26 (Verification)*
*Judge: Claude Code (Opus 4.5) - LLM-as-Judge Method*
