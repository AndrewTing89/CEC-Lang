# CEC Evaluation Run 8 - Human Review Report

## Summary
- **Total Questions**: 30
- **Model**: qwen/qwen3-32b
- **Runs per Question**: 3
- **Date**: 2025-12-07

---

## cec-001: panelboard_requirements

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected Answer:** CEC 408.2 requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, (4) electric clothes dryers, and (5) electric vehicle charging equipment. This is a California-specific requirement for electrification readiness.

**CEC Reference:** CEC 408.2

### Agent's Answer:

## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022)

### **Reserved Circuit Breaker Spaces**
Per **CEC 2022 Section 408.2(A)**, single-family residential panelboards **must reserve circuit breaker spaces** for the following appliances:
1. **Heat pump water heaters**  
2. **Heat pump space heaters**  
3. **Electric cooktops**  
4. **Electric clothes dryers**  

These requirements are mandated by the **California Energy Code Section 150.0(n), (t), (u), and (v)** to ensure future-ready electrical infrastructure for electrification and energy efficiency.

---

### **Exception Search Results**
After searching for exceptions to **CEC 2022 Section 408.2**, the following exceptions were found, but **none directly modify the reserved space requirements** for single-family dwellings:
- **426.14**, **424.10**, **422.23**, and **425.10** relate to "special permission" for non-standard installations of heating, deicing, and industrial equipment. These exceptions apply to **equipment installation methods**, not panelboard space requirements.

---

### **Key Details**
- **Appliance-Specific Mandates**:  
  - **Heat pump water heaters** and **space heaters** are explicitly required due to California's push for decarbonization (Title 24, Part 6).  
  - **Electric cooktops** and **dryers** must have reserved spaces even if not installed at the time of construction.  
- **Panelboard Rating**: Panelboards must be rated **not less than the calculated feeder load** (per Article 220).  

---

### **NEC 2023 Reference**
- **No equivalent requirement** in NEC 2023. California’s mandate for reserved spaces for heat pump appliances and electric cooking/drying is **unique to CEC** and Title 24.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-002: ev_charging

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected Answer:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. CEC 408.2 requires panelboard spaces for EV charging equipment. Title 24 also mandates EV charging readiness.

**CEC Reference:** CEC 408.2, Title 24

### Agent's Answer:

## California EV Charging Requirements (CEC 2022)  

### 1. **Mandatory EV Infrastructure (CALGreen)**  
- **Reserved Circuit Space**: Panelboards must include reserved circuit breaker space for EV charging (CEC 408.2).  
- **CALGreen Mandates**:  
  - **EV-Ready Circuits**: New residential construction must include **40-amp minimum circuits** for EV charging.  
  - **Conduit to Parking**: Conduit must be installed from the electrical panel to designated EV parking spaces.  
  - **Panel Capacity**: Electrical panels must have sufficient capacity to accommodate EV loads.  

---

### 2. **Electrical System Requirements**  
- **Individual Branch Circuits** (625.40):  
  - Each EV outlet must be on a **dedicated branch circuit** with **no other outlets**.  
  - **Exception**: Backfeeding prevention required (625.46) – systems must prevent energy backfeed to the grid when utility power is lost.  
- **Overcurrent Protection** (625.41):  
  - Overcurrent devices must be sized at **125% of the continuous load**.  
- **Ground-Fault Protection** (625.56):  
  - All EV receptacles require **GFCI protection** for personnel safety.  
- **Receptacle Enclosures** (625.56):  
  - Outdoor/wet location receptacles must have **weatherproof enclosures** (extra-duty rated).  

---

### 3. **Equipment and Installation**  
- **Cord Lengths** (625.17):  
  - Portable EVSE cords ≤ **12 inches** (if interrupting device is in the enclosure) or ≤ **15 feet** (if at the plug).  
  - Total cord length (including output) ≤ **25 feet** unless using a listed cable management system.  
- **Ventilation** (625.52):  
  - Mechanical ventilation required if equipment is listed for indoor charging with ventilation needs.  
  - Ventilation must be **interlocked with the charging circuit**.  
- **Connection Methods** (625.44):  
  - Portable EVSE: 15/20A, 125V or 250V receptacles.  
  - Fastened-in-place: Up to 50A, 250V receptacles.  

---

### 4. **Safety and Compliance**  
- **No Backfeeding** (625.46):  
  - Systems must prevent energy backfeed to the grid when utility power is lost.  
- **Personnel Protection** (625.22):  
  - Listed personnel protection systems required for equipment ≥60V DC.  
- **Labeling** (625.52):  
  - Equipment requiring ventilation must be clearly marked.  

---

### 5. **Exceptions and Special Conditions**  
- **Rating Adjustments** (625.42):  
  - Adjustable settings on fixed equipment permitted **only with restricted access** (locked doors, tool-required covers, or password-protected software).  
  - Service/feeder sizing must match adjusted current settings.  

---

## NEC 2023 Reference  
- **Similar Requirements**: NEC 625 covers EV installation basics (GFCI, dedicated circuits).  
- **California-Specific Mandates**:  
  - **CALGreen** requirements (EV-ready circuits, conduit, panel capacity) are **exclusive to California** and not in NEC.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-003: solar_pv

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected Answer:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Reference:** CEC 690, Title 24 Part 6

### Agent's Answer:

## California Solar PV Requirements (CEC 2022) with Exceptions

### 1. **Arc-Fault Protection (690.11)**
- **Mandatory**: All residential PV systems with DC circuits ≥80V must have listed DC arc-fault circuit interrupters.
- **Exception** (690.11): Systems **not installed on/in buildings** are exempt if:
  - Installed in **metallic raceways**, metal-clad cables, enclosed metallic trays, or **underground**
  - Detached structures housing PV equipment are **not considered buildings**
- **California-specific**: Title 24 requires arc-fault protection for all new residential PV systems regardless of location.

---

### 2. **Ground-Fault Protection (690.41)**
- **Required**: DC ground-fault protection for PV systems >30V or >8A.
- **Exception** (690.41): Solidly grounded systems with **≤2 modules in parallel** and **not in buildings** may omit ground-fault protection.
- **California mandate**: CALGreen requires additional fire mitigation documentation for systems without integrated protection.

---

### 3. **Stand-Alone Systems (690.10)**
- Must comply with **Article 710** for off-grid systems.
- **California requirement**: Minimum 1.5kW PV capacity for new homes (Title 24 §150.1).

---

### 4. **Interconnection Compliance (690.59)**
- Must follow **Article 705** and **Article 712** for utility and storage interconnections.
- **California-specific**: Net energy metering and EV-ready infrastructure (CALGreen §110.6).

---

### 5. **AC Module Systems (690.6)**
- AC modules treated as inverter-output circuits.
- **Exception**: PV source circuit rules **do not apply** to AC modules.
- **California**: AC modules must still comply with Title 24 labeling and monitoring requirements.

