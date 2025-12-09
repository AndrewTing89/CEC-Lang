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
| **Total Duration** | 830.1s |
| **Avg per Question** | 27.7s |

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

**California Requirements:**  
1. **Reserved Circuit Breaker Spaces**:  
   - Panelboards in single-family dwellings **must include dedicated spaces** for:  
     - Heat pump water heaters  
     - Heat pump space heaters  
     - Electric cooktops  
     - Electric clothes dryers  
   - This is mandated by **CEC 2022 Section 408.2(A)**, which references California Energy Code Sections 150.0, 150.11, and 160.9.  

2. **Panelboard Rating**:  
   - Minimum rating must match the calculated feeder capacity per Article 220 (CEC 408.30).  

3. **Wire-Bending Space**:  
   - Enclosures must comply with **Table 312.6(B)** for conductor sizes, with exceptions for smaller panelboards (≤225A, ≤42 overcurrent devices) (CEC 408.55).  

**Exceptions Checked**:  
- No exceptions override the reserved space requirement in 408.2(A).  
- Exceptions for wire-bending spaces (408.55) and grounding (408.40) do not affect appliance-specific reserved spaces.  

---

## NEC 2023 Reference  
- **Reserved Spaces**: **No requirement** in NEC. California’s appliance-specific reserved spaces are a [CEC] amendment.  
- **Panelboard Rating**: Same as CEC (NEC 2023 Section 408.30).  
- **Wire-Bending Space**: Identical to CEC (NEC 2023 Section 312.6).  

---

**Final Answer**:  
In California, single-family dwelling panelboards must reserve spaces for heat pump water heaters, heat pump space heaters, electric cooktops, and dryers per **CEC 2022 Section 408.2(A)**. Panelboard ratings and wire-bending spaces align with NEC 2023, but reserved spaces are a California-specific requirement.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 408.55, 408.2, 150.11, 408.40, 160.9, 312.6, 150.0, 408.30

**Response Time:** 23.7s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. CEC 408.2 requires panelboard spaces for EV charging equipment. Title 24 also mandates EV charging readiness.

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California Electrical Code (CEC 2022) Requirements for EV Charging in New Residential Construction

### **1. Branch Circuit Requirements (625.40)**
- **Dedicated Circuits**: Each EV charging outlet must be supplied by an **individual branch circuit** with **no other outlets**.  
- **Exception**: 625.46 requires anti-backfeed mechanisms to prevent energy from the EV from feeding back into the premises wiring if the utility power fails.  
- **NEC Comparison**: NEC 424.4 allows shared circuits for fixed electric space-heating equipment but does not specifically mandate dedicated circuits for EVs. California adds this requirement for safety.

---

### **2. Equipment Connection Methods (625.44)**
- **Portable Equipment**: Must use receptacles rated 125V–250V, 15–50A (e.g., NEMA 14-50).  
- **Fastened-in-Place Equipment**: Requires permanent wiring or listed receptacles (e.g., NEMA 14-50 for Level 2 chargers).  
- **Fixed Equipment**: Must be hardwired and permanently mounted.  
- **Exception**: 625.47 allows multiple branch circuits if equipment is identified for such use (e.g., dual-port chargers).  
- **NEC Comparison**: NEC 625.44 mirrors CEC requirements but lacks California’s emphasis on weatherproof enclosures for outdoor installations.

---

### **3. Receptacle Enclosures (625.56)**
- **Weatherproof Enclosures**: All outdoor EVSE receptacles must have **listed, weatherproof enclosures** (e.g., NEMA 3R or 4X).  
- **Extra Duty Rating**: Outlet box hoods must be marked "extra duty" if used.  
- **NEC Comparison**: NEC 314.72(C) requires complete enclosures but does not mandate "extra duty" ratings for EV-specific applications. California adds this for durability in wet locations.

---

### **4. GFCI Protection (625.60)**
- **Mandatory GFCI**: All EVSE receptacles must have **GFCI protection** for personnel safety.  
- **Reset Accessibility**: GFCI reset buttons must be **readily accessible**.  
- **Exception**: 210.8(A) excludes GFCI for certain industrial equipm...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec, compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 9 found
- 625.40, 625.60, 314.72, 625.46, 625.44, 625.56, 210.8, 424.4, 625.47

**Response Time:** 20.6s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California-Specific Solar PV Requirements (CEC 2022)  

### 1. **Voltage Limits**  
- **CEC 2022 Section 690.7**:  
  - **Residential systems** (one- and two-family dwellings) are limited to **600 volts DC maximum** for PV system DC circuits.  
  - Non-residential systems on buildings may go up to **1000 volts DC**, and off-site equipment (e.g., racking) may use up to **1500 volts DC** if listed.  
  - **Voltage correction**: Maximum voltage must account for lowest ambient temperatures using module-specific temperature coefficients or Table 690.7(A) for crystalline silicon modules.  

- **NEC Comparison**:  
  NEC 2023 allows **1000 volts DC** for all systems on or in buildings, with no residential-specific voltage limit. California’s 600V limit for dwellings is stricter.  

---

### 2. **Overcurrent Protection**  
- **CEC 2022 Section 690.9**:  
  - Conductors must be protected against overcurrent per 690.8 calculations.  
  - **Exceptions**:  
    - Conductors ≤3m (10ft) in metal raceways/cables or underground need only one-end protection.  
    - Systems with listed "current-limiting" devices may bypass overcurrent protection if currents do not exceed device ratings.  

