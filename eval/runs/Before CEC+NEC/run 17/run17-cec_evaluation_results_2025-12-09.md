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
| **Total Duration** | 394.0s |
| **Avg per Question** | 13.1s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2(A) requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers, as specified in California Energy Code Section 150.0(n), (t), (u), and (v). ...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022)

### **Panelboard Space Requirements**
Per **CEC 2022 Section 408.2(A)**, single-family residential buildings must have panelboards with **dedicated circuit breaker spaces** for specific appliances as mandated by the California Energy Code. This ensures future-ready electrical infrastructure for electrification.

---

### **Appliances Requiring Reserved Circuit Breaker Spaces**
The following appliances **must have reserved circuit breaker spaces** in single-family dwelling panelboards:
1. **Heat pump water heaters**  
2. **Heat pump space heaters**  
3. **Electric cooktops**  
4. **Electric clothes dryers**  

This requirement is specified in **California Energy Code Section 150.0(n), (t), (u), and (v)**, as referenced in CEC 408.2(A).

---

### **Exception Analysis**
After checking exceptions to CEC 408.2(A) using `cec_exception_search`, no exceptions were found that modify or relax the requirement for reserved circuit breaker spaces for the listed appliances. The exceptions returned (408.55, 408.38, 408.36, 424.97) pertain to wire-bending spaces, enclosures, overcurrent protection, and heating leads—none of which impact the appliance-specific reserved space mandate.

---

### **Key Notes**
- These reserved spaces are in addition to standard panelboard sizing requirements.
- The mandate supports California’s electrification goals and ensures panelboards can accommodate high-efficiency electric appliances.

✓ Source: CEC 2022 Section 408.2(A) and California Energy Code

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 408.55, 150.0, 408.2, 408.36, 424.97, 408.38

**Response Time:** 12.2s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in CEC Article 625 and Title 24 CALGreen (not CEC 408.2). Title 24 CALGreen mandates EV charging readi...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements (CEC 2022)  

### **Core Requirements for New Residential Construction**  
1. **Dedicated Branch Circuit** (CEC 625.40)  
   - Each EV charging outlet must be supplied by an **individual branch circuit** with **no other outlets**.  
   - **Exception**: 625.42 allows adjustable settings on fixed-in-place equipment if:  
     - Adjustments are **locked, tool-restricted, or password-protected**.  
     - Service/feeder sizing matches the adjusted current setting.  

2. **Connection Methods** (CEC 625.44)  
   - **Portable EVSE**: Use standard receptacles (15–50A, 125/250V AC or 60V DC max).  
   - **Fixed EVSE**: Permanently wired and fixed in place for higher-power installations.  

3. **Location Requirements** (CEC 625.50)  
   - **Indoor**: EVSE connectors must be at least **18 inches (450 mm)** above the floor.  
   - **Outdoor**: Connectors must be **24 inches (600 mm)** above grade unless listed for lower heights.  

4. **Weatherproof Enclosures** (CEC 625.56)  
   - Outdoor receptacles must use **weatherproof enclosures** (extra-duty rated) with the plug inserted or removed.  

5. **Ground-Fault Protection** (CEC 625.54)  
   - All EV charging receptacles require **GFCI protection** for personnel safety.  

6. **Ventilation** (CEC 625.52)  
   - Indoor charging areas must have **mechanical ventilation** if equipment requires it (e.g., for hydrogen generation).  
   - Ventilation formulas apply for multi-vehicle charging spaces.  

7. **CALGreen Mandates** (CEC 625.1)  
   - New residential buildings must include:  
     - **Reserved panel space** for EV circuits.  
     - **Conduit to parking spaces** for future EV charging infrastructure.  
     - Compliance with **CALGreen Chapter 4 & 5** for electrification readiness.  

8. **Overcurrent Protection** (CEC 625.42)  
   - EV loads are **continuous**, requiring service/feeder sizing at **125% of the load**.  
   - Adjustable settings on fixed equipment must be **locked or p...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 11 found
- 625.52, 625.42, 625.40, 625.46, 625.50, 625.48, 625.1, 625.56, 625.54, 625.60

**Response Time:** 14.9s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements (CEC 2022) with Exceptions

### 1. **Rapid Shutdown Labeling** (CEC 690.56)
- **Mandatory labels** at service equipment and on rapid shutdown switches:
  - "SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN" (9.5mm min. text, yellow background)
  - "RAPID SHUTDOWN SWITCH FOR SOLAR PV SYSTEM" (9.5mm red-on-white label)
- **Exception**: Ground-mounted PV systems in detached buildings (solely housing PV equipment) are **exempt** from rapid shutdown requirements per **690.12 Exception**.

### 2. **Grounding Requirements** (CEC 690.43/45/47)
- **Equipment grounding**: All metal parts must connect to grounding conductors per 250.134/136.
- **Grounding electrode connection**: PV arrays must tie to building grounding electrode system (250.52) with conductor sized per 250.66.
- **Solidly grounded systems**: Grounded conductor connects to electrode via 250.166-sized conductor.

### 3. **DC Arc-Fault Protection** (CEC 690.11)
- **All residential PV systems** with DC circuits ≥80V must have **listed PV arc-fault circuit interrupters**.
- **Exception**: Detached equipment buildings or metallic raceway installations.