---

## NEC 2023 Reference
- **Arc-fault protection**: NEC 690.11 (same requirement)
- **Ground-fault exceptions**: NEC 690.41 (same exceptions)
- **California mandates**: Title 24 and CALGreen requirements are **exclusive to California**; NEC does not include these.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison), Title 24 Part 6, CALGreen

---

## cec-004: heat_pump

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected Answer:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Reference:** CEC 408.2

### Agent's Answer:

## California Heat Pump Water Heater Circuit Requirements (CEC 2022)  

### **Single-Family Buildings (1–2 Dwellings)**  
1. **Panelboard Requirements** (CEC 408.2(A)):  
   - Panelboards must include **dedicated circuit breaker spaces** for heat pump water heaters as specified in **California Energy Code Section 150.0(n)**.  
   - *Example*: Reserved 30–50A circuit breaker space for water heater.  

2. **Branch Circuit Requirements** (CEC 422.3(A)):  
   - **Designated receptacles/branch circuits** must be provided for heat pump water heaters.  
   - Circuits must be **identified and labeled** per California Energy Code Section 150.0(n).  

---

### **Multifamily Buildings**  
- **Panelboard Requirements** (CEC 408.2(B)):  
  - Panelboards must include **circuit breaker spaces** for heat pump water heaters as per **California Energy Code Section 160.9**.  

- **Branch Circuit Requirements** (CEC 422.3(B)):  
  - **Dedicated circuits** and circuit identifications are required.  
  - Specific details referenced to **California Energy Code Sections 160.9(b)**.  

---

### **Exceptions and Notes**  
1. **Temperature Controls** (CEC 422.47):  
   - Storage-type water heaters (including heat pump models) must have a **temperature-limiting means** in addition to the thermostat.  
   - *Exceptions*:  
     - Storage water heaters rated ≥60 kW and suitable for ≥82°C (180°F).  
     - Instantaneous-type water heaters ≤4 L (1 gal).  

2. **Special Installations** (CEC 422.23):  
   - Non-standard installation methods require **special permission**.  

3. **Central Heating Equipment** (CEC 422.12):  
   - Not directly applicable to heat pump water heaters but requires individual branch circuits for central heating systems.  

---

### **Key Notes**  
- **California Energy Code References**:  
  - Sections **150.0(n)** and **160.9** (single-family/multifamily) define specific readiness requirements but are **not included in CEC 2022 text**.  
- **NEC 2023**:  
  - No equivalent requirement. California mandates heat pump water heater readiness via **Title 24 Energy Code**, not NEC.  

---

## NEC 2023 Reference  
No equivalent requirement in NEC 2023. California mandates heat pump water heater readiness via Title 24 Energy Code, not NEC.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-005: electrification

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected Answer:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Reference:** CEC 408.2

### Agent's Answer:

## Electric Cooktop Readiness in New California Homes (CEC 2022)  

New California homes must comply with **dedicated infrastructure requirements** for electric cooktops under the California Energy Code (Title 24) and CEC 2022:  

---

### **Core Requirements**  
1. **Dedicated Circuits**  
   - **Single-family homes**: Must include **dedicated circuits** for electric cooktops per **California Energy Code Section 150.0(u)** (CEC 2022 422.3(A)).  
   - **Multifamily buildings**: Requires **dedicated circuits** per **California Energy Code Section 160.9(b)** (CEC 2022 422.3(B)).  

2. **Panelboard Spaces**  
   - Panelboards must reserve **circuit breaker spaces** for electric cooktops:  
     - **Single-family**: As specified in **California Energy Code Section 150.0(u)** (CEC 2022 408.2(A)).  
     - **Multifamily**: As specified in **California Energy Code Section 160.9(b)** (CEC 2022 408.2(B)).  

3. **Electrification Mandate**  
   - California mandates **readiness for all-electric appliances** (including cooktops) in new residential construction to align with climate goals (Title 24 Part 6, CALGreen).  

---

### **Exceptions and Special Cases**  
- **422.33 (Disconnection Requirements)**:  
  - Cord-and-plug-connected cooktops may use a **receptacle as the disconnecting means**, provided it meets accessibility and rating requirements. This does not negate the need for dedicated circuits.  
  - Example: A cooktop with a plug-and-receptacle connection must still have a dedicated circuit sized per 422.3.  

- **210.52(C) (Receptacle Placement)**:  
  - Receptacles behind cooktops are exempt from wall-space requirements (Exception in 210.52(C)(1)). This applies to **installation** but does not affect the **readiness** mandate for dedicated circuits.  

---

### **NEC 2023 Reference**  
NEC 2023 covers **installation standards** (e.g., branch circuit sizing, receptacle placement) but **does not mandate** dedicated circuits or panelboard spaces for electrification. California’s requirements are **stricter**, enforcing infrastructure for future all-electric adoption.  

---

✓ **Sources**: CEC 2022 (primary), NEC 2023 (comparison)  
✓ **Exceptions Checked**: 422.3, 408.2 (no overriding exceptions found for readiness mandates).

---

## cec-006: electrification

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected Answer:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Reference:** CEC 408.2

### Agent's Answer:

## Panelboard Requirements for Electric Clothes Dryers in California (CEC 2022)  

### **Single-Family Buildings**  
- **Panelboard Spaces**: Panelboards must include **designated circuit breaker spaces** for electric clothes dryers as specified in **California Energy Code Section 150.0(v)** (CEC 408.2(A) and 422.3(A)).  
- **Dedicated Circuits**: A **dedicated circuit** with proper circuit identification is required for electric clothes dryers (422.3(A)).  

### **Multifamily Buildings**  
- **Panelboard Spaces**: Panelboards must include **designated spaces** for electric clothes dryers per **California Energy Code Section 160.9(c)** (CEC 408.2(B) and 422.3(B)).  
- **Dedicated Circuits**: A **dedicated circuit** with circuit identification is required for each dwelling unit’s electric clothes dryer (422.3(B)).  

### **Key Exceptions**  
1. **Shared Laundry Facilities**: In multifamily buildings, **receptacles for laundry equipment** are not required if on-site laundry facilities serve all occupants (210.52(F) Exception No. 1).  
   - *Note*: This exception applies to receptacles, not panelboard circuit spaces.  

2. **Special Permission**: Appliances installed with non-standard methods require **special permission** (422.23, 424.10).  
   - *Note*: Does not override the dedicated circuit/space requirements.  

### **Conclusion**  
California mandates **dedicated panelboard spaces and circuits** for electric clothes dryers in both single-family and multifamily buildings. Exceptions exist only for receptacle requirements in multifamily buildings with shared laundry facilities, but **no exceptions remove the panelboard circuit space/circuit requirements**.  

