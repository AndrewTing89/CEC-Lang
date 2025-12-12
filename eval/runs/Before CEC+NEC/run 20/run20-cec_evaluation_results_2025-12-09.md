# CEC Agent Evaluation - Run 20 (No Mandatory Exception Search)

**Date:** 2025-12-09
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**NEC Comparison:** ENABLED
**Prompt Version:** v3 - no mandatory exception search

## Key Changes in This Run

1. **Removed mandatory exception search enforcement** - Agent no longer forced to call exception search on every question
2. **Added missing tools to search_tools** - `cec_lookup_table`, `nec_lookup_table`, `cec_lookup_conductor_size`, `nec_lookup_conductor_size`
3. **Relying on footnote augmentation** - Table lookups automatically inject cross-references (e.g., 240.4(D))

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Successful** | 30 (100.0%) |
| **Failed** | 0 |
| **Exception Search Called (Voluntary)** | 1/30 |
| **Total Duration** | 346.8s |
| **Avg per Question** | 11.6s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2(A) requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) e...

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022)

### **California Requirements (CEC 2022 Section 408.2(A))**
- **Reserved Circuit Breaker Spaces**: Panelboards in single-family dwellings must reserve spaces for:
  1. **Heat pump water heaters**
  2. **Heat pump space heaters**
  3. **Electric cooktops**
  4. **Electric clothes dryers**
- **Code Reference**: California Energy Code Section 150.0(n), (t), (u), and (v).

### **NEC 2023 Comparison**
- **General Requirements**: NEC Article 408 covers panelboard installation but does **not mandate reserved spaces** for specific appliances. It focuses on:
  - Enclosure types (dead-front, listed enclosures).
  - Wiring space fill limits (≤ 40% for conductors, ≤ 75% for splices/taps).
  - Grounding and bonding requirements.
- **No Appliance-Specific Mandates**: NEC does not require reserved spaces for heat pumps, cooktops, or dryers. Panelboard sizing is based on load calculations (NEC 220.85 for dwelling units).

### **Key Differences**
| **Aspect**               | **CEC 2022 (California)**                          | **NEC 2023**                                  |
|--------------------------|--------------------------------------------------|---------------------------------------------|
| **Reserved Spaces**      | Required for 4 specific appliances               | No appliance-specific reserved spaces       |
| **Code Basis**           | California Energy Code (Title 24)                | General panelboard in...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 3 found

**Response Time:** 18.0s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in...

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements (CEC 2022) vs NEC 2023

### **California (CEC 2022) Requirements**
1. **CALGreen Mandates**  
   - **EV-Ready Infrastructure**: New residential construction must include:  
     - Dedicated 40-amp minimum circuits for EV charging.  
     - Conduit to parking spaces for future EV installations.  
     - Panelboard capacity to accommodate EV loads (CEC 408.2).  

2. **Branch Circuit Requirements**  
   - **Individual Circuits**: Each EV outlet must be supplied by an individual branch circuit with no other outlets (625.40).  
   - **GFCI Protection**: All EV charging receptacles require ground-fault circuit-interrupter (GFCI) protection (625.54).  

3. **Ventilation**  
   - Indoor EV charging requires mechanical ventilation if equipment is listed to need it (625.52). Ventilation must be interlocked with the charging circuit.  

4. **Cable Lengths**  
   - Power-supply cords for portable EVSE are limited to 15 ft (4.6 m) unless using a listed cable management system (625.17).  

5. **Personnel Protection**  
   - Listed personnel protection systems are required for equipment over 60 VDC (625.22).  

---

### **NEC 2023 Comparison**  
1. **Branch Circuits**  
   - NEC 625.12 allows shared circuits for EVSE with other loads if the EVSE is listed for such use, whereas CEC mandates individual circuits.  

2. **GFCI Protection**  
   - NEC 210.8(A)(7) requires GFCI for EV receptacles but does not explicitly mandate it for all EV charging circuit...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- Exception Search Called: Yes

**Citations:** 10 found

**Response Time:** 15.4s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requir...

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements (CEC 2022) vs NEC 2023

### **1. Rapid Shutdown Requirements**  
**CEC 690.12** adds stricter requirements than NEC:  
- **Voltage Limits**:  
  - **Outside array boundary**: ≤30V within 30 seconds  
  - **Inside array boundary**: ≤80V within 30 seconds  
- **Labeling**: Permanent labels at service equipment locations indicating rapid shutdown status (CEC 690.56(C)).  
- **Initiation Devices**: Must be located outside buildings for single-family homes.  

**NEC 2023**:  
- Requires rapid shutdown but lacks CEC's specific voltage thresholds and labeling mandates.  

---

### **2. System Grounding and Ground-Fault Protection**  
**CEC 690.41**:  
- Mandates ground-fault protection for DC circuits >30V/8A.  
- Allows **solidly grounded** or **functionally grounded** systems but requires labels for solidly grounded bipolar systems.  

**NEC 2023**:  
- Ground-fault protection required for DC circuits but does not specify California’s voltage/current thresholds.  

---

### **3. Wiring Methods**  
**CEC 690.31**:  
- **DC circuits >30V/8A** must use metal raceways, MC cable, or metal enclosures (except tracking arrays).  
- **Labeling**: "PHOTOVOLTAIC POWER SOURCE" labels with **white-on-red** markings (minimum 9.5mm height).  

**NEC 2023**:  
- Permits nonmetallic raceways for DC circuits but lacks CEC’s detailed labeling and material requirements.  

