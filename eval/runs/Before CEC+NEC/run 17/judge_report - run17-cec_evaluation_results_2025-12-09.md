# Judge Report - run17-cec_evaluation_results_2025-12-09

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | qwen/qwen3-32b |
| **Source File** | run17-cec_evaluation_results_2025-12-09.md |
| **Judge** | Claude Code (Opus 4.5) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-09 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Total Score** | 293 / 300 |
| **Percentage** | 97.67% |
| **Avg Accuracy** | 4.90 / 5 |
| **Avg Completeness** | 4.87 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 24 |
| High (8-9/10) | 6 |
| Medium (5-7/10) | 0 |
| Low (0-4/10) | 0 |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| cec-001 | What are the panelboard space requirements... | 5/5 | 5/5 | 10/10 |
| cec-002 | What are California's electrical requirements for EV... | 5/5 | 5/5 | 10/10 |
| cec-003 | What are the California-specific electrical requirements for solar PV... | 5/5 | 5/5 | 10/10 |
| cec-004 | What circuit requirements does California have for heat pump... | 5/5 | 5/5 | 10/10 |
| cec-005 | What is required for electric cooktop readiness... | 5/5 | 5/5 | 10/10 |
| cec-006 | What are the panelboard requirements for electric clothes dryer... | 5/5 | 5/5 | 10/10 |
| cec-007 | What does CEC Table 240.4(G) specify that is unique... | 4/5 | 4/5 | 8/10 |
| cec-008 | What does CEC Table 242.3 specify for California... | 5/5 | 5/5 | 10/10 |
| cec-009 | What does CEC Table 430.72(B) specify for motor control... | 5/5 | 5/5 | 10/10 |
| cec-010 | What medium voltage cable tables does California have... | 5/5 | 5/5 | 10/10 |
| cec-011 | What is the ampacity of 4/0 AWG copper conductor at 75C... | 5/5 | 5/5 | 10/10 |
| cec-012 | What size equipment grounding conductor is required for 200A... | 5/5 | 5/5 | 10/10 |
| cec-013 | What size grounding electrode conductor is required for 3/0 AWG... | 5/5 | 4/5 | 9/10 |
| cec-014 | What is the temperature correction factor for a 75C rated... | 5/5 | 5/5 | 10/10 |
| cec-015 | What is the ampacity adjustment factor for 7-9 conductors... | 5/5 | 5/5 | 10/10 |
| cec-016 | What is the minimum working space depth for 480V... | 5/5 | 5/5 | 10/10 |
| cec-017 | What type of enclosure is suitable for outdoor use... | 4/5 | 5/5 | 9/10 |
| cec-018 | What is the general lighting load in VA per square foot... | 5/5 | 5/5 | 10/10 |
| cec-019 | What is the ampacity of a 12 AWG flexible cord... | 5/5 | 5/5 | 10/10 |
| cec-020 | What is the maximum operating temperature for Type SF-2... | 5/5 | 5/5 | 10/10 |
| cec-021 | Calculate the adjusted ampacity for 8 AWG THWN copper... | 5/5 | 5/5 | 10/10 |
| cec-022 | Size the conductors, EGC, and GEC for a 200A residential... | 4/5 | 5/5 | 9/10 |
| cec-023 | Calculate the general lighting load for a 5,000 sq ft office... | 5/5 | 5/5 | 10/10 |
| cec-024 | What is the maximum overcurrent protection for motor control... | 5/5 | 5/5 | 10/10 |
| cec-025 | Calculate the general lighting load for a 2,400 sq ft dwelling... | 5/5 | 5/5 | 10/10 |
| cec-026 | Compare the kitchen GFCI requirements between CEC and NEC... | 5/5 | 5/5 | 10/10 |
| cec-027 | Compare the panelboard space requirements between CEC and NEC... | 5/5 | 5/5 | 10/10 |
| cec-028 | Compare California's EV charging infrastructure requirements... | 5/5 | 4/5 | 9/10 |
| cec-029 | Compare the AFCI protection requirements between CEC and NEC... | 5/5 | 5/5 | 10/10 |
| cec-030 | Compare California's solar PV requirements with NEC 2023... | 4/5 | 5/5 | 9/10 |

---

## Detailed Results

### cec-001
**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies all 4 appliances (heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers) and cites CEC 408.2(A) and California Energy Code 150.0
**Completeness Notes:** Comprehensive with exception analysis verifying no exceptions modify the requirement

---

### cec-002
**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly covers CEC 625 requirements including dedicated circuits (625.40), connection methods (625.44), location requirements (625.50), GFCI (625.54), and CALGreen mandates
**Completeness Notes:** Very thorough coverage including weatherproofing, ventilation, and overcurrent protection requirements

---

### cec-003
**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All key points correct: rapid shutdown (690.56), arc-fault (690.11), grounding (690.43/45/47), voltage limits (690.7)
**Completeness Notes:** Comprehensive with circuit sizing (690.8), system identification (690.56), and exceptions for ground-mounted systems

---

### cec-004
**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly cites 408.2(A), 422.3(A), and California Energy Code 150.0(n)
**Completeness Notes:** Covers both single-family (408.2(A)) and multifamily (408.2(B)) requirements with exception analysis

---

### cec-005
**Question:** What is required for electric cooktop readiness in new California homes?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct citation of 422.3(A) and Energy Code 150.0(u)
**Completeness Notes:** Thorough coverage including multifamily (160.9(b)) and disconnecting means exceptions (422.33)

