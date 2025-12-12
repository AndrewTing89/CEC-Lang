# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-06
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Successful** | 30 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 702.1s |
| **Avg per Question** | 23.4s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2 requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, (4) electric clothes dryers, and (5) electric vehicle charging equipment. This is a California-specific requirem...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings in California

**California Requirement (CEC 2022):**  
Per **CEC 2022 Section 408.2(A)**, panelboards in single-family residential buildings must include **reserved circuit breaker spaces** for the following appliances:  
- Heat pump water heaters  
- Heat pump space heaters  
- Electric cooktops  
- Electric clothes dryers  

This requirement is part of the California Energy Code (CEC) to ensure future-ready electrical infrastructure for energy-efficient appliances.  

**Key Details:**  
- Applies to **single-family buildings** with one or two dwellings.  
- Panelboards must be sized to accommodate these reserved spaces even if the appliances are not yet installed.  

---

## NEC 2023 Reference  
The **NEC 2023 does not include these specific appliance-reserved space requirements**. California’s 408.2(A) is an amendment to the national code, reflecting state-specific energy efficiency goals.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 408.2

**Response Time:** 18.2s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. CEC 408.2 requires panelboard spaces for EV charging equipment. Title 24 also mandates EV charging readiness.

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California Electrical Code (CEC 2022) Requirements for EV Charging in New Residential Construction  

### **1. Scope and CALGreen Integration**  
- **CEC 625.1**:  
  - Applies to EV charging infrastructure, including power export and bidirectional systems.  
  - **California-specific**: Requires compliance with **CALGreen Chapter 4 and 5** for new construction (e.g., pre-wiring for EV charging).  
  - **NEC Comparison**: NEC 2023 lacks CALGreen integration; CEC mandates additional pre-wiring and sustainability requirements.  

---

### **2. Branch Circuits and Load Management**  
- **CEC 625.40**:  
  - Each EV charging outlet must be on an **individual branch circuit** with **no other outlets**.  
  - **Exception (625.42)**: EV charging loads are treated as **continuous loads**. Service/feeder sizing must match equipment ratings or use automatic load management systems (with restricted access to prevent user tampering).  
  - **NEC Comparison**: NEC 2023 (220.57) allows EV load calculations at 7,200W or nameplate rating, but CEC adds CALGreen pre-wiring and stricter load management rules.  

---

### **3. Equipment Connection Methods**  
- **CEC 625.44**:  
  - **Portable Equipment**: Must use listed receptacles (e.g., 15/20A, 125V or 250V).  
  - **Fastened-in-Place Equipment**: Requires listed receptacles up to 50A.  
  - **Fixed Equipment**: Must be **permanently wired**.  
  - **NEC Comparison**: NEC 2023 (625.44) has similar connection methods but lacks CALGreen pre-wiring mandates.  

---

### **4. Ventilation Requirements**  
- **CEC 625.52**:  
  - **Ventilation Not Required**: If equipment is listed for indoor use without ventilation (e.g., battery-based systems).  
  - **Ventilation Required**: If equipment requires it, mechanical ventilation (supply/exhaust) must be installed per **Table 625.52(B)(1)(a/b)** or engineering calculations.  
  - **Exception**: Positive-pressure systems allowed only in approved facilities.  
  - **NEC Comparison**: NEC 20...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 9 found
- 220.57, 625.40, 625.54, 210.8, 625.42, 625.44, 625.48, 625.1, 625.52

**Response Time:** 34.8s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California-Specific Solar PV Requirements (CEc 2022)  

### 1. **Voltage Limits & Temperature Corrections**  
- **CEC 2022 Section 690.7**:  
  - **Residential systems**: Maximum DC voltage limited to **600V** (vs. 1000V for non-residential).  
  - **Voltage correction**: Must use module-specific temperature coefficients or **Table 690.7(A)** for crystalline silicon modules.  
  - **Exception**: Systems not in buildings may use up to **1500V** with listed equipment.  
- **NEC Comparison**:  
  NEC 2023 allows 1000V for all systems in buildings. California’s 600V limit for residential is stricter.  

---

### 2. **Arc-Fault Circuit Protection**  
- **CEC 2022 Section 690.11**:  
  - **Mandatory**: Listed PV arc-fault circuit interrupters (AFCIs) for DC circuits ≥80V.  
  - **Exception**: Systems in **metallic raceways**, **metal-clad cables**, or **underground** are exempt.  
- **NEC Comparison**:  
  NEC 2023 requires similar AFCI protection but does **not exempt** metallic raceways. California’s exception reduces AFCI use in certain installations.  

---

### 3. **Overcurrent Protection & Conductor Sizing**  
- **CEC 2022 Sections 690.8/690.9**:  
  - **Conductor sizing**: Must be ≥**125%** of calculated maximum current.  
  - **Exception**: Listed devices rated for continuous operation at **100%** of their rating may use 100% capacity.  
  - **Short conductors** (≤3m/10ft): May be protected at one end if in raceways or underground.  
- **NEC Comparison**:  
  NEC 2023 requires 125% sizing but does **not allow** 100% use of listed devices. California’s flexibility reduces overcurrent device size in some cases.  

---

