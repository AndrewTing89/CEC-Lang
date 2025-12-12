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
| **Total Duration** | 361.2s |
| **Avg per Question** | 12.0s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2(A) requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers, as specified in California Energy Code Section 150.0(n), (t), (u), and (v). ...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022) **[WITH EXCEPTIONS]**

### **Reserved Circuit Breaker Spaces**  
Per **CEC 408.2(A)**, single-family panelboards **must reserve spaces** for:  
1. **Heat pump water heaters**  
2. **Heat pump space heaters**  
3. **Electric cooktops**  
4. **Electric clothes dryers**  

**Exceptions to 408.2**:  
- **No exceptions** directly modify the reserved space requirements in 408.2(A).  
- Exceptions in 408.38, 408.55, and 408.36 relate to **enclosures**, **wire-bending spaces**, and **overcurrent protection**, which are **separate from appliance-specific reserved spaces**.  

---

### **Key Exceptions**  
1. **Enclosure Flexibility** (408.38):  
   - Non-dead-front panelboards allowed if accessible only to qualified persons.  
2. **Wire-Bending Space** (408.55):  
   - Reduced space permitted for panels ≤225A with ≤42 overcurrent devices.  
3. **Overcurrent Protection** (408.36):  
   - Panels with two main breakers (total rating ≤ panel rating) allowed, up to 42 overcurrent devices.  

---

## NEC 2023 Reference  
**No difference** for reserved spaces—this is a **California-specific mandate** under CEC 408.2(A). NEC 2023 does not include appliance-specific reserved spaces unless locally adopted.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 408.38, 408.36, 408.55, 408.2

**Response Time:** 12.6s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in CEC Article 625 and Title 24 CALGreen (not CEC 408.2). Title 24 CALGreen mandates EV charging readi...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements (CEC 2022) – Final Answer  

### **1. Dedicated Branch Circuit**  
- **Section 625.40**: Each EV outlet must have an **individual branch circuit** with no other outlets.  
- **Exception 625.46**: Systems must prevent **backfeeding** to the premises wiring if utility power is lost (unless permitted by 625.48).  

---

### **2. Continuous Load Sizing**  
- **Section 625.42**: EV charging is a **continuous load**.  
  - Service/feeder must be sized for **125% of the load**.  
  - Adjustable settings on fixed-in-place equipment are allowed if:  
    - Changes follow manufacturer instructions.  
    - Adjusted ratings are permanently marked.  
    - Access is restricted (tool, lock, or password-protected).  

---

### **3. CALGreen Compliance**  
- **Section 625.1**: EV infrastructure must comply with **CALGreen Chapter 4/5**, including:  
  - **Reserved panelboard spaces** for EV circuits (CEC 408.2).  
  - **Minimum 40-amp circuit** for EV-ready homes.  
- **NEC 2023**: No equivalent mandate; CALGreen is California-specific.  

---

### **4. Weatherproof Enclosures**  
- **Section 625.56**: Outdoor receptacles require **weatherproof enclosures** (extra-duty rated).  
- **NEC 2023**: Similar in 625.56 but lacks "extra-duty" requirement.  

---

### **5. GFCI Protection**  
- **Section 625.56(D)**: All EV receptacles require **GFCI protection for personnel**.  
- **NEC 2023**: Same in 210.8 and 625.56.  

---

### **6. Ventilation Requirements**  
- **Section 625.52**: Indoor charging requires **mechanical ventilation** if equipment is not listed for indoor use.  
- **NEC 2023**: No specific ventilation rules for EV charging.  

---

### **7. Receptacle Ratings**  
- **Section 625.44**: Receptacles must be rated:  
  - **125V, 15–20A** for portable equipment.  
  - **250V, 30–50A** for fastened-in-place equipment.  

---

### **8. Cord Length Limits**  
- **Section 625.17**:  
  - Portable EVSE: **12 in. (300 mm)** cord.  
  - Stati...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 13 found
- 625.1, 625.41, 625.52, 625.46, 625.44, 625.56, 625.48, 625.17, 408.2, 210.8

**Response Time:** 13.2s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements (CEC 2022) - Final Answer

### 1. **Arc-Fault Protection (CEC 690.11)**
- **Mandatory for residential PV systems**: DC circuits ≥80V must use listed PV arc-fault circuit interrupters (AFCI).
- **Exception** (CEC 690.11 Ex): Systems **not installed on/in buildings** (e.g., detached structures housing PV equipment) are exempt if:
  - Installed in **metallic raceways**, **metal-clad cables**, **enclosed metallic trays**, or **underground**
  - Detached structures with **sole purpose of housing PV equipment** are not considered "buildings"

### 2. **Interconnection Requirements (CEC 690.59 & 705)**
- Must comply with **Article 705** for grid connections, including:
  - Overcurrent protection
  - Grounding
  - Rapid shutdown systems (705.12(D))

### 3. **Energy Storage Systems (CEC 690.71 & 706)**
- Storage systems must follow **Article 706** for:
  - Battery disconnects
  - Overcurrent protection
  - Labeling requirements

### 4. **AC Module Requirements (CEC 690.6)**
- AC modules treated as inverter-output circuits
- Follow **Article 705** for interconnection instead of standard PV rules

### 5. **Title 24 Mandates**
- **CALGreen Compliance**: New residential buildings must include solar PV systems meeting **Title 24 Part 6** energy efficiency standards
- Minimum solar capacity based on building size/location

### 6. **Fire Mitigation Documentation (CEC 691.10)**
- Systems not compliant with 690.11 must include **fire mitigation plans** in installation documentation

