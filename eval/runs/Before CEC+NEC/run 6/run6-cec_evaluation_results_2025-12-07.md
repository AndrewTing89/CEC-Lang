# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-07
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Successful** | 30 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 396.1s |
| **Avg per Question** | 13.2s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2 requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, (4) electric clothes dryers, and (5) electric vehicle charging equipment. This is a California-specific requirem...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022)  

**California Requirement (CEC 2022 Section 408.2(A)):**  
Panelboards in single-family residential buildings **must provide dedicated circuit breaker spaces** for:  
1. Heat pump water heaters  
2. Heat pump space heaters  
3. Electric cooktops  
4. Electric clothes dryers  

This requirement is mandated by California Energy Code Sections 150.0(n), 150.0(t), 150.0(u), and 150.0(v) to ensure future-ready electrical infrastructure for energy-efficient appliances.  

---

### **Exception Analysis**  
After checking for exceptions to **CEC 2022 Section 408.2(A)** using `cec_exception_search`, no direct exceptions were found that modify or override the reserved space requirements for the listed appliances. The returned exceptions (e.g., Sections 210.52, 422.23) pertain to receptacle installations and appliance circuits, not panelboard spaces.  

---

### **NEC 2023 Reference**  
This is a **California-specific requirement** [CEC]. The base NEC 2023 does not mandate reserved panelboard spaces for these appliances. California’s amendment ensures compliance with state energy efficiency goals.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 150.0, 210.52, 422.23, 408.2

**Response Time:** 13.2s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. CEC 408.2 requires panelboard spaces for EV charging equipment. Title 24 also mandates EV charging readiness.

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California's EV Charging Requirements for New Residential Construction (CEC 2022)  

**CEC 2022 Requirements with Exceptions Checked:**  
1. **Mandatory 240V Circuit**  
   - **CEC 625.5** requires new residential units to have a **dedicated 240V, 60A circuit** for EV charging (minimum).  
   - **Exception 5 (625.42):** Continuous load sizing applies; service/feeder must match EVSE ratings.  

2. **Panelboard Reserved Spaces**  
   - **CEC 408.2** mandates panelboards have **reserved spaces** for future EV circuits.  
   - **Exception 1 (408.38):** Panelboards accessible only to qualified personnel may bypass standard dead-front requirements.  

3. **GFCI Protection**  
   - **CEC 210.11** requires **GFCI protection** for all EV receptacles.  
   - **Exception 1 (210.8):** Receptacles not readily accessible (e.g., for snow-melting) may skip GFCI if dedicated to specific equipment.  

4. **Overcurrent Protection**  
   - **CEC 240.6** enforces standard overcurrent rules for EV circuits.  
   - **Exception (370.23):** Cablebus overcurrent protection may follow 240.100/101 for specialized systems.  

---

## NEC 2023 Reference  
- **NEC 625.5** only requires a **120V, 20A circuit** for residential EV readiness.  
- **California amendments** (CEC) **upgrade this to 240V, 60A** and add panel reserved spaces, stricter GFCI rules, and continuous load sizing.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 9 found
- 370.23, 408.38, 625.5, 210.11, 210.8, 240.100, 240.6, 625.42, 408.2

**Response Time:** 13.3s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California-Specific Electrical Requirements for Solar PV Systems on New Residential Construction (CEC 2022)

### Key CEC Requirements:
1. **Voltage Limits**  
   - **Maximum DC Voltage**:  
     - For residential systems (one- and two-family dwellings), PV dc circuits must not exceed **600 volts** (CEC 2022 690.7).  
     - For non-residential systems, the limit is **1000 volts**.  
   - **Voltage Calculations**:  
     - Use temperature correction factors (Table 690.7(A)) for crystalline silicon modules to account for low ambient temperatures.  
     - Systems ≥100 kW require a licensed engineer's documented design.

2. **Arc-Fault Protection**  
   - **Mandatory**: All PV systems with dc circuits ≥80V must have **listed PV arc-fault circuit interrupters** (CEC 690.11).  
   - **Exception**: Systems installed in metallic raceways, metal-clad cables, or enclosed metal trays (e.g., ground-mounted systems) are exempt.

3. **Circuit Sizing and Overcurrent Protection**  
   - **Conductor Sizing**:  
     - Conductors must be sized for **125% of the maximum current** (690.8(B)(1)).  
     - Example: For a 20A circuit, use conductors rated for at least 25A.  
   - **Overcurrent Devices**:  
     - Rated for **125% of calculated current** (690.9(B)(1)).  
     - Exception: Listed assemblies operating at 100% of their rating may use 100% (e.g., some inverters).

4. **Grounding and Bonding**  
   - **Equipment Grounding**:  
     - PV module frames and metal supports must be bonded per **250.134/250.136** (690.43).  
     - Grounding electrode connections required per **250.52/250.54** (690.47).  
   - **Grounded-Fault Protection**:  
     - Solidly grounded systems must connect to a grounding electrode system (690.47(A)(2)).

5. **Rapid Shutdown Requirements**  
   - **Mandatory for PV systems on buildings**:  
     - **Voltage Limits**:  
       - **≤30V** within 30 seconds outside the array boundary (1 ft from array).  
       - **≤80V** within 30 seconds inside the ar...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 14 found
- 250.52, 690.7, 690.13, 690.8, 690.43, 690.47, 690.12, 210.12, 310.15, 690.9

**Response Time:** 12.5s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Circuit Requirements for Heat Pump Water Heaters in California (CEC 2022)  

**California Requirements:**  

1. **Single-Family Dwellings (1-2 units):**  
   - **Panelboard Requirements (408.2(A)):** Panelboards must include **dedicated circuit breaker spaces** for heat pump water heaters as specified in California Energy Code §150.0(n).  
   - **Appliance Readiness (422.3(A)(1)):** Each dwelling unit must have **designated branch circuits, receptacles, and circuit identifications** for heat pump water heaters per Energy Code §150.0(n).  

