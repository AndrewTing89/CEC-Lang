# Judge Report - CEC Run 26

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | CEC Lang Agent (qwen/qwen3-32b) |
| **Source File** | cec-run26_evaluation_results_2025-12-10.md |
| **Judge** | Claude Code (Opus 4.5) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-10 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 29 |
| **Total Score** | 263 / 290 |
| **Percentage** | 90.7% |
| **Avg Accuracy** | 4.59 / 5 |
| **Avg Completeness** | 4.86 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 22 |
| High (8-9/10) | 6 |
| Medium (5-7/10) | 0 |
| Low (0-4/10) | 1 |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| cec-002 | EV charging infrastructure requirements | 5/5 | 5/5 | 10/10 |
| cec-003 | Solar PV requirements | 4/5 | 5/5 | 9/10 |
| cec-004 | Heat pump water heater circuit | 5/5 | 5/5 | 10/10 |
| cec-005 | Electric cooktop readiness | 4/5 | 5/5 | 9/10 |
| cec-006 | Electric clothes dryer panelboard | 5/5 | 5/5 | 10/10 |
| cec-007 | Table 240.4(G) | 4/5 | 4/5 | 8/10 |
| cec-008 | Table 242.3 | 5/5 | 5/5 | 10/10 |
| cec-009 | Table 430.72(B) | 5/5 | 5/5 | 10/10 |
| cec-010 | Medium voltage tables | 5/5 | 5/5 | 10/10 |
| cec-011 | 4/0 AWG copper ampacity | 5/5 | 5/5 | 10/10 |
| cec-012 | EGC for 200A circuit | 5/5 | 5/5 | 10/10 |
| cec-013 | GEC for 3/0 AWG service | 5/5 | 5/5 | 10/10 |
| cec-014 | Temperature correction factor | 5/5 | 5/5 | 10/10 |
| cec-015 | Bundling factor 7-9 conductors | 5/5 | 5/5 | 10/10 |
| cec-016 | Working space 480V Condition 3 | 5/5 | 5/5 | 10/10 |
| cec-017 | Enclosure types outdoor use | 4/5 | 5/5 | 9/10 |
| cec-018 | Office lighting load | 5/5 | 5/5 | 10/10 |
| cec-019 | Flexible cord ampacity 12 AWG | 5/5 | 5/5 | 10/10 |
| cec-020 | SF-2 fixture wire temperature | 5/5 | 5/5 | 10/10 |
| cec-021 | Adjusted ampacity calculation | 5/5 | 5/5 | 10/10 |
| cec-022 | 200A service sizing | 3/5 | 5/5 | 8/10 |
| cec-023 | Office lighting calculation | 1/5 | 3/5 | 4/10 |
| cec-024 | Motor control OCP 16 AWG | 5/5 | 5/5 | 10/10 |
| cec-025 | Dwelling lighting load | 5/5 | 5/5 | 10/10 |
| cec-026 | Kitchen GFCI comparison | 5/5 | 5/5 | 10/10 |
| cec-027 | Panelboard space comparison | 5/5 | 5/5 | 10/10 |
| cec-028 | EV comparison | 5/5 | 5/5 | 10/10 |
| cec-029 | AFCI comparison | 4/5 | 5/5 | 9/10 |
| cec-030 | Solar PV comparison | 3/5 | 4/5 | 7/10 |

---

## Detailed Results

### cec-002
**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All key facts correct: 40-amp circuits, conduit requirements, panel capacity, CALGreen/Title 24 compliance, Article 625 references.
**Completeness Notes:** Exceeds expected answer with GFCI, ventilation, cable requirements, and bidirectional systems.

---

### cec-003
**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Covers rapid shutdown and grounding correctly but cites 690.56 (labeling) rather than 690.12 (rapid shutdown timing). Missing explicit arc-fault (690.11) mention.
**Completeness Notes:** Very thorough with Title 24 mandate, grounding, bonding, wiring methods.

---

### cec-004
**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly cites 408.2(A), 422.3(A), dedicated circuits, panelboard spaces, Energy Code 150.0(n).
**Completeness Notes:** Includes both single-family and multifamily requirements.

---

### cec-005
**Question:** What is required for electric cooktop readiness in new California homes?
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Correct concept but emphasizes 422.3(A) over 408.2 as primary reference.
**Completeness Notes:** Complete coverage with both building types.

---

### cec-006
**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly cites 408.2(A) and (B), reserved spaces requirement.
**Completeness Notes:** Complete with Energy Code references for both building types.

---

### cec-007
**Question:** What does CEC Table 240.4(G) specify that is unique to California?
**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Identifies California-specific modifications but doesn't explicitly state "does not exist in NEC 2023."
**Completeness Notes:** Provides content but could be more definitive about NEC absence.

---

### cec-008
**Question:** What does CEC Table 242.3 specify for California installations?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies as "California amendment not present in base NEC."
**Completeness Notes:** Comprehensive list of cross-references.

---

### cec-009
**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct description of columns, conductor sizes, protection ratings.
**Completeness Notes:** Very thorough with example values and derivation.

---

### cec-010
**Question:** What medium voltage cable tables does California have that are not in the NEC?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly cites Tables 311.60(C)(67) through 311.60(C)(86), identifies as California-specific.
**Completeness Notes:** Explains purpose and NEC limitation.

---