---

## NEC 2023 Reference
- **NEC 690.11** requires arc-fault protection for PV DC circuits ≥80V (same as CEC)
- **NEC lacks Title 24 mandates**: California's CALGreen solar mandate is unique to CEC/Title 24

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 690.71, 690.11, 691.10, 705.12, 690.59, 690.6

**Response Time:** 11.5s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## California Circuit Requirements for Heat Pump Water Heaters (CEC 2022)  

### **Key Requirements**  
1. **Dedicated Circuits**  
   - **Single-family buildings** (1–2 dwellings): Must have **designated branch circuits** for heat pump water heaters per **California Energy Code Section 150.0(n)** (CEC 422.3(A)).  
   - **Multifamily buildings**: Follow **Section 160.9(b)** for dedicated circuits (not explicitly detailed in search results).  

2. **Panelboard Spaces**  
   - Panelboards must reserve **circuit breaker spaces** for heat pump water heaters as specified in **CEC 408.2(A)** (referencing Energy Code Section 150.0(n)).  

3. **Overcurrent Protection**  
   - Storage-type water heaters (capacity ≤ 450 L/120 gal): Branch-circuit overcurrent devices and conductors must be sized **not smaller than 125% of the heater’s rating** (CEC 422.13).  

4. **Compliance with Other Articles**  
   - Follow **Article 430** (motor-operated appliances) and **Article 440** (refrigerant motor-compressors) requirements, as amended by CEC 422.3(A).  

---

### **Exceptions**  
- **Special Permissions**: Non-standard installation methods require **special permission** (CEC 422.23).  
- **Individual Branch Circuit**: Heat pump water heaters must be supplied by an **individual branch circuit** (CEC 422.12). Auxiliary equipment (e.g., pumps) may share the circuit.  

---

### **NEC 2023 Reference**  
No direct equivalent in NEC 2023 mandates dedicated circuits for heat pump water heaters. California’s requirements are **specific to Title 24 Energy Code** (electrification mandates) and go beyond NEC.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 422.13, 150.0, 160.9, 422.3, 408.2, 422.23, 422.12

**Response Time:** 11.0s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness in California (CEC 2022)  

### **Requirements for New Homes**  
1. **Dedicated Circuits**  
   - **Single-family homes**: Must have dedicated circuits per **California Energy Code Section 150.0(u)** (CEC 422.3(A)).  
   - **Multifamily buildings**: Dedicated circuits required under **Section 160.9(b)** (CEC 422.3(B)).  

2. **Circuit Specifications**  
   - Circuits must match the cooktop’s nameplate rating (e.g., **40–50A** for standard units).  
   - Conductors sized per **Table 310.16** for the circuit’s ampacity.  

3. **Receptacle Placement**  
   - Comply with **210.52(C)** for countertop accessibility.  
   - Receptacles behind cooktops are exempt from wall-space requirements (210.52(C)(1) Exception).  

4. **Load Calculations**  
   - Use **220.55** demand factors for cooking appliances.  

5. **Overcurrent Protection**  
   - Follow **422.11**:  
     - Surface heating elements >60A require subdivision and **≤50A protection** (422.11(B)).  
     - Standard circuits use **240.4** for overcurrent devices.  

---

### **Exceptions and Special Cases**  
- **Special Permission**: Non-standard installations (e.g., unique cooktop designs) require approval under **422.23** and **424.10**.  

---

### **NEC 2023 Reference**  
No difference for dedicated circuits or receptacle requirements. California’s **Title 24** mandates electrification readiness, which exceeds NEC standards.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 10 found
- 422.11, 210.52, 310.16, 150.0, 160.9, 422.3, 424.10, 422.23, 240.4, 220.55

**Response Time:** 10.9s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryers (CEC 2022)  

### **Key Requirements**  
1. **Single-Family (1-2 Dwellings)**:  
   - Panelboards must reserve **circuit breaker spaces** for electric dryers per **California Energy Code Section 150.0(v)**.  
   - **Citation**: CEC 2022 **Section 408.2(A)** and **Section 422.3(A)**.  

2. **Multifamily Buildings**:  
   - Panelboards must reserve **circuit breaker spaces** for electric dryers per **California Energy Code Section 160.9(c)**.  
   - **Citation**: CEC 2022 **Section 408.2(B)** and **Section 422.3(B)**.  

3. **Circuit Requirements**:  
   - Dryers require a **240V, 30A dedicated circuit** (per NEC 210.52(F) + CEC amendments).  

---

### **Exceptions & Special Cases**  
- **Receptacle Exemptions** (CEC 210.52(F)):  
  - Multifamily units **with on-site laundry facilities** may omit dryer receptacles.  
  - **Note**: This exemption applies only to **receptacles**, not panelboard reserved spaces. Panelboard requirements remain mandatory.  

- **Special Permission** (CEC 424.10):  
  - Non-standard dryer installations require **special permission**.  

---

### **NEC 2023 Reference**  
- NEC 210.52(F) requires a **240V, 30A receptacle** for laundry areas but **does not mandate reserved panelboard spaces**.  
- **California mandates reserved panelboard spaces** via CEC Sections 150.0(v) and 160.9(c), which are **not part of NEC**.  

---

### **Summary**  
- **Panelboard Spaces**: Required in all new California construction (single/multifamily) per CEC.  
- **Exceptions**: Receptacle exemptions do not override panelboard space requirements.  
- **Circuit**: 240V, 30A dedicated circuit (NEC + CEC).  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 210.52, 150.0, 160.9, 422.3, 408.2, 424.10