### 4. **Stand-Alone Systems**  
- **CEC 2022 Section 690.10**:  
  - Requires compliance with **CEC 710.15** for stand-alone systems (e.g., battery storage integration).  
- **NEC Comparison**:  
  NEC 2023 references 705.12 for interconnections but does **not mandate** 710.15 specifics. California adds explicit residential integration rules.  

-...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 690.9, 705.12, 710.15, 690.7, 690.11, 690.8, 690.10

**Response Time:** 27.1s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Final Answer: California Circuit Requirements for Heat Pump Water Heaters in New Dwellings (CEC 2022)

**CEC 2022 Requirements:**
1. **Dedicated Circuits and Panelboard Spaces**  
   - Per **CEC 2022 Section 422.3(A)** and **408.2(A)**:  
     - Single-family buildings (1–2 dwellings) must provide **designated spaces, receptacles, branch circuits, and circuit identifications** for heat pump water heaters.  
     - Panelboards must include **dedicated circuit breaker spaces** for heat pump water heaters as specified in **California Energy Code Section 150.0(n)**.  

2. **No Applicable Exceptions**  
   - Exceptions found in **Section 422.12** (central heating equipment) and **Section 422.47** (water heater controls) do **not apply** to heat pump water heaters.  
   - These exceptions pertain to **conventional water heaters** or **central heating systems**, not heat pump appliances.  

3. **California-Specific Amendment**  
   - This requirement is a **California Energy Code amendment** to the NEC, ensuring infrastructure readiness for energy-efficient appliances.  

---

## NEC 2023 Reference  
**No direct equivalent in NEC 2023.**  
- The base NEC does **not mandate dedicated circuits** for heat pump water heaters in dwelling units.  
- California’s requirements are **amendments to the NEC**, ensuring readiness for future installations of high-efficiency appliances.  

---

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 422.3, 422.47, 422.12, 150.0, 408.2

**Response Time:** 29.9s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness Requirements (CEC 2022)

**California Requirement:**  
Per **CEC 2022 Section 422.3**, new residential buildings in California must provide **dedicated circuits and circuit identifications** for electric cooktop readiness:  

- **Single-Family Buildings** (1–2 dwellings):  
  Each dwelling unit must include:  
  - Designated spaces, receptacles, and branch circuits for electric cooktops as specified in **California Energy Code Section 150.0(u)**.  

- **Multifamily Buildings**:  
  Each dwelling unit must include:  
  - Dedicated circuits and circuit identifications for electric cooktops as specified in **California Energy Code Section 160.9(b)**.  

These requirements ensure future-ready infrastructure for electric cooktops, even if not installed at the time of construction.  

---

## NEC 2023 Reference  
The **NEC 2023** does not include equivalent provisions for electric cooktop readiness. This is a **California-specific amendment** [CEC] to promote energy efficiency and support electrification goals.  

---

**Sources:**  
✓ **CEC 2022 (primary):** Sections 422.3, California Energy Code 150.0(u)/160.9(b)  
✓ **NEC 2023 (comparison):** No equivalent requirements  
⚠️ **No exceptions** apply to these readiness provisions.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 422.3, 150.0, 160.9

**Response Time:** 13.0s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryers in California New Construction (CEC 2022)

**California Requirements (CEC 2022):**  
1. **Single-Family Buildings** (Section 408.2(A) & 422.3(A)):  
   - Panelboards must include **circuit breaker spaces** for electric clothes dryers as specified in the California Energy Code (Section 150.0(v)).  
   - This ensures readiness for future electric dryer installations, including heat pump dryers.  

2. **Multifamily Buildings** (Section 408.2(B) & 422.3(B)):  
   - Panelboards must include **dedicated circuits** for electric clothes dryers as per California Energy Code (Section 160.9(c)).  
   - Applies to each dwelling unit unless on-site laundry facilities are provided for all occupants (Exception 210.52(F)).  

3. **Load Calculations** (Section 220.54):  
   - Electric dryers must be calculated at **5000W minimum** (or nameplate rating, whichever is larger).  

**Exceptions:**  
- In multifamily buildings, receptacles for laundry equipment are **not required** if on-site laundry facilities are provided (Exception 210.52(F)).  

---

## NEC 2023 Reference  
- **NEC 2023** requires a **240V circuit** for electric dryers (Section 220.54) but does **not mandate** pre-wiring for specific appliances like heat pump dryers.  
- California’s CEC adds **Energy Code amendments** requiring panelboard readiness for future electric appliances, which are **not part of the base NEC**.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 220.54, 422.3, 150.0, 408.2, 160.9, 210.52

**Response Time:** 14.6s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) and California-Specific Exceptions

**California Requirement (CEC 2022):**  
While **Table 240.4(G)** itself is not explicitly amended in the CEC 2022, **Section 370.23** provides a California-specific exception for cablebus overcurrent protection. This exception allows compliance with **240.100** and **240.101** instead of the standard requirements in 240.4(G).  

**Key Details from CEC 2022:**  
- **Section 370.23 Exception**:  
  > *"Overcurrent protection shall be permitted in accordance with 240.100 and 240.101."*  
  This exception is unique to the CEC and not present in the NEC.  

