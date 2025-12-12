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
| **Total Duration** | 365.6s |
| **Avg per Question** | 12.2s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2(A) requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers, as specified in California Energy Code Section 150.0(n), (t), (u), and (v). ...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022) – Final Answer

### **Reserved Circuit Breaker Spaces**
Per **CEC 2022 Section 408.2(A)**, single-family residential buildings **must reserve circuit breaker spaces** for the following appliances:

1. **Heat Pump Water Heaters**  
2. **Heat Pump Space Heaters**  
3. **Electric Cooktops**  
4. **Electric Clothes Dryers**  

These requirements are mandated by the **California Energy Code (CEC) Sections 150.0(n), (t), (u), and (v)** to ensure future-ready electrical infrastructure for energy-efficient appliances.

---

### **Exception Check**
After calling `cec_exception_search` for **Section 408.2(A)**, no exceptions were found that modify or relax the reserved space requirements for single-family dwellings. The returned exceptions relate to panelboard enclosures, wire-bending spaces, overcurrent protection, and special permissions for heating equipment, none of which impact the reserved breaker spaces for the listed appliances.

---

### **Key Details**
- **Scope**: Applies to panelboards serving individual dwelling units in **single-family buildings** (1–2 dwellings).  
- **Purpose**: Ensures sufficient breaker spaces for electrification and energy code-compliant appliances.  
- **California-Specific**: These requirements are amendments to the NEC and not found in the national code.  

---

### **Source**
✓ **CEC 2022 Section 408.2(A)** and California Energy Code Sections 150.0(n), (t), (u), (v).  

No exceptions apply to this rule for single-family dwellings.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 408.2, 150.0

**Response Time:** 13.1s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in CEC Article 625 and Title 24 CALGreen (not CEC 408.2). Title 24 CALGreen mandates EV charging readi...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements (CEC 2022)  

### 1. **CALGreen Compliance**  
New residential construction must comply with **CALGreen Chapter 4 & 5** (CEC 625.1):  
- **Panelboard Space**: Reserved circuit breaker space for EV charging (CEC 408.2).  
- **Minimum Circuit**: Dedicated 40-amp branch circuit for EV charging.  

---

### 2. **Dedicated Branch Circuits**  
- **Individual Circuit**: Each EV outlet must be on a dedicated branch circuit with **no other outlets** (CEC 625.40).  
  - **Exception Check**: No exceptions apply to this rule. Section 625.46 (loss of primary source) and Section 694.10 (wind turbines) are unrelated to the dedicated circuit requirement.  

---

### 3. **Ventilation Requirements**  
- **Indoor Charging**: If EVSE requires ventilation (marked by manufacturer), install **mechanical ventilation** per Table 625.52(B)(1) or engineered systems (CEC 625.52).  
  - Ventilation must be **interlocked with the charging circuit** to remain energized during charging.  

---

### 4. **Weatherproof Enclosures**  
- **Outdoor Receptacles**: Enclosures must be **weatherproof** with extra-duty outlet box hoods (CEC 625.56).  

---

### 5. **Ground-Fault Protection**  
- **GFCI Required**: All EV charging receptacles must have **ground-fault circuit-interrupter (GFCI) protection** (CEC 625.54).  

---

### 6. **Cord and Cable Rules**  
- **Power-Supply Cord**:  
  - Max length: **12 in. (300 mm)** for portable equipment, **6 ft (1.8 m)** for stationary equipment (CEC 625.17).  
  - Cord types must comply with Table 400.4 (e.g., EV, EVJ, EVT).  
- **Output Cable**: Max usable length **25 ft (7.5 m)** unless using a listed cable management system.  

---

### 7. **Overcurrent Protection**  
- **EVPE (Power Export)**: Overcurrent protection must match receptacle ratings (CEC 625.60(C)).  

---

### 8. **Multiple Feeders/Branch Circuits**  
Allowed if equipment is identified for multi-circuit use (CEC 625.47).  

---

### Key California Mandates (CA...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 12 found
- 625.56, 625.54, 694.10, 400.4, 625.47, 625.60, 625.46, 625.40, 625.1, 408.2

**Response Time:** 15.2s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements (CEC 2022) with Exceptions

### 1. **Rapid Shutdown (690.12)**
- **Voltage Limits**: 
  - **Outside array boundary** (305 mm/1 ft from array): ≤30V within 30 seconds
  - **Inside array boundary**: ≤80V within 30 seconds (or use listed hazard control systems)
- **Initiation Device**: 
  - Must be located at a **readily accessible location outside the building** for single-family homes
  - Requires a **permanent label** indicating "RAPID SHUTDOWN SWITCH" (white on red, ≥9.5 mm font)
- **Exception**: 
  - **Ground-mounted systems** entering buildings (sole purpose: housing PV equipment) **exempt** from 690.12 requirements

### 2. **System Grounding (690.41)**
- **Ground-Fault Protection** required for DC circuits >30V or 8A
- **Exceptions**: 
  - Solidly grounded systems with ≤2 modules in parallel (not on/in buildings)
  - Systems using listed equipment with equivalent protection

### 3. **Labeling Requirements (690.56)**
- **Rapid Shutdown Labels**:
  - **Yellow background** with black text: "SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN"
  - **Red label** at switch: "RAPID SHUTDOWN SWITCH"
- **Voltage Labels**:
  - Permanent label showing **maximum DC voltage** at disconnect, inverter, or distribution equipment

### 4. **Wiring Methods (690.31)**
- **DC Circuits >30V/8A**:
  - Must use **metal raceways**, Type MC cable, or metal enclosures
  - **Exposed DC wiring** requires guarding or Type MC cable
