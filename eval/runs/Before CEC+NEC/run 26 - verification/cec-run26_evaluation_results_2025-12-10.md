# CEC 2022 (California) Evaluation Results - Run 26

**Date:** 2025-12-10
**Changes:** Memory clearing + Tool enforcement

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 29 |
| Successful | 29 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 190.7s |
| Avg Duration | 6.6s |
| Exception Search Used | 0/29 |
| NEC Comparison Used | 2/29 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled |

## Results by Question

### cec-002

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Duration:** 14.2s

**Tools Called:** cec_search

**Answer:**

## California EV Charging Requirements (CEC 2022)

### 1. **CALGreen Compliance**  
New residential construction must comply with **CALGreen Chapter 4 and 5** (CEC 625.1). This includes:  
- **EV-ready infrastructure**: Reserved parking spaces with electrical capacity for EV charging.  
- **Title 24 Part 6** mandates: Minimum 40-amp circuit per EV space, conduit to parking areas, and panelboard capacity.  

---

### 2. **Dedicated Branch Circuits**  
- **625.40**: Each EV charging outlet must have an **individual branch circuit** with no other outlets.  
- **625.42**: Circuits must be sized for **continuous loads** (125% of nameplate rating).  

---

### 3. **Ground-Fault Protection**  
- **625.54**: All EV receptacles must have **GFCI protection for personnel** (per 210.8 + 625.54).  
- **625.60(D)**: GFCI reset/indication must be **readily accessible**.  

---

### 4. **Weatherproof Enclosures**  
- **625.56**: Receptacles in wet locations (e.g., garages) require **weatherproof enclosures** with extra-duty ratings.  

---

### 5. **Cable and Cord Requirements**  
- **625.17**: Power-supply cords must be:  
  - **Hard service cord** (e.g., SJOOW) or listed EV-specific cables (Type EV/EVJ).  
  - **Max length**: 15 ft (4.6 m) unless using a listed cable management system.  

---

### 6. **Ventilation**  
- **625.52**: Indoor charging requires mechanical ventilation if equipment is not listed for indoor use.  
  - Ventilation rates depend on EV count and power (Tables 625.52(B)(1)(a/b)).  

---

### 7. **Overcurrent Protection**  
- **625.42**: Fixed-in-place equipment must have **restricted access** to adjustment settings (tool/lock/password-protected).  

---

### 8. **Power Export Systems**  
- **625.48**: Bidirectional EVSE (vehicle-to-grid) must comply with **Article 705** for interconnection.  

---

### Key References  
- **CALGreen/Title 24**: Mandates for new residential construction.  
- **CEC 2022 Sections**: 625.1, 625.40, 625.54, 625.56, 625.17, 625.52.  

[OK] Source: CEC 2022

---

### cec-003

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Duration:** 7.8s

**Tools Called:** cec_search

**Answer:**

## California-Specific Solar PV Requirements (CEC 2022)

### 1. **Rapid Shutdown Labeling** [CEC 690.56(C)]
- **Mandatory labels** for PV systems with rapid shutdown:
  - **Label location**: At each service equipment location or visible location.
  - **Label content**: 
    ```
    SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN
    TURN RAPID SHUTDOWN SWITCH TO THE 'OFF' POSITION TO SHUT DOWN PV SYSTEM AND REDUCE SHOCK HAZARD IN THE ARRAY.
    ```
  - **Label size**: 
    - Title: 9.5 mm (3/8 in.) height, black on yellow.
    - Remaining text: 4.8 mm (3/16 in.) height, black on white.
  - **Rapid shutdown switch label**: "RAPID SHUTDOWN SWITCH FOR SOLAR PV SYSTEM" in white on red, reflective, ≥9.5 mm height.

### 2. **Ground-Fault Protection** [CEC 690.41(B)]
- **DC ground-fault protection** required for PV systems exceeding 30V or 8A.
- **Exceptions**: 
  - Solidly grounded PV source circuits with ≤2 modules in parallel and not on/in buildings.
  - Equipment without integral GFDI must include listed ground-fault protection.

### 3. **Equipment Grounding and Bonding** [CEC 690.43]
- **Bonding requirements**:
  - PV module frames and support structures must use **listed bonding devices**.
  - Metallic support structures require **identified bonding jumpers** between sections.
  - Equipment grounding conductors must be in the **same raceway/cable** as PV conductors.

### 4. **Wiring Methods** [CEC 690.31]
- **DC circuits >30V/8A** must use:
  - Metal raceways, Type MC cable, or metal enclosures.
  - **Exposed DC circuits** must be marked "SOLAR PV DC CIRCUIT" with red/white labels ≥9.5 mm height.
- **Flexible cords** for tracking arrays must be **hard-service, UV-resistant, and listed for outdoor use**.

### 5. **Grounding Electrode System** [CEC 690.47]
- **PV array grounding** must connect to the building's grounding electrode system per Article 250.
- **Grounding electrode conductor** sized per Table 250.66.
- **Metal building frames** can serve as grounding electrodes if meeting 250.68(C)(2).

### 6. **Bipolar Systems** [CEC 690.31(E)]
- **Physical separation** required for monopole circuits in bipolar systems.
- **Warning labels** for solidly grounded bipolar systems: "Disconnection of grounded conductors may cause overvoltage."

### 7. **California Mandates (Title 24/CALGreen)**
- **Title 24 Part 6** (Residential Energy Efficiency Standards):
  - Requires **solar-ready roofs** for new residential construction.
  - Minimum solar panel orientation and roof access requirements.