- **NEC Comparison**:  
  NEC 2023 requires overcurrent protection for all PV circuits unless conductors are sized for 125% of maximum current and sources are current-limited. California adds exceptions for short runs in metal raceways.  

---

### 3. **Arc-Fault Circuit Protection**  
- **CEC 2022 Section 690.11**:  
  - **Mandatory** for PV systems with DC circuits ≥80V.  
  - **Exception**: Systems not installed on/in buildings (e.g., ground-mounted arrays in metal raceways) are exempt.  

- **NEC Comparison**:  
  NEC 2023 requires arc-fault protection for all PV systems ≥80V. California’s exception for non-building installations is unique.  

---

### 4. **Circuit Sizing and Current Calculations**  
- **CEC 2022 Section 690.8**:  
  - **Source circuit current** = 125% of total short-circui...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 690.7, 690.8, 690.11, 310.15, 690.10, 690.9

**Response Time:** 15.6s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## California Circuit Requirements for Heat Pump Water Heaters in New Dwellings (CEC 2022)

### **CEC 2022 Requirements**
1. **Dedicated Circuits and Panelboard Spaces**  
   - **Single-family buildings** (1–2 dwellings):  
     - Each dwelling unit must have **designated spaces, receptacles, and dedicated branch circuits** for heat pump water heaters as specified in California Energy Code §150.0(n) (CEC 422.3(A)).  
     - Panelboards must include **circuit breaker spaces** for heat pump water heaters (CEC 408.2(A)).  

   - **Multifamily buildings**:  
     - Panelboards must reserve **circuit breaker spaces** for heat pump water heaters as per California Energy Code §160.9 (CEC 408.2(B)).  

2. **General Installation Rules**  
   - Heat pump water heaters must comply with **Article 430** (motor-operated appliances) and **Article 440** (refrigerant motor-compressors) (CEC 422.3).  

3. **Exceptions**  
   - **Auxiliary equipment** (e.g., pumps, valves) associated with the water heater may share the same branch circuit (Exception 1, CEC 422.12).  
   - Installations using non-standard methods require **special permission** (CEC 422.23).  

---

## NEC 2023 Comparison  
- **NEC 422.12** requires central heating equipment (including water heaters) to have an individual branch circuit, but **no explicit provisions** for "readiness" or panelboard spaces for future appliances.  
- **NEC 422.13** addresses storage water heater overcurrent protection but does **not mandate dedicated circuits** for heat pump water heaters.  
- **California amendments** (CEC 422.3, 408.2) add **readiness requirements** for panelboard spaces and circuits in new dwellings, ensuring compatibility with future heat pump water heater installations.  

---

**Sources:**  
✓ CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 408.2, 422.13, 160.9, 422.23, 150.0, 422.3, 422.12

**Response Time:** 15.4s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
**Electric Cooktop Readiness Requirements in California**  

### **Single-Family Residential Buildings**  
Per **CEC 2022 Section 422.3(A)** and **California Energy Code Section 150.0(u)**:  
- Each dwelling unit must have **dedicated circuits and circuit identifications** for electric cooktops.  
- Panelboards must include **designated spaces and branch circuits** to accommodate future electric cooktop installations.  
- This ensures readiness for electric cooktops even if not immediately installed.  

### **Multifamily Buildings**  
Per **CEC 2022 Section 422.3(B)** and **California Energy Code Section 160.9(b)**:  
- Each dwelling unit requires **dedicated circuits and circuit identifications** for electric cooktops.  
- Panelboards must provide **circuit breaker spaces** to support electric cooktops as specified in the Energy Code.  

### **Key Provisions**  
- **CEC 408.2(A/B)** mandates panelboards in single-family and multifamily buildings to include spaces for electric cooktops.  
- No exceptions were found for these readiness requirements via `cec_exception_search`.  

---

## NEC 2023 Reference  
The **NEC 2023** does not include these specific readiness provisions for electric cooktops. California’s Energy Code amendments (150.0(u) and 160.9(b)) are **unique to CEC**, emphasizing energy efficiency and future-proofing for electric appliances.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 422.3, 160.9, 150.0, 408.2

**Response Time:** 16.2s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryers in California (CEC 2022)

### **California Electrical Code (CEC) Requirements**
1. **Dedicated Circuit Breaker Spaces**  
   - **Single-Family/Multifamily Buildings**:  
     - **CEC 408.2(A)/(B)**: Panelboards must include dedicated circuit breaker spaces for electric clothes dryers.  
     - **Single-Family**: Spaces for heat pump water heaters, electric cooktops, and dryers (per California Energy Code Section 150.0(v)).  
     - **Multifamily**: Spaces for electric cooktops and dryers (per California Energy Code Section 160.9(c)).  

2. **Dedicated Circuits**  
   - **CEC 422.3(A)/(B)**:  
     - **Single-Family**: Dryers must have dedicated circuits with proper circuit identification.  
     - **Multifamily**: Dryers require dedicated circuits per California Energy Code Section 160.9(c).  

3. **Exceptions**  
   - **210.52(F)**:  
     - Laundry receptacles are not required in multifamily buildings if on-site laundry facilities exist for all occupants.  
     - Not required in non-one-family dwellings if laundry facilities are not installed/allowed.  

---

## NEC 2023 Comparison  
- **NEC 220.54**: Load calculations for dryers (5,000W minimum), but **no mandate** for dedicated panelboard spaces or circuits for dryers.  
- **NEC 422.10**: General appliance circuit requirements (e.g., conductor ampacity ≥ appliance rating), but **no specific dryer panelboard provisions**.  