- **Conductor Identification**:
  - Positive conductors: **+ or POSITIVE** (non-green/white/gray insulation)
  - Negative conductors: **- or NEGATIVE** (non-green/white/gray/red insulation)
- **Exception**: 
  - PV hazard control systems (per 690.12(B)(2)(1)) permitted to use **nonmetallic enclosures/raceways** at building penetration points

### 5. **Equipment Grounding (690.43)**
- All **non-current-carrying metal parts** (module frames, enclosures) must be bonded
- **Grounding Electrode Connection**:
  - PV arrays must connect to ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 9 found
- 690.41, 691.4, 690.31, 250.52, 691.9, 690.43, 250.54, 690.12, 690.56

**Response Time:** 14.3s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## California Circuit Requirements for Heat Pump Water Heaters (CEC 2022)  

### Key Requirements:  
1. **Dedicated Circuits**  
   - Single-family dwellings: Must have **dedicated circuits** as specified in **California Energy Code Section 150.0(n)**.  
   - Multifamily buildings: Follow **Section 160.9(b)** for circuit requirements.  

2. **Panelboard Spaces**  
   - Panelboards must reserve **circuit breaker spaces** for heat pump water heaters (and other appliances) per:  
     - **CEC 408.2(A)** for single-family buildings.  
     - **CEC 408.2(B)** for multifamily buildings.  

3. **Applicable Articles**  
   - **Article 430** (motor-operated appliances) and **Article 440** (refrigerant motor-compressors) apply, as amended by CEC.  

---

### Exceptions:  
1. **Temperature-Limiting Controls (422.47)**  
   - **Exception No. 1**: Storage water heaters rated for 82°C (180°F) or above and ≥60 kW capacity are exempt from additional temperature-limiting controls.  
   - **Exception No. 2**: Instantaneous-type water heaters ≤4 L (1 gal) capacity are exempt.  

2. **Central Heating Equipment (422.12)**  
   - **Exception No. 1**: Auxiliary equipment (e.g., pumps, humidifiers) can share a branch circuit with central heating equipment.  
   - **Exception No. 2**: Permanently connected air-conditioning equipment can share a circuit.  

---

### Limiting Rules:  
- **Overcurrent Protection**: Must comply with **Article 240** (e.g., OCP device sizing per 240.4).  
- **Conductor Sizing**: Follow **Article 310** ampacity tables (e.g., 310.16 for general use).  

---

### California Energy Code Cross-References:  
- **Single-family**: Check **Section 150.0(n)** for exact circuit details (e.g., voltage, amperage, receptacle requirements).  
- **Multifamily**: Refer to **Section 160.9** for multifamily dwelling unit specifications.  

---

### Summary of Actions Required:  
- **Designate dedicated circuits** for heat pump water heaters.  
- **Reserve panelboard spaces** as per...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 240.4, 310.16, 422.12, 150.0, 160.9, 422.47, 408.2

**Response Time:** 12.1s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness in New California Homes (CEC 2022)

### Requirements:
1. **Dedicated Circuits**  
   - **Single-family homes** (1–2 dwellings): Each dwelling unit must have **dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 150.0(u)**.  
   - **Multifamily buildings**: Each dwelling unit must have **dedicated circuits and circuit identifications** per **California Energy Code Section 160.9(b)**.  

2. **Circuit Identification**  
   - Circuits must be clearly labeled in the electrical panel to identify them as dedicated for electric cooktops.  

3. **Receptacle and Branch Circuit Requirements**  
   - Receptacles for cooktops must comply with **Section 210.52(C)**, ensuring accessibility and proper placement.  
   - **Exception**: No receptacle is required directly behind a counter-mounted cooking unit (see Figure 210.52(C)(1)).  

4. **Overcurrent Protection**  
   - Follow **Section 422.11** for overcurrent protection, ensuring branch-circuit protection matches the cooktop’s rated current.  

5. **Load Calculations**  
   - For service/feeder calculations, use **Table 220.55** for household cooking appliances.  

---

### Exceptions:
- **Alternative Installation Methods**:  
  If an electric cooktop uses an installation method not covered by CEC 422.3, it may still be permitted **with special permission** under **Section 422.23**.  

---

### Key CEC Sections:
- **CEC 422.3**: Mandates dedicated circuits for electric cooktops in residential buildings.  
- **CEC 422.23**: Allows alternative installation methods with special permission.  
- **CEC 210.52(C)**: Receptacle placement requirements for countertops/work surfaces.  
- **CEC 422.11**: Overcurrent protection for appliances.  

---

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 422.11, 422.23, 210.52, 220.55, 150.0, 160.9, 422.3

**Response Time:** 11.1s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

In California new construction, panelboards must include **dedicated circuit breaker spaces** for electric clothes dryers as mandated by **CEC 408.2** and the California Energy Code:

### Key Requirements:
1. **Single-Family Buildings**  
   - Panelboards must reserve **circuit breaker spaces** for:  
     - Heat pump water heaters  
     - Heat pump space heaters  
     - Electric cooktops  
     - **Electric clothes dryers**  
   - Per **CEC 408.2(A)**, this aligns with **California Energy Code Section 150.0(n), (t), (u), and (v)**.

2. **Multifamily Buildings**  
   - Panelboards serving individual dwelling units must reserve spaces for:  
     - Heat pump space heaters  
     - Electric cooktops  
     - **Electric clothes dryers**  
   - Per **CEC 408.2(B)**, this aligns with **California Energy Code Section 160.9(a), (b), and (c)**.

