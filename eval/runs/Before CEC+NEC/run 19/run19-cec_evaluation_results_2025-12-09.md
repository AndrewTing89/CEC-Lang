# CEC Agent Evaluation - Run 19 (Prompt Fixes)

**Date:** 2025-12-09
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)
**NEC Comparison:** ENABLED
**Prompt Version:** v2 - table routing, completeness, comparison reasoning

## Prompt Improvements in This Run

1. **Table Content Routing:** Added `cec_lookup_table` to tool reference with explicit routing for "What does Table X specify?" questions
2. **Completeness Check:** Enhanced checklist to include copper/aluminum options and all enclosure/equipment types
3. **Comparison Reasoning:** Added structured reasoning for "which is more restrictive" questions

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Successful** | 30 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 557.2s |
| **Avg per Question** | 18.6s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2(A) requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) e...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022 vs NEC 2023)

### **California Energy Code (CEC 2022) Requirements**
**Reserved Circuit Breaker Spaces**  
Per **CEC 2022 Section 408.2**, single-family panelboards must include **dedicated spaces** for:
1. **Heat pump water heaters**  
2. **Heat pump space heaters**  
3. **Electric cooktops**  
4. **Electric clothes dryers**  

These mandates are **California-specific** and tied to energy efficiency goals (CEC Sections 150.0(n), (t), (u), (v)).  

---

### **NEC 2023 Comparison**  
The **National Electrical Code (NEC 2023)** does **not** require reserved spaces for these appliances. Its panelboard rules (NEC 408.16, 408.18) focus on:
- Overcurrent device spacing (e.g., no more than 6 spaces between breakers).  
- Accessibility and labeling requirements.  

**Key Differences:**  
| **Aspect**                | **CEC 2022**                          | **NEC 2023**                          |  
|--------------------------|---------------------------------------|---------------------------------------|  
| **Reserved Spaces**       | Mandates spaces for 4 appliances     | No appliance-specific requirements    |  
| **Purpose**              | Electrification readiness (e.g., heat pumps) | General safety and accessibility      |  
| **Code Basis**           | CEC 408.2 + Energy Code Sections     | NEC 408 (general panelboard rules)    |  

---

### **Why California is More Restrictive**  
CEC 408.2 adds **future-p...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 150.0, 408.16, 408.18, 408.2

**Response Time:** 20.9s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements (CEC 2022) vs NEC 2023 **(Final Answer)**

---

### **Key CEC 2022 Requirements for Residential EV Charging**
1. **CALGreen Compliance**  
   - **EV-Ready Panel Space**: Reserved circuit breaker space for future EV charging (CEC 408.2).  
   - **Conduit to Parking**: Required in new residential construction (CALGreen Chapter 4).  

2. **Ventilation Mandates**  
   - **General Rule**: Indoor EV charging requires **mechanical ventilation** if equipment is not listed for indoor use without ventilation (625.52(B)).  
   - **Exception**: Ventilation not required if:  
     - Equipment is **listed for indoor use without ventilation** (625.52(A)).  
     - Equipment uses **storage batteries** (625.52(A)).  
   - **Ventilation Rates**: Calculated via **Table 625.52(B)(1)(a)** (e.g., 15A/120V = 1.1 m³/min).  

3. **Cable Length Restrictions**  
   - **Power-Supply Cords**:  
     - ≤12 in. (300 mm) if interrupting device is in the enclosure.  
     - ≤6 ft (1.8 m) for stationary equipment.  
   - **Output Cables**: ≤25 ft (7.5 m) unless using a listed cable management system.  

4. **Ground-Fault Protection**  
   - **All EV charging receptacles** require GFCI protection (625.54).  

5. **Personnel Protection Systems**  
   - Required for systems ≥60 Vdc. Interruptinging devices must be within 12 in. of the plug for portable equipment.  

---

### **Comparison with NEC 2023**  
1. **Ventilation**  
   - **CEC**: Mandates ventilation for indoor EV...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 210.8, 400.12, 408.2, 450.45, 450.9, 625.52, 625.54

**Response Time:** 21.5s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requir...

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements (CEC 2022) with Exceptions

### **1. Rapid Shutdown (CEC 690.12)**
**Primary Rule**:  
- **Voltage Limits**:  
  - ≤30V outside array boundary (30s shutdown)  
  - ≤80V inside array boundary (30s shutdown)  
- **Initiation Devices**: Must include visible "off" position indicator.  
- **Labeling**: Permanent labels at service disconnectss (CEC 690.56).  

**Exceptions**:  
- **Ground-mounted systems** in buildings *solely for housing PV equipment* are exempt from rapid shutdown requirements.  
- **Nonmetallic enclosures** permitted for PV hazard control systems per 690.12(B)(2)(1).  

---

### **2. System Grounding (CEC 690.41)**
**Primary Rule**:  
- **Mandatory DC ground-fault protection** for circuits >30V or 8A.  
- Solidly grounded systems must connect to grounding electrode via **250.66-sized conductor**.  

**Exceptions**:  
- None explicitly noted in exceptions search, but NEC allows functionally grounded systems without solid grounding.  

---

### **3. Wiring Methods (CEC 690.31)**
**Primary Rule**:  
- **DC conductor identification**: Color coding or permanent markings (+/−) required.  
- **Labeling**: Minimum 9.5mm high "SOLAR PV DC CIRCUIT" labels.  
- **Ampacity adjustments**: Use Table 690.31 for ambient temps >30°C.  

**Exceptions**:  
- **Grouping requirements** waived if circuits enter via unique raceways.  
- **Support intervals** for PV wire may follow engineered designs (691.4).  

---

### **4. California-Specific Mand...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 250.66, 408.2, 690.12, 690.31, 690.41, 690.56, 691.4

**Response Time:** 31.6s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can sup...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Circuit Requirements for Heat Pump Water Heaters in California (CEC 2022)