2. **Multifamily Dwellings:**  
   - **Panelboard Requirements (408.2(B)):** Panelboards must include **dedicated circuit breaker spaces** for heat pump water heaters as specified in California Energy Code §160.9(a).  

3. **General Installation (422.3):**  
   - Motor-operated appliances (including heat pump water heaters) must comply with **Article 430** (motor circuits) and **Article 440** (HVAC equipment) requirements, unless amended by CEC.  

---

### Exceptions and Special Conditions  
- **422.12 (Central Heating Equipment):**  
  - Heat pump water heaters must be supplied by an **individual branch circuit**.  
  - **Exception 1:** Auxiliary equipment (e.g., pumps, humidifiers) may share the same branch circuit.  
  - **Exception 2:** Permanently connected air-conditioning equipment may share the circuit.  

- **422.47 (Water Heater Controls):**  
  - Storage or instantaneous water heaters must have a **temperature-limiting means** (e.g., trip-free thermostat).  
  - **Exceptions:** Applies only to water heaters rated for ≥82°C (180°F) or ≥60 kW (storage) or ≤4 L (instantaneous).  

- **424.10 (Special Permission):**  
  - Non-standard installations require **special permission** from the authority having jurisdiction.  

---

### NEC 2023 Comparison  
The base NEC 2023 does **not** mandate **pre-wired dedicated circuits** for heat pump water heaters in dwelling units. California’s requirements in **408.2 and 422.3** are...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 422.12, 422.3, 160.9, 422.47, 150.0, 424.10, 408.2

**Response Time:** 10.1s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness Requirements (CEC 2022)  
**Primary Rule (Section 422.3):**  
California requires new residential buildings to include **electric cooktop readiness** with:  
1. **Dedicated 240V circuits** (minimum 40A service)  
2. **Panelboard space reserved** for future installation  
3. **Conduit/raceway pre-installed** to the cooktop location  
4. **Minimum 8 AWG copper conductors**  

**Exceptions Found:**  
1. **Section 422.23** – Allows non-standard installation methods *only with special permission* (not applicable to standard readiness requirements).  
2. **Section 422.33** – Permits cord-and-plug-connected appliances to use demand factors for receptacle ratings. This applies to *existing appliances* but does not override the readiness mandates in 422.3 for new construction.  

**Key Compliance Notes:**  
- Exceptions 422.23 and 422.33 address *installation methods* and *disconnection requirements*, not the core readiness provisions.  
- Readiness requirements (dedicated circuits, panel space, etc.) remain mandatory regardless of appliance type.  

---
## NEC 2023 Reference  
NEC 2023 does **not** include "readiness" requirements for future appliances. California’s CEC provisions are **amendments specific to California** [CEC]. NEC only requires:  
- 240V circuits for cooking appliances (NEC 210.52(K)).  
- Minimum 20A small-appliance branch circuits (NEC 210.52(B)).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 422.3, 422.23, 422.33, 210.52

**Response Time:** 10.7s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryers in California New Construction (CEC 2022)

**California Requirements:**
1. **Dedicated Circuit Breaker Spaces**  
   Per **CEC 2022 Section 408.2(A)** and **408.2(B)**:
   - **Single-family buildings** (1-2 dwellings): Panelboards must include dedicated circuit breaker spaces for electric clothes dryers as specified in California Energy Code Section 150.0(v).
   - **Multifamily buildings**: Panelboards must include dedicated spaces for electric clothes dryers per California Energy Code Section 160.9(c).

2. **Circuit Readiness**  
   Per **CEC 2022 Section 422.3(A)** and **422.3(B)**:
   - **Single-family**: Dryer circuits must have dedicated circuits and circuit identifications (e.g., labeled "Dryer") as per Energy Code 150.0(v).
   - **Multifamily**: Dryer circuits must include dedicated circuits and identifications per Energy Code 160.9(c).

3. **Load Calculation**  
   Per **CEC 2022 Section 220.54**:  
   Dryer load must be calculated at **5000 VA minimum** (or nameplate rating, whichever is larger) for dwelling units.

4. **Exceptions and Special Cases**  
   - **Multifamily buildings with shared laundry facilities**:  
     Per **Exception to 210.52(F)**, individual dryer circuits/receptacles are **not required** in multifamily units if on-site laundry facilities are provided for all occupants.  
   - **No laundry facilities**:  
     Per **Exception to 210.52(F)**, dryer circuits are not required in non-one-family dwellings where laundry facilities are not to be installed or permitted.  

---

## NEC 2023 Reference  
The base NEC does **not** mandate dedicated panelboard spaces for future dryer circuits. California’s CEC adds these requirements to align with energy code readiness provisions.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 422.3, 160.9, 150.0, 220.54, 210.52, 408.2

**Response Time:** 11.7s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Final Verification and Answer

**California-Specific Enforcement of CEC Table 240.4(G):**  
While CEC Table 240.4(G) mirrors NEC in structure, **California amendments in related sections** (e.g., 242.54, 250.54, 240.21(C)) impose unique enforcement requirements. These amendments affect how the table’s cross-references (e.g., to Articles 440, 760) are applied, particularly in:

1. **Surge Arrester Grounding (242.54):**  
   - Requires specific interconnections for transformer secondary systems, impacting overcurrent protection for related conductors (e.g., fire alarm circuits).

2. **Transformer Secondary Conductors (240.21(C)):**  
   - Limits reliance on primary overcurrent devices for secondary conductor protection, affecting applications like motor circuits referenced in Table 240.4(G).

3. **Grounding Electrode Modifications (250.54):**  
   - Permits auxiliary grounding electrodes, which may alter overcurrent protection designs for systems like control circuits.

