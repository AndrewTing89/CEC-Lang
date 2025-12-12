# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-09
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Successful** | 30 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 334.1s |
| **Avg per Question** | 11.1s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2(A) requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers, as specified in California Energy Code Section 150.0(n), (t), (u), and (v). ...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022)  

### **Panelboard Space Requirements**  
Per **CEC 2022 Section 408.2(A)**:  
- Panelboards in **single-family residential buildings** (1–2 dwellings) **must reserve circuit breaker spaces** for specific appliances as mandated by the California Energy Code.  

---

### **Required Reserved Circuit Breaker Spaces**  
The following appliances **must have designated spaces** in panelboards for single-family dwellings:  
1. **Heat pump water heaters**  
2. **Heat pump space heaters**  
3. **Electric cooktops**  
4. **Electric clothes dryers**  

**Citation**: CEC 2022 Section 408.2(A) and 440.3(E) (for heat pump space heaters).  
**Code Reference**: California Energy Code Sections 150.0(n), (t), (u), and (v).  

---

### **Exceptions Checked**  
- **No exceptions** were found that relax or modify the reserved space requirements in **Section 408.2(A)** for single-family dwellings.  
- Cross-referenced exceptions (e.g., 424.10, 426.14) apply to special permissions for non-standard equipment installation, not panelboard space reservations.  

---

### **Key Notes**  
- Compliance is mandatory for **new construction** and **major renovations** in California.  
- These requirements ensure future-ready electrical infrastructure for energy-efficient appliances.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 426.14, 424.10, 440.3, 150.0, 408.2

**Response Time:** 12.0s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in CEC Article 625 and Title 24 CALGreen (not CEC 408.2). Title 24 CALGreen mandates EV charging readi...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements (CEC 2022) – Final Answer  

### 1. **CALGreen Compliance**  
New residential construction must comply with **CALGreen Chapter 4, Division 4.1** and **Chapter 5, Division 5.1**, mandating **EV-ready infrastructure** (Section 625.1). This includes:  
- Reserved panelboard space for EV circuits.  
- Conduit to parking spaces.  
- Panel capacity to accommodate EV loads.  

---

### 2. **Ventilation Exception**  
**Exception to 625.1.1 (CALGreen):**  
- **No mechanical ventilation required** if:  
  - EVSE is **listed for indoor use without ventilation** (Section 625.52(A)).  
  - Or the equipment uses **electric vehicle storage batteries** (e.g., Tesla Powerwall).  
- **Otherwise**, mechanical ventilation (fans) with supply/exhaust to outdoors is required, interlocked with the charging circuit (Section 625.52(B)).  

---

### 3. **Key Requirements**  
| **Requirement**               | **Detail**                                                                 | **CEC Section**       |  
|-------------------------------|---------------------------------------------------------------------------|-------------------------|  
| **Dedicated Branch Circuit**  | Each EV outlet must have a **dedicated circuit** with no other outlets.   | 625.40                  |  
| **GFCI Protection**           | All EV charging receptacles require **ground-fault circuit-interrupter (GFCI)** protection. | 625.54                  |  
| **Receptacle Ratings**       | Portable EVSE must use listed receptacles rated up to **50A, 250V**.     | 625.44(A)               |  
| **Height Requirements**      | Indoor: **18 inches (450 mm)** above floor; Outdoor: **24 inches (600 mm)** above grade. | 625.50                  |  
| **Weatherproof Enclosures**  | Outdoor receptacles must use **listed, weatherproof enclosures**.         | 625.56                  |  
| **Overcurrent Protection**   | Power export systems must have **integral overcurrent protection**.      ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 9 found
- 625.1, 625.52, 625.60, 625.42, 625.40, 625.50, 625.54, 625.44, 625.56

**Response Time:** 12.9s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California Solar PV System Requirements (CEC 2022) with Exceptions

### 1. **Rapid Shutdown Requirements** [CEC 690.12]  
- **Voltage Limits**:  
  - **Outside array boundary**: ≤30V within 30 seconds.  
  - **Inside array boundary**: ≤80V within 30 seconds.  
- **Initiation Device**: Must be located **outside the building** for single-family homes. Requires visible "OFF" position.  
- **Labeling**: Permanent label at service equipment:  
  `SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN` (black on yellow, 9.5mm min. text).  

**Exception**:  
- **Ground-mounted systems** in detached structures (sole purpose: housing PV equipment) **exempt** from rapid shutdown requirements [690.12 Exception].  

---