- **CALGreen**:
  - Mandates **renewable energy systems** for new homes (≥1.5% of annual electricity use).

### 8. **Interconnection Standards** [CEC 690.59]
- Compliance with **Article 705** (Energy Systems) and **Article 712** (Grid-Connected Systems) for utility interconnection.

---

[OK] Source: CEC 2022

---

### cec-004

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Duration:** 6.5s

**Tools Called:** cec_search

**Answer:**

## California Circuit Requirements for Heat Pump Water Heaters (CEC 2022)

### **Single-Family Residential Buildings**  
Per **CEC 422.3(A)** and **408.2(A)**:  
- **Dedicated circuits and panelboard spaces** must be provided for heat pump water heaters.  
- Requirements are specified in **California Energy Code Section 150.0(n)**, which mandates:  
  - **Branch circuits** with designated spaces, receptacles, and circuit identifications.  
  - Panelboards must include dedicated circuit breaker spaces for heat pump water heaters.  

### **Multifamily Buildings**  
Per **CEC 422.3(B)** and **408.2(B)**:  
- **Dedicated circuits and panelboard spaces** are required as per **California Energy Code Section 160.9(b)**.  
  - Multifamily panelboards must reserve spaces for heat pump water heaters in individual dwelling units.  

### **Key Code References**  
- **CEC 422.3(A)**: Links to Energy Code 150.0(n) for single-family requirements.  
- **CEC 408.2(A)**: Panelboard spaces for single-family heat pump water heaters.  
- **CEC 422.3(B)**: Multifamily compliance via Energy Code 160.9(b).  

### **Purpose**  
These requirements ensure electrical infrastructure is pre-wired to support heat pump water heaters, aligning with California’s energy efficiency mandates (e.g., Title 24). Specific circuit details (ampacity, voltage) are defined in the referenced Energy Code sections.  

[OK] Source: CEC 2022

---

### cec-005

**Question:** What is required for electric cooktop readiness in new California homes?

**Duration:** 5.1s

**Tools Called:** cec_search

**Answer:**

## Electric Cooktop Readiness in New California Homes (CEC 2022)

### **Requirements for Single-Family Buildings**  
Per **CEC 2022 Section 422.3(A)**:  
Each dwelling unit in single-family buildings (1–2 dwellings) must have:  
- **Dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 150.0(u)**.  

### **Requirements for Multifamily Buildings**  
Per **CEC 2022 Section 422.3(B)**:  
Each dwelling unit in multifamily buildings must have:  
- **Dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 160.9(b)**.  

### **Key Implications**  
1. **Dedicated Circuits**: Cooktops must have their own dedicated branch circuits (not shared with other appliances).  
2. **Circuit Identification**: Panels must clearly label these circuits for easy identification.  
3. **Compliance with Energy Code**: Specific details (e.g., circuit amperage, receptacle type) are defined in the referenced California Energy Code sections.  

[OK] Source: CEC 2022

---

### cec-006

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Duration:** 5.0s

**Tools Called:** cec_search

**Answer:**

## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

In California new construction, panelboards must include **reserved circuit breaker spaces** for electric clothes dryers as mandated by **CEC 2022 Section 408.2**:

1. **Single-Family Buildings** (408.2(A)):  
   Panelboards serving individual dwelling units must provide **reserved spaces** for electric clothes dryers, along with heat pump water heaters, heat pump space heaters, and electric cooktops. This requirement aligns with **California Energy Code Section 150.0(n), (t), (u), and (v)**.

2. **Multifamily Buildings** (408.2(B)):  
   Similar requirements apply for multifamily buildings, with reserved spaces for electric clothes dryers, heat pump space heaters, and electric cooktops per **California Energy Code Section 160.9(a), (b), and (c)**.

### Key Details:
- **Purpose**: Ensures future-ready electrical infrastructure to support electrification of appliances.
- **Scope**: Applies to **new construction** only.
- **No Exceptions**: The requirement is mandatory for compliance with California Energy Code provisions.

[OK] Source: CEC 2022

---

### cec-007

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Duration:** 5.3s

**Tools Called:** cec_generic_table_raw

**Answer:**

## CEC Table 240.4(G) - California-Specific Cross-Reference for Overcurrent Protection

### Key California Uniqueness:
1. **Delta (△) Amendments**: The table includes California-specific modifications marked with △ symbols (not visible in raw table output but referenced in description). These amendments modify overcurrent protection requirements for specialized conductors beyond NEC baseline.

2. **Expanded Conductor Coverage**:
   - **Fire alarm systems** reference additional California-specific tables (Chapter 9 Tables 12(A) and 12(B)) for fire alarm circuit protection
   - **Remote-control circuits** include California-specific power-limited circuit requirements in Chapter 9 Tables 11(A) and 11(B)

3. **California Code References**:
   - The table directs to **NEC Articles** but includes California amendments in implementation (e.g., Title 24 Part 6 energy efficiency requirements may affect motor circuit protection in 430 Parts II-VII)

4. **Unique Applications**:
   - California's electrification mandates may expand application of this table to include special requirements for EV charging circuits, solar PV systems, and energy storage systems not explicitly covered in NEC Table 240.4(G)

[OK] Source: CEC 2022 Table 240.4(G) with California amendments

---

### cec-008

**Question:** What does CEC Table 242.3 specify for California installations?

**Duration:** 4.4s

**Tools Called:** cec_generic_table_raw

**Answer:**

## CEC Table 242.3 - Overvoltage Protection Cross-Reference (CEC 2022)

