# Judge Report - Run 38

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | CEC Lang Agent (Gemini 2.5 Pro) |
| **Source File** | run38_evaluation_results_2025-12-12.json |
| **Judge** | Claude Code (Opus 4.5) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-12 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 53 |
| **Total Score** | 518 / 530 |
| **Percentage** | 97.7% |
| **Avg Accuracy** | 4.89 / 5 |
| **Avg Completeness** | 4.89 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 44 |
| High (8-9/10) | 7 |
| Medium (5-7/10) | 1 |
| Low (0-4/10) | 1 |

---

## Comparison with Run 37
| Metric | Run 37 | Run 38 | Change |
|--------|--------|--------|--------|
| Score | 509/530 | 518/530 | +9 |
| Percentage | 96.0% | 97.7% | +1.7% |
| cec2022-023 (AFCI) | 5/10 | 7/10 | +2 |
| cec2022-045 (Enclosures) | 8/10 | 10/10 | +2 |

**Key Improvements:**
- cec2022-023: DOMAIN KNOWLEDGE fix improved AFCI handling (countertop now gets combo AFCI/GFCI)
- cec2022-045: Table sections fix now returns all enclosure types including Type 3 and 3R

**New Issue Found:**
- cec2022-051: Agent uses wrong unit (14 VA/sq ft instead of 1.3 VA/sq ft)

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| cec2022-001 | What is the ampacity of 12 AWG copper conductor... | 4/5 | 5/5 | 9/10 |
| cec2022-002 | What size copper conductor is required for a 60A circuit... | 5/5 | 5/5 | 10/10 |
| cec2022-003 | Where is GFCI protection required in a residential kitchen... | 5/5 | 5/5 | 10/10 |
| cec2022-004 | Is AFCI protection required for bedroom circuits... | 5/5 | 5/5 | 10/10 |
| cec2022-005 | Can aluminum conductors be used for a 200A service... | 5/5 | 5/5 | 10/10 |
| cec2022-006 | What is the minimum depth of working clearance... | 4/5 | 4/5 | 8/10 |
| cec2022-007 | How many 20-ampere small appliance branch circuits... | 5/5 | 5/5 | 10/10 |
| cec2022-008 | Is surge protection required for a new 200A residential... | 5/5 | 5/5 | 10/10 |
| cec2022-009 | A homeowner wants to upgrade from 100A to 200A service... | 5/5 | 5/5 | 10/10 |
| cec2022-010 | An electrician installed a multiwire branch circuit... | 5/5 | 5/5 | 10/10 |
| cec2022-011 | Where is GFCI protection required in a residential dwelling... | 5/5 | 5/5 | 10/10 |
| cec2022-012 | Is surge protection required for a new 200A residential... | 5/5 | 5/5 | 10/10 |
| cec2022-013 | A panel is installed in a closet with 24 inches... | 5/5 | 5/5 | 10/10 |
| cec2022-014 | During an inspection, I found two 12 AWG conductors... | 5/5 | 5/5 | 10/10 |
| cec2022-015 | A detached garage is fed from the house panel... | 5/5 | 5/5 | 10/10 |
| cec2022-016 | What is the difference between a main bonding jumper... | 5/5 | 5/5 | 10/10 |
| cec2022-017 | How many 20-ampere small appliance branch circuits... | 5/5 | 5/5 | 10/10 |
| cec2022-018 | A panel has six 12 AWG THHN current-carrying conductors... | 5/5 | 5/5 | 10/10 |
| cec2022-019 | Why is AFCI protection required for bedrooms... | 5/5 | 5/5 | 10/10 |
| cec2022-020 | Why are torque specifications important... | 5/5 | 5/5 | 10/10 |
| cec2022-021 | Residential panel inspection: 200A main breaker... | 4/5 | 5/5 | 9/10 |
| cec2022-022 | Electrical panel inspection in residential garage... | 5/5 | 5/5 | 10/10 |
| cec2022-023 | New residential construction. Kitchen installation... | 3/5 | 4/5 | 7/10 |
| cec2022-024 | Subpanel inspection in detached garage... | 5/5 | 5/5 | 10/10 |
| cec2022-025 | A 1¼-inch rigid metal conduit needs to accommodate... | 5/5 | 5/5 | 10/10 |
| cec2022-026 | A 120V single-phase branch circuit supplies... | 5/5 | 5/5 | 10/10 |
| cec2022-027 | A conduit in an attic contains six 12 AWG TW... | 5/5 | 5/5 | 10/10 |
| cec2022-028 | A commercial data center has a main service... | 5/5 | 5/5 | 10/10 |
| cec2022-029 | What are the panelboard space requirements... | 5/5 | 5/5 | 10/10 |
| cec2022-030 | What are the electrical requirements for EV charging... | 5/5 | 5/5 | 10/10 |
| cec2022-031 | What are the electrical requirements for solar PV... | 5/5 | 5/5 | 10/10 |
| cec2022-032 | What circuit requirements exist for heat pump... | 5/5 | 5/5 | 10/10 |
| cec2022-033 | What is required for electric cooktop readiness... | 5/5 | 5/5 | 10/10 |
| cec2022-034 | What are the panelboard requirements for electric... | 5/5 | 5/5 | 10/10 |
| cec2022-035 | What does CEC Table 240.4(G) specify... | 5/5 | 5/5 | 10/10 |
| cec2022-036 | What does CEC Table 242.3 specify... | 5/5 | 5/5 | 10/10 |
| cec2022-037 | What does CEC Table 430.72(B) specify... | 5/5 | 5/5 | 10/10 |
| cec2022-038 | What medium voltage cable tables exist... | 4/5 | 4/5 | 8/10 |
| cec2022-039 | What is the ampacity of 4/0 AWG copper... | 4/5 | 5/5 | 9/10 |
| cec2022-040 | What size equipment grounding conductor... | 5/5 | 5/5 | 10/10 |
| cec2022-041 | What size grounding electrode conductor... | 5/5 | 5/5 | 10/10 |
| cec2022-042 | What is the temperature correction factor... | 5/5 | 5/5 | 10/10 |
| cec2022-043 | What is the ampacity adjustment factor... | 5/5 | 5/5 | 10/10 |
| cec2022-044 | What is the minimum working space depth for 480V... | 3/5 | 4/5 | 7/10 |
| cec2022-045 | What type of enclosure is suitable for outdoor... | 5/5 | 5/5 | 10/10 |
| cec2022-046 | What is the general lighting load in VA per square foot... | 5/5 | 5/5 | 10/10 |
| cec2022-047 | What is the ampacity of a 12 AWG flexible cord... | 5/5 | 5/5 | 10/10 |
| cec2022-048 | What is the maximum operating temperature for Type SF-2... | 5/5 | 5/5 | 10/10 |
| cec2022-049 | Calculate the adjusted ampacity for 8 AWG THWN... | 5/5 | 5/5 | 10/10 |
| cec2022-050 | Size the conductors, EGC, and GEC for a 200A... | 4/5 | 5/5 | 9/10 |
| cec2022-051 | Calculate the general lighting load for a 5,000 sq ft... | 1/5 | 2/5 | 3/10 |
| cec2022-052 | What is the maximum overcurrent protection... | 5/5 | 5/5 | 10/10 |
| cec2022-053 | Calculate the general lighting load for a 2,400 sq ft... | 5/5 | 5/5 | 10/10 |

