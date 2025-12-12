# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-09
**Model:** gemini-2.5-pro
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Successful** | 8 (26.7%) |
| **Failed** | 22 |
| **Total Duration** | 1614.0s |
| **Avg per Question** | 53.8s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2(A) requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers, as specified in California Energy Code Section 150.0(n), (t), (u), and (v). ...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in CEC Article 625 and Title 24 CALGreen (not CEC 408.2). Title 24 CALGreen mandates EV charging readi...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor for 200A Circuit (CEC 2022)

For a 200-ampere circuit in California, the required equipment grounding conductor (EGC) size is determined by the rating of the overcurrent protection device.

Based on the California Electrical Code, the minimum EGC sizes are:

*   **Copper:** **6 AWG**
*   **Aluminum or Copper-Clad Aluminum:** **4 AWG**

This requirement is specified in **CEC 2022, Table 250.122**, "Minimum Size Equipment Grounding Conductors for Grounding Raceway and Equipment." The table bases the size of the EGC on the rating of the automatic overcurrent device in the circuit ahead of the equipment.

It is important to note that if the ungrounded circuit conductors are increased in size (e.g., to compensate for voltage drop), the equipment grounding conductor must also be increased proportionately in size, as per CEC 250.122(B).

No common exceptions alter this specific requirement for a standard 200A circuit.

✓ Source: CEC 2022 Table 250.122

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.122

**Response Time:** 13.2s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Outdoor Enclosures for Rain, Sleet, and Ice (CEC 2022)

Based on a complete review of CEC 2022 Table 110.28 and related sections, several enclosure types are suitable for outdoor use where exposed to rain, sleet, and ice. The primary consideration is selecting a type that prevents water ingress and remains functional when covered with ice.

The following enclosure types provide protection against rain, sleet, and the external formation of ice:

*   **Type 3S / 3SX:** These enclosures are the most suitable for conditions with sleet. They are raintight and dusttight, and critically, their external mechanisms (like handles or buttons) are designed to **remain operable when the enclosure is covered in ice**. The "S" designation specifically indicates this protection against sleet. The "X" signifies added corrosion resistance.
*   **Type 4 / 4X:** These enclosures are rated as watertight and are intended for indoor or outdoor use. They protect against falling rain, splashing water, and even hose-directed water. Per Table 110.28, they are designed to be **undamaged by the external formation of ice**. The "X" indicates added corrosion resistance.
*   **Type 6 / 6P:** Offering the highest level of water ingress protection, these enclosures are rated for temporary (Type 6) or prolonged (Type 6P) submersion. They are inherently protected against rain and are also designed to be **undamaged by the external formation of ice**.

### Summary of Suitable Enclosures:

| Enclosure Type | Protection Level for Rain, Sleet, and Ice |
| :--- | :--- |
| **Type 3S, 3SX** | **Best for Sleet:** Raintight. External mechanisms are operable when ice-covered. |
| **Type 4, 4X** | **Watertight:** Protects against hose-directed water and is undamaged by external ice. |
| **Type 6, 6P** | **Submersible:** Provides the highest level of water protection and is undamaged by external ice. |

### Exceptions and Special Conditions

A search for exceptions to the general rules in Table 110.28 reveals ...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 110.28, 406.9

**Response Time:** 59.3s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for SF-2 Fixture Wire (CEC 2022)

According to the California Electrical Code, the maximum operating temperature for **Type SF-2** (Silicone insulated fixture wire — solid or 7-strand) is **200°C (392°F)**.

This is specified in **CEC 2022, Table 402.3 "Fixture Wires"**.

### Important Considerations:

While the wire insulation itself is rated for 200°C, the actual operating temperature must not exceed the lowest temperature rating of any connected component in the circuit. This is a critical safety requirement.

*   **General Rule**: "No conductor shall be used in such a manner that its operating temperature exceeds that designated for the type of insulated conductor involved." (CEC 2022, Section 310.14(A)(3)).
*   **Termination Limitation**: The temperature rating of a circuit is limited by the lowest-rated component, which is often the terminal lugs on a device or circuit breaker. Per CEC 2022, Section 110.14(C), unless a device is specifically marked for a higher temperature, terminals for circuits 100A or less are typically rated for 60°C, and circuits over 100A are typically rated for 75°C. Using a high-temperature wire like SF-2 does not permit you to exceed these termination limits.

In practice, a high-temperature wire like SF-2 is used in environments with high ambient heat, such as inside a luminaire, where its high insulation rating prevents degradation. However, its ampacity must still be calculated based on the lower temperature rating of its terminations.

✓ **Source**: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search, cec_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.14, 402.3, 310.14

**Response Time:** 53.2s

---


## Complex Calculations

### cec-021: adjusted_ampacity

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 x 0.88 x 0.70 = 30.8A

**CEC Ref:** CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1) | **NEC Ref:** NEC Tables 310.16, 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
No response generated

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 0 found
- None

**Response Time:** 72.3s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Conductor Sizing for a 200A California Residential Service (CEC 2022)

For a 200-amp single-phase residential service in California, the required copper conductors are sized as follows:

*   **Service Conductors**: **2/0 AWG** copper
    *   **Source**: CEC 2022, Table 310.12(A) (Single-Phase Dwelling Services and Feeders). This table is specifically used for 120/240-volt, single-phase dwelling services and allows for a smaller conductor size than would be required under the general ampacity tables.
    *   **Conditions & Exceptions**: The use of Table 310.12(A) is permitted under CEC 310.12, provided no ampacity adjustment or correction factors for ambient temperature or bundling are required. Exception No. 5 of CEC 230.90(A) explicitly permits overload protection for 120/240-volt single-phase dwelling services to be sized according to 310.12.