**Key California Amendment**:  
- CEC explicitly requires **pre-wiring** (dedicated spaces/circuits) for dryers in new construction, which is **not required by NEC**.  

---

### **Summary**  
- **California (CEC)**: Mandates dedicated panelboard spaces and circuits for dryers in new construction (408.2, 422.3).  
- **NEC**: No such requirement; focuses on load calculations and general appliance circuits.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 210.52, 408.2, 220.54, 160.9, 422.10, 150.0, 422.3

**Response Time:** 16.9s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Final Answer

**California Requirement (CEC 2022):**  
CEC Table 240.4(G) is a **California-specific amendment** that modifies the National Electrical Code (NEC) by adding cross-references to overcurrent protection requirements for specialized conductors. Key unique features include:  

1. **California-Specific Cross-References**:  
   - Directs users to **CEC Sections 240.100 and 240.101** for overcurrent protection of conductors in applications like fire alarm systems, surge arresters, and low-voltage control circuits. These sections are not explicitly referenced in the NEC version of Table 240.4(G).  

2. **Exception in 370.23**:  
   - Allows cablebus overcurrent protection to follow **240.100/240.101** instead of general rules in 240.4. This exception is unique to California and not present in the NEC.  

3. **[CEC] Markers**:  
   - The table includes [CEC] annotations indicating modifications to NEC requirements, such as stricter rules for conductors in commercial kitchens or data centers.  

**NEC 2023 Reference**:  
The NEC version of Table 240.4(G) contains only general cross-references without California-specific amendments. California’s additions are **not present in the national code** and are enforced solely under the CEC.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 240.4, 240.100, 240.101, 370.23

**Response Time:** 25.7s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC 2022 Table 242.3 Specification (California)

**CEC Table 242.3** is a **cross-reference table** for Article 242 (Overvoltage Protection) in the California Electrical Code. It specifies that **equipment must be protected against overvoltage** in accordance with the article in the Code that covers the type of equipment or location. The table directs users to **other NEC articles** that contain additional overvoltage protection requirements for specific equipment types (e.g., motors, transformers, etc.).  

This table is a **California-specific amendment** (marked with [N] in the CEC) and does not exist in the base NEC 2023. It ensures California installations comply with localized overvoltage protection requirements beyond the national code.

---

## NEC 2023 Reference  
The **NEC 2023 does not include Table 242.3**. This is a **California-specific addition** to the CEC, reflecting localized amendments to address overvoltage protection requirements for equipment types not explicitly covered in the national code.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 242.3

**Response Time:** 38.8s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC 2022 Table 430.72(B) - Motor Control Circuit Overcurrent Protection  
**California Electrical Code (CEc 2022) Amendment**  

### **Table Structure**  
Specifies **maximum overcurrent protective device ratings (in amperes)** for motor control circuits based on:  
- **Conductor size** (18 AWG to larger than 10 AWG)  
- **Material** (copper or aluminum)  
- **Installation configuration** (Columns A, B, C):  
  - **Column A**: Separate overcurrent protection required (per 430.72(B)(1)).  
  - **Column B**: Protection by motor branch-circuit device (conductors do not extend beyond the motor control equipment enclosure).  
  - **Column C**: Protection by motor branch-circuit device (conductors extend beyond the enclosure).  

**Example Values** (Copper Only):  
| Conductor Size | Column A (Separate Protection) | Column B (Branch-Circuit Protection) | Column C (Extended Conductors) |  
|----------------|-------------------------------|--------------------------------------|--------------------------------|  
| 14 AWG         | (Note 1)                      | 100A                                 | 45A                            |  
| 12 AWG         | (Note 1)                      | 120A                                 | 60A                            |  
| 10 AWG         | (Note 1)                      | 160A                                 | 90A                            |  

**Notes**:  
1. Values derived from **Table 310.15** (60°C conductors).  
2. 400% of Table 310.17 values for 60°C conductors.  
3. 300% of Table 310.16 values for 60°C conductors.  

---

### **Key Exceptions**  
1. **Hazardous Circuits**:  
   - Overcurrent protection **may be omitted** if the control circuit’s opening creates a hazard (e.g., fire pump motors).  
   - Example: Fire pump control circuits only require short-circuit/ground-fault protection (per motor branch-circuit device).  

2. **Transformer Protections**:  
   - Conductors supplied by a single-phase transformer’s secondary ca...

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 430.72, 430.32, 310.16, 310.17, 310.15, 430.55

**Response Time:** 28.3s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Final Answer

### California-Specific Medium Voltage (MV) Cable Tables in CEC 2022

The **California Electrical Code (CEC 2022)** includes **17+ medium voltage (2001–35,000V) cable ampacity tables** (311.60(C)(67)–(C)(86)) that are **not present in the NEC 2023**. These tables address unique installation scenarios, including:

1. **Triplexed Cables** (e.g., 311.60(C)(67)–(C)(68))  
   - Ampacities for three single-conductor cables twisted together.  
   - NEC lacks equivalent tables for triplexed configurations.

2. **Isolated Conductors** (e.g., 311.60(C)(69)–(C)(70))  
   - Single copper/aluminum conductors in air.  
   - NEC does not include isolated conductor ampacities.

3. **Underground Ducts** (e.g., 311.60(C)(77)–(C)(80))  
   - Three-conductor cables in ducts.  
   - NEC tables omit direct burial depth adjustments.