### 4. **Voltage Limits** (CEC 690.7)
- **Residential systems**: Max DC voltage limited to **600V** (vs. NEC 1000V).
- Voltage calculations must use temperature correction factors (Table 690.7(A)) for crystalline modules.

### 5. **Circuit Sizing** (CEC 690.8)
- **Conductor sizing**: Minimum ampacity = 125% of max circuit current (690.8(B)(1)).
- **Module interconnects**: Sized for 125% of short-circuit current + overcurrent device rating.

### 6. **System Identification** (CEC 690.56)
- **Directory requirements**: Per 705.10, identify PV disconnects and interconnections at service equipment.
- **Stand-alone systems**: Comply with 710.15 for labeling and documentation.

---

### Key Exceptions
- **Rapid Shutdown Exemption**: Ground-mounted PV systems in detached buildings (solely housing PV equipment) are **not required** to comply ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 12 found
- 690.56, 690.7, 690.8, 250.134, 690.43, 690.11, 250.52, 250.66, 690.12, 705.10

**Response Time:** 18.8s

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
   - **Single-family buildings** (1–2 dwellings):  
     **CEC 422.3(A)** mandates **dedicated branch circuits** and circuit identifications for heat pump water heaters, as specified in **California Energy Code Section 150.0(n)**.  
   - **Multifamily buildings**:  
     **CEC 422.3(B)** requires dedicated circuits per **California Energy Code Section 160.9(b)**.

2. **Panelboard Spaces**  
   - **Single-family**: **CEC 408.2(A)** reserves circuit breaker spaces in panelboards for heat pump water heaters (per **Energy Code 150.0(n)**).  
   - **Multifamily**: **CEC 408.2(B)** requires reserved spaces per **Energy Code 160.9(a)**.

3. **General Compliance**  
   - **CEC 422.3** references **Article 430** (motor-operated appliances) and **Article 440** (refrigerant motor-compressors) for installation requirements, amended for heat pump water heaters.

---

### Exceptions Checked:
- **CEC 422.47** (temperature-limiting means for water heaters):  
  - Applies to **storage or instantaneous water heaters** but does not override dedicated circuit requirements.  
  - Requires temperature-limiting controls (not applicable to circuit design).  

- **CEC 422.12** (central heating equipment):  
  - Allows auxiliary equipment on the same branch circuit for central heating systems.  
  - **Does not apply** to heat pump water heaters, which require **dedicated circuits** per 422.3(A)/(B).

---

### Final Answer:
- **Single-family**: Dedicated circuits and panelboard spaces per **CEC 422.3(A)** and **408.2(A)**.  
- **Multifamily**: Dedicated circuits and panelboard spaces per **CEC 422.3(B)** and **408.2(B)**.  
- **No exceptions** relax the dedicated circuit requirement for heat pump water heaters.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 422.3, 150.0, 422.47, 408.2, 160.9, 422.12

**Response Time:** 14.7s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness in New California Homes (CEC 2022)  

### **Requirements**  
1. **Single-Family Homes**  
   - Must include **dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 150.0(u)**.  
   - Per **CEC 422.3(A)**, this applies to dwellings with one or two units.  

2. **Multifamily Buildings**  
   - Requires **dedicated circuits and circuit identifications** for electric cooktops per **California Energy Code Section 160.9(b)**.  
   - Covered under **CEC 422.3(B)** for buildings with multiple dwelling units.  

---

### **Exceptions and Additional Notes**  
1. **Disconnecting Means for Cord-and-Plug-Connected Cooktops**  
   - **CEC 422.33** allows an accessible **plug-and-receptacle connection** at the rear base of a range (e.g., a 40A, 240V receptacle) as the disconnecting means, provided it is accessible by removing a drawer.  
   - This applies if the cooktop uses a cord-and-plug connection instead of hardwiring.  

2. **Non-Standard Installations**  
   - **CEC 422.23** requires **special permission** from the authority having jurisdiction (AHJ) for cooktop installations using methods not covered by standard code provisions.  

---

### **Key Citations**  
- **CEC 2022 Section 422.3(A)** (Single-family requirements)  
- **CEC 2022 Section 422.3(B)** (Multifamily requirements)  
- **CEC 2022 Section 422.33** (Plug-and-receptacle disconnect exceptions)  
- **CEC 2022 Section 422.23** (Special permission for non-standard installations)  
- **California Energy Code Sections 150.0(u)** and **160.9(b)** (Dedicated circuit specifications)  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 422.23, 422.3, 150.0, 160.9, 422.33

**Response Time:** 19.0s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

In California new construction, panelboard requirements for electric clothes dryer circuits are specified in **CEC 408.2** and **422.3**, with references to the California Energy Code:

### **Single-Family Buildings** (CEC 408.2(A) + 422.3(A))
- Panelboards **must reserve circuit breaker spaces** for electric clothes dryers.
- Dryers require **dedicated circuits** as specified in **California Energy Code Section 150.0(v)**.
- Circuits must include:
  - **Dedicated branch circuits** sized for the dryer's nameplate rating (typically 30A or higher).
  - **Proper circuit identification** in the panelboard.