### **California Electrical Code (CEC) Requirements**
1. **Dedicated Circuits and Panelboard Spaces**  
   - **Single-family buildings** (1–2 dwellings):  
     - Panelboards must include **designated circuit breaker spaces** for heat pump water heaters (CEC 408.2(A)).  
     - **Branch circuits** and **receptacles** must be provided as specified in California Energy Code Section 150.0(n) (CEC 422.3(A)).  
   - **Multifamily buildings**:  
     - Panelboards must reserve spaces for heat pump water heaters per energy code, though specifics are tied to single-family provisions (CEC 408.2(B)).  

2. **Application of Other Articles**  
   - Heat pump water heaters must comply with **Article 430** (motor-operated appliances) and **Article 440** (hermetic motor-compressors) unless amended by CEC (CEC 422.3).  

---

### **Exceptions Checked**
- **CEC 422.47**: Applies to storage/instantaneous water heaters, not heat pump water heaters.  
- **CEC 422.12**: Relates to central heating equipment, not applicable to heat pump water heaters.  

No exceptions specific to heat pump water heaters were found for the cited rules (422.3, 408.2).  

---

### **Comparison with NEC 2023**
- **NEC 2023** lacks provisions for **dedicated circuits** or **panelboard spaces** for heat pump water heaters.  
- California’s CEC 2022 is **more restrictive**, mandating readiness for electrification in new residential construction....

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 150.0, 408.2, 422.12, 422.3, 422.47

**Response Time:** 13.8s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrif...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness in New California Homes (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirements**  
Per **CEC 2022 Section 422.3**:  
- **Single-family homes**: Must include **dedicated circuits** and circuit identifications for electric cooktops (California Energy Code Section 150.0(u)).  
- **Multifamily homes**: Must comply with **California Energy Code Section 160.9(b)**, requiring dedicated circuits for electric cooktops.  
- **Exceptions**:  
  - **422.33**: Allows cord-and-plug-connected appliances to use accessible separable connectors or receptacles as disconnecting means.  
  - **422.23**: Non-standard installation methods require special permission but do not override readiness mandates.  

### **NEC 2023 Comparison**  
The **National Electrical Code (NEC 2023)** does **not** mandate "readiness" provisions for electric cooktops. Key differences:  
1. **No Dedicated Circuit Mandates**:  
   - NEC focuses on electrical safety (e.g., Article 422 for appliances) and load calculations (NEC 220.55 for cooking appliances).  
   - Example: NEC 422.10 requires branch circuits to match appliance ratings but does not require pre-wiring for future cooktops.  

2. **Load Calculations**:  
   - NEC 220.55 uses demand factors to size service/feeder conductors for cooking appliances but does not address infrastructure readiness.  

3. **Disconnecting Means**:  
   - NEC 422.30 requires disconnecting means for appliances but does not specify pre-wiring for cooktops.  

--...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 8 found
- 150.0, 160.9, 220.55, 422.10, 422.23, 422.3, 422.30, 422.33

**Response Time:** 18.6s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022 vs NEC 2023)

---

### **California Code (CEC 2022)**  
**Mandatory Reserved Spaces**  
- **Section 408.2**: Panelboards in **new residential construction** (single-family and multifamily) **must reserve dedicated circuit breaker spaces** for electric clothes dryers.  
  - **Single-family**: Spaces for dryers, heat pump water heaters, and cooktops (Energy Code 150.0).  
  - **Multifamily**: Spaces for dryers and cooktops (Energy Code 160.9).  
- **No exceptions** to this requirement in CEC 2022.  

**Load Calculation**  
- **Section 220.54**: Dryer load is calculated as **5,000 VA** (or nameplate rating, whichever is larger).  

---

### **National Code (NEC 2023)**  
**No Reserved Spaces**  
- **NEC 2023 does not require** reserved panelboard spaces for dryers. Compliance depends on local adoption of CEC amendments.  

**Dryer Circuit Requirements**  
- **Section 210.11(C)(2)**: A **20-amp branch circuit** must supply the laundry area (includes dryers).  
- **Section 220.54**: Load calculation uses **5,000 VA** for dryers (same as CEC).  

---

### **Key Differences**  
| **Aspect**               | **CEC 2022 (California)**                     | **NEC 2023 (National)**                     |  
|--------------------------|-----------------------------------------------|---------------------------------------------|  
| **Reserved Spaces**      | **Required** for dryers in new residential construction | **...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 150.0, 160.9, 210.11, 220.54, 408.2

**Response Time:** 20.9s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) Exceptions Analysis (CEC 2022)

### Key Exceptions Affecting Table 240.4(G):
1. **Motor Circuit Overcurrent Protection**  
   - **Exception 230.90(A) No. 1**:  
     *Allows motor circuits to comply with **430.52** (motor overload protection) instead of general overcurrent rules in 240.4(G).*  
     - **Impact**: For motor and motor-control circuits listed in Table 240.4(G), California permits using **Article 430** requirements (e.g., 430.52 for motor overload protection) instead of the standard 240.4(G) rules.  
     - **CEC Unique**: This exception reflects California’s emphasis on motor-specific protection, aligning with 430.52’s focus on motor-starting currents and thermal protection.

2. **Service Conductor Overload Protection**  
   - **Exception 230.90(A) No. 3**:  
     *Permits overcurrent devices exceeding service conductor ampacity if calculated load ≤ conductor ampacity.*  
     - **Impact**: For service conductors referenced in Table 240.4(G) (e.g., HVAC systems), California allows oversized overcurrent devices (e.g., 225A breaker for 200A service) if the calculated load remains within the conductor’s ampacity.  
     - **CEC Unique**: This provides flexibility for high-demand systems like HVAC, common in California’s climate.