4. **Direct Burial** (e.g., 311.60(C)(81)–(C)(86))  
   - Single and three-conductor cables buried in earth.  
   - CEC includes burial depth derating (6% per 300mm/ft) in 311.60(D)(4).

---

### Exceptions Affecting Table Application

1. **Short-Circuit Portion Exception** (311.60(A)(2))  
   - Allows higher ampacity for short circuit segments (≤3m/10ft or 10% of total circuit).  
   - Example: A 100A cable in a 10m run could use 120A ampacity for the first 1m if the rest meets 100A.

2. **Cable Tray Derating** (392.80(B))  
   - 95% derating for covered trays >1.8m (6ft).  
   - 75% derating for 600kcmil+ cables in covered trays.  
   - NEC lacks these specific derating rules.

3. **Shielding Requirements** (311.44)  
   - Non-shielded cables up to 2400V permitted in industrial settings with qualified personnel.  
   - NEC requires shielding for all MV cables above 2000V.

4. **Direct Burial Exceptions** (311.36)  
   - Non-shielded cables with metallic sheath/armor allowed up to 2400V.  
   - NEC mandates shielding for all MV direct burial.

---

### NEC 2023 Comparison

- **NEC 315.60(C)** includes 20 tables but omits:  
  - Triplexed cab...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 311.36, 315.60, 311.44, 311.60, 315.32, 392.80

**Response Time:** 28.1s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
The ampacity of a 4/0 AWG copper conductor at 75°C is **230 amperes** per CEC 2022 Table 310.16. This value accounts for standard conditions (30°C ambient temperature, up to 3 current-carrying conductors). 

**Exceptions Checked**:  
- Section 310.12 (special conditions for conductor types/locations)  
- Section 310.15(B/C) (temperature/bundling adjustments)  
- Section 210.19 (branch circuit ampacity requirements)  

No exceptions directly modify this base ampacity for general applications. For dwelling services/feeders, see Section 310.12 (special ampacity rules for single-phase dwellings).

---
## NEC 2023 Reference  
No difference from NEC 2023. The ampacity of 4/0 AWG copper at 75°C remains **230 amperes** per NEC Table 310.16. California has no amendments to this specific value.

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.15, 310.12, 310.16, 210.19

**Response Time:** 11.6s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size (CEC 2022)  
For a **200A circuit** in California, the required equipment grounding conductor (EGC) size is:  
- **6 AWG copper**  
- **4 AWG aluminum/copper-clad aluminum**  

This is specified in **CEC 2022 Table 250.122**, which maps overcurrent device ratings to minimum EGC sizes. The California amendment (∆) indicates this requirement may differ from the NEC in specific scenarios (e.g., auxiliary grounding electrodes), but for standard 200A circuits, the size matches NEC Table 250.122.  

### Exceptions Checked:  
- **250.121**: Prohibits using EGC as a grounding electrode conductor (not applicable here).  
- **356.60/352.60**: Require separate EGC in conduits (applicable if using metallic conduit, but size remains 6 AWG/4 AWG).  
- **250.134**: Permits separate EGC runs (does not affect sizing).  
- **250.54**: Relates to auxiliary electrodes (not relevant for standard installations).  

No exceptions override the base EGC size for this scenario.  

---
## NEC 2023 Reference  
The NEC 2023 also specifies **6 AWG copper** or **4 AWG aluminum** for 200A circuits per **NEC Table 250.122**. California amendments (∆) may add local requirements (e.g., auxiliary grounding), but standard sizing aligns with NEC.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 356.60, 250.134, 250.122, 250.54, 352.60, 250.121

**Response Time:** 17.3s

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
- **Code Reference**: CEC 2022 Table 250.66  
- **California Amendment**: The table includes a California-specific amendment (delta symbol) indicating localized adjustments (e.g., installation methods or additional grounding electrodes) may apply, but the conductor size remains unchanged from NEC 2023.  

---

## NEC 2023 Reference  
The NEC also specifies **4 AWG copper** for a 3/0 AWG service conductor per Table 250.66. California’s requirement matches the NEC in this case.  

✓ **Sources**: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 35.6s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)
For a **75°C rated conductor** at **40°C ambient temperature**, the temperature correction factor is **0.88** per **CEC 2022 Table 310.15(B)(1)**.  

**Exceptions checked:**  
- **Rooftop adjustment exception (310.15(B)(2))** does not apply (no mention of rooftop installation).  
- **Type XHHW-2 exception** does not apply (conductor type not specified).  

No other exceptions modify this correction factor.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The same temperature correction factor of **0.88** applies.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 24.5s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Factor (CEC 2022)  
For **7–9 current-carrying conductors** in a raceway, the ampacity adjustment factor is **0.70**, per **CEC 2022 Table 310.15(C)(1)**.  

**Exception Analysis**:  
- No exceptions in CEC 2022 override this factor for 7–9 conductors.  
- Exceptions like 310.15(C)(1)(d) apply to **more than 20 conductors** or specific cable types (e.g., Type AC/MC), which are irrelevant here.  

**Footnote Clarification**:  
The count includes all conductors (spare, neutrals, grounding/bonding) unless they cannot be simultaneously energized.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The adjustment factor for 7–9 conductors is also **0.70** per NEC Table 310.15(C)(1).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 61.5s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth (CEC 2022)  
For a **480V panelboard under Condition 3** (exposed live parts on both sides of the working space), the **minimum working space depth** required is **1.2 meters (4 feet)** per **CEC 2022 Table 110.26(A)(1)**.  