### 2. **Grounding & Bonding** [CEC 690.43, 690.47]  
- **Grounding Electrode System**: Connect PV arrays to a grounding electrode system per [250.52](#).  
- **Equipment Grounding Conductors**: Sized per [250.122](#). For solidly grounded systems, grounded conductor must connect to a grounding electrode conductor sized per [250.166](#).  

---

### 3. **Wiring Methods** [CEC 690.31]  
- **Cable Types**: Use **Type PV wire** (UL 4703) or **DG cable** (UL 3003) for outdoor DC circuits.  
- **Labeling**: All PV DC circuits must be marked `PHOTOVOLTAIC POWER SOURCE` (white on red, 9.5mm min. text) on raceways, enclosures, and at 3m (10ft) intervals.  
- **Protection**: DC circuits >30V must be in metal raceways, MC cable, or metal enclosures (except for listed hazard control systems).  

**Exception**:  
- **Non-metallic enclosures/raceways** permitted for PV hazard control systems at building penetration points [690.31(D) Exception].  

---

### 4. **Arc-Fault Protection** [CEC 690.11]  
- **Requirement**: Listed PV arc-fault circuit interrupters for DC circuits ≥80V.  
- **Exception**: Ground-mounted systems in non-building structures exempt if in metallic raceways or underground.  

---

### 5. **Identification & Labeling** [CEC 690.56, 690.53]  
- **System Directo...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 13 found
- 690.47, 690.56, 710.15, 690.10, 250.166, 690.7, 690.12, 690.31, 250.122, 690.43

**Response Time:** 14.3s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Circuit Requirements for Heat Pump Water Heaters in California (CEC 2022)  

### **Key Requirements**  
1. **Dedicated Circuits**  
   - **Single-family buildings** (1–2 dwellings): Each dwelling unit must have **designated branch circuits** for heat pump water heaters as specified in **California Energy Code Section 150.0(n)**.  
   - **Multifamily buildings**: Dedicated circuits are required per **California Energy Code Section 160.9(b)**.  

2. **Panelboard Spaces**  
   - Panelboards must reserve **circuit breaker spaces** for heat pump water heaters in:  
     - **Single-family**: Per **CEC 408.2(A)** (aligns with Energy Code 150.0(n)).  
     - **Multifamily**: Per **CEC 408.2(B)** (aligns with Energy Code 160.9(b)).  

3. **Compliance with Other Articles**  
   - Follow **Article 430** (motor-operated appliances) and **Article 440** (refrigerant motor-compressors) as amended by CEC.  

---

### **Exceptions Checked**  
- **CEC 422.47**: Applies to temperature-limiting controls for water heaters (not circuit requirements).  
- **CEC 422.12**: Exceptions for central heating equipment (not applicable to water heaters).  

No exceptions override the dedicated circuit requirements for heat pump water heaters.  

---

### **Code Citations**  
- **CEC 2022 Section 422.3**: Mandates dedicated circuits and compliance with Energy Code for heat pump water heaters.  
- **CEC 2022 Section 408.2**: Requires panelboard spaces for heat pump water heaters in single- and multifamily buildings.  

---

### **Additional Notes**  
- Specific circuit sizing (ampacity, conductor size) follows the water heater’s nameplate requirements and **NEC 422.13** (storage-type water heaters).  
- Verify **California Title 24 Energy Code** (Sections 150.0(n) and 160.9) for exact details on receptacle locations and installation readiness.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 422.12, 422.47, 422.3, 422.13, 160.9, 150.0, 408.2

**Response Time:** 11.9s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness in New California Homes (CEC 2022)  

New California homes must comply with **CEC Section 422.3** for electric cooktop readiness:  

1. **Single-Family Homes** (1–2 dwellings):  
   - Each dwelling unit must have **dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 150.0(u)**.  
   - This includes designated spaces, receptacles, and branch circuits to support future electric cooktop installation.  

2. **Multifamily Buildings**:  
   - Each dwelling unit must have **dedicated circuits and circuit identifications** for electric cooktops per **California Energy Code Section 160.9(b)**.  

---

### Exceptions and Additional Considerations:  
- **CEC 422.33**:  
  - Allows **cord-and-plug-connected appliances** to use a separable connector or plug/receptacle as the disconnecting means.  
  - For ranges, a rear-base plug accessible via a drawer is permitted.  
  - Receptacle ratings must match the appliance’s rating.  

- **CEC 422.23**:  
  - Non-standard installation methods require **special permission**.  

---

### Key Notes:  
- The CEC 2022 **references the California Energy Code** (Sections 150.0 and 160.9) for specific requirements, as these details are not included in the CEC text itself.  
- Compliance ensures homes are pre-wired for electric cooktops, aligning with California’s electrification goals and building standards.  

✓ Source: CEC 2022 Sections 422.3, 422.33, 422.23

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 422.23, 422.3, 422.33, 160.9, 150.0

**Response Time:** 10.5s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryers (CEC 2022)  

### **Key Requirements**  
1. **Dedicated Circuit Breaker Spaces**:  
   - **Single-Family**: Panelboards must reserve spaces for dryers per **California Energy Code Section 150.0(v)** (CEC 408.2(A)).  
   - **Multifamily**: Spaces must comply with **California Energy Code Section 160.9(c)** (CEC 408.2(B)).  

2. **Dedicated Branch Circuits**:  
   - Dryers require **dedicated circuits** with proper labeling (CEC 422.3(A) and 422.3(B)).  

3. **Load Calculation**:  
   - Dryers are calculated at **5,000 VA** (or nameplate rating) per **CEC 220.54**.  

---

### **Exception Analysis**  
- **No exceptions** override the dedicated space/circuit requirements for dryers in **Section 408.2**.  
- Exceptions found (e.g., 408.38, 408.55) relate to **panelboard enclosures** and **wire-bending spaces**, not dryer-specific rules.  

---

### **Final Answer**  
California requires **dedicated panelboard spaces and branch circuits** for electric clothes dryers in new construction:  
- **Single-family**: Per CEC 408.2(A) and 422.3(A).  
- **Multifamily**: Per CEC 408.2(B) and 422.3(B).  
- **No exceptions** relax these requirements for dryers.  

✓ **Source**: CEC 2022 Sections 408.2, 422.3, 220.54.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 408.55, 220.54, 422.3, 408.38, 160.9, 150.0, 408.2

**Response Time:** 9.7s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) Unique California Provisions (CEC 2022)  

**CEC Table 240.4(G)** specifies overcurrent protection requirements for **specific conductor applications** with California amendments. The unique California provisions include:  

1. **Supply Cord of Listed Appliances/Luminaires**  
   - Permits use of flexible cord in listed appliances/luminaires **per listing requirements** (CEC 240.4(G)(1)).  
   - [CEC Amendment]: California mandates compliance with **Title 24 Part 6** energy efficiency standards for listed appliances, which may influence cord approvals.  

2. **Fixture Wire Tap Rules**  
   - Allows 18 AWG (up to 15 m) and 16 AWG (up to 30 m) on 15/20A circuits (CEC 240.4(G)(2)).  
   - [CEC Amendment]: California adds **CALGreen** requirements for energy-efficient lighting, restricting non-compliant fixture wire in new construction.  

3. **Extension Cords**  
   - 16 AWG minimum for 20A circuits in field-assembled cords (CEC 240.4(G)(4)).  
   - [CEC Amendment]: California bans certain extension cord types in residential construction per **Title 24, Section 110.12** (arc-fault protection for cords).  

---

### Exceptions Check:  
No direct exceptions to **Table 240.4(G)** were found in the CEC 2022. The returned exceptions apply to broader overcurrent protection rules (e.g., service conductors, busways) and do not modify Table 240.4(G) itself.  

---

### California-Specific Context:  
- **Title 24 Part 6** (Energy Efficiency): Requires listed appliances to meet efficiency standards, affecting cord approvals.  
- **CALGreen** (Sustainable Building Standards): Prohibits non-energy-efficient fixture wire in new buildings.  
- **Arc-Fault Protection** (CEC 210.12(D)): Extension cords in residential circuits must comply with AFCI requirements, not explicitly in NEC.  

✓ Source: CEC 2022, Title 24, CALGreen

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.12, 210.12, 240.4

**Response Time:** 9.9s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 242.3 - Overvoltage Protection Cross-Reference (California-Specific)

**Purpose**: Directs users to specific NEC articles containing overvoltage protection requirements for specialized equipment types in California installations. This is a **California amendment** (marked [N]) not present in the base NEC.

**Key Equipment-to-Article Cross-References**:
- **Class I locations** → Article 501
- **Class II locations** → Article 502
- **Emergency systems** → Article 700
- **Fire pumps** → Article 695
- **Wind electric systems** → Article 694
- **Information technology equipment** → Article 645
- **Equipment over 1000V** → Article 490

**Additional Notes**:
1. **California Amendment**: Table 242.3 is explicitly marked [N] in the CEC, indicating it's a new California-specific addition.
2. **No Direct Exceptions**: The `cec_exception_search` for **Section 242.3** returned no exceptions specific to Table 242.3 itself. However, related overvoltage protection limitations are found in **Section 242.6**, which prohibits SPD installation on:
   - Circuits over 1000 volts
   - Ungrounded/impedance grounded systems (unless listed)
   - Systems where SPD rating < phase-to-ground voltage

**Usage**: When designing or inspecting systems in California, this table identifies which additional NEC articles must be consulted for equipment-specific overvoltage protection requirements beyond the general rules in Article 242.

✓ Source: CEC 2022 Table 242.3 [N] (California amendment)

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 242.6, 242.3

**Response Time:** 11.4s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)  
**Complete with Application Rules and Exceptions**

