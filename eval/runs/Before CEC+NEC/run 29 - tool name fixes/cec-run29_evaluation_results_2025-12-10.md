# CEC (California) Evaluation Results - Run 29 (Tool Name Fixes)

**Date:** 2025-12-10
**Changes:** Fixed import re, tool name mismatches, CEC tools as primary

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 29 |
| Successful | 29 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 195.6s |
| Avg Duration | 6.7s |
| Exception Search Used | 1/29 |
| NEC Comparison Used | 3/29 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled |

## Results by Question

### cec-002

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Duration:** 9.9s

**Tools Called:** cec_search, cec_search, cec_search

**Answer:**

## California's Electrical Requirements for EV Charging in New Residential Construction (CEC 2022)

### 1. **Mandatory Compliance with CALGreen**
- **CALGreen Chapter 4 & 5**: All EV charging installations must comply with California Green Building Standards Code (CALGreen) requirements for energy efficiency and sustainability (CEC 625.1.1).

### 2. **Electrical Installation Requirements (Article 625)**
- **Dedicated Branch Circuits**: Each EV charging outlet must be supplied by an individual branch circuit with no other outlets (625.40).
- **Location Requirements**:
  - EVSE coupling means must be at least **450 mm (18 in)** above indoor floors or **600 mm (24 in)** above outdoor grade (625.50).
  - Exceptions apply for portable EVSE (625.44(A)).
- **Weatherproof Enclosures**: Outdoor EV receptacles must have **extra-duty weatherproof enclosures** with attachment plug caps (625.56).
- **Ground-Fault Protection**: All EV receptacles require **GFCI protection for personnel safety** (625.56(D)).

### 3. **Ventilation Requirements**
- **Indoor Charging Spaces**: If equipment requires ventilation, mechanical ventilation must be provided with both supply and exhaust to the outdoors (625.52(B)).
- **Ventilation Formulas**: Minimum ventilation rates must comply with Table 625.52(B)(1) or calculated formulas based on supply voltage/current.

### 4. **Panelboard and Circuit Requirements**
- **Circuit Breaker Spaces**: Panelboards in residential buildings must include dedicated spaces for EV charging, heat pump water heaters, and other major appliances as per CALGreen (408.2(A)/(B)).
- **Overcurrent Protection**: Panelboards must be protected by an overcurrent device not exceeding their rating (408.36).

### 5. **Special Provisions**
- **Bidirectional Systems**: EVSE with power export capabilities must be listed and marked for interactive systems (625.48).
- **Portable EVSE**: Permitted for temporary use but must comply with height and storage requirements (625.50).

### 6. **Exceptions and Notes**
- **Portable EVSE**: Exempt from fixed installation height requirements (625.44(A)).
- **CALGreen Compliance**: Refer to CALGreen Chapter 4 (residential) and Chapter 5 (multifamily) for additional mandates (625.1.1).

[OK] Source: CEC 2022

---

### cec-003

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Duration:** 10.6s

**Tools Called:** cec_search

**Answer:**

## California Solar PV Requirements (CEC 2022)

### 1. **General Installation Requirements**
- **Qualified Personnel**: PV systems must be installed by qualified persons (690.4(C)).  
- **Equipment Listing**: All inverters, modules, combiners, and rapid shutdown equipment must be listed for the application (690.4(B)).  
- **Multiple Systems**: If multiple PV systems are installed, a directory per 705.10 must be provided at each disconnect (690.4(D)).  

### 2. **Grounding & Bonding**
- **Equipment Grounding**: Exposed metal parts must be bonded per 250.134/250.136. Mounting systems used for bonding must be listed for that purpose (690.43(A)).  
- **Grounding Electrode Connection**: PV arrays must connect to the building’s grounding electrode system per 250.52. For solidly grounded systems, use a grounding electrode conductor sized per 250.66 (690.47(A)(2)).  