### Exceptions Checked:  
1. **Dead-front assemblies** (110.26(A)(1)(a)): Does not apply unless the panelboard is a dead-front type (not specified in the question).  
2. **Low-voltage exceptions** (110.26(A)(1)(b)): Inapplicable (480V exceeds 30V RMS).  
3. **Existing buildings** (110.26(A)(1)(c)): Requires Condition 2 clearance, but the question specifies Condition 3.  
4. **Existing dwelling units** (Exception No. 2): Not applicable unless the panel is in a dwelling unit.  

No exceptions override the base requirement for this scenario.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The same 4-foot (1.2-meter) depth requirement applies under NEC Table 110.26(A)(1) for 480V systems under Condition 3.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 20.9s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
**Suitable Enclosures for Outdoor Use with Rain, Sleet, and Ice (CEC 2022 Table 110.28):**  
- **Type 3**: Raintight, dusttight, and ice-covered operable.  
- **Type 3S**: Raintight, dusttight, sleet-resistant.  
- **Type 3SX**: Raintight, dusttight, sleet-resistant, snow load-resistant.  
- **Type 3X**: Raintight, dusttight, corrosion-resistant.  
- **Type 4**: Watertight, dusttight, hose-directed water protection.  
- **Type 4X**: Watertight, dusttight, corrosion-resistant.  
- **Type 6**: Watertight, temporary submersion-resistant.  
- **Type 6P**: Watertight, prolonged submersion-resistant.  

**Exceptions and Additional Requirements:**  
1. **110.70 General**:  
   - Enclosures for personnel entry must provide safe workspace.  
   - *Exception*: Industrial systems under qualified supervision may use engineering-practice designs (documentation required).  

2. **110.31 Enclosure for Electrical Installations**:  
   - Outdoor installations must be enclosed with fences ≥2.1 m (7 ft) to restrict access to qualified persons.  
   - Fences must comply with clearance requirements from live parts (see Table 110.31).  

3. **Mechanism Operability**: All listed types must have mechanisms operable when ice-covered.  

**No California-specific exceptions override Table 110.28.**  

---

## NEC 2023 Reference  
No difference from NEC 2023. Table 110.28 and its exceptions are identical in both codes.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.31, 110.70, 110.28

**Response Time:** 24.4s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 3.5 VA per square foot per CEC 2022 Table 220.12 [California Amendment]

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)

**California Requirement (CEC 2022):**  
Per CEC 2022 Table 220.12, the general lighting load for **office buildings** is **14 volt-amperes per square foot (VA/ft²)**. This value includes the 125% continuous load multiplier required by 210.20(A) for branch circuit calculations.  

**Exceptions/Modifications:**  
- **Energy Code Compliance Exception (Section 220.12(B)):**  
  If the building complies with a local energy code and meets specific monitoring requirements (e.g., power monitoring system with load alarms), the lighting load may be calculated using the energy code’s unit values instead of 14 VA/ft².  

**NEC Comparison:**  
The NEC 2023 specifies the same value of **14 VA/ft²** for office buildings in Table 220.12. There are no differences between CEC 2022 and NEC 2023 for this requirement.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 210.20

**Response Time:** 22.3s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1) [California Amendment]

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
The ampacity of a 12 AWG flexible cord with Column B thermoset insulation is **15 amperes** per CEC 2022 Table 400.5(A)(2). This value applies to two-conductor flexible cords where only two conductors are current-carrying.  

**Key Notes:**  
- **Table 400.5(A)(2)** specifically addresses flexible cords like those in Column B (e.g., SC, SCT, PPE types).  
- **No exceptions** override this ampacity for standard conditions (30°C ambient, ≤3 current-carrying conductors).  
- **Cross-references** (e.g., 310.15(B), 310.15(C)(1)) apply if temperature or bundling adjustments are needed, but these are not required for the base 15A value.  

**Prohibited Uses (from Exceptions):**  
Flexible cords must not be used as a substitute for fixed wiring (Section 400.12(1)) or in concealed locations (Section 400.12(5)), but these restrictions do not affect the ampacity calculation itself.  

---
## NEC 2023 Reference  
No difference from NEC 2023. Table 400.5(A)(2) retains the 15A rating for 12 AWG two-conductor flexible cords.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 400.12, 400.5

**Response Time:** 31.4s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire

**California Code Requirement (CEC 2022):**  
Type SF-2 silicone insulated fixture wire has a **maximum operating temperature of 200°C**, as specified in **CEC Table 402.3**. This rating applies to both solid/7-strand and flexible stranding configurations. No exceptions or amendments in CEC 2022 override this temperature limit.

**NEC 2023 Comparison:**  
NEC 2023 also specifies a **200°C maximum operating temperature** for Type SF-2 silicone insulated fixture wire (NEC Table 402.3). No differences exist between CEC 2022 and NEC 2023 for this requirement.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_lookup_table
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 402.3

**Response Time:** 40.0s

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

1. **Base Ampacity** (CEc_lookup_conductor_ampacity):  
   8 AWG copper, 75°C column = **50 amperes**  
   *Source: CEC 2022 Table 310.16*

2. **Temperature Correction** (ce_lookup_ampacity_adjustment):  
   40°C ambient, 75°C conductor = **0.88 factor**  
   *Source: CEC 2022 Table 310.15(B)(1)*

3. **Bundling Adjustment** (ce_lookup_ampacity_adjustment):  
   7 current-carrying conductors = **0.70 factor**  
   *Source: CEC 2022 Table 310.15(C)(1)*