---
## NEC 2023 Reference  
NEC 2023 does **not** mandate dedicated panelboard spaces or circuits for electric clothes dryers. California’s requirements are **more stringent** and specific to Title 24 energy code.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-007: overcurrent

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected Answer:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Reference:** CEC 240.4(G), Table 240.4(G)

### Agent's Answer:

## CEC Table 240.4(G) - Exception Analysis (CEC 2022)

After calling `cec_exception_search("440.3", "California amendment")`, **no direct exceptions** to Table 240.4(G) were found. However, the returned exception in **Section 394.12** highlights California's broader approach to enforcing wiring methods referenced in Table 240.4(G):

1. **Knob-and-Tube Wiring Exception**  
   While not directly related to Table 240.4(G), this exception demonstrates California's **strict enforcement of wiring method compatibility** with overcurrent protection requirements. For example:
   - Air-conditioning circuits (referenced in Table 240.4(G) row 1) must not use obsolete wiring methods unless grandfathered under 394.12.
   - This reinforces that **Table 240.4(G) applications must comply with modern wiring standards** (e.g., THHN/THWN conductors) unless specifically exempted.

2. **Implications for Table 240.4(G) Enforcement**  
   - California inspectors may reject non-compliant conductor types (e.g., knob-and-tube) for specialized circuits listed in Table 240.4(G), even if NEC allows them.
   - The "delta" amendments in **440.3(C)∆** (CALGreen requirements) indirectly interact with this exception by mandating modern, energy-efficient wiring methods for HVAC circuits.

---
## Final Verification
- **No direct exceptions** to Table 240.4(G) exist in CEC 2022.
- The returned exception (394.12) illustrates California's **wiring method enforcement philosophy**, which impacts how Table 240.4(G) is applied in practice.
- All prior conclusions about Title 24/CALGreen integration remain valid.

✓ Sources: CEC 2022 Table 240.4(G), Section 440.3(C)∆, Section 394.12

---

## cec-008: surge_protection

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected Answer:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Reference:** CEC 242.3, Table 242.3

### Agent's Answer:

## CEC Table 242.3 Specifications (CEC 2022)

**Purpose**: Cross-reference table for Article 242 (Overvoltage Protection) directing users to other NEC articles containing overvoltage protection requirements for specific equipment types. This is a **California-specific NEW table** (N marker) not found in NEC.

**Equipment and Corresponding Articles**:
- Class I locations → Article 501 (Hazardous Locations)
- Class II locations → Article 502 (Hazardous Locations)
- Community antenna TV/radio systems → Article 820
- Critical operations power systems → Article 708
- Elevators/dumbwaiters → Article 620
- Emergency systems → Article 700
- Equipment >1000V → Article 490
- Fire pumps → Article 695
- Industrial machinery → Article 670
- Information technology equipment → Article 645
- Modular data centers → Article 646
- Outdoor overhead >1000V → Article 399
- Radio/TV equipment → Article 810
- Receptacles/cord connectors → Article 406
- Wind electric systems → Article 694

**Code Reference**:  
CEC 2022 Section 242.3 explicitly requires equipment to be protected against overvoltage per the referenced articles in Table 242.3.

**Exceptions**:  
No direct exceptions apply to Table 242.3 itself. The only exception found (Section 370.23) relates to **overcurrent protection for cablebus**, which is unrelated to Table 242.3's overvoltage protection scope.

---
## NEC 2023 Reference
This table is **unique to CEC 2022** and does not exist in NEC 2023. California added this cross-reference table to clarify overvoltage protection requirements for specific equipment types.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-009: motor_control

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected Answer:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum conductors.

**CEC Reference:** CEC 430.72(B), Table 430.72(B)

### Agent's Answer:

## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)

**Specifies maximum overcurrent protective device ratings (in amperes) for motor control circuits based on conductor size and installation configuration.**

### Conductor Sizes and Ratings:
| Conductor Size | Column A (Copper) | Column A (Aluminum) | Column B (Copper) | Column B (Aluminum) | Column C (Copper) | Column C (Aluminum) |
|----------------|-------------------|---------------------|-------------------|---------------------|-------------------|---------------------|
| 18 AWG         | 7A                | —                   | 25A               | —                   | 7A                | —                   |
| 16 AWG         | 10A               | —                   | 40A               | —                   | 10A               | —                   |
| 14 AWG         | (Note 1)          | —                   | 100A              | —                   | 45A               | —                   |
| 12 AWG         | (Note 1)          | (Note 1)            | 120A              | 100A                | 60A               | 45A                 |
| 10 AWG         | (Note 1)          | (Note 1)            | 160A              | 140A                | 90A               | 75A                 |
| >10 AWG        | (Note 1)          | (Note 1)            | (Note 2)          | (Note 2)            | (Note 3)          | (Note 3)            |

---

### Notes:
1. **(Note 1):** See 310.15 for applicable ampacity adjustments.
2. **(Note 2):** 400% of values in **Table 310.19** for 60°C conductors.
3. **(Note 3):** 300% of values in **Table 310.16** for 60°C conductors.

---

### Key Exceptions:
1. **Critical Motor Circuits** (430.225):  
   - Overload protection can be replaced with a supervised alarm if motor failure would create a greater hazard (e.g., fire pumps).

2. **Combined Overcurrent Protection** (430.55):  
   - Overload and fault-current protection can be combined in a single device if it meets 430.32 requirements.

3. **Control Circuit Protection** (430.72 Exceptions):  
   - **Exception 1**: Control circuits posing a hazard if interrupted (e.g., fire pumps) only require short-circuit/ground-fault protection, not separate overload protection.
   - **Exception 2**: Transformers in control circuits <50 VA may use primary-side protection without separate overcurrent devices.

4. **Transformer Protection** (430.72(C)):  
   - Control circuit transformers <2A primary current can use primary overcurrent devices rated ≤500% of primary current.

---

### Supporting Code References:
- **CEC 430.71** confirms general motor control circuit requirements.
- **CEC 430.74** adds safety rules for grounded control circuits.
- **CEC 430.39** allows motor controllers to serve as overload protection under specific conditions.

---

## NEC 2023 Reference
No difference from NEC 2023. Table 430.72(B) and exceptions are identical in CEC 2022 and NEC 2023.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-010: medium_voltage

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected Answer:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Reference:** CEC 311.60(C), Tables 311.60(C)(67-86)

### Agent's Answer:

## Medium Voltage Cable Tables in CEC 2022 (Not in NEC)

California's CEC 2022 includes **18 specialized medium voltage (MV) cable ampacity tables** (311.60(C)(67) through 311.60(C)(86)) that are **not present in the NEC**. These tables address unique installation scenarios for MV cables (2001–35,000 volts) and include configurations not covered in national code.