**NEC Comparison:**  
- The NEC 2023 version of Table 240.4(G) does not include this exception. California’s CEC explicitly permits alternative overcurrent protection methods for cablebus systems via 240.100/240.101, which are not referenced in the NEC for this application.  

**Conclusion:**  
The **unique California provision** is the exception in **Section 370.23**, which allows compliance with 240.100/240.101 for cablebus overcurrent protection. This is not part of the NEC and reflects a specific amendment in the CEC.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_search, cec_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 240.100, 240.4, 370.23, 240.101

**Response Time:** 25.8s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 242.3 for California Installations

**California Requirement (CEC 2022):**  
CEC Table 242.3 is a **cross-reference table** under Article 242 (Overvoltage Protection). It specifies that equipment must be protected against overvoltage in accordance with the article in the Code that covers the type of equipment or location. This table is marked with an **"N"** in the CEC, indicating it is a **California-specific amendment** not present in the base NEC.  

Key details:  
- **Purpose**: Directs users to other NEC/CEC articles containing overvoltage protection requirements for specific equipment types (e.g., SPDs, Class I/II locations).  
- **Example Cross-References**:  
  - 240.4 (Overcurrent protection for conductors).  
  - 240.100–240.101 (Overcurrent protection for specific equipment).  
  - 450.3 (Transformers).  
  - 610.33 (Industrial control equipment).  

**Exception Note**:  
While no direct exceptions to Table 242.3 were found, CEC Section 370.23 permits alternative overcurrent protection methods for cablebus systems under 240.100/240.101. This highlights California’s emphasis on flexibility in overcurrent/overvoltage protection for specialized systems.  

---

## NEC 2023 Reference  
The NEC includes a similar Table 242.3 but **lacks California-specific amendments**. The CEC’s version adds explicit cross-references tailored to California’s electrical needs (e.g., industrial control systems, cablebus).  

**Key Difference**:  
- **CEC**: Explicitly marks Table 242.3 as a California amendment [CEC].  
- **NEC**: No such amendments; the table remains general.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 240.100, 240.4, 242.3, 450.3, 610.33, 370.23, 240.101

**Response Time:** 34.8s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection  
**California Electrical Code (CEC 2022)**  

### Table Structure and Values  
The table specifies **maximum overcurrent protective device ratings (in amperes)** for motor control circuits based on conductor size and installation configuration. Columns A, B, and C apply to different scenarios:  

| Conductor Size | Column A (Separate Protection) | Column B (Branch-Circuit Protection, In-Enclosure) | Column C (Branch-Circuit Protection, Beyond Enclosure) |  
|----------------|-------------------------------|---------------------------------------------------|------------------------------------------------------|  
| 18 AWG         | 7A (Copper)                   | 25A (Copper)                                      | 7A (Copper)                                          |  
| 16 AWG         | 10A (Copper)                  | 40A (Copper)                                      | 10A (Copper)                                         |  
| 14 AWG         | *Note 1*                      | 100A (Copper)                                     | 45A (Copper)                                         |  
| 12 AWG         | *Note 1*                      | 120A (Copper/Aluminum)                            | 60A (Copper/Aluminum)                                |  
| 10 AWG         | *Note 1*                      | 160A (Copper/Aluminum)                            | 90A (Copper/Aluminum)                                |  
| >10 AWG        | *Note 1*                      | *Note 2*                                          | *Note 3*                                             |  

**Notes:**  
1. Refer to **CEC 310.15** for values.  
2. 400% of **Table 310.17** (60°C conductors).  
3. 300% of **Table 310.16** (60°C conductors).  

---

### Key Exceptions and Applications  
1. **Exception No. 1 (Critical Systems):**  
   - Control circuits where opening would create a hazard (e.g., fire pump motors) require **only short-c...

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 8 found
- 430.55, 430.72, 430.32, 310.15, 310.17, 310.16, 430.94, 430.206

**Response Time:** 23.7s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Final Answer

**California's Medium Voltage Cable Tables and Exceptions**

### **CEC 2022 Medium Voltage Cable Tables**  
California's **20 unique medium voltage cable tables** (311.60(C)(67)-(C)(86)) address ampacities for cables rated 2001V–35,000V in air and underground installations. These tables are **not present in NEC 2023** and include scenarios like triplexed conductors, three-conductor cables, and direct burial.  

---

### **Key Exceptions Affecting Table Application**  
1. **Ampacity Selection Flexibility**  
   - **CEC 311.60(A)(2):** Allows using higher ampacity for portions of a circuit if the lower ampacity section is ≤ 3.0 m (10 ft) or 10% of the total circuit.  
   - *NEC Comparison:* No equivalent exception. NEC requires using the lowest ampacity for the entire circuit.  

2. **Nonshielded Cable Permits**  
   - **CEC 311.36:** Nonshielded multiconductor cables rated 2001V–2400V are permitted with a metallic sheath or armor.  
   - *NEC Comparison:* NEC 2023 requires shielding for all medium voltage cables above 2000V.  

3. **Shielding Requirements**  
   - **CEC 311.44:** Nonshielded cables up to 5000V are allowed in industrial facilities with qualified personnel, provided insulation resists ozone, discharge, and tracking.  
   - *NEC Comparison:* NEC mandates shielding for all medium voltage cables above 2000V.  

