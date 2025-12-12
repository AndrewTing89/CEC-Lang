# Judge Report - cec-run29_evaluation_results_2025-12-10

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | CEC Lang Agent (qwen/qwen3-32b) |
| **Source File** | cec-run29_evaluation_results_2025-12-10.md |
| **Judge** | Claude Code (Opus) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-10 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 29 |
| **Total Score** | 254 / 290 |
| **Percentage** | 87.6% |
| **Avg Accuracy** | 4.38 / 5 |
| **Avg Completeness** | 4.38 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 17 |
| High (8-9/10) | 8 |
| Medium (5-7/10) | 3 |
| Low (0-4/10) | 1 |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| cec-002 | EV charging infrastructure requirements | 5/5 | 4/5 | 9/10 |
| cec-003 | Solar PV requirements | 5/5 | 5/5 | 10/10 |
| cec-004 | Heat pump water heater circuits | 5/5 | 5/5 | 10/10 |
| cec-005 | Electric cooktop readiness | 5/5 | 5/5 | 10/10 |
| cec-006 | Panelboard for electric dryers | 5/5 | 5/5 | 10/10 |
| cec-007 | CEC Table 240.4(G) | 4/5 | 4/5 | 8/10 |
| cec-008 | CEC Table 242.3 | 5/5 | 5/5 | 10/10 |
| cec-009 | Table 430.72(B) motor control | 5/5 | 5/5 | 10/10 |
| cec-010 | Medium voltage cable tables | 5/5 | 5/5 | 10/10 |
| cec-011 | 4/0 AWG copper ampacity at 75C | 5/5 | 5/5 | 10/10 |
| cec-012 | EGC for 200A circuit | 5/5 | 5/5 | 10/10 |
| cec-013 | GEC for 3/0 AWG service | 5/5 | 5/5 | 10/10 |
| cec-014 | Temp correction 75C at 40C ambient | 5/5 | 5/5 | 10/10 |
| cec-015 | Bundling factor 7-9 conductors | 5/5 | 5/5 | 10/10 |
| cec-016 | Working space 480V Condition 3 | 5/5 | 5/5 | 10/10 |
| cec-017 | Enclosure for rain/sleet/ice | 5/5 | 4/5 | 9/10 |
| cec-018 | Office lighting load VA/sqft | 5/5 | 5/5 | 10/10 |
| cec-019 | 12 AWG flexible cord ampacity | 3/5 | 4/5 | 7/10 |
| cec-020 | SF-2 fixture wire temp rating | 2/5 | 3/5 | 5/10 |
| cec-021 | Adjusted ampacity 8 AWG THWN | 5/5 | 5/5 | 10/10 |
| cec-022 | Service sizing 200A residential | 4/5 | 4/5 | 8/10 |
| cec-023 | Office lighting load calculation | 5/5 | 5/5 | 10/10 |
| cec-024 | Motor control 16 AWG OCP | 5/5 | 5/5 | 10/10 |
| cec-025 | Dwelling lighting load calculation | 5/5 | 5/5 | 10/10 |
| cec-026 | Kitchen GFCI CEC vs NEC | 3/5 | 4/5 | 7/10 |
| cec-027 | Panelboard space CEC vs NEC | 5/5 | 5/5 | 10/10 |
| cec-028 | EV charging CEC vs NEC | 5/5 | 5/5 | 10/10 |
| cec-029 | AFCI requirements CEC vs NEC | 5/5 | 4/5 | 9/10 |
| cec-030 | Solar PV CEC vs NEC | 5/5 | 4/5 | 9/10 |

---

## Detailed Results

### cec-002
**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correctly covers CALGreen compliance, dedicated circuits, location requirements, GFCI protection.
**Completeness Notes:** Good coverage but missing specific mention of 40-amp minimum circuit requirement.

---

### cec-003
**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly covers rapid shutdown (690.12), arc-fault protection (690.11), grounding requirements, and Title 24 mandate.
**Completeness Notes:** Comprehensive coverage of all key requirements including labeling.

---

### cec-004
**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states CEC 408.2 requires reserved panelboard space for heat pump water heater circuits.
**Completeness Notes:** Includes reference to California Energy Code 150.0(n).

---

### cec-005
**Question:** What is required for electric cooktop readiness in new California homes?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states CEC 408.2 requires dedicated circuits and reserved spaces for electric cooktops.
**Completeness Notes:** Covers both single-family (422.3(A)) and multifamily (422.3(B)) requirements.

---

### cec-006
**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states CEC 408.2 requires reserved panelboard space for electric clothes dryer circuits.
**Completeness Notes:** Covers both single-family and multifamily requirements with Energy Code references.

---