### **Multifamily Buildings** (CEC 408.2(B) + 422.3(B))
- Panelboards serving each dwelling unit must include:
  - **Dedicated circuits** for electric clothes dryers per **California Energy Code Section 160.9(c)**.
  - Circuits must be **sized and identified** to match dryer requirements (typically 30A minimum).

### Key Requirements:
- **No exceptions** for omitting dryer circuits in new construction.
- Dryer circuits must comply with **Article 422** (appliances) and **Article 220** (load calculations).
- Grounding: Frames of dryers must be connected to the equipment grounding conductor per **CEC 250.140**.

### Exception Check:
- **No applicable exceptions** were found that would relax these requirements for new construction. The exceptions related to grounding (408.40) and load calculations (220.54) do not override the mandatory panelboard readiness provisions.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 220.54, 422.3, 150.0, 408.2, 408.40, 160.9, 250.140

**Response Time:** 10.2s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) California-Specific Modifications (Final Answer)  

**Unique California Requirements in Table 240.4(G):**  

1. **Delta (△) Amendments**:  
   - The table includes **△ symbols** indicating California-specific modifications to NEC Table 240.4(G). These adjustments affect overcurrent protection for specialized conductors, such as:  
     - **Fire alarm systems** (ref. 760.43/45): California may enforce stricter overcurrent protection for fire alarm circuits due to enhanced fire safety mandates (Title 24, CALGreen).  
     - **Solar/welder circuits** (ref. 630.12): Adjustments for renewable energy systems (e.g., EV charging, solar PV).  

2. **Cross-References with Local Mandates**:  
   - The table directs users to NEC sections that California has modified. For example:  
     - **Fire alarm conductors** (760.43/45): California may require additional protection for fire alarm circuits in high-risk areas.  
     - **Motor circuits** (430, 440): Adjustments for energy efficiency (Title 24 Part 6) or electrification mandates.  

3. **Key California Uniqueness**:  
   - **Title 24 Compliance**: Overcurrent protection for HVAC (440) and lighting circuits aligns with California’s energy efficiency standards.  
   - **CALGreen Requirements**: Stricter rules for fire alarm and emergency systems in commercial buildings.  

**Exceptions Check**:  
- No direct exceptions were found for **Table 240.4(G)** itself. However, related exceptions in sections like **230.90** (service conductors) and **368.17** (busway overcurrent) may indirectly affect applications cross-referenced in Table 240.4(G).  

**Action**: Use `compare_with_nec("240.4(G)", "California overcurrent")` to identify exact amendments.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 630.12, 368.17, 240.4, 230.90, 760.43

**Response Time:** 26.3s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 242.3 Specifications (CEC 2022)  

**Table 242.3** specifies **overvoltage protection requirements** for equipment in California installations by directing to the applicable Code articles based on equipment type or location. Key details:  

1. **Core Requirement** (CEC 242.3):  
   Equipment must be protected against overvoltage in accordance with the article covering its type or location as specified in **Table 242.3**.  

2. **Prohibited Uses** (CEC 242.6):  
   Surge protective devices (SPDs) **shall not** be installed:  
   - On circuits **over 1000 volts**  
   - On **ungrounded systems**, **impedance grounded systems**, or **corner grounded delta systems** (unless listed for such use)  
   - Where SPD rating is **less than the maximum continuous phase-to-ground voltage** at the installation point  

3. **Exception Found**:  
   - **Section 370.23 Exception**: For cablebus overcurrent protection, exceptions permit compliance with **240.100 and 240.101** instead of the general overcurrent rules in 240.4.  
   - *Note: This exception relates to overcurrent protection (not overvoltage) and is not directly tied to Table 242.3 but highlights potential cross-references in related sections.*  

**See Table 242.3** for cross-references to specific articles governing overvoltage protection for different equipment types (e.g., motors, transformers, etc.).  

✓ Source: CEC 2022 Sections 242.3, 242.6, 370.23

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 240.100, 370.23, 242.6, 240.4, 242.3, 240.101

**Response Time:** 21.2s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)  
**Final Answer with Exceptions and Cross-References**

---

### **Key Exceptions from CEC 2022**  
1. **Exception No. 1 (430.72(B))**:  
   - **Hazardous Circuits**: For control circuits where opening the circuit would create a hazard (e.g., fire pump motors), **only short-circuit and ground-fault protection** is required.  
   - **Implication**: Overcurrent protection (e.g., fuses/circuit breakers) is **not required** for these circuits.  

2. **Exception No. 2 (430.72(B))**:  
   - **Transformer-Fed Circuits**: Conductors supplied by a **single-phase transformer with a two-wire secondary** may use **primary-side overcurrent protection**, scaled by the **secondary-to-primary voltage ratio**.  
   - **Example**: If the secondary conductor rating is 10A (from Table 430.72(B)) and the voltage ratio is 2:1, primary protection may be up to **20A**.  
   - **Restriction**: This applies **only to two-wire secondaries**. Other configurations require direct protection.  

---

### **Updated Application Rules**  
1. **Standard Protection (Non-Exception Cases)**:  
   - Use **Table 430.72(B)** values based on conductor size, material, and protection type (Columns A/B/C).  
   - For conductors **larger than 10 AWG**:  
     - Column B = **400% of Table 310.17** (60°C).  
     - Column C = **300% of Table 310.16** (60°C).  