4. **Direct Burial Derating**  
   - **CEC 311.60(D)(2)(b):** Requires a **6% ampacity reduction per foot** for burial depths exceeding standard values.  
   - *NEC Comparison:* NEC lacks specific burial depth derating rules for medium voltage cables.  

5. **Insulation Thickness Variations**  
   - **CEC 311.10:** Specifies insulation thickness for shielded/unshielded conductors (Tables 311.10(B) and (C)).  
   - *NEC Comparison:* NEC uses generalized insulation standards (e.g., Table 310.104(B)).  

---

### **Critical Cross-References**  
- **Cable Tray Rules:** Tables apply with modifications from **392.80(B)** (e.g., 75% ampac...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 311.60, 311.10, 392.80, 310.104, 310.16, 310.17, 311.44, 311.36

**Response Time:** 26.1s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Ampacity of 4/0 AWG Copper Conductor at 75°C (CEC 2022)

**California Requirement:**  
Per **CEC 2022 Table 310.16**, the ampacity of a **4/0 AWG copper conductor at 75°C** is **230 amperes**. This value applies under standard conditions (30°C ambient temperature, not more than three current-carrying conductors in a raceway/cable).

**Exceptions Checked:**  
- **Section 310.12** (dwelling service/feeder adjustments): Not applicable here.  
- **Section 210.19** (branch circuit ampacity requirements): Does not override Table 310.16 for this conductor size/temperature.  
- **Section 240.4(D)** (overcurrent protection limitations): Must be referenced for overcurrent device sizing (e.g., 4/0 AWG copper at 75°C allows up to 250A protection per 240.4(D)).  

**Key Notes:**  
- If more than three current-carrying conductors are bundled, apply **Section 310.15(C)(1)** derating.  
- For ambient temperatures ≠ 30°C, apply **Section 310.15(B)** temperature correction factors.  

---
## NEC 2023 Reference  
**No difference from NEC 2023.** The ampacity for 4/0 AWG copper at 75°C is also **230A** per NEC Table 310.16.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 240.4, 310.12, 210.19, 310.15, 310.16

**Response Time:** 8.7s

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

This is specified in **CEC 2022 Table 250.122**, which aligns with NEC 2023 Table 250.122 but includes a California amendment ([CEC]). The amendment modifies the base NEC requirement, ensuring the EGC can safely carry fault currents and coordinate with the overcurrent device.

**Exception Analysis**:  
After reviewing exceptions to Table 250.122 (e.g., 250.121, 250.134, 356.60), no applicable exceptions override the standard sizing for a typical 200A AC circuit. Exceptions related to DC circuits, separately run EGCs, or grounded conductor use for grounding do not apply here unless specific conditions are met (not indicated in the question).

---
## NEC 2023 Reference  
No difference from NEC 2023. The EGC sizing for 200A circuits is identical in both codes.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.122, 250.121, 250.134, 356.60

**Response Time:** 15.0s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022)

For a **3/0 AWG copper service conductor** in California:

- **Required GEC Size**: **4 AWG copper**  
  (Per CEC 2022 Table 250.66, Column for copper grounding electrode conductors)

**Exceptions Checked**:  
- **250.66(A)**: If connected to rod/pipe electrodes, GEC can be 6 AWG copper.  
- **250.66(B)**: If connected to concrete-encased electrodes, GEC can be 4 AWG copper.  
- **250.66(C)**: If connected to ground rings, GEC size matches the ground ring conductor.  

Since the question does not specify the electrode type, the default requirement from **Table 250.66** applies (4 AWG copper). This aligns with the exception for concrete-encased electrodes, which is a common installation type.

---

## NEC 2023 Reference  
No difference from NEC 2023. The same 4 AWG copper requirement applies under NEC Table 250.66 for a 3/0 AWG service conductor.  

✓ **Sources**: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 15.4s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)

**California Requirement:**
- For a 75°C rated conductor at 40°C ambient temperature:
  - **Correction Factor:** 0.88  
  - **Reference:** CEC 2022 Table 310.15(B)(1)(1)

**Exceptions/Conditions:**
1. **Exception 2 (310.15):** Correction factors apply only if the corrected ampacity does not exceed the termination temperature rating (per 110.14(C)).  
2. **Exception 3 (310.14):** Higher ampacity is permitted for short circuit portions (<3.0 m or 10% of total circuit length).

---
## NEC 2023 Reference
No difference from NEC 2023. The same correction factor of 0.88 applies per NEC Table 310.15(B)(1).

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 110.14, 310.15, 310.14

**Response Time:** 26.1s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor for 7-9 Conductors (CEC 2022)

**California Requirement:**
For 7-9 current-carrying conductors in a raceway, the ampacity adjustment factor is **0.70** per CEC 2022 Table 310.15(C)(1). This means you multiply the conductor's base ampacity by 0.70 to account for the heat generated by multiple conductors in close proximity.

**Exceptions Checked:**
- No California-specific exceptions apply to this adjustment factor. The general exceptions in CEC 310.15 (e.g., for cable trays, short raceways, or specific conductor types) do not override the 0.70 factor for 7-9 conductors.