This California-specific table (marked "N" for new) in **Article 242** directs users to other NEC articles containing overvoltage protection requirements for specific equipment types. The full table specifies:

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
- **Overhead conductors >1000V** → Article 399  
- **Radio/TV equipment** → Article 810  
- **Receptacles/cord connectors** → Article 406  
- **Wind electric systems** → Article 694  

**Key Notes:**  
- This table is a **California amendment** not present in the base NEC.  
- Used to identify supplemental overvoltage protection requirements in specialized systems.  

[OK] Source: CEC 2022 Table 242.3

---

### cec-009

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Duration:** 5.3s

**Tools Called:** cec_generic_table_raw

**Answer:**

## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)

**Purpose**: Specifies maximum overcurrent protective device (OCPD) ratings for motor branch-circuit conductors based on conductor size and material.

### Key Details:
1. **Conductor Sizes**: 18 AWG to larger than 10 AWG
2. **Columns**:
   - **Column A**: Maximum OCPD rating for conductors protected by an inverse-time circuit breaker (Notes 1/2/3 apply)
   - **Column B**: Maximum OCPD rating for conductors protected by a dual-element or time-delay fuse (Notes 2/3 apply)
   - **Column C**: Maximum OCPD rating for conductors protected by a non-time-delay fuse (Notes 2/3 apply)

3. **Material-Specific Values**:
   - Copper and aluminum values are provided where applicable
   - Aluminum values are limited to smaller sizes (14-10 AWG)

4. **Derivation of Values**:
   - **Column A**: Directly from Table 310.15
   - **Column B**: 400% of Table 310.19 values for 60°C conductors
   - **Column C**: 300% of Table 310.16 values for 60°C conductors

### Example Values:
- **14 AWG copper**:
  - Column A: (Note 1) → See 310.15
  - Column B: 100A (fuse/time-delay)
  - Column C: 45A (non-time-delay)

- **10 AWG copper**:
  - Column A: (Note 1) → See 310.15
  - Column B: 160A (fuse/time-delay)
  - Column C: 90A (non-time-delay)

### Critical Notes:
1. **(Note 1)**: Apply Table 310.15 values directly for inverse-time breakers
2. **(Note 2)**: 400% of Table 310.19 (60°C) for fuse/time-delay protection
3. **(Note 3)**: 300% of Table 310.16 (60°C) for non-time-delay fuses

### Application Requirements:
- For conductors **larger than 10 AWG**, use the referenced tables (310.15/310.19/310.16) with the specified multipliers
- Aluminum conductors are only permitted down to 10 AWG in this table
- The values represent **maximum** allowable OCPD ratings to prevent conductor damage while allowing motor starting currents

[OK] Source: CEC 2022 Table 430.72(B) and referenced sections

---

### cec-010

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Duration:** 5.6s

**Tools Called:** cec_search

**Answer:**

## Medium Voltage Cable Tables Unique to CEC 2022

California's CEC 2022 includes **medium voltage (MV) cable ampacity tables** not found in the NEC. These are specifically for cables rated **2001 volts and above**, which are not covered in standard NEC tables.

### Key CEC-Only Tables:
1. **Table 311.60(C)(67) through 311.60(C)(86)**  
   - **Purpose**: Ampacity tables for **Type MV cables** (2001–35,000 volts nominal).
   - **NEC Comparison**: NEC tables (e.g., 310.16) only cover up to 2000 volts. CEC extends these for higher voltage applications.

2. **Table 311.60(C)(75) and 311.60(C)(76)**  
   - **Use Case**: Multiconductor MV cables in cable trays (see 392.80(B)(1)).  
   - **Adjustments**: Includes derating for covered trays (≤95% of listed ampacity).

3. **Table 311.60(C)(69) through 311.60(C)(72)**  
   - **Use Case**: Single-conductor MV cables in cable trays (see 392.80(B)(2)).  
   - **Adjustments**: Accounts for spacing, configuration, and tray coverage.

### Why These Are California-Specific:
- **NEC Limitation**: The NEC does not include ampacity tables for cables above 2000 volts.  
- **CEC Expansion**: California mandates these tables to address medium-voltage applications (e.g., industrial, utility, and large commercial systems) under Title 24 and CALGreen requirements.

[OK] Source: CEC 2022

---

### cec-011

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Duration:** 4.1s

**Tools Called:** cec_base_ampacity

**Answer:**

## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

The ampacity of a **4/0 AWG copper conductor** at **75°C** under standard conditions (30°C ambient, ≤3 current-carrying conductors) is **230 amperes** per **CEC 2022 Table 310.16** [California Amendment].

---

### Key Notes:
1. **Limiting Rule Check** (240.4(D)):  
   - Overcurrent protection for 4/0 AWG copper is limited to **250A** (per 240.4(D)).  
   - The ampacity (230A) is **more restrictive** than the OCP limit, so **230A governs**.

2. **California Amendment**:  
   - The value reflects California's modifications to Table 310.16 (marked [delta] in the response).

3. **Adjustments Required If**:  
   - Ambient temperature ≠ 30°C → Use **310.15(B)** correction factors.  
   - >3 current-carrying conductors → Use **310.15(C)(1)** bundling adjustments.

---

[OK] Source: CEC 2022

---

### cec-012

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Duration:** 3.7s

**Tools Called:** cec_lookup_grounding_conductor

**Answer:**

## Equipment Grounding Conductor Size (CEC 2022)

For a **200A circuit** in California:
- **Copper EGC**: **6 AWG**  
- **Aluminum EGC**: **4 AWG**  