---

### **Table Overview**  
Specifies maximum overcurrent protective device (OCPD) ratings for motor control circuits based on conductor size and installation conditions.  

| Conductor Size | Column A (Copper) | Column A (Aluminum) | Column B (Copper) | Column B (Aluminum) | Column C (Copper) | Column C (Aluminum) |  
|----------------|------------------|---------------------|-------------------|---------------------|-------------------|---------------------|  
| 18 AWG         | 7A               | —                   | 25A               | —                   | 7A                | —                   |  
| 16 AWG         | 10A              | —                   | 40A               | —                   | 10A               | —                   |  
| 14 AWG         | (Note 1)         | —                   | 100A              | —                   | 45A               | —                   |  
| 12 AWG         | (Note 1)         | (Note 1)            | 120A              | 100A                | 60A               | 45A                 |  
| 10 AWG         | (Note 1)         | (Note 1)            | 160A              | 140A                | 90A               | 75A                 |  
| >10 AWG        | (Note 1)         | (Note 1)            | (Note 2)          | (Note 2)            | (Note 3)          | (Note 3)            |  

---

### **Key Notes**  
1. **For conductors 14 AWG and larger**:  
   - Column A values are not explicitly listed. Use **Table 310.15** for ampacity calculations.  
2. **Column B (400% Rule)**:  
   - For conductors >10 AWG, use **400% of Table 310.17 (60°C conductors)**.  
3. **Column C (300% Rule)**:  
   - For conductors >10 AWG, use **300% of Table 310.16 (60°C conductors)**.  

---