---

### **4. Identification and Labeling**  
**CEC 690.56**:  
- **Mandatory labels** at ser...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 5 found

**Response Time:** 10.8s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can sup...

**Status:** PASS

**Agent Answer:**
## Circuit Requirements for Heat Pump Water Heaters in California (CEC 2022)

### California Requirements:
1. **Dedicated Circuits** (CEC 422.3(A)):
   - Single-family dwellings: Must have **dedicated branch circuits** for heat pump water heaters as specified in **California Energy Code Section 150.0(n)**.
   - Panelboards must include **designated circuit breaker spaces** for heat pump water heaters (CEC 408.2(A)).

2. **Panelboard Readiness** (CEC 408.2(A)):
   - Single-family buildings require **reserved panelboard spaces** for heat pump water heaters, electric cooktops, and dryers to ensure future readiness.

3. **Energy Code Compliance**:
   - Specific sizing and installation details are governed by **California Energy Code Sections 150.0(n)** (single-family) and **160.9** (multifamily).

---

### NEC 2023 Comparison:
- **General Requirements**: NEC 422.13 covers storage water heaters (125% overcurrent protection) but does **not explicitly mandate dedicated circuits** for heat pump water heaters.
- **Panelboard Spaces**: NEC does not require reserved panelboard spaces for future heat pump installations.
- **Focus**: NEC focuses on overcurrent protection and general appliance circuits, while CEC adds **readiness provisions** for electrification (e.g., reserved spaces).

---

### Key Differences:
| **Aspect**               | **California (CEC 2022)**                          | **NEC 2023**                          |
|--------------------------|-----------------------------...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 5 found

**Response Time:** 7.7s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrif...

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness: CEC 2022 vs NEC 2023

### **California (CEC 2022) Requirements**
1. **Mandatory Pre-Wiring**:
   - **Single-Family**: Requires **dedicated circuits and circuit identifications** per **California Energy Code 150.0(u)** (Section 422.3(A)(2)).
   - **Multifamily**: Requires **dedicated circuits** per **California Energy Code 160.9(b)** (Section 422.3(B)(1)).
   - Includes **designated panel space** and **labeling** for future electric cooktops.

2. **Labeling**:
   - Circuit identifications must be **clearly marked** for easy installation (Section 422.3).

3. **Scope**:
   - Applies to **all new residential construction** (single-family and multifamily).

---

### **NEC 2023 Provisions**
1. **No Readiness Mandate**:
   - NEC does **not require pre-wiring** or dedicated circuits for future electric cooktops in new construction.
   - Focuses on **installation standards** for existing appliances (Section 422.10, 220.55).

2. **Branch Circuit Requirements**:
   - Requires circuits to match appliance ratings (e.g., 40–50A for cooktops) but does **not address future readiness**.

3. **Labeling**:
   - No specific labeling requirements for future appliances.

---

### **Key Differences**
| **Aspect**               | **CEC 2022 (California)**                          | **NEC 2023**                          |
|--------------------------|----------------------------------------------------|--------------------------------------|
| **Readiness Mandate**     |...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 5 found

**Response Time:** 12.0s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

### **California (CEC 2022) Requirements**
1. **Reserved Circuit Breaker Spaces**  
   - **Single-family buildings**: Panelboards must include reserved circuit breaker spaces for **electric clothes dryers** as specified in **California Energy Code Section 150.0** (CEC 408.2(A)).  
   - **Multifamily buildings**: Panelboards must include reserved spaces for **electric clothes dryers** per **California Energy Code Section 160.9** (CEC 408.2(B)).  
   - *Purpose*: Ensures future capacity for electrification upgrades (e.g., heat pump dryers).

2. **Load Calculations**  
   - Dryer load is calculated at **5,000 VA minimum** (CEC 220.54), same as NEC. Demand factors from Table 220.54 apply for multiple dryers.

---

### **National Electrical Code (NEC 2023) Requirements**
1. **No Reserved Panelboard Spaces**  
   - NEC does **not mandate reserved circuit breaker spaces** for dryers. Load calculations follow **NEC 220.54** (5,000 VA minimum), but panelboards are sized based on calculated load without requiring dedicated spaces for specific appliances.

2. **Load Calculations**  
   - Identical to CEC: Dryer load is **5,000 VA or nameplate rating**, whichever is larger. Demand factors apply for 3-phase systems.

---

### **Key Differences**
| **Aspect**                | **California (CEC)**                          | **NEC 2023**                     |
|---------------------------|------------------------------...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 4 found

**Response Time:** 8.6s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) Unique California Provisions (CEC 2022)

### **Key Differences from NEC 2023**
1. **Control/Instrumentation Circuits (Type ITC):**
   - **CEC:** References **Article 725** (Class 1, 2, 3 Circuits) with specific sections:  
     `725.43, 725.45, 725.121` + **Chapter 9 Tables 11(A) & 11(B)**  
   - **NEC:** References **Article 335** (Instrumentation Cables) with only:  
     `335.9`  
   - **Impact:** CEC mandates stricter compliance with power-limited circuit rules (725) vs. NEC's focus on cable type (335).

2. **Remote-Control/Signaling Conductors:**
   - **CEC:** Explicitly ties to **Article 725** (power-limited circuits) with:  
     `725.43, 725.45, 725.121` + Tables 11(A)/11(B)  
   - **NEC:** References **Article 724** (Class 2/3 circuits) with:  
     `724.43, 724.45` + Tables 11(A)/11(B)  
   - **Impact:** CEC enforces stricter classification under 725 (safety-critical circuits) vs. NEC's broader 724.