---
## NEC 2023 Reference
No difference from NEC 2023. The adjustment factor for 7-9 conductors remains **0.70** in Table 310.15(C)(1).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 24.0s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth for 480V Panelboard (Condition 3)  
**California Requirement (CEC 2022):**  
The minimum working space depth for a 480V panelboard under **Condition 3** (exposed live parts on both sides) is **1.2 meters (4 feet)**, per **CEC 2022 Table 110.26(A)(1)**.  

**Key Details:**  
- **Voltage Range:** 151–600 volts (480V falls in this range).  
- **Condition 3:** Applies when exposed live parts are on both sides of the working space.  
- **Table Reference:** CEC Table 110.26(A)(1) specifies depths for all voltage ranges and conditions.  

**No applicable exceptions** were found for this rule in the CEC.  

---
## NEC 2023 Reference  
The requirement matches **NEC 2023 Table 110.26(A)(1)**. California has no amendments to this specific requirement.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_working_space, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 13.6s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
According to **CEC 2022 Table 110.28**, the following enclosure types are suitable for outdoor use with protection against rain, sleet, and ice:

- **Type 4**: Watertight, dusttight, and corrosion-resistant for outdoor use.  
- **Type 4X**: Same as Type 4 but with corrosion protection for chemical environments.  
- **Type 6**: Watertight and dusttight, suitable for outdoor use with temporary water submersion.  
- **Type 6P**: Same as Type 6 but includes protection against the entry of water from hose-directed spray.  

**Key Requirements**:  
- These enclosures are rated **watertight** (protects against water ingress from all directions, including sleet).  
- The **mechanism shall be operable when ice-covered** (footnote in Table 110.28).  
- They are not intended for environments with condensation or corrosion from within the enclosure (per Section 409.100).  

**Exceptions/Additional Context**:  
- **110.26(E)**: Outdoor installations must comply with dedicated equipment space requirements (e.g., 1.8 m [6 ft] dedicated zone above equipment).  
- **110.70**: Enclosures for personnel entry must be sized for safe work space and conductor installation.  

No exceptions to Table 110.28 itself were found.  

---
## NEC 2023 Reference  
No difference from NEC 2023. Table 110.28 and its requirements are identical in both codes.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 110.26, 409.100, 110.70, 110.28

**Response Time:** 23.7s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 3.5 VA per square foot per CEC 2022 Table 220.12 [California Amendment]

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)

**California Requirement:**  
Per **CEC 2022 Table 220.12**, the general lighting load for **office buildings** is **1.3 volt-amperes per square foot (VA/ft²)**. This value includes the 125% continuous load multiplier required by 210.20(A) for lighting circuits.

**Key Notes:**  
- The 1.3 VA/ft² value accounts for minimum load conditions and assumes 100% power factor (as noted in the CEC text).  
- **Exception (220.12(B))**: If the building complies with an energy code and meets specific monitoring/system requirements, the lighting load may be calculated using energy code values instead of Table 220.12.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The national code also specifies **1.3 VA/ft²** for office buildings in **NEC Table 220.42(A)**.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 220.42, 210.20, 220.12

**Response Time:** 28.6s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1) [California Amendment]

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Final Answer

**California Requirement (CEC 2022):**  
The ampacity for a 12 AWG flexible cord with Column B thermoset insulation is specified in **Table 400.5(A)(2)** of the California Electrical Code. While the exact value was not retrieved via tools, the table typically lists ampacities for flexible cords based on conductor size and insulation type. For example, similar entries in NEC Table 400.5(A)(2) (which aligns with CEC unless amended) show:  
- **12 AWG Column B thermoset** = **20 amperes** (for two-conductor cords with ≤3 current-carrying conductors).  

**Key Adjustments per CEC 2022:**  
1. **Temperature Correction**: If ambient temperature exceeds 30°C (86°F), apply factors from Table 310.15(B)(1).  
2. **Bundling Adjustment**: If more than three current-carrying conductors are bundled, reduce ampacity per Table 400.5(A)(3).  

---

## NEC 2023 Reference  
The NEC specifies identical ampacities in **Table 400.5(A)(2)** for 12 AWG Column B thermoset. California amendments ([CEC]) do not modify this value, so no difference exists between CEC and NEC for this requirement.  

**Action Required:**  
Verify the exact ampacity in **CEC Table 400.5(A)(2)** for 12 AWG Column B thermoset. Apply correction factors if ambient temperature or conductor count deviates from standard conditions.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**  
⚠️ *Exact value not retrieved via tools; consult official CEC document.*

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_ampacity, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 400.5, 310.15

**Response Time:** 32.8s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire

**California Requirement (CEc 2022):**  
Per CEC 2022 Table 402.3, **Type SF-2 silicone insulated fixture wire** has a **maximum operating temperature of 200°C (392°F)**. This applies to both solid/7-strand and flexible stranding configurations.  

**NEC 2023 Reference:**  
No difference from NEC 2023. The temperature rating for Type SF-2 remains 200°C in the national code as well.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 402.3

**Response Time:** 23.9s

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

4. **Adjusted Ampacity Calculation**:  
   ```python
   adjusted = 50 × 0.88 × 0.70 = 30.8 amperes
   ```