### **Application Rules**  
1. **Column A**:  
   - For control circuits **not extending beyond** the motor control equipment e...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 310.17, 450.3, 725.43, 310.16, 430.72, 310.15

**Response Time:** 17.5s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in CEC 2022 (Not in NEC)

California's CEC 2022 includes **18 dedicated medium voltage (MV) cable ampacity tables** not found in the NEC. These are:

- **Tables 311.60(C)(67) through 311.60(C)(86)**  
  Provide ampacities for **Type MV cables rated 2001–35,000 volts** installed in cable trays, underground ducts, and direct burial. Key applications include:
  - **Cable trays**: Triplexed, isolated, or conduit-installed cables (Tables 67–76)
  - **Underground ducts**: Three-conductor or single-conductor cables (Tables 77–80)
  - **Direct burial**: Single or three-conductor cables (Tables 81–86)

### Exceptions and Limiting Rules
1. **Ambient Temperature Corrections** (311.60(D)(4)):  
   Ampacities must be adjusted for temperatures other than 40°C using correction factors or the provided equation.

2. **Shield Grounding**:  
   For cables with shields grounded at multiple points (Tables 69, 70, 81, 82), ampacities must be derated due to shield currents (Exception 311.60(D)(1)).

3. **Burial Depth Adjustments**:  
   Deeper burial than table values allows a 6% ampacity reduction per 1 ft (300 mm) depth increase (311.60(D)(2)(b)).

4. **Conductor Temperature Limits**:  
   Refer to **Table 311.10(A)** for maximum operating temperatures based on insulation type.

5. **Engineering Supervision**:  
   Tables may be overridden by engineering calculations under qualified supervision (311.60(A)(1)).

These tables are explicitly mandated for MV systems in California, whereas the NEC relies on engineering calculations for such applications. Always verify installation conditions (e.g., burial depth, shielding) against the table footnotes and cross-referenced sections.

✓ Source: CEC 2022 Sections 311.60, 311.10, and 311.60(D)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 311.60, 311.10

**Response Time:** 10.5s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer: Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

**Ampacity**: **230 amperes**  
Per CEC 2022 Table 310.16 for copper conductors at 75°C rating.

---

### Key Considerations:
1. **Overcurrent Protection Limit** (CEC 240.4(D)):  
   - Maximum overcurrent protection for 4/0 AWG copper is **250A** (not 230A).  
   - This is a **limiting rule** that restricts the overcurrent device size even if the ampacity is higher.

2. **Adjustment Factors** (Footnotes):  
   - If ambient temperature exceeds 30°C, apply correction factors from **CEC 310.15(B)**.  
   - If more than 3 current-carrying conductors are bundled, apply derating from **CEC 310.15(C)(1)**.

3. **Exceptions for Specific Equipment** (CEC 440.6):  
   - The 230A value applies to **general conductors**. For **hermetic refrigerant motor-compressors** or **multimotor equipment**, special rules in 440.6 may override standard ampacity calculations using nameplate data instead of Table 310.16 values.

4. **California Amendment**:  
   - The value includes [CEC] amendments to NEC Table 310.16. Verify specific modifications via `compare_with_nec("310.16")` if needed.

---

✓ Source: CEC 2022 Table 310.16, 240.4(D), 440.6

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.15, 440.6, 310.16, 240.4

**Response Time:** 8.0s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size (CEC 2022)

For a **200A circuit** in California:
- **Copper EGC**: 6 AWG (CEC Table 250.122)
- **Aluminum/Copper-Clad Aluminum EGC**: 4 AWG (CEC Table 250.122)

### Exceptions and Special Conditions:
1. **Replacement Luminaires** (CEC 410.44):  
   May connect EGC like replacement receptacles per 250.130(C) if no existing EGC exists.  
2. **DC Circuits** (CEC 250.134):  
   EGC can be run separately from circuit conductors.  
3. **Grounded Conductor Use** (CEC 250.142):  
   Equipment may be grounded using the grounded conductor in specific cases.  

⚠️ **California Amendment**: Table 250.122 includes state-specific modifications. Verify local amendments apply.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 250.134, 410.44, 250.130, 250.122, 250.142

**Response Time:** 8.3s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022) with Exceptions

For a **3/0 AWG copper service conductor**, the required **grounding electrode conductor (GEC)** size is:

**4 AWG copper**  
(Per CEC 2022 Table 250.66, California amendment applies)

### Exceptions Considered:
1. **250.66(A)**: Allows 6 AWG copper if connected only to rod/pipe/plate electrodes (not applicable here unless electrode type is specified).
2. **250.66(B)**: Allows 4 AWG copper for concrete-encased electrodes (valid if concrete-encased electrode is used).
3. **250.66(C)**: Ground ring-specific exception (not applicable unless ground ring is used).

No exceptions override the base rule for general electrode types. The California amendment confirms this requirement is formally adopted into CEC.

✓ Source: CEC 2022 Table 250.66 with exception review

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 8.1s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** at **40°C ambient temperature** is:

**0.88** (per CEC 2022 Table 310.15(B)(1)(1))

### Exception Review:
After checking for exceptions to Table 310.15(B)(1)(1), no applicable exceptions were found for temperature correction factors in this context. The exceptions returned relate to grounding conductor requirements in specific conduit types (Sections 352.60, 353.60, etc.), which are unrelated to temperature correction calculations.