3. **Fire Pump Conductors**  
   - **Exception 230.90(A) No. 4**:  
     *Requires fire pump conductors to comply with **695.4(B)(2)** instead of 240.4(G).*  
     - **Impact**: Fire alarm/fire pump systems (listed in...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 230.90, 240.4, 430.52, 695.4

**Response Time:** 14.4s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 242.3 Exceptions (CEC 2022)

**Exception Found:**  
[CEC Section 370.23 Exception]  
**Cablebus Overcurrent Protection:**  
Cablebus systems may use **240.100** (conductor ampacity-based protection) and **240.101** (specific overcurrent protection for conductors) instead of the standard 240.4 requirements. This provides an alternative compliance path for cablebus installations.

---

### **Impact on Table 242.3 Application**
- **Primary Rule:** Table 242.3 directs overvoltage protection to specific articles (e.g., 490 for >1000V equipment).
- **Exception:** For cablebus systems, **240.100/240.101** may override the general overcurrent protection rules in 240.4. This is a **California-specific exception** not explicitly in NEC.

---

### **Final Answer**
CEC Table 242.3 specifies cross-references for overvoltage protection requirements, with California-specific additions (marked "N"). Key exceptions include:
- **Cablebus systems** (370.23 Exception): Permitted to use 240.100/240.101 instead of 240.4 for overcurrent protection.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 240.100, 240.101, 240.4, 242.3, 370.23

**Response Time:** 10.6s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC 430.72(B) vs NEC 2023: Motor Control Circuit Overcurrent Protection

### **Key Structural Similarities**
- **Table Format**: Both codes use **Table 430.72(B)** with identical conductor sizes (18–10 AWG) and columns (A/B/C).
- **Derivation Rules**:
  - **Column B**: 400% of Table 310.17 (free-air ampacity).
  - **Column C**: 300% of Table 310.16 (raceway ampacity).
- **Example for 12 AWG Copper**:
  - CEC/NEC Column C: $ 20A \times 3 = 60A $.
  - CEC/NEC Column B: $ 30A \times 4 = 120A $.

---

### **Critical Differences**
| Feature                | **CEC 2022**                          | **NEC 2023**                          |
|------------------------|---------------------------------------|---------------------------------------|
| **Aluminum Conductors** | Prohibited for sizes ≤10 AWG (marked "—"). | Permitted for sizes ≥12 AWG (values provided). |
| **Fire Pump Exceptions** | Explicitly allows protection by branch-circuit device (Exception 1). | Same exception exists but less emphasized in text. |
| **Transformer Protection** | Requires voltage ratio calculation for primary-side protection. | Identical requirement but with broader aluminum allowances. |

---

### **Material Restrictions**
- **CEC 430.72(B)**:
  - **No aluminum** for 10 AWG and smaller (safety-focused amendment).
  - Example: 12 AWG aluminum = "—" in CEC vs. 45A in NEC.
- **NEC 430.72(B)**:
  - Permits aluminum for 12 AWG and larger (e.g., 12 AWG aluminum = 45A in Column C).

---

### **Derivation C...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search, cec_lookup_table
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 310.15, 310.16, 310.17, 430.72

**Response Time:** 36.3s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found i...

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in CEC vs NEC (CEC 2022)

### California (CEC 2022) Medium Voltage Tables
CEC has **18 dedicated medium voltage (MV) tables** in the **311.60(C) series** for Type MV cables (2001–35,000V nominal). These include:
- **Tables 311.60(C)(67) through 311.60(C)(86)**  
  Provide ampacities for MV cables in various configurations (e.g., triplexed in air, direct burial, underground ducts).

**Key CEC Provisions:**
- **311.60(C):** Specifies ampacities for copper and aluminum conductors in 20+ configurations.
- **311.60(D):** Ambient temperature correction factors (e.g., 40°C baseline).
- **Exceptions:** Allow higher ampacity for short circuit segments (≤10 ft or 10% of total length).

---

### NEC 2023 Comparison
The NEC **does not include equivalent tables** for medium voltage cables. Instead, it references:
- **NEC 310.15(B)(3)(a):** General ambient temperature correction factors.
- **NEC 310.15(C)(1):** Bundling derating factors for conductors.
- **NEC 311.10:** Limited to definitions and general installation rules for MV cables.

**Key Differences:**
- **CEC is more restrictive** by providing **dedicated MV ampacity tables** (311.60 series) not found in NEC.
- NEC relies on **general adjustment factors** (temperature, bundling) without MV-specific tables.
- CEC tables account for **installation-specific scenarios** (e.g., cable trays, burial depth), while NEC uses broad adjustments.

---

### Why CEC Has Unique MV Tables
California mandates detailed ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 311.10, 311.60

**Response Time:** 20.3s

---


## CEC Delta Tables

### cec-011: conductor_ampacity [CA-SPECIFIC]

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Ampacity of 4/0 AWG Copper Conductor at 75°C (CEC 2022)

**California Electrical Code (CEC 2022):**  
- **Ampacity:** 230 amperes  
- **Reference:** CEC Table 310.16 (identical to NEC Table 310.16)  

**Exceptions and Special Conditions:**  
1. **Section 440.6 Exceptions** apply to specialized equipment (e.g., hermetic refrigerant motor-compressors). These exceptions modify ampacity requirements for specific applications but do **not affect general conductor ampacity** in this case.  
   - Exception No. 1: Allows use of "branch-circuit selection current" for hermetic compressors.  
   - Exception No. 2: Applies to cord-and-plug-connected equipment (see 440.22(B)).  

2. **Cross-References to Check:**  
   - **Section 310.15(B):** Ambient temperature correction factors (if ambient ≠ 30°C).  
   - **Section 240.4(D):** Overcurrent protection limitations (e.g., 4/0 AWG copper must be protected at ≤ 250A unless exceptions apply).  

**Comparison with NEC 2023:**  
- NEC Table 310.16 also specifies **230A** for 4/0 AWG copper at 75°C.  
- No California amendments modify this value.  

**Final Notes:**  
- The 230A value applies under standard conditions (≤3 conductors, 30°C ambient).  
- Adjustments for temperature, bundling, or overcurrent protection must follow CEC 310.15 and 240.4(D).  

✓ Source: CEC 2022 and NEC 2023 Table 310.16

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 240.4, 310.15, 310.16, 440.22, 440.6

**Response Time:** 19.3s

---

### cec-012: grounding [CA-SPECIFIC]

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size for 200A Circuit (CEC 2022)  
**Final Answer with Exceptions Considered**  

**Required Size:**  
- **Copper**: 6 AWG  
- **Aluminum/Copper-Clad**: 4 AWG  
- **Reference**: CEC 2022 Table 250.122 [California Amendment]  

**Key Exceptions Analyzed:**  
1. **250.142**: Permits using the grounded circuit conductor for grounding **supply-side equipment** (e.g., service disconnect enclosures).  
   - *Not applicable here* unless the circuit is on the supply side of the service disconnect.  

2. **215.2(A)(2)**: Grounded conductor size must comply with Table 250.122 for feeders.  
   - *Reinforces the Table 250.122 requirement for 200A circuits*.  

3. **Other exceptions** (410.44, 352.60, 356.60): Apply to specialized equipment (luminaires, conduit systems) and do not override general grounding rules for standard 200A circuits.  

**Conclusion:**  
No exceptions override the Table 250.122 sizing for a standard 200A circuit. The required grounding conductor size remains **6 AWG copper or 4 AWG aluminum**.  

**NEC 2023 Comparison:**  
- Sizes match CEC (Table 250.122).  
- NEC lacks California-specific amendments but aligns with CEC for this application.  

✓ Source: CEC 2022 / NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 215.2, 250.122, 250.142, 352.60, 356.60, 410.44

**Response Time:** 11.7s

---

### cec-013: grounding [CA-SPECIFIC]

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022 vs NEC 2023)  