**Final Answer: 30.8 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1). No exceptions to these derating requirements were found.

---
## NEC 2023 Reference
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 14.8s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Final Answer

## Service Conductor Sizing (CEC 2022)

**For a 200A residential service using copper conductors:**

1. **Service Conductors**  
   - **Size:** 4/0 AWG copper  
   - **Ampacity:** 230 amperes (per CEC 2022 Table 310.16, 75°C column)  
   - **Rationale:** 4/0 AWG copper at 75°C provides 230A, which exceeds the 200A service rating. This complies with CEC 240.4(D) overcurrent protection limits (200A breaker is permitted for 4/0 AWG).  

2. **Equipment Grounding Conductor (EGC)**  
   - **Size:** 6 AWG copper  
   - **Reference:** CEC 2022 Table 250.122  
   - **Rationale:** For a 200A overcurrent device, the minimum EGC size is 6 AWG copper.  

3. **Grounding Electrode Conductor (GEC)**  
   - **Size:** 4 AWG copper  
   - **Reference:** CEC 2022 Table 250.66 (interpolated for 200A service)  
   - **Rationale:** For a 200A service, the GEC must be at least 4 AWG copper when connected to a ground rod electrode.  

---

## NEC 2023 Reference  
- **Service Conductors:** Same requirements apply (NEC 2023 Table 310.16, 4/0 AWG copper at 75°C = 230A).  
- **EGC/GEC:** Same sizes apply (NEC 2023 Tables 250.122 and 250.66).  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_conductor_ampacity, cec_lookup_conductor_ampacity, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.122, 240.4, 310.16, 250.66

**Response Time:** 22.6s

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
- Floor area: 5,000 sq ft  

**Steps:**  
1. **Unit Load from CEC Table 220.12:**  
   - Office occupancy = **14 VA/sq ft** (per CEC 2022 Table 220.12).  
   - Note: The 125% continuous load multiplier is already included in this value.  

2. **Calculation:**  
   $$
   5,000 \, \text{sq ft} \times 14 \, \text{VA/sq ft} = 70,000 \, \text{VA}
   $$  

**Final Answer:**  
The general lighting load for the 5,000 sq ft office building is **70,000 volt-amperes (VA)**.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The unit load for office occupancies is also 14 VA/sq ft in NEC Table 220.12.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 220.12

**Response Time:** 18.5s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit Conductors (CEC 2022)

**CEC Requirement:**  
16 AWG copper conductors are **not listed in CEC Table 310.16** for ampacity, and **240.4(D)** does not specify overcurrent limits for 16 AWG. However, **motor control circuits** are governed by **Article 430**, which allows exceptions to standard overcurrent rules.

**Key CEC Provisions:**  
1. **430.55 (Combined Overcurrent Protection):**  
   - Permits combining overload and fault-current protection in a single device if it meets motor protection requirements.  
   - **Exception:** Overcurrent protection for motor control circuits may be based on motor overload settings, not conductor size.  

2. **430.225 (Motor-Circuit Overcurrent Protection):**  
   - Overload protection must be set to **115% of the motor’s full-load current (FLC)**.  
   - Fault-current protection (e.g., fuses or breakers) must be sized to protect the motor and conductors from short circuits.  

3. **240.21(F) (Motor Circuit Taps):**  
   - Allows motor control conductors to be protected by the motor’s overload protection, bypassing standard 240.4(D) limits.  

**Practical Application:**  
- For 16 AWG conductors in motor control circuits, the **overcurrent protection is determined by the motor’s FLC**, not the conductor’s ampacity.  
- Example: If the motor’s FLC is 10A, overload protection can be set to **11.5A (10A × 1.15)**. Fault-current protection (e.g., a circuit breaker) must be sized to protect the motor and circuit from short circuits.  

**NEC 2023 Reference:**  
- NEC 2023 aligns with CEC on motor control circuits (Article 430). 16 AWG is not in NEC Table 310.16, and 240.4(D) does not apply. Overcurrent protection is based on motor requirements, not conductor size.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 430.225, 240.4, 430.55, 240.21, 310.16

**Response Time:** 47.9s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## Final Answer (CEC 2022)  
The general lighting load for a 2,400 sq ft dwelling unit in California is **7,200 volt-amperes (VA)**, calculated as:  
$$
2,400 \, \text{sq ft} \times 3 \, \text{VA/sq ft} = 7,200 \, \text{VA}
$$  
This follows **CEC 2022 Section 220.14(J)**, which mandates 3 VA/ft² for dwelling units.  

---

## NEC 2023 Reference  
No difference from NEC 2023. The national code also specifies **3 VA/ft²** for dwelling unit general lighting and receptacle loads (NEC 220.14(J)).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 220.14

**Response Time:** 18.7s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## **Final Answer: CEC 2022 vs. NEC 2023 Kitchen GFCI Requirements**  

### **CEC 2022 (California Electrical Code)**  
- **Scope**: GFCI protection required **only for receptacles serving countertop surfaces** in kitchens (Section 210.8(A)(6)).  
- **Exceptions**:  
  - Receptacles not readily accessible (e.g., for snow-melting, deicing).  
  - Listed weight-supporting ceiling receptacles (WSCR) for ceiling fans/luminaires.  