4. **Final Calculation** (python_calculator):  
   ```python
   adjusted = 50 × 0.88 × 0.70 = 30.8 amperes
   ```

**Final Answer: 30.8 amperes**  
This adjusted ampacity accounts for both elevated ambient temperature and multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).  

**Exception Check:**  
No applicable exceptions found in cec_exception_search for base rules 310.15(B) and 310.15(C)(1). The standard derating factors apply.

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

**Response Time:** 37.5s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

### **1. Service Conductors (Phase and Neutral)**
- **Size**: **3/0 AWG copper**  
- **Ampacity**: 200A at 75°C (CEc_lookup_conductor_ampacity)  
- **Rationale**:  
  - 3/0 AWG is the smallest copper conductor meeting 200A requirement (Table 310.16).  
  - **Exceptions Checked**:  
    - **310.16 Exceptions**: No exceptions apply for standard service conductors.  
    - **230.31**: Minimum size (8 AWG) overridden by ampacity requirement.  

---

### **2. Equipment Grounding Conductor (EGC)**
- **Size**: **6 AWG copper**  
- **Reference**: CEC Table 250.122  
- **Rationale**:  
  - Required for 200A overcurrent device.  
  - **Exceptions Checked**:  
    - **250.121**: Prohibits using EGC as GEC; not applicable here.  
    - **250.122 Exceptions**: No exceptions reduce size for 200A.  

---

### **3. Grounding Electrode Conductor (GEC)**
- **Size**: **6 AWG copper**  
- **Reference**: CEC Table 250.66  
- **Rationale**:  
  - Required for 3/0 AWG service conductors.  
  - **Exceptions Checked**:  
    - **250.66(A)**: Allows 6 AWG for rod/pipe electrodes; aligns with requirement.  
    - **250.54**: Permits auxiliary electrodes but does not reduce GEC size.  

---

## **NEC 2023 Comparison**
- **Service Conductors**: Same as CEC (3/0 AWG copper for 200A).  
- **EGC**: Same as CEC (6 AWG copper for 200A).  
- **GEC**: Same as CEC (6 AWG copper for 3/0 AWG service).  

**Note**: No California-specific amendments affect these requirements.  

---

**Final Answer**:  
For a 200A residential service in California using copper:  
- **Service Conductors**: 3/0 AWG copper (200A at 75°C).  
- **EGC**: 6 AWG copper (per Table 250.122).  
- **GEC**: 6 AWG copper (per Table 250.66).  

✓ **Sources**: CEC 2022 (primary), NEC 2023 (comparison).

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 250.66, 230.31, 310.16, 250.122, 250.54, 250.121

**Response Time:** 31.3s

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
- Unit load from CEC Table 220.12: **14 VA/ft²** (includes 125% continuous load multiplier)  

**Calculation:**  
$$
\text{General Lighting Load} = 14 \, \text{VA/ft²} \times 5,000 \, \text{ft²} = 70,000 \, \text{VA}
$$

**CEC 2022 Requirements:**  
- The 125% continuous load multiplier is **already included** in the unit load value (per CEC 220.12 note).  
- No additional demand factors apply for general lighting load (per CEC 220.42 exception).  

**NEC 2023 Reference:**  
- NEC Table 220.12 also specifies **14 VA/ft²** for offices.  
- The 125% multiplier is similarly included in the unit load value.  
- **No difference** from CEC requirements.  

**Final Answer:**  
The general lighting load for the 5,000 sq ft office building is **70,000 volt-amperes**.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_lookup_table
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 21.8s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Copper in Motor Control Circuits (CEC 2022)

**CEC Requirement:**  
Per CEC 2022 Section 430.52(B), the maximum overcurrent protection for 16 AWG copper conductors in motor control circuits is **15 amperes**. This aligns with NEC 2023 Section 430.52(B)(1).  

**Key Exception (430.22(G)(2)):**  
16 AWG copper is permitted for motors with a full-load current (FLC) of **5.5A to 8A** (or ≤5.5A with Class 20 overload protection), provided:  
- Overcurrent protection complies with 240.4(D)(2)(2) (15A maximum for 16 AWG).  
- Overload protection meets 430.32 requirements.  

**NEC Comparison:**  
- **No Difference:** CEC 2022 adopts NEC 2023 requirements without amendments for this rule.  

**Final Answer:**  
- **Standard Case:** 15A maximum overcurrent protection (per 430.52(B)).  
- **Exception:** 16 AWG may be used for motors with FLC between 5.5A–8A (see 430.22(G)(2)).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 240.4, 430.32, 430.22, 430.52

**Response Time:** 24.0s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## Final Answer

**General Lighting Load for a 2,400 sq ft Dwellling Unit (CEC 2022):**  
$$
2,400 \, \text{sq ft} \times 3 \, \text{VA/sq ft} = 7,200 \, \text{VA}
$$

**CEC 2022 Basis:**  
- **Section 220.82(B)(1):** Mandates 3 VA per square foot for general lighting and general-use receptacles in dwelling units.  
- **Exceptions Checked:** No exceptions apply to this calculation (Sections 220.12, 220.85, 220.52, and 220.40 do not override the base rule for this scenario).  

---

## NEC 2023 Reference  
- **NEC 220.12(B):** Specifies the same 3 VA/sq ft requirement for dwelling units.  
- **No difference from CEC 2022.**

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 220.12, 220.82, 220.40, 220.52, 220.85