3. **Fire Alarm Conductors:**
   - Both codes reference **Article 760**, but CEC adds emphasis on:  
     `760.43 (installation), 760.45 (maintenance)`  
   - **NEC** lacks explicit cross-reference to these sections.

4. **California-Specific Cross-References:**
   - **CEC Sections 440.51 & 220.3** explicitly tie Table 240.4(G) to:  
     - Air-conditioning/refrigeration equipment (Article 440)  
     - Motor overload protection (Article 430)  
   - **NEC** lacks these direct ties to California amendments.

---

### **California-Only Additions**
- ...

**Tool Usage:**
- CEC Tools: None
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 12 found

**Response Time:** 6.9s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**Status:** PASS

**Agent Answer:**
## CEC Table 242.3 Specifications (CEC 2022)

**CEC Table 242.3** is a **California-specific cross-reference table** (marked with "N" for California amendment) that directs users to other NEC articles containing overvoltage protection requirements for specific equipment types. It applies to California installations and modifies NEC 2023 Table 242.3 in two key ways:

---

### **Key Differences Between CEC and NEC Tables**
| Equipment Type | **CEC 2022 Reference** | **NEC 2023 Reference** | **Difference** |
|----------------|------------------------|------------------------|----------------|
| Equipment over 1000V | Article 490 | Article 495 | CEC references Article 490 instead of 495 |
| Outdoor overhead conductors >1000V | Article 399 | Article 395 | CEC references Article 399 instead of 395 |

---

### **Full Table Entries (CEC 2022)**
- Class I locations → Article 501  
- Fire pumps → Article 695  
- Industrial machinery → Article 670  
- Wind electric systems → Article 694  
- **New California entry**: Equipment over 1000V → Article 490 [CEC-only amendment]

---

### **NEC 2023 Table 242.3 (For Comparison)**
- Equipment over 1000V → Article 495  
- Outdoor overhead conductors >1000V → Article 395  

---

### **California-Specific Notes**
1. **[CEC 242.3]**: Explicitly requires compliance with referenced articles for overvoltage protection in California installations.
2. The "N" marker indicates this table was **added/modified by California** to address local electrical nee...

**Tool Usage:**
- CEC Tools: cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 1 found

**Response Time:** 5.8s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, condu...

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) vs NEC 2023 Comparison

### **CEC 2022 Table 430.72(B) Specifications**
- **Purpose**: Specifies maximum overcurrent protective device ratings for motor control circuits based on conductor size and installation type.
- **Key Values**:
  - **18 AWG copper**: 7A (Column A), 25A (Column B), 7A (Column C)
  - **16 AWG copper**: 10A (Column A), 40A (Column B), 10A (Column C)
  - **14 AWG copper**: 100A (Column B), 45A (Column C)
  - **12 AWG copper/aluminum**: 120A/100A (Column B), 60A/45A (Column C)
  - **10 AWG copper/aluminum**: 160A/140A (Column B), 90A/75A (Column C)
  - **Larger than 10 AWG**: Notes reference multipliers (see below).

- **Notes**:
  1. For conductors **larger than 10 AWG**, use:
     - **Column A/B**: 400% of Table 310.19 (60°C conductors)
     - **Column C**: 300% of Table 310.16 (60°C conductors)
  2. Aluminum values are limited to specific sizes (e.g., 12 AWG and larger).

---

### **NEC 2023 Table 430.72(B)(2) Comparison**
- **Structure**: Identical to CEC Table 430.72(B), with the same conductor sizes and column ratings.
- **Key Differences**:
  - **Aluminum Conductors**: NEC explicitly labels "aluminum/copper-clad aluminum" instead of just "aluminum."
  - **Notes**: Same multipliers (400% for Column B, 300% for Column C) referencing NEC Tables 310.16 and 310.19.

---

### **Critical Observations**
1. **No Substantive Differences**: The tables are **identical in structure and values** between CEC 2022 and NEC 2023 for motor contro...

**Tool Usage:**
- CEC Tools: cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 3 found

**Response Time:** 8.5s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found i...

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables: CEC vs NEC Comparison

**California Electrical Code (CEC 2022):**
- **Unique Tables**: CEC includes **18 dedicated MV ampacity tables** (311.60(C)(67)–(86)) for Type MV cables (2001–35,000V) in specific configurations (e.g., triplexed cables in conduit, cable trays).
- **Detailed Configurations**: Provides ampacities for:
  - Triplexed/single-conductor copper cables in isolated conduit (Table 311.60(C)(67)).
  - Voltage ranges: 2001–5000V and 5001–35,000V.
  - Temperature ratings: 90°C and 105°C.
- **Ambient Conditions**: Tables assume 40°C ambient (air) or 20°C (地下), with correction factors for other temperatures.

**National Electrical Code (NEC 2023):**
- **General Guidance**: Article 311 covers MV cables but **no equivalent tables** for specific configurations like CEC’s 311.60(C).
- **Relies on IEEE Standards**: References IEEE 835 for ampacity calculations rather than codifying detailed tables.
- **Engineering Calculations**: Requires engineering supervision for MV ampacity determinations (311.60(A)(1)), unlike CEC’s tabulated values.

**Key Differences:**
1. **Tables**: CEC provides **detailed, prescriptive tables** for MV ampacities; NEC offers **general methods** without California-specific configurations.
2. **Temperature Ratings**: CEC includes 105°C ratings (higher than NEC’s typical 90°C for MV).
3. **Installation Scenarios**: CEC tables address specific installations (e.g., isolated conduit, cable trays), while NEC relies on broad...

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 1 found

