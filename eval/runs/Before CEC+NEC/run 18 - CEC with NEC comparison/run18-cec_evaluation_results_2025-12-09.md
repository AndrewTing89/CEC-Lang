# CEC Agent Evaluation - LangChain + Groq (NEC Comparison ON)

**Date:** 2025-12-09
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)
**NEC Comparison:** ENABLED

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Successful** | 30 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 528.3s |
| **Avg per Question** | 17.6s |

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

---

### **California Electrical Code (CEC 2022) Requirements**
1. **Reserved Circuit Breaker Spaces** (CEC 408.2(A)):
   - **Mandated appliances**: Heat pump water heaters, heat pump space heaters, electric cooktops, and electric clothes dryers.
   - **Code basis**: California Energy Code Sections 150.0(n), (t), (u), (v).

2. **Heat Pump Space Heater Readiness** (CEC 440.3(E)):
   - Requires designated spaces, receptacles, and branch circuits for heat pump space heaters.

3. **Exceptions**:
   - Special permission exceptions (424.10, 426.14) apply to **installation methods**, not panelboard space reservations.

---

### **National Electrical Code (NEC 2023) Comparison**
- **No appliance-specific reserved spaces**: NEC does not mandate reserved panelboard spaces for specific appliances (e.g., heat pump water heaters, cooktops).
- **General requirements**:
  - Panelboard ratings must match calculated loads (NEC 408.30).
  - Disconnecting means for fixed electric space heaters (NEC 424.19).
  - No provisions for appliance-specific readiness (e.g., heat pump circuits).

---

### **Key Differences**
| **Aspect**                     | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|-------------------------------|----------------------------------------------------------------------------...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 150.0, 408.2, 408.30, 424.10, 424.19, 426.14, 440.3

**Response Time:** 27.6s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements (CEC 2022) with Exceptions

### **Exceptions Check**
- **CEC 625.1**: No relevant exceptions found for residential construction.  
  - The only exception returned (604.12) relates to manufactured wiring systems and is not applicable to EV charging infrastructure.  

---

### **Final Answer**
#### **1. CALGreen Compliance (CEC 625.1.1)**  
- **Mandatory for new residential construction**:  
  - Reserved panel space for EV charging (CALGreen Chapter 4).  
  - EV-ready infrastructure (CALGreen Chapter 5).  

#### **2. Cords and Cables (CEC 625.17)**  
- **Maximum cord lengths**:  
  - Portable EVSE: **25 ft (7.5 m)**.  
  - Stationary equipment: **6 ft (1.8 m)** power-supply cord.  
- **Cable types**: Must use listed EV cable (EV, EVJ, etc.) or hard service cord (Table 400.4).  

#### **3. Ventilation (CEC 625.52)**  
- **Indoor charging**:  
  - If equipment isn’t listed for indoor use, **mechanical ventilation** is required.  
  - Ventilation must be **interlocked with the charging system**.  

#### **4. Ground-Fault Protection (CEC 625.54)**  
- **All EV receptacles** require **GFCI protection** (no exceptions for <60V DC).  

#### **5. NEC vs CEC Differences**  
- **CALGreen mandates**: No NEC equivalent.  
- **Stricter cord/ventilation rules**: CEC adds 25 ft max cord length and ventilation interlocks.  
- **GFCI exceptions**: CEC requires GFCI for all EVSE (<60V DC still requires protection).  

---

### **Key Citations**  
- **CEC 62...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 8 found
- 210.8, 220.57, 400.4, 604.12, 625.1, 625.17, 625.52, 625.54

**Response Time:** 23.9s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requir...

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements (CEC 2022) with Exceptions

### 1. **Rapid Shutdown (690.12)**  
**Requirement**:  
- All PV systems on buildings must include rapid shutdown to reduce firefighter shock hazards.  
- **Voltage limits**:  
  - ≤30V within 30 seconds outside the array boundary (1 ft from array).  
  - ≤80V within 30 seconds inside the array boundary.  
- **Labeling**: Permanent label at service equipment with **white text on red background** (min 9.5mm height).  

**Exceptions**:  
- Ground-mounted PV systems in buildings **solely housing PV equipment** are exempt (690.12 Exception).  
- PV hazard control systems meeting 690.12(B)(2)(1) may use **nonmetallic enclosures** at building penetration points (690.31(D) Exception).  

---

### 2. **Arc-Fault Protection (690.11)**  
**Requirement**:  
- DC arc-fault protection required for all systems ≥80V DC.  

**Exception**:  
- NEC allows exceptions for systems in metallic raceways or enclosed trays; **CEC has no such exception** for ground-mounted systems.  

---

### 3. **Grounding and Bonding (690.43)**  
**Requirement**:  
- PV arrays must connect to a grounding electrode system via **250.66-sized conductor**.  
- Metallic support structures require bonding jumpers between sections.  

**Exception**:  
- None noted for grounding electrode connection.  

---

### 4. **Wiring Methods (690.31)**  
**Requirement**:  
- **Type PV wire** or **distributed generation (DG) cable** for exposed outdoor DC circuits.  
- L...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 8 found
- 250.66, 690.11, 690.12, 690.31, 690.43, 690.56, 691.4, 691.9

**Response Time:** 19.4s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can sup...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## California vs NEC 2023 Requirements for Heat Pump Water Heaters

### **CEC 2022 (California) Requirements**  
1. **Dedicated Circuits & Panelboard Spaces** (CEC 422.3(A), 408.2(A)):  
   - **Single-family**: Panelboards must reserve spaces for heat pump water heaters per California Energy Code §150.0(n).  
   - **Multifamily**: Dedicated circuits required per §160.9(b).  
   - **Purpose**: Ensures electrification readiness for future adoption.  

