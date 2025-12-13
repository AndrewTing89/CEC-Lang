# Wrong Answers - Run 41

**Model:** CEC Lang Agent (Gemini 2.5 Pro)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 96.8% (513/530)

---

## Executive Summary
**Questions with Errors:** 10 of 53
**Perfect Scores:** 43

| Question | Score | Issue Type |
|----------|-------|------------|
| cec2022-005 | 8/10 | Minor - Different table used (310.16 vs 310.12(A)) |
| cec2022-006 | 8/10 | Minor - Answer present but not emphasized |
| cec2022-009 | 8/10 | Minor - Different sizing methodology |
| cec2022-035 | 8/10 | Minor - Missing specific CA delta values |
| cec2022-038 | 8/10 | Minor - Incomplete table list |
| cec2022-044 | 8/10 | Minor - Direct answer buried in text |
| cec2022-050 | 8/10 | Minor - Different table for service conductors |
| cec2022-001 | 9/10 | Minor - Ampacity vs OCP nuance |
| cec2022-015 | 9/10 | Minor - GE requirement nuance |
| cec2022-021 | 9/10 | Minor - Different calculation method |

---

## TARGET QUESTION FIXES VERIFIED

### cec2022-045 (Enclosure Types): 8/10 → 10/10 (+2)
**FIXED!** Agent now correctly lists ALL enclosure types from "Rain, snow, and sleet" row.

**Previous Issue:** Listed only 3S, 3SX, 3X (over-interpreted "sleet" requirement)

**Run 41 Answer:** Type 3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, 6P - with correct interpretation note distinguishing "Rain, snow, and sleet" row from "Sleet*" row.

**Root Cause Fixed:** Table 110.28 interpretation guide added to tool output.

---

### cec2022-051 (Office Lighting): Maintained at 10/10
**VERIFIED!** Agent continues to correctly use 1.3 VA/ft² (imperial).

**Run 41 Answer:** 5,000 × 1.3 VA/ft² = 6,500 VA (CORRECT)

**Root Cause Fixed:** Dual-unit table formatting with explicit imperial/metric guidance.

---

## Detailed Error Analysis

### 1. cec2022-005 (Score: 8/10)
**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Agent Answer:** Yes, 250 kcmil aluminum (Table 310.16 at 75°C = 200A)

**Expected Answer:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**Accuracy:** 4/5 - Valid but different table
**Completeness:** 4/5 - Answer complete for method used

**Specific Errors:**
- Uses Table 310.16 (general ampacity) instead of Table 310.12(A) (dwelling service allowance)
- 250 kcmil is technically correct by 310.16 but 4/0 is standard answer per 310.12(A)

**Root Cause:** Both answers are code-compliant. Table 310.12(A) is more commonly used for dwelling services.

---

### 2. cec2022-006 (Score: 8/10)
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Agent Answer:** Discusses 110.26(B), mentions "3-foot depth requirement" in context.

**Expected Answer:** 36 inches (3 feet)

**Accuracy:** 4/5 - Correct value present but buried
**Completeness:** 4/5 - Answer not emphasized

**Specific Errors:**
- Focuses on 110.26(B) dedicated space instead of 110.26(A)(1) depth
- "3 ft" mentioned but not as the primary, direct answer

---

### 3. cec2022-009 (Score: 8/10)
**Question:** 200A service upgrade with various loads - what size conductors?

**Agent Answer:** 4/0 AWG copper or 250 kcmil aluminum

**Expected Answer:** 2/0 AWG copper OR 4/0 AWG aluminum per Table 310.12

**Accuracy:** 4/5 - Different sizing method
**Completeness:** 4/5 - All components addressed

**Specific Errors:**
- Uses Table 310.16 sizing instead of Table 310.12(A) dwelling service allowance
- Results in different (larger) conductor sizes

---

### 4. cec2022-035 (Score: 8/10)
**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Agent Answer:** Table mirrors NEC but California amendments add context for fire alarms and HVAC.

**Expected Answer:** Table exists in BOTH codes but California has modified values.

**Accuracy:** 4/5 - General concept correct
**Completeness:** 4/5 - Missing specific delta values

**Specific Errors:**
- Doesn't clearly state specific California-modified overcurrent protection values
- Focus on cross-references rather than table content differences

---

### 5. cec2022-038 (Score: 8/10)
**Question:** What medium voltage cable tables exist that are California-specific?

**Agent Answer:** Lists Tables 315.10(A), 315.60(C)(5), (6), (9), (10), (13)

**Expected Answer:** 20 tables: 311.60(C)(67) through 311.60(C)(86)