2. **Hazardous Circuits (Exception No. 1)**:  
   - Apply **short-circuit/ground-fault protection only** (e.g., fuses or circuit breakers rated for these faults).  
   - **No overcurrent protection** (e.g., thermal overload devices) is required.  

3. **Transformer-Fed Circuits (Exception No. 2)**:  
   - For two-wire secondaries:  
     - Primary protection = **Secondary rating × (Secondary Voltage / Primary Voltage)**.  
   - For non-two-wire secondaries:  
     - Use **direct protection** per Table 430.72(B).  

---

### **Example Scenarios**  
1. **Fire Pump Control Circu...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.16, 430.72, 310.17

**Response Time:** 21.0s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in CEC 2022

California's CEC 2022 includes **18 medium voltage (MV) cable tables** not found in the NEC, covering Type MV cables (2001–35,000 volts). These are:

- **Tables 311.60(C)(67) through 311.60(C)(86)**  
  - **Applications**: Ampacities for MV cables in air, underground, and direct burial installations.
  - **Configurations**: Triplexed cables, three-conductor cables, single-conductor cables in ducts, and more.
  - **Adjustments**: Ambient temperature corrections (311.60(D)(4)) and burial depth derating (6% per 300 mm depth increase).

### Key Exceptions and Limitations:
1. **Ambient Temperature Adjustments** (311.60(D)(4)):  
   - Ampacities must be corrected for temperatures other than 40°C using Table 311.60(D)(4) or a provided formula.

2. **Burial Depth Derating** (311.60(D)(2)(b)):  
   - For depths exceeding table values, derate ampacity by **6% per 300 mm (1 ft)** of additional depth.

3. **Shield Grounding Adjustments** (311.60(D)(1)):  
   - Cables with shields grounded at multiple points require ampacity adjustments due to shield currents.

4. **Circuit Length Exception** (311.60(A)(2)):  
   - Higher ampacity sections are permitted if lower ampacity portions do not exceed **10% of total length** or **3.0 m (10 ft)**.

These tables and exceptions are unique to California and address MV installations beyond NEC scope, emphasizing environmental and configuration-specific derating factors.

✓ Source: CEC 2022 Sections 311.60 and exceptions

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 311.60

**Response Time:** 10.7s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Ampacity of 4/0 AWG Copper Conductor at 75°C (CEC 2022)

**Ampacity:** 230 amperes  
**Source:** CEC 2022 Table 310.16 (California Amendment)

**Key Notes:**
1. **Base Value:** 230A from Table 310.16 for 4/0 AWG copper at 75°C.
2. **Adjustments Required For:**
   - Ambient temperatures ≠ 30°C (use §310.15(B))
   - More than 3 current-carrying conductors (use §310.15(C)(1))
3. **Overcurrent Protection Limit:** 250A maximum (per §240.4(D) for 4/0 copper)
4. **Exceptions:** None apply generally – the exceptions in §440.6 relate to specific equipment (refrigeration motors) and do not affect standard conductor ampacity.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 240.4, 440.6, 310.16, 310.15

**Response Time:** 6.3s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size (CEC 2022)

For a **200A circuit** in California:
- **Copper EGC**: 6 AWG (per **CEC Table 250.122**)
- **Aluminum/Copper-Clad Aluminum EGC**: 4 AWG

### Exceptions and Special Conditions:
1. **Luminaires** (Section 410.44):  
   - Replacement luminaires may use alternative grounding methods (e.g., GFCI protection) if no EGC exists at the outlet.  
   - Applies only to lighting fixtures, not general circuits.

2. **Conduit Systems** (Sections 352.60/356.60):  
   - Exceptions permit using the grounded conductor for grounding in specific DC or separately run conductor scenarios.  
   - Does not apply to standard 200A AC circuits.

3. **Separate EGC Runs** (Section 250.134):  
   - Allows EGC to run separately from circuit conductors in fixed installations.  
   - Requires compliance with 250.118 for conductor sizing.

### Key Notes:
- The California amendment note (∆) indicates state-specific modifications exist in Table 250.122, but the 200A sizing remains unchanged from NEC.  
- Exceptions apply to **specific applications** (e.g., luminaires, DC systems) and **do not override** the general 200A EGC sizing rule.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 356.60, 352.60, 250.134, 250.118, 250.122, 410.44

**Response Time:** 7.5s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022)

For a **3/0 AWG copper service conductor**, the required **grounding electrode conductor (GEC)** size is:

- **4 AWG copper** (per CEC 2022 Table 250.66)  
  ⚠️ California amendment applies (delta symbol in table)

### Exception Analysis:
After reviewing exceptions to 250.66:
1. **250.54** (auxiliary electrodes) – Does not affect GEC sizing
2. **250.30(A)** (separately derived systems) – Not applicable for standard service
3. **250.190(B)** – Confirms GEC sizing based on largest ungrounded conductor
4. **250.32(E)** – Explicitly references Table 250.66 for GEC sizing

No exceptions override the 4 AWG requirement for 3/0 AWG service conductors. The California amendment note in the table indicates local modifications, but the size remains valid as calculated.

✓ Source: CEC 2022 Table 250.66 with exception review complete

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 250.54, 250.32, 250.30, 250.66, 250.190