2. **Application of Other Articles**:  
   - Follows NEC Articles 430 (motor-operated appliances) and 440 (refrigerant compressors) but with California amendments.  

---

### **NEC 2023 Provisions**  
1. **General Requirements** (NEC 422.10):  
   - Requires **dedicated branch circuits** for water heaters but **no panelboard space mandates**.  
   - No specific provisions for **heat pump water heaters** or electrification readiness.  

2. **Exceptions & Controls** (NEC 422.47):  
   - Applies to **storage/instantaneous water heaters**, not heat pumps.  
   - Exceptions for high-capacity storage heaters (60 kW+) or small instantaneous units (≤1 gal) **do not apply** to heat pump systems.  

---

### **Key Differences**  
| **Aspect**                | **CEC 2022 (California)**                          | **NEC 2023**                          |
|---------------------------|----------------------------------------------------|---------------------------------------|
| **Dedicated Circuits**    | Required for heat pump water heaters (1...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 150.0, 160.9, 408.2, 422.10, 422.3, 422.47

**Response Time:** 16.7s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrif...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness in California (CEC 2022) with Exceptions

### **California Requirements**
1. **Dedicated Circuits** (CEC 422.3 & CALGreen 150.0(u)/160.9(b)):
   - **Single-family**: Each dwelling unit must have a **dedicated circuit** for electric cooktops with **circuit identification** (e.g., labeled breaker).
   - **Multifamily**: Same requirement under CALGreen 160.9(b).
   - **Panelboard Space**: Panelboards must reserve **circuit breaker spaces** for cooktops (CEC 408.2).

2. **Electrification Mandate**:
   - Part of CALGreen's push for all-electric homes; no exceptions for gas appliances in new construction.

3. **Ampacity Compliance**:
   - Conductors must meet appliance ratings (CEC 422.10), typically requiring **40–50A circuits** for cooktops.

---

### **Exceptions to Rule 422.3**
1. **Non-Standard Installations** (CEC 422.23):
   - Appliances using installation methods not covered by CEC are **permitted only with special permission**.
   - Example: Custom cooktop installations requiring engineering approval.

2. **Cord-and-Plug-Connected Appliances** (CEC 422.33):
   - **Exception**: A plug-and-receptacle connection can serve as the disconnecting means **if accessible**.
   - For ranges, a rear-base plug accessible via a drawer is allowed.
   - Receptacle rating must match the appliance’s rating.

---

### **NEC 2023 Comparison**
- **No Dedicated Circuit Mandate**: NEC 422.10 only requires conductor ampacity ≥ appliance rating. No specific requiremen...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 150.0, 160.9, 408.2, 422.10, 422.23, 422.3, 422.33

**Response Time:** 13.1s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022 vs NEC 2023)  

---

### **Key Differences**  
| **Requirement**               | **CEC 2022 (California)**                                                                 | **NEC 2023 (National)**                                                                 |  
|------------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|  
| **Load Calculation**         | Minimum **5,000 VA** per dryer (or nameplate rating, whichever is larger).               | Same 5,000 VA minimum with **identical demand factors** in Table 220.54.               |  
| **Demand Factors**           | Identical to NEC Table 220.54 (e.g., 85% for 5 dryers, 75% for 6 dryers).              | Identical to CEC.                                                                      |  
| **Panelboard Readiness**     | **Mandates reserved circuit breaker spaces** for dryers in new construction (CEC 408.2). | **No requirement** for reserved spaces unless locally adopted.                         |  
| **Dedicated Circuits**       | Requires **dedicated circuits** for dryers in single-family and multifamily buildings.   | Permits shared circuits if load calculations allow (no dedicated circuit rule).        |  
| **Energy Code Integration**  | Tied to **California Energy Code (Title 24)** for electr...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 150.0, 160.9, 220.54, 408.2, 422.3

**Response Time:** 22.1s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) Exceptions and Limitations (CEC 2022)

After identifying exceptions related to **Table 240.4(G)**, here are the key findings that impact its application in California:

---

### 🔧 **Relevant Exceptions**
1. **Motor-Starting Currents (CEC 230.90, Exception 1)**  
   - **Applies to**: Motor and motor-control circuits (referenced in Table 240.4(G) under Article 430).  
   - **Exception**: Overcurrent devices for motor circuits may exceed conductor ampacity if the higher rating complies with **430.52, 430.62, and 430.63** (motor-starting current requirements).  
   - **Impact**: California allows higher overcurrent protection for motor circuits than standard 240.4(G) rules, accommodating inrush currents during motor startup.

2. **Busway Overcurrent Protection (CEC 370.23, Exception 1)**  
   - **Applies to**: Industrial busways referenced in Table 240.4(G) for motor and feeder circuits.  
   - **Exception**: Permits using **240.100/240.101** instead of 240.4 for overcurrent protection in industrial settings.  
   - **Impact**: California provides flexibility for industrial busway installations, overriding standard 240.4(G) requirements.

---

### 🚫 **Non-Applicable Exceptions**
- **Grounding Electrode Conductors (250.121)** and **Service Raceway Conductors (230.7)** do not affect Table 240.4(G) directly.  
- **Busway Reductions (370.23, Exceptions 2/3)** apply to specific industrial busway reductions, not the general conductor types in Table 240.4(G).

---
...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 10 found
- 230.7, 230.90, 240.100, 240.101, 240.4, 250.121, 370.23, 430.52, 430.62, 430.63

**Response Time:** 16.9s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Final Answer: CEC 2022 vs NEC 2023 on Wind Turbine Surge Protection  