3. **Purpose**  
   - Ensures future-ready infrastructure for electrification and energy-efficient appliances.  
   - Prevents retrofit challenges by reserving spaces during initial construction.

4. **California-Specific Mandate**  
   - These requirements are **beyond standard NEC** and are part of California’s Title 24 Energy Code to support decarbonization goals.

### Exceptions Checked:
- **No exceptions** apply to **CEC 408.2** for electric clothes dryer circuits.  
- Cross-references to **Section 220.54** (load calculations) and **Section 210.52(F)** (laundry receptacles) are unrelated to panelboard space requirements.

✓ Source: CEC 2022 Sections 408.2, California Energy Code 150.0/160.9

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 210.52, 220.54, 160.9, 150.0, 408.2

**Response Time:** 9.5s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) Unique California Provisions (Final Answer)  

**Unique California Aspect:**  
CEC Table 240.4(G) includes a **delta (Δ) symbol** in its description, indicating **California amendments** to the referenced NEC sections. This notation is unique to California's code and signals localized modifications to overcurrent protection requirements for specific conductors.  

**Key Findings:**  
1. **Delta Symbol Significance:**  
   - The Δ symbol in **Section 240.4(G)** explicitly marks California amendments to the referenced NEC articles/sections (e.g., 440, 460, 725).  
   - These amendments may impose stricter or modified overcurrent protection rules for specialized conductors (e.g., fire alarm systems, motor circuits).  

2. **No Direct Exceptions Found:**  
   - The `cec_exception_search` for **240.4(G)** returned exceptions related to service conductors, busways, and wiring methods, but **no exceptions directly addressing Table 240.4(G)** itself.  
   - This confirms the table’s delta notation refers to broader California amendments in other sections, not exceptions to the table.  

3. **Cross-Reference Implications:**  
   - Conductors listed in the table (e.g., *fire alarm systems*, *electric welders*) must comply with **California-amended versions** of the referenced NEC articles (e.g., NEC 760 for fire alarms).  
   - Example: California may require additional overcurrent protection for fire alarm circuits in high-rise buildings beyond NEC 760.  

**Final Answer:**  
CEC Table 240.4(G) is unique to California due to the **delta (Δ) symbol**, which indicates localized amendments to the referenced NEC sections. These amendments modify overcurrent protection requirements for specialized conductors but **no direct exceptions** to the table itself were found. Users must consult the full CEC text for specific California modifications to the referenced articles.  

✓ Source: CEC 2022 Table 240.4(G) with delta amendment notation

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 240.4

**Response Time:** 14.5s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 242.3 Specifications (CEC 2022) – Final Answer

**Purpose**: CEC Table 242.3 is a **California-specific cross-reference table** (marked with "N") that directs users to other NEC articles containing **overvoltage protection requirements** for specific equipment types. It is not part of the base NEC.

---

### **Key Equipment-to-Article Mappings**:
- **Class I locations** → Article 501  
- **Class II locations** → Article 502  
- **Community antenna TV/radio systems** → Article 820  
- **Critical operations power systems** → Article 708  
- **Elevators/escalators** → Article 620  
- **Emergency systems** → Article 700  
- **Equipment >1000V** → Article 490  
- **Fire pumps** → Article 695  
- **Industrial machinery** → Article 670  
- **IT equipment** → Article 645  
- **Modular data centers** → Article 646  
- **Outdoor overhead >1000V** → Article 399  
- **Radio/TV equipment** → Article 810  
- **Receptacles/cord connectors** → Article 406  
- **Wind electric systems** → Article 694  

---

### **California-Specific Amendments**  
1. **Table 242.3 Note**: Marked with "N" to indicate it is a **California amendment** to NEC 2023.  
2. **Section 242.6 (Uses Not Permitted)**:  
   - SPD devices **shall not be installed**:  
     - On circuits over 1000 volts.  
     - On ungrounded/impedance-grounded systems unless listed for such use.  
     - If SPD rating is less than the maximum continuous phase-to-ground voltage.  

---

### **Relevant Exceptions**  
- **Section 370.23 Exception**:  
  > Cablebus overcurrent protection may follow **240.100 and 240.101** instead of 240.4.  
  *(Note: Applies to overcurrent, not overvoltage, but highlights California’s broader amendments.)*

---

**Source**:  
- CEC 2022 Table 242.3  
- CEC 2022 Section 242.6 (uses not permitted)  
- CEC 2022 Section 370.23 (exception)  

✓ **Compliance Note**: Use Table 242.3 to identify applicable overvoltage articles, and cross-check with California-specific exceptions like 370.23 and...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 240.4, 240.100, 242.3, 240.101, 370.23, 242.6

**Response Time:** 14.8s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)  
**With Exceptions and Cross-References**

### **Standard Requirements**  
- **Table Structure**:  
  - **Column A**: Maximum ratings for **separate overcurrent protection** (instantaneous trip devices).  
  - **Columns B/C**: Maximum ratings when using the **motor branch-circuit protective device**:  
    - **Column B**: Conductors **within the motor control equipment enclosure**.  
    - **Column C**: Conductors **extending beyond** the enclosure.  

- **Derating for Larger Conductors**:  
  - For conductors **larger than 10 AWG**:  
    - Column A: 400% of Table 310.17 (60°C conductors).  
    - Columns B/C: 300% of Table 310.16 (60°C conductors).  

---

### **Critical Exceptions**  
1. **Hazardous Control Circuits** (Exception No. 1):  
   - **Applies to**: Circuits where opening creates a hazard (e.g., fire pump motors).  
   - **Allowance**: Requires only **short-circuit and ground-fault protection**.  
   - **Source**: CEC 2022 Section 430.72(B).  