**Response Time:** 8.4s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** in a **40°C ambient temperature** is:

**0.88** (per CEC 2022 Table 310.15(B)(1)(1))

### Exception Analysis:
Reviewed exceptions for 310.15(B)(1)(1) using `cec_exception_search`. The returned exceptions (352.60, 356.60, etc.) relate to **grounding conductor requirements** and **conduit expansion characteristics**, not temperature correction factors. None of these exceptions apply to the temperature correction calculation for ampacity adjustments.

No applicable exceptions modify this correction factor.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 352.60, 356.60, 310.15

**Response Time:** 5.8s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor for Bundling (CEC 2022)

The ampacity adjustment factor for **7-9 current-carrying conductors in a raceway** is **0.70 (70%)** per **CEC 2022 Table 310.15(C)(1)**. 

### Exceptions and Limitations:
1. **NM/NMC Cable Exception** (Section 334.80):  
   - If using **NM or NMC cables** installed in wood framing that will be sealed with insulation, caulk, or foam, the 0.70 factor still applies.  
   - The 90°C rating may be used for adjustment calculations, but the final ampacity must not exceed the 60°C rating of the conductor.

2. **Other Exceptions**:  
   - Adjustments do **not apply** for short raceway lengths (≤24 in.) or specific conduit types (e.g., rigid metal conduit with ≤4 conductors).  
   - Grounding/bonding conductors are **excluded** from the conductor count (Section 310.15(F)).

### Key Footnote:
- The conductor count includes **all current-carrying conductors** (including spares and neutrals) but **excludes** conductors connected to non-simultaneously energized components.

✓ Source: CEC 2022 Table 310.15(C)(1) and exceptions

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 334.80, 310.15

**Response Time:** 8.9s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth (CEC 2022)

For a **480V panelboard under Condition 3**, the minimum working space depth is:

**1.2 meters (4 feet)**  
Per **CEC 2022 Table 110.26(A)(1)** for voltages 151–600V.

### Exception Review:
- **Section 110.26(E)** addresses dedicated equipment space height (1.8 m/6 ft above equipment) but does not modify the working space depth requirement.
- Other exceptions (352.60, 356.60, 440.14) relate to grounding and disconnecting means, not working space depth.

### Condition 3 Context:
- Applies when **exposed live parts are on both sides** of the working space.
- This requirement ensures safe access for maintenance and reduces arc flash risk.

✓ Source: CEC 2022 Table 110.26(A)(1) and exceptions verified.

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 352.60, 440.14, 356.60, 110.26

**Response Time:** 7.8s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Final Answer: Suitable Enclosures for Outdoor Use with Rain, Sleet, and Ice (CEC 2022)

**Enclosure Types:**  
For outdoor use with **rain, sleet, and ice**, the following enclosure types are suitable per **CEC Table 110.28**:  
- **Type 3S** (Rain- and sleet-tight, ice-covered operable)  
- **Type 3SX** (Same as 3S with corrosion protection)  
- **Type 4** (Watertight, rain- and sleet-tight, ice-covered operable)  
- **Type 4X** (Same as 4 with corrosion protection)  
- **Type 6** (Watertight, rain- and sleet-tight, ice-covered operable)  
- **Type 6P** (Same as 6 with corrosion protection)  

### Key Code Requirements:
1. **Rain/Sleet Protection**: Types **3S, 3SX, 4, 4X, 6, 6P** are **raintight** (protect against rain/sleet).  
2. **Ice Operability**: All listed types must have **mechanisms operable when ice-covered** (CEC 110.28 footnote [*]).  
3. **Watertight Protection**: Types **4, 4X, 6, 6P** provide **watertight** protection against sleet and ice.  

### Exceptions and Additional Notes:
- **Receptacles in Wet Locations** (CEC 406.9):  
  - Must use **weatherproof enclosures** (e.g., Type 4 or 4X) whether the plug is inserted or removed.  
  - Weather-resistant receptacles (e.g., Type 5-15, 5-20) are required for 15/20A, 125/250V outdoor use.  

- **Dedicated Equipment Space** (CEC 110.26(E)):  
  - Structural overhangs or roof extensions are permitted in the dedicated space for outdoor equipment.  

### Supporting References:
- **CEC Table 110.28**: Defines enclosure types for environmental conditions.  
- **CEC 409.100**: Industrial control panels must comply with Table 110.28 for non-hazardous outdoor use.  
- **CEC 110.28 Footnotes**: Clarify terms like "raintight," "watertight," and operability requirements.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 110.28, 409.100, 406.9, 110.26

**Response Time:** 17.2s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)  

The **standard general lighting load** for office buildings in California is **1.3 VA per square foot** per **CEC Table 220.12**.  

### Exception for Energy Code Compliance  
Per **CEC 2022 Section 220.12(B)**, an alternative calculation using **local energy code values** is permitted if:  
1. A **power monitoring system** is installed to track total general lighting load.  
2. The system includes **alarms** to alert owners/managers if loads exceed energy code limits.  
3. **Demand factors from Table 220.42** are *not* applied to the lighting load.  
4. The **125% continuous load multiplier** is applied.  

This exception allows flexibility for buildings designed to meet stricter energy efficiency standards, provided the monitoring and control requirements are satisfied.  