### **Key Differences**  
1. **CEC 2022 (California):**  
   - **Mandates SPD for Wind Systems** (Section 694.7(D)):  
     - Requires surge protective devices (SPD) between wind systems and premises loads.  
     - Permits **Type 3 SPD** on wind system circuits or **Type 2 SPD** on load side of service disconnect.  
     - SPD installation must comply with **Part II of Article 242** (overcurrent protection).  
   - **Dwelling Unit SPD Mandate** (Section 230.67):  
     - All residential services **must** have a **Type 1 or Type 2 SPD**.  
     - Exceptions allow SPD installation downstream if not in service equipment.  

2. **NEC 2023:**  
   - **No Wind System SPD Requirements:**  
     - General SPD rules exist in Article 242 (overcurrent protection) but no wind-specific mandates.  
   - **Backfeed Signage** (Section 495.25):  
     - Requires "DANGER - CONTACTS ON EITHER SIDE..." signs where backfeed is possible.  

---

### **California-Specific Mandates**  
- **Residential SPDs:** CEC 230.67 enforces SPD installation for all dwelling units, a stricter requirement than NEC.  
- **Wind System SPDs:** CEC 694.7(D) ties SPD installation to **Part II of Article 242**, ensuring overcurrent protection compliance.  

---

### **Exceptions and Flexibility**  
- **SPD Location Flexibility** (CEC 230.67 Exception):  
  - Permits SPD installation downstream toward the load if not in service equipment.  
- **S...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search, compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 230.67, 230.94, 495.25, 694.7

**Response Time:** 24.0s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) vs NEC 2023 Comparison  
**California Electrical Code (CEC 2022) and National Electrical Code (NEC 2023) share identical table values** for motor control circuit overcurrent protection but differ in **exceptions, cross-references, and application rules**. Below is a structured comparison:

---

### **1. Table Structure and Values**  
| **Conductor Size** | **CEC Column A** | **CEC Column B** | **CEC Column C** | **NEC Column A** | **NEC Column B** | **NEC Column C** |
|---------------------|------------------|------------------|------------------|------------------|------------------|------------------|
| 18 AWG             | 7A (Cu)          | 25A (Cu)         | 7A (Cu)          | 7A (Cu)          | 25A (Cu)         | 7A (Cu)          |
| 16 AWG             | 10A (Cu)         | 40A (Cu)         | 10A (Cu)         | 10A (Cu)         | 40A (Cu)         | 10A (Cu)         |
| 14 AWG             | *(Note 1)*       | 100A (Cu)        | 45A (Cu)         | *(Note 1)*       | 100A (Cu)        | 45A (Cu)         |
| 12 AWG             | *(Note 1)*       | 120A (Cu/Al)     | 60A (Cu/Al)      | *(Note 1)*       | 120A (Cu/Al)     | 60A (Cu/Al)      |
| 10 AWG+            | *(Note 1)*       | 160A/140A (Cu/Al)| 90A/75A (Cu/Al)  | *(Note 1)*       | 160A/140A (Cu/Al)| 90A/75A (Cu/Al)  |

**Key Notes**:  
- **Column A**: CEC references **310.15** (ambient derating); NEC implicitly uses **310.15**.  
- **Column B**: CEC explicitly ties to **310.19** (60°C conductors ...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 310.15, 310.16, 310.19, 409.21, 430.72

**Response Time:** 27.5s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found i...

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in California (CEC 2022)  

### **California-Specific Medium Voltage Tables**  
California has **18 unique medium voltage cable tables** in **CEC 311.60(C)(67)–(86)** not present in the NEC. These tables cover:  
- **Triplexed cables** in air or conduit (e.g., Table 311.60(C)(67))  
- **Underground installations** (Tables 311.60(C)(77)–86)  
- **Direct burial** in earth  
- **Cable trays** with spacing/ventilation requirements  

---

### **Key Exceptions and Limitations**  
1. **Ampacity Selection (CEC 311.60(A)(2))**  
   - *Exception*: If a circuit has sections with different ampacities, the **higher ampacity** is permitted **if** the lower-ampacity section is ≤ 3.0 m (10 ft) or 10% of the total circuit length.  

2. **Temperature Corrections (CEC 311.60(D)(4))**  
   - Tables assume a **40°C ambient temperature**. For other temperatures, use correction factors from IEEE 835 or the formula:  
     $$
     I' = I \times \frac{T_c - T_a'}{T_c - T_a}
     $$  
     Where $ T_c $ = conductor rating, $ T_a $ = table ambient, $ T_a' $ = actual ambient.  

3. **Burial Depth Adjustments (CEC 311.60(D)(2))**  
   - For **deeper burial** than table values:  
     - **6% derating per 300 mm (1 ft)** increase in depth.  
   - For **shallower burial**, no adjustment is required.  

4. **Shield Grounding (CEC 311.60(D)(1))**  
   - Tables for cables with **single-point grounded shields** (e.g., Table 311.60(C)(69)).  
   - For **multi-point grounded shield...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 311.10, 311.60, 315.60

**Response Time:** 17.1s

---


## CEC Delta Tables

### cec-011: conductor_ampacity [CA-SPECIFIC]

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer: Ampacity of 4/0 AWG Copper at 75°C (CEC 2022)

**California Electrical Code (CEC 2022):**  
✓ **Ampacity:** 230 amperes  
✓ **Source:** CEC Table 310.16 (standard conditions)  

**Exceptions Checked:**  
1. **Section 440.6** (Refrigerant motor-compressors):  
   - Applies only to hermetic motor-compressors or multimotor equipment.  
   - Does not affect general conductor ampacity unless specifically for such equipment.  

2. **Section 110.40** (Termination temperature limitations):  
   - Permits 90°C-rated conductors for terminations (not applicable here, as the question specifies 75°C).  