**Conclusion:**  
CEC Table 240.4(G) itself has no explicit amendments, but **California’s delta notes and related sections enforce stricter interpretations** of referenced articles compared to NEC. Inspectors in California must apply these amendments when using the table’s cross-references.

---
## NEC 2023 Reference  
No differences in table structure. California amendments affect referenced section enforcement.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 240.21, 250.54, 242.54, 240.4

**Response Time:** 17.2s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC 2022 Table 242.3 Requirements (California)  
**Verified via cec_search, cec_lookup_table, and cec_exception_search**  

**CEC Table 242.3** is a California-specific cross-reference table added to Article 242 (Overvoltage Protection). It directs users to other NEC articles containing overvoltage protection requirements for specific equipment types. This table is marked with a [CEC] amendment and does not exist in the base NEC.  

**Key Equipment-to-Article Cross-References:**  
- **Class I locations** → Article 501  
- **Emergency systems** → Article 700  
- **Fire pumps** → Article 695  
- **Information technology equipment** → Article 645  
- **Wind electric systems** → Article 694  
- **Receptacles** → Article 406  
- **Outdoor overhead conductors >1000V** → Article 399  

**Code Basis:**  
- CEC 2022 Section 242.3 explicitly references this table for overvoltage protection requirements.  

**Exceptions Checked:**  
- No exceptions apply directly to Table 242.3 itself.  
- A related exception exists in **CEC Section 370.23** for cablebus overcurrent protection (not overvoltage), permitting alternative overcurrent protection methods per 240.100/240.101. This is unrelated to Table 242.3’s scope.  

---
## NEC 2023 Reference  
The base NEC 2023 **does not include Table 242.3**. This cross-reference table is a California-specific addition [CEC] to clarify which other articles contain overvoltage protection requirements for specific equipment types.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 242.3, 240.100, 240.101, 370.23

**Response Time:** 17.5s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (With Exceptions)

**CEC 2022 Specification:**
Table 430.72(B) defines **maximum overcurrent protective device ratings** for motor control circuits based on conductor protection scenarios:

1. **Column A** - *Separate Overcurrent Protection*  
   - Required when the motor branch-circuit protective device does not provide adequate protection.  
   - Ratings derived from conductor ampacity tables (see Notes 1-3 for 300-400% multipliers).

2. **Column B** - *Branch-Circuit Protection (Within Enclosure)*  
   - Permits the motor branch-circuit device to protect conductors **if they do not extend beyond the motor control equipment**.  
   - Ratings limited to values in Column B.

3. **Column C** - *Branch-Circuit Protection (Beyond Enclosure)*  
   - Applies when conductors extend beyond the motor control equipment.  
   - More restrictive ratings in Column C apply.

---

### **Critical Exceptions:**
1. **Exception No. 1** (430.72(B)):  
   - **Hazardous applications** (e.g., fire pump motors) require **only short-circuit and ground-fault protection**, not full overcurrent protection.  
   - Control circuits critical to life safety systems are exempt from standard overcurrent rules.

2. **Exception No. 2** (430.72(B)):  
   - **Transformers** supplying control circuits may use **primary-side overcurrent protection** if:  
     - The transformer is single-phase with a two-wire secondary.  
     - Primary protection does not exceed secondary-rated protection multiplied by the voltage ratio.  
   - Secondary conductors (non-two-wire) must have their own protection.

3. **Combined Protection** (430.55):  
   - Overload and fault-current protection may be combined in a single device if it meets overload requirements (430.32).

---

### **Cross-Reference Requirements:**
- **Conductor Ampacity** (Notes 1-3):  
  - Column values depend on **Table 310.16/310.17** ampacities for 60°C conductors.  
  - Example: A...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 310.16, 430.72, 430.55, 310.17, 430.32

**Response Time:** 11.5s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in California (CEC 2022) with Exceptions

California’s CEC includes **medium voltage cable ampacity tables** (2001–35,000 volts) not found in the NEC, with specific exceptions affecting their application:

---

### **1. CEC 311.60(C)(67)–(C)(86): Medium Voltage Cable Ampacities**
- **Scope**: Ampacities for copper and aluminum conductors in air, underground ducts, and direct burial.
- **Key Exceptions**:
  - **Engineering Supervision**: Ampacities can be determined via tables **or** engineering calculations (311.60(A)(1)).
  - **Circuit Length Adjustments**: If a circuit has segments with different ampacities, the **higher** value is permitted if the lower segment is ≤ 10 ft (3.0 m) or 10% of the total length (Exception to 311.60(A)(2)).

---

### **2. CEC 392.80: Cable Tray Installations**
- **Derating Rules**: 
  - Multiconductor cables in covered trays: 95% of Table 311.60(C) values.
  - Single-conductor cables in covered trays: 70–75% derating (size-dependent).
- **Exception**: Cables in **uncovered trays with spacing** may use free-air ampacities (392.80(A)(1)(c)).

---

### **3. Shielding and Installation Exceptions**
- **Shielding Requirements**:
  - Shielded cables must have **grounded shields** (311.44). Nonshielded cables up to 2400V are allowed in industrial settings with qualified personnel (Exception No. 1).
  - Direct-burial cables must be shielded unless they have a metallic sheath (311.36 Exception No. 1).

- **Direct-Burial Exceptions**:
  - Nonshielded multiconductor cables rated 2001–2400V are permitted with an **overall metallic sheath** (311.36 Exception No. 1).

---

### **4. Cable Tray Fill Limits (CEC 392.22)**
- **Fill Area Limits**: Tables specify maximum fill for different tray types (ladder, ventilated, solid bottom).
- **Exception**: Solid-bottom trays with cables ≥4/0 AWG must be installed in a **single layer** (392.22(A)(3)(a)).

---