**Response Time:** 41.1s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
**California Electrical Code (CEC 2022) Requirements for Kitchen GFCI Protection:**  
- **Coverage**: GFCI protection is required for **all 125–250V receptacles in kitchens** where they serve countertop surfaces (Section 210.8(A)(6)).  
- **Exceptions**:  
  - Receptacles not readily accessible and dedicated to electric snow-melting/deicing equipment (Section 210.8(A)(3) exception).  
  - Listed locking receptacles for ceiling luminaires/fans (Section 210.8(A) exception).  
- **Additional Context**: CEC aligns with NEC 210.8 but does not expand coverage beyond countertop receptacles in kitchens.  

---

## [NEC 2023 Reference]  
**National Electrical Code (NEC 2023) Requirements for Kitchen GFCI Protection:**  
- **Coverage**:  
  - Kitchens **and areas with sinks** having permanent food prep/provisioning (Section 210.8(A)(5)).  
  - Sinks with receptacles within 1.8 m (6 ft) of the bowl (Section 210.8(A)(7)).  
  - **Buffet serving areas** with food preparation (Section 210.8(B)(4)).  
- **Exceptions**:  
  - HVAC equipment (until 2026) and dedicated circuits for specific appliances (Section 210.8(B) exceptions).  
- **Broader Scope**: NEC explicitly includes **sinks**, **buffet areas**, and **non-dwelling kitchens**, while CEC focuses only on countertop receptacles.  

---

**Which Code is More Restrictive?**  
The **NEC 2023** is more restrictive than CEC 2022 for kitchen GFCI requirements because:  
1. **NEC covers additional locations**: Sinks, buffet areas, and non-dwelling kitchens.  
2. **Fewer exceptions**: NEC allows fewer exemptions (e.g., HVAC exception expires in 2026).  
3. **Explicit sink coverage**: NEC 210.8(A)(7) mandates GFCI for sinks, which CEC does not explicitly require.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search, nec_exception_search, compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 210.8

**Response Time:** 11.9s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2 requires reserved panelboard spaces for heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers, and EV charging equipment. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Final Answer: Panelboard Space Requirements (CEC 2022 vs. NEC 2023)

---

### **1. General Panelboard Rating**  
- **CEC & NEC (Section 408.30):**  
  Panelboards must have a rating ≥ minimum feeder capacity (per Article 220).  

---

### **2. Wire-Bending Space (Section 408.55)**  
- **CEC & NEC:**  
  - **Top/Bottom Space:** Sized per **Table 312.6(B)** (CEC) or **Table 312.6(B)(2)** (NEC) for largest conductor.  
  - **Exceptions (CEC 408.55):**  
    - Panelboards ≤ 225A with ≤ 42 overcurrent devices: Use **Table 312.6(A)** for top or bottom space.  
    - If one side uses Table 312.6(B), the other side can use Table 312.6(A).  
    - Single 90° bends allow Table 312.6(A) spacing.  
    - Unused spaces can use Table 312.6(A).  

---

### **3. California-Specific Amendments (CEC 408.2(A))**  
- **CEC 2022:**  
  - **Single-Family Dwellings:** Panelboards must include **dedicated circuit breaker spaces** for:  
    - Heat pump water heaters  
    - Heat pump space heaters  
    - Electric cooktops  
    - Electric clothes dryers  
  - **Purpose:** Future-proofing for energy-efficient appliances (per California Energy Code).  

- **NEC 2023:**  
  - **No Equivalent Requirement:** No mandated spaces for these appliances.  

---

### **4. Exceptions to Panelboard Rules**  
#### **(A) Enclosure Type (Section 408.38)**  
- **CEC Exception:**  
  - Non-dead-front panelboards allowed if accessible only to qualified persons.  
- **NEC:** Requires dead-front enclosures unless exceptions apply.  

#### **(B) Overcurrent Protection (Section 408.36)**  
- **CEC Exceptions:**  
  1. Existing residential panelboards used as service equipment **do not require individual protection**.  
  2. Panelboards with two main breakers (combined rating ≤ panelboard rating) allowed, but limited to **42 overcurrent devices**.  
  3. Transformers: Primary-side protection acceptable if per 240.21(C)(1).  
- **NEC:** Similar exceptions but lacks California-specific residential provisions.  
...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 408.55, 408.38, 408.2, 312.6, 408.36, 240.21, 408.30

**Response Time:** 29.7s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## Final Answer: California (CEC 2022) vs. NEC 2023 EV Charging Requirements  

### **1. Branch Circuit Requirements**  
- **CEC 625.40**:  
  - **Mandatory individual branch circuit**: Each EV charging outlet must be on a dedicated circuit with **no other outlets**.  
  - **Exception (625.47)**: Allows **multiple feeders/branch circuits** if equipment is identified for the application (e.g., bidirectional systems).  
  - **No shared circuits** unless under 625.48 (interactive systems).  

- **NEC 625.40**:  
  - **Permits shared circuits**: Multiple EV outlets can share a circuit if total load ≤ circuit rating (e.g., 20A circuit for 12A outlets).  
  - **No exception** for multiple feeders unless specified in 625.48.  

**Key Difference**: CEC mandates stricter isolation (no shared circuits), while NEC allows shared circuits under load limits.  

---

### **2. Electrified Truck Parking (626.11)**  
- **CEC 626.11**:  
  - Requires **dedicated infrastructure** for electrified truck parking, including:  
    - Compliance with **CALGreen** (Chapter 4/5 for new construction).  
    - **Loss of power provisions** (626.26): Prevent back-feeding unless permitted by 626.27.  
  - **Scope**: Applies to external wiring systems for trucks and refrigerated units.  