- **No GFCI for**: Wall, floor, or other non-countertop receptacles in kitchens.  

---

### **NEC 2023 (National Electrical Code)**  
- **Scope**: GFCI protection required for **all 125–250V receptacles in kitchens**, including countertops, walls, and floors (Section 210.8(A)(5)).  
- **Exceptions**:  
  - Non-accessible receptacles for snow-melting/deicing.  
  - HVAC equipment (temporary exemption until 2026).  
  - Factory-installed, non-accessible receptacles in bathroom exhaust fans.  
- **Broader Coverage**: Applies to all kitchen receptacles, not just countertops.  

---

### **Which Code is More Restrictive?**  
The **NEC 2023 is more restrictive** because:  
1. **Broader Scope**: Requires GFCI protection for **all kitchen receptacles** (walls, floors, countertops), while CEC 2022 limits it to **only countertop receptacles**.  
2. **Exceptions**: Both codes share similar exceptions, but NEC includes additional exemptions (e.g., HVAC equipment), which do not outweigh its broader scope.  

**Example**: A wall-mounted receptacle in a kitchen for a microwave would require GFCI under NEC but not under CEC unless it serves a countertop.  

✓ **Sources**: CEC 2022 (California), NEC 2023 (reference)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: Yes

**Citations:** 1 found
- 210.8

**Response Time:** 28.8s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2 requires reserved panelboard spaces for heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers, and EV charging equipment. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Final Answer: Panelboard Space Requirements (CEC 2022 vs NEC 2023)

---

### **California Electrical Code (CEC 2022) Requirements**  
1. **Appliance-Specific Circuit Breaker Spaces**  
   - **Mandatory**: Panelboards in single-family dwellings must include dedicated spaces for:  
     - Heat pump water heaters  
     - Heat pump space heaters  
     - Electric cooktops  
     - Electric clothes dryers  
     *(Per CEC 408.2(A), referencing California Energy Code Sections 150.0(n), (t), (u), and (v)).*  

2. **Wire-Bending Space Exceptions**  
   - **Standard**: Top/bottom wire-bending space must comply with **Table 312.6(B)** for the largest conductor.  
   - **Exceptions** (CEC 408.55):  
     - **Exception No. 1**: Panelboards rated ≤225A with ≤42 overcurrent devices can use **Table 312.6(A)** for top/bottom spaces.  
     - **Exception No. 2**: If one side uses Table 312.6(B), the opposite side can use Table 312.6(A).  
     - **Exception No. 3**: Single 90° bends allow Table 312.6(A) spacing if wiring diagrams specify the method.  
     - **Exception No. 4**: Unused spaces can use Table 312.6(A).  

3. **Enclosure Requirements**  
   - Panelboards must be dead-front unless accessible only to qualified persons *(CEC 408.38 exception)*.  

---

### **National Electrical Code (NEC 2023) Requirements**  
1. **General Panelboard Rating**  
   - Same as CEC: Panelboards must meet the minimum feeder capacity per Article 220.  

2. **Wire-Bending Space**  
   - Top/bottom wire-bending space must comply with **Table 312.6(B)(2)** for the largest conductor.  
   - Exceptions mirror CEC 408.55 but reference **Table 312.6(B)(2)** instead of Table 312.6(B).  

3. **No Appliance-Specific Requirements**  
   - NEC does **not** mandate pre-wiring for heat pump water heaters, cooktops, or dryers in single-family dwellings.  

---

### **Key Differences**  
| **Aspect**                     | **CEC 2022 (California)**                          | **NEC 2023 (National)**          ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 312.6, 408.55, 150.0, 408.2, 408.38

**Response Time:** 26.8s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## Final Answer: California (CEC 2022) vs. NEC 2023 EV Charging Requirements  

### **1. Electric Vehicle Branch Circuits**  
- **CEC 625.40**:  
  - **Base Rule**: Individual branch circuits required for EV outlets (no shared circuits).  
  - **Exception (625.47)**: Allows **multiple feeders/branch circuits** if equipment is identified for the application.  
  - **California Amendment**: CALGreen integration for new construction.  
- **NEC 625.40**:  
  - Permits **shared circuits** for dedicated EVSE (not individual circuits).  
  - **No state-specific mandates** or CALGreen requirements.  

**Key Difference**: CEC mandates **individual circuits** unless exceptions apply, while NEC allows shared circuits for dedicated EVSE.  

---

### **2. Electrified Truck Parking Safety**  
- **CEC 626.3**:  
  - **Base Rule**: Applies to electrified truck parking systems but **excludes** equipment for cargo loading/unloading (626.4).  
  - **Exception (626.4)**: Clarifies scope limitations.  
  - **California Amendment**: Requires compliance with **Article 511/514** for repair/storage facilities.  
- **NEC 626.3**:  
  - General safety requirements but **no explicit cross-references** to 511/514.  

**Key Difference**: CEC adds **mandatory 511/514 compliance** for truck parking in repair/storage facilities.  

---

### **3. Bidirectional Systems (Power Export)**  
- **CEC 625.48**:  
  - **Base Rule**: EVSE with power export must be **listed** and marked for interactive systems.  
  - **Exception (625.47)**: References **UL 9741/SAE J3072** standards (California-specific).  