**Response Time:** 18.1s

---


## CEC Delta Tables

### cec-011: conductor_ampacity [CA-SPECIFIC]

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**Status:** PASS

**Agent Answer:**
## Ampacity of 4/0 AWG Copper Conductor at 75°C (CEC 2022)

**California Electrical Code (CEC 2022):**  
- **Ampacity:** 230 amperes  
- **Reference:** CEC Table 310.16 (same as NEC 2023 Table 310.16)  

**NEC 2023 Comparison:**  
- **Ampacity:** 230 amperes (identical to CEC)  
- **Reference:** NEC Table 310.16  

**Key Notes:**  
1. No California amendments affect this specific ampacity value.  
2. Both codes use the same table data for 4/0 AWG copper at 75°C.  
3. Footnotes reference correction factors (e.g., 310.15(B) for temperature, 240.4(D) for overcurrent limits), but no adjustments are required for standard conditions.  

✓ Source: CEC 2022 / NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 3 found

**Response Time:** 20.4s

---

### cec-012: grounding [CA-SPECIFIC]

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size for 200A Circuit (CEC 2022)

**California (CEC 2022):**  
- **Copper**: 6 AWG  
- **Aluminum**: 4 AWG  
- **Reference**: CEC Table 250.122 (with California amendment note)  

**NEC 2023 Comparison:**  
- **Copper**: 6 AWG  
- **Aluminum**: 4 AWG  
- **Reference**: NEC Table 250.122  

**Key Differences:**  
- **Table Values**: Identical in both codes for 200A circuits.  
- **California Amendments**: The CEC table includes a delta symbol indicating modifications in other sections (e.g., 692.45, 647.6) but does not alter the 200A EGC sizing in Table 250.122.  

**Conclusion**: Both CEC and NEC 2023 require **6 AWG copper** or **4 AWG aluminum** for a 200A equipment grounding conductor. California maintains the same table values as NEC but adds application-specific references (e.g., technical equipment grounding in 647.6).  

✓ Source: CEC 2022 / NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 3 found

**Response Time:** 8.2s

---

### cec-013: grounding [CA-SPECIFIC]

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022 vs NEC 2023)

For a **3/0 AWG copper service conductor**:
- **CEC 2022 Table 250.66** specifies **4 AWG copper** GEC [CEC Amendment]
- **NEC 2023 Table 250.66** also specifies **4 AWG copper** GEC

### Key Differences:
1. **Table Values**: Identical requirements for 3/0 AWG service conductors in both codes.
2. **California Amendments**:
   - CEC includes additional installation requirements in **Section 250.64(D)** for buildings with multiple disconnecting means in separate enclosures.
   - Requires specific grounding electrode conductor taps and common grounding electrode conductor installation not explicitly detailed in NEC.
3. **Semantic Context**:
   - NEC allows flexibility in grounding electrode conductor routing (e.g., 250.35(B) about securing exposed conductors).
   - CEC emphasizes bonding requirements in **Section 250.190(A)** for non-current-carrying metal parts.

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 4 found

**Response Time:** 10.0s

---

### cec-014: ampacity_adjustment [CA-SPECIFIC]

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)

**California (CEC 2022):**  
For a **75°C rated conductor** at **40°C ambient temperature**, the temperature correction factor is **0.88** per **CEC Table 310.15(B)(1)(1)**.

**NEC 2023 Comparison:**  
NEC 2023 Table 310.15(B)(1) specifies a **0.82** correction factor for the same conditions (75°C conductor at 40°C ambient).  

**Key Difference:**  
- **CEC allows a higher correction factor (0.88 vs. NEC 0.82)**, making California requirements **more permissive** for ampacity adjustments in this scenario.  

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 1 found

**Response Time:** 5.1s

---

### cec-015: ampacity_adjustment [CA-SPECIFIC]

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor for 7-9 Conductors (CEC 2022 vs NEC 2023)

**California (CEC 2022):**  
- **Adjustment factor**: 0.7 (70%) for 7-9 current-carrying conductors in a raceway  
- **Source**: CEC Table 310.15(C)(1)  
- **Key Notes**:  
  - Applies to all conductors in the raceway, including spares and neutrals (if current-carrying).  
  - Excludes conductors connected to non-simultaneously energized components.  

**National (NEC 2023):**  
- **Adjustment factor**: 0.7 (70%) for 7-9 current-carrying conductors in a raceway  
- **Source**: NEC Table 310.15(C)(1)  
- **Key Notes**:  
  - Same bundling rules as CEC, but additional exceptions for specific installations (e.g., Type MC cables in thermal insulation require derating per Table 310.15(C)(1)).  

**Comparison:**  
- **Same**: Both codes use **0.7 for 7-9 conductors**.  
- **Differences**:  
  - CEC includes California-specific applications (e.g., underfloor raceways in 390.23, cellular metal floor raceways in 374.23).  
  - NEC adds exceptions for Type MC cables in thermal insulation (NEC 330.31(C)).  

✓ Source: CEC 2022 / NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 4 found

**Response Time:** 7.5s

---

### cec-016: working_space [CA-SPECIFIC]

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth (CEC 2022)

**California Code (CEC 2022):**  
For a 480V panelboard under **Condition 3** (exposed live parts on both sides), the minimum working space depth is **1.2 meters (4 feet)** per **CEC Table 110.26(A)(1)**.