**Conclusion:**  
No exceptions override the base ampacity of **230A** for 4/0 AWG copper at 75°C under standard conditions. If the conductor is for refrigeration equipment or has special termination requirements, additional rules apply (see exceptions above).  

✓ Source: CEC 2022 Table 310.16 / Exceptions 440.6, 110.40

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 110.40, 310.16, 440.6

**Response Time:** 11.0s

---

### cec-012: grounding [CA-SPECIFIC]

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size for 200A Circuit (CEC 2022)

**California Requirement (CEC 2022 Table 250.122):**
- **Copper**: 6 AWG
- **Aluminum/Copper-Clad**: 4 AWG

**NEC 2023 Comparison:**
- **NEC Table 250.122** specifies identical sizes:
  - 6 AWG copper
  - 4 AWG aluminum/copper-clad

**Key Exceptions and Notes:**
1. **250.142 Exception**: Permits using the grounded conductor for grounding equipment on the supply side or within specific enclosures. Not applicable here unless the installation meets those conditions.
2. **250.122 Exception**: Allows proportional sizing if ungrounded conductors are oversized. Not applicable for standard 200A circuits.
3. **Parallel Conductors (250.122(F))**: Requires separate EGCs in each raceway for parallel installations. Not relevant unless parallel conductors are used.

**Conclusion:**  
No exceptions modify the base requirement for a standard 200A circuit. The EGC must be sized per Table 250.122 as **6 AWG copper** or **4 AWG aluminum/copper-clad**.

✓ Source: CEC 2022 Table 250.122 (aligned with NEC 2023 Table 250.122)

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 250.122, 250.142

**Response Time:** 10.0s

---

### cec-013: grounding [CA-SPECIFIC]

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Final Answer: Grounding Electrode Conductor Size for 3/0 AWG Service Conductor

**Required GEC Size**: **4 AWG copper**  
**Reference**: CEC 2022 Table 250.66 (same as NEC 2023 Table 250.66)

---

### Exception Analysis
1. **Exception 250.66(A)**:  
   - Allows **6 AWG copper** if the GEC connects only to rod/pipe/plate electrodes *and* does not extend to other electrode types requiring larger conductors.  
   - **Does not apply here** because the question does not specify electrode type, and the default requirement remains 4 AWG copper.

2. **Exception 250.66(B)**:  
   - Allows **4 AWG copper** for concrete-encased electrodes (same as standard table value).  
   - **Applies if** the electrode is concrete-encased, but this is not specified in the question.

3. **Other exceptions** (250.66(C), 250.30, 250.190):  
   - Pertain to separately derived systems, equipment grounding, or specific installation scenarios not relevant to this service conductor application.

---

### Key Takeaways
- **Standard requirement**: 4 AWG copper (Table 250.66 for 3/0 AWG service conductor).  
- **No applicable exceptions** reduce the size unless specific electrode types are used (not indicated in the question).  
- **NEC 2023 alignment**: Identical table values, but California may have additional installation rules (e.g., 250.64(D) for multiple disconnects).

✓ Source: CEC 2022 Table 250.66 and exceptions

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 250.190, 250.30, 250.64, 250.66

**Response Time:** 10.3s

---

### cec-014: ampacity_adjustment [CA-SPECIFIC]

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (Final Answer with Exceptions Checked)

**Correction Factor:** 0.88  
**Source:** CEC Table 310.15(B)(1)(1) for 75°C-rated conductors at 40°C ambient temperature  

**Exception Review:**  
- Searched exceptions for **CEC 310.15(B)(1)** using context "temperature correction factor 75°C conductor 40°C ambient"  
- **No applicable exceptions** were found that modify this correction factor  
- Returned exceptions (352.60, 356.60, etc.) relate to grounding requirements, not temperature correction  

**Conclusion:**  
The correction factor of **0.88** applies without exception for 75°C-rated conductors in 40°C ambient conditions per CEC 2022.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 352.60, 356.60

**Response Time:** 8.9s

---

### cec-015: ampacity_adjustment [CA-SPECIFIC]

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor for 7-9 Conductors (CEC 2022)  

**California Code (CEC 2022):**  
- **Adjustment factor**: **0.70 (70%)** for 7–9 current-carrying conductors in a raceway.  
- **Applies to**: All conductors in the raceway, including spares and neutrals (per 310.15(C)(1)).  

**Exceptions/Overrides**:  
1. **Short raceways**: Adjustment factors **do not apply** if the raceway length does not exceed **600 mm (24 in.)** (310.15(C)(1)(b)).  
2. **Specific cable types**:  
   - **Type NM/NMC cables** in cable trays or contact with insulation: Adjustment factors apply (334.80).  
   - **Type AC/MC cables** with ≤3 conductors, 12 AWG copper, and ≤20 current-carrying conductors: Adjustment factors may not apply (310.15(C)(1)(d)).  
3. **Grounding/bonding conductors**: Excluded from the count (310.15(F)).  

**NEC 2023 Comparison**:  
- NEC uses **identical adjustment factors** in **Table 310.15(C)(1)** (7–9 conductors = 0.70).  
- Same exceptions apply, including short raceways (≤24 in.) and grounding conductor exclusions.  

✓ **Source**: CEC 2022 / NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 334.80

**Response Time:** 12.4s

---

### cec-016: working_space [CA-SPECIFIC]

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth (CEC 2022 vs NEC 2023)

**California Code (CEC 2022):**  
For 480V panelboard under **Condition 3** (exposed live parts on both sides of the working space):  
- **Minimum depth**: **1.2 meters (4 feet)**  
- Source: CEC Table 110.26(A)(1)  

**Exceptions Checked:**  
- **CEC 110.26(E)**: Requires dedicated electrical space (6 ft height zone) but does **not modify** the 4 ft working space depth for Condition 3.  
- Other exceptions (408.40, 352.60, etc.) relate to grounding and equipment location, not working space depth.  