2. **Transformer-Supplied Circuits** (Exception No. 2):  
   - **Applies to**: Single-phase transformers with **two-wire secondary**.  
   - **Allowance**: Primary-side overcurrent protection is permitted if:  
     - Protection value ≤ (Table 430.72(B) rating × secondary-to-primary voltage ratio).  
   - **Restriction**: Not allowed for non-two-wire secondaries.  
   - **Source**: CEC 2022 Section 430.72(B).  

3. **Control Circuit Transformers** (Section 430.72(C)):  
   - **<50 VA Transformers**: Protected by primary devices, impedance limiting, or inherent means.  
   - **Primary <2A Transformers**: Overcurrent device ≤ 500% of primary current.  
   - **Source**: CEC 2022 Section 430.72(C).  

---

### **Cross-References and Limiting Rules**  
- **Ampacity Derating**:  
  - Columns B/C use **Table 310.16** (60°C column) for derating.  
  - Column A uses **Table 310.17** (60°C column).  
  - **Source**: Notes in Table 430.72(B). ...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.17, 310.16, 430.72

**Response Time:** 20.0s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in CEC 2022 (Not in NEC)

California's CEC 2022 includes **18 medium voltage (MV) cable ampacity tables** not found in the NEC. These are:

- **Tables 311.60(C)(67) through 311.60(C)(86)**  
  - Cover Type MV cables rated **2001–35,000 volts**
  - Provide ampacities for:
    - Multiconductor cables in cable trays (311.60(C)(75–76))
    - Single-conductor cables in various configurations (311.60(C)(69–70))
    - Triplexed/quadruplexed cables (311.60(C)(67–68))
    - Cables in ventilated vs. covered trays (311.60(C)(71–72))

### Key Exceptions and Notes:
1. **Engineering Supervision**: Ampacities can be determined by tables or under engineering supervision (311.60(A)(1)).
2. **Ambient Temperature Adjustments**: Corrections required per Table 311.60(D)(4) for temps ≠ 40°C.
3. **Shield Grounding**: Cables with shields grounded at multiple points require derating (311.60(D)(1)).
4. **Burial Depth**: Derating factors apply for depths >300mm (311.60(D)(2)(b)).

### Key Differences from NEC:
1. **Voltage Range**: CEC tables cover **2001–35,000V** (NEC stops at 2000V)
2. **Installation Conditions**: Include specific derating factors for:
   - Cable tray coverage (solid vs. ventilated)
   - Conductor spacing (minimum 1x cable diameter)
   - Triplex/quadruplex configurations
3. **California-Specific**: These tables are added in CEC Article 311 and 392, with no direct NEC equivalents

✓ Source: CEC 2022 Sections 311.60 and 392.80

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 311.60, 392.80

**Response Time:** 10.7s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Ampacity of 4/0 AWG Copper Conductor (CEC 2022) – Final Answer

**Ampacity**: **230 amperes** at 75°C  
**Source**: CEC 2022 Table 310.16 [California Amendment]  

---

### Exceptions and Limiting Rules:
1. **Exceptions Found**:  
   - **CEC 440.6** applies only to **hermetic refrigerant motor-compressors** and **multimotor equipment**. These exceptions modify how ampacity is determined for specific HVAC/refrigeration equipment but **do not override the base 230A value** for general conductors.  
   - **Not applicable** to standard 4/0 AWG copper conductors unless used in the specialized equipment described in 440.6.  

2. **Limiting Rule**:  
   - **CEC 240.4(D)**: Overcurrent protection for 4/0 AWG copper is limited to **250A**, even though the ampacity is 230A.  

---

### Key Considerations:
- **Ambient Temperature**: Use **CEC 310.15(B)** for corrections if ambient ≠ 30°C.  
- **Bundling**: Apply **CEC 310.15(C)(1)** derating if >3 conductors are bundled.  
- **California Amendments**: No direct amendments to Table 310.16 for this conductor size.  

---

### Final Answer:
The ampacity of **4/0 AWG copper** at 75°C is **230A** per CEC Table 310.16. Overcurrent protection is limited to **250A** per CEC 240.4(D). Exceptions in CEC 440.6 apply only to refrigeration/motor equipment and do not affect this general-case calculation.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.15, 240.4, 310.16, 440.6

**Response Time:** 9.4s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size (CEC 2022) with Exceptions

For a **200A circuit** in California:
- **Copper EGC**: 6 AWG (CEC Table 250.122)
- **Aluminum/Copper-Clad Aluminum EGC**: 4 AWG (CEC Table 250.122)

### Exceptions Found:
1. **410.44** - Applies to replacement luminaires/receptacles under specific conditions (not general 200A circuits).
2. **352.60/356.60** - Permits alternate grounding methods in conduit systems (requires separate EGC installation).
3. **250.121** - Prohibits using EGC as grounding electrode conductor (except under 250.6(A)).
4. **250.134** - Allows separate routing of EGC for fixed equipment (installation method, not sizing).

### Key Notes:
- Exceptions apply to **specific equipment types** (luminaires, fixed equipment) or **installation methods**, not general circuit sizing.
- For standard 200A circuits, **Table 250.122 remains the primary rule**.
- California amendments ([delta] symbols) may modify NEC requirements – verify local interpretations.

✓ Source: CEC 2022 Table 250.122 with exceptions from Sections 250.121, 250.134, 352.60, 356.60, 410.44

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 250.122, 250.134, 250.6, 250.121, 356.60, 352.60, 410.44

**Response Time:** 7.5s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022)