**NEC 2023 Comparison:**  
NEC 2023 Table 110.26(A)(1) specifies the **same 1.2 m (4 ft)** depth for 480V under Condition 3. Both codes align on this requirement.

**Key Differences:**  
- CEC includes additional rules in **Section 646.19** (entrance/egress requirements for large equipment) and **Section 425.8** (industrial heating equipment) that expand on working space accessibility.
- NEC does not have equivalent amendments in this context, making CEC slightly more restrictive in specific industrial scenarios.

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_working_space
- NEC Tools: lookup_working_space, compare_with_nec
- Exception Search Called: No

**Citations:** 3 found

**Response Time:** 5.3s

---

### cec-017: enclosure [CA-SPECIFIC]

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**Status:** PASS

**Agent Answer:**
## Outdoor Enclosure Selection for Rain, Sleet, and Ice (CEC 2022)

### **California Electrical Code (CEC 2022) Requirements**
For outdoor use with **rain, sleet, and ice**, Table 110.28 specifies the following **suitable enclosure types**:
- **Type 3**: Raintight, dusttight, and operable when ice-covered.
- **Type 3S**: Raintight, dusttight, and watertight (for severe ice conditions).
- **Type 3SX**: Raintight, dusttight, watertight, and corrosion-resistant.
- **Type 3X**: Raintight and corrosion-resistant.
- **Type 4**: Watertight and dusttight.
- **Type 4X**: Watertight, dusttight, and corrosion-resistant.
- **Type 6**: Watertight for hose-directed water.
- **Type 6P**: Watertight for prolonged submersion.

**Key CEC Amendment**:  
Footnote [*] in Table 110.28 **requires mechanisms to be operable when ice-covered** for all listed types. This is a California-specific mandate not explicitly emphasized in NEC.

---

### **NEC 2023 Comparison**
NEC Table 110.28 includes **similar enclosure types** (3, 3S, 3X, 4, etc.) for outdoor use but:
- **No explicit "ice-covered operability" requirement** in standard NEC text.
- Raintight enclosures (Types 3, 3S, 3X) are specified, but California’s CEC adds the [*] footnote for ice conditions.
- Corrosion resistance (Type 3X/4X) is optional in NEC unless specified by local amendments.

---

### **Conclusion**
- **CEC is more restrictive** for ice-prone areas due to the [*] footnote requiring operable mechanisms when iced.
- Use **Type 3S,...

**Tool Usage:**
- CEC Tools: cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 1 found

**Response Time:** 12.9s

---

### cec-018: lighting_load [CA-SPECIFIC]

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022 vs NEC 2023)

**California Code (CEC 2022):**  
- **1.3 VA per square foot** (14 VA/m²) for office buildings per **Table 220.12**.  
- Includes a **125% continuous load multiplier** (per 210.20(A)) for lighting systems expected to operate ≥3 hours continuously.  

**NEC 2023:**  
- **1.0 VA per square foot** (11 VA/m²) for office buildings per **Table 220.42(A)**.  
- No mandatory continuous load multiplier unless specified by local amendments.  

**Key Difference:**  
California’s CEC requires a **30% higher lighting load** (1.3 VA/ft² vs. 1.0 VA/ft²) compared to NEC 2023. This reflects California’s stricter energy code alignment (Title 24) and safety provisions for continuous lighting operations in commercial spaces.  

✓ Source: CEC 2022 Table 220.12, NEC 2023 Table 220.42(A)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 3 found

**Response Time:** 16.5s

---

### cec-019: flexible_cord [CA-SPECIFIC]

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**Status:** PASS

**Agent Answer:**
## 12 AWG Flexible Cord Ampacity (CEC 2022 vs NEC 2023)

### California Code (CEC 2022)
- **Ampacity**: **25 amperes** for 12 AWG flexible cord in **Column B (thermoset)**  
- **Reference**: CEC Table 400.5(A)(1), Column B  
- **Key Notes**:  
  - Applies to two-conductor cords or multiconductor cords with only two current-carrying conductors.  
  - No California amendments to NEC Table 400.5(A)(1) for this value.  

### NEC 2023
- **Ampacity**: **25 amperes** for 12 AWG flexible cord in Column B (thermoset)  
- **Reference**: NEC Table 400.5(A)(1), Column B  
- **Key Notes**:  
  - Identical values and conditions as CEC 2022.  
  - No differences in ampacity calculations or application requirements.  

### Direct Comparison
| **Parameter**               | **CEC 2022**       | **NEC 2023**       | **Difference?** |
|-----------------------------|--------------------|--------------------|-----------------|
| 12 AWG Column B Ampacity    | 25A                | 25A                | **No**          |
| Ambient Temperature Basis   | 30°C (86°F)        | 30°C (86°F)        | **No**          |
| Application Conditions      | Two current-carrying conductors | Two current-carrying conductors | **No**          |

### California-Specific Notes
- **No amendments** to NEC Table 400.5(A)(1) in CEC 2022 for flexible cord ampacity.  
- Both codes reference the same temperature and conductor assumptions (30°C ambient, standard insulation).  

✓ Source: CEC 2022 and NEC 2023 Tables 400.5(A)(1)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 1 found

**Response Time:** 15.8s

---

### cec-020: fixture_wire [CA-SPECIFIC]

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire  
### **California Code (CEc 2022)**  
- **Rating:** 200°C (392°F)  
- **Source:** CEC Table 402.3 explicitly lists Type SF-2 silicone insulated fixture wire (both solid/7-strand and flexible stranding) with a **200°C maximum operating temperature**.  