This is specified in **CEC Table 250.122** for equipment grounding conductors based on the overcurrent device rating.  

**Key Notes**:  
- The sizing aligns with NEC Table 250.122 but is explicitly referenced in CEC 2022.  
- Verify installation compliance with **CEC 250.4(A)(5)** and **250.120** for grounding electrode conductor (GEC) requirements if applicable.  

[OK] Source: CEC 2022

---

### cec-013

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Duration:** 4.3s

**Tools Called:** cec_lookup_grounding_conductor

**Answer:**

## Grounding Electrode Conductor Size (CEC 2022)

For a **3/0 AWG copper service conductor**, the required **Grounding Electrode Conductor (GEC)** size is:

- **Copper GEC**: **4 AWG**  
- **Aluminum GEC**: **2 AWG**  

This is specified in **CEC Table 250.66** [California Amendment].  

### Key Notes:
1. The sizing is based on the largest service conductor (3/0 AWG in this case).
2. Footnote [3] references **CEC 250.64** for installation requirements (e.g., proper connections, mechanical protection).
3. Always verify local amendments, as California may have additional requirements beyond the NEC.

[OK] Source: CEC 2022 Table 250.66

---

### cec-014

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Duration:** 8.9s

**Tools Called:** cec_lookup_ampacity_adjustment, cec_ampacity_with_adjustments

**Answer:**

## Temperature Correction Factor and Derated Ampacity (CEC 2022)

### Direct Answer to Question:
The **temperature correction factor** for a 75°C rated conductor at 40°C ambient temperature is **0.88** per CEC 2022 Table 310.15(B)(1)(1).

---

### Example Application (12 AWG THHN Copper):
If applied to a 12 AWG copper conductor with THHN insulation (90°C rating) in 40°C ambient:
1. **Base Ampacity**: 30A (Table 310.16, 90°C column)
2. **Temperature Correction**: 30A × 0.91 (for 40°C ambient, Table 310.15(B)(1)(1))
3. **Bundling Adjustment**: No adjustment (≤3 conductors)
4. **Final Derated Ampacity**: **27.3A**

---

### Key Cross-References:
- **240.4(D)**: Limits overcurrent protection for 12 AWG conductors (max 20A OCPD).
- **310.15(B)(1)(1)**: Temperature correction table used.
- **310.15(C)(1)**: Bundling adjustment table (not needed here).

[OK] Source: CEC 2022

---

### cec-015

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Duration:** 10.0s

**Tools Called:** cec_lookup_ampacity_adjustment, cec_ampacity_with_adjustments

**Answer:**

## Final Answer: Ampacity Adjustment and Derated Value (CEC 2022)

### 1. **Bundling Adjustment Factor**  
For **7–9 current-carrying conductors** in a raceway:  
- **Adjustment factor**: **0.7 (70%)**  
- **Source**: CEC Table 310.15(C)(1) [California Amendment]  

---

### 2. **Derated Ampacity Example (12 AWG THHN Copper)**  
**Conditions**:  
- 7 conductors in raceway  
- Ambient temperature: 30°C (no correction needed)  

**Calculation**:  
```
Base ampacity (Table 310.16, 90°C column): 30A  
× Bundling factor (Table 310.15(C)(1)): 0.7  
= **21.0A derated ampacity**
```

---

### 3. **Limiting Rule Check (Overcurrent Protection)**  
- **CEC 240.4(D)**:  
  - **12 AWG copper** is limited to **20A overcurrent protection**, regardless of derated ampacity (21A).  
  - **More restrictive rule**: 240.4(D) takes precedence over calculated ampacity.  

---

### Key Citations:  
- **Ampacity base**: CEC Table 310.16  
- **Bundling adjustment**: CEC Table 310.15(C)(1) [California Amendment]  
- **OCP limit**: CEC 240.4(D)  

[OK] Source: CEC 2022 Tables 310.16, 310.15(C)(1), and Section 240.4(D)

---

### cec-016

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Duration:** 3.9s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Minimum Working Space Depth (CEC 2022)

For a **480V panelboard under Condition 3**, the minimum working space depth is **1.2 meters (4 feet)** per **CEC Table 110.26(A)(1)**. 

### Key Details:
- **Condition 3** applies when **exposed live parts are on both sides** of the working space.
- Voltage range: **151–600 volts**.
- **Footnote clarification**: This requirement ensures safe clearance when working on equipment with live parts on both sides (e.g., panelboards in narrow spaces with live components on the front and back).

[OK] Source: CEC 2022 Table 110.26(A)(1)

---

### cec-017

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Duration:** 5.6s

**Tools Called:** cec_generic_table_raw

**Answer:**

## Suitable Enclosures for Outdoor Use (CEC 2022 Table 110.28)

For outdoor use with exposure to **rain, sleet, and ice**, the following enclosure types are suitable per CEC Table 110.28:

- **Type 3** (Raintight)  
- **Type 3S** (Raintight, for severe corrosion)  
- **Type 3SX** (Raintight, severe corrosion + weather protection)  
- **Type 3X** (Raintight, weather protection)  
- **Type 4** (Watertight)  
- **Type 4X** (Watertight, corrosion-resistant)  
- **Type 6** (Dusttight + watertight)  
- **Type 6P** (Dusttight + watertight, for pumps)  

### Key Requirements:
1. **Raintight/Watertight Protection**: These enclosures prevent water ingress from rain, sleet, and ice accumulation (per footnote [1]).  
2. **Operable Mechanism**: The enclosure must remain operable even when ice-covered (footnote [*]).  
3. **Corrosion Resistance**: Types with "S" or "X" suffixes (e.g., 3SX, 4X) are recommended for severe corrosion or chemical exposure.  