This factor remains valid for adjusting ampacity based on ambient temperature.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 353.60, 352.60, 310.15

**Response Time:** 6.2s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor for Bundling (CEC 2022)

For **7-9 current-carrying conductors** in a raceway, the ampacity adjustment factor is **0.70 (70%)** per **CEC Table 310.15(C)(1)**. This is a California-specific amendment to the NEC.

### Exceptions Found:
1. **Section 334.80** (NM/NMC Cables):  
   - Applies to **NM/NMC cables** installed in contact with thermal insulation or in cable trays.  
   - Requires using Table 310.15(C)(1) adjustments **even if** the cables are not spaced.  
   - Does **not override** the 0.70 factor but adds context for specific cable types.

2. **Section 310.15(C)(1)**:  
   - Confirms the general rule for **all conductor types** (not just NM/NMC).  
   - No exceptions to the 0.70 factor for 7-9 conductors in standard raceways.

### Key Notes:
- **Application**: Multiply the base ampacity (from Table 310.16) by **0.70** when 7-9 conductors are bundled.  
- **California Amendment**: This table is identical to NEC 2023 Table 310.15(C)(1), but California enforces it for all applications without exception.  
- **Exclusions**: Grounding/bonding conductors are **not counted** (per 310.15(F)).  

### Footnote Clarification:
> "Number of conductors includes spares, neutrals, and grounding/bonding conductors, but excludes conductors connected to components that cannot be simultaneously energized."

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 334.80, 310.16, 310.15

**Response Time:** 8.6s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth (CEC 2022)

For a **480V panelboard under Condition 3**, the minimum working space depth is:

**1.2 meters (4 feet)**  
(CEC 2022 Table 110.26(A)(1), Voltage Range: 151–600V)

### Condition 3 Definition:
Exposed live parts on **both sides** of the working space.

### Exceptions Review:
1. **Section 110.26(E)** - Dedicates space requirements but does not override depth for Condition 3.
2. **Section 110.26(A)(1)** - Allows reduced depth only if Conditions 1/2/3 are met (Condition 3 is the most restrictive).
3. **Section 352.60/356.60** - Grounding exceptions unrelated to working space depth.

No exceptions override the **1.2 m (4 ft)** requirement for Condition 3 at 480V.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 352.60, 110.26, 356.60

**Response Time:** 8.2s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Final Answer: Suitable Enclosures for Outdoor Use (CEC 2022)

For outdoor use with **rain, sleet, and ice**, the following enclosures are suitable per **CEC Table 110.28**:

- **Type 3S** (Raintight, sleet-resistant, ice-covered operable)
- **Type 3SX** (Same as 3S with additional sealing)
- **Type 3X** (Raintight, sleet-resistant, ice-covered operable)
- **Type 4** (Watertight, dusttight, for wet and corrosive environments)
- **Type 4X** (Same as Type 4 with corrosion resistance)
- **Type 6** (Watertight for submersion up to 30 minutes)
- **Type 6P** (Watertight for submersion up to 30 minutes, with additional protection)

### Key Notes:
- **Mechanisms must remain operable when ice-covered** (explicitly required in Table 110.28 footnotes).
- **No exceptions** override these enclosure types for the specified conditions. The exceptions found (406.9, 110.26(E)) apply to receptacles and dedicated spaces, not the enclosure types themselves.

✓ Source: CEC 2022 Table 110.28 and exception search results

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.28, 406.9, 110.26

**Response Time:** 12.7s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for **office buildings** in California is **1.3 volt-amperes (VA) per square foot**, as specified in **CEC Table 220.12** for non-dwelling occupancies.

### Exceptions and Additional Notes:
1. **Energy Code Compliance Exception (220.12(B))**:  
   If the building complies with a local energy code and meets specific conditions (power monitoring system, alarm thresholds, 125% continuous load multiplier), the lighting load can be calculated using the energy code's unit values instead of 1.3 VA/sq ft.

2. **Receptacle Load for Office Buildings (220.14(K))**:  
   Receptacle loads in office buildings must be calculated as the larger of:  
   - (1) Calculated load from 220.14(I) with demand factors, or  
   - (2) **1 VA per square foot** (11 VA/m²).  
   *Note: This applies to receptacles, not general lighting loads.*

3. **Demand Factors (220.42)**:  
   Demand factors from Table 220.42 apply to general lighting loads **except** in specific areas like surgery suites, emergency departments, and critical care facilities (OSHPD 1 footnote).

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 220.12, 220.42, 220.14

**Response Time:** 9.8s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Final Answer - CEC 2022

The ampacity of a **12 AWG flexible cord** in **Column B (thermoset)** is **20 amperes** per **CEC Table 400.5(A)(1)**. 

### Exception Review:
- No exceptions apply to **Table 400.5(A)(1)** for flexible cord ampacity in this context.
- The exceptions found (352.60, 356.60, etc.) relate to grounding requirements, not ampacity adjustments.

✓ Source: CEC 2022 Table 400.5(A)(1)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 352.60, 400.5, 356.60

**Response Time:** 9.4s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

The maximum operating temperature for **Type SF-2 silicone insulated fixture wire** is **200°C (392°F)**, as specified in **CEC Table 402.3**. 