---

### **California-Only Medium Voltage Tables**
**Tables 311.60(C)(67)–(86):**  
These tables provide ampacities for MV cables in specific installation methods:
1. **Triplexed cables in air** (C67/C68)  
2. **Isolated cables in air** (C69/C70)  
3. **Three-conductor cables in air** (C71/C72)  
4. **Triplexed cables in conduit** (C73/C74)  
5. **Three-conductor cables in conduit** (C75/C76)  
6. **Underground electrical duct (three-conductor)** (C77/C78)  
7. **Directly buried single conductors** (C81/C82)  
8. **Directly buried three-conductor cables** (C83/C84)  
9. **Triplexed directly buried cables** (C85/C86)  

---

### **Key Exceptions and Installation Requirements**
1. **Ampacity Selection (311.60(A)(2)):**  
   - If multiple ampacities apply, use the **lowest value**.  
   - Exception: Higher ampacity can be used for short segments (≤ 10 ft or 10% of total circuit length).  

2. **Shielding Requirements (311.44):**  
   - MV cables above 2000V must be **shielded** and grounded.  
   - Exceptions allow nonshielded cables up to 2400V in industrial settings with qualified personnel.  

3. **Direct-Burial (311.36):**  
   - MV cables must be **shielded** for direct burial.  
   - Exception: Nonshielded cables with metallic sheathing are permitted up to 2400V.  

4. **Cable Tray Installations (311.32):**  
   - MV cables in trays must comply with **392.80(B)** for ampacity adjustments.  

---

### **NEC 2023 Reference**
The NEC does not include Tables 311.60(C)(67)–(86). Its MV ampacity guidance is limited to general cases in **NEC 311.60**, without the detailed installation-specific adjustments found in California code.

---

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected Answer:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Reference:** CEC Table 310.16

### Agent's Answer:

## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

The ampacity of **4/0 AWG copper conductor at 75°C** is **230 amperes** per **CEC Table 310.16**. 

After reviewing exceptions via **cec_exception_search(310.16)**, no California-specific exceptions modify this base ampacity value for 4/0 AWG copper conductors in standard applications. The returned exceptions primarily address:
- Parallel conductor installations (310.10(G))
- Environmental conditions (dry/wet locations, sunlight exposure)
- Direct-burial requirements
- Corrosive environments

These exceptions do not override the base ampacity value from Table 310.16 for standard installations.

---
## NEC 2023 Reference
No difference from NEC 2023 Table 310.16 for this conductor size and temperature rating.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---
### Important Notes:
1. **Ambient Temperature**: This value assumes 30°C ambient temperature (see footnote [1]). For different temperatures, apply correction factors from **CEC 310.15(B)**.
2. **Bundling**: If more than 3 current-carrying conductors are bundled, apply derating per **CEC 310.15(C)(1)**.
3. **Overcurrent Protection**: Maximum overcurrent protection limitations are governed by **CEC 240.4(D)**.

No California-specific exceptions apply to this basic ampacity lookup.

---

## cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected Answer:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Reference:** CEC Table 250.122

### Agent's Answer:

## Equipment Grounding Conductor Size (CEC 2022)  

For a **200A circuit**, the required equipment grounding conductor (EGC) is:  
- **6 AWG copper**  
- **4 AWG aluminum/copper-clad aluminum**  

This is per **CEC 2022 Table 250.122**, with no applicable exceptions overriding this size for standard 200A circuits.  

### Key Exceptions Reviewed:  
1. **Section 250.142** allows using the grounded conductor for grounding in specific supply-side scenarios, but this does not affect EGC sizing for standard circuits.  
2. **Section 250.121** prohibits using an EGC as a grounding electrode conductor (GEC), which is unrelated to this question.  
3. **Section 250.54** permits auxiliary grounding electrodes but does not modify EGC sizing requirements.  

No exceptions apply to a standard 200A circuit’s EGC size.  

---  
## NEC 2023 Reference  
NEC 2023 Table 250.122 specifies the same 6 AWG copper/4 AWG aluminum for 200A circuits. California’s amendments do not alter this requirement for standard applications.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected Answer:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Reference:** CEC Table 250.66

### Agent's Answer:

## Grounding Electrode Conductor (GEC) Sizing (CEC 2022)

For a **3/0 AWG copper service conductor**, the required **grounding electrode conductor (GEC)** size is:

- **4 AWG copper** (per CEC Table 250.66)

### Exception Analysis:
After reviewing exceptions to 250.66, none directly modify the GEC sizing requirement for this scenario. Key exceptions include:
1. **250.54** (auxiliary electrodes) – Permits additional electrodes but doesn't affect GEC size
2. **250.50** (grounding electrode system) – Requires bonding of electrodes, not related to conductor sizing
3. **250.121** – Prohibits using equipment grounding conductors as GECs (not applicable here)

The California amendment note in Table 250.66 indicates modifications from NEC, but in this case, the CEC and NEC requirements align (4 AWG copper for 3/0 service conductors).

---
## NEC 2023 Reference
NEC 2023 Table 250.66 also specifies 4 AWG copper for 3/0 AWG service conductors. **No difference** from CEC 2022.

✓ Sources: CEC 2022 Table 250.66 (primary), NEC 2023 Table 250.66 (comparison)

---

## cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected Answer:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Reference:** CEC Table 310.15(B)(1)(1)

### Agent's Answer:

## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** in a **40°C ambient temperature** is **0.88** per **CEC 2022 Table 310.15(B)(1)(1)**.

### Exceptions and Notes:
1. **Exception 2** in CEC 2022 Section 310.15 clarifies:
   - Temperature correction factors **can be applied** to the conductor's ampacity **if the corrected ampacity does not exceed** the ampacity for the temperature rating of the termination (per **110.14(C)**).
   - This ensures compatibility with termination temperature limits (e.g., 60°C for most residential terminations).

2. **Exception 3** in Section 310.14 allows higher ampacity for short circuit segments (≤10 ft or 10% of total length), but this does not override the correction factor itself.

---
## NEC 2023 Reference
No difference from NEC 2023 - Table 310.15(B)(1)(1) and exceptions are identical in both codes.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected Answer:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Reference:** CEC Table 310.15(C)(1)

### Agent's Answer:

## Ampacity Adjustment Factor for Bundling (CEC 2022)

For **7-9 current-carrying conductors** in a raceway, the ampacity adjustment factor is **0.70** per **CEC 2022 Table 310.15(C)(1)**.

**Key Notes:**
- This factor applies to all conductors in the same raceway (including neutrals and spares)
- Excludes conductors in separate circuits that cannot be simultaneously energized
- Applies to conductors rated 40°C or higher (see Table 310.15(C)(1) footnotes)