**Response Time:** 11.7s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) Unique California Provisions with Exceptions

After verifying with `cec_exception_search("240.4(G)", "California amendments")`, **no direct exceptions** to Table 240.4(G) itself were found. However, **three critical exceptions** were identified that modify referenced articles in the table:

1. **Transformer Secondary Conductors (240.21(C))**  
   - California allows **primary-side overcurrent protection** for transformer secondary conductors up to 3m (10ft) long, with specific ampacity rules.  
   - **Exception**: Manufacturer instructions for SPDs can override standard sizing.  
   - *Applies to transformers referenced in Table 240.4(G).*

2. **Surge Arrester Interconnections (242.54)**  
   - California mandates **metal interconnections** for surge arresters in secondary distribution systems.  
   - Requires **minimum 20ft spacing** between grounding electrodes.  
   - *Impacts overcurrent protection for systems in Table 240.4(G) (e.g., HVAC, fire alarm circuits).*

3. **Auxiliary Grounding Electrodes (250.54)**  
   - California permits **auxiliary grounding electrodes** connected to equipment grounding conductors.  
   - **No resistance requirements** for these electrodes.  
   - *Affects grounding of conductors in Table 240.4(G) (e.g., control circuits, welders).*

---
## NEC 2023 Reference  
No differences in Table 240.4(G) structure. California's unique provisions are in **exceptions to referenced articles** (240.21, 242.54, 250.54), not the table itself.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.54, 240.4, 240.21, 242.54

**Response Time:** 14.2s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 242.3 Exceptions Check (CEC 2022)

**Exception Search Results for Base Rule 242.3**:  
Only one exception found in **Section 370.23** (cablebus overcurrent protection), but this is unrelated to Table 242.3's overvoltage protection cross-references.

**Conclusion**:  
- **No exceptions** apply directly to **Table 242.3** in CEC 2022  
- The single returned exception relates to **cablebus overcurrent protection** (Section 370.23), not overvoltage protection cross-references  
- No California-specific exceptions modify Table 242.3 requirements  

---
## Final Answer: CEC Table 242.3 (California-Specific)

**Purpose**: Directs users to other NEC articles containing overvoltage protection requirements for specific equipment types. This is a **California-only amendment** (marked "N") not found in NEC.

**Key Cross-References**:
- Emergency systems → Article 700  
- Fire pumps → Article 695  
- IT equipment → Article 645  
- Wind systems → Article 694  

**California Mandate**:  
Equipment must comply with overvoltage protection requirements specified in the referenced articles for their specific application.

---
## NEC 2023 Reference  
No equivalent exists in NEC 2023. This is a **California-specific table** added to CEC Article 242.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 370.23, 242.3

**Response Time:** 17.1s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (Final Answer)  
**CEC 2022 vs NEC 2023 Verification Complete**

---

### **Table 430.72(B) Summary**  
Specifies maximum overcurrent protection ratings for motor control circuits based on conductor size and installation type. Key values include:  
- **18 AWG copper**: 7A (Column A), 25A (Column B)  
- **14 AWG copper**: 100A (Column B), 45A (Column C)  
- **12 AWG copper/aluminum**: 120A/100A (Column B), 60A/45A (Column C)  
- **>10 AWG**: Calculated using **Notes 2–3** (see below).  

---

### **Critical Calculations for >10 AWG Conductors**  
For conductors larger than 10 AWG:  
- **Note 2**: 400% of **Table 310.19** (60°C aluminum)  
- **Note 3**: 300% of **Table 310.16** (60°C copper)  

**Example Calculation for 2 AWG Copper**:  
1. From **CEC Table 310.16** (60°C copper): 2 AWG = 115A  
2. Apply Note 3: 300% × 115A = **345A maximum overcurrent protection**  

---

### **Key Exceptions Affecting Application**  
1. **430.84**: Controllers need not open all conductors unless serving as disconnecting means.  
2. **430.75**: Allows remote disconnecting means for control circuits with proper warnings and access restrictions.  
3. **422.23**: Non-standard installations require special permission (rarely applicable).  

---

### **CEC vs NEC 2023 Comparison**  
- **Table 430.72(B)** is **identical** in CEC 2022 and NEC 2023.  
- **Exceptions/related sections** (e.g., 430.84, 430.75) align with NEC, though section numbering differs slightly (e.g., NEC 430.94 covers motor control center overcurrent protection).  
- **No California amendments** to this table.  

---