---

### **NEC 2023 Comparison**  
- **Rating:** 200°C (392°F) for silicone rubber-insulated conductors  
- **Source:** NEC 310.104(B) permits silicone rubber-insulated conductors for use at **200°C**. While NEC 2023 does not explicitly reference "Type SF-2," it aligns with CEC by allowing silicone insulation at the same temperature rating.  

---

### **Key Differences**  
1. **Explicit Listing:**  
   - CEC 2022 **explicitly names** "Type SF-2" in Table 402.3 with a 200°C rating.  
   - NEC 2023 references silicone rubber generically in **310.104(B)** without specific type designations like "SF-2."  

2. **Application Scope:**  
   - Both codes permit 200°C operation for silicone-insulated wires, but NEC uses broader language for insulation types.  

---

### **Conclusion**  
The maximum operating temperature for Type SF-2 silicone insulated fixture wire is **200°C (392°F)** in both CEC 2022 and NEC 2023. California explicitly lists this type in its tables, while NEC references silicone insulation generically but with equivalent temperature ratings.  

✓ **Sources:** CEC 2022 Table 402.3, NEC 2023 310.104(B)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 2 found

**Response Time:** 22.9s

---


## Complex Calculations

### cec-021: adjusted_ampacity [CA-SPECIFIC]

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 ...

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

### **Base Ampacity**
- **8 AWG THWN copper**: 50A at 75°C (CEC Table 310.16)

### **Adjustment Factors**
1. **Temperature Correction (40°C ambient)**:  
   - Factor: **0.88** (CEC Table 310.15(B)(1))  
   - *Same as NEC 2023 Table 310.15(B)(1)(1)*

2. **Bundling Adjustment (7 conductors)**:  
   - Factor: **0.70** (CEC Table 310.15(C)(1))  
   - *Same as NEC 2023 Table 310.15(C)(1)*

### **Final Calculation**
```
Adjusted Ampacity = 50A × 0.88 × 0.70 = 30.8A
```

### **CEC vs NEC Comparison**
- **California (CEC 2022)**:  
  - Temperature correction and bundling factors match NEC.  
  - No additional amendments for this calculation.  
- **NEC 2023**:  
  - Identical adjustment factors (0.88 for 40°C, 0.70 for 7 conductors).  

### **Key Citations**
- Base ampacity: CEC Table 310.16  
- Temperature correction: CEC 310.15(B)(1)  
- Bundling adjustment: CEC 310.15(C)(1)  

✓ **Source**: CEC 2022 and NEC 2023 tables match for this scenario.

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment
- NEC Tools: lookup_conductor_ampacity, lookup_ampacity_adjustment, lookup_ampacity_adjustment, compare_with_nec
- Exception Search Called: No

**Citations:** 2 found

**Response Time:** 6.5s

---

### cec-022: service_sizing [CA-SPECIFIC]

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper...

**Status:** PASS

**Agent Answer:**
## Service Sizing for 200A Residential (CEC 2022 vs NEC 2023)  

### **1. Service Conductors**  
- **CEC**: **2/0 AWG copper** (Table 310.12(A) for dwelling services).  
- **NEC**: **250 kcmil copper** (Table 310.16 for general conductors at 75°C).  
- **Difference**: CEC allows smaller conductors for dwelling services due to Table 310.12(A), while NEC uses Table 310.16 for general applications.  

---

### **2. Equipment Grounding Conductor (EGC)**  
- **CEC & NEC**: **6 AWG copper** (Table 250.122 for 200A OCPD).  
- **No difference** between codes.  

---

### **3. Grounding Electrode Conductor (GEC)**  
- **CEC & NEC**: **4 AWG copper** (Table 250.66 for 2/0 service conductor).  
- **No difference** between codes.  

---

### **Key Takeaways**  
1. **Service Conductors**:  
   - CEC uses **Table 310.12(A)** (dwelling-specific), allowing **2/0 AWG** for 200A.  
   - NEC uses **Table 310.16** (general), requiring **250 kcmil** for 200A.  
   - **California is more permissive** for residential services.  

2. **Grounding Conductors**:  
   - Tables 250.122 and 250.66 are identical in CEC and NEC for this application.  

---

### **California Amendments**  
- **CEC 310.12(A)**: Explicitly permits smaller conductors for dwelling services compared to NEC.  
- **CEC 250.122/250.66**: Same as NEC tables but marked with [delta] symbols for California amendments.  

✓ Source: CEC 2022 & NEC 2023

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 4 found

**Response Time:** 15.1s

---

### cec-023: commercial_load [CA-SPECIFIC]

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The ...

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)

### California (CEC 2022)
- **Unit load for office**: 1.3 VA/ft² (Table 220.12)
- **125% multiplier included**: Yes (per CEC 220.12 note)
- **Calculation**:  
  $$
  5,000 \, \text{ft}^2 \times 1.3 \, \text{VA/ft}^2 = 6,500 \, \text{VA}
  $$

### NEC 2023 Comparison
- **Unit load for office**: 1.3 VA/ft² (Table 220.42(A))
- **125% multiplier included**: No (NEC applies 125% separately per 210.20(A))
- **Calculation**:  
  $$
  5,000 \, \text{ft}^2 \times 1.3 \, \text{VA/ft}^2 = 6,500 \, \text{VA} \, (\text{before 125%})
  $$