### Exception Review:
- **Section 402.9** only addresses marking requirements for thermoplastic wires (not silicone).
- **Section 402.12** prohibits using fixture wires as branch-circuit conductors (does not affect temperature rating).
- **Section 422.23** relates to appliance installation methods (not applicable here).

No exceptions override the 200°C maximum operating temperature specified in Table 402.3 for Type SF-2.

### Key Details from Table 402.3:
- **Type Letter**: SF-2  
- **Insulation**: Silicone rubber  
- **AWG Sizes**: 18–12 and 10  
- **Outer Covering**: Nonmetallic covering  
- **Application**: General fixture wiring  

This temperature rating applies to both solid/7-strand and flexible stranding configurations of Type SF-2 wire.

✓ Source: CEC 2022 Table 402.3

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 422.23, 402.12, 402.9, 402.3

**Response Time:** 10.5s

---


## Complex Calculations

### cec-021: adjusted_ampacity

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 x 0.88 x 0.70 = 30.8A

**CEC Ref:** CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1) | **NEC Ref:** NEC Tables 310.16, 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Final Adjusted Ampacity with Exceptions Considered (CEC 2022)

1. **Base Calculation**:  
   8 AWG THWN copper at 75°C = **50A** (Table 310.16)  
   Adjusted for 40°C ambient: 50A × 0.88 = **44A**  
   Adjusted for 7 conductors: 44A × 0.70 = **30.8A**

2. **Exception Review**:  
   - **Section 310.15(B)(2)**: No exception applies (rooftop temperature adder not relevant here).  
   - **Section 310.15(C)(1)**: Standard bundling adjustment already applied (0.70 factor).  
   - **Section 240.4(D)**: Overcurrent protection limit for 8 AWG copper is **40A** (Table 240.4(D)). Final adjusted ampacity (30.8A) is below this limit.  

3. **Temperature Termination Compliance**:  
   - THWN conductors are rated 75°C, but terminations (e.g., breakers) are typically 60°C or 75°C.  
   - Final ampacity (30.8A) complies with 110.14(C) temperature limitations.  

**Final Answer**: **30.8 amperes**  
✓ Source: CEC 2022 Tables 310.16, 310.15(B)(1), 310.15(C)(1), and Section 240.4(D)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 240.4, 310.16, 310.15, 110.14

**Response Time:** 11.7s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Verified

### Service Conductor Sizing (CEC 310.12(A))
- **Size**: 2/0 AWG copper  
- **Basis**: Table 310.12(A) for single-phase dwelling services (200A rating).  
- **Exception Check**:  
  - No applicable exceptions for standard residential services.  
  - Parallel conductor exceptions (310.12(G)) do not apply here.  

---

### Equipment Grounding Conductor (EGC) (CEC 250.122)
- **Size**: 6 AWG copper  
- **Basis**: Table 250.122 for 200A service.  
- **Exception Check**:  
  - No exceptions override this for residential services.  

---

### Ground Electrode Conductor (GEC) (CEC 250.66)
- **Size**: 4 AWG copper  
- **Basis**: Table 250.66 for 2/0 AWG service conductors.  
- **Exception Check**:  
  - Exception 1 allows smaller GECs only with AHJ approval (not applicable here).  

---

### California-Specific Compliance
- **CALGreen**: Grounding requirements met (Title 24 Part 6).  
- **Panel Readiness**: CEC 408.2 requires reserved spaces for future EV/solar circuits.  

✓ **Final Answer**:  
- **Service Conductors**: 2/0 AWG copper  
- **EGC**: 6 AWG copper  
- **GEC**: 4 AWG copper  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.12, 250.66, 408.2, 250.122

**Response Time:** 14.0s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The 125% continuous load multiplier is already included in this table value.

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)

For a **5,000 sq ft office building** in California:

1. **Base Rule**:  
   Per **CEC Table 220.12**, offices require **1.3 VA per square foot**.

2. **Exceptions Checked**:  
   - **Exception 220.12(B)** allows using energy code values *if*:
     - A power monitoring system is installed.
     - Demand factors from 220.42 are **not applied**.
     - 125% continuous load multiplier is used.  
   - **No evidence** in the question satisfies these conditions, so the standard 1.3 VA/sq ft applies.

3. **Calculation**:  
   $$
   5,000 \, \text{sq ft} \times 1.3 \, \text{VA/sq ft} = 6,500 \, \text{VA (6.5 kVA)}
   $$

**Final Answer**: **6,500 volt-amperes (6.5 kVA)**

✓ Source: CEC 2022 Section 220.12, Table 220.12

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 8.9s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Final Answer: Maximum Overcurrent Protection for 16 AWG Copper Motor Control Circuits

**Answer:**  
The maximum overcurrent protection for **16 AWG copper conductors** in motor control circuits is **10 amperes**, as specified in **CEC 2022 Section 240.4(D)(2)**.  

### Exceptions Checked:  
- **No applicable exceptions** modify this requirement for 16 AWG copper motor control circuits.  
- Exceptions in Sections 368.17, 230.90, 352.60, and 356.60 relate to busways, service conductors, or grounding, which are **not applicable** to this specific motor control circuit scenario.  