✓ Source: CEC 2022 Sections 220.12, 220.42

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 9.6s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Final Answer: Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

The ampacity of a **12 AWG flexible cord** with **Column B thermoset insulation** is **25 amperes** per CEC 2022 Table 400.5(A)(1). 

**Key Details:**
- Column B applies to thermoset types like SPT-1, SPT-2, and similar (see table footnotes)
- This rating assumes **two-conductor cords** with only two current-carrying conductors
- Ambient temperature is 30°C (86°F) per table conditions
- No applicable exceptions found that modify this ampacity value

✓ Source: CEC 2022 Table 400.5(A)(1)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 400.5

**Response Time:** 10.2s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

**Answer:**  
The maximum operating temperature for **Type SF-2 silicone insulated fixture wire** is **200°C (392°F)**, as specified in **CEC Table 402.3**.  

### Key Exceptions and Limitations:
1. **Usage Restriction (CEC 402.12):**  
   - Type SF-2 is **permitted only for fixture wiring** and **not for general branch-circuit conductors** unless exceptions in other sections apply.  
   - This confirms the temperature rating applies **only to its intended fixture wiring applications**.

2. **Marking Requirements (CEC 402.9):**  
   - While not affecting temperature limits, Type SF-2 must be marked with its type designation and other required information (e.g., voltage rating, manufacturer).  

### Supporting Code References:
- **CEC Table 402.3**: Directly specifies 200°C for Type SF-2.  
- **CEC 402.12**: Confirms usage limitations for fixture wires.  
- **CEC 310.14(A)(3)**: Reinforces conductor temperature limits based on insulation type.  

✓ Source: CEC 2022 Table 402.3 and exceptions.

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 402.12, 402.3, 402.9, 310.14

**Response Time:** 14.2s

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
   8 AWG THWN copper @ 75°C = **50A** (CEC Table 310.16)  

2. **Temperature Correction**:  
   40°C ambient → **0.88 factor** (CEC Table 310.15(B)(1)(1))  

3. **Bundling Adjustment**:  
   7 conductors → **0.70 factor** (CEC Table 310.15(C)(1))  

4. **Final Calculation**:  
   ```
   50A × 0.88 × 0.70 = 30.8A
   ```

**Adjusted Ampacity**: **30.8 amperes**  

**Exception Review**:  
- **Section 310.15** confirms temperature correction and adjustment factors are permitted **if the corrected ampacity does not exceed the termination temperature rating** (110.14(C)).  
- THWN conductors are rated 75°C, and terminations are typically 60°C or 75°C. Since **30.8A < 50A (75°C column)**, the result complies with termination limits.  

No applicable exceptions override this calculation.  

✓ Source: CEC 2022 (Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1))

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.14, 310.16, 310.15

**Response Time:** 8.2s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Service Sizing for 200A Residential Service (CEC 2022)

**Final Answer with Exceptions Verified:**

✓ **Service Conductors**: 2/0 AWG copper  
  - Per **CEC Table 310.12(A)** (Single-Phase Dwelling Services)  
  - **No applicable exceptions** found for standard residential service conductor sizing  

✓ **Equipment Grounding (EGC)**: 6 AWG copper  
  - Per **CEC Table 250.122** for 200A overcurrent device  
  - **Exceptions** (410.44, 352.60) relate to special equipment grounding scenarios not applicable here  

✓ **Grounding Electrode Conductor (GEC)**: 4 AWG copper  
  - Per **CEC Table 250.66** for 2/0 AWG service conductors  
  - **Exceptions** (250.66) allow smaller conductors for specific electrode types, but standard rod/pipe electrode sizing applies  

**Key Code References:**  
- Service conductors: CEC 310.12(A)  
- EGC sizing: CEC 250.122  
- GEC sizing: CEC 250.66  

**California Amendments:**  
- All tables include [CEC] delta marks showing California-specific modifications from NEC  

**Final Verification:**  
No exceptions apply to this standard residential service configuration. All values reflect California code requirements with proper grounding electrode conductor sizing for typical rod/pipe electrodes.

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 352.60, 250.66, 310.12, 250.122, 410.44

**Response Time:** 12.2s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The 125% continuous load multiplier is already included in this table value.

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Building (CEC 2022)

**Calculation:**
- **Occupancy Type**: Office (per CEC Table 220.12)
- **Unit Load**: 1.3 VA per square foot (from CEC Table 220.12)
- **Area**: 5,000 square feet

$$
5,000 \, \text{sq ft} \times 1.3 \, \text{VA/sq ft} = 6,500 \, \text{VA}
$$

**Exceptions Checked**:
- **CEC 220.12(B)** allows alternative energy code calculations **if**:
  1. Power monitoring system is installed
  2. Alarm thresholds are set
  3. Demand factors from 220.42 are **not** applied
  4. 125% continuous load multiplier is applied
  → *Not applicable here as question provides no such conditions*

**Final Answer**:  
The general lighting load for a 5,000 sq ft office building in California is **6,500 volt-amperes** (VA), per CEC 2022 Table 220.12.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 220.42

**Response Time:** 9.7s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit (CEC 2022)

For **16 AWG copper conductors extending beyond the motor control equipment enclosure**, the maximum overcurrent protection is determined by **Column C of Table 430.72(B)** in the CEC 2022. 