For a **3/0 AWG copper service conductor** in California:
- **Required GEC size**: **4 AWG copper**
- **Reference**: CEC 2022 Table 250.66  
- **California Amendment**: This table includes California-specific modifications from NEC ([CEC 250.66](https://www.ca.gov/code/250.66))

### Exceptions Checked:
1. **250.66(A)**: Allows 6 AWG copper for rod/pipe electrodes if not extending to other electrodes requiring larger conductors.  
2. **250.66(B)**: Allows 4 AWG copper for concrete-encased electrodes under similar conditions.  
3. **250.66(C)**: Ground ring connections permit GEC size equal to the ground ring conductor.  

Since the question does not specify a specific electrode type (e.g., concrete-encased, rod, or ground ring), the **general requirement from Table 250.66 applies**, mandating **4 AWG copper** for a 3/0 AWG service conductor. No applicable exceptions reduce this requirement without additional context.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 7.2s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)  

The temperature correction factor for a **75°C rated conductor** in a **40°C ambient temperature** is **0.88** per **CEC Table 310.15(B)(1)(1)**.  

### Exception Review:  
After searching for exceptions to **CEC 310.15(B)(1)(1)**, no relevant exceptions apply to this specific temperature correction scenario. The returned exceptions (e.g., Sections 352.60, 356.60) pertain to grounding conductor requirements and do not modify the temperature correction factor for ampacity adjustments.  

**Final Answer:**  
✓ **Correction Factor:** 0.88 (no exceptions apply)  
✓ **Source:** CEC 2022 Table 310.15(B)(1)(1)

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 356.60, 352.60

**Response Time:** 7.0s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor for Bundling (CEC 2022)

The ampacity adjustment factor for **7-9 current-carrying conductors** in a raceway is **0.70 (70%)** per **CEC Table 310.15(C)(1)** [California Amendment].

### Exceptions Review:
1. **Section 334.80** - Applies specifically to NM/NMC cables in thermal insulation or cable trays. Does not override general bundling rules.
2. **Section 310.15** - Confirms Table 310.15(C)(1) applies unless specific exceptions apply (e.g., raceways ≤ 24" long, certain cable types).
3. **Grounding exceptions (355.60, 352.60, 356.60)** - Relate to equipment grounding requirements, not ampacity adjustments.

**No exceptions override the 0.70 factor** for standard raceway installations with 7-9 conductors. The general rule in Table 310.15(C)(1) remains valid.

**Key Note from Table Footnotes:**
- This count includes **all conductors** (spare, neutral, grounding/bonding) **except** those connected to components that cannot be simultaneously energized.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 334.80, 355.60, 310.15, 356.60, 352.60

**Response Time:** 8.0s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth for 480V Panelboard (CEC 2022)

**Minimum depth required:**  
**1.2 meters (4 feet)** per **CEC Table 110.26(A)(1)** for 480V under **Condition 3** (exposed live parts on both sides of the working space).

**Exception Review:**  
After searching for exceptions to **CEC 110.26(A)(1)** with context "Condition 3," no applicable exceptions were found that would modify the 1.2 m (4 ft) requirement. The returned exceptions relate to:
- Dedicated electrical space (110.26(E))
- Grounding requirements (352.60, 356.60)
- Disconnecting means location (440.14)

None of these exceptions override or modify the working space depth for Condition 3 in Table 110.26(A)(1).

**Citation:**  
CEC 2022 Table 110.26(A)(1) with no applicable exceptions for this specific condition.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 440.14, 356.60, 352.60, 110.26

**Response Time:** 8.5s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Suitable Enclosures for Outdoor Use (CEC 2022)  

For outdoor use with **rain, sleet, and ice**, Table 110.28 specifies the following suitable enclosure types:  

- **Type 3S** (Rain, sleet, and ice protection)  
- **Type 3SX** (Rain, sleet, ice, and corrosion resistance)  
- **Type 4** (Water and ice protection)  
- **Type 4X** (Water, ice, and corrosion resistance)  
- **Type 6** (Water and ice protection)  
- **Type 6P** (Water, ice, and corrosion resistance)  

### Key Exceptions and Notes:  
1. **Receptacles in Wet/Damp Locations** (CEC 406.9):  
   - Outdoor receptacles in wet locations must use **weatherproof enclosures** (e.g., Type 4 or 4X).  
   - **Exception**: Receptacles subject to high-pressure spray washing may use weatherproof enclosures when the plug is removed.  

2. **Mechanism Operability**: Enclosures must remain operable when ice-covered (per Table 110.28 notes).  

3. **Corrosion Resistance**: Use **Type 3X, 4X, 6P, or 3SX** in corrosive environments.  

4. **Sleet Protection**: **Type 3S** and **3SX** are explicitly rated for sleet.  

### Code References:  
- **CEC Table 110.28** (primary rule)  
- **CEC 406.9** (receptacle-specific exceptions)  
- **CEC 110.11** (protection against environmental deterioration)  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.28, 110.11, 406.9

**Response Time:** 13.5s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)

According to **CEC Table 220.12**, the general lighting load for **office buildings** is:

- **11 volt-amperes per square meter (VA/m²)**  
- **1 volt-ampere per square foot (VA/ft²)**  

This value is explicitly stated in **CEC 2022 Section 220.14(K)** for office building receptacle loads, where it specifies the larger of two options, one of which is this 11 VA/m² (1 VA/ft²) value.

### Exceptions and Notes:
1. **Energy Code Compliance** (Section 220.12(B)):  
   If the building complies with a local energy code, alternative lighting load values from the energy code may be used **if**:
   - A power monitoring system is installed.
   - Demand factors from Table 220.42 are **not applied** to the general lighting load.
   - The 125% continuous load multiplier is applied.

2. **Table Cross-Reference**:  
   The value is derived from **Table 220.12**, which categorizes "banks" as office-type occupancies (footnote "d") but does not alter the base 1 VA/ft² requirement for standard office buildings.

No direct exceptions override the 1 VA/ft² base value for typical office buildings. The energy code exception provides an **alternative method**, not a modification of the base requirement.

✓ Source: CEC 2022 Section 220.12, Table 220.12

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 220.14, 220.12, 220.42

**Response Time:** 8.7s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## 12 AWG Flexible Cord Ampacity (CEC 2022)

The ampacity of a **12 AWG flexible cord** in **Column B (thermoset)** is **25 amperes** per CEC 2022 Table 400.5(A)(1). 

**Key Verification:**
- **Table 400.5(A)(1)** explicitly lists 25A for 12 AWG flexible cord in Column B (thermoset) at 30°C ambient temperature.
- **No applicable exceptions** modify this value for standard installations (CEC 400.12 restrictions apply to permitted uses but do not affect ampacity).
- **Overcurrent protection** for flexible cords is governed by **240.5(A)**, which permits protection based on the cord's ampacity (25A in this case).

**Final Answer:**  
✓ **25 amperes** (CEC Table 400.5(A)(1))  

✓ Source: CEC 2022 Table 400.5(A)(1)

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 400.12, 400.5, 240.5

**Response Time:** 13.1s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

**Final Answer with Exceptions Considered:**  
The maximum operating temperature for **Type SF-2 silicone insulated fixture wire** is **200°C (392°F)**, as specified in **CEC 2022 Section 620.11(A)(1)** for hoistway door interlock wiring applications. 

### Key Findings:
1. **Primary Rule (Section 620.11):**  
   - Type SF (including SF-2) conductors must be suitable for **not less than 200°C** in hoistway applications.  
   - No exceptions in the returned results override or limit this temperature requirement for Type SF-2 in this context.

2. **Exceptions Review:**  
   - **Section 620.42** (hazardous locations) and **Section 600.32** (neon circuits) apply to specialized installations and do not affect general hoistway or fixture wire applications.  
   - **Section 410.115** (luminaire temperatures) is unrelated to conductor insulation ratings.  

3. **Conclusion:**  
   - The 200°C rating in **Section 620.11(A)(1)** remains valid with no applicable exceptions reducing this temperature limit for Type SF-2 in hoistway or similar applications.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 410.115, 620.11, 620.42, 600.32

**Response Time:** 15.2s

---


## Complex Calculations

### cec-021: adjusted_ampacity

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 x 0.88 x 0.70 = 30.8A

**CEC Ref:** CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1) | **NEC Ref:** NEC Tables 310.16, 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Final Adjusted Ampacity Calculation (CEC 2022)