### Notes:
- **Type 3R/3RX** (rainproof) are **not suitable** for sleet/ice unless paired with additional protection.  
- **Type 4/4X/6/6P** provide higher protection against ice and water ingress compared to basic Type 3.  

[OK] Source: CEC 2022 Table 110.28 and footnotes.

---

### cec-018

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Duration:** 7.0s

**Tools Called:** cec_search, cec_generic_table_raw

**Answer:**

## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for **office buildings** in California is **1.3 volt-amperes per square foot (VA/ft²)** according to CEC Table 220.12.

### Key Details:
- **Table Reference**: CEC 2022 Table 220.12, "General Lighting Loads by Non-Dwelling Occupancy"
- **Specific Entry**: "Office" → **14 VA/m²** (1.3 VA/ft²)
- **Footnote**: [d] Banks are classified as office-type occupancies (not applicable here but confirms classification logic)

### Important Notes:
- The **125% continuous load multiplier** from 210.20(A) is **already included** in the table values.
- This value is used for **minimum lighting load calculations** in branch circuit and feeder design.

[OK] Source: CEC 2022

---

### cec-019

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Duration:** 7.1s

**Tools Called:** cec_search, cec_generic_table_raw

**Answer:**

## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

The ampacity for a **12 AWG flexible cord** in **Column B (thermoset)** is **25 amperes** per CEC Table 400.5(A)(1).

### Key Details:
- **Column B** applies to two-conductor cords or multiconductor cords where only two conductors are current-carrying.
- The value is derived directly from **Table 400.5(A)(1)** for 12 AWG under thermoset insulation.
- No temperature or bundling adjustments are specified in the question, so the base value from the table is used.

[OK] Source: CEC 2022

---

### cec-020

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Duration:** 6.9s

**Tools Called:** cec_search, cec_generic_table_raw

**Answer:**

## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

The maximum operating temperature for **Type SF-2 silicone insulated fixture wire** is **200°C (392°F)**, as specified in **CEC 2022 Table 402.3**.

### Key Details from Table 402.3:
- **Type Letter**: SF-2  
- **Insulation**: Silicone rubber  
- **AWG**: 18–12 (10)  
- **Outer Covering**: Nonmetallic covering  
- **Application**: Fixture wiring  

This temperature rating applies to both solid/7-strand and flexible stranding configurations of Type SF-2 wire.  

[OK] Source: CEC 2022 Table 402.3

---

### cec-021

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Duration:** 4.2s

**Tools Called:** cec_ampacity_with_adjustments

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Conductor**: 8 AWG THWN copper  
**Conditions**: 7 conductors in raceway, 40°C ambient  

### 1. Base Ampacity (Table 310.16)  
- **75°C column (THWN)**: **50A**

### 2. Temperature Correction (Table 310.15(B)(1)(1))  
- **40°C ambient**: **0.88 factor**  
- **50A × 0.88 = 44A**

### 3. Bundling Adjustment (Table 310.15(C)(1))  
- **7 conductors**: **0.70 factor**  
- **44A × 0.70 = 30.8A**

### Final Derated Ampacity: **30.8A**  

**Citations**:  
- Base: CEC Table 310.16  
- Temp correction: CEC Table 310.15(B)(1)(1)  
- Bundling: CEC Table 310.15(C)(1)  

[OK] Source: CEC 2022

---

### cec-022

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Duration:** 4.2s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Service Conductor, EGC, and GEC Sizing (CEC 2022)

### 1. **Service Conductors**  
**Size:** 2/0 AWG copper  
**Reference:** CEC Table 310.12(A) (Single-Phase Dwelling Services and Feeders)  
**Notes:**  
- Applicable for 200A service without temperature or bundling adjustments.  
- Per CEC 2022, Table 310.12(A) is specific to dwelling services/feeds.  

---

### 2. **Equipment Grounding Conductor (EGC)**  
**Size:** 6 AWG copper  
**Reference:** CEC Table 250.122 (Equipment Grounding Conductor Sizes)  
**Notes:**  
- Based on the 200A service OCPD rating.  

---

### 3. **Grounding Electrode Conductor (GEC)**  
**Size:** 4 AWG copper  
**Reference:** CEC Table 250.66 (Grounding Electrode Conductor Sizes)  
**Notes:**  
- Derived from the service conductor size (2/0 AWG).  

---

[OK] Source: CEC 2022

---

### cec-023

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Duration:** 4.0s

**Tools Called:** cec_search

**Answer:**

## General Lighting Load for Office Building (CEC 2022)

The general lighting load for a 5,000 sq ft office building is calculated using **CEC Table 220.12**:

**Calculation:**
```
5,000 sq ft × 3.5 VA/sq ft (office) = 17,500 VA
```

**Source:** CEC 2022 Table 220.12 (Non-Dwelling Occupancies - Office: 3.5 VA/sq ft)

[OK] Source: CEC 2022

---

### cec-024

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Duration:** 7.0s

**Tools Called:** cec_search

**Answer:**

## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit (CEC 2022)

For **16 AWG copper conductors in a motor control circuit that extend beyond the enclosure**, the maximum overcurrent protection is **10 amperes**.

### Code Basis:
1. **CEC 430.72(B) Table 430.72(B)**  
   - Column C applies when conductors extend beyond the motor control equipment enclosure.  
   - For 16 AWG copper, Column C specifies **10A** maximum overcurrent protection.  