*   **Equipment Grounding Conductor (EGC)**: **6 AWG** copper
    *   **Source**: CEC 2022, Table 250.122. The EGC is sized based on the 200A rating of the main overcurrent protective device.
    *   **Conditions & Exceptions**: Per CEC 250.122(A), the EGC is not required to be larger than the circuit conductors supplying the equipment. In this case, 6 AWG is smaller than 2/0 AWG, so the rule is met. If the service conductors were increased in size (e.g., for voltage drop), the EGC would need to be increased proportionately per 250.122(B).

*   **Grounding Electrode Conductor (GEC)**: **4 AWG** copper
    *   **Source**: CEC 2022, Table 250.66. The GEC is sized based on the size of the largest ungrounded service-entrance conductors (2/0 AWG copper).
    *   **Conditions & Exceptions**: Per CEC 250.66, exceptions exist that may permit a smaller GEC. For example, if the *only* connection is to a rod, pipe, or plate electrode, the GEC is not required to be larger than 6 AWG copper (250.66(A)). If the *only* connection is to a concrete-encased electrode, the GEC is not required to be larger than 4 AWG copper (250.66(B)). Howe...

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 250.50, 250.122, 230.90, 310.12, 250.66

**Response Time:** 38.4s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The 125% continuous load multiplier is already included in this table value.

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Motor Control Circuit Protection (CEC 2022)

For a motor control circuit using **16 AWG copper conductors** that extend beyond the enclosure, the maximum rating of the overcurrent protective device is **10 amperes**.

This is determined by the specific rules for motor control circuits in the California Electrical Code.

### Code Breakdown

1.  **Governing Article**: Article 430 covers motors and motor circuits. Specifically, CEC 430.72(B)(2) addresses the protection of control circuit conductors by the main motor branch-circuit protective device.

2.  **Installation Method**: This section distinguishes between conductors that stay within the enclosure and those that extend beyond it. Your question specifies conductors "that extend beyond the enclosure," which is the more restrictive scenario.

3.  **Table Reference**: According to CEC 430.72(B)(2), for conductors extending beyond the enclosure, the overcurrent protection must not exceed the values listed in **Column C of Table 430.72(B)**.

4.  **Value from the Table**:
    *   **Conductor Size**: 16 AWG Copper
    *   **Applicable Column**: Column C (Conductors Extending Beyond Enclosure)
    *   **Maximum OCPD Rating**: **10 Amperes**

It is important to note that if the same 16 AWG conductors *did not* extend beyond the control equipment enclosure, they could be protected by an overcurrent device rated up to 40 amperes, as specified in Column B of the same table.

✓ Source: CEC 2022 Article 430, Section 430.72, and Table 430.72(B)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 430.72

**Response Time:** 34.7s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification. No...

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** FAIL

**Agent Answer:**
Error: 'list' object has no attribute 'startswith'

**Tool Usage:**
- CEC Tools: None
- NEC Tools: None
- CEC Primary: No

**Citations:** 0 found
- None

**Response Time:** 0s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
No response generated

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search, compare_with_nec, nec_exception_search
- CEC Primary: Yes

**Citations:** 0 found
- None

**Response Time:** 59.5s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements vs. NEC (CEC 2022) - Updated with Exceptions

While California's solar PV requirements in CEC Article 690 are largely harmonized with the NEC, the state implements significant amendments for firefighter safety, particularly in rapid shutdown and labeling. A key exception to the rapid shutdown rules exists for certain utility and large-scale structures.

### 1. California Energy Code (Title 24, Part 6) Mandate

The most fundamental difference is that California's Building Energy Efficiency Standards (Title 24, Part 6) mandate the installation of solar PV systems on nearly all new residential and nonresidential buildings. The NEC, as a model electrical safety code, has no such requirement. This mandate is a state energy policy implemented through the building code, with the electrical installation itself governed by the CEC.

### 2. Rapid Shutdown of PV Systems (CEC 690.12)

California has specific and detailed requirements for rapid shutdown systems to ensure that controlled conductors can be quickly de-energized to safe voltage levels for emergency responders.

**Key Requirements:**

*   **Boundary Definition:** The "array boundary" is defined as 1 foot from the array in all directions. The voltage limits differ for conductors inside versus outside this boundary.
*   **Voltage Limits Outside the Array:** Conductors outside the array boundary must be reduced to **not more than 30 volts within 30 seconds** of rapid shutdown initiation (CEC 690.12(B)(1)).
*   **Voltage Limits Inside the Array:** Conductors inside the array boundary must meet one of the following requirements (CEC 690.12(B)(2)):
    1.  Be part of a listed **PV hazard control system (PVHCS)**.
    2.  Be limited to **not more than 80 volts within 30 seconds** of initiation.
    3.  Have no exposed wiring or conductive parts and be installed more than 8 feet from exposed grounded conductive parts.
*   **Initiation Device:** For one- and two-family dwellings, the initia...

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_search, cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec, nec_search, nec_search, nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 690.56, 690.12

**Response Time:** 88.9s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 8/30
- **Success Rate**: 26.7%
- **Average Response Time**: 53.8s

### Model Information

- **Provider**: Groq
- **Model**: gemini-2.5-pro
- **Framework**: LangChain + LangGraph