**NEC 2023 Comparison:**  
- NEC Table 110.26(A)(1) also requires **4 feet (1.2 meters)** for 480V under Condition 3.  
- **No amendments** in California for this requirement ([CEC vs NEC comparison](#tool_call_2)).  

**Key Footnote:**  
Condition 3 applies when **exposed live parts are present on both sides** of the working space (e.g., front and back of a panelboard).  

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 110.26, 352.60, 408.40

**Response Time:** 10.2s

---

### cec-017: enclosure [CA-SPECIFIC]

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Final Answer: Suitable Enclosures for Outdoor Use (CEC 2022 with Exceptions)

### **California Code (CEC 2022)**
For outdoor use with **rain, sleet, and ice**, the following enclosures are suitable per **Table 110.28**:
- **Type 3S**, **3SX**, **3X** (raintight, dusttight, operable when ice-covered)
- **Type 4**, **4X**, **6**, **6P** (watertight, dusttight)

**Exceptions and Additional Requirements:**
1. **Receptacles in Damp/Wet Locations (Section 406.9):**
   - Outdoor receptacles must use **weatherproof enclosures** (e.g., Type 3S/3X/4) and be listed as weather-resistant (e.g., NEMA 5-15/5-20).
   - In wet locations, enclosures must remain weatherproof **with or without the plug inserted**.
   - Example: Type 3S or 4 enclosures are suitable for receptacles in outdoor kitchens or patios.

2. **Dedicated Equipment Space (Section 110.26(E)):**
   - Outdoor electrical equipment (e.g., panelboards) must be installed in **dedicated spaces** with:
     - Enclosures rated for outdoor use (per Table 110.28).
     - Protection from accidental contact, spills, or leaks.
   - Example: A Type 4X enclosure for a subpanel on a commercial building’s exterior.

---

### **NEC 2023 Comparison**
NEC 2023 aligns with CEC 2022 for enclosure types but lacks explicit "ice-covered operability" requirements. Both codes require:
- **Type 3S/3X/4/4X/6/6P** for outdoor use with rain/sleet.
- **Weatherproof enclosures** for receptacles in damp/wet locations (NEC 406.9).

**Key California-Specific ...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 110.26, 110.28, 406.9

**Response Time:** 13.6s

---

### cec-018: lighting_load [CA-SPECIFIC]

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022 vs NEC 2023)

**California Code (CEC 2022):**  
**1.3 VA per square foot** (14 VA/m²) per **Table 220.12**. This value includes the 125% continuous load multiplier from 210.20(A).

**NEC 2023:**  
**1.5 VA per square foot** (16 VA/m²) per **Table 220.42(A)** for office buildings. No automatic continuous load multiplier is applied unless specified in 210.20(A).

---

### Key Differences:
1. **Amended Value in CEC:**  
   California reduces the office lighting load from **1.5 VA/ft² (NEC)** to **1.3 VA/ft²** to align with stricter energy efficiency standards (Title 24, Part 6).

2. **Continuous Load Multiplier:**  
   - **CEC:** 125% multiplier is **included** in Table 220.12 values.  
   - **NEC:** 125% multiplier is **not included** in Table 220.42(A) and must be applied separately if required by 210.20(A).

3. **Exception for Energy Code Compliance (CEC 220.12(B)):**  
   If the building complies with a local energy code, alternative calculations are permitted **with monitoring systems** and alarms for load management.

---

### Cross-Reference Notes:
- **CEC 220.12** explicitly includes the 125% multiplier in its table values.  
- **NEC 220.42(A)** requires separate application of demand factors and does not embed the multiplier in the table.  
- California’s amendment reflects Title 24 energy code requirements, which prioritize reduced baseline loads for commercial buildings.

✓ Source: CEC 2022 Table 220.12, NEC 2023...

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 210.20, 220.12, 220.42

**Response Time:** 18.2s

---

### cec-019: flexible_cord [CA-SPECIFIC]

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Final Answer: 12 AWG Flexible Cord (Column B Thermoset) Ampacity

**California Code (CEC 2022):**  
**25 amperes** (CEC Table 400.5(A)(1)) for 12 AWG flexible cord in Column B thermoset.  
- Applies to two-conductor cords or multiconductor cords with only two current-carrying conductors.  
- Assumes ambient temperature of 30°C (86°F) and ≤3 current-carrying conductors.  

**NEC 2023 Comparison:**  
**25 amperes** (NEC Table 400.5(A)(1)) for the same conductor type.  
- **No amendments** in California for this specific value.  

---

### Key Differences/Amendments:  
- **No California amendments** to Table 400.5(A)(1) for Column B thermoset ampacities.  
- Exceptions found (e.g., Sections 352.60, 356.60) relate to grounding requirements, not ampacity adjustments.  
- Both codes reference the same temperature correction factors (Table 310.15(B)(1)) and bundling adjustments (Table 400.5(A)(3)).  

---

### Notes:  
- Column B applies to thermoset-insulated cords (e.g., SJOOW, SOOW, SPT-2).  
- For non-standard applications (e.g., >3 conductors, elevated temps), apply adjustments from **Table 310.15(B)(1)** and **Table 400.5(A)(3)**.  

✓ Source: CEC 2022 Table 400.5(A)(1) and NEC 2023 Table 400.5(A)(1)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 310.15, 352.60, 356.60, 400.5

**Response Time:** 19.7s

---

### cec-020: fixture_wire [CA-SPECIFIC]

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

### **California Electrical Code (CEC 2022)**
- **Type SF-2 Silicone Insulated Fixture Wire**:
  - **Solid or 7-strand**: **200°C (392°F)**  
    (Per CEC Table 402.3, entry for "Silicone insulated fixture wire — solid or 7-strand, type SF-2").
  - **Flexible stranding**: **150°C (302°F)**  
    (Per CEC Table 402.3, entry for "Silicone insulated fixture wire — flexible stranding, type SFF-2").

### **Exceptions Checked**
1. **CEC 336.80** (Ampacity for Type TC tray cable):  
   - References CEC 402.5 for 18–16 AWG conductors in cable trays.  
   - Does not override temperature ratings for Type SF-2.  
2. **CEC 402.12** (Uses Not Permitted):  
   - Prohibits using fixture wires as branch-circuit conductors except as permitted.  
   - No impact on temperature ratings.  
3. **CEC 337.80** (Ampacity for Type P cable):  
   - References Table 402.5 for 18–16 AWG conductors in cable trays.  
   - Temperature limits remain governed by Table 402.3.  

### **NEC 2023 Comparison**
- NEC does not explicitly list "Type SF-2" but includes similar silicone rubber-insulated types with **150°C** maximum operating temperature for flexible stranding.  
- CEC allows **200°C** for solid/7-strand Type SF-2, exceeding NEC-equivalent types.  

✓ Source: CEC 2022 Table 402.3 and exceptions verified.

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 336.80, 337.80, 402.12, 402.3, 402.5

**Response Time:** 21.4s

---


## Complex Calculations

### cec-021: adjusted_ampacity [CA-SPECIFIC]

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 ...

**CEC Ref:** CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1) | **NEC Ref:** NEC Tables 310.16, 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Final Answer with NEC 2023 Comparison