### **Comparison with NEC**
- The **NEC 2023** lacks equivalent tables ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 311.44, 311.36, 311.60, 392.80, 392.22

**Response Time:** 12.3s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

**California Requirement (CEC 2022):**
- **Ampacity:** 230 amperes for 4/0 AWG copper at 75°C per **CEC 2022 Table 310.16**.
- **Key Exceptions Checked:**
  1. **Parallel Conductors (310.16 exceptions):** Not applicable here since the question does not involve parallel conductor installations.
  2. **Dwelling Service Conductors (310.12):** Not applicable as this question pertains to general conductor ampacity, not dwelling service sizing.
  3. **Continuous Load Requirements (210.19):** This applies to load calculations, not direct ampacity table values. The 230A value remains valid for the specified conditions.

**No applicable exceptions** modify the base ampacity of 230A for 4/0 AWG copper at 75°C under standard conditions (30°C ambient, ≤3 conductors).

---
## NEC 2023 Reference
NEC 2023 Table 310.16 also specifies **230A for 4/0 AWG copper at 75°C**. No difference from CEC 2022 in this specific ampacity value.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.12, 310.16, 210.19

**Response Time:** 10.0s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size (CEC 2022)  

For a **200A circuit** in California, the required equipment grounding conductor (EGC) sizes are:  

- **Copper**: **6 AWG**  
- **Aluminum/Copper-Clad Aluminum**: **4 AWG**  

This is specified in **CEC 2022 Table 250.122**, which includes a California amendment ([CEC]) but does not alter the EGC sizing for 200A circuits.  

---

### Exception Analysis  
After reviewing exceptions to **CEC 2022 Section 250.122**, no applicable exceptions modify the EGC sizing for this scenario:  
1. **Section 250.142** allows using the grounded conductor for grounding in specific supply-side or load-side cases, but the user’s question does not involve these conditions.  
2. **Section 352.60/356.60** references exceptions for DC circuits or separately run grounding conductors, which are not relevant here.  
3. **Section 250.121** and **250.54** address alternative grounding methods (e.g., structural frames, auxiliary electrodes) but do not affect EGC sizing for standard 200A circuits.  

No exceptions override the Table 250.122 requirements for this case.  

---

## NEC 2023 Reference  
No difference from NEC 2023. The EGC sizes for a 200A circuit remain **6 AWG copper** or **4 AWG aluminum** per NEC Table 250.122.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 250.142, 250.121, 356.60, 250.54, 250.122, 352.60

**Response Time:** 9.8s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022)  
**Standard Requirement:**  
For a **3/0 AWG copper service conductor**, the minimum grounding electrode conductor (GEC) size is **4 AWG copper** per **CEC 2022 Table 250.66**.  

**Exceptions and Special Conditions:**  
1. **If connected to a rod, pipe, or plate electrode** (per 250.52(A)(5) or (A)(7)):  
   - GEC may be reduced to **6 AWG copper** or **4 AWG aluminum** (per **250.66(A)**).  
2. **If connected to a concrete-encased electrode** (per 250.52(A)(3)):  
   - GEC may be reduced to **4 AWG copper** (per **250.66(B)**).  
3. **If connected to a ground ring** (per 250.52(A)(4)):  
   - GEC size matches the ground ring conductor (per **250.66(C)**).  

**California Amendment:**  
These requirements include California-specific modifications [CEC] from the base NEC, particularly in Table 250.66 sizing and exception applicability.  

**NEC 2023 Reference**  
The NEC 2023 (Article 250.66) specifies the same 4 AWG copper for 3/0 AWG service conductors. Exceptions for electrode types (rod, concrete-encased, ground ring) are also present in NEC but are explicitly reinforced in CEC with [CEC] markings.  

**Final Answer:**  
- **Standard GEC size:** 4 AWG copper (per Table 250.66).  
- **Reduced sizes permitted** if connected to specific electrodes (see exceptions above).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 250.52, 250.66

**Response Time:** 12.8s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)  

For a 75°C rated conductor at 40°C ambient temperature:  

**Correction Factor:** 0.88  
**Source:** CEC 2022 Table 310.15(B)(1)(1)  

**Exceptions/Notes from CEC 2022:**  
1. **Exception for Type XHHW-2 Insulated Conductors:**  
   - Not subject to ampacity adjustments for rooftop temperatures (does not apply here).  
2. **Key Notes:**  
   - Correction factors apply to ambient temperatures other than 30°C (86°F).  
   - Ensure corrected ampacity does not exceed termination temperature limits (110.14(C)).  
   - See Table 310.4(A)/4(B) for conductor insulation types and temperature ratings.  

No exceptions override the 0.88 factor for this scenario.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The temperature correction factor for 40°C ambient with 75°C conductors is also **0.88** per NEC Table 310.15(B)(1)(1).  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 310.4, 110.14

**Response Time:** 8.5s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor (CEC 2022)

For **7-9 current-carrying conductors** in a raceway, the ampacity adjustment factor is **0.70** per **CEC 2022 Table 310.15(C)(1)**.

**Key Exceptions Checked:**
1. **No applicable exceptions** override this adjustment factor for general bundling scenarios.
2. Exceptions in 310.15 relate to:
   - Rooftop temperature adjustments (not applicable here)
   - Parallel conductor requirements (not relevant to standard bundling)
   - Special conductor types (e.g., Type XHHW-2) which don't apply to typical installations

**Footnote:**  
The count includes *all conductors in the raceway* (including spares, neutrals, and grounding/bonding conductors) unless they cannot be simultaneously energized (per 310.15(E) and (F)).

---
## NEC 2023 Reference  
No difference from NEC 2023. Same adjustment factor of 0.70 applies for 7-9 conductors per NEC Table 310.15(C)(1).

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 31.6s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth for 480V Panelboard (Condition 3) - CEC 2022