**Required GEC Size**: **4 AWG copper**  
Per **CEC Table 250.66** and **NEC Table 250.66** for a 3/0 AWG copper service conductor.  

### Key Code Comparison:  
| **Requirement**                | **CEC 2022**                          | **NEC 2023**                          | **Difference**                                                                 |
|----------------------------------|----------------------------------------|----------------------------------------|---------------------------------------------------------------------------------|
| **GEC Size for 3/0 AWG Copper**  | 4 AWG copper (Table 250.66)            | 4 AWG copper (Table 250.66)            | **Same size required**                                                          |
| **Exceptions**                   | Includes California-specific amendments (e.g., stricter electrode requirements in certain soil conditions) | No California amendments; follows general NEC rules | CEC adds localized mandates not in NEC                                          |
| **Electrode Type Flexibility**   | Exceptions 250.66(A)/(B) allow smaller GEC for rod/pipe or concrete-encased electrodes if not extending to other electrode types | Same exceptions apply (250.66(A)/(B)) | **Same exceptions**, but CEC emphasizes additional compliance for California conditions |

### California-Specific Notes:  
- **Soil Conditions**: CEC may require supplemental grounding ...

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 15.6s

---

### cec-014: ampacity_adjustment [CA-SPECIFIC]

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)  

**California (CEC 2022):**  
For a 75°C rated conductor at 40°C ambient temperature:  
✓ **Correction factor = 0.88** (CEC Table 310.15(B)(1)(1))  

**Exception Check:**  
No exceptions apply to temperature correction factors in this scenario. The returned "exceptions" relate to grounding requirements (Sections 352.60, 356.60, etc.), which are unrelated to ampacity adjustments.  

**NEC 2023 Comparison:**  
NEC 310.15(B)(1) also specifies **0.88** for 75°C conductors at 40°C ambient.  

**Final Answer:**  
The temperature correction factor is **0.88** for both CEC and NEC in this case.  

✓ Source: CEC 2022 / NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 352.60, 356.60

**Response Time:** 8.3s

---

### cec-015: ampacity_adjustment [CA-SPECIFIC]

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Final Answer: Ampacity Adjustment Factor for 7-9 Conductors (CEC 2022)

**California Code (CEC 2022):**  
- **Adjustment factor**: **0.7 (70%)** for 7-9 current-carrying conductors in a raceway  
- **Source**: CEC Table 310.15(C)(1)  

**NEC 2023 Comparison:**  
- **Adjustment factor**: **0.7 (70%)** for 7-9 current-carrying conductors in a raceway  
- **Source**: NEC Table 310.15(C)(1)  

**Exceptions Checked:**  
- No exceptions override the 70% adjustment for general bundling scenarios (7-9 conductors).  
- Exceptions in CEC 2022 (e.g., 334.80, 310.15) apply to specific cases like NM/NMC cables or grounding conductors, not the general bundling rule.  

**Key Notes:**  
- Both codes apply the same 70% adjustment factor.  
- California’s CEC aligns with NEC 2023 for this requirement.  
- The count includes all current-carrying conductors (spares, neutrals classified as current-carrying).  

✓ Source: CEC 2022 and NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 334.80

**Response Time:** 13.0s

---

### cec-016: working_space [CA-SPECIFIC]

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth for 480V Panelboard (CEC 2022)  

**California Code (CEC 2022):**  
For **Condition 3** (exposed live parts on both sides of the working space), the minimum working space depth required for a **480V panelboard** is **1.2 meters (4 feet)** per **CEC Table 110.26(A)(1)**. This applies to systems operating between **151–600 volts to ground**.  

**Exceptions Checked:**  
- **CEC 110.26(E):** Requires dedicated electrical space (6 ft height zone) but does not override the 4 ft depth requirement for Condition 3.  
- **Other exceptions (352.60, 356.60, 440.14):** Relate to grounding and disconnecting means, not working space depth.  