**Exceptions Checked:**
1. **Exception for >20 conductors**: Only applies to Type AC/MC cables with >20 conductors (not applicable here)
2. **Exception for cable trays**: Only affects raceways in cable trays (not applicable here)
3. **Exception for parallel conductors**: Requires separate adjustment (not applicable here)

---
## NEC 2023 Reference
No difference from NEC 2023 Table 310.15(C)(1).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected Answer:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Reference:** CEC Table 110.26(A)(1)

### Agent's Answer:

## Minimum Working Space Depth (CEC 2022)

For a **480V panelboard under Condition 3**, the minimum working space depth is **1.2 meters (4 feet)** per **CEC Table 110.26(A)(1)**. This applies to systems with nominal voltage to ground between **151-600V**.

**Condition 3** specifically covers scenarios with **exposed live parts on both sides** of the working space.

**Exceptions Reviewed:**
- No exceptions in CEC 2022 override this requirement for 480V panelboards under Condition 3.
- Exceptions related to dead-front assemblies (110.26(A)(1)), existing buildings (Exception No. 2), or wire-bending spaces (408.55) do not apply to this scenario.
- Cross-references to 110.33 (entrance requirements) and 408.38 (panelboard enclosures) are unrelated to working space depth.

---
## NEC 2023 Reference
No difference from NEC 2023 Table 110.26(A)(1). Both codes require 4 feet (1.2 m) for 480V systems under Condition 3.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected Answer:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Reference:** CEC Table 110.28

### Agent's Answer:

## Final Answer: Suitable Enclosure Types for Outdoor Use (CEC 2022)

For outdoor installations exposed to **rain, sleet, and ice**, the following enclosure types are suitable per **CEC Table 110.28** and exceptions:

### Approved Enclosure Types:
- **Type 3**: Raintight (operable when ice-covered).
- **Type 3S**: Raintight with corrosion protection.
- **Type 3SX**: Raintight with corrosion protection and sealed joints.
- **Type 3X**: Raintight with corrosion protection (severe environments).
- **Type 4**: Watertight (also raintight).
- **Type 4X**: Watertight with corrosion protection.
- **Type 6**: Watertight (resists water ingress).
- **Type 6P**: Watertight with flooding protection.

### Key Exceptions and Additional Requirements:
1. **Dedicated Space (110.26(E))**:
   - Outdoor enclosures must have **1.8 m (6 ft) dedicated clearance** from grade to equipment height.
   - Structural overhangs are permitted in the dedicated space zone.

2. **Fencing Requirements (110.31)**:
   - Fences for outdoor enclosures must be **at least 2.1 m (7 ft) high** or **1.8 m (6 ft) with barbed wire**.
   - Minimum distance from fence to live parts per **Table 110.31**.

3. **Industrial Systems (110.70 Exception)**:
   - Enclosures in industrial systems with **qualified supervision** may follow engineering practice (not applicable to general installations).

---
## NEC 2023 Reference
No difference from NEC 2023 Table 110.28.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected Answer:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Reference:** CEC Table 220.12

### Agent's Answer:

## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for **office buildings** in California is **3.5 volt-amperes (VA) per square foot** per CEC 2022 Table 220.12.

### Exceptions and Special Conditions:
1. **Energy Code Compliance** (CEC 220.12(B)):  
   If the building complies with a local energy code, the lighting load may be calculated using the energy code's unit values **if**:
   - A power monitoring system is installed to track lighting load.
   - The system has alarms to alert owners/managers if loads exceed energy code limits.
   - Demand factors from Table 220.42 are **not applied**.
   - The **125% continuous load multiplier** is used.

2. **Informational Note**:  
   The 3.5 VA/ft² value assumes 100% power factor and minimum load conditions. Installations with lower power factor or higher actual loads may require additional capacity.

---
## NEC 2023 Reference  
No difference from NEC 2023. NEC 2023 Table 220.12 also specifies 3.5 VA/ft² for office buildings.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected Answer:** 25 amperes per CEC 2022 Table 400.5(A)(1) [California Amendment]

**CEC Reference:** CEC Table 400.5(A)(1)

### Agent's Answer:

## 12 AWG Flexible Cord Ampacity (CEC 2022)

The ampacity of a **12 AWG flexible cord** with **Column B thermoset insulation** is **25 amperes** per CEC 2022 Table 400.5(A)(1). 

**Key Details:**
- Column B applies to **two-conductor cords** or multiconductor cords with **only two current-carrying conductors**
- This rating assumes **ambient temperature of 30°C (86°F)**
- See **400.13** and **Table 400.4** for additional construction requirements

**Exceptions Checked:**
- **400.12** restricts flexible cord use (e.g., not as fixed wiring substitute)
- **400.10** permits flexible cord use only for specific applications (e.g., appliances, luminaires)
- No exceptions modify the 25A value for 12 AWG Column B

---
## NEC 2023 Reference
No difference from NEC 2023 Table 400.5(A)(1).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected Answer:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Reference:** CEC Table 402.3

### Agent's Answer:

## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

**Maximum Operating Temperature**: **200°C (392°F)** for **Type SF-2 silicone insulated fixture wire** (solid or 7-strand), per **CEC Table 402.3**.

---

### Key Code Requirements:
1. **Permitted Uses** (CEC 402.10):  
   - Allowed in **luminaires** and similar equipment where:  
     - Conductors are **enclosed/protected**  
     - Not subject to **bending or twisting** in use  
     - Used to **connect luminaires** to branch-circuit conductors  

2. **Prohibited Uses** (CEC 402.12):  
   - **Not permitted** as general **branch-circuit conductors**  
   - Exceptions apply only where explicitly permitted elsewhere in the Code  

---

### Temperature Rating Details:
- **Type SF-2**: 200°C (392°F) for solid/7-strand  
- **Flexible stranding variants** (e.g., SFF-2): 150°C (302°F)  

---

## NEC 2023 Reference  
No difference from NEC 2023. Temperature ratings and usage restrictions for Type SF-2 are consistent between CEC and NEC in Table 402.3 and 402.10/402.12.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-021: adjusted_ampacity

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected Answer:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 x 0.88 x 0.70 = 30.8A

**CEC Reference:** CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)

### Agent's Answer:

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**: 50A (CEC Table 310.16 for 8 AWG THWN copper at 75°C)  
2. **Temperature Correction**: 0.88 (CEC Table 310.15(B)(1)(1) for 40°C ambient)  
3. **Bundling Adjustment**: 0.70 (CEC Table 310.15(C)(1) for 7 conductors)  

**Calculation**:  
$$
50A \times 0.88 \times 0.70 = 30.8A
$$

**Final Answer**: **30.8 amperes**  

---
## Exceptions Checked
- **Exception 310.15**: Confirmed correction factors are applied correctly without exceeding termination temperature ratings (75°C).  
- **Exception 310.12**: Not applicable (dwelling service rules not relevant here).  