### Final Requirements:  
1. **Overcurrent Device**:  
   - **10A maximum** using:  
     - Branch-circuit-rated breakers **listed for 16 AWG copper**.  
     - Fuses **marked for 16 AWG copper** (Class CC/J/T).  
2. **Load Limit**:  
   - Continuous loads ≤ **8A** (80% of 10A).  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 240.4, 230.90, 368.17, 356.60, 352.60

**Response Time:** 10.4s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Dwelling Unit (CEC 2022)

**Final Calculation:**
```
2,400 sq ft × 3 VA/sq ft (per CEC 2022 220.14(J)) = 7,200 VA
```

**Exceptions Review:**
- **CEC 2022 220.14(J) Exception**: Confirms dwelling units require **3 VA/ft²** with no reduction allowed for general lighting load.
- Other exceptions (220.12, 220.52) apply to non-dwelling units or specific circuits (small-appliance, laundry), which are not relevant here.

**Citations:**
- **CEC 2022 Section 220.14(J)**: 3 VA/ft² for dwelling units.
- **No applicable exceptions** reduce this requirement for general lighting load.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 220.52, 220.12, 220.14

**Response Time:** 7.8s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## Final Answer: CEC 2022 vs NEC 2023 Kitchen GFCI Requirements

### **CEC 2022 Key Requirements**  
- **Scope**: GFCI required **only for countertop receptacles** (210.8(A)(6)).  
- **Exceptions**:  
  - Locking receptacles for ceiling fans/luminaires (if not general-purpose).  
  - Receptacles for refrigerators (under 210.52(B)(2)).  

### **NEC 2023 Key Requirements**  
- **Scope**: GFCI required for **countertop receptacles AND sink areas with food prep** (210.8(A)(5) and (6)).  
- **Exceptions**:  
  - HVAC equipment (until 2026).  
  - Weight-supporting ceiling receptacles (WSCR).  

---

### **Critical Exceptions Found**  
1. **CEC 210.8(A)(6) Exception**:  
   - Allows locking receptacles for ceiling fans/luminaires to omit GFCI if not general-purpose.  
   - **Limitation**: Does not extend to sink areas or additional kitchen appliances.  

2. **NEC 210.8(A)(5) Exception**:  
   - Excludes HVAC equipment (until 2026) but applies GFCI to broader kitchen zones.  

---

### **Which Code is More Restrictive?**  
**NEC 2023 is more restrictive** because:  
1. It mandates GFCI protection for **sink areas with food preparation** (e.g., dishwashers, sinks with disposals), which CEC 2022 does not explicitly cover.  
2. Its language explicitly includes **"areas with sinks and permanent provisions for food preparation"**, expanding coverage beyond countertops.  
3. Fewer exceptions for standard kitchen circuits compared to CEC.  

**Example**: A receptacle near a sink for a dishwasher requires GFCI under NEC but not CEC unless it’s within 6 ft of the sink (covered under 210.8(A)(7)).  

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.8

**Response Time:** 14.1s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification. No...

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Final Answer: Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023)

### **California-Specific Requirements (CEC 2022)**
- **408.2(A)** mandates **minimum circuit breaker spaces** in single-family dwellings for:  
  - Heat pump water heaters  
  - Heat pump space heaters  
  - Electric cooktops  
  - Electric clothes dryers  
  *No exceptions apply to this requirement for single-family dwellings.*  

---

### **Key Differences from NEC 2023**
1. **Appliance-Specific Spaces**  
   - **CEC**: Requires dedicated spaces for listed appliances (408.2A).  
   - **NEC**: No appliance-specific panelboard space requirements.  

2. **Wire-Bending Space Exceptions**  
   - **CEC 408.55**: Permits reduced wire-bending space for panelboards ≤225A with ≤42 devices.  
   - **NEC 312.6**: Requires full compliance with Table 312.6(B) without exceptions for device count.  

3. **Conduit Height Limit**  
   - **CEC 408.5**: Limits conduit height to 3 in. above enclosure bottom.  
   - **NEC**: No specific limit.  

---

### **Exception Search Results**
- **No applicable exceptions** were found for **CEC 408.2(A)** related to single-family dwellings.  
- Cross-referenced sections (424.10, 426.14, 440.8) pertain to heating, deicing, and HVAC systems—**not panelboard spaces**.  

---

### **Conclusion**
California’s CEC 2022 imposes **stricter, appliance-specific panelboard space requirements** not present in NEC 2023. Exceptions for wire-bending space (408.55) provide flexibility for smaller panelboards but do not affect the mandatory appliance spaces in 408.2(A).  

✓ **Source**: CEC 2022 Sections 408.2, 408.55; NEC 2023 Articles 408, 312.6.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 426.14, 312.6, 408.5, 424.10, 440.8, 408.55, 408.2

**Response Time:** 11.7s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## Final Answer: California EV Charging Requirements vs NEC 2023 (CEC 2022)

### **Key Differences with Exceptions Considered**

1. **Dedicated Branch Circuits (CEC 625.40)**  
   - **CEC**: *No exceptions* apply to the dedicated branch circuit requirement for EV charging. Each EV outlet must have its own circuit with no other outlets.  
   - **NEC 210.24**: Permits shared circuits but requires dedicated circuits for EVSE if supplied by a branch circuit rated ≥ 20A.  