**Base Ampacity**:  
8 AWG THWN copper = **50A** (CEC Table 310.16, 75°C column)  

**Temperature Correction (40°C ambient)**:  
Factor = **0.88** (CEC Table 310.15(B)(1)(1))  

**Bundling Adjustment (7 conductors)**:  
Factor = **0.70** (CEC Table 310.15(C)(1))  

**Exceptions Review**:  
- No applicable exceptions found for general ampacity adjustments in this scenario.  
- Exceptions in **440.6** (hermetic motor-compressors) and **311.60** (MV cables) do not apply here.  
- **310.15** confirms standard correction factors apply unless specific equipment conditions exist.  

**Final Calculation**:  
$$
50A \times 0.88 \times 0.70 = 30.8A
$$

**Adjusted Ampacity**: **30.8 amperes**  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.15, 310.16, 311.60, 440.6

**Response Time:** 11.1s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Exception Review (CEC 2022)

**1. Primary Exception for Table 310.12(A):**  
- **Section 310.12(A)** explicitly permits using Table 310.12 for single-phase dwelling services **without adjustment/correction factors**.  
- The note states conductors must have an ampacity of **at least 83% of the service rating** (200A × 0.83 = 166A).  
- **2/0 AWG copper** (175A at 75°C per Table 310.12) satisfies this requirement.  

**2. Overload Protection Exception (Section 230.90):**  
- Allows overcurrent devices to exceed conductor ampacity **if calculated load ≤ conductor ampacity**.  
- **Not applicable here** since the service is sized directly per Table 310.12.  

**3. Splicing Exception (Section 230.33):**  
- Permits splicing service conductors under specific conditions.  
- **Not relevant to this question**.  

**Conclusion**: No exceptions override the 2/0 AWG copper service conductor, 6 AWG EGC, or 4 AWG GEC sizing.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 230.90, 230.33, 310.12

**Response Time:** 15.3s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The 125% continuous load multiplier is already included in this table value.

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Building (CEC 2022)

**Final Calculation:**  
For a **5,000 sq ft office building**:  
Unit load from **CEC Table 220.12** for "Office" = **1.3 VA/ft²**  
Total lighting load = 5,000 ft² × 1.3 VA/ft² = **6,500 volt-amperes**

**Key Notes:**  
- The 125% continuous load multiplier (per 210.20(A)) is **already included** in the Table 220.12 values.  
- **No applicable exceptions** modify the 1.3 VA/ft² value for standard office calculations.  
- Exception 220.12(B) (energy code alternative) requires specific monitoring systems not mentioned in the question.  

✓ Source: CEC 2022 Table 220.12

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 210.20

**Response Time:** 11.5s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for Motor Control Circuit (CEC 2022)

For **16 AWG copper conductors** in a motor control circuit **extending beyond the enclosure**, the maximum overcurrent protection is:

**10 amperes**  
(Per CEC Table 430.72(B), Column C for conductors extending beyond the enclosure)