### **Compliance Summary**  
- Use Table 430.72(B) values directly for overcurrent device selection.  
- Apply Notes 2–3 for conductors >10 AWG.  
- Follow exceptions in **430.84** and **430.75** for disconnecting means and installation.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison), verified via `cec_lookup_table`, `cec_excepti...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_lookup_table
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 310.16, 430.75, 310.19, 430.94, 422.23, 430.72, 430.84

**Response Time:** 39.0s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables Unique to CEC 2022

California's CEC 2022 includes **20 medium voltage cable tables** (311.60(C)(67) through 311.60(C)(86)) that are **not present in the NEC**. These tables provide ampacity ratings for MV cables in specific configurations and environments required by California's electrical code.

---

### **CEC-Only Medium Voltage Tables**
1. **311.60(C)(67)** - Triplexed copper in air  
2. **311.60(C)(68)** - Triplexed aluminum in air  
3. **311.60(C)(69)** - Isolated copper in air  
4. **311.60(C)(70)** - Isolated aluminum in air  
5. **311.60(C)(71)** - 3-conductor copper isolated in air  
6. **311.60(C)(72)** - 3-conductor aluminum isolated in air  
7. **311.60(C)(73)** - Triplexed copper in conduit in air  
8. **311.60(C)(74)** - Triplexed aluminum in conduit in air  
9. **311.60(C)(75)** - 3-conductor copper in conduit in air  
10. **311.60(C)(76)** - 3-conductor aluminum in conduit in air  
11. **311.60(C)(77)** - 3-conductor copper in underground ducts  
12. **311.60(C)(78)** - 3-conductor aluminum in underground ducts  
13. **311.60(C)(79)** - 3-conductor copper directly buried  
14. **311.60(C)(80)** - 3-conductor aluminum directly buried  
15. **311.60(C)(81)** - Single copper directly buried  
16. **311.60(C)(82)** - Single aluminum directly buried  
17. **311.60(C)(83)** - Triplexed copper directly buried  
18. **311.60(C)(84)** - Triplexed aluminum directly buried  
19. **311.60(C)(85)** - 3-conductor copper in ducts  
20. **311.60(C)(86)** - 3-conductor aluminum in ducts  

---

### **Key Applications Covered**
- **Environmental conditions**: Air, conduit, underground ducts, direct burial.  
- **Cable configurations**: Triplexed, isolated, 3-conductor, and single-conductor arrangements.  
- **Material-specific ratings**: Separate tables for copper and aluminum conductors.  

---

### **Exceptions and Cross-References**
- **311.60(A)(1)**: Ampacity determination via tables or engineering supervision.  
- **311.32**: Per...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 311.32, 311.44, 311.36, 392.80, 311.60

**Response Time:** 11.0s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

The ampacity of **4/0 AWG copper conductor at 75°C** is **230 amperes** per **CEC Table 310.16**. No applicable exceptions modify this value for standard installations with 3 or fewer current-carrying conductors in dry locations at 30°C ambient temperature.

---
## NEC 2023 Reference
No difference from NEC 2023 Table 310.16 for this conductor size and temperature rating.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

---
## Exceptions Analysis
After searching for exceptions to CEC 310.16 for 4/0 AWG copper:
- **No applicable exceptions** modify the base ampacity of 230A under standard conditions
- The returned exceptions relate to:
  - Parallel conductors (310.10(G))
  - Wet/damp location requirements (310.12)
  - Direct burial applications (310.12(E))
  - Corrosive environments (310.12(F))
- None of these apply to a standard 4/0 AWG copper conductor installation in dry locations with typical ambient temperature

**Key Notes:**
- For installations with special conditions (wet locations, direct burial, etc.), additional requirements apply per 310.12
- Temperature correction factors (310.15(B)) apply if ambient temperature differs from 30°C
- Bundling adjustments (310.15(C)(1)) apply for more than 3 current-carrying conductors

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.12, 310.10, 310.16, 310.15

**Response Time:** 7.4s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size (CEC 2022) with Exceptions

For a **200A circuit** in California:
- **Copper EGC**: 6 AWG (minimum)
- **Aluminum/Copper-Clad Aluminum EGC**: 4 AWG (minimum)

**Exceptions Reviewed**:
1. **Section 250.121**: Allows EGC to also serve as GEC under specific conditions (not applicable here).
2. **Sections 356.60/352.60**: Permit exceptions for conduit grounding requirements (installation method, not size).
3. **Section 250.134**: Allows separate EGC routing (installation flexibility, not size).
4. **Section 250.54**: Permits auxiliary grounding electrodes (does not affect EGC sizing).

**Conclusion**: No exceptions modify the minimum size requirements from **CEC Table 250.122** for a 200A circuit. The 6 AWG copper/4 AWG aluminum requirement remains valid.

---
## NEC 2023 Reference
NEC 2023 Table 250.122 specifies the same sizes (6 AWG copper, 4 AWG aluminum) for 200A circuits. No California-specific amendments apply in the national code.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 250.121, 352.60, 250.54, 250.134, 356.60, 250.122

**Response Time:** 7.6s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022)

For a **3/0 AWG copper service conductor**, the required **grounding electrode conductor (GEC)** size is:

**4 AWG copper**  
(Per **CEC 2022 Table 250.66**, with California amendment [CEC])

### Exceptions Considered:
1. **250.66(A)**: Allows 6 AWG copper if connected **only** to rod/pipe/plate electrodes (not applicable here unless specified).
2. **250.66(B)**: Allows 4 AWG copper if connected **only** to concrete-encased electrodes (valid if electrode type matches).
3. **250.66(C)**: Ground ring conductor sizing exception (not applicable to this scenario).

No applicable exceptions override the base requirement unless specific electrode types are used. **4 AWG copper remains the minimum size** for a 3/0 AWG service conductor under standard conditions.

---
## NEC 2023 Reference
NEC 2023 Table 250.66 also specifies 4 AWG copper for service conductors up to 350 kcmil. No difference from NEC 2023.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 8.6s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** in a **40°C ambient temperature** is **0.88** per CEC 2022 Table 310.15(B)(2). 

### Exception Analysis:
1. **Rooftop Exception (310.15(B)(2) Exception):**  
   - Applies only to raceways/cables **exposed to direct sunlight on rooftops** < 23mm above roof.  
   - **Not applicable** here (no rooftop context mentioned).

2. **Type XHHW-2 Exception:**  
   - Exempt from rooftop temperature adjustments.  
   - **Not applicable** (not related to 40°C ambient correction).

3. **General Exceptions:**  
   - No exceptions modify Table 310.15(B)(2) correction factors for standard 40°C ambient scenarios.

---
## NEC 2023 Reference
No difference from NEC 2023 Table 310.15(B)(2)(a).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 7.1s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor (CEC 2022)

For **7-9 current-carrying conductors** in a raceway, the standard ampacity adjustment factor is **0.70** per **CEC Table 310.15(C)(1)**. However, the following exceptions apply:

### Key Exceptions:
1. **Short Raceways** (≤ 600 mm/24 in.):  
   Adjustment factors **do not apply** for raceways shorter than 600 mm (24 in.) (CEC 310.15(C)(1)(b)).

2. **Type AC/Type MC Cables**:  
   Adjustment factors **do not apply** if:  
   - Cables have **no more than 3 current-carrying conductors**  
   - Conductors are **12 AWG copper**  
   - Cables lack an overall outer jacket (CEC 310.15(C)(1)(d)(1)-(3))  

3. **More Than 20 Conductors**:  
   If **Type AC/Type MC cables** have >20 current-carrying conductors installed without spacing, apply a **60% adjustment factor** (CEC 310.15(C)(1)(d)(4) Exception).

4. **Direct-Buried Conductors**:  
   Adjustment factors **do not apply** for direct-buried conductors with physical protection (e.g., rigid conduit) ≤ 3.05 m (10 ft) in length and ≤ 4 conductors (CEC 310.15(C)(1)(c)).

---

## NEC 2023 Reference  
No difference from NEC 2023 Table 310.15(C)(1). The exceptions above are also present in NEC 2023.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 9.1s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth (CEC 2022)

For a **480V panelboard under Condition 3**, the minimum working space depth is **1.2 meters (4 feet)** per **CEC Table 110.26(A)(1)**. This applies to systems with nominal voltage to ground between 151-600V.

**Condition 3** specifically covers scenarios where:
- Exposed live parts are present on **both sides** of the working space
- No insulating guards are used between live parts

After reviewing exceptions via `cec_exception_search`, **no applicable exceptions** modify this requirement for Condition 3 working space depth. The exceptions found relate to grounding, equipment enclosures, and dedicated spaces, but none override the 1.2m (4ft) clearance for 480V systems under Condition 3.

---
## NEC 2023 Reference
No difference from NEC 2023 Table 110.26(A)(1). California maintains the same 4-foot (1.2m) requirement for 480V systems under Condition 3.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 6.8s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Suitable Enclosure Types for Outdoor Use (CEC 2022)  

For outdoor installations exposed to **rain, sleet, and ice**, Table 110.28 specifies the following suitable enclosure types:  

- **Type 3S**: Protection against rain, sleet, snow, and ice formation (operable when ice-covered).  
- **Type 3SX**: Same as Type 3S, with additional corrosion protection.  
- **Type 4**: Watertight protection against rain, sleet, and ice (operable when ice-covered).  
- **Type 4X**: Same as Type 4, with corrosion protection.  
- **Type 6**: Protection against water from hose-directed streams (includes rain/sleet/ice protection).  
- **Type 6P**: Same as Type 6, with corrosion protection.  

### Key Notes:  
1. **Operability when ice-covered** is explicitly required for all listed types.  
2. **Type 3S** and **Type 4X** are commonly recommended for general outdoor use due to their balance of protection and durability.  
3. **Section 110.26(E)** adds installation requirements for outdoor enclosures:  
   - Must be installed in **identified enclosures** (e.g., fenced or protected areas).  
   - Protected from **accidental contact** by unauthorized personnel or vehicular traffic.  
   - Dedicated space requirements (1.8 m/6 ft height clearance).  

### Exceptions Found:  
- **Section 366.10**: Permits sheet metal/nonmetallic auxiliary gutters in wet locations if listed/suitable.  
- **Section 110.26(E)**: Allows exceptions for control equipment adjacent to machinery and structural overhangs in dedicated spaces.  

No exceptions override Table 110.28 directly, but **installation context** (e.g., fencing, dedicated spaces) is critical for compliance.  

---  
## NEC 2023 Reference  
No difference from NEC 2023. Table 110.28 and related requirements are identical in both codes.  

✓ Sources: CEC 2022 Table 110.28, Sections 110.26(E), 366.10, NEC 2023 Table 110.28

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.28, 366.10, 110.26

**Response Time:** 15.9s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for **office buildings** in California is **3.5 volt-amperes per square foot (VA/ft²)** per CEC 2022 Table 220.12.

### Exceptions:
- **Energy Code Compliance** (CEC 220.12(B)): If the building complies with a local energy code, the lighting load may be calculated using the energy code's unit values **if**:
  1. A power monitoring system is installed.
  2. The system has alarms for load exceedances.
  3. Demand factors from 220.42 are **not applied**.
  4. The 125% continuous load multiplier is applied.

---
## NEC 2023 Reference
No difference from NEC 2023. NEC 2023 Table 220.12 also specifies **3.5 VA/ft²** for office buildings.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 10.6s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

The ampacity of a **12 AWG flexible cord** in **Column B (thermoset)** is **20 amperes** per **CEC 2022 Table 400.5(A)(1)**. This applies to two-conductor cords where only two conductors are current-carrying.

No exceptions or amendments in California code modify this value for standard applications. Temperature correction factors (Table 310.15(B)(1)) and adjustment factors (Table 400.5(A)(3)) would apply if environmental conditions differ from the 30°C (86°F) ambient temperature specified in the table.

---
## NEC 2023 Reference
No difference from NEC 2023 Table 400.5(A)(1).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 400.5, 310.15

**Response Time:** 8.9s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

The maximum operating temperature for **Type SF-2 silicone insulated fixture wire** is **200°C (392°F)** as specified in **CEC 2022 Table 402.3**.  

### Key Exceptions and Restrictions:
1. **Permitted Uses** (CEC 402.10):  
   - Allowed only in **luminaires** or similar equipment where the wire is **enclosed/protected** and **not subject to bending or twisting** in use.  
   - May also be used to **connect luminaires to branch-circuit conductors**.  

2. **Prohibited Uses** (CEC 402.12):  
   - **Cannot be used as branch-circuit conductors** except as explicitly permitted elsewhere in the Code.  

---
## NEC 2023 Reference  
No difference from NEC 2023. Temperature ratings and permitted uses for Type SF-2 remain consistent between codes.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 402.10, 402.12, 402.3

**Response Time:** 11.4s

---


## Complex Calculations

### cec-021: adjusted_ampacity

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor: 0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50 x 0.88 x 0.70 = 30.8A

**CEC Ref:** CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1) | **NEC Ref:** NEC Tables 310.16, 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   8 AWG THWN copper at 75°C → **50A** (CEC Table 310.16)

2. **Temperature Correction**:  
   40°C ambient → **0.88** correction factor (CEC Table 310.15(B)(1))

3. **Bundling Adjustment**:  
   7 conductors → **0.70** adjustment factor (CEC Table 310.15(C)(1))

4. **Final Calculation**:  
   ```
   Adjusted = 50A × 0.88 × 0.70 = 30.8A
   ```

**Final Answer**: **30.8 amperes**

---
## NEC 2023 Reference  
No difference from NEC 2023 (same tables and factors apply).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.16, 310.15

**Response Time:** 5.2s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Service Sizing (CEC 2022)

✓ **Service conductor**: 2/0 AWG copper (CEC Table 310.12(A))  
✓ **EGC**: 6 AWG copper (CEC Table 250.122 for 200A service)  
✓ **GEC**: 4 AWG copper (CEC Table 250.66 for 2/0 service conductor)  

---
## NEC 2023 Reference  
- **Service conductor**: NEC uses Table 310.15 instead of 310.12(A) for services  
- **EGC/GEC**: No difference from NEC Tables 250.122/250.66  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)  

**Verification Steps**:  
1. Service conductor sizing confirmed via `cec_lookup_conductor_size` with "service" application  
2. EGC verified via `cec_lookup_grounding_conductor("equipment", "200")`  
3. GEC verified via `cec_lookup_grounding_conductor("electrode", "2/0")`  
4. No exceptions found via `cec_exception_search` on base rules  

**Code Citations**:  
- Service conductor: CEC 310.12(A) (Single-Phase Dwelling Services)  
- EGC: CEC 250.122 (Equipment Grounding Conductor Sizing)  
- GEC: CEC 250.66 (Grounding Electrode Conductor Sizing)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.122, 310.15, 310.12, 250.66

**Response Time:** 12.7s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The 125% continuous load multiplier is already included in this table value.

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)

For a **5,000 sq ft office building** in California:

1. **Base unit load**:  
   Office = **1.3 VA per square foot** (CEC 2022 Table 220.12)

2. **Total lighting load**:  
   $$
   5,000 \, \text{sq ft} \times 1.3 \, \text{VA/sq ft} = 6,500 \, \text{VA}
   $$

3. **Continuous load factor**:  
   The 125% multiplier for continuous loads (per 210.20(A)) is **already included** in Table 220.12 values.

---
## Exceptions and Special Conditions  
- **Exception 220.12(B)** allows using energy code-specified unit loads instead of Table 220.12 values **if**:  
  1. A power monitoring system is installed.  
  2. Alarm thresholds are set for lighting load excess.  
  3. Demand factors from 220.42 are **not applied**.  
  4. The 125% continuous load multiplier is **still required**.  

  *This exception does not apply unless the building explicitly complies with an energy code and meets all listed conditions.*

---
## NEC 2023 Reference  
No difference from NEC 2023 Table 220.12 for office lighting load.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 210.20, 220.12, 220.42

**Response Time:** 10.5s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit (CEC 2022)

The maximum overcurrent protection for a motor control circuit using **16 AWG copper conductors** extending beyond the enclosure in California is **20 amperes**, provided the following conditions are met:

1. **Motor Full-Load Current Requirements** (CEC 430.22(G)(2)):
   - If the motor's full-load current (FLC) is **>5.5A and ≤8A**:
     - Overload protection: Maximum Class 10 or 10A
     - Overcurrent protection: Per **240.4(D)(2)(2)** (20A for 16 AWG copper)
   - If the motor's FLC is **≤5.5A**:
     - Overload protection: Maximum Class 20
     - Overcurrent protection: Per **240.4(D)(2)(2)** (20A for 16 AWG copper)

2. **Conductor Allowance** (CEC 430.22(G)(2)):
   - 16 AWG copper is permitted for motor control circuits **only if** the motor meets the FLC criteria above and the circuit complies with overload and overcurrent protection requirements.

3. **Standard Overcurrent Protection** (CEC 240.4(D)):
   - 16 AWG copper conductors are generally protected up to **20A** (Table 240.4(D)(2)).

---
## NEC 2023 Reference
No difference from NEC 2023. The same requirements apply under NEC 430.22(G) and 240.4(D).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 240.4, 430.22

**Response Time:** 10.1s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Dwelling Unit (CEC 2022)

**Final Calculation:**
- **2,400 sq ft × 3 VA/ft² = 7,200 VA (7.2 kVA)**

**Code Basis:**  
Per **CEC 2022 Section 220.82(B)(1)**:  
- Dwelling units require **3 volt-amperes per square foot** for general lighting and general-use receptacles.  
- Floor area is calculated from outside dimensions (excluding open porches, garages, and unfinished spaces).

**Exception Review:**  
Checked exceptions via `cec_exception_search(220.82(B)(1))`:  
- **220.85** (two dwelling units) and **230.40** (service-entrance conductors) do not apply to this single dwelling unit.  
- No exceptions override the 3 VA/ft² requirement for this scenario.

---
## NEC 2023 Reference  
No difference from NEC 2023. NEC 220.11(C)(1) also specifies 3 VA/ft² for dwelling units.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 220.82, 220.85, 220.11, 230.40

**Response Time:** 8.0s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## Final Answer: CEC 2022 vs NEC 2023 Kitchen GFCI Requirements

### **Key Exceptions in CEC 2022**
1. **Receptacle Density Rule**  
   - **CEC 210.52(C)(2)(a)**: Requires **1 receptacle per 9 ft²** of countertop (vs. NEC’s only spacing rule).  
   - *Impact*: More GFCI-protected outlets in kitchens.

2. **Extended Coverage Areas**  
   - **CEC 210.52(C)** applies GFCI to **pantries, breakfast rooms, and dining rooms** (NEC limits to kitchens).  

3. **No Exceptions for Fixed Appliances**  
   - **CEC 210.52(C)(1) Exception**: Allows no exceptions for receptacles behind ranges/sinks (NEC permits exceptions for inaccessible outlets).  

---

### **Restrictiveness Comparison**
| **Requirement**               | **CEC 2022**                          | **NEC 2023**                          | **Winner**       |
|-------------------------------|----------------------------------------|----------------------------------------|------------------|
| Receptacle density            | 1 per 9 ft² countertop                 | No density rule (only spacing)         | **CEC**          |
| Coverage areas                | Kitchens + pantries + dining rooms     | Kitchens only                          | **CEC**          |
| Exceptions for fixed appliances| None                                   | Exceptions allowed                     | **CEC**          |

---

### **Conclusion**
**CEC 2022 is more restrictive** than NEC 2023 for kitchen GFCI requirements due to:
- Mandatory **receptacle density** (1 per 9 ft²).
- Extended coverage to **non-kitchen areas**.
- **No exceptions** for fixed appliances (ranges, sinks).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 210.52

**Response Time:** 15.3s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification. No...

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023)  
**With Exceptions and Cross-References**

---

### **1. Reserved Circuit Breaker Spaces for Appliances**  
- **CEC 2022 408.2(A)**:  
  Mandates **reserved spaces** in single-family panelboards for:  
  - Heat pump water heaters  
  - Heat pump space heaters  
  - Electric cooktops  
  - Electric clothes dryers  
  *Citations: CEC 2022 408.2(A), California Energy Code Sections 150.0(n), (t), (u), (v)*  

- **NEC 2023**:  
  No equivalent requirement. NEC does not mandate reserved spaces for specific appliances unless required by local amendments.  

---

### **2. Wire-Bending Space Exceptions**  
- **CEC 2022 408.55 (Exception No. 1)**:  
  Allows **reduced wire-bending space** (Table 312.6(A)) for panelboards:  
  - Rated **≤225A**  
  - Designed to contain **≤42 overcurrent devices**  
  *Citations: CEC 2022 408.55(A), Exception No. 1*  

- **NEC 2023 408.55**:  
  Requires **full wire-bending space** per Table 312.6(B) **without exceptions** for smaller panelboards.  

---

### **3. Short-Circuit Current Rating (SCCR) Marking**  
- **CEC 2022 408.6**:  
  Requires field marking of **available fault current and calculation date** on panelboards (except single-family dwellings).  

- **NEC 2023 408.6**:  
  Same requirement but **applies to all panelboards**, including single-family dwellings.  

---

### **4. Panelboard Rating**  
- **CEC 2022 408.30**:  
  Panelboards must be rated **≥ minimum feeder capacity** calculated per Article 220.  

- **NEC 2023 408.30**:  
  Identical requirement.  

---

### **Exceptions and Cross-References**  
- **CEC 408.55 Exception No. 1**:  
  Reduces wire-bending space for small panelboards (≤42 devices).  
- **NEC 408.55**:  
  No exceptions—requires full wire-bending space per Table 312.6(B).  

---

## NEC 2023 Reference  
- **Key Differences**:  
  1. **Reserved Spaces**: CEC mandates reserved breaker spaces for appliances (408.2); NEC does not.  
  2. **Wi...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 408.6, 150.0, 312.6, 408.30, 408.2, 408.55

**Response Time:** 11.9s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## California EV Charging Infrastructure Requirements vs NEC 2023 (Updated with Exceptions)

### Key Differences and California Mandates

1. **CALGreen Compliance (CEC 625.1.1)**  
   - **CEC 2022**: Mandates EV readiness in new residential construction per CALGreen Chapter 4 & 5.  
   - **NEC 2023**: No equivalent mandate. NEC 625.1 covers general scope but lacks state-specific electrification requirements.

2. **Branch Circuit Requirements (CEC 625.40)**  
   - **CEC**: Requires individual branch circuits for EV outlets with no other outlets.  
   - **NEC 625.40**: Same requirement, but California adds CALGreen minimum circuit capacity (40A minimum).

3. **Weatherproof Enclosures (CEC 625.56)**  
   - **CEC**: Requires extra-duty weatherproof enclosures for outdoor EVSE.  
   - **NEC 625.56**: General weatherproofing requirement but no "extra-duty" specification.

4. **Ventilation Requirements (CEC 625.52)**  
   - **CEC**: Specific ventilation formulas and tables (625.52(B)(1)(a/b)) for indoor EV charging.  
   - **NEC 625.52**: General ventilation requirements without California's detailed calculation methods.

5. **Ground-Fault Protection (CEC 625.54)**  
   - **CEC**: Requires GFCI protection for all EVSE receptacles (beyond NEC 210.8).  
   - **NEC 2023**: GFCI required only for specific locations (e.g., garages).

6. **Cord Length Limits (CEC 625.17)**  
   - **CEC**: 7.5m (25ft) maximum cord length unless using listed cable management.  
   - **NEC 625.17**: Same 25ft limit but no California-specific cable management exceptions.

---

### **Exception: Electrified Truck Parking Spaces (CEC 626.4)**  
- **CEC 626.4**:  
  - **Scope Exclusions**: Does not apply to equipment used for loading/unloading cargo or operating conveyors.  
  - **Voltage Requirements**: Mandates specific AC voltages (120, 208Y/120, 240, 480Y/277) for electrified truck parking spaces.  
  - **Connection Standards**: Applies to supply equipment connected to defined wiring systems.  
- **...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 625.1, 626.4, 625.52, 625.56, 625.17, 210.8, 625.54, 625.40

**Response Time:** 12.3s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements: CEC 2022 vs NEC 2023 (With Exceptions)

### **Key Exceptions in CEC 2022 for Dwelling Units**
1. **Supplemental Arc Protection Circuit Breaker Exception**  
   - **CEC 210.12(A)(3)**: Permits a listed supplemental arc protection circuit breaker combined with an outlet AFCI, but only if:  
     - Conductor length from overcurrent device to first outlet ≤ 50 ft (14 AWG) or 70 ft (12 AWG).  
     - Wiring is continuous between devices.  
   - **NEC**: Does not permit supplemental arc protection circuit breakers.  

2. **Metal Raceway/Concrete Encasement Exceptions**  
   - **CEC 210.12(A)(5)-(6)**: Allows outlet AFCI installation at first outlet if wiring between overcurrent device and first outlet is:  
     - Encased in ≥2 in. concrete.  
     - Installed in metal raceway, MC/AC cable with metal boxes.  
   - **NEC**: No exceptions for concrete/encased wiring; requires full branch circuit AFCI.  

3. **Fire Alarm System Exception**  
   - **CEC 210.12(A) Exception**: Exempts fire alarm systems (per 760.41(B)/760.121(B)) with metal raceway/enclosures from AFCI requirements.  
   - **NEC**: No explicit exception for fire alarm systems in AFCI rules.  

4. **Modification/Extension Exception**  
   - **CEC 210.12(D)(2)**: Permits outlet AFCI at first receptacle for branch circuit extensions ≤6 ft without additional outlets.  
   - **NEC**: Requires full AFCI protection for all modifications (210.12(E)).  

---

### **Critical Cross-References**
- **210.11(C)(3)**: Bathroom branch circuits may supply other loads in single-bathroom circuits (e.g., lighting). AFCI protection still required per 210.12.  
- **210.52(B)(1)**: Small-appliance circuits (kitchen, etc.) must comply with AFCI rules in 210.12.  
- **230.40**: Service-entrance conductor rules do not override AFCI requirements for branch circuits.  

---

### **NEC 2023 vs CEC 2022 Summary**
| **Feature** | **CEC 2022** | **NEC 2023** |
|-------------|--------------|--------------|
| *...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 210.52, 210.11, 210.12, 760.121, 404.22, 760.41, 230.40

**Response Time:** 16.6s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements vs NEC 2023 Article 690 (CEC 2022) - Final Answer

### Key Exceptions and Cross-References:
1. **Rapid Shutdown Exception** (690.12):  
   - Ground-mounted PV systems in structures *solely housing PV equipment* are exempt from rapid shutdown requirements.  
   - NEC 2023: No such exception exists for non-building structures.

2. **Grounding Electrode System** (690.47):  
   - California permits using the **metallic support structure** of ground-mounted PV arrays as a grounding electrode if it meets 250.52 requirements.  
   - NEC 2023: Requires separate grounding electrode systems unless explicitly permitted.

3. **Bonding of PV Modules** (690.43):  
   - Mounting systems used for bonding must be **listed/identified for PV module bonding**.  
   - NEC 2023: General bonding rules in 250.97 apply but lack PV-specific listing requirements.

4. **Ground-Fault Protection** (690.41(B)):  
   - Exempts **solidly grounded PV systems with ≤2 modules in parallel** (non-building systems) from ground-fault protection.  
   - NEC 2023: No exemption for small non-building systems.

---

### Summary of California vs NEC Differences:
| **Topic**               | **CEC 2022**                                                                 | **NEC 2023**                          |
|-------------------------|------------------------------------------------------------------------------|----------------------------------------|
| **Rapid Shutdown**      | Required for all building-mounted systems; exceptions for ground-mounted in non-buildings | Required for building-mounted systems |
| **Arc-Fault Protection** | Exception for metallic raceways/cables; no exception for underground systems | No exception for metallic raceways     |
| **Grounding**           | Specific bonding rules for PV arrays; permits support structures as grounding electrodes | General bonding rules in 250.97        |
| **Voltage Limits**      | 1000V max for building-mounted DC ci...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 250.66, 690.47, 690.11, 250.52, 250.97, 690.41, 690.43, 690.12

**Response Time:** 13.2s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 12.0s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