---
## NEC 2023 Reference  
No difference from NEC 2023 (same tables and factors apply).  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected Answer:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Reference:** CEC Tables 310.16, 250.122, 250.66

### Agent's Answer:

## Service Sizing for 200A Residential (CEC 2022) with Exceptions Checked

### Final Sizing
✓ **Service conductor**: 2/0 AWG copper (CEC Table 310.12(A))  
✓ **EGC**: 6 AWG copper (CEC Table 250.122 for 200A)  
✓ **GEC**: 4 AWG copper (CEC Table 250.66 for 2/0 service conductor)  

### Exception Analysis
1. **310.12(A) Exceptions**:
   - **Exception 1** (Conductor types by location): Not applicable. Standard residential service conductors are sized per Table 310.12(A) without location-specific adjustments unless installed in wet/damp locations (not indicated in question).
   - **Parallel conductors**: Not applicable. Question specifies a standard 200A service, not parallel conductors.
   - **Temperature/ampacity adjustments**: No derating factors mentioned in the question, so Table 310.12(A) applies directly.

2. **California Amendments**:
   - Tables 250.122 and 250.66 include [California-specific requirements](#footnote1) for grounding conductors in residential applications, which are already reflected in the EGC/GEC sizes.

---
## NEC 2023 Reference  
- **Service conductor**: No difference from NEC 2023 Table 310.12(A)  
- **EGC/GEC**: NEC uses same tables (250.122/250.66) but **no amendments** for California-specific requirements  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

**Footnotes**  
[1] California amendments (δ) in Tables 250.122 and 250.66 reflect stricter requirements for grounding conductor sizing in residential applications compared to NEC.

---

## cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected Answer:** Per CEC Table 220.12, office buildings require 3.5 VA per square foot. General lighting load = 5,000 sq ft x 3.5 VA/sq ft = 17,500 VA (17.5 kVA).

**CEC Reference:** CEC Table 220.12

### Agent's Answer:

## General Lighting Load Calculation (CEC 2022)  

For a **5,000 sq ft office building**, the general lighting load is calculated using **Table 220.12** for non-dwelling occupancies:  

1. **Unit Load for Offices**:  
   Per CEC 2022 Table 220.12, **office buildings** require **3.5 VA per square foot** (includes 125% continuous load multiplier).  

2. **Calculation**:  
   $$
   5,000 \, \text{sq ft} \times 3.5 \, \text{VA/sq ft} = 17,500 \, \text{VA (17.5 kVA)}
   $$  

---

### Exceptions Checked  
- **CEC 220.12(B)**: Allows alternative lighting load calculations using energy code values **if** a power monitoring system is installed.  
  - **Not applicable here** (no monitoring system mentioned).  
- **Informational Note**: Table 220.12 values assume 100% power factor and minimum load conditions. Actual installations may require higher capacity.  

---

## NEC 2023 Reference  
No difference from NEC 2023. Table 220.12 specifies **3.5 VA/sq ft** for office buildings.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-024: motor_circuit

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected Answer:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Reference:** CEC Table 430.72(B)

### Agent's Answer:

## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit Conductors (CEC 2022)

The maximum overcurrent protection for **16 AWG copper conductors** in a motor control circuit extending beyond the enclosure in California is **10 amperes** under standard conditions. However, an exception allows **15 amperes** under specific motor load conditions.

---

### Key Requirements and Exceptions:
1. **Standard Rule (10A Protection):**  
   - 16 AWG copper conductors have an ampacity of **10A** at 60°C (CEC Table 310.16).  
   - Overcurrent protection must not exceed the conductor's ampacity (CEC 240.4(D)).  

2. **Exception for Small Motors (15A Protection):**  
   - **Per CEC 430.22(G)(2):**  
     - 16 AWG copper conductors are permitted for motors with a **full-load current rating** between **5.5A and 8A**, provided:  
       - Overcurrent protection is sized per **240.4(D)(2)(2)** (15A for 16 AWG).  
       - Overload protection complies with **430.32** (Class 10 or 10A overload protection).  
       - The circuit is protected per **430.52** (motor branch-circuit short-circuit and ground-fault protection).  

3. **Critical Conditions for Exception:**  
   - The motor must have a **full-load current rating** (per 430.6(A)(1)) **≤ 8A** and **> 5.5A**.  
   - Conductors must be installed in a **cabinet or enclosure**, part of a **jacketed multiconductor cable**, or in a **flexible cord**.  

---

### NEC 2023 Reference  
No difference from NEC 2023. NEC 240.4(D) and 430.22(G)(2) also permit 15A protection for 16 AWG conductors under the same conditions.  

---

**Final Answer:**  
- **Standard:** 10A (for general motor control circuits).  
- **Exception:** 15A **if** the motor’s full-load current is between 5.5A and 8A, and all conditions in CEC 430.22(G)(2) are met.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected Answer:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Reference:** CEC Table 220.12

### Agent's Answer:

## General Lighting Load Calculation (CEC 2022)

For a **2,400 sq ft dwelling unit**, the general lighting load is calculated using **CEC 2022 Section 220.14(J)** and **220.82(B)(1)**:

**Formula**:  
$$
\text{General Lighting Load} = \text{Floor Area} \times \text{Unit Load}
$$
$$
= 2,400 \, \text{sq ft} \times 3 \, \text{VA/sq ft} = 7,200 \, \text{VA}
$$

**Citations**:  
- **CEC 220.14(J)**: Minimum unit load of 3 VA/sq ft for dwelling units.  
- **CEC 220.82(B)(1)**: General calculated load includes 3 VA/sq ft for lighting and receptacles.

**Exceptions Checked**:  
- **CEC 220.85**: Applies to multi-unit dwellings (not relevant here).  
- **CEC 230.40**: Service-entrance conductor rules (no impact on lighting load).  
- **CEC 220.44**: Demand factors for non-dwelling units (not applicable to dwellings).  

---
## NEC 2023 Reference  
No difference from NEC 2023. NEC 220.14(J) also specifies 3 VA/sq ft for dwelling units.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-026: gfci

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected Answer:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Reference:** CEC 210.8(A)

### Agent's Answer:

## Kitchen GFCI Requirements Comparison (CEC 2022 vs NEC 2023)  
**With Exceptions Considered**

---

### **CEC 2022 Key Exceptions**  
1. **Ceiling Fans/Luminaires**:  
   - **Exempt**: Listed locking receptacles used with compatible attachment fittings for ceiling fans or luminaires **do not require GFCI** (Section 210.8, Exception).  
   - **NEC 2023**: No such exception exists—GFCI is required for all countertop receptacles, including those serving ceiling fans.  

2. **Receptacles Behind Appliances**:  
   - **Exempt**: Receptacles not readily accessible and dedicated to fixed appliances (e.g., ranges) are **exempt** from GFCI (Section 210.8, Exception).  
   - **NEC 2023**: No explicit exception for appliance-dedicated circuits; GFCI applies broadly.  

3. **Spacing Requirements**:  
   - **CEC**: Countertop receptacles must be within **600 mm (24 in)** of the outer end of peninsular countertops (Section 210.52(C)(2)(b)).  
   - **NEC**: Same spacing requirement, but **no exceptions** for appliance-mounted receptacles.  

---

### **NEC 2023 Key Differences**  
1. **No Exceptions for Ceiling Fans/Luminaires**:  
   - GFCI is required for **all countertop receptacles**, including those serving ceiling fans or luminaires.  

2. **Appliance-Dedicated Circuits**:  
   - **No exception** for receptacles behind fixed appliances; GFCI applies to all countertop receptacles unless explicitly exempted elsewhere (e.g., 422.5 for appliances).  

3. **Receptacle Spacing**:  
   - Same as CEC (24 in from peninsular ends), but **no exceptions** for appliance-mounted or locking receptacles.  

---

### **Restrictiveness Comparison**  
| **Aspect**                | **CEC 2022**                          | **NEC 2023**                          | **More Restrictive** |  
|---------------------------|---------------------------------------|---------------------------------------|----------------------|  
| **Ceiling Fans/Luminaires** | Exempt with locking receptacles       | GFCI required for all countertop receptacles | **NEC**              |  
| **Appliance-Dedicated Circuits** | Exempt if not readily accessible    | GFCI required unless exempted elsewhere | **NEC**              |  
| **General Countertop GFCI** | Required                              | Required                              | **Same**             |  

---

### **Conclusion**  
- **NEC 2023 is more restrictive** because:  
  1. It **does not allow exceptions** for ceiling fans/luminaires using locking receptacles.  
  2. It **requires GFCI for all countertop receptacles**, including those serving dedicated appliances, unless explicitly exempted (which CEC permits).  

- **CEC 2022** provides **specific exceptions** for certain installations (e.g., ceiling fans with locking receptacles), making it less restrictive in those scenarios.  

Both codes align on core GFCI requirements for kitchens, but NEC extends protection to edge cases where CEC allows exemptions.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-027: panelboard

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected Answer:** CEC 2022 Section 408.2 requires reserved panelboard spaces for heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers, and EV charging equipment. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification.

**CEC Reference:** CEC 408.2

### Agent's Answer:

## Final Answer: Panelboard Space Requirements (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirements**  
1. **Reserved Circuit Breaker Spaces** (CEC 408.2(A)):  
   - **Single-family dwellings** must have panelboards with **reserved spaces** for:  
     - Heat pump water heaters  
     - Heat pump space heaters  
     - Electric cooktops  
     - Electric clothes dryers  
   - Mandated by **California Energy Code Section 150.0**.  

2. **General Panelboard Rating** (CEC 408.30):  
   - Panelboard rating must match or exceed the **calculated feeder load** (per Article 220).  

3. **Wire-Bending Space** (CEC 408.55):  
   - Top/bottom wire-bending space must comply with **Table 312.6(B)** for the largest conductor.  
   - **Exceptions** apply for panelboards ≤225A with ≤42 overcurrent devices.  

---

### **NEC 2023 Requirements**  
1. **General Panelboard Rating** (NEC 408.30):  
   - Same as CEC: Panelboard rating must match or exceed the **calculated feeder load**.  

2. **Construction and Enclosure** (NEC 408.6, 408.38):  
   - Panelboards must be **dead-front** and mounted in approved enclosures.  
   - **No reserved spaces** required for specific appliances.  

3. **Wire-Bending Space** (NEC 312.6):  
   - Aligns with CEC 408.55, referencing **Table 312.6(A) and (B)**.  

---

### **Key Differences**  
| **Aspect**                | **CEC 2022**                                                                 | **NEC 2023**                          |  
|---------------------------|------------------------------------------------------------------------------|---------------------------------------|  
| **Reserved Spaces**       | **Mandates** reserved spaces for appliances in single-family dwellings.      | **No specific requirement**.          |  
| **Energy Code Integration** | Includes **California Energy Code** mandates (Section 150.0).              | No appliance-specific energy code mandates. |  
| **Wire-Bending Space**    | Same as NEC, with exceptions for ≤225A, ≤42-device panelboards.              | Same as CEC.                          |  

---

### **Exceptions Checked**  
- **CEC 408.2** exceptions referenced sections about **special permissions** for appliances (e.g., 422.23, 424.10), but these do not override the **reserved space requirement** in 408.2(A).  
- No exceptions negate the California Energy Code mandate for reserved spaces.  

---

### **NEC 2023 Reference**  
- NEC 2023 does **not include** California’s appliance-specific panelboard space requirements.  
- Reserved spaces for appliances are **California-only mandates** under **Title 24 Energy Code**.  

✓ **Sources**: CEC 2022 (primary), NEC 2023 (comparison)

---

## cec-028: ev_charging

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected Answer:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requirements.

**CEC Reference:** CEC 408.2, Title 24

### Agent's Answer:

## **Revised California EV Charging Requirements with Exceptions**  

### **California CEC 2022 Additions from Exceptions**  
1. **Load Management for Continuous Loads**  
   - **CEC 625.42**: EV charging loads are **continuous**, requiring service/feeder sizing based on product ratings. Automatic load management systems must limit service/feeder loads to their maximum permitted values. Adjustable settings require restricted access (e.g., locked doors, password-protected software).  

2. **Backfeed Prevention**  
   - **CEC 625.46**: Systems must prevent energy backfeed to premises wiring when utility power is lost, unless permitted by 625.48.  

3. **Ventilation Exceptions**  
   - **CEC 625.52**: Ventilation is **not required** if equipment is listed for indoor use without ventilation. Otherwise, mechanical ventilation must be interlocked with charging circuits.  

---

### **Updated Comparison with NEC 2023**  

| **Requirement**               | **California CEC**                                                                 | **NEC 2023**                                                                 |  
|-------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------|  
| **Load Management**           | Mandates automatic load management systems for continuous EV loads (625.42).    | General load management in 220.85; no EV-specific requirements.               |  
| **Backfeed Prevention**       | Explicitly requires anti-backfeed measures (625.46).                           | No EV-specific backfeed rules; general AC system requirements in 705.43.     |  
| **Ventilation**               | Ventilation required for indoor charging unless equipment is listed for indoors.   | No specific ventilation requirements for EV charging.                        |  
| **CALGreen Mandates**         | EV readiness in new construction (CALGreen Ch. 4 & 5).                           | No mandatory EV infrastructure in new construction.                            |  

---

### **Key Takeaways**  
- California’s **625.42** adds strict load management rules not found in NEC.  
- **625.46** introduces anti-backfeed requirements beyond NEC’s general PV/system interconnection rules.  
- Ventilation exceptions (**625.52**) clarify compliance paths for indoor EV charging.  

Always verify local amendments and CALGreen compliance for full adherence to California’s EV infrastructure mandates.

---

## cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected Answer:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Reference:** CEC 210.12

### Agent's Answer:

## AFCI Protection Requirements Comparison: CEC 2022 vs NEC 2023 (With Exceptions)

### **CEC 2022 Requirements (Section 210.12)**
1. **Scope**  
   - Applies to **15- and 20-ampere** branch circuits in dwelling units for areas like kitchens, family rooms, bedrooms, hallways, laundry areas, and similar rooms.  
   - **Permitted AFCI Types**:  
     - Combination-type AFCI (protects entire circuit).  
     - Branch/feeder-type AFCI + outlet branch-circuit-type AFCI at first outlet.  
     - Supplemental arc protection circuit breaker + outlet AFCI (with conductor length limits).  
     - Outlet branch-circuit-type AFCI at first outlet (for circuits in metal raceways or concrete-encased wiring).  

2. **Exceptions**  
   - Fire alarm systems (per 760.41(B)/760.121(B)) if installed in metal raceways.  
   - No AFCI required for branch circuit extensions ≤1.8 m (6 ft) without additional outlets.  

3. **Key Exceptions from cec_exception_search**  
   - **Section 210.11(C)(3)**: Bathroom branch circuits must have no other outlets, but this does not override AFCI requirements.  
   - **Section 210.52(A)**: Receptacle spacing rules do not affect AFCI application.  
   - **Section 230.40**: Service-entrance conductor rules are unrelated to AFCI requirements.  

---

### **NEC 2023 Requirements (Section 210.12)**
1. **Scope**  
   - Applies to **10-, 15-, and 20-ampere** branch circuits in dwelling units, dormitory units, and guest rooms.  
   - **Protected Locations**:  
     - Kitchens, bathrooms, garages, outdoors, crawl spaces, laundry areas, and similar areas.  
     - **Additional locations**: Boathouses, aquariums, and HVAC equipment (with expiring exception).  

2. **Exceptions**  
   - Fire alarm systems (per 760.41(B)/760.121(B)).  
   - **Arc welding equipment**: No AFCI required until January 1, 2025.  
   - **HVAC equipment**: Exempt until September 1, 2026 (NEC 2023).  
   - Short extensions (≤1.8 m/6 ft) without additional outlets.  

3. **Key Exceptions from NEC**  
   - **Section 210.12(E)**: Temporary exemption for arc welding equipment.  
   - **Section 210.12(F)**: Temporary exemption for HVAC equipment.  

---

### **Side-by-Side Comparison**
| **Feature**                | **CEC 2022**                          | **NEC 2023**                          |
|-----------------------------|---------------------------------------|---------------------------------------|
| **Applicable Circuits**     | 15- and 20-ampere                     | 10-, 15-, and 20-ampere               |
| **Protected Locations**     | Kitchens, bedrooms, family rooms, etc. | Includes bathrooms, garages, outdoors |
| **AFCI Types**              | Combination, branch/feeder, outlet    | Same, with system combination-type    |
| **Exceptions**              | Fire alarm systems, short extensions  | + Arc welding (until 2025), HVAC (until 2026) |
| **Code References**         | UL 1699, UL 1699A                     | UL 1699, UL 1699A, UL 1699C          |

---

### **Conclusion**
- **CEC 2022** focuses on dwelling units with broader "similar rooms" but excludes 10A circuits and arc welding exceptions.  
- **NEC 2023** expands AFCI requirements to 10A circuits, adds explicit locations (bathrooms, garages), and includes temporary exemptions for specialized equipment.  

**Sources**:  
- CEC 2022 Section 210.12 and exceptions (210.11, 210.52, 230.40)  
- NEC 2023 Section 210.12 and exceptions (210.12(E), 210.12(F))

---

## cec-030: solar_pv

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected Answer:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Reference:** CEC 690, Title 24 Part 6

### Agent's Answer:

## Final Answer: California Solar PV Requirements vs NEC 2023 Article 690

### 1. **Voltage Calculations (CEC 690.7 vs NEC 690.7)**
- **CEC 2022 690.7**:  
  - **Mandatory use of Table 690.7(A)** for crystalline silicon modules (California-specific correction factors).  
  - Voltage limits:  
    - 1000V for building-mounted systems  
    - 600V for residential systems  
    - 1500V for non-building locations  
  - **Exception**: Systems ≥100kW can use licensed engineer designs (690.7(3)).  

- **NEC 2023 690.7**:  
  - General temperature correction methods without California-specific tables.  
  - No voltage limit differentiation by installation type.  

---

### 2. **Circuit Sizing (CEC 690.8 vs NEC 690.8)**
- **CEC 2022 690.8(B)(1)**:  
  - Requires **125% of maximum current** without adjustment factors.  
  - **Exception**: Circuits with assemblies listed for continuous operation at 100% rating can use 100% (690.8(B)(1) Exception).  

- **NEC 2023 690.8**:  
  - Allows conductor sizing with or without adjustment factors (NEC 310.15).  
  - No exception for large systems.  

---

### 3. **Overcurrent Protection (CEC 690.9 vs NEC 690.9)**
- **CEC 2022 690.9(C)**:  
  - Permits **single overcurrent device** in DC circuits if paired with ground-fault protection.  
  - Devices must be **listed for PV systems**.  
  - **Exception**: Conductors ≤3m (10ft) in metal raceways can have protection on one end (690.9(A)(4)).  

- **NEC 2023 690.9**:  
  - No exception for single overcurrent devices with ground-fault protection.  
  - Less restrictive device listing requirements.  

---

### 4. **Arc-Fault Protection (CEC 690.11 vs NEC 690.11)**
- **CEC 2022 690.11**:  
  - **Mandatory** for DC circuits ≥80V **on or in buildings**.  
  - **Exception**: Systems in metallic raceways or underground (not in NEC).  

- **NEC 2023 690.11**:  
  - Requires arc-fault protection for DC circuits ≥80V but **no exception** for non-building locations.  

---

### 5. **Key California Exceptions**
- **Voltage Correction**: Table 690.7(A) (NEC lacks this).  
- **Arc-Fault Exception**: Non-building systems in metallic raceways (690.11 Exception).  
- **Overcurrent Exception**: Single device with ground-fault protection (690.9(C)).  

---

## NEC 2023 Reference
- **Differences**:  
  - California mandates **Table 690.7(A)** voltage corrections.  
  - Unique arc-fault exceptions for non-building systems.  
  - Functionally grounded system definition absent in NEC.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---