### Key Differences
- **CEC**: 125% multiplier is **already embedded** in Table 220.12 values.
- **NEC**: 125% multiplier must be applied **separately** per 210.20(A).

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 3 found

**Response Time:** 10.7s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit (CEC 2022 vs NEC 2023)

### **California (CEC 2022) Requirement**
- **Conductor**: 16 AWG copper  
- **Condition**: Conductors extend beyond the motor control equipment enclosure  
- **Maximum OCPD**: **10 amperes**  
  (Per **CEC Table 430.72(B), Column C** for 16 AWG copper)

---

### **NEC 2023 Comparison**
- **NEC Table 430.72(B)(2)** specifies identical values:  
  - **Column C (conductors extending beyond enclosure)**: **10A** for 16 AWG copper  
- **No differences** between CEC 2022 and NEC 2023 for this application.

---

### **Key Findings**
1. **Alignment**: California's CEC adopts NEC 430.72 without modification for motor control circuit overcurrent protection.  
2. **Column C Applies**: Both codes use Column C when conductors extend beyond the enclosure.  
3. **No Additional Restrictions**: CEC 2022 does not impose stricter limits than NEC 2023 for this scenario.

✓ Source: CEC 2022 Table 430.72(B) and NEC 2023 Table 430.72(B)(2)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 1 found

**Response Time:** 13.2s

---

### cec-025: dwelling_load [CA-SPECIFIC]

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation for Dwelling Unit (CEC 2022 vs NEC 2023)

### **California Electrical Code (CEC 2022)**
**Calculation:**  
2,400 sq ft × **3 VA/sq ft** (per CEC 220.14(J)) = **7,200 VA**  

**Key Provisions:**  
- **CEC 220.14(J):** Mandates **3 VA per square foot** for dwelling units (1-family, 2-family, multifamily).  
- **125% Continuous Load Factor:** Already incorporated in the 3 VA/sq ft value (per CEC 220.14 note).  

---

### **NEC 2023 Comparison**  
**Calculation:**  
2,400 sq ft × **3 VA/sq ft** (per NEC 220.41) = **7,200 VA**  

**Key Provisions:**  
- **NEC 220.41:** Specifies **3 VA per square foot** for dwelling units.  
- **No Additional Multiplier:** NEC requires separate application of the 125% continuous load factor (not pre-included in the 3 VA/sq ft value).  

---

### **Critical Differences**  
| **Aspect**               | **CEC 2022**                          | **NEC 2023**                          |  
|--------------------------|---------------------------------------|---------------------------------------|  
| **VA per sq ft**         | 3 VA/sq ft (dwelling units)           | 3 VA/sq ft (dwelling units)           |  
| **125% Continuous Load** | **Pre-included** in 3 VA/sq ft        | **Not included** – apply separately   |  
| **Code Reference**        | CEC 220.14(J)                         | NEC 220.41                            |  

**Conclusion:**  
Both codes use **3 VA/sq ft** for dwelling units, but **CEC 2022** incorpora...

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 2 found

**Response Time:** 11.8s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for...

**Status:** PASS

**Agent Answer:**
## Kitchen GFCI Requirements Comparison (CEC 2022 vs NEC 2023)

### **Common Requirements**
Both codes require **GFCI protection for countertop receptacles** in kitchens:
- **CEC 210.8(A)(6)**: Applies to receptacles serving countertop surfaces.
- **NEC 210.8(A)(6)**: Same requirement for countertop receptacles within 6 ft of a sink.

### **Key Differences**
| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|---------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Scope of Protection**   | Explicitly includes **all countertop receptacles** in kitchens.             | Covers countertop receptacles but allows exceptions for appliances with built-in GFCI (NEC 422.5). |
| **Exceptions**            | Limited exceptions (e.g., dedicated circuits for specific appliances).      | More exceptions for appliances (e.g., vending machines, sump pumps).         |
| **Additional CEC Mandates** | **Title 24 CALGreen** requires GFCI for **all 125V receptacles in kitchens**, including those not near countertops. | No state-specific mandates; follows national scope only.                   |

### **Restrictiveness Analysis**
- **CEC is MORE RESTRICTIVE** because:
  1. **Broader coverage**: Requires GFCI for **all kitchen receptacl...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 2 found

**Response Time:** 8.8s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO suc...

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023)

### **California Energy Code (CEC 2022)**
1. **Reserved Circuit Breaker Spaces** (CEC 408.2(A)):
   - **Single-family dwellings** must have reserved spaces in panelboards for:
     - Heat pump water heaters
     - Heat pump space heaters
     - Electric cooktops
     - Electric clothes dryers
   - Mandated by **California Energy Code Section 150.0** (n), (t), (u), and (v).
   - Ensures future-ready infrastructure for electrification and energy efficiency.

2. **General Panelboard Requirements**:
   - Panelboard ratings must meet minimum feeder capacity (CEC 408.30).
   - Wire-bending spaces must comply with Table 312.6(B) (or exceptions for smaller panelboards).

---

### **National Electrical Code (NEC 2023)**
1. **General Panelboard Requirements**:
   - Panelboards must have a rating ≥ calculated feeder load (NEC 408.30).
   - No specific mandates for reserved spaces for appliances like heat pumps or electric cooktops.
   - Focuses on **safety and installation standards** (e.g., disconnecting means, enclosure ratings).

2. **Appliance-Specific Provisions**:
   - NEC 422.34 allows unit switches as disconnecting means in multifamily dwellings but does not address reserved panelboard spaces.
   - No direct equivalent to CEC 408.2(A) for single-family dwellings.