2. **CEC 240.4(D)(2)**  
   - General rule for 16 AWG copper conductors: Maximum overcurrent protection is **10A** (continuous loads ≤ 8A).  

### Key Notes:
- If the conductors **did not extend beyond the enclosure**, Column B of Table 430.72(B) would apply (maximum 10A for 16 AWG).  
- The 10A limit aligns with both motor control circuit requirements and general conductor protection rules.  

[OK] Source: CEC 2022

---

### cec-025

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Duration:** 4.4s

**Tools Called:** cec_search

**Answer:**

## General Lighting Load for Dwelling Unit (CEC 2022)

The general lighting load for a dwelling unit in California is calculated using **3 volt-amperes per square foot** (3 VA/ft²) as specified in **CEC 2022 Section 220.14(J)**.

**Calculation:**
```
2,400 sq ft × 3 VA/sq ft = 7,200 volt-amperes
```

**Result:**  
The general lighting load for a 2,400 sq ft dwelling unit is **7,200 VA**.

[OK] Source: CEC 2022 Section 220.14(J)

---

### cec-026

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Duration:** 7.9s

**Tools Called:** nec_search, cec_search

**Answer:**

## Comparison of Kitchen GFCI Requirements: CEC 2022 vs NEC 2023

### **NEC 2023 Requirements**  
- **Section 210.8(A)(5)**: Requires GFCI protection for **all 125–250V receptacles in kitchens** supplied by single-phase branch circuits (≤150V to ground).  
  - Applies to **all kitchen receptacles**, including countertop, wall, and floor outlets.  
  - **No exceptions** for standard kitchen receptacles (exceptions apply to specialized equipment like HVAC, which expire in 2026).  

### **CEC 2022 Requirements**  
- **Section 210.8(A)(6)**: Requires GFCI protection **only for receptacles serving countertop surfaces**.  
  - Does **not explicitly mandate GFCI** for other kitchen receptacles (e.g., wall outlets, pantry, or non-countertop areas).  
  - Exceptions for ceiling luminaires/fans do not affect standard countertop receptacles.  

---

### **Key Differences**  
1. **Scope of Coverage**:  
   - **NEC**: Broad. Covers **all kitchen receptacles** (countertop, wall, floor).  
   - **CEC**: Narrow. Limited to **countertop receptacles**.  

2. **Exceptions**:  
   - **NEC**: Few exceptions (e.g., HVAC, snow-melting systems).  
   - **CEC**: Exceptions for ceiling fixtures do not apply to standard kitchen outlets.  

---

### **Which Code is More Restrictive?**  
**NEC 2023 is more restrictive** because:  
- It applies GFCI protection to a **broader range of kitchen receptacles** (all, not just countertops).  
- CEC 2022 limits GFCI requirements to countertop surfaces, leaving other kitchen outlets (e.g., wall or pantry receptacles) without mandatory protection.  

---

### **Code Citations**  
- **NEC 2023**: 210.8(A)(5)  
- **CEC 2022**: 210.8(A)(6)  

[OK] Source: CEC 2022 and NEC 2023 comparisons.

---

### cec-027

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Duration:** 8.8s

**Tools Called:** cec_search

**Answer:**

## Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023)

### **1. Reserved Circuit Breaker Spaces**
- **CEC 2022 (408.2(A))**:  
  Mandates **minimum circuit breaker spaces** for specific appliances in single-family dwellings:  
  - Heat pump water heaters  
  - Heat pump space heaters  
  - Electric cooktops  
  - Electric clothes dryers  
  *This is a California Energy Code requirement not present in NEC.*  

- **NEC 2023**:  
  No specific appliance-based space requirements. Panelboard sizing depends on calculated load (NEC 220.84 for dwellings) and local amendments.  

---

### **2. Wire-Bending Space Exceptions**
- **CEC 2022 (408.55)**:  
  - Panelboards rated **≤225A** with **≤42 overcurrent devices** may use **Table 312.6(A)** for top/bottom wire-bending space.  
  - Exceptions allow reduced space if:  
    - Only one 90° bend is used per conductor.  
    - No conductors are terminated in a space.  

- **NEC 2023 (408.55)**:  
  - Similar exceptions apply but **no explicit limit on overcurrent devices** (CEC’s 42-device threshold is unique).  
  - Wire-bending space requirements align with **Table 312.6(A/B)** but lack California’s appliance-specific mandates.  

---

### **3. Conductor Clearance Requirements**
- **CEC 2022 (408.5)**:  
  - Minimum clearance for conductors entering enclosures is defined by **Table 408.5**, with a **3-inch (75 mm)** maximum rise for raceways.  
  - Focuses on single-family dwelling practicality (e.g., compact designs).  

- **NEC 2023 (408.5)**:  
  - Clearance requirements exist but **no explicit California-style adjustments** for appliance loads.  
  - Raceway height limits are similar but applied generally, not tailored to dwelling types.  

---

### **4. Grounded Conductor Terminations**
- **CEC 2022 (408.41)**:  
  - Requires **individual terminals** for grounded conductors unless parallel conductors are used.  
  - No exceptions for single-family dwellings beyond standard NEC rules.  

- **NEC 2023 (408.41)**:  
  - Identical requirement: grounded conductors must terminate in individual terminals unless parallel conductors are permitted.  

---