**NEC 2023 Comparison:**  
NEC 2023 Table 110.26(A)(1) specifies the **same 1.2 m (4 ft)** depth for Condition 3 at 480V. No differences exist between CEC 2022 and NEC 2023 for this requirement.  

---

### Key Footnotes:  
- **Condition 3** applies when **exposed live parts are on both sides** of the working space (e.g., front and back of a panelboard with live components on both sides).  
- The depth is measured from the **front of the equipment** to the **obstruction** (wall, equipment, etc.).  
- **Exceptions** for dedicated spaces (110.26(E)) do not modify the 4 ft depth requirement but add requirements for ceiling zones and foreign systems.  

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 110.26, 352.60, 356.60, 440.14

**Response Time:** 11.3s

---

### cec-017: enclosure [CA-SPECIFIC]

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Outdoor Enclosure Selection: CEC 2022 vs NEC 2023

### **Key Differences for Rain, Sleet, and Ice Protection**

| **Requirement** | **CEC 2022** | **NEC 2023** | **Restrictiveness** |
|------------------|--------------|--------------|----------------------|
| **Enclosure Types** | Types 3S, 3SX, 4, 4X, 6, 6P | Same types (3S, 4, 4X, 6, 6P) | **Same** |
| **Hazardous Location Compatibility** | Explicitly states dusttight enclosures (Types 3S, 4, etc.) are suitable for Class II/III/Zone 22 locations (Footnotes [3] and [4]) | No explicit hazardous location compatibility notes | **CEC more restrictive** |
| **IP Ratings** | IP ratings not referenced (only enclosure types) | IP ratings referenced as supplementary (Footnote [2]) | **NEC more permissive** |
| **Receptacle Requirements** | 15-20A receptacles must be **listed weather-resistant type** (NEMA 5-15/20, 6-15/20) in wet locations | Requires weatherproof enclosures but no specific NEMA listing | **CEC more restrictive** |
| **Dedicated Outdoor Spaces** | Mandates **1.8m (6ft) dedicated clearance** above equipment (110.70) | No minimum clearance specified | **CEC more restrictive** |
| **High-Pressure Wash Exceptions** | Permits enclosures without attachment plug when subject to high-pressure washing | No specific exception for high-pressure wash areas | **CEC more permissive** |

---

### **Critical Code Citations**
- **CEC 2022**:  
  - Table 110.28 (enclosure types)  
  - Section 406.9 (weatherproof receptacles)  
  - S...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 110.28, 110.70, 406.9

**Response Time:** 24.7s

---

### cec-018: lighting_load [CA-SPECIFIC]

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022 vs NEC 2023)

### **California Code (CEC 2022)**
- **Standard Requirement**: **1.3 VA per square foot** (14 VA/m²)  
- **Exception for Energy Code Compliance**:  
  - Lighting load may use energy code values if:  
    1. Power monitoring system is installed  
    2. System has alarm for load exceedance  
    3. Demand factors from 220.42 **do not apply**  
    4. 125% continuous load multiplier **must still be applied**  
  - *Source*: CEC 220.12(B)  

### **NEC 2023 Comparison**
- **NEC Value**: **1.3 VA/ft²** (14 VA/m²) for office buildings  
- **Key Differences**:  
  1. **Power Factor Assumption**:  
     - CEC: Based on **100% power factor** (CEC Table 220.12 note)  
     - NEC: Based on **80% power factor** (NEC 220.42 informational note)  
  2. **Continuous Load Multiplier**:  
     - CEC: **125% multiplier is already included** in the 1.3 VA/ft² value  
     - NEC: 125% multiplier **must be applied separately** (not included in table value)  
  3. **Demand Factors**:  
     - CEC: 220.42 demand factors **do not apply** to general lighting load when using energy code values  
     - NEC: 220.42 demand factors **apply to feeder/service calculations** (not branch circuits)  

### **Cross-Reference Notes**
- Both codes use **identical VA/ft² values** for office buildings.  
- CEC explicitly includes the 125% continuous load multiplier in Table 220.12, while NEC requires it to be applied separately.  
- CEC allows ene...

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 20.4s

---

### cec-019: flexible_cord [CA-SPECIFIC]

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

**Ampacity Value:**
- **25 amperes** (CEC Table 400.5(A)(1), Column B thermoset)

**Exceptions and Limitations:**
1. **Prohibited Uses** (CEC 400.12):
   - Cannot substitute for fixed wiring of a structure
   - Cannot be run through walls/ceilings/floors (exception: 368.56(B) and 590.4 for specific attachments)
   - Cannot be concealed by walls/ceilings (exception: 300.22(C)(3) for environmental air spaces)

2. **Overcurrent Protection**:
   - Must comply with 240.4(D) limitations (cross-reference from Table 310.16 footnote [*])

**Additional Considerations:**
- **Temperature Adjustments**: Apply 310.15(B) if ambient ≠ 30°C
- **Bundling Derate**: Apply 310.15(C)(1) for >3 current-carrying conductors
- **California-Specific**: No amendments to Table 400.5(A)(1) values, but exceptions restrict installation locations

**NEC Comparison**:
- NEC 2023 also specifies 25A for 12 AWG Column B thermoset (Table 400.5(A)(1))
- Same prohibited uses in NEC 400.12

✓ Source: CEC 2022 / NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 8 found
- 240.4, 300.22, 310.15, 310.16, 368.56, 400.12, 400.5, 590.4

**Response Time:** 8.9s

---

### cec-020: fixture_wire [CA-SPECIFIC]

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire  
**California Code (CEC 2022) vs. NEC 2023**  

### **California Electrical Code (CEC 2022)**  
- **Type SF-2** silicone insulated fixture wire has a **maximum operating temperature of 200°C (392°F)**.  
- This is explicitly specified in **Table 402.3** for SF-2 entries.  
- **No exceptions** override this temperature rating (verified via `cec_exception_search`).  