---

### **Key Differences**
| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 5 found

**Response Time:** 9.1s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules fo...

**Status:** PASS

**Agent Answer:**
## California vs NEC EV Charging Requirements (CEC 2022 vs NEC 2023)

### 1. **Scope and Application**
- **CEC 625.1**: Explicitly includes **bidirectional power flow** (vehicle-to-grid) and references **CALGreen** mandates for new construction.  
- **NEC 2023**: Focuses on **unidirectional charging** (no specific mention of power export).  
- **Key Difference**: California requires compliance with **CALGreen Chapter 4/5** for EV infrastructure in new buildings, which NEC does not address.

---

### 2. **Branch Circuit Requirements**
- **CEC 625.40**:  
  - *Mandates individual branch circuits* for EV outlets with **no other outlets**.  
  - *No exceptions* for shared circuits.  
- **NEC 210.11(C)(1)**:  
  - Permits shared circuits for EV receptacles if rated ≤ 20A.  
- **Restrictiveness**: **CEC is more restrictive** by prohibiting shared circuits.

---

### 3. **Ventilation Requirements**
- **CEC 625.52**:  
  - Requires **mechanical ventilation** for indoor EV charging if equipment is not listed for "ventilation-free" use.  
  - Specifies formulas for calculating ventilation based on number of EVs and power levels.  
- **NEC 2023**:  
  - No specific ventilation requirements for EV charging.  
- **Restrictiveness**: **CEC adds mandatory ventilation** not present in NEC.

---

### 4. **Receptacle Enclosures**
- **CEC 625.56**:  
  - Requires **weatherproof enclosures** for outdoor EV receptacles, with **extra-duty** outlet box hoods.  
  - Permits non-hooded enclosures onl...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 13 found

**Response Time:** 16.3s

---

### cec-029: afci [CA-SPECIFIC]

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and sim...

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements: CEC 2022 vs NEC 2023 for Dwelling Units

### **1. Scope of Protection**
- **CEC 2022 (210.12(A))**  
  - Applies to **all 120V, 15/20A branch circuits** in **kitchens, family rooms, dining rooms, living rooms, bedrooms, and similar areas** of dwelling units.  
  - **Exceptions**: Fire alarm circuits (760.41(B)/760.121(B)) and branch circuit extensions ≤1.8m (6ft) without additional outlets.

- **NEC 2023 (210.12(B))**  
  - Same scope as CEC but explicitly includes **dormitory units, guest rooms, and patient sleeping rooms** in nursing homes.  
  - **Exceptions**: Fire alarm circuits and circuits modified/extended under 210.12(D).

---

### **2. Permitted AFCI Types**
Both codes allow:  
1. **Combination-type AFCI** (entire circuit protection).  
2. **Branch/feeder-type AFCI + outlet branch-circuit AFCI**.  
3. **Supplemental arc protection circuit breaker + outlet AFCI** (with wiring continuity and length limits).  
4. **Outlet branch-circuit AFCI** (if metal raceway or concrete-encased wiring is used between OCPD and first outlet).  

**Key Difference**:  
- **CEC** explicitly permits **Type MC/AC cable** in 210.12(A)(5), while **NEC** references **UL 1699** and **UL Subject 1699A** for AFCI listings.

---

### **3. Installation Requirements**
- **Location**: Both require AFCI to be **readily accessible**.  
- **Wiring Continuity**:  
  - CEC: Requires **continuous wiring** from OCPD to first outlet for methods 210.12(A)(3) and (4).  
  - NE...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 6 found

**Response Time:** 10.1s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key differ...

**Status:** PASS

**Agent Answer:**
## California vs NEC Solar PV Requirements (CEC 2022 vs NEC 2023)

### **Key Differences in AC Module Requirements**
| **Requirement**                | **California (CEC 2022)**                                                                 | **NEC 2023**                                                                 |
|-------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **AC Module Source Circuits** | **690.6(A):** PV source circuit requirements *do not apply* to AC modules.               | General PV source circuit rules in 690.8 apply to all systems.              |
| **Output Circuit Classification** | **690.6(B):** AC module output is treated as an *inverter output circuit*.              | No specific exception for AC modules; output circuits follow 690.9.         |
| **Internal Components**        | Conductors and inverters within AC modules are considered *internal components*.        | No explicit provision; assumes separate compliance for all components.      |

---

### **California-Specific Provisions**
1. **AC Module Exemption**  
   - CEC 690.6(A) explicitly excludes AC modules from PV source circuit requirements (e.g., 690.8 for DC circuits).  
   - NEC 2023 does not differentiate AC modules in Article 690.

2. **Output Circuit Treatment**  
   - CEC 690.6(B) classifies AC module output as an *inverter output cir...

**Tool Usage:**
- CEC Tools: cec_search
- NEC Tools: compare_with_nec
- Exception Search Called: No

**Citations:** 5 found

**Response Time:** 8.9s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 27/30
- **NEC Comparison Tool Used**: 30/30
- **cec_lookup_table Used**: 10/30
- **Exception Search Called (Voluntary)**: 1/30
- **Success Rate**: 100.0%
- **Average Response Time**: 11.6s

### Exception Search Analysis

With mandatory exception search removed, the agent now calls it voluntarily based on context.
This should result in:
- Fewer irrelevant exception results polluting answers
- Better answer quality for table description questions (cec-007, cec-008)
- Same quality for questions where exceptions are legitimately relevant