2. **Ground-Fault Protection (CEC 625.54)**  
   - **CEC**: Mandates GFCI protection for all EV receptacles (no exceptions).  
   - **NEC 210.8(B)(9)**: Requires GFCI for EVSE receptacles rated ≤ 150V to ground.  

3. **Ventilation (CEC 625.52)**  
   - **CEC**: No exceptions to mechanical ventilation requirements for indoor EV charging. Ventilation must be interlocked with EVSE power.  
   - **NEC**: No ventilation requirements.  

4. **CALGreen Mandates (CEC 625.1.1)**  
   - **CEC**: New construction must include reserved panel spaces, conduit to parking, and minimum 40A circuits.  
   - **NEC**: No equivalent green building provisions.  

5. **Panelboard Reservations (CEC 408.2)**  
   - **CEC**: Requires reserved spaces for EV circuits in new panelboards.  
   - **NEC**: No such requirement.  

---

**Exceptions Check**:  
- Searched exceptions for **CEC 625.40** (dedicated circuits) but found no applicable exceptions. The returned exceptions (230.40) relate to service-entrance conductors, not EV branch circuits.  

**Conclusion**: California imposes stricter, more comprehensive requirements for EV infrastructure, including ventilation, green building mandates, and panelboard reservations, with no exceptions to core EV safety rules like dedicated circuits or GFCI protection.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 8 found
- 625.1, 625.52, 625.40, 625.54, 210.24, 210.8, 230.40, 408.2

**Response Time:** 14.8s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements: CEC 2022 vs NEC 2023 for Dwelling Units (Updated with Exceptions)

---

### **Key Exceptions in CEC 2022**
1. **Receptacle Replacement Requirements** (CEC 406.4(D)(4)):  
   - When replacing receptacles in AFCI-protected areas (per 210.12), the replacement must be:  
     - A listed outlet branch-circuit type AFCI receptacle, **or**  
     - A receptacle protected by a listed outlet branch-circuit type AFCI receptacle, **or**  
     - A receptacle protected by a listed combination-type AFCI circuit breaker.  
   - **Exception**: Section 210.12(D) exception does **not apply** to receptacle replacements (unlike general circuit modifications).  

2. **Marking Requirements**:  
   - First outlet box in a branch circuit must be **marked** to identify it as the first outlet (CEC 210.12(A)(3)(c), (A)(4)(c)).  

3. **Fire Alarm Exemption**:  
   - AFCI protection is **not required** for circuits supplying fire alarm systems installed per 760.41(B)/760.121(B), provided they are in metal raceways or encased in concrete (CEC 210.12(A) Exception).  

---

### **Updated Key Differences**

| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|---------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Receptacle Replacements** | **Strict requirement**: AFCI receptacles or protection for replacements in AFCI-protected areas (406.4(D)(4)). | **No specific requirement** for AFCI receptacles in replacements; general AFCI rules apply. |
| **Conductor Length Limits** | Explicit limits for supplemental AFCI systems: 14 AWG (50 ft), 12 AWG (70 ft). | No specific length limits mentioned.                                         |
| **First Outlet Marking**    | **Required** marking on first outle...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 404.22, 210.12, 210.11, 406.4, 760.121, 760.41

**Response Time:** 15.6s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements vs NEC 2023 Article 690 (CEC 2022) – **Updated with Exceptions**

---

### **Key Exception: Rapid Shutdown (690.12)**
**CEC 2022 Exception to 690.56(C):**  
- **Voltage Limits**:  
  - **Outside array boundary**: ≤30V within 30 seconds (690.12(B)(1)).  
  - **Inside array boundary**: ≤80V within 30 seconds (690.12(B)(2)).  
  ➔ *NEC 2023 690.12* has similar limits but lacks California's explicit **305mm (1ft)** array boundary definition.  

- **Ground-Mounted Exemption**:  
  - Ground-mounted systems entering buildings (solely for housing PV equipment) are exempt from rapid shutdown (690.12 Exception).  
  ➔ *NEC 2023* does not include this exemption.  

- **Hazard Control Systems**:  
  - Requires **UL 3741-listed** systems for arrays with exposed wiring (690.12(B)(2)(1)).  
  ➔ *NEC 2023* references UL standards but does not mandate specific listings.  

---

### **Updated Cross-Reference Rules**
1. **690.12(C)**:  
   - **Initiation Devices**: Must include **"RAPID SHUTDOWN"** labels in **white-on-red** (minimum 3/8" text).  
   - **Multi-System Buildings**: Allows up to **6 switches/breakers** in a single enclosure for rapid shutdown.  
   ➔ *NEC 2023* permits similar devices but lacks California's **color/size mandates** and **multi-switch limits**.  

2. **690.12(D)**:  
   - Requires **listed equipment** for rapid shutdown functions (e.g., switches, circuit breakers).  
   ➔ *NEC 2023* requires listed equipment but does not specify California's **field-labeling** requirements.  

---

### **Revised Summary of Differences**
| **Topic**               | **CEC 2022**                                                                 | **NEC 2023**                          |
|--------------------------|------------------------------------------------------------------------------|----------------------------------------|
| **Rapid Shutdown Voltage** | 30V/80V limits with array boundary (690.12)                                  | 30...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 690.56, 690.12

**Response Time:** 14.6s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 11.1s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