**Adjusted Ampacity**:  
**30.8 amperes** for both CEC 2022 and NEC 2023 calculations.

---

### **Key Comparison Details**

| **Parameter**               | **CEC 2022**       | **NEC 2023**       | **Difference** |
|-----------------------------|--------------------|--------------------|----------------|
| **Base Ampacity (8 AWG THWN)** | 50A @ 75°C         | 50A @ 75°C         | None           |
| **Temp Correction (40°C)**   | 0.88 (Table 310.15B)| 0.88 (Table 310.15B)| None           |
| **Bundling Adjustment (7 cond)** | 0.70 (Table 310.15C)| 0.70 (Table 310.15C)| None           |
| **Final Result**              | 30.8A              | 30.8A              | None           |

---

### **California Amendment Note**
- **No amendments** to NEC 310.16 for this scenario in CEC 2022.
- Temperature correction (40°C) and bundling (7 conductors) rules are **identical** to NEC 2023.
- California retains NEC's ampacity calculation methodology without modification for this case.

✓ Source: CEC 2022 & NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_find_limiting_rules, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 310.16

**Response Time:** 23.6s

---

### cec-022: service_sizing [CA-SPECIFIC]

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper...

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Final Service Sizing with NEC Comparison (CEC 2022)

### ✅ **Final Sizing for 200A Residential Service**
- **Service Conductor**: **2/0 AWG copper**  
  - **CEC/NEC Table 310.12(A)**: Identical in both codes.  
- **Equipment Grounding Conductor (EGC)**: **6 AWG copper**  
  - **CEC/NEC Table 250.122**: Identical in both codes.  
- **Grounding Electrode Conductor (GEC)**: **4 AWG copper**  
  - **CEC/NEC Table 250.66**: Identical in both codes.  

---

### 🔄 **CEC vs NEC Comparison**
| **Component**         | **CEC 2022**       | **NEC 2023**       | **Delta Markings**                     |
|-------------------------|--------------------|--------------------|----------------------------------------|
| **Service Conductor** | 2/0 AWG (Table 310.12) | 2/0 AWG (Table 310.12) | ✅ Same, [delta](#california-amendments) for CALGreen compliance |
| **EGC (200A)**        | 6 AWG (Table 250.122) | 6 AWG (Table 250.122) | ✅ Same                                |
| **GEC (2/0 service)** | 4 AWG (Table 250.66) | 4 AWG (Table 250.66) | ✅ Same                                |

---

### ⚠ **California Amendments ([Delta Markings](#delta-markings))**
- **Table 310.12(A)**: CALGreen mandates minimum conductor sizes for energy efficiency (no change for 200A).  
- **Tables 250.122/250.66**: No size changes, but California enforces stricter grounding electrode requirements (e.g., additional rods in some regions).  

---

### 📚 **Code Citations**
1. **Service Conductor**: CEC/NEC Table 310.12(A) ...

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 250.122, 250.66, 310.12

**Response Time:** 25.8s

---

### cec-023: commercial_load [CA-SPECIFIC]

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The ...

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)  
**Final Answer with Exceptions**  

### **Standard Calculation**  
- **Unit load**: 1.3 VA/sq ft (CEC Table 220.12 for "Office")  
- **Total load**:  
  `5,000 sq ft × 1.3 VA/sq ft = 6,500 VA (6.5 kVA)`  
- **Note**: The 125% continuous load multiplier is **already included** in CEC Table 220.12 values.  

---

### **Exceptions and Special Conditions**  
1. **Energy Code Compliance (CEC 220.12(B))**  
   - **Permitted alternative**: Use unit values from the local energy code **if**:  
     - A power monitoring system is installed.  
     - Alarms are set to alert if lighting load exceeds energy code limits.  
     - Demand factors from 220.42 are **not applied**.  
     - 125% continuous load multiplier is **applied separately**.  
   - **Relevance**: Not applicable here unless the building complies with an energy code.  

2. **Informational Note (CEC 220.12(A))**  
   - Table values are based on **100% power factor** and may be insufficient for installations with lower power factor.  

---