---

### cec-006
**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly covers 408.2(A)/(B), 422.3, Energy Code 150.0(v)
**Completeness Notes:** Comprehensive including grounding requirements (250.140) and exception verification

---

### cec-007
**Question:** What does CEC Table 240.4(G) specify that is unique to California?
**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies delta amendments and California-specific nature, but includes speculative interpretations about specific modifications for fire alarm systems
**Completeness Notes:** Good coverage of cross-references but could provide more concrete table contents

---

### cec-008
**Question:** What does CEC Table 242.3 specify for California installations?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct explanation of overvoltage protection requirements and equipment type references
**Completeness Notes:** Good detail on prohibited uses (242.6) and cross-references

---

### cec-009
**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly explains columns (A/B/C), conductor sizing, and application rules
**Completeness Notes:** Very thorough with both exceptions (hazardous circuits, transformer-fed) and practical examples

---

### cec-010
**Question:** What medium voltage cable tables does California have that are not in the NEC?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies 18 tables (311.60(C)(67) through 311.60(C)(86))
**Completeness Notes:** Includes adjustment factors (ambient temperature, burial depth, shield grounding)

---

### cec-011
**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 230 amperes - exact match with CEC Table 310.16
**Completeness Notes:** Includes adjustment requirements (310.15(B)/(C)) and overcurrent protection limits (240.4(D))

---

### cec-012
**Question:** What size equipment grounding conductor is required for a 200A circuit in California?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 6 AWG copper, 4 AWG aluminum - exact match with Table 250.122
**Completeness Notes:** Includes exceptions for luminaires (410.44) and conduit systems (352.60/356.60)

---

### cec-013
**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** 4 AWG copper - correct per Table 250.66
**Completeness Notes:** Missing aluminum option (2 AWG); otherwise includes exception analysis (250.54, 250.32)

---

### cec-014
**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 0.88 - exact match with Table 310.15(B)(1)(1)
**Completeness Notes:** Includes exception analysis confirming no modifications apply

---

### cec-015
**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 0.70 (70%) - exact match with Table 310.15(C)(1)
**Completeness Notes:** Includes NM cable exception (334.80) and conductor count rules (310.15(F))

---

### cec-016
**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 1.2 m (4 ft) - exact match with Table 110.26(A)(1)
**Completeness Notes:** Includes Condition 3 context (exposed live parts on both sides) and exception review

---

### cec-017
**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Lists 3S, 3SX, 4, 4X, 6, 6P - missing Type 3 and 3R from the complete list
**Completeness Notes:** Very detailed on enclosure properties (raintight, watertight, ice operability)

---

### cec-018
**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 1.3 VA per square foot - exact match with Table 220.12
**Completeness Notes:** Includes 220.12(B) exception for energy code compliance with monitoring

---

### cec-019
**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 25 amperes - exact match with Table 400.5(A)(1)
**Completeness Notes:** Includes explanation of Column B (2-conductor cords) and ambient temperature assumptions

---

### cec-020
**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 200C (392F) - exact match with Table 402.3
**Completeness Notes:** Includes usage restrictions from 402.12 and marking requirements (402.9)

---

### cec-021
**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 50A x 0.88 x 0.70 = 30.8A - perfect calculation with correct factors
**Completeness Notes:** Shows all steps with table references and termination temperature verification

---

### cec-022
**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** EGC (6 AWG) and GEC (4 AWG) correct. Service conductor uses Table 310.12(A) giving 2/0 AWG; expected used Table 310.16 giving 3/0 AWG. Both are technically valid approaches.
**Completeness Notes:** Complete with all three components and exception review

---

### cec-023
**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 5,000 x 1.3 = 6,500 VA - exact match
**Completeness Notes:** Includes exception analysis for alternative energy code calculations

---

### cec-024
**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 10 amperes per Column C - exact match with Table 430.72(B)
**Completeness Notes:** Includes both exceptions and confirms neither applies

---

### cec-025
**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** 2,400 x 3 = 7,200 VA - exact match
**Completeness Notes:** Correct code references (220.14(J)) and exception review

---

### cec-026
**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies NEC as more restrictive (CEC more permissive)
**Completeness Notes:** Detailed comparison of scope, exceptions, and practical implications

---

### cec-027
**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies CEC 408.2 requirements vs NEC having no equivalent
**Completeness Notes:** Detailed comparison table with all four appliance categories

---

### cec-028
**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correct comparison of anti-backfeed, truck parking, and enclosure requirements
**Completeness Notes:** Could more explicitly emphasize California MANDATES vs NEC provides optional rules

---

### cec-029
**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct showing similarities with nuanced differences in receptacle replacement requirements
**Completeness Notes:** Detailed comparison including wiring length limits and marking requirements

---

### cec-030
**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Correct technical comparison but doesn't strongly emphasize Title 24 Part 6 solar mandate
**Completeness Notes:** Very detailed on AC module exemptions, labeling, bonding, and battery charge control

---

## Category Performance

| Category | Questions | Avg Score |
|----------|-----------|-----------|
| CA Policy (Panelboard/EV/Heat Pump) | cec-001 to cec-006 | 10.0/10 |
| CA-Only Tables | cec-007 to cec-010 | 9.5/10 |
| CEC Delta Tables | cec-011 to cec-020 | 9.9/10 |
| Complex Calculations | cec-021 to cec-025 | 9.8/10 |
| CEC vs NEC Comparison | cec-026 to cec-030 | 9.6/10 |