---

### Key Code References:
1. **CEC 430.72(B)(2):**  
   - *Column C applies when conductors extend beyond the motor control equipment enclosure.*  
   - Maximum rating for 16 AWG copper = **10A**.

2. **Exceptions Checked:**  
   - **Exception No. 1** (CEC 430.72): Allows using the motor branch-circuit protective device if the control circuit's opening creates a hazard (e.g., fire pump).  
     → **Does not apply** here, as no hazard scenario was specified.  
   - Other exceptions relate to transformer secondary conductors or grounding, which are **not applicable** to this question.

---

### Final Answer:
- **Maximum OCP:** 10A (per Table 430.72(B), Column C).  
- **No applicable exceptions** for this configuration.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 430.72

**Response Time:** 11.9s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Dwelling Unit (CEC 2022)

The general lighting load for a **2,400 sq ft dwelling unit** is calculated per **CEC 2022 Section 220.14(J)**:

**Calculation:**
```
2,400 sq ft × 3 VA/sq ft = 7,200 VA
```

**Key Requirements:**
- Minimum unit load: **3 VA per square foot** (CEC 220.14(J))
- Includes all general-use receptacles, lighting, and small appliance circuits
- **No exceptions apply** for standard dwelling units under this calculation method
- No additional demand factors required for dwelling units using this method

✓ Source: CEC 2022 Section 220.14(J)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 220.14

**Response Time:** 8.6s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## **Final Comparison of Kitchen GFCI Requirements**  
### **CEC 2022 vs. NEC 2023**  

---

### **1. Scope of GFCI Protection**  
- **CEC 2022 (Section 210.8(A)(6))**:  
  - **Applies only to receptacles serving countertop surfaces** in kitchens.  
  - **Exceptions**:  
    - Receptacles for ceiling luminaires/ceiling fans (if not general-purpose convenience receptacles).  
    - Receptacles not readily accessible (e.g., dedicated circuits for specific appliances).  

- **NEC 2023 (Section 210.8(A)(5))**:  
  - **Applies to all 125–250V receptacles in kitchens**, including:  
    - Countertops.  
    - Areas with sinks and permanent food preparation/provisioning.  
  - **Exceptions**:  
    - HVAC equipment (expiring September 1, 2026).  
    - Receptacles for security systems or specific ceiling-mounted devices.  

---

### **2. Key Differences**  
| **Aspect**               | **CEC 2022**                          | **NEC 2023**                          |  
|---------------------------|----------------------------------------|----------------------------------------|  
| **Coverage**              | Countertop receptacles only.           | All kitchen receptacles (countertops, sinks, food prep areas). |  
| **Future Restrictions**   | No expiring exceptions.                | HVAC exception expires 2026, tightening requirements. |  
| **Exceptions**            | Focus on accessibility/dedicated circuits. | Includes HVAC (temporarily), security systems, and ceiling devices. |  

---

### **3. Which Code is More Restrictive?**  
- **NEC 2023 is more restrictive** because:  
  1. **Broader Scope**: Covers **all kitchen receptacles**, not just countertops.  
  2. **Future-Proofing**: The HVAC exception expires in 2026, eliminating a key exception.  
  3. **Additional Locations**: Includes sinks and food preparation areas explicitly.  

- **CEC 2022** remains narrower but aligns with California’s residential focus, prioritizing countertop safety.  

---

### **4. Excepti...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.8

**Response Time:** 13.5s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification. No...

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023)  
**Updated with Exception Analysis**

### **CEC 2022 Requirements**  
**Section 408.2(A)** mandates **reserved circuit breaker spaces** in single-family dwellings for:  
- Heat pump water heaters  
- Heat pump space heaters  
- Electric cooktops  
- Electric clothes dryers  

**Exception Check Results:**  
- No exceptions apply to **408.2(A)** for single-family dwellings.  
- Cross-referenced sections (424.10, 426.14, 440.8) relate to special permissions for heating/deicing systems, not panelboard space requirements.  

**Key Differences from NEC:**  
- NEC 2023 **does not include** mandatory reserved spaces for these appliances.  
- NEC allows flexibility for installers to size panelboards based on calculated load (NEC 220.84), without prescriptive space requirements.  

### **NEC 2023 Requirements**  
- **No specific reserved spaces** for appliances in single-family panelboards.  
- Panelboard sizing depends on **calculated load** (NEC 220.84) and **minimum busbar ratings** (NEC 230.79).  
- NEC 408.3–408.5 covers general panelboard construction, clearances, and conductor support but does not address appliance-specific spaces.  

### **California-Specific Amendments**  
The CEC adds **prescriptive requirements** beyond NEC to align with California’s energy efficiency goals. These amendments ensure:  
- Future-proofing for electrification (e.g., heat pumps).  
- Compliance with **Title 24 Part 6** (residential energy efficiency standards).  

### **Summary**  
| **Requirement**               | **CEC 2022**                          | **NEC 2023**                  |  
|-------------------------------|----------------------------------------|-------------------------------|  
| Reserved spaces for appliances | **Mandatory** (408.2(A))              | **Not required**              |  
| Panelboard sizing basis       | Prescriptive + calculated load         | Calculated load only (220.84) |  
| Energy co...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 424.10, 440.8, 230.79, 408.5, 220.84, 426.14, 408.3, 408.2

**Response Time:** 13.2s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## California vs NEC EV Charging Requirements (CEC 2022 vs NEC 2023)  

### Key Exceptions Check  
After searching for exceptions to **CEC 625.40** (dedicated branch circuits for EV outlets), **no applicable exceptions** were found. The only returned exception (675.10) relates to irrigation motors and is unrelated to EV charging systems.  