### **NEC 2023 Comparison**  
- **Unit load**: 1.3 VA/sq ft (NEC Table 220.42(A) for "Office")  
- **Total load**:  
  `5,000 sq ft × 1.3 VA/sq ft = 6,500 VA (6.5 kVA)`  
- **Key Difference**:  
  - CEC Table 220.12 **includes** the 125% continuous load multiplier.  
  - NEC Table 220.42(A) requires applying the 125% multiplier **separately** per 220.42.  

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 17.1s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for Motor Control Circuit (CEC vs NEC)

### **California Electrical Code (CEC 2022)**
- **Requirement:** 10A maximum overcurrent protection for **16 AWG copper conductors extending beyond the enclosure** (Table 430.72(B), Column C).
- **Basis:** 400% of the ampacity of 16 AWG copper at 60°C (19A from Table 310.19) → 76A theoretical maximum, but **hardcoded limit of 10A** in Table 430.72(B).

---

### **National Electrical Code (NEC 2023)**
- **Requirement:** Identical **10A limit** for 16 AWG copper conductors extending beyond the enclosure (Table 430.72(B)(2), Column C).
- **Basis:** Same 400% multiplier from Table 310.19 (19A × 4 = 76A), with the same hardcoded 10A cap.

---

### **Key Differences (if any)**
- **No California amendments** apply here. CEC aligns fully with NEC 2023 for this specific requirement.
- Both codes reference the **same tables** (310.19 for conductor ampacity, 430.72(B) for overcurrent limits).

---

### **Final Answer**
- **CEC 2022:** 10A maximum overcurrent protection for 16 AWG copper conductors extending beyond the enclosure.
- **NEC 2023:** Identical 10A requirement.
- **Conclusion:** California follows NEC without amendments for this provision.

✓ Source: CEC 2022 Table 430.72(B) and NEC 2023 Table 430.72(B)(2)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 310.19, 430.72

**Response Time:** 19.8s

---

### cec-025: dwelling_load [CA-SPECIFIC]

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Dwelling Unit (CEC 2022 vs NEC 2023)

### California Electrical Code (CEC 2022)
- **Section 220.14(J)**: Requires **3 VA per square foot** for **general lighting and receptacle loads** in dwelling units.
- **Calculation**:  
  $ 2,400 \, \text{sq ft} \times 3 \, \text{VA/sq ft} = 7,200 \, \text{VA} $

### National Electrical Code (NEC 2023)
- **Section 220.14(I)**: Also specifies **3 VA per square foot** for general lighting and receptacle loads in dwelling units.
- **Key Difference**:  
  - **CEC explicitly includes receptacle loads** in the 3 VA/ft² calculation (per 220.14(J)(1)-(3)).  
  - **NEC 220.14(I)** treats receptacle loads separately in some contexts but aligns with CEC for dwelling unit general lighting calculations.

### Code Comparison
- **No California amendments** to this section in CEC 2022 compared to NEC 2023.  
- Both codes yield the **same result**: **7,200 VA** for a 2,400 sq ft dwelling unit.

✓ Source: CEC 2022 Section 220.14(J) and NEC 2023 Section 220.14(I)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 220.14

**Response Time:** 18.7s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for...

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## Final Answer: CEC 2022 vs NEC 2023 Kitchen GFCI Requirements

### **Exceptions Found in CEC 2022**  
1. **Ceiling Fixtures Exception**:  
   - Listed locking receptacles for ceiling luminaires/fans are exempt from GFCI if they're integral to the fixture (Section 210.8).  
   - **Relevance**: Does not apply to countertop receptacles.  

2. **Fire Alarm Systems**:  
   - Receptacles for fire alarms in basements are exempt (Section 210.8(A)(5)).  
   - **Relevance**: Not applicable to standard kitchen circuits.  

3. **Dedicated Appliance Circuits**:  
   - No specific exception for refrigerators or microwaves on dedicated circuits.  

---

### **Final Comparison**  
| **Requirement**               | **CEC 2022**                          | **NEC 2023**                          |  
|-------------------------------|---------------------------------------|---------------------------------------|  
| **Countertop GFCI**           | Required (Section 210.8(A)(6)).       | Required (Section 210.8(A)(6)).       |  
| **Exceptions**                | Few exceptions (e.g., ceiling fixtures). | More exceptions (e.g., dedicated circuits for appliances). |  
| **Spacing Rules**            | 6 ft spacing required (Section 210.52). | No explicit spacing rules for kitchens. |  

---

### **Conclusion**  
**CEC 2022 is more restrictive** than NEC 2023 for kitchen GFCI requirements due to:  
1. **No exceptions** for common kitchen appliances on dedicated circuits.  
2. **Mandatory 6 ft spacing...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 210.52, 210.8, 422.5

**Response Time:** 15.2s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO suc...

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Final Answer: Panelboard Space Requirements (CEC 2022 vs NEC 2023)

### **California Electrical Code (CEC 2022)**
1. **Mandatory Reserved Spaces** (CEC 408.2(A)):
   - Single-family panelboards **must** include dedicated circuit breaker spaces for:
     - Heat pump water heaters
     - Heat pump space heaters
     - Electric cooktops
     - Electric clothes dryers
   - **Basis**: California Energy Code (Title 24) Sections 150.0(n), 150.0(t), 150.0(u), and 150.0(v).

2. **Exceptions**:
   - No exceptions apply to **408.2(A)** for reserved spaces in single-family dwellings.
   - Exceptions in related sections (e.g., 408.55 for wire-bending spaces) do not affect the reserved space requirements.

---

### **National Electrical Code (NEC 2023)**
1. **No Appliance-Specific Reserved Spaces**:
   - NEC does **not** mandate reserved spaces for specific appliances in single-family dwellings.
   - Focuses on general requirements:
     - Panelboard ratings based on load calculations (NEC 408.30).
     - Wire-bending spaces per Table 312.6 (NEC 408.55).