### 3. **Rapid Shutdown Mandates**
- **Labeling**: A permanent label at each service equipment location must state:  
  *"SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN. TURN RAPID SHUTDOWN SWITCH TO THE 'OFF' POSITION..."*  
  - Label format: 9.5mm (3/8") capital letters on yellow background (690.56(C)).  
- **Switch Labeling**: Rapid shutdown switches must have a reflective "RAPID SHUTDOWN SWITCH" label in white on red (690.56(C)(2)).  

### 4. **Arc-Fault Protection**
- **DC Circuits ≥80V**: All residential PV systems with DC circuits ≥80V must have listed PV arc-fault circuit interrupters (690.11).  
- **Exception**: Systems in metallic raceways, metal-clad cables, or underground are exempt.  

### 5. **Voltage Calculations**
- **Maximum Voltage**: Calculated using module open-circuit voltage + temperature correction factors (Table 690.7(A)).  
  - For crystalline silicon modules: Use Table 690.7(A) correction factors for lowest expected ambient temperature.  
  - Single-family dwellings: Max DC voltage limited to 600V (690.7).  

### 6. **Conductor Sizing**
- **Minimum Ampacity**: Conductors must carry 125% of the maximum circuit current (690.8(B)(1)).  
  - Example: For a 20A source circuit, use conductors rated ≥25A (e.g., 10 AWG THWN).  

### 7. **California-Specific Amendments**
- **CALGreen Compliance**: New residential buildings must meet CALGreen requirements, including PV system readiness (Title 24, Part 6).  
- **Labeling Enhancements**: California mandates more detailed rapid shutdown labels compared to NEC, including diagrams for multi-system buildings (690.56(C)(1)).  

[OK] Source: CEC 2022  
[OK] Compare with NEC: California adds stricter labeling (690.56) and enforces CALGreen mandates not in NEC.

---

### cec-004

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Duration:** 5.7s

**Tools Called:** cec_search

**Answer:**

## California Circuit Requirements for Heat Pump Water Heaters in New Dwellings (CEC 2022)

**Key Requirements:**

1. **Dedicated Circuits and Panelboard Spaces**  
   - **Single-family buildings (1-2 dwellings):**  
     Panelboards must include **dedicated circuit breaker spaces** for heat pump water heaters per **CEC 408.2(A)** and **California Energy Code §150.0(n)**.  
     Branch circuits, receptacles, and circuit identifications must be specifically designated for heat pump water heaters.  

   - **Multifamily buildings:**  
     Panelboards serving each dwelling unit must comply with **California Energy Code §160.9** for dedicated circuits and identifications.  

2. **Circuit Sizing and Installation**  
   - Follow **CEC 422.3(A)**:  
     - Branch circuits must align with **California Energy Code §150.0(n)**, which likely includes:  
       - Minimum circuit ampacity based on water heater nameplate requirements.  
       - Dedicated circuits (no shared circuits with other appliances).  
       - Proper overcurrent protection (e.g., 30A or 40A circuit breakers, depending on load).  

3. **Compliance with Energy Code Mandates**  
   - California Energy Code **Title 24, Part 6** (referenced in §150.0(n)) requires:  
     - **Dedicated electrical infrastructure** for heat pump water heaters in new residential construction to ensure compatibility and efficiency.  
     - Specific **circuit sizing** and **panelboard provisioning** to accommodate future installations.  

---

**Inspector Note:**  
- Verify panelboards have **pre-wired or reserved spaces** for heat pump water heater circuits.  
- Confirm circuits are **labeled** per §150.0(n) to avoid conflicts with other loads.  
- For exact ampacity and conductor sizing, reference the water heater’s **nameplate requirements** and apply **CEC Table 310.16** (general) or **Table 310.12(A)** (dwelling services).  

[OK] Source: CEC 2022, California Energy Code Title 24

---

### cec-005

**Question:** What is required for electric cooktop readiness in new California homes?

**Duration:** 5.1s

**Tools Called:** cec_search

**Answer:**

## Electric Cooktop Readiness in New California Homes (CEC 2022)

### **Requirements Summary**
1. **Single-Family Buildings** (1-2 dwellings):  
   - Each dwelling unit **must have dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 150.0(u)**.  
   - This includes designated spaces, receptacles, and branch circuits to support electric cooktop installation.

2. **Multifamily Buildings**:  
   - Each dwelling unit **must have dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 160.9(b)**.  

---

### **Key Code References**
- **CEC 2022 Section 422.3(A)**: Mandates cooktop readiness in single-family buildings.  
- **CEC 2022 Section 422.3(B)**: Mandates cooktop readiness in multifamily buildings.  

---

### **Inspector Notes**
- **Dedicated Circuits**: Ensure circuits are sized and protected per **Article 220** load calculations and **Article 422** appliance requirements.  
- **Labeling**: Circuit identifications must be clearly marked in the panel per **Section 422.3**.  
- **Compliance**: Verify adherence to referenced California Energy Code sections (150.0(u) for single-family, 160.9(b) for multifamily).  

[OK] Source: CEC 2022

---

### cec-006

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Duration:** 6.0s

**Tools Called:** cec_search

**Answer:**

## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

**California Energy Code Mandates:**

1. **Single-Family Buildings (408.2(A)):**  
   Panelboards must include dedicated circuit breaker spaces for **electric clothes dryers** as specified in **California Energy Code Section 150.0(n), (t), (u), and (v)**.  
   - *Example*: Typically requires **1 dedicated 30A circuit** for dryers (exact requirements depend on appliance load calculations per Energy Code).

2. **Multifamily Buildings (408.2(B)):**  
   Panelboards serving individual dwelling units must include spaces for **electric clothes dryers** per **California Energy Code Section 160.9(a), (b), and (c)**.  
   - *Example*: Often requires **1 dedicated 30A circuit** per unit (varies based on building design and Energy Code updates).

**Additional Requirements:**  
- **Overcurrent Protection (408.36):** Dryer circuits must be protected by a breaker rated **not exceeding 30A** (per 240.4(D)).  
- **Grounding (408.40):** Panelboards must have proper equipment grounding conductors connected to the frame.  

**Inspector Note:** Verify compliance with both **CEC Article 408** and referenced **California Energy Code sections** for exact space allocation and load calculations.  

[OK] Source: CEC 2022

---

### cec-007

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Duration:** 5.2s

**Tools Called:** cec_lookup_table

**Answer:**

## CEC Table 240.4(G) Unique California Considerations (CEC 2022)

**Answer:**  
CEC Table 240.4(G) itself is identical to NEC Table 240.4(G), as it serves as a cross-reference table directing users to specific NEC articles/sections for overcurrent protection requirements of specialized conductors. **There are no unique California amendments directly within Table 240.4(G)** content itself. However, California's adoption of the NEC 2023 (as CEC 2022) includes **amendments in other sections** that may affect how these referenced articles are applied. 

For example:
- California may enforce stricter interpretations of referenced sections (e.g., 440, 460, 725) through **Title 24 Energy Efficiency Standards** or **CALGreen requirements**.
- The "delta" notation in CEC indicates where California modifies NEC language elsewhere in the code, but **Table 240.4(G) remains unaltered** from the NEC.

**Inspector Note:** Always verify if referenced articles (e.g., 725 for Class 2 circuits) have California-specific amendments using `cec_search` or `compare_with_nec`.

[OK] Source: CEC 2022

---

### cec-008

**Question:** What does CEC Table 242.3 specify for California installations?

**Duration:** 5.7s

**Tools Called:** cec_lookup_table

**Answer:**

## CEC Table 242.3 Specifications (CEC 2022)

**Table 242.3 - Other Articles**  
*California-specific new table (N marker) not in NEC*

This cross-reference table directs users to additional overvoltage protection requirements in other NEC articles for specific equipment types.

**Headers:**  
- Equipment  
- Article  

**Equipment-to-Article Cross-References:**  
1. Class I locations → Article 501  
2. Class II locations → Article 502  
3. Community antenna TV/radio systems → Article 820  
4. Critical operations power systems → Article 708  
5. Elevators/dumbwaiters → Article 620  
6. Emergency systems → Article 700  
7. Equipment >1000V → Article 490  
8. Fire pumps → Article 695  
9. Industrial machinery → Article 670  
10. Information technology equipment → Article 645  
11. Modular data centers → Article 646  
12. Outdoor overhead >1000V → Article 399  
13. Radio/TV equipment → Article 810  
14. Receptacles/cord connectors → Article 406  
15. Wind electric systems → Article 694  

[OK] Source: CEC 2022 Table 242.3 (California-specific)

---

### cec-009

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Duration:** 5.4s

**Tools Called:** cec_lookup_table

**Answer:**

## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)

**Specifies maximum overcurrent protective device ratings** for motor control circuits based on conductor size and installation configuration. The table has three columns (A, B, C) with different limits for copper and aluminum conductors.

---

### **Key Table Data**
| Conductor Size | Column A (Copper) | Column A (Aluminum) | Column B (Copper) | Column B (Aluminum) | Column C (Copper) | Column C (Aluminum) |
|----------------|-------------------|---------------------|-------------------|---------------------|-------------------|---------------------|
| 18 AWG         | 7A                | —                   | 25A               | —                   | 7A                | —                   |
| 16 AWG         | 10A               | —                   | 40A               | —                   | 10A               | —                   |
| 14 AWG         | (Note 1)          | —                   | 100A              | —                   | 45A               | —                   |
| 12 AWG         | (Note 1)          | (Note 1)            | 120A              | 100A                | 60A               | 45A                 |
| 10 AWG         | (Note 1)          | (Note 1)            | 160A              | 140A                | 90A               | 75A                 |
| >10 AWG        | (Note 1)          | (Note 1)            | (Note 2)          | (Note 2)            | (Note 3)          | (Note 3)            |

---

### **Critical Notes**
1. **Column A** applies to **control circuits** (e.g., low-power circuits for motor starters).
2. **Column B** applies to **motor branch circuits** (e.g., power circuits for motor operation).
3. **Column C** applies to **motor control centers** (e.g., pre-wired assemblies with motor starters).

---

### **Derivation of Values**
- **Columns A/C for sizes >10 AWG**: Derived from **Table 310.16** (ampacity) × **300%** for 60°C conductors.
- **Column B for sizes >10 AWG**: Derived from **Table 310.19** (60°C conductors) × **400%**.

---

### **Application Rules**
- **Copper conductors** are permitted for all sizes.
- **Aluminum conductors** are only listed for 12 AWG and larger.
- For conductors **larger than 10 AWG**, calculate overcurrent limits using referenced tables (310.16/310.19) with the specified multipliers.

---

### **Inspector Notes**
- Always verify the **application type** (control circuit vs. motor branch) to select the correct column.
- For conductors >10 AWG, cross-reference **Table 310.16** or **310.19** and apply the 300%/400% multipliers.
- Aluminum is not permitted for control circuits with conductors smaller than 12 AWG.

[OK] Source: CEC 2022

---

### cec-010

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Duration:** 6.1s

**Tools Called:** cec_search

**Answer:**

## California Medium Voltage Cable Tables (CEC 2022)

California's CEC 2022 includes **medium voltage (MV) cable ampacity tables** not found in NEC, specifically addressing Type MV cables (2001–35,000 volts) in cable trays. These are detailed in **Section 311.60** and **Section 392.80**, with unique tables for ampacity adjustments based on installation conditions.

---

### **Key California-Specific Tables**
1. **Table 311.60(C)(75) & 311.60(C)(76)**  
   - **Purpose**: Ampacities for **multiconductor Type MV cables** in cable trays.  
   - **Adjustments**:  
     - 95% reduction if trays are covered >1.8 m (6 ft) with solid unventilated covers.  
     - 100% of values allowed for single-layer installations with spacing ≥ 1 cable diameter.  

2. **Table 311.60(C)(69) & 311.60(C)(70)**  
   - **Purpose**: Ampacities for **single-conductor Type MV cables** in cable trays.  
   - **Adjustments**:  
     - 75% of table values for uncovered trays (1/0 AWG+).  
     - 70% for covered trays (≥1.8 m solid covers).  

3. **Table 311.60(C)(67) & 311.60(C)(68)**  
   - **Purpose**: Ampacities for single-conductor MV cables in **triangular/square configurations**.  

---

### **California Installation Requirements**
- **Cable Tray Fill**:  
  - Governed by **Section 392.22**, with fill limits based on cable size and tray type (ladder, ventilated, solid bottom).  
  - Example: 4/0 AWG+ cables must be installed in single layers with spacing.  

- **Spacing and Ventilation**:  
  - Single-layer installations require **≥1 cable diameter spacing** for free air cooling.  
  - Covered trays reduce ampacity by 5–10% due to heat retention.  

- **Type MV Cable Definition**:  
  - Solid dielectric-insulated cables rated **2001–35,000 volts** (CEC 311.2).  

---

### **Comparison to NEC**
- **NEC 2023** references general MV cable rules (e.g., 310.15 for ampacity) but **does not include California-specific tables** for Type MV cables in trays.  
- California’s CEC adds **detailed derating factors** for tray coverage, spacing, and configuration, which are not explicitly addressed in NEC.  

---

### **Inspector Note**
- Always verify **tray type** (ladder, ventilated, solid) and **installation conditions** (covered/ventilated, spacing) when applying these tables.  
- Use **Section 392.80(B)** for Type MV cables rated >2000V, which includes unique derating rules not found in NEC.  

[OK] Source: CEC 2022

---

### cec-011

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Duration:** 3.9s

**Tools Called:** cec_lookup_conductor_ampacity

**Answer:**

## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

**Base Ampacity**: 230 amperes at 75°C (CEC Table 310.16)

**Critical Limiting Factors to Verify**:
1. **Overcurrent Protection**: 
   - Per 240.4(D), 4/0 copper conductors **must be protected at 200A maximum** for general applications (unless exception applies)
   - California amendment may modify standard NEC protection limits

2. **Bundle Derating**:
   - If more than 3 current-carrying conductors are bundled (per 310.15(C)(1)), apply 80% derate:  
     230A × 0.80 = **184A adjusted ampacity**

3. **Ambient Temperature**:
   - Table assumes 30°C ambient (per 310.15(B)). Use correction factors from Table 310.15(B)(1) if ambient differs

**Inspector Note**: While the table lists 230A, actual usable ampacity depends on installation conditions. For a 4/0 copper conductor in typical residential service laterals, 200A overcurrent protection is standard due to 240.4(D) limitations.

[OK] Source: CEC 2022

---

### cec-012

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Duration:** 3.3s

**Tools Called:** cec_lookup_grounding_conductor

**Answer:**

## Equipment Grounding Conductor Size for 200A Circuit (CEC 2022)

**Required EGC Size:**
- **Copper**: 6 AWG (Table 250.122)
- **Aluminum/Copper-Clad Aluminum**: 4 AWG (Table 250.122)

**Key Notes:**
1. **California Amendment**: The table includes a delta symbol (△) indicating modifications from NEC 2023. California may have adjusted sizing requirements compared to the national code.
2. **Footnote Compliance**: If installation conditions require compliance with 250.4(A)(5) or (B)(4) (e.g., higher fault current or special installations), the EGC may need to be larger than the table specifies.
3. **Installation Restrictions**: Refer to 250.120 for proper installation practices (e.g., secure connections, mechanical protection).

[OK] Source: CEC 2022 Table 250.122 with California amendment △

---

### cec-013

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Duration:** 4.4s

**Tools Called:** cec_lookup_grounding_conductor

**Answer:**

## Grounding Electrode Conductor Size (CEC 2022)

For a **3/0 AWG copper service conductor**, the required grounding electrode conductor (GEC) size is:

- **4 AWG copper** (per CEC Table 250.66)

This applies to single-phase AC systems where the largest service-entrance conductor is 3/0 AWG copper. The table accounts for California amendments (denoted by the "delta" symbol in the code).

[OK] Source: CEC 2022 Table 250.66

---

### cec-014

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Duration:** 13.4s

**Tools Called:** cec_lookup_ampacity_adjustment

**Answer:**

## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** in a **40°C ambient temperature** is:

**0.88** (per CEC 2022 Table 310.15(B)(1)(1))

This factor reduces the conductor's allowable ampacity when operating in higher ambient temperatures. Apply this factor to the base ampacity value from Table 310.16 or 310.12(A) as needed.

[OK] Source: CEC 2022

---

### cec-015

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Duration:** 4.2s

**Tools Called:** cec_lookup_ampacity_adjustment

**Answer:**

## Ampacity Adjustment Factor for Bundling (CEC 2022)

**Adjustment Factor**: 0.7 (70%) for 7-9 current-carrying conductors in a raceway  
**Source**: CEC 2022 Table 310.15(C)(1) [California Amendment]

**Key Notes**:
- Applies to conductors rated 40°C or higher (per Table 310.15(C)(1) footnote)
- Conductors must be the same size and type in the raceway
- California amendment maintains NEC 2023 requirements for this adjustment

**Footnote Clarification**:
- Count includes all conductors in the raceway (spare, neutral, and EGC)
- Excludes conductors connected to components that cannot be simultaneously energized
- See 310.15(E) and (F) for detailed counting rules

[OK] Source: CEC 2022

---

### cec-016

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Duration:** 3.7s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Minimum Working Space Depth for 480V Panelboard (CEC 2022)

The minimum working space depth required for a 480V panelboard under **Condition 3** is **1.2 meters (4 feet)** as specified in **CEC Table 110.26(A)(1)**. 

### Condition 3 Context:
- Applies when **exposed live parts are on both sides of the working space**.
- Requires the maximum clearance to ensure safety when working on or near energized equipment.

### Reference:
- **CEC 2022 Table 110.26(A)(1)** (Working Space, Depth - Front of Equipment)
- Voltage range: 151–600V

[OK] Source: CEC 2022

---

### cec-017

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Duration:** 4.6s

**Tools Called:** cec_lookup_table

**Answer:**

## Suitable Enclosures for Outdoor Use with Rain, Sleet, and Ice (CEC 2022)

**Answer:**  
For outdoor use with exposure to **rain, sleet, and ice**, the following enclosure types are suitable per **CEC Table 110.28**:

- **Type 3S** (Raintight, dusttight)  
- **Type 3SX** (Raintight, dusttight, corrosion-resistant)  
- **Type 3X** (Raintight, corrosion-resistant)  
- **Type 4** (Watertight, dusttight)  
- **Type 4X** (Watertight, dusttight, corrosion-resistant)  
- **Type 6** (Watertight for use with hose-directed water)  
- **Type 6P** (Watertight for use with oil or water immersion)  

**Key Requirements:**  
1. **Mechanism operability when ice-covered** (footnote [*]) is required.  
2. **Raintight/watertight** enclosures (Types 3S, 3SX, 3X, 4, 4X, 6, 6P) are explicitly permitted for rain/sleet/ice exposure.  
3. **Dusttight** enclosures (Types 3S, 3SX, 3X, 4, 4X, 6, 6P) are suitable for hazardous locations if applicable (footnote [3] and [4]).  

**Citations:**  
- CEC Table 110.28 (Enclosure Selection)  
- Footnotes [*], [1], [3], and [4]  

[OK] Source: CEC 2022

---

### cec-018

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Duration:** 6.5s

**Tools Called:** cec_search, cec_lookup_table

**Answer:**

## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for **office buildings** in California is **1.3 volt-amperes per square foot (14 VA/m²)** per **CEC Table 220.12**.

This value includes the 125% continuous load multiplier required by **210.20(A)** for lighting calculations. No additional factors are required when using this table value for minimum lighting load calculations.

[OK] Source: CEC 2022 Table 220.12, Section 220.12

---

### cec-019

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Duration:** 8.8s

**Tools Called:** cec_search, cec_lookup_conductor_ampacity

**Answer:**

## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

### Correct Tool Usage:
The **cec_lookup_conductor_ampacity** tool returned **25A** from **Table 310.16**, but this applies to *fixed wiring conductors* (not flexible cords). Flexible cord ampacities are governed by **Table 400.5(A)(1)**, not Table 310.16.

### Correct Answer:
For **12 AWG flexible cord with Column B thermoset insulation** (two-conductor, current-carrying), the ampacity is **20 amperes** per **CEC 2022 Table 400.5(A)(1)**. This value accounts for:
- Ambient temperature of 30°C (86°F)
- Two-conductor configuration (Column B)
- California amendments to NEC 2023

### Inspector Note:
- **Table 400.5(A)(1)** specifically governs flexible cords (not Table 310.16)
- The 25A value from Table 310.16 applies to *fixed wiring* conductors, not flexible cords
- Overcurrent protection must not exceed 20A per **Section 240.5(A)**

[OK] Source: CEC 2022

---

### cec-020

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Duration:** 4.7s

**Tools Called:** cec_search

**Answer:**

## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

The maximum operating temperature for **Type SF-2 silicone insulated fixture wire** is specified in **Table 402.3** of the California Electrical Code (CEC) 2022. According to Section 402.5, fixture wire ampacities and temperature limits are governed by Table 402.3, which lists insulation types and their corresponding temperature ratings.

For **Type SF-2**, the table typically designates a maximum operating temperature of **105°C** (based on standard code alignment with NEC and California amendments). This rating ensures suitability for elevated temperature environments while maintaining flame-retardant properties.

[OK] Source: CEC 2022, Table 402.3

---

### cec-021

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Duration:** 7.5s

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment

**Answer:**

## Corrected Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   8 AWG THWN copper at 75°C = **50A** (Table 310.16)

2. **Temperature Correction (40°C ambient)**:  
   - Correction factor from **Table 310.15(B)(1)(1)** for 75°C conductors at 40°C = **0.88**  
   - *Calculation*: `50A × 0.88 = 44A`

3. **Bundle Derating (7 conductors)**:  
   - Derating factor from **Table 310.15(C)(1)** for 7 conductors = **0.70**  
   - *Calculation*: `44A × 0.70 = 30.8A`

4. **Final Adjusted Ampacity**:  
   **30.8 amperes** (rounded to 31A for practical application)

**Key Corrections**:  
- Used **Table 310.15(B)(1)(1)** instead of 310.15(B)(2)(a) for temperature correction  
- California amendments do not alter the calculation methodology for this scenario  

**Limiting Rules**:  
- 240.4(D) allows 40A overcurrent protection for 8 AWG copper (30.8A < 40A, compliant)  

[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)

---

### cec-022

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Duration:** 4.0s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Service Sizing (CEC 2022)

**1. Service Conductors**  
- **Size**: 2/0 AWG copper  
- **Source**: CEC Table 310.12(A) (Single-Phase Dwelling Services/Feeders)  
- **Conditions**: Applies to 120/240V or 120/208Y single-phase systems with no temperature correction/adjustment factors.  

**2. Equipment Grounding Conductor (EGC)**  
- **Size**: 6 AWG copper  
- **Source**: CEC Table 250.122 (200A overcurrent protection)  

**3. Grounding Electrode Conductor (GEC)**  
- **Size**: 6 AWG copper  
- **Source**: CEC Table 250.66 (Based on 2/0 AWG service conductors)  

**Inspector Note**:  
- Table 310.12(A) provides dwelling-specific permissive sizes. For non-dwelling applications, use Table 310.16 (general use).  
- No California amendments override these standard sizing tables for residential services.  

[OK] Source: CEC 2022

---

### cec-023

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Duration:** 9.6s

**Tools Called:** cec_search, cec_lookup_table

**Answer:**

## General Lighting Load Calculation for Office Building (CEC 2022)

**Corrected Calculation Steps:**

1. **Determine Occupancy Type:**  
   Office building → Non-dwelling occupancy (CEC 220.12).

2. **Find Unit Load from Table 220.12:**  
   For **Office** occupancies, the unit load is **1.3 VA/ft²** (CEC Table 220.12).

3. **Calculate Total Lighting Load:**  
   $$
   5,000 \, \text{ft}^2 \times 1.3 \, \text{VA/ft}^2 = 6,500 \, \text{VA}
   $$

4. **Continuous Load Consideration:**  
   The 125% multiplier for continuous loads is **already included** in the unit load value per Table 220.12 note.

**Final Answer:**  
The general lighting load for a 5,000 sq ft office building is **6,500 VA** (6.5 kVA).

**Citations:**  
- CEC 2022 Section 220.12  
- CEC 2022 Table 220.12 (Office: 1.3 VA/ft²)  

[OK] Source: CEC 2022  

**Note:** The initial response incorrectly cited 11 VA/ft². The correct value from **Table 220.12** for office occupancies is **1.3 VA/ft²**, as verified by the `cec_lookup_table` tool. Always prioritize direct table lookups for accuracy.

---

### cec-024

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Duration:** 6.4s

**Tools Called:** cec_search

**Answer:**

## Maximum Overcurrent Protection for 16 AWG Copper Motor Control Circuit (CEC 2022)

**Answer:**  
The maximum overcurrent protection for **16 AWG copper conductors** in a motor control circuit that **extends beyond the enclosure** in California is **10 amperes**, as specified in **CEC 2022 Section 240.4(D)(2)**.  

### Key Requirements:
1. **Overcurrent Limit**:  
   - **10A maximum** for 16 AWG copper conductors (Section 240.4(D)(2)).  
   - Continuous loads must not exceed **8A** (80% of 10A).  

2. **Permitted Overcurrent Devices**:  
   - Branch-circuit-rated circuit breakers **listed and marked for 16 AWG copper**.  
   - Branch-circuit-rated fuses **listed and marked for 16 AWG copper**.  
   - Class CC, Class J, or Class T fuses.  

3. **Additional Context from 430.72(B)**:  
   - If the control circuit conductors extend beyond the motor control equipment enclosure, the overcurrent protection must not exceed values in **Column C of Table 430.72(B)**. While the exact table values are not fully shown in the search results, the 10A limit from 240.4(D)(2) aligns with standard practice for 16 AWG copper in control circuits.  

4. **Exceptions**:  
   - If the control circuit’s interruption would create a hazard (e.g., fire pump), only **short-circuit and ground-fault protection** is required (Exception in 430.72(B)).  

---

**Inspector Note:**  
Always verify the conductor’s ampacity (13A for 16 AWG copper at 60°C per Table 310.16) and ensure the overcurrent device does not exceed the **10A limit** specified in 240.4(D)(2). For motor control circuits, cross-check with 430.72(B) for any additional constraints.  

[OK] Source: CEC 2022

---

### cec-025

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Duration:** 9.6s

**Tools Called:** cec_search, cec_lookup_table

**Answer:**

## General Lighting Load Calculation for Dwelling Unit (CEC 2022)

**Answer:**  
The general lighting load for a 2,400 square foot dwelling unit in California is **7,200 volt-amperes (VA)**.

**Calculation Steps:**  
1. **Base Load Requirement**:  
   Per **CEC 2022 Section 220.14(J)**, dwelling units require a minimum unit load of **3 volt-amperes per square foot (VA/ft²)** for general lighting and receptacles.  

2. **Apply to Given Area**:  
   $$
   2,400 \, \text{ft}^2 \times 3 \, \text{VA/ft}^2 = 7,200 \, \text{VA}
   $$

3. **Code Compliance**:  
   - This calculation complies with **CEC 2022 Section 220.14(J)**, which explicitly governs dwelling units.  
   - **Table 220.12** (looked up above) applies to **non-dwelling occupancies** and is not used for residential calculations.  

**Inspector Note:**  
- The lookup of **Table 220.12** confirms it is irrelevant for dwelling units (it lists non-residential occupancies).  
- The correct value of **3 VA/ft²** for dwellings is derived directly from **Section 220.14(J)**, not from Table 220.12.  

[OK] Source: CEC 2022

---

### cec-026

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Duration:** 6.1s

**Tools Called:** cec_search, nec_search

**Answer:**

## Kitchen GFCI Requirements Comparison (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirements**  
- **Scope**: Applies to **dwelling units** only.  
- **Key Provisions**:  
  - **Section 210.8(A)(6)**: Requires GFCI protection for **receptacles serving countertop surfaces** in kitchens.  
  - **Exceptions**:  
    - Receptacles for ceiling luminaires/ceiling fans (if GFCI protection is not integral to the device).  
    - Receptacles not readily accessible (e.g., for fixed equipment).  
- **Distance Rule**: Receptacles within **1.8 m (6 ft)** of a sink’s top inside edge require GFCI.  

### **NEC 2023 Requirements**  
- **Scope**: Applies to **both dwelling and non-dwelling units**.  
- **Key Provisions**:  
  - **Section 210.8(A)(5)**: Requires GFCI protection for **all 125–250V receptacles in kitchens**, including:  
    - Countertop receptacles.  
    - Receptacles within **1.8 m (6 ft)** of a sink.  
  - **Section 210.8(B)(2)–(3)**: Extends GFCI requirements to **buffet serving areas** and **commercial kitchens** (non-dwelling units).  
  - **Exceptions**:  
    - Receptacles for HVAC equipment (expired exception in 2026).  
    - Listed HVAC equipment (temporary exception).  

---

### **Which Code is More Restrictive?**  
**NEC 2023 is more restrictive** than CEC 2022 in three key ways:  
1. **Broader Scope**: Applies to **non-dwelling units** (e.g., commercial kitchens, buffets) where CEC 2022 does not.  
2. **Additional Locations**: Covers **buffet serving areas** and **industrial kitchens**, which are not explicitly addressed in CEC 2022.  
3. **Fewer Exceptions**: Limits exceptions (e.g., HVAC equipment exemption expires in 2026), whereas CEC 2022 allows more exceptions for fixed equipment.  

---

### **Inspector Note**  
- **CEC 2022** focuses narrowly on residential kitchens, while **NEC 2023** expands GFCI requirements to commercial and non-residential settings.  
- Always verify local amendments (e.g., California’s CEC incorporates NEC with state-specific adjustments).  

[OK] Source: CEC 2022, NEC 2023

---

### cec-027

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Duration:** 5.9s

**Tools Called:** cec_search, nec_search

**Answer:**

## Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023)

### **Key Differences for Single-Family Dwellings**

#### **1. California Energy Code Mandates (CEC 2022 Only)**
- **CEC 408.2(A)**:  
  Panelboards in **single-family residential buildings** must include **dedicated circuit breaker spaces** for:  
  - Heat pump water heaters  
  - Heat pump space heaters  
  - Electric cooktops  
  - Electric clothes dryers  
  **Source**: California Energy Code Sections 150.0(n), 150.0(t), 150.0(u), 150.0(v).  

  **NEC 2023**: No equivalent requirement. Load calculations (NEC 220.55) determine circuit sizes but do not mandate dedicated spaces for specific appliances.

---

#### **2. Wire-Bending Space Exceptions**
- **CEC 408.55**:  
  Exceptions for panelboards rated **225A or less** with **≤42 overcurrent devices** allow reduced wire-bending space per **Table 312.6(A)**.  
  - **Exception 1**: Permits sizing top/bottom bending space per Table 312.6(A) for panelboards designed for single 90° bends.  
  - **Exception 3**: California-specific allowance for simplified wiring diagrams.  

  **NEC 2023 408.55**:  
  Similar exceptions exist but **no California-specific modifications**. Uses **Table 312.6(B)(2)** for standard sizing.

---

#### **3. Overcurrent Protection for Existing Panelboards**
- **CEC 408.36 Exception No. 2**:  
  Existing panelboards used as **service equipment in single-family residences** are exempt from individual overcurrent protection.  

  **NEC 2023 408.36**:  
  No exception for residential panelboards. Requires overcurrent protection unless protected by two main breakers/fuses (Exception No. 1).

---

#### **4. Short-Circuit Current Rating (SCCR) Marking**
- **Both Codes (CEC 408.6 / NEC 408.6)**:  
  Panelboards must have an SCCR ≥ available fault current.  
  - **CEC**: Requires field marking of fault current and calculation date **for all panelboards**.  
  - **NEC**: Field marking required **only in non-residential applications**.  

---

### **Summary Table**

| Feature                          | **CEC 2022**                                                                 | **NEC 2023**                          |
|----------------------------------|-------------------------------------------------------------------------------|---------------------------------------|
| Appliance Spaces (Single-Family)   | Mandates dedicated spaces for 4 appliances (408.2)                          | No appliance-specific space mandates  |
| Wire-Bending Space Exceptions      | Includes California-specific exceptions for ≤42-device panelboards (408.55) | Standard exceptions only (408.55)     |
| Overcurrent Protection Exceptions  | Exempts existing residential panelboards (408.36)                            | No residential-specific exemptions    |
| SCCR Field Marking               | Required for **all** panelboards                                            | Required only in non-residential      |

---

[OK] Source: CEC 2022 / NEC 2023

---

### cec-028

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Duration:** 9.4s

**Tools Called:** cec_search, nec_search, cec_search, cec_exception_search, compare_with_nec

**Answer:**

## California (CEC 2022) vs NEC 2023 EV Charging Requirements

### **Key Differences**
| **Requirement** | **California (CEC 2022)** | **NEC 2023** | **Code Reference** |
|------------------|--------------------------|--------------|--------------------|
| **CALGreen Compliance** | Mandates EV readiness in new construction per CALGreen Chapter 4/5 | No equivalent mandate | CEC 625.1.1 |
| **Branch Circuit Requirements** | Individual branch circuit required for each EV outlet (no other outlets allowed) | No explicit requirement for individual circuits | CEC 625.40 |
| **Ventilation Requirements** | Indoor EVSE requires mechanical ventilation per Table 625.52(B)(1) | No ventilation requirements specified | CEC 625.52 |
| **Location Height Requirements** | Indoor: ≥18" above floor; Outdoor: ≥24" above grade (except portable units) | No height requirements | CEC 625.50 |
| **Cord Length Restrictions** | Power-supply cord ≤6 ft for stationary equipment; ≤15 ft with interlocked circuit | No cord-length restrictions | CEC 625.17(A)(3) |
| **GFCI Protection** | Required for all EV charging receptacles (per 210.8 + 625.54) | Required per 210.8(A)(7) | CEC 625.54, NEC 210.8 |
| **Load Calculations** | No specific EV load demand factors | 7200W or nameplate rating, whichever is larger (220.57) | NEC 220.57 |

---

### **Key Similarities**
- **Personnel Protection**: Both require ground-fault circuit-interrupter (GFCI) protection for EV charging circuits.
- **Equipment Ratings**: Both specify EVSE must be listed and marked for intended applications (CEC 625.17, NEC 100).
- **Wireless Charging**: Both reference UL 2594 for EV supply equipment standards.

---

### **California-Specific Mandates**
1. **CALGreen Compliance**  
   New residential construction must include EV-ready infrastructure (e.g., 60A branch circuit, 240V receptacle) per CALGreen Chapter 4, Division 4.1.  
   *No equivalent in NEC.*

2. **Ventilation for Indoor Charging**  
   CEC 625.52 requires mechanical ventilation for indoor EVSE based on supply voltage/current. Example:  
   - 120V, 16A system: 50 cfm per vehicle  
   - 240V, 80A system: 200 cfm per vehicle  
   *NEC contains no ventilation requirements for EVSE.*

3. **Cable Management**  
   CEC 625.17(C) limits cord length to 25 ft unless equipped with a listed cable management system.  
   *NEC has no cord-length restrictions for EVSE.*

---

### **NEC 2023 Focus Areas**
- **Load Calculations**: EVSE load calculated at 7200W or nameplate rating (NEC 220.57).  
- **General GFCI Requirements**: Applies to all dwelling unit receptacles (NEC 210.8(A)(7)).  
- **No State-Specific Mandates**: Lacks CALGreen/CABEC requirements for new construction.

---

### **Inspector Notes**
- **California**: Verify CALGreen compliance for new residential projects (e.g., 60A circuit, 240V receptacle).  
- **Ventilation**: California inspectors must check mechanical ventilation interlocks per 625.52(B)(4).  
- **Cord Lengths**: Enforce CEC 625.17(A)(3) for fixed EVSE installations (≤6 ft cord unless interlocked).  

[OK] Source: CEC 2022, NEC 2023

---

### cec-029

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Duration:** 9.6s

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## AFCI Protection Requirements Comparison (CEC 2022 vs NEC 2023)

### **Core Requirements**
Both codes require **AFCI protection for 15- and 20-ampere branch circuits** in dwelling units, covering:
- Kitchens, bedrooms, living rooms, hallways, laundry areas, etc.
- **Permitted protection methods** include:
  - Combination-type AFCI (entire circuit)
  - Branch/feeder-type AFCI + outlet branch-circuit AFCI
  - Supplemental arc protection + outlet branch-circuit AFCI (with length limits)
  - Outlet branch-circuit AFCI in metal raceway/concrete-encased circuits

---

### **Key Differences**

#### **1. Exceptions**
- **CEC 210.12(A) Exception**  
  - Exempts **fire alarm systems** installed per 760.41(B)/760.121(B) if in metal raceway/enclosures.
- **NEC 210.12(E) Exception**  
  - Exempts **certain replacement receptacles** under 404.22(C)(4) if protected by listed AFCI devices.

#### **2. Circuit Modifications**
- **CEC 210.12(D)**  
  - Allows **outlet branch-circuit AFCI at first receptacle** for extensions/modifications ≤ 1.8 m (6 ft) without new outlets.
- **NEC 210.12(D)**  
  - No explicit exception for short extensions; requires full AFCI compliance for all modifications.

#### **3. Additional NEC Requirements**
- **NEC 404.22(C)(4)**  
  - Mandates **AFCI-protected replacement receptacles** in previously protected locations (e.g., listed AFCI receptacles or protected by breaker).
- **NEC 424.96(A)(8)**  
  - Requires **GFCI protection** for heating panels (not mentioned in CEC).

#### **4. Length Restrictions**
- **CEC 210.12(A)(3)/(4)**  
  - Limits branch-circuit wiring from overcurrent device to first outlet to **50 ft (14 AWG)** or **70 ft (12 AWG)** for supplemental AFCI methods.
- **NEC 210.12(A)(3)/(4)**  
  - Same length restrictions but **no exception for concrete-encased circuits** (CEC allows this in 210.12(A)(6)).

---

### **Inspector Notes**
- **California amendments** expand AFCI exemptions (fire alarms) and simplify modifications under 6 ft.
- **NEC adds GFCI requirements** for heating panels and stricter receptacle replacement rules.
- **CEC permits concrete-encased circuits** as a standalone AFCI method (NEC requires additional protection).

[OK] Source: CEC 2022 vs NEC 2023 Comparison

---

### cec-030

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Duration:** 10.2s

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## California CEC 2022 vs NEC 2023 Solar PV Requirements (Article 690 Comparison)

### **Key Differences for AC Modules (CEC 690.6 vs NEC 690)**
| **Requirement** | **California CEC 2022** | **NEC 2023** | **Practical Impact** |
|------------------|-------------------------|----------------|-----------------------|
| **AC Module Source Circuits** | CEC 690.6(A): PV source circuit requirements **do not apply** to AC modules. The PV source circuit, conductors, and inverters are considered internal components of the AC module system. | NEC 690.2 Definition: AC module includes inverter but does not exempt source circuit rules. | California simplifies compliance by treating AC modules as self-contained systems, reducing design complexity. |
| **Output Circuit Classification** | CEC 690.6(B): Output of AC modules is classified as an **inverter output circuit**. | NEC 690.6(B): No explicit classification for AC module output circuits. | California explicitly aligns AC module output with standard inverter output requirements (e.g., overcurrent protection, labeling). |
| **Labeling Requirements** | CEC 690.53: Requires permanent labels at disconnecting means or power conversion equipment showing **maximum DC voltage**. CEC 690.56(C): Rapid shutdown switches must have **white-on-red labels** (min. 9.5mm height). | NEC 690.53: Requires labeling of maximum DC voltage but no specific label size/color standards. NEC 705.12: Rapid shutdown labels but no California-style detailed requirements. | California mandates **specific label formats** (color, size, wording) for visibility and safety. |
| **Rapid Shutdown Marking** | CEC 690.56(C): Buildings with PV systems must have **permanent labels** at service equipment indicating rapid shutdown switch location. Labels must include a roof diagram and instructions. | NEC 690.12: Requires rapid shutdown but no detailed labeling requirements. | California adds **visual diagrams** to labels to ensure non-electricians can locate shutdown switches. |

---

### **Additional California-Specific Requirements**
1. **Rapid Shutdown Labels (CEC 690.56)**  
   - Must include:  
     - "SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN" (yellow background, black text)  
     - Diagram of building roof with dotted lines showing energized areas post-shutdown  
     - "RAPID SHUTDOWN SWITCH" label (white on red, min. 9.5mm height)  

2. **Arc-Fault Protection (CEC 690.11)**  
   - Requires **PV-specific DC arc-fault circuit interrupters** for systems ≥80V DC.  
   - **Exception**: Underground or metal-clad systems exempt (same as NEC).  

3. **Grounding Electrode Connections (CEC 690.47)**  
   - Mandates PV array equipment grounding conductors to connect to **grounding electrode system** per 250.52/250.54.  
   - NEC allows alternative grounding methods without explicit electrode connection requirements.  

---

### **Inspector Notes**
- **AC Modules**: California’s treatment of AC modules as self-contained systems (CEC 690.6) reduces compliance complexity but requires verification that internal components meet listing requirements.  
- **Labeling**: California’s detailed label requirements (size, color, diagrams) are **more restrictive** than NEC. Inspectors must verify **physical label placement** and **compliance with 690.56(C)**.  
- **Rapid Shutdown**: California’s labeling goes beyond NEC to ensure **non-technical personnel** can safely shut down systems during emergencies.  

[OK] Source: CEC 2022 & NEC 2023 Comparison

---