---

### Final Comparison Summary  

| **Feature**               | **California (CEC 2022)**                                                                 | **NEC 2023**                                                                 |  
|---------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|  
| **Scope**                 | Includes **power export/bidirectional charging**; mandates CALGreen compliance for new construction | Focuses on **conductive charging only**                                      |  
| **Branch Circuits**       | **Individual circuit per EV outlet** (625.40) – **no exceptions** found                | Permits multi-outlet circuits if rated (210.21(B)(3))                        |  
| **GFCI Protection**       | **All EV receptacles** require GFCI (625.54) – **no exceptions**                       | GFCI required only for **garages/outdoors** (210.8(A)(6))                    |  
| **Ventilation**           | **Mandatory** for indoor EVSE (625.52) with specific airflow tables                    | **No requirements**                                                         |  
| **Cord Lengths**          | Max 25 ft (7.5 m) unless using cable management system (625.17)                         | No specific EVSE cord length limits (400.5)                                 |  
| **CALGreen Mandates**     | New residential/commercial buildings must have **EV-ready infrastructure**             | **No equivalent requirements**                                                |  

...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 8 found
- 625.54, 675.10, 625.40, 400.5, 625.52, 210.21, 625.17, 210.8

**Response Time:** 17.9s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements: CEC 2022 vs NEC 2023 for Dwelling Units

### **1. Scope of Protection**
- **CEC 2022 (210.12(A))**  
  - **Expanded coverage**: Includes **hallways, closets, laundry areas**, and **all 15/20A 120V circuits** in kitchens, bedrooms, etc.  
  - **Exception**: Fire alarm systems in metal raceway are exempt.  
- **NEC 2023 (210.12(A))**  
  - Covers **kitchens, bedrooms, family rooms**, etc., but **no explicit mention** of hallways, closets, or laundry areas.  

---

### **2. Protection Methods**
| **Method** | **CEC 2022** | **NEC 2023** |
|------------|--------------|--------------|
| **Supplemental arc protection** | Permitted with **50/70 ft wiring limits** (14/12 AWG). | **Not permitted** as a listed method. |
| **Outlet branch-circuit AFCI** | Allowed with **wiring continuity** and first-outlet marking. | Permitted but **no wiring length limits**. |
| **Metal raceway exception** | Permits outlet AFCIs in **metal raceway or concrete-encased wiring**. | **No equivalent exception**. |

---

### **3. Installation Requirements**
- **CEC 2022**  
  - **First outlet marking**: Required for non-combination AFCI installations.  
  - **Wiring continuity**: Must be continuous from overcurrent device to AFCI.  
- **NEC 2023**  
  - **No first-outlet marking** requirement.  
  - **No wiring continuity** requirement for outlet AFCIs.  

---

### **4. Exceptions**
- **CEC 2022**  
  - **Short extensions**: AFCI not required for **≤6 ft** extensions without additional outlets (210.12(D) Exception).  
  - **Fire alarm systems**: Exempt if installed per 760.41(B)/760.121(B) in metal raceway.  
- **NEC 2023**  
  - **Fire alarm systems**: Exempt if installed per 760.41(B)/760.121(B) but **no raceway requirement**.  
  - **No exception** for short circuit extensions.  

---

### **5. Receptacle Replacement Rules**
- **CEC 2022**  
  - **No specific requirements** for replacements.  
- **NEC 2023 (406.4(D)(4))**  
  - Replaced receptacles in AFCI-protec...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 210.12, 760.41, 760.121, 406.4

**Response Time:** 16.1s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements vs NEC 2023 Article 690 (CEC 2022) – Finalized

### Key Differences and California Amendments

1. **AC Module Treatment (CEC 690.6)**
   - **CEC**: AC modules are exempt from PV source circuit rules (690.6(A)). Their internal components (conductors, inverters) are treated as part of the module system.
   - **NEC 2023**: Similar exemption exists but lacks California's explicit clarification on internal component classification.
   - **Exception**: No additional exceptions found beyond 690.6(A). The exemption applies only to factory-assembled AC modules.

2. **Rapid Shutdown Labeling (CEC 690.56(C))**
   - **CEC**: Mandates:
     - 9.5mm capital letters on yellow background for main labels.
     - Reflective red/white labels on shutdown switches.
     - Diagrams showing energized areas post-shutdown.
   - **NEC 2023**: General labeling without dimensional/color requirements.
   - **Amendment**: CEC adds safety visibility standards.

3. **System Identification (CEC 690.56)**
   - **CEC**: Requires "SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN" labels at service equipment.
   - **NEC 2023**: No equivalent requirement.
   - **Amendment**: CEC adds location-specific labeling for emergency responders.

4. **Engineered Design Documentation (CEC 691.6)**
   - **CEC**: Large-scale systems require stamped engineering reports proving compliance with Article 690.
   - **NEC 2023**: No documentation requirement.
   - **Amendment**: CEC adds verification obligations for AHJ.

5. **Installation Restrictions (CEC 690.4(E))**
   - **CEC**: Prohibits PV equipment in bathrooms.
   - **NEC 2023**: No such restriction.
   - **Amendment**: CEC adds location-specific safety limits.

### Limiting Rules
- **CEC 690.4(B)**: All inverters/converters must be listed/evaluated – stricter than NEC's "listed" requirement.
- **CEC 690.4(C)**: Requires qualified personnel for installation.

### Exceptions Confirmed
- **690.6(A) Exception**: AC modules must be fa...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 690.4, 690.6, 691.6, 690.56

**Response Time:** 12.9s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 12.2s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