---

### **National Electrical Code (NEC 2023)**  
- **Type SF-2 is not listed** in NEC Table 402.3.  
- The closest comparable insulation type in NEC is **PFHH-2** (heat-resistant cross-linked synthetic polymer), which has a **maximum operating temperature of 150°C (302°F)**.  
- General silicone rubber insulation in NEC is typically rated for **150°C (302°F)** unless manufacturer data specifies otherwise.  

---

### **Key Differences**  
| **Aspect**               | **CEC 2022 (California)**          | **NEC 2023 (National)**          |  
|---------------------------|-----------------------------------|-----------------------------------|  
| **Type SF-2 Rating**      | 200°C (392°F)                     | Not explicitly listed             |  
| **Closest NEC Equivalent**| N/A                               | PFHH-2: 150°C (302°F)            |  
| **Permissiveness**        | **More permissive** (higher temp) | Standard silicone: 150°C          |  

---

### **Conclusion**  
California’s CEC 2022 allows **Type SF-2** silicone insulated...

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 402.3

**Response Time:** 20.0s

---


## Complex Calculations

### cec-021: adjusted_ampacity [CA-SPECIFIC]

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 ...

**CEC Ref:** CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1) | **NEC Ref:** NEC Tables 310.16, 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## CEC 2022 vs NEC 2023 Comparison for Ampacity Adjustments

### **1. Base Ampacity (Table 310.16)**
- **CEC 2022**: 8 AWG THWN copper = **50A** (75°C column)  
- **NEC 2023**: 8 AWG THWN copper = **50A** (75°C column)  
  ➔ **Identical values** for base ampacity.

---

### **2. Temperature Correction (40°C Ambient)**
- **CEC 2022**:  
  Factor = **0.88** (Table 310.15(B)(1))  
  *Based on 30°C ambient baseline.*  

- **NEC 2023**:  
  Factor = **0.88** (Table 310.15(B)(1))  
  *Same correction factor applied.*  

**Key Difference**:  
- **NEC** allows an **equation-based** temperature correction (Section 315.60(A)(4)):  
  $$
  I' = I \sqrt{\frac{T_c - T_a'}{T_c - T_a}}
  $$  
  *Not used in this case since the table factor matches.*  
- **CEC** uses **fixed table factors** (no equation-based adjustments).

---

### **3. Bundling Adjustment (7 Conductors)**
- **CEC 2022**:  
  Factor = **0.70** (Table 310.15(C)(1))  

- **NEC 2023**:  
  Factor = **0.70** (Table 310.15(C)(1))  

**Key Difference**:  
- **NEC** excludes **grounding/bonding conductors** from the count (Section 310.15(C)(1)(f)).  
- **CEC** includes all conductors unless explicitly excluded (Section 310.15(C)(1)).  

---

### **4. Termination Temperature Limitations**
- **CEC 2022**:  
  Requires corrected/adjusted ampacity **not to exceed termination ratings** (Section 310.15, referencing 110.14(C)).  
  *THWN is 75°C-rated; terminations must be ≥75°C.*  