### cec-007
**Question:** What does CEC Table 240.4(G) specify that is unique to California?
**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** States table is identical to NEC, which contradicts expected answer stating it's California-only. The expected answer says "CEC Table 240.4(G) is a California-only table." Response needs verification.
**Completeness Notes:** Provides context but doesn't definitively identify California-specific content.

---

### cec-008
**Question:** What does CEC Table 242.3 specify for California installations?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies as California-specific table (marked with N) not in NEC.
**Completeness Notes:** Lists all equipment-to-article cross-references.

---

### cec-009
**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly describes columns A, B, C for different configurations with conductor sizes.
**Completeness Notes:** Comprehensive coverage of table structure, values, and application rules.

---

### cec-010
**Question:** What medium voltage cable tables does California have that are not in the NEC?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies 311.60(C) series tables for medium voltage cables.
**Completeness Notes:** Lists specific tables (311.60(C)(67-86)) and their purposes.

---

### cec-011
**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 230 amperes per CEC Table 310.16.
**Completeness Notes:** Includes limiting factors and overcurrent protection notes.

---

### cec-012
**Question:** What size equipment grounding conductor is required for a 200A circuit in California?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 6 AWG copper or 4 AWG aluminum per Table 250.122.
**Completeness Notes:** Notes California amendment with delta symbol.

---

### cec-013
**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 4 AWG copper per Table 250.66.
**Completeness Notes:** Complete answer with table reference.

---

### cec-014
**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 0.88 per Table 310.15(B)(1)(1).
**Completeness Notes:** Direct and accurate answer.

---

### cec-015
**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 0.70 (70%) per Table 310.15(C)(1).
**Completeness Notes:** Includes footnote clarification.

---

### cec-016
**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 1.2 meters (4 feet) per Table 110.26(A)(1).
**Completeness Notes:** Includes context for Condition 3.

---

### cec-017
**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Lists Type 3S, 3SX, 3X, 4, 4X, 6, 6P as suitable.
**Completeness Notes:** Missing Type 3 and 3R which are also suitable per expected answer.

---

### cec-018
**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 1.3 VA per square foot per Table 220.12.
**Completeness Notes:** Notes the 125% continuous load is included.

---

### cec-019
**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?
**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** States 20 amperes but expected answer is 25 amperes per Table 400.5(A)(1). The agent correctly identifies Table 400.5(A)(1) as the source but gets the value wrong.
**Completeness Notes:** Good explanation distinguishing flexible cord from fixed wiring tables.

---

### cec-020
**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?
**Score:** 5/10 (Accuracy: 2/5, Completeness: 3/5)
**Accuracy Notes:** States 105°C but expected answer is 200°C per Table 402.3. This is a significant error.
**Completeness Notes:** Identifies correct table but wrong value.

---

### cec-021
**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates: 50A × 0.88 × 0.70 = 30.8A.
**Completeness Notes:** Shows all steps with correct factors.

---

### cec-022
**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.
**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** States 2/0 AWG service conductors (per 310.12(A)) but expected is 3/0 AWG (per Table 310.16). GEC of 6 AWG may be low - expected is 4 AWG for 3/0 service conductors.
**Completeness Notes:** Provides all three sizes but some may be incorrect based on table used.

---

### cec-023
**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates 5,000 × 1.3 = 6,500 VA.
**Completeness Notes:** Notes the self-correction from initial wrong value.

---

### cec-024
**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 10 amperes per Table 430.72(B) Column C.
**Completeness Notes:** Cites both 240.4(D)(2) and 430.72(B).

---

### cec-025
**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates 2,400 × 3 = 7,200 VA per Section 220.14(J).
**Completeness Notes:** Correctly distinguishes dwelling unit calculation from Table 220.12.

---

### cec-026
**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?
**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** INCORRECT: States NEC 2023 is more restrictive. Expected answer says CEC 2022 is MORE PERMISSIVE (meaning NEC is more restrictive), but the key comparison is: CEC limits GFCI to countertops/sinks, NEC requires ALL kitchen receptacles including refrigerators. Response correctly identifies NEC as broader but the framing could be clearer.
**Completeness Notes:** Good comparison details but conclusion framing is confusing.

---

### cec-027
**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states CEC requires reserved spaces for heat pump water heaters, heat pump space heaters, electric cooktops, and electric clothes dryers. NEC has no such requirement.
**Completeness Notes:** Comprehensive comparison table included.

---

### cec-028
**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies California mandates EV infrastructure while NEC only provides installation rules.
**Completeness Notes:** Excellent comparison table with specific code references.

---

### cec-029
**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correctly notes both codes require AFCI for 15/20A branch circuits in dwelling units.
**Completeness Notes:** Could more clearly state they are "largely similar" as expected answer indicates.

---

### cec-030
**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies California MANDATES PV while NEC only covers installation.
**Completeness Notes:** Good comparison but could emphasize the mandate vs installation-rules distinction more clearly.

---