### Key Requirements:
- **Table 430.72(B)** specifies that when conductors extend beyond the enclosure, the overcurrent protective device rating **shall not exceed the value in Column C**.
- For **16 AWG copper conductors**, Column C of Table 430.72(B) permits a maximum overcurrent protection of **10 amperes**.

### Exceptions Review:
- **Exception No. 1** (430.72(B)): Applies only if the control circuit opening creates a hazard (e.g., fire pump motors). Not applicable here.
- **Exception No. 2** (430.72(B)): Pertains to transformer secondary conductors. Not relevant for this scenario.
- Other exceptions (430.75, 430.84) address disconnection requirements, not overcurrent protection ratings.

### Conclusion:
No exceptions override the **10-ampere limit** for 16 AWG conductors extending beyond the enclosure. This aligns with California's adoption of NEC 2023 without conflicting amendments.

✓ Source: CEC 2022 Section 430.72, Table 430.72(B)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 430.84, 430.72, 430.75

**Response Time:** 9.6s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Dwelling Unit (CEC 2022)

**Final Calculation**:  
For a **2,400 sq ft dwelling unit**, the general lighting load is:  
$$
2,400 \, \text{sq ft} \times 3 \, \text{VA/sq ft} = 7,200 \, \text{VA (7.2 kVA)}
$$

**Exceptions Review**:  
- **Section 220.12** applies to *non-dwelling* occupancies and does not override the dwelling unit requirement.  
- **Section 220.14(J)** explicitly confirms the **3 VA/ft²** minimum for dwelling units.  
- No exceptions reduce or alter this requirement for standard dwelling units.  

**Conclusion**:  
The general lighting load remains **7,200 VA** as calculated.  

✓ Source: CEC 2022 Section 220.14(J)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.14, 220.12

**Response Time:** 9.0s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## Revised Comparison with Exceptions Considered

### **CEC 2022 Exceptions for Kitchen GFCI**  
- **Section 210.8(A)(6):**  
  - **Exemption 1:** Receptacles for ceiling fans/luminaires (weight-supporting ceiling receptacles) are exempt if not general-purpose.  
  - **Exemption 2:** Receptacles for specific appliances (e.g., refrigerators) on dedicated circuits are exempt.  
  - **Exemption 3:** Receptacles in industrial labs or healthcare facilities may bypass GFCI if safety risks exist.  

### **NEC 2023 Exceptions for Kitchen GFCI**  
- **Section 210.8(A)(5):**  
  - **Limited Exemption 1:** Permanently installed fire alarm systems (limited scope).  
  - **Limited Exemption 2:** HVAC equipment (expires September 2026).  

---

### **Final Analysis**  
1. **Scope of Protection:**  
   - **CEC:** GFCI required **only for countertop receptacles**. Other kitchen areas (e.g., near sinks, laundry) are **not explicitly covered**.  
   - **NEC:** GFCI required for **all kitchen receptacles**, including countertops, within **1.8 m (6 ft) of sinks**, and laundry areas.  

2. **Exceptions:**  
   - **CEC** allows **multiple exemptions** (e.g., ceiling fans, dedicated appliance circuits), reducing coverage.  
   - **NEC** has **fewer exceptions** and narrower exemptions (e.g., HVAC, fire alarms).  

3. **Stringency:**  
   - **NEC is more restrictive** by:  
     - Covering additional high-risk kitchen zones (e.g., near sinks).  
     - Limiting exceptions, ensuring broader protection.  

---

### **Conclusion**  
**NEC 2023 is more restrictive** than CEC 2022 for kitchen GFCI requirements. While CEC focuses narrowly on countertop circuits with multiple exemptions, NEC extends protection to additional kitchen areas and allows fewer exceptions. This makes NEC a safer standard for kitchens, aligninging with its broader approach to personnel protection.  

✓ Source: CEC 2022 Sections 210.8(A)(6), NEC 2023 Sections 210.8(A)(5).

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 210.8

**Response Time:** 18.2s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification. No...

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Final Comparison: CEC 2022 vs NEC 2023 Panelboard Space Requirements

### **California Energy Code (CEC) 2022 Key Provisions**
1. **Reserved Spaces for Electrification** (CEC 408.2):
   - **Mandatory** in single-family dwellings: Panelboards must reserve spaces for:
     - Heat pump water heaters
     - Heat pump space heaters
     - Electric cooktops
     - Electric clothes dryers
   - **Enforced by California Energy Code** (Sections 150.0(n), 150.0(t), etc.).
   - **Purpose**: Future-proofing for appliance electrification and energy efficiency.

2. **Wire-Bending Space** (CEC 408.55):
   - Matches NEC requirements (Tables 312.6(A) and 312.6(B)) with exceptions for small panelboards.

3. **Grounded Conductor Terminations** (CEC 408.41):
   - Same as NEC: Individual terminals required unless parallel conductors are used.

---

### **National Electrical Code (NEC) 2023 Key Provisions**
1. **General Installation Rules** (NEC 408.55):
   - Wire-bending space requirements align with CEC (Tables 312.6(A) and 312.6(B)).

2. **Grounding Requirements** (NEC 408.40):
   - Metal panelboards must be bonded; grounding conductors require dedicated terminal bars.