- **NEC 625.48**:  
  - Similar listing requirements but **no state-specific standards**.  

**Key Difference**: CEC mandates **UL 9741/SAE J3072 compliance** for bidirectional systems.  

---

### **4. Weatherproof Enclosures**  
- **CEC 625.56**:  
  - **Base Rule**: Receptacles in wet locations require **extra-duty weatherproof enclosures**.  
  - **Exception (250.86)**: Allows exceptions for short sect...

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_search, cec_exception_search, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: nec_search, compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 625.56, 250.86, 625.40, 625.48, 625.47, 626.3, 626.4

**Response Time:** 27.6s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## **CEC 2022 AFCI Requirements for Dwelling Units**  
**Section 210.12(A)**:  
- **Scope**: All 120V, single-phase, 15- and 20-ampere branch circuits in **kitchens, family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, or similar rooms/areas** must have AFCI protection.  
- **Permitted Methods**:  
  1. Combination-type AFCI at the branch circuit origin.  
  2. Branch/feeder-type AFCI + outlet branch-circuit-type AFCI at the first outlet.  
  3. Supplemental arc protection circuit breaker + outlet branch-circuit AFCI (with conductor length limits).  
  4. Outlet branch-circuit AFCI at the first outlet (with conductor length limits).  
  5. Outlet branch-circuit AFCI if metal raceway or concrete-encased wiring is used.  

**Exceptions**:  
- Fire alarm systems installed per 760.41(B)/760.121(B) are exempt.  
- Branch circuit extensions ≤1.8 m (6 ft) without additional outlets are exempt.  

---

## **NEC 2023 AFCI Requirements for Dwelling Units**  
**Section 210.12(A)**:  
- **Scope**: All 120V, single-phase, 10-, 15-, and 20-ampere branch circuits in **bedrooms, living rooms, hallways, closets, bathrooms, and similar rooms**.  
- **Permitted Methods**:  
  1. Combination-type AFCI.  
  2. Branch/feeder-type AFCI + outlet branch-circuit AFCI.  
  3. Outlet branch-circuit AFCI (with conductor length limits).  

**Exceptions**:  
- Fire alarm systems installed per 760.41(B)/760.121(B) are exempt.  
- Arc welding equipment circuits are exempt until January 1, 2025.  
- HVAC equipment is exempt until September 1, 2026.  

---

## **Key Differences**  
1. **Scope of Coverage**:  
   - **CEC**: Explicitly includes **laundry areas** and "similar rooms/areas" (e.g., sunrooms, recreation rooms).  
   - **NEC**: Adds **bathrooms** and **closets** to the list but excludes laundry areas (covered under general "similar rooms").  

2. **Permitted Methods**:  
   - **CEC**: Allows **six methods*...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search, nec_exception_search, compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 760.121, 760.41, 210.12

**Response Time:** 12.4s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California (CEC 2022) vs NEC 2023 Solar PV Requirements

### **1. Arc-Fault Circuit Protection (690.11)**  
- **CEC 2022**:  
  - Requires arc-fault protection for PV systems with DC circuits ≥80V.  
  - **Exception**: Permits omission for systems installed in metallic raceways, metal-clad cables, enclosed metallic trays, or underground (e.g., remote PV arrays in conduit).  
  - [CEC 690.11 Exception]  

- **NEC 2023**:  
  - Requires arc-fault protection for all PV DC circuits ≥80V (no exception for raceway installations).  
  - No exception found in tool results for NEC 2023.  

---

### **2. Energy Storage System Integration (690.71)**  
- **CEC 2022**:  
  - Requires energy storage systems (ESS) connected to PV systems to comply with **Article 706** (ESS installation).  
  - [CEC 690.71]  

- **NEC 2023**:  
  - Also references Article 706 for ESS, but CEC adds explicit enforcement for PV-ESS hybrid systems.  

---

### **3. Connection to Other Sources (690.59)**  
- **CEC 2022**:  
  - Mandates compliance with **Article 705 (Interconnection)** and **Article 712 (Grid-Tied Systems)** for PV systems connected to other sources (e.g., grid, generators).  
  - [CEC 690.59]  

- **NEC 2023**:  
  - Similar requirements exist in NEC 705, but CEC adds specificity for California's grid-tied systems.  

---

### **4. Stand-Alone Systems (690.10)**  
- **CEC 2022**:  
  - Requires stand-alone PV systems to comply with **Article 710** (Emergency Systems).  
  - [CEC 690.10]  

- **NEC 2023**:  
  - No direct equivalent found in tool results.  

---

### **5. Wind Systems (Article 694)**  
- **CEC 2022**:  
  - Separately addresses wind electric systems in Article 694 (not part of Article 690 in NEC).  
  - [CEC Article 694]  

- **NEC 2023**:  
  - Wind systems are included in Article 690 (PV + wind combined).  

---

## Key California Amendments [CEC]  
1. **Arc-fault exception** for raceway-installed PV systems (690.11).  
2. **Explicit references** to Articles 705, 7...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search, compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 690.59, 690.11, 690.10, 690.71

**Response Time:** 24.1s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 23.4s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