**California Requirement (CEC 2022):**
Per **CEC 2022 Table 110.26(A)(1)**, the minimum working space depth for a 480V panelboard under **Condition 3** (exposed live parts on both sides of the working space) is **914 mm (36 inches)**. This applies to systems operating at 600V or less.

**Key Details:**
- **Condition 3** requires **36 inches (914 mm)** depth for voltages up to 600V.
- This depth is measured from the live parts or enclosure front to ensure safe access for maintenance.
- No exceptions apply for standard panelboard installations in this scenario.

**Exceptions Checked:**
- **Exception 1 (110.26(A)(1)(a)):** Applies to dead-front assemblies (e.g., switchgear with no rear adjustable parts). Not applicable here.
- **Exception 2 (110.26(A)(1)(b)):** Permits smaller spaces for low-voltage equipment (≤30V AC/RMS, ≤60V DC). Not applicable to 480V.
- **Exception 3 (110.26(A)(1)(c)):** Applies to existing buildings with controlled access during equipment replacement. Not relevant to new installations.

---
## NEC 2023 Reference
No difference from NEC 2023. The same 36-inch (914 mm) depth requirement applies under NEC Table 110.26(A)(1) for 480V panelboards under Condition 3.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 14.7s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Suitable Enclosure Types for Outdoor Use (CEC 2022 Table 110.28)  
**With Exceptions and Cross-References Applied**

**California Requirement (CEC 2022):**  
For outdoor electrical equipment exposed to rain, sleet, and ice, **raintight** or **watertight** enclosures are required per Table 110.28. The suitable enclosure types are:  

- **Type 3 (Raintight):** Protects against rain, sleet, and ice formation.  
- **Type 3S (Raintight, Sleet Resistant):** Adds sleet protection.  
- **Type 3SX (Raintight, Sleet Resistant, Snow Load):** For heavy snow loads.  
- **Type 3X (Raintight, Corrosion Resistant):** For corrosive environments.  
- **Type 4 (Watertight):** Protects against rain, sleet, ice, and hose-directed water.  
- **Type 4X (Watertight, Corrosion Resistant):** Same as Type 4 but for corrosive environments.  
- **Type 6 (Dusttight and Watertight):** For dust and water exposure.  
- **Type 6P (Dusttight, Watertight, Pest Protection):** Adds pest protection.  

**Key Exceptions and Cross-References:**  
1. **Dedicated Outdoor Spaces (110.26(E)):**  
   - Enclosures must be installed in **dedicated spaces** with 1.8 m (6 ft) of clearance above the equipment.  
   - Protected from accidental contact by unauthorized personnel or vehicular traffic.  

2. **Vault/Enclosure Security (110.31):**  
   - Outdoor installations accessible only to qualified persons require **fencing** (≥2.1 m/7 ft) or locked enclosures.  
   - Fences must comply with Table 110.31 clearance distances to live parts.  

3. **Personnel-Entry Enclosures (110.70):**  
   - Enclosures designed for personnel entry must provide **safe work space** for energized equipment maintenance.  

**Implementation Notes:**  
- Enclosures must be **marked with their type** (e.g., Type 4X) to ensure compliance.  
- Watertight types (4, 4X, 6, 6P) are preferred in ice-prone areas due to higher ingress protection.  
- Dusttight enclosures (Types 3, 3S, 3SX, 3X, 4, 4X, 6, 6P) are required if dust is a concern.  
...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 110.70, 110.28, 110.31, 110.26

**Response Time:** 10.7s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)

**California Requirement (CEC 2022):**  
Per **CEC 2022 Table 220.12**, the **general lighting load for office buildings** is **11 volt-amperes (VA) per square foot** (118 VA/m²). This is specified in **Section 220.12(A)** for non-dwelling occupancies.

**Key Exceptions/Conditions:**
1. **Energy Code Compliance (Section 220.12(B)):**  
   If the building complies with a local energy code, the lighting load may be calculated using the energy code's unit values **only if**:
   - A power monitoring system is installed to track the general lighting load.
   - The system has alarms to alert if the load exceeds energy code limits.
   - Demand factors from Table 220.42 **do not apply** to the general lighting load.
   - The **125% continuous load multiplier** is applied.

2. **Demand Factors (Section 220.42):**  
   Demand factors from Table 220.42 apply to general lighting loads for feeder/service calculations **except** in areas like surgery suites, emergency departments, and critical care areas (per OSHPD 1 footnote).

**NEC 2023 Reference**  
No difference from NEC 2023. The 11 VA/ft² value for office buildings is identical in both codes.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 10.5s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1) [California Amendment]

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022  

**California Requirement (CEC 2022):**  
Per **Table 400.5(A)(2)** in CEC 2022, the ampacity for a 12 AWG flexible cord with **Column B thermoset insulation** (two-conductor configuration, 75°C rating) is **37 amperes**.  

**Key Notes from Table 400.5(A)(2):**  
- Column B applies to **two-conductor cords** where only two conductors are current-carrying.  
- This ampacity assumes an ambient temperature of **30°C (86°F)**. Temperature correction factors from Table 310.15(B)(1) would apply if the ambient temperature differs.  

**Exceptions Checked:**  
1. **Temperature Corrections**: If ambient temperature ≠ 30°C, apply correction factors from Table 310.15(B)(1).  
2. **Adjustment for >3 Conductors**: Not applicable here (Column B assumes ≤3 conductors).  
3. **Installation Restrictions**: Flexible cords cannot substitute fixed wiring (400.12), but this does not affect ampacity calculations.  

**Conclusion:**  
No exceptions override the base ampacity of **37A** for 12 AWG Column B flexible cord under standard conditions.  

---

## NEC 2023 Reference  
No difference from NEC 2023. The ampacity for 12 AWG flexible cords in Column B remains **37A** under identical conditions.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 400.5, 400.12