- **NEC 625.40**:  
  - No specific provisions for truck parking. General EVSE requirements apply.  
  - Loss of power provisions are less detailed (focuses on standard EVSE).  

**Key Difference**: CEC includes **truck-specific rules** and integrates with CALGreen, while NEC lacks truck parking specifics.  

---

### **3. Safety and Grounding-Fault Protection**  
- **CEC 625.56**:  
  - **Mandatory GFCI protection** for all EV charging receptacles.  
  - Receptacles in wet locations must have **weatherproof enclosures**.  

- **NEC 625.56**:  
  - GFCI protection required for personnel safety (similar to CEC).  
  - **No explicit weatherproof enclosure** requirement for receptacles.  

**Key Difference**: CEC adds...

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_search, cec_exception_search, cec_exception_search
- NEC Tools: nec_search, compare_with_nec
- CEC Primary: Yes

**Citations:** 8 found
- 626.26, 626.11, 625.40, 625.56, 625.46, 625.48, 626.27, 625.47

**Response Time:** 28.0s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## **Final Answer: CEC 2022 vs. NEC 2023 AFCI Requirements for Dwellings**  

---

### **1. CEC 2022 (California) Key Exceptions**  
From **CEc_exception_search** results:  
- **Fire Alarm Systems**:  
  - **CE 210.12(A) Exception**: No AFCI required for circuits supplying fire alarm systems (760.41(B)/760.121(B)) **if installed in metal raceway, MC cable, or Type AC cable**.  
  - **NEC 2023**: Similar exception exists (210.12(E)), but **no explicit requirement for metal raceway**.  

- **Short Extensions**:  
  - **ce 210.12(D) Exception**: AFCI not required for **extensions ≤6 ft** with no new outlets (e.g., splicing devices).  
  - **NEC 2023**: No equivalent exception for short extensions.  

- **Concrete-Encased Wiring**:  
  - **ce 210.12(A)(6)**: Permits outlet AFCI at first outlet if wiring is encased in ≥2 in. concrete.  
  - **NEC 2023**: No concrete-encased wiring exception.  

- **Marking Requirements**:  
  - **ce 210.12(A)(1)-(6)**: First outlet box **must be marked** as the circuit’s first outlet.  
  - **NEC 2023**: No explicit marking requirement.  

---

### **2. NEC 2023 Key Exceptions**  
From **compare_with_nec** results:  
- **Fire Alarm Systems**:  
  - **NEC 210.12(E)**: No AFCI required for fire alarm circuits (760.41(B)/760.121(B)).  
  - **No metal raceway requirement** (unlike CEC).  

- **Industrial and Healthcare Exceptions**:  
  - **NEC 517.21**: Permits GFCI exemptions in healthcare facilities (not directly related to AFCI).  

---

### **3. Key Differences**  
| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|---------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Installation Methods**    | 6 additional methods (e.g., concrete-encased wiring, metal raceway).  ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 517.21, 760.121, 760.41, 210.12

**Response Time:** 31.6s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California (CEC 2022) vs NEC 2023 Solar PV Requirements

---

### **1. Arc-Fault Circuit Protection (DC Circuits)**  
**CEC 2022 690.11**  
- **Requirement**: PV systems with DC circuits ≥80V must use **listed PV arc-fault circuit interrupters** or equivalent.  
- **Exception**: Systems **not installed on/in buildings** (e.g., detached structures) with conductors in **metallic raceways**, **metal-clad cables**, or **underground** installations **do not require** arc-fault protection.  
- **California-Specific**: Fire mitigation plans must be documented for non-compliant systems (691.10).  

**NEC 2023**  
- **No direct equivalent** to CEC 690.11. NEC references arc-fault protection in **690.11** but lacks California’s exception for metallic raceways.  
- Focuses on **ground-fault protection** (690.5) rather than DC arc-fault specifics.  

---

### **2. Grounding-Fault Protection**  
**CEC 2022 690.41**  
- **Permitted configurations**:  
  - Ungrounded PV arrays.  
  - Solidly grounded systems with ground-fault protection.  
- **Exception**: Ungrounded systems are explicitly allowed (e.g., 690.41(A)(4)).  
- **Ground-Fault Protection**: Required for DC circuits >30V or 8A (690.41(B)).  

**NEC 2023**  
- Requires **functional grounding** for PV arrays (690.41).  
- **No explicit allowance** for ungrounded systems; NEC 250.20(B) requires grounding for AC systems but is less specific for DC.  

---

### **3. Stand-Alone Systems**  
**CEC 2022 690.10**  
- Stand-alone PV systems must comply with **Article 710** (emergency systems).  

**NEC 2023**  
- **No direct equivalent**. NEC 710 applies only to **emergency systems**, not general stand-alone PV.  

---

### **4. AC Modules**  
**CEC 2022 690.6**  
- **Exempts AC modules** from PV source circuit requirements (treated as internal components).  

**NEC 2023**  
- No specific exemption for AC modules; treated as standard inverters (690.6).  

---

### **5. Fire Mitigation Plans**  
**CEC 2022 691.10**  
- **Califor...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: nec_search, nec_search, compare_with_nec, nec_search
- CEC Primary: Yes

**Citations:** 9 found
- 690.7, 690.8, 690.11, 690.41, 690.6, 691.10, 250.20, 690.5, 690.10

**Response Time:** 54.6s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 27.7s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