- **NEC 2023**:  
  Same requirement (Section 110.14(C...

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_find_limiting_rules, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 110.14, 310.15, 310.16, 315.60, 400.5, 625.51

**Response Time:** 28.9s

---

### cec-022: service_sizing [CA-SPECIFIC]

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper...

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Final Answer with NEC Comparison

## Service Sizing for 200A Residential (CEC 2022)

### Conductors
✓ **Service conductor**: 2/0 AWG copper (CEC Table 310.12(A))  
*Identical to NEC 2023 Table 310.12(A) for 200A dwelling services*

### Equipment Grounding Conductor (EGC)
✓ **EGC**: 6 AWG copper (CEC Table 250.122)  
*Matches NEC 2023 Table 250.122 requirements for 200A overcurrent device*

### Grounding Electrode Conductor (GEC)
✓ **GEC**: 4 AWG copper (CEC Table 250.66)  
*Same as NEC 2023 Table 250.66 for 2/0 service conductors*

---

## CEC vs NEC 2023 Detailed Comparison

### Service Conductor Sizing (200A Dwelling)
| Code | Table | 200A Service Conductor Size |
|------|-------|-----------------------------|
| **CEC 2022** | Table 310.12(A) | 2/0 AWG copper |
| **NEC 2023** | Table 310.12(A) | 2/0 AWG copper |
*No California amendments modify this requirement*

### EGC Sizing (200A Overcurrent Device)
| Code | Table | EGC Size |
|------|-------|----------|
| **CEC 2022** | Table 250.122 | 6 AWG copper |
| **NEC 2023** | Table 250.122 | 6 AWG copper |
*California maintains identical requirements*

### GEC Sizing (2/0 Service Conductors)
| Code | Table | GEC Size |
|------|-------|----------|
| **CEC 2022** | Table 250.66 | 4 AWG copper |
| **NEC 2023** | Table 250.66 | 4 AWG copper |
*No differences between codes for this conductor size*

---

## Key Code References
1. **Service Conductors**: CEC 310.12(A) (identical to NEC 2023)
2. **EGC Sizing**: CEC 250.122 (matches ...

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 250.122, 250.66, 310.12

**Response Time:** 21.2s

---

### cec-023: commercial_load [CA-SPECIFIC]

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The ...

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022 vs NEC 2023)

### **California (CEC 2022) Calculation**
- **Base Value**: **1.3 VA per square foot** (Table 220.12)  
- **Total Load**:  
  ```
  5,000 sq ft × 1.3 VA/sq ft = 6,500 VA (6.5 kVA)
  ```
- **Key Note**: The **125% continuous load multiplier** is **already included** in CEC Table 220.12 values (per informational note).  
  → **Final Load**: 6,500 VA × 1.25 = **8,125 VA (8.125 kVA)**

---

### **NEC 2023 Comparison**
- **Base Value**: **1.3 VA per square foot** (Table 220.42(A))  
- **Total Load**:  
  ```
  5,000 sq ft × 1.3 VA/sq ft = 6,500 VA (6.5 kVA)
  ```
- **Key Difference**: NEC **does not include** the 125% multiplier in Table 220.42(A). It must be applied separately for continuous loads.  
  → **Final Load**: 6,500 VA × 1.25 = **8,125 VA (8.125 kVA)**

---

### **Critical Code Differences**
| Feature                | **CEC 2022**                          | **NEC 2023**                          |
|------------------------|----------------------------------------|----------------------------------------|
| **Table Reference**    | Table 220.12                           | Table 220.42(A)                        |
| **Base Value (Office)**| 1.3 VA/sq ft (includes 125% multiplier) | 1.3 VA/sq ft (multiplier applied separately) |
| **Power Factor Basis** | 100% power factor (note)               | 80% power factor (note)                |

---

### **Final Answer**
- **California (CEC 2022)**: **8,125 VA** (includes 1...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 17.2s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit (CEc vs NEC)

### **California (CEC 2022)**
- **Requirement**: **10 amperes** for 16 AWG copper conductors extending beyond the enclosure.
- **Basis**: CEC Table 430.72(B), Column C explicitly lists **10A** for 16 AWG copper.

### **NEC 2023**
- **Requirement**: **10 amperes** for 16 AWG copper conductors extending beyond the enclosure.
- **Basis**: NEC Table 430.72(B)(2), Column C also lists **10A** for 16 AWG copper.

---

### **Key Comparison**
| **Aspect**                | **CEC 2022**                     | **NEC 2023**                     |
|---------------------------|----------------------------------|----------------------------------|
| **Conductor Size**         | 16 AWG copper                   | 16 AWG copper                   |
| **Protection Rating**      | 10A (Column C)                  | 10A (Column C)                  |
| **Table Reference**        | Table 430.72(B)                 | Table 430.72(B)(2)              |
| **California Amendments**  | **No amendments** apply here.   | N/A                             |

---

### **Conclusion**
- **CEC and NEC alignment**: Both codes specify **10A** as the maximum overcurrent protection for 16 AWG copper motor control conductors extending beyond the enclosure.
- **No California amendments**: The CEC adopts NEC Table 430.72(B) without modification for this application.

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 430.72

**Response Time:** 20.2s

---

### cec-025: dwelling_load [CA-SPECIFIC]

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022 vs NEC 2023)

**California (CEC 2022):**  
Per **CEC Table 220.12**:  
- **Dwelling unit general lighting load**: **3 VA per square foot**  
- **Calculation**: 2,400 sq ft × 3 VA/sq ft = **7,200 VA (7.2 kVA)**  

**NEC 2023 Comparison:**  
- **NEC Table 220.42(A)** specifies identical **3 VA/sq ft** for dwelling units (Section 220.41).  
- **No amendments** in California for this specific calculation.  

**Key Code References:**  
- **CEC 2022**: Table 220.12, Section 220.12(A)  
- **NEC 2023**: Table 220.42(A), Section 220.41  

**Conclusion:**  
The general lighting load calculation for a 2,400 sq ft dwelling unit is **identical** under both CEC 2022 and NEC 2023 at **7,200 VA**.  

✓ Source: CEC 2022 / NEC 2023 Table 220.12 (CEC) / Table 220.42(A) (NEC)

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 220.12, 220.41, 220.42

**Response Time:** 18.6s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for...

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## Kitchen GFCI Requirements Comparison (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirements**  
- **Section 210.8(A)(6):** Requires **GFCI protection for all receptacles installed to serve countertop surfaces in kitchens**.  
- **Exceptions:**  
  - Listed locking receptacles for ceiling fans (not applicable to countertop circuits).  
  - Receptacles for fire alarm systems (not relevant to kitchens).  

### **NEC 2023 Requirements**  
- **Section 210.8(A)(6):** Mandates **GFCI protection for all kitchen countertop receptacles**.  
- **Exceptions:**  
  - Identical exceptions for ceiling fans and fire alarm systems (no impact on countertop circuits).  

---

### **Restrictiveness Analysis**  
1. **Scope of Application**  
   - Both codes apply GFCI protection to **all kitchen countertop receptacles**.  
   - CEC explicitly references **sink proximity** (1.8 m/6 ft) in its GFCI requirements, while NEC 2023 includes this implicitly under general GFCI rules.  

2. **Exceptions**  
   - Exceptions in both codes (e.g., ceiling fans) **do not apply to countertop circuits**, preserving full coverage.  

3. **California Amendments**  
   - CEC does **not add stricter requirements** beyond NEC for kitchen countertop GFCI.  

---

### **Conclusion**  
- **Equally Restrictive:** Both CEC 2022 and NEC 2023 have **identical requirements** for kitchen countertop GFCI protection.  
- **No Additional Restrictions:** California does not impose stricter rules than NEC for this application.  

✓...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 210.8

**Response Time:** 16.3s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO suc...

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Final Answer: Panelboard Space Requirements (CEC 2022 vs NEC 2023)

### **California Electrical Code (CEC 2022)**
- **Reserved Circuit Breaker Spaces** (Section 408.2(A)):
  - **Mandatory** for single-family dwellings: Panelboards must include dedicated spaces for:
    - Heat pump water heaters
    - Heat pump space heaters
    - Electric cooktops
    - Electric clothes dryers
  - **Exceptions Checked**: No exceptions override this requirement. Related exceptions (e.g., 408.38 for enclosures, 408.55 for wire-bending space) do not relax the reserved space mandate in 408.2(A).

### **National Electrical Code (NEC 2023)**
- **No Specific Requirements** for reserved spaces in single-family dwellings.
  - General panelboard rules apply (e.g., 408.30 for minimum rating), but **no appliance-specific space mandates**.

---

### **Key Differences**
| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**                          |
|---------------------------|------------------------------------------------------------------------------|---------------------------------------|
| **Reserved Spaces**       | Requires 4 dedicated spaces for appliances (Section 408.2(A)).              | No appliance-specific space mandates. |
| **Scope**                 | Applies to single-family residential buildings.                             | Applies universally without CA amendments. |
| **Restrictiveness**       | **More restricti...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 408.2, 408.30, 408.38, 408.55

**Response Time:** 13.3s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules fo...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## California EV Charging Exceptions (CEC 2022)

### **Exceptions to Key Rules**
1. **Interactive Systems (625.48)**  
   - Allows EVSE with *power export* functions (bidirectional charging) if:  
     - Listed and marked for the application.  
     - Compliant with Article 702 (optional standby systems) or 705 (PV systems).  
   - **Exception Context**: Permits shared circuits in interactive systems if equipment is listed for the application.  

2. **Multiple Feeders/Branch Circuits (625.47)**  
   - Permits more than one feeder/branch circuit to supply EVSE *if equipment is identified* for the application.  
   - **Exception Context**: Overrides the general rule in 625.40 requiring individual circuits for non-interactive systems.  

---

### **Impact on CEC vs NEC Comparison**
- **NEC 2023** allows shared circuits for EVSE (per 625.15) unless local codes prohibit it.  
- **CEC 2022** generally requires individual circuits (625.40) but *permits exceptions* for:  
  - Bidirectional systems (625.48).  
  - Multi-circuit installations with listed equipment (625.47).  

---

### **Final Answer**  
California’s CEC 2022 mandates stricter EV infrastructure requirements than NEC 2023, including CALGreen mandates for new construction, individual branch circuits, and weatherproof enclosures. However, exceptions in **625.47** and **625.48** provide flexibility for interactive/bidirectional systems and multi-circuit installations with listed equipment. NEC 2023 lacks these specific exc...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 625.15, 625.40, 625.47, 625.48

**Response Time:** 15.9s

---

### cec-029: afci [CA-SPECIFIC]

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and sim...

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements Comparison (CEC 2022 vs NEC 2023) – **With Exceptions**

---

### **Exceptions in CEC 2022 for 210.12(A) (Dwelling Units)**

1. **Receptacle Replacements (CEC 406.4(D)(4))**  
   - **Requirement**: When replacing receptacles in AFCI-protected areas (per 210.12(A)), the replacement must be:  
     - A listed outlet branch-circuit type AFCI receptacle, or  
     - A receptacle protected by a listed outlet branch-circuit type AFCI receptacle, or  
     - A receptacle protected by a listed combination-type AFCI circuit breaker.  
   - **Exception**: Section 210.12(D) Exception **does not apply** to receptacle replacements.  
   - **Implication**: California mandates **strict compliance** for AFCI-protected receptacle replacements, with no exceptions for short extensions (unlike 210.12(D)).  

2. **Marking Requirements**  
   - Receptacles protected by AFCI circuit breakers must be marked "GFCI Protected" and "No Equipment Ground" if no grounding conductor is present.  
   - This aligns with NEC 406.4(D)(2)(c) but emphasizes **visible markings** post-installation.  

---

### **Updated Comparison Table**

| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|---------------------------|------------------------------------------------------------------------------|------------------------------------------------------...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 210.12, 404.22, 406.4

**Response Time:** 17.5s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key differ...

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## Final Answer: California vs NEC Solar PV Requirements (CEC 2022 vs NEC 2023)

### Key Exceptions Identified:
1. **Rapid Shutdown Exemption** (CEC 690.12 Exception):  
   - **Ground-mounted PV systems** in buildings *solely* housing PV equipment are **exempt** from rapid shutdown requirements.  
   - Example: A ground-mounted PV array with a building used only for equipment storage does **not** need rapid shutdown compliance.  

2. **Wiring Method Flexibility** (CEC 690.31 Exception):  
   - **Nonmetallic enclosures/raceways** permitted for PV hazard control systems if listed/field-labeled.  
   - Allows use of nonmetallic materials at building penetration points for hazard control actuators.  

3. **Bipolar System Separation Exception** (CEC 690.31(E) Exception):  
   - Listed switchgear with physical barriers can replace separate enclosures for bipolar PV systems.  

---

### Revised Comparison with Exceptions Considered

#### 1. **Rapid Shutdown Requirements**  
- **CEc**:  
  - **Mandatory** for **all PV systems on buildings** (≤30V/80V limits).  
  - **Exception**: Ground-mounted systems in buildings with *sole purpose* of housing PV equipment are **exempt**.  
- **nec**:  
  - Similar rapid shutdown requirements but **no explicit voltage limits** or exemptions for ground-mounted systems.  
- **Restrictiveness**:  
  - **CEC is more restrictive** for most building-integrated systems but **more permissive** for ground-mounted systems in dedicated buildings.  

#### 2. *...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 310.15, 690.12, 690.31, 690.47

**Response Time:** 25.7s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **NEC Comparison Tool Used**: 30/30
- **cec_lookup_table Used**: 7/30
- **Success Rate**: 100.0%
- **Average Response Time**: 18.6s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

### Prompt Improvements Tested

This run tests 3 prompt improvements from run 18 error analysis:

1. **Table Content Routing** (fixes cec-007, cec-008)
   - Added `cec_lookup_table` to CEC tools table
   - Added explicit routing rule for "What does Table X specify?" questions

2. **Completeness Check** (fixes cec-013, cec-017)
   - Added: "Did I include BOTH copper AND aluminum options?"
   - Added: "Did I list ALL types from the table?"

3. **Comparison Reasoning** (fixes cec-026)
   - Added structured reasoning for "which is more restrictive" questions
   - MORE RESTRICTIVE = applies to MORE things/places/situations