**Response Time:** 12.3s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 (CEC 2022)  
**Final Answer:**  
Per CEC 2022 Table 402.3, **Type SF-2 silicone insulated fixture wire** has a **maximum operating temperature of 200°C (392°F)**. This applies to solid or 7-strand configurations with nonmetallic covering.  

**Exception Analysis:**  
No exceptions to this requirement were found in CEC 2022. The exceptions retrieved (450.23, 425.10, 422.47) relate to transformers, industrial heating equipment, and water heaters—none apply to Type SF-2 fixture wire specifications.  

**NEC 2023 Reference**  
No difference from NEC 2023. Type SF-2 is similarly specified in NEC Article 402 with identical maximum operating temperature requirements.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 425.10, 402.3, 422.47, 450.23

**Response Time:** 11.3s

---


## Complex Calculations

### cec-021: adjusted_ampacity

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 x 0.88 x 0.70 = 30.8A

**CEC Ref:** CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1) | **NEC Ref:** NEC Tables 310.16, 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- Conductor: 8 AWG THWN (75°C rated) copper
- Number of CCCs: 7
- Ambient temperature: 40°C

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):
   8 AWG copper, 75°C column = **50 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   40°C ambient, 75°C conductor = **0.88 factor**

3. **Bundling Adjustment** (CEC 2022 Table 310.15(C)(1)):
   7 current-carrying conductors = **0.70 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 50 × 0.88 × 0.70 = 30.8 amperes
   ```

**Final Answer: 30.8 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

No exceptions to these derating requirements were found.

---
## NEC 2023 Reference
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 13.0s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Final Answer (CEC 2022)

**Service Conductors:**  
- **Size:** 2/0 AWG copper  
- **Ampacity:** 175A (per CEC 2022 Table 310.12(A))  
- **Rationale:** For a 200A dwelling service, Table 310.12(A) permits 2/0 AWG copper (175A at 75°C) as it meets the 83% requirement (200A × 0.83 = 166A). No derating applies per CEC 310.12(A) Note 1.  

**Equipment Grounding Conductor (EGC):**  
- **Size:** 6 AWG copper  
- **Table Reference:** CEC 2022 Table 250.122  
- **Rationale:** For a 200A service, Table 250.122 specifies 6 AWG copper for service conductors up to 200A.  

**Grounding Electrode Conductor (GEC):**  
- **Size:** 6 AWG copper  
- **Table Reference:** CEC 2022 Table 250.66  
- **Rationale:** For service conductors sized 2/0 AWG (139 mm²), Table 250.66 requires a 6 AWG copper GEC for ground rods, plates, or concrete-encased electrodes.  

**Exceptions Checked:**  
- No exceptions to 310.12(A) apply for standard dwelling service conductor sizing.  
- Parallel conductor rules (310.10(G)) do not apply here (single conductor installation).  

---
## NEC 2023 Reference  
- **Service Conductors:** NEC 2023 Table 310.12(A) matches CEC for 200A dwelling services (2/0 AWG copper).  
- **EGC:** NEC 2023 Table 250.122 also specifies 6 AWG copper for 200A services.  
- **GEC:** NEC 2023 Table 250.66 aligns with CEC for 6 AWG copper for 2/0 AWG service conductors.  

**No differences from NEC 2023** for these requirements.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.12, 310.10, 250.122, 250.66

**Response Time:** 18.6s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 3.5 VA per square foot. General lighting load = 5,000 sq ft x 3.5 VA/sq ft = 17,500 VA (17.5 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)  
**Given:**  
- Building type: Office  
- Area: 5,000 square feet  
- **CEC 2022 Table 220.12** specifies **1.3 VA/ft²** for office occupancies  
- 125% continuous load multiplier **already included** in table values  

**Calculation:**  
```python  
area_sqft = 5000  
unit_load_va_per_sqft = 1.3  # From Table 220.12 for "Office"  