3. **Circuit Descriptions** (NEC 408.4):
   - Legible, permanent circuit descriptions required for all panelboards (no dwelling-specific exceptions).

---

### **Critical Differences**
| **Feature**               | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|---------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Appliance Electrification** | **Mandates reserved spaces** for heat pumps, cooktops, and dryers in single-family homes. | **No appliance-specific requirements**; focuses on general installation.       |
| **Code Basis**             | Driven by **California Title 24...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 9 found
- 312.6, 408.41, 408.55, 150.0, 408.2, 408.40, 426.14, 408.4, 424.10

**Response Time:** 14.3s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## Updated Comparison with Exceptions

### 9. **Anti-Backfeed Requirements (California Specific)**
- **CEC 2022 Exception (625.46)**:  
  - Requires **anti-backfeed protection** when the primary power source is lost. This prevents energy from being fed back through the EV and supply equipment to the premises wiring unless permitted by 625.48 (interactive systems).  
  - **No direct equivalent in NEC 2023**, which addresses bidirectional systems in Article 705 but lacks this specific anti-backfeed mandate.  

---

### Revised Key Differences Summary
| **Aspect**               | **CEC 2022**                          | **NEC 2023**                  |
|--------------------------|--------------------------------------|-------------------------------|
| **Anti-Backfeed**        | 625.46 mandates prevention           | Addressed in Article 705 only |
| **Truck Parking**        | Article 626 for electrified spaces     | No provisions                 |
| **Receptacle Enclosures**| Extra-duty weatherproof enclosures   | Weatherproof only             |

✓ Source: CEC 2022, NEC 2023

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 625.48, 625.46

**Response Time:** 12.7s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements Comparison: CEC 2022 vs NEC 2023 for Dwelling Units (With Exceptions)

### **Key Exceptions in CEC 2022**
1. **Receptacle Replacement Requirements**  
   - **CEC 2022 (406.4(D)(4))**:  
     When replacing receptacles in AFCI-protected areas (per 210.12(A), (B), or (C)), the replacement must be:  
     - A listed outlet branch-circuit type AFCI receptacle, or  
     - A receptacle protected by an outlet branch-circuit type AFCI, or  
     - A receptacle protected by a combination-type AFCI breaker.  
     *Exception: Section 210.12(D) exception does not apply to receptacle replacements.*  

   - **NEC 2023 (404.22(C)(4))**:  
     Similar requirement but **no explicit wiring length limits** or marking requirements for outlet AFCIs.  

---

### **Updated Comparison Summary**
| **Aspect**               | **CEC 2022**                                                                 | **NEC 2023**                                                                 |
|--------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Receptacle Replacements** | Requires AFCI-protected replacements in protected areas (406.4(D)(4)).<br> - Wiring length limits: 50 ft (14 AWG), 70 ft (12 AWG).<br> - First outlet must be marked. | Requires AFCI-protected replacements (404.22(C)(4)).<br> - No wiring length or marking requirements. |
| **Exception Scope**        | Explicit exception for short extensions (≤6 ft) without additional outlets. | No exception for short extensions.                                           |

---

### **Final Answer**
**CEC 2022** imposes stricter requirements for AFCI-protected receptacle replacements in dwelling units, including:  
- **Wiring length limits** (50 ft for 14 AWG, 70 ft for 12 AWG) for outlet AFCI configurations.  
- **First outlet marking** requirements.  
- **Exception for short extens...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 210.12, 404.22, 406.4

**Response Time:** 16.2s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California vs NEC Solar PV Requirements (CEC 2022 vs NEC 2023) - Final Answer

### **Key Exceptions for AC Modules (CEC 690.6)**
- **Exemption from PV Source Circuit Rules**:  
  AC modules and systems are exempt from CEC 690 requirements for PV source circuits (690.6(A)). Their internal conductors and inverters are treated as part of the module, not separate components (CEC 690.6(A)).
- **Output Circuit Classification**:  
  AC module output circuits are classified as **inverter output circuits** (690.6(B)), subject to inverter-specific rules rather than general PV source circuit requirements.

---

### **Critical Differences Between CEC and NEC**
| **Topic**               | **California (CEC 2022)**                                                                 | **NEC 2023**                                                                 |
|--------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **AC Module Exemptions** | Explicit exemptions for AC modules from PV source circuit rules (690.6).                  | No specific exemptions; AC modules treated as standard PV systems.           |
| **Rapid Shutdown Labels**| **Mandatory**: Black-on-yellow title (3/8" min), white-on-red switch labels.           | General labeling requirements; no color/size mandates.                     |
| **Module Frame Bonding** | **Explicit requirement**: Exposed metal parts of PV modules must be bonded (690.43).     | Bonding required but less emphasis on module frames specifically.          |
| **Field Labels**          | Required for evaluated AC modules, combiners, and charge controllers (690.4(B)).         | Listed equipment required; no field-labeling mandate for all components.     |
| **Battery Charge Control**| Unique rule (690.72): Charging current ≤ 3% of battery capacity or manufacturer spec.   | No equivalent provision for s...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 7 found
- 690.72, 690.59, 690.43, 690.11, 690.71, 690.4, 690.6

**Response Time:** 19.1s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 13.1s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