### cec-011
**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: "230 amperes per CEC 2022 Table 310.16 [California Amendment]"
**Completeness Notes:** Includes OCP limit check and adjustment notes.

---

### cec-012
**Question:** What size equipment grounding conductor is required for a 200A circuit in California?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 6 AWG copper, 4 AWG aluminum per Table 250.122.
**Completeness Notes:** Both materials with table reference.

---

### cec-013
**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 4 AWG copper, 2 AWG aluminum per Table 250.66.
**Completeness Notes:** Both materials with table reference and footnotes.

---

### cec-014
**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 0.88 per Table 310.15(B)(1)(1).
**Completeness Notes:** Includes example application.

---

### cec-015
**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 0.70 (70%) per Table 310.15(C)(1).
**Completeness Notes:** Includes example and OCP limit check.

---

### cec-016
**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 1.2 meters (4 feet) per Table 110.26(A)(1).
**Completeness Notes:** Includes Condition 3 explanation.

---

### cec-017
**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Lists correct types but includes extra types (3SX, 3X) and notes 3R is not suitable (expected answer includes 3R).
**Completeness Notes:** Comprehensive with explanations.

---

### cec-018
**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 1.3 VA/sq ft per Table 220.12.
**Completeness Notes:** Notes 125% already included.

---

### cec-019
**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 25 amperes per Table 400.5(A)(1).
**Completeness Notes:** Explains Column B application.

---

### cec-020
**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 200°C (392°F) per Table 402.3.
**Completeness Notes:** Includes wire details.

---

### cec-021
**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 50A × 0.88 × 0.70 = 30.8A with all citations.
**Completeness Notes:** Shows all steps.

---

### cec-022
**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.
**Score:** 8/10 (Accuracy: 3/5, Completeness: 5/5)
**Accuracy Notes:** EGC (6 AWG) and GEC (4 AWG) correct, but service conductor is 2/0 AWG instead of 3/0 AWG. 2/0 has 175A ampacity at 75°C, insufficient for 200A.
**Completeness Notes:** All three conductor types addressed with references.

---

### cec-023
**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.
**Score:** 4/10 (Accuracy: 1/5, Completeness: 3/5)
**Accuracy Notes:** **CRITICAL ERROR:** Used outdated 3.5 VA/sq ft instead of current 1.3 VA/sq ft. Answer is 17,500 VA but should be 6,500 VA.
**Completeness Notes:** Shows calculation method but with wrong table value.

---

### cec-024
**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 10 amperes per Table 430.72(B) Column C.
**Completeness Notes:** Includes code basis.

---

### cec-025
**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact match: 2,400 × 3 VA = 7,200 VA.
**Completeness Notes:** Shows calculation.

---

### cec-026
**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies NEC 2023 as more restrictive, CEC limits to countertop surfaces.
**Completeness Notes:** Clear comparison with code citations.

---

### cec-027
**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies CEC 408.2(A) requirement, NEC has no such requirement.
**Completeness Notes:** Comprehensive comparison table.

---

### cec-028
**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly explains CA mandate vs NEC installation-only rules.
**Completeness Notes:** Detailed comparison table.

---

### cec-029
**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Mostly correct but claim that NEC "excludes hallways/laundry areas" is questionable.
**Completeness Notes:** Very detailed comparison.

---

### cec-030
**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.
**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** Misses the key point that California MANDATES solar PV installation on new homes (Title 24 Part 6) while NEC only provides installation rules. Focuses on technical differences instead.
**Completeness Notes:** Very detailed but misses the central distinction.

---

## Issues to Address

### Critical Error (cec-023)
**Office lighting calculation used wrong table value (3.5 VA/sq ft instead of 1.3 VA/sq ft)**
- The agent retrieved the wrong value from cec_search
- CEC 2022 Table 220.12 shows 1.3 VA/sq ft for offices (updated from older 3.5 value)
- This is a table data or search retrieval issue

### Significant Error (cec-022)
**Service conductor undersized (2/0 instead of 3/0)**
- 2/0 AWG copper has 175A ampacity at 75°C
- 3/0 AWG copper has 200A ampacity at 75°C
- For 200A service, 3/0 AWG is required

### Minor Issue (cec-030)
**Missed key comparison point**
- Should emphasize California MANDATES solar installation via Title 24
- NEC only provides HOW to install, not IF to install

---

## Strengths

1. **Table Lookups (22 perfect scores):** Ampacity, EGC, GEC, temperature factors, bundling factors, working space all 100% accurate
2. **Code References:** Consistently cites correct CEC sections (408.2, 250.122, 310.16, etc.)
3. **Comparison Questions:** CEC vs NEC comparisons generally well-handled
4. **Calculations:** Derating calculations (cec-021) perfectly executed

---

## Conclusion

**Final Score: 263/290 (90.7%)**

- 22 perfect scores (75.9%)
- 6 high scores (8-9/10)
- 1 critical error (cec-023)

The CEC Lang agent demonstrates strong performance on:
- Table lookups and conductor sizing
- Code citation accuracy
- Ampacity calculations

Areas for improvement:
- Table 220.12 office lighting values (outdated data?)
- Service conductor sizing logic
- Comparison question focus on key distinctions

---
*Report Generated: CEC Run 26 (Verification)*
*Evaluation Set: CEC 2022 California-Specific Questions*
*Judge: Claude Code (Opus 4.5) - LLM-as-Judge Method*