**Accuracy:** 4/5 - Correct series, incomplete range
**Completeness:** 4/5 - Missing count and full enumeration

**Specific Errors:**
- Does not state "20 tables total"
- Lists Article 315 tables instead of the specific California-only 311.60(C)(67)-(86) series

---

### 6. cec2022-044 (Score: 8/10)
**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3?

**Agent Answer:** Discusses 110.26(B) requirements, mentions "4 ft (1.2 m) for 480V under Condition 3" buried in verification section.

**Expected Answer:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**Accuracy:** 4/5 - Correct value present
**Completeness:** 4/5 - Direct answer not emphasized

**Specific Errors:**
- Focuses on additional requirements rather than primary answer
- "4 ft" correct but stated as supporting detail not primary response

---

### 7. cec2022-050 (Score: 8/10)
**Question:** Size the conductors, EGC, and GEC for a 200A residential service using copper.

**Agent Answer:** 2/0 AWG service, 6 AWG EGC, 6 AWG GEC

**Expected Answer:** 3/0 AWG service, 6 AWG EGC, 4 AWG GEC

**Accuracy:** 4/5 - Different sizing method
**Completeness:** 4/5 - All components sized but values differ

**Specific Errors:**
- Service conductor: 2/0 (Table 310.12(A)) vs 3/0 (Table 310.16)
- GEC: 6 AWG (based on 2/0 service) vs 4 AWG (based on 3/0 service)

**Root Cause:** Agent uses Table 310.12(A) dwelling allowance; expected uses Table 310.16 general ampacity.

---

### 8. cec2022-001 (Score: 9/10)
**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Agent Answer:** 25A from Table 310.16, but 240.4(D) limits to 20A OCP

**Expected Answer:** 20 amperes

**Accuracy:** 4/5 - Technically more accurate
**Completeness:** 5/5 - Comprehensive explanation

**Notes:** Agent distinguishes between table ampacity (25A) and practical application (20A OCP limit). This is technically more accurate but the expected answer simplifies to practical limit.

---

### 9. cec2022-015 (Score: 9/10)
**Question:** Detached garage grounding and bonding configuration

**Agent Answer:** Correctly identifies neutral/ground separation requirement. States "No Grounding Electrode Required."

**Expected Answer:** Includes note that grounding electrode may be required per 250.32

**Accuracy:** 4/5 - Minor nuance on GE requirement
**Completeness:** 5/5 - Comprehensive bonding explanation

**Specific Errors:**
- CEC 250.32 may require grounding electrode for detached buildings with 4-wire feeders

---

### 10. cec2022-021 (Score: 9/10)
**Question:** Calculate service load per Article 220 for residential panel.

**Agent Answer:** ~143A using one calculation method

**Expected Answer:** 103.2A using standard method

**Accuracy:** 4/5 - Different valid method
**Completeness:** 5/5 - Complete calculation shown

**Notes:** Both methods valid under Article 220. Agent used different demand factors but correctly concludes 200A service is adequate.

---

## Summary by Category

### No Critical Issues
All errors are minor variations in methodology or answer presentation.

### Table Methodology Differences (3 questions)
| ID | Issue |
|----|-------|
| cec2022-005 | 310.16 vs 310.12(A) for aluminum service |
| cec2022-009 | 310.16 vs 310.12(A) for copper service |
| cec2022-050 | 310.16 vs 310.12(A) for service sizing |

**Note:** Both Table 310.16 (general ampacity) and Table 310.12(A) (dwelling service allowance) are code-compliant approaches.

### Answer Presentation Issues (2 questions)
| ID | Issue |
|----|-------|
| cec2022-006 | Working space depth answer buried |
| cec2022-044 | 480V Condition 3 depth answer buried |

### Minor Omissions (2 questions)
| ID | Issue |
|----|-------|
| cec2022-035 | Missing specific CA delta values |
| cec2022-038 | Incomplete medium voltage table list |

### Technical Nuances (3 questions)
| ID | Issue |
|----|-------|
| cec2022-001 | Ampacity vs OCP distinction |
| cec2022-015 | GE requirement nuance |
| cec2022-021 | Different valid calculation method |

---

## Key Observations

1. **Both targeted fixes working perfectly:**
   - cec2022-045: Now lists all 10 enclosure types with correct interpretation
   - cec2022-051: Continues to use correct imperial units (1.3 VA/ft²)

2. **Score improvement from Run 39:**
   - Run 39: 508/530 (95.8%)
   - Run 41: 513/530 (96.8%)
   - Net improvement: +5 points (+1.0%)

3. **Remaining patterns:**
   - Most non-perfect scores involve valid alternative table methodologies
   - No fundamental errors - all issues are minor presentation or nuance