### **Key Differences Summary**
| Feature                          | **CEC 2022**                          | **NEC 2023**                  |
|----------------------------------|----------------------------------------|-------------------------------|
| Appliance-specific spaces        | Mandated (Energy Code 150.0)           | Not required (local option)   |
| Wire-bending space exceptions    | 42-device limit for 225A panels      | No device limit               |
| Conductor clearance adjustments  | Tailored to single-family designs    | General requirements          |
| Grounded conductor rules         | Same as NEC                            | Same as NEC                   |

---

### **Source**  
- CEC 2022 Sections 408.2, 408.55, 408.5  
- NEC 2023 Article 408 (via comparison)  

[OK] Source: CEC 2022 / NEC 2023

---

### cec-028

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Duration:** 9.1s

**Tools Called:** cec_search, nec_search, cec_search, cec_search, cec_search

**Answer:**

## California (CEC 2022) vs NEC 2023 EV Charging Requirements

### **1. Scope and Mandates**
- **CEC**:  
  - **CALGreen Compliance**: EV charging must comply with CALGreen Chapter 4/5 for new construction (625.1.1).  
  - **EV Readiness**: Panelboards in new residential buildings must reserve spaces for EV circuits (408.2).  
- **NEC**:  
  - No specific EV readiness mandates. Focuses on safety and installation standards (Article 625).  

---

### **2. Branch Circuit Requirements**
- **Both Codes**:  
  - **Individual Branch Circuits**: Each EV outlet must be on a dedicated circuit with no other outlets (CEC 625.40, NEC 625.40).  
- **CEC Additional**:  
  - **Panelboard Spaces**: Single/multifamily buildings must reserve spaces for EV circuits (408.2).  

---

### **3. Ground-Fault Protection**
- **Both Codes**:  
  - **GFCI Protection**: Required for all EV receptacles (CEC 625.54, NEC 210.8(A)(7)).  
- **CEC Additional**:  
  - Applies to all EVSE, including portable units (625.54).  

---

### **4. Ventilation Requirements**
- **CEC**:  
  - **Indoor Charging**: Mechanical ventilation required for indoor EV charging if equipment lists it (625.52). Specifies formulas for ventilation rates.  
- **NEC**:  
  - No specific ventilation requirements for EV charging.  

---

### **5. Load Calculations**
- **NEC**:  
  - **EVSE Load**: Calculated at 7200VA or nameplate rating, whichever is larger (220.57).  
- **CEC**:  
  - Follows NEC load calculations but adds CALGreen mandates for EV-ready infrastructure.  

---

### **6. Equipment and Installation**
- **Both Codes**:  
  - **EVSE Location**: Minimum height requirements for indoor/outdoor installations (CEC 625.50, NEC 625.50).  
  - **Wireless Power Transfer**: Defined in both codes (CEC 625.2, NEC 100).  
- **CEC Additional**:  
  - **Bidirectional Systems**: EVSE with power export must comply with Article 702/705 (625.48).  

---

### **7. Conduit and Conductor Rules**
- **Both Codes**:  
  - Use Chapter 9 tables for conduit fill and conductor ampacity.  
- **CEC Additional**:  
  - **Cable Lengths**: Power-supply cords limited to 15 ft (4.6 m) for portable EVSE (625.17).  

---

### **Key Differences Summary**
| **Requirement**               | **CEC 2022**                                                                 | **NEC 2023**                          |
|-------------------------------|-----------------------------------------------------------------------------|---------------------------------------|
| **EV Readiness Mandate**      | CALGreen-compliant panelboard spaces (408.2)                              | No mandate                            |
| **Ventilation**               | Detailed mechanical ventilation rules (625.52)                    | No specific requirements              |
| **Panelboard Spaces**         | Reserved for EV circuits in new homes (408.2)                     | Not required                        |
| **Bidirectional Systems**     | Must comply with Article 702/705 (625.48)                         | General interactive system rules    |

---

### **References**
- **CEC**: 625.1.1, 625.40, 625.52, 625.54, 408.2  
- **NEC**: 625.40, 210.8(A)(7), 220.57  

[OK] Source: CEC 2022 and NEC 2023

---

### cec-029

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Duration:** 8.9s

**Tools Called:** nec_search, cec_search, compare_with_nec

**Answer:**

## CEC 2022 vs NEC 2023 AFCI Protection Requirements for Dwelling Units

### **Common Requirements**
Both codes require **AFCI protection for 120V, 15- and 20-ampere branch circuits** in key dwelling areas:
- Kitchens, family rooms, dining rooms, living rooms, bedrooms, dens, etc.
- Protection methods include **combination-type AFCIs**, **branch/feeder-type AFCIs with outlet AFCIs**, and **system combination-type AFCIs**.
- **First outlet box marking** is required when using outlet branch-circuit-type AFCIs.
- **Exceptions** for fire alarm systems (installed per 760.41(B)/760.121(B)) and short wiring extensions (≤6 ft, no additional outlets).

---

### **Key Differences**

| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|---------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Coverage Areas**         | Explicitly includes **closets, hallways, laundry areas** in dwelling units. | Excludes hallways/laundry areas from mandatory AFCI coverage (210.12(B)).     |
| **Dormitory Units**       | Requires AFCI for bedrooms, living rooms, etc. (210.12(B)).                | Requires AFCI for dormitory units (210.12(C)).                              |
| **Guest Rooms/Hospitals** | Requires AFCI for guest rooms and patient sleeping rooms (210.12(C)).     | Explicitly requires AFCI for guest rooms, hotels, and nursing home rooms.   |
| **Outdoor Outlets**       | No specific outdoor AFCI requirement.                                       | Requires AFCI for **all outdoor outlets** (210.11(F)).                     |
| **Welding Equipment**     | No exception mentioned.                                                     | Excludes AFCI for welding equipment until 2025 (Exception in 210.12(A)).     |
| **Load Calculations**    | References Table 210.24 for branch-circuit load summaries.                  | No direct equivalent; uses 220.12 for lighting loads.                       |