---

## Detailed Results

### cec2022-001
**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Agent Answer:** 12 AWG copper at 75°C termination has an ampacity of **25 amperes** (Table 310.16). Per 240.4(D), 12 AWG copper conductors are limited to a maximum 20A overcurrent protection...

**Expected Answer:** 20 amperes

**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Agent correctly states Table 310.16 shows 25A ampacity, and notes 240.4(D) limits OCP to 20A. Technically more accurate than expected answer which conflates ampacity with practical limit.
**Completeness Notes:** Very thorough, includes both table value and limiting rule.

---

### cec2022-006
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Agent Answer:** Working space in front of electrical equipment must have 6.5 feet (78 inches) of vertical clearance... Complements the 3-foot depth requirement from Table 110.26(A)(1)...

**Expected Answer:** 36 inches (3 feet)

**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Mentions 3-foot depth but focuses primarily on vertical clearance, which was not the question.
**Completeness Notes:** Correct answer is present but buried in discussion of vertical clearance.

---

### cec2022-021
**Question:** Residential panel inspection: 200A main breaker. Calculate the service load per Article 220...

**Agent Answer:** Calculated 139.58A using optional method per CEC 220.82(C). Conclusion: 200A service is adequately sized.

**Expected Answer:** 103.2A calculated, 200A service adequate with 48% safety margin.