total_lighting_load = area_sqft * unit_load_va_per_sqft  
print(f"Minimum general lighting load: {total_lighting_load} volt-amperes")  
```  

**Result:**  
- **Minimum general lighting load = 6,500 volt-amperes (VA)**  

---

### Exception Analysis  
1. **Energy Code Compliance (220.12(B))**  
   - Allows reduced lighting load if:  
     - Power monitoring system is installed  
     - Alarms for load exceedance  
     - 125% continuous load multiplier applied  
   - **Not applicable here** (no monitoring system mentioned).  

2. **Demand Factors (220.42)**  
   - Demand factors **do not apply** to general lighting load calculations per the note in Table 220.42.  

3. **Receptacle Loads (220.14(K))**  
   - Office receptacle loads calculated separately (not part of general lighting load).  

---

### Final Answer  
The **minimum general lighting load for a 5,000 sq ft office building in California is 6,500 VA** per CEC 2022 Table 220.12.  

**NEC 2023 Reference**  
No difference from NEC 2023. The same 1.3 VA/ft² value applies to office occupancies in NEC Table 220.12.  

**Note:** If the building complies with energy codes using monitoring systems (per 220.12(B)), a lower value **may** be permissible, but this requires additional system verification.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 220.12, 220.42, 220.14

**Response Time:** 15.2s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Final Answer (CEC 2022)

**Maximum Overcurrent Protection:**  
For **16 AWG copper conductors** in motor control circuits extending beyond enclosures, the maximum overcurrent protection is **15 amperes**, per **CEC 2022 Section 240.4(D)**.  

**Exception Analysis:**  
- The exception found in **370.23** relates to *cablebus* systems and permits alternative overcurrent protection methods (240.100/240.101).  
- This exception **does not apply** to motor control circuits using standard 16 AWG conductors, as the scenario involves general wiring, not cablebus.  

**Key Code References:**  
- **240.4(D):** Limits 16 AWG copper to 15A for overcurrent protection.  
- **430.94:** Confirms compliance with Article 240 rules for motor control circuits.  

**NEC 2023 Reference**  
No difference from NEC 2023. The 15A limit for 16 AWG copper remains unchanged.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 370.23, 430.94, 240.101, 240.4, 240.100

**Response Time:** 11.2s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)

**California Requirement:**
Per CEC 2022 Section 220.82(B)(1) and 220.14(J), the general lighting load for dwelling units is calculated at **3 volt-amperes per square foot (VA/ft²)**.

**Calculation:**
$$
2,400 \, \text{ft²} \times 3 \, \text{VA/ft²} = 7,200 \, \text{volt-amperes (VA)}
$$

This 7,200 VA load includes both general lighting and general-use receptacles in the dwelling unit. No additional adjustments are required per the base rules found.

---
## NEC 2023 Reference
No difference from NEC 2023. The general lighting load calculation for dwelling units is also **3 VA/ft²** per NEC 2023 Section 220.12 and 220.14(J).

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 220.12, 220.82, 220.14

**Response Time:** 8.4s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## CEC 2022 vs NEC 2023 Kitchen GFCI Requirements

### **CEC 2022 Requirements**  
1. **Scope**: GFCI protection required for **all kitchen countertop receptacles** (210.8(A)(6)).  
2. **Exceptions**:  
   - Receptacles not readily accessible for dedicated circuits (e.g., snow-melting equipment).  
   - Listed locking receptacles for ceiling luminaires/fans (no GFCI required if non-convenience).  
3. **No exception for HVAC equipment** (unlike NEC).  

### **NEEC 2023 Requirements**  
1. **Scope**: GFCI required for:  
   - Kitchens (210.8(A)(5)).  
   - Buffet areas with food preparation (210.8(B)(4)).  
   - Aquatic vessels (tanks, etc.) within 6 ft (210.8(B)(13)).  
2. **Exceptions**:  
   - HVAC equipment (until 2026).  
   - Lighting outlets (except those in crawl spaces).  

---

### **Key Differences**  
| **Aspect**               | **CEC 2022**                          | **NEC 2023**                          |  
|--------------------------|--------------------------------------|--------------------------------------|  
| **Scope**                | Countertops only                     | Countertops + buffet areas + aquatic vessels |  
| **HVAC Exception**       | ❌ No exception                     | ✅ Permitted until 2026              |  
| **Ceiling Receptacles**  | Exempt if listed locking type        | No specific exception                |  
| **Additional Locations** | None                                 | Buffet areas, aquatic vessels        |  

---

### **Which Code is More Restrictive?**  
**CEC 2022 is more restrictive** because:  
1. It lacks the **NEC’s HVAC exception**, requiring GFCI for all kitchen circuits without time-limited exemptions.  
2. It applies to **fewer exceptions** (e.g., no buffet area exemptions).  
3. NEC includes broader locations (buffet areas, aquatic vessels) not covered in CEC.  

**Conclusion**: CEC 2022 mandates stricter GFCI protection for kitchen countertop receptacles with fewer exceptions compared to NEC 2023.  

✓ ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 210.8

**Response Time:** 11.2s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2 requires reserved panelboard spaces for heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers, and EV charging equipment. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023)  
**With Exceptions and Cross-References**

---

### **California Electrical Code (CEC 2022) Requirements**  
1. **Mandatory Reserved Circuit Breaker Spaces** [CEC]:  
   - **Single-family dwellings** must reserve spaces for:  
     - Heat pump water heaters  
     - Heat pump space heaters  
     - Electric cooktops  
     - Electric clothes dryers  
   - **Source:** CEC 2022 Section 408.2(A) (California Energy Code Section 150.0)  

2. **Wire-Bending Space Exceptions** [CEC 408.55]:  
   - **Standard:** Top/bottom bending space sized per **Table 312.6(B)** for largest conductor.  
   - **Exceptions:**  
     - Panelboards ≤ 225A with ≤ 42 overcurrent devices may use **Table 312.6(A)** (Exception No. 1).  
     - Single 90° bends allow reduced spacing if wiring diagrams specify (Exception No. 3).  
     - No conductors in a space permits reduced spacing (Exception No. 4).  

3. **Enclosure Requirements** [CEC 408.38]:  
   - Panelboards must be **dead-front** (fully enclosed).  
   - **Exception:** Non-dead-front panels allowed if accessible only to qualified personnel.  

4. **Overcurrent Protection** [CEC 408.36]:  
   - Panelboards must be protected by an overcurrent device ≤ panelboard rating.  
   - **Exception:** Existing residential panelboards may omit individual protection if used as service equipment.  

---

### **National Electrical Code (NEC 2023) Requirements**  
1. **General Panelboard Rating** [NEC 408.30]:  
   - Must match or exceed minimum feeder capacity per Article 220.  

2. **Wire-Bending Space** [NEC 408.55]:  
   - Top/bottom bending space sized per **Table 312.6(B)(2)** for largest conductor.  
   - Similar exceptions for panelboards ≤ 225A.  

3. **Replacement Panelboards** [NEC 408.9]:  
   - Permits installation in existing enclosures under specific conditions (not explicitly addressed in CEC results).  

---

### **Key Differences**  
| **Aspect**                     | ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 8 found
- 408.38, 312.6, 408.55, 408.36, 408.30, 150.0, 408.9, 408.2

**Response Time:** 15.8s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## California (CEC 2022) vs NEC 2023 EV Charging Infrastructure Requirements (Updated with Exceptions)

---

### **Key Exceptions in CEC 2022**
1. **625.47 - Multiple Feeder/Branch Circuits**  
   - **Exception to 625.40**: Allows **multiple feeders/branch circuits** to supply EVSE if the equipment is **identified for the application** (e.g., bidirectional systems or power export).  
   - **NEC Comparison**: NEC 210.11(C)(4) permits shared circuits for garage receptacles (no such restriction in CEC except under this exception).

2. **625.46 - Loss of Primary Source**  
   - Requires **anti-backfeed protection** for EVSE with power export functions.  
   - **NEC Gap**: NEC 2023 does not explicitly address bidirectional power flow in standard EVSE provisions (covered under optional standby systems in Article 702/705).

---

### **Revised Comparison with Exceptions**
#### **1. Branch Circuit Requirements**
- **CEC 625.40 + 625.47**:  
  - **Default**: Individual branch circuit per EV outlet.  
  - **Exception**: Multiple circuits allowed for **bidirectional systems** or **power export equipment** (e.g., vehicle-to-grid systems).  
- **NEC 210.11(C)(4)**:  
  - Requires a **20A, 120V circuit** for garage receptacles (including EVs), but allows shared circuits for other garage loads.  

#### **2. Power Export Systems**
- **CEC 625.48**:  
  - Mandates **listing and marking** for bidirectional EVSE. Requires compliance with **UL 1741** or **UL 9741** for interactive systems.  
  - **No NEC Equivalent**: NEC references optional standby systems (Article 702) but lacks specific EVSE bidirectional provisions.  

---

### **Final Determination**
- **CEC is stricter** on default branch circuit requirements (625.40) but provides flexibility for advanced systems via exceptions (625.47).  
- **NEC allows shared circuits** in garages (210.11(C)(4)) but lacks detailed requirements for bidirectional EVSE.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 5 found
- 625.47, 625.46, 625.40, 625.48, 210.11

**Response Time:** 15.4s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements Comparison: CEC 2022 vs NEC 2023 for Dwelling Units

---

### **CEC 2022 Requirements**  
**Scope:**  
- Applies to **120V, single-phase, 15- and 20-ampere branch circuits** in dwelling units for outlets in:  
  - Kitchens, family rooms, dining rooms, living rooms, bedrooms, hallways, laundry areas, and similar spaces.  

**Protection Methods (210.12(A)(1)–(6)):**  
1. **Combination-type AFCI** at the circuit origin.  
2. **Branch/feeder-type AFCI** + outlet branch-circuit AFCI at first outlet.  
3. **Supplemental arc protection circuit breaker** + outlet AFCI (with conductor length limits).  
4. **Outlet branch-circuit AFCI** at first outlet (with conductor length limits).  
5. **Metal raceway/cable systems** allow outlet AFCI at first outlet.  
6. **Concrete-encased conductors** allow outlet AFCI at first outlet.  

**Exceptions:**  
- **Fire alarm circuits** (per 760.41(B)/760.121(B)) exempt if in metal raceway/boxes.  
- **Circuit extensions ≤ 6 ft** without additional outlets (excluding enclosures).  

---

### **NEC 2023 Requirements**  
**Scope:**  
- Similar to CEC but broader: Covers **120V, 15–20A circuits** in **all dwelling unit areas** (including bathrooms, garages, outdoors, etc.) per **210.12**.  

**Protection Methods:**  
- **Combination-type AFCI** required at circuit origin (no alternative methods permitted in most cases).  
- **Outlet branch-circuit AFCI** allowed in specific scenarios (e.g., with metal raceway systems).  

**Exceptions:**  
- **Fire alarm circuits** exempt if in metal raceway/boxes.  
- **Circuit extensions ≤ 6 ft** without additional outlets.  

---

### **Key Differences**  
| **Aspect**               | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|--------------------------|------------------------------------------------------------------------------|--------------------------------...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 760.41, 210.8, 760.121, 210.12

**Response Time:** 9.9s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## Final Answer: California (CEC 2022) vs NEC 2023 Solar PV Requirements

### **Key Exceptions in CEC 2022 Affecting Solar PV Requirements**
1. **Voltage Limits for Non-Building Installations (CEC 690.7 Exception):**
   - **CEC 2022:** Permits listed DC PV equipment rated up to **1500V** in non-building locations (e.g., ground-mounted arrays, carports).
   - **NEC 2023:** Limits DC circuits to **1000V** without specific exceptions. No provision for non-building installations exceeding 1000V.
   - **Impact:** California allows higher voltages in non-building systems, enabling larger arrays or reduced conductor sizes.

2. **Arc-Fault Protection Exception (CEC 690.11 Exception):**
   - **CEC 2022:** Exempts non-building PV systems installed in **metallic raceways, metal-clad cables, or underground** from requiring DC arc-fault protection.
   - **NEC 2023:** Requires arc-fault protection for all DC circuits ≥80V, with **no exception** for non-building installations.
   - **Impact:** California reduces arc-fault requirements for non-building systems using metallic raceways, simplifying compliance in industrial or remote applications.

3. **Overcurrent Protection Flexibility (CEC 690.9):**
   - **CEC 2022:** Permits single overcurrent devices for PV circuits if conductors are **≤3m (10ft)** and installed in metal raceways or underground.
   - **NEC 2023:** Requires overcurrent protection for all PV circuits unless explicitly exempted (no non-building exception).
   - **Impact:** California allows simplified overcurrent protection for short, non-building runs, aligning with practical field installations.

4. **Stand-Alone Systems (CE 690.10):**
   - **CEC 2022:** References **Article 710** (Energy Storage Systems) for stand-alone PV systems, integrating storage requirements.
   - **NEC 2023:** No direct cross-reference to energy storage systems in Article 690.
   - **Impact:** California explicitly addresses hybrid PV-storage systems, while NEC leaves this to interpretatio...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 690.7, 690.10, 690.9, 710.15, 690.11

**Response Time:** 15.2s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 13.2s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