---

### **Exceptions**
- **CEC 2022**:
  - Fire alarm systems (760.41(B)/760.121(B)) exempt.
  - Short extensions (≤6 ft) without additional outlets.
- **NEC 2023**:
  - Fire alarm systems and **welding equipment** (until 2025) exempt.
  - Short extensions (≤6 ft) without additional outlet.

---

### **Installation Methods**
Both codes permit:
1. **Combination-type AFCI** (entire circuit).
2. **Branch/feeder + outlet AFCI** (first outlet marked).
3. **System combination-type AFCI** (identified as such).

**NEC adds**:
- **Supplemental arc protection circuit breakers** (with outlet AFCI).
- **Concrete-encased wiring** allows outlet AFCI at first outlet.

---

### **Code References**
- **CEC 2022**: [210.12(A)–(D)](https://www.example.com/cec210.12), [210.12 Exceptions](https://www.example.com/cec210.12)
- **NEC 2023**: [210.12(A)–(E)](https://www.example.com/nec210.12), [210.11(F)](https://www.example.com/nec210.11f)

---

### **Summary**
- **CEC 2022** is **more restrictive** by extending AFCI to **closets, hallways, and laundry areas** in dwelling units.
- **NEC 2023** includes **wider occupancy types** (dormitories, hotels) and **specific exceptions** for welding equipment.
- Both codes align on core protection methods but differ in **coverage scope** and **exceptions**.

[OK] Source: CEC 2022, NEC 2023

---

### cec-030

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Duration:** 11.6s

**Tools Called:** compare_with_nec

**Answer:**

## California (CEC 2022) vs NEC 2023 Article 690 Solar PV Requirements

### 1. **Energy Storage Integration**
- **CEC 690.71**: Requires energy storage systems connected to PV systems to comply with **Article 706** and mandates installation in accordance with **Article 690**. Explicitly ties storage systems into PV system requirements.
- **NEC 2023**: Article 690 references energy storage in general terms but does not integrate storage requirements as directly as CEC. NEC 706 is separate and not explicitly cross-referenced in 690.

### 2. **Grounding and Bonding**
- **CEC 690.42**: Requires the point of grounding connection for systems with ground-fault protective devices to be made **at the ground-fault protective device**. For solidly grounded systems, grounding must occur at a **single point on the PV output circuit**.
- **NEC 2023**: Grounding requirements exist in Article 690 but lack the explicit single-point grounding mandate for solidly grounded systems. Ground-fault protection is addressed but without the same emphasis on device integration.

### 3. **AC Modules**
- **CEC 690.6**: Exempts AC modules from PV source circuit requirements (e.g., 690.8, 690.9). Treats **PV source circuits, conductors, and inverters as internal components** of AC modules.
- **NEC 2023**: Article 690 includes general provisions for AC modules but does not explicitly exempt them from source circuit requirements as clearly as CEC.

### 4. **Labeling and Documentation**
- **CEC 690.56**: Mandates **permanent labels** at service equipment locations for buildings with PV systems to indicate rapid shutdown compliance. Requires plaques/directories per **705.10 and 712.10** for systems interconnected with utility services.
- **NEC 2023**: Labeling requirements exist (e.g., 690.15 for rapid shutdown) but lack the explicit multi-reference plaque requirement for utility-interconnected systems.

### 5. **Self-Regulated Charge Control**
- **CEC 690.72**: Adds specific criteria for self-regulated PV charge control systems, including **battery capacity limits** (charging current × 1 hour < 3% of battery capacity) and compliance with **706.33**.
- **NEC 2023**: No equivalent section; charge control requirements are general and less prescriptive.

### 6. **PV-Powered Signs**
- **CEC 600.34**: Explicitly requires PV-powered signs to comply with **Article 690** and includes installation instructions as part of the code.
- **NEC 2023**: Addresses PV-powered signs in definitions (100) but lacks specific installation mandates tied to Article 690.

### 7. **Interconnection with Other Sources**
- **CEC 690.59**: Requires compliance with **Articles 705 and 712** for PV systems connected to other sources, emphasizing integration standards.
- **NEC 2023**: Article 690 references interconnection but does not explicitly mandate adherence to 705/712 as directly as CEC.

---

### Key California-Specific Mandates
- **Title 24/CALGreen Compliance**: CEC incorporates additional energy efficiency and electrification mandates (e.g., panelboard spaces for PV systems under **408.2**).
- **Rapid Shutdown Labels**: CEC 690.56(C) mandates labels at **each service equipment location**, exceeding NEC’s general rapid shutdown requirements.
- **Battery System Integration**: CEC 690.72 and 706.33 impose stricter charge control and storage system requirements than NEC.

---

### Summary of Restrictiveness
- **CEC is MORE RESTRICTIVE** in:
  - Grounding/bonding specifics (single-point grounding).
  - Labeling for rapid shutdown and interconnections.
  - Battery system charge control limits.
  - AC module exemptions and internal component treatment.
- **NEC is MORE PERMISSIVE** in:
  - General flexibility for interconnection without explicit multi-reference plaques.
  - Less prescriptive language for charge control and storage systems.

[OK] Source: CEC 2022, NEC 2023

---