2. **Exceptions for Multifamily**:
   - NEC 422.34 allows unit switches as disconnecting means in **multifamily** dwellings but does **not** extend to single-family.

---

### **Key Differences**
| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|---------------------------|--------------------------...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 150.0, 312.6, 408.2, 408.30, 408.55, 422.34

**Response Time:** 12.7s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules fo...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## Final Answer: California (CEC 2022) vs NEC 2023 EV Charging Requirements  

### **Key Differences**  
1. **Scope**  
   - **CEC 625.1**: Explicitly includes **bidirectional power flow** (vehicle-to-grid).  
   - **NEC**: Focuses on unidirectional charging (no bidirectional requirements).  

2. **GFCI Protection**  
   - **CEC 625.54**: **Mandatory GFCI** for all EV receptacles.  
   - **NEC 210.8**: GFCI required only in specific locations (e.g., garages, wet areas).  

3. **Ventilation**  
   - **CEC 625.52**: **Mandatory ventilation** for indoor EV charging (based on power level).  
   - **NEC**: No ventilation requirements.  

4. **New Construction**  
   - **CEC 625.1.1**: CALGreen mandates **EV readiness** (reserved panel space, infrastructure).  
   - **NEC**: No state-specific mandates.  

5. **Load Calculations**  
   - **CEC**: Follows NEC 220.57 (7,200 VA minimum).  

---

### **Exceptions Check**  
- **CEC 625.1**: No exceptions found.  
- **CEC 625.40**: No exceptions found.  
- **CEC 625.52**: No exceptions found.  

---

### **Source Citations**  
- CEC 2022: Sections 625.1, 625.1.1, 625.40, 625.52, 625.54  
- NEC 2023: Sections 100, 210.8, 220.57  

✓ Source: CEC 2022 vs NEC 2023 comparison with exception verification.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 210.8, 220.57, 625.1, 625.40, 625.52, 625.54

**Response Time:** 15.5s

---

### cec-029: afci [CA-SPECIFIC]

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and sim...

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements: CEC 2022 vs NEC 2023 for Dwelling Units (With Exceptions)

### **California Electrical Code (CEC 2022)**
1. **Required Locations**  
   - All 120V, single-phase, 15- and 20-ampere branch circuits in:  
     - Kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, and similar spaces.  
     - Dormitory units (bedrooms, living rooms, etc.).  
     - Guest rooms, guest suites, and patient sleeping rooms in nursing homes.  

2. **Permitted AFCI Types**  
   - **Combination-type AFCI** (protects entire branch circuit).  
   - **Branch/feeder-type AFCI** + outlet branch-circuit-type AFCI at first outlet.  
   - **Supplemental arc protection circuit breaker** + outlet AFCI (with conductor length limits: 50 ft for 14 AWG, 70 ft for 12 AWG).  
   - **Outlet branch-circuit-type AFCI** at first outlet (with specific wiring continuity requirements).  
   - Exceptions for metal raceway/concrete-encased circuits.  

3. **Exceptions**  
   - Fire alarm circuits (760.41(B)/760.121(B)) if installed in metal raceway.  
   - Branch circuit extensions ≤6 ft without additional outlets (210.12(D)).  
   - **Receptacle Replacements**:  
     - **Exception 406.4(D)(4)**: When replacing receptacles in AFCI-protected areas (per 210.12(A), (B), or (C)), the replacement must be:  
       - A listed outlet branch-circuit-type AFCI receptacle.  
       - A receptacle protected by an outlet branch-circuit-...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 210.12, 404.22, 406.4, 760.121, 760.41

**Response Time:** 17.5s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key differ...

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California vs NEC Solar PV Requirements (CEC 2022 vs NEC 2023) – **Updated with Exceptions**

---

### **1. AC Module Treatment**  
- **CEC 690.6 (Exception)**  
  - **Key Exception**: PV source circuit requirements **do not apply** to AC modules.  
  - **Internal Component Rule**: PV source circuits, conductors, and inverters are treated as **internal components** of AC modules.  
  - **Output Circuit**: Output of AC modules is classified as an **inverter output circuit** (per 690.6(B)).  
  - **NEC 2023**: No specific exception for AC modules; PV source circuits are treated as standard DC circuits.  

---

### **2. PV-Powered Signs**  
- **CEC 600.34**  
  - Mandates compliance with **Article 690** for PV-powered signs.  
  - **California-Specific Rules**:  
    - Wiring must be **listed for PV applications**, secured every 0.91m (3 ft), and protected from damage.  
    - Flexible cords must be **extra hard usage**, **outdoor-rated**, and **water/sunlight-resistant**.  
  - **NEC 2023**: No specific provisions for PV-powered signs.  

---

### **3. Energy Storage Integration**  
- **CEC 690.71**  
  - Requires energy storage systems to comply with **Article 706**.  
  - **NEC 2023**: Article 706 exists but is not explicitly cross-referenced in NEC 690.  

---

### **4. System Connections**  
- **CEC 690.59**  
  - PV systems connected to other sources must follow **Article 705** and **Article 712** (microgrids).  
  - **NEC 2023**: Article 705 applies but lacks reference...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 9 found
- 600.34, 690.11, 690.4, 690.41, 690.47, 690.59, 690.6, 690.71, 690.91

**Response Time:** 18.6s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **NEC Comparison Tool Used**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 17.6s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

### NEC Comparison Feature

This evaluation was run with **force_nec_comparison=True**, which instructs the agent to:
1. Call the `compare_with_nec` tool for each question
2. Include differences between CEC 2022 and NEC 2023 in responses
3. Highlight California-specific amendments and requirements