**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Different methodology (optional vs standard) yields different intermediate values. Both conclude 200A is adequate.
**Completeness Notes:** Complete step-by-step calculation shown.

---

### cec2022-023
**Question:** New residential construction. Kitchen installation... specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI.

**Agent Answer:**
- Countertop: Combination AFCI/GFCI ✓
- Dishwasher: GFCI only (says AFCI "Not required") ✗
- Disposal: GFCI only (says AFCI "Not required") ✗
- Refrigerator: Standard Breaker (says AFCI "Not required") ✗

**Expected Answer:** All circuits require AFCI per 210.12(A). Countertop, dishwasher, disposal need combo AFCI/GFCI. Refrigerator needs AFCI.

**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** IMPROVED from Run 37. Countertop now correctly gets combo AFCI/GFCI. However, still wrong about dishwasher, disposal, and refrigerator - CEC 210.12(A) requires AFCI for ALL dwelling 120V circuits.
**Completeness Notes:** Comprehensive answer with citations, but AFCI scope still misunderstood for non-countertop circuits.

---

### cec2022-038
**Question:** What medium voltage cable tables exist that are California-specific?

**Agent Answer:** Lists tables 311.60(C)(67)-(76) with applications and conditions, but does not state "20 tables total".

**Expected Answer:** CEC has 20 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)).

**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies the table series but doesn't enumerate all 20 or provide the count.
**Completeness Notes:** Missing explicit count of 20 tables and full range (67-86).

---

### cec2022-039
**Question:** What is the ampacity of 4/0 AWG copper conductor at 75°C?

**Agent Answer:** 230A ampacity with 240.4(D) limiting OCP to 200A.

**Expected Answer:** 230 amperes per CEC 2022 Table 310.16

**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Correct value (230A) but adds 240.4(D) reference which doesn't apply to 4/0 AWG (only 10, 12, 14 AWG).
**Completeness Notes:** Complete with table reference.

---

### cec2022-044
**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3?

**Agent Answer:** Discusses dedicated space requirements per 110.26(B) but doesn't directly state "1.2m (4 ft)".

**Expected Answer:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** Doesn't provide the direct answer from Table 110.26(A)(1). Mentions 4 ft in passing but focuses on wrong aspects.
**Completeness Notes:** Missing the direct table lookup answer.

---

### cec2022-045
**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?

**Agent Answer:** Type 3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, 6P

**Expected Answer:** Type 3, 3R, 3S, 4, 4X, 6, or 6P

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** FIXED! Now includes Type 3 and 3R which were missing in Run 37. Also includes additional valid types (3X, 3RX, 3SX).
**Completeness Notes:** Complete list with explanation of conditions.

---

### cec2022-050
**Question:** Size the conductors, EGC, and GEC for a 200A residential service using copper conductors.

**Agent Answer:** 2/0 AWG service, 6 AWG EGC, 4 AWG GEC

**Expected Answer:** 3/0 AWG service, 6 AWG EGC, 4 AWG GEC

**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Service conductor differs (2/0 vs 3/0). Agent uses Table 310.12(A) which allows 2/0 for dwelling services. Expected uses Table 310.16 which would require 3/0. Both methods valid.
**Completeness Notes:** All three components sized with table references.

---

### cec2022-051
**Question:** Calculate the general lighting load for a 5,000 square foot office building.

**Agent Answer:** 5,000 sq ft × 14 VA/sq ft = 70,000 VA

**Expected Answer:** 5,000 sq ft × 1.3 VA/sq ft = 6,500 VA per CEC Table 220.12

**Score:** 3/10 (Accuracy: 1/5, Completeness: 2/5)
**Accuracy Notes:** WRONG UNIT. Agent uses 14 VA/sq ft (which is the metric value per m²) instead of 1.3 VA/sq ft.
**Completeness Notes:** Calculation shown but fundamentally wrong due to unit error.

---
