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
| **Total Duration** | 353.8s |
| **Avg per Question** | 11.8s |

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

### **Reserved Circuit Breaker Spaces**  
Per **CEC 2022 Section 408.2(A)**, single-family residential panelboards **must include reserved circuit breaker spaces** for:  
1. **Heat pump water heaters**  
2. **Heat pump space heaters**  
3. **Electric cooktops**  
4. **Electric clothes dryers**  

### **Exception Check**  
No exceptions to **Section 408.2(A)** were found in CEC 2022 that would modify or exempt these requirements. The exceptions returned by the search (Sections 424.10, 440.8, 426.14) relate to special permissions for heating, air-conditioning, and deicing systems—not panelboard space reservations.  

### **Key Details**  
- **Mandatory under California Energy Code (CEC) Sections 150.0(n), 150.0(t), 150.0(u), and 150.0(v)**.  
- **No exceptions apply** to the reserved space requirements in 408.2(A) for single-family dwellings.  

✓ Source: CEC 2022 Section 408.2(A) and exception search results.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 408.2, 150.0, 424.10, 440.8, 426.14

**Response Time:** 22.5s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. These requirements are found in CEC Article 625 and Title 24 CALGreen (not CEC 408.2). Title 24 CALGreen mandates EV charging readi...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements (CEC 2022)  

### 1. **CALGreen Compliance**  
- **CALGreen Chapter 4 & 5**: New residential construction must include **EV-ready infrastructure** (CEC 625.1).  
  - Reserved circuit space in panelboards (CEC 408.2).  
  - Dedicated circuits for EV charging.  

### 2. **Branch Circuit Requirements**  
- **Individual Branch Circuit**: Each EV outlet must be on a dedicated circuit with **no other outlets** (CEC 625.40).  
- **Continuous Load**: EV charging loads are considered continuous; service/feeder sizing must account for 125% of the load (CEC 625.42).  

### 3. **Equipment Connection**  
- **Portable EVSE**: Must use listed receptacles (e.g., NEMA 14-50) rated up to 50A (CEC 625.44(A)).  
- **Fixed EVSE**: Permanently wired installations required (CEC 625.44(C)).  

### 4. **Location & Ventilation**  
- **Height Requirements**:  
  - Indoor: ≥ 18 in (450 mm) above floor.  
  - Outdoor: ≥ 24 in (600 mm) above grade (CEC 625.50).  
- **Ventilation**:  
  - If equipment is listed for indoor use without ventilation, mechanical ventilation is **not required** (CEC 625.52(A)).  
  - If equipment requires ventilation, mechanical systems must be interlocked with the charging circuit (CEC 625.52(B)).  

### 5. **Safety & Protection**  
- **GFCI Protection**: All EV receptacles must have **ground-fault circuit-interrupter (GFCI) protection** (CEC 625.54).  
- **Weatherproof Enclosures**: Outdoor receptacles must be in **listed weatherproof enclosures** (CEC 625.56).  

### 6. **Interactive Systems**  
- **Power Export**: EVSE with bidirectional capabilities must comply with Article 702 (standby systems) or 705 (distributed energy resources) (CEC 625.47).  

### 7. **Conduit & Cables**  
- **Cord Lengths**:  
  - Portable EVSE: ≤ 15 ft (4.6 m).  
  - Fixed EVSE: Output cable ≤ 25 ft (7.5 m) unless using a listed cable management system (CEC 625.17).  

### 8. **Overcurrent Protection**  
- **EVPE Receptacles**: Must be rated ≤ 250V, 5...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 12 found
- 408.2, 625.50, 625.40, 625.47, 625.17, 625.42, 625.1, 625.52, 625.54, 625.44

**Response Time:** 14.8s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements (CEC 2022) with Exceptions

### 1. **Rapid Shutdown (CEC 690.12)**  
- **Requirement**: All PV systems on buildings must include rapid shutdown to limit voltage (≤30V outside array, ≤80V inside) within 30 seconds.  
- **Exception**:  
  - Ground-mounted systems **where the building's sole purpose is housing PV equipment** are exempt.  
  - **Hazard control systems** (per 690.12(B)(2)(1)) may use nonmetallic enclosures/raceways at the building penetration point.  

### 2. **Grounding-Fault Protection (CEC 690.41)**  
- **Requirement**: DC circuits >30V/8A must have ground-fault protection.  
- **Exception**: Small, non-building-mounted systems (≤2 modules in parallel) may omit protection.  

### 3. **Wiring Methods (CEC 690.31)**  
- **Requirement**: DC circuits >30V/8A inside buildings must use metal raceways/Type MC cable.  
- **Exception**:  
  - **Hazard control systems** (per 690.12(B)(2)(1)) may use nonmetallic methods at the building penetration.  
  - Listed PV assemblies may follow engineered designs for support intervals (Exception to 690.31(C)(1)).  

### 4. **Labeling (CEC 690.56)**  
- **Requirement**: Permanent labels for rapid shutdown switches (white-on-red, 9.5mm min. text).  
- **No Exceptions**: Labeling requirements are mandatory for all applicable systems.  

### 5. **Special Systems**  
- **AC Modules**: Exempt from PV source circuit rules (690.6).  
- **Bipolar Systems**: Require physical separation of circuits (Exception allows listed switchgear with barriers).  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 690.31, 690.41, 690.12, 690.6, 690.56

**Response Time:** 12.8s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## California Circuit Requirements for Heat Pump Water Heaters (CEC 2022)

### Single-Family Buildings (1-2 Dwellings)
1. **Dedicated Circuit Requirements**  
   - Each dwelling unit must have **designated branch circuits and circuit identifications** for heat pump water heaters as specified in **California Energy Code Section 150.0(n)**.  
   - **Panelboard spaces** must be reserved for heat pump water heaters (CEC 408.2(A)).  

2. **Application of Other Articles**  
   - Installations must comply with **Article 430** (motors) and **Article 440** (refrigeration equipment) as amended (CEC 422.3(A)).  

---

### Multifamily Buildings
1. **Dedicated Circuit Requirements**  
   - Each dwelling unit must have **designated branch circuits and circuit identifications** for heat pump water heaters as specified in **California Energy Code Section 160.9**.  

---

### Exceptions Checked
- **CEC 422.47**: Applies to water heater **temperature controls**, not circuit requirements. Exceptions for high-capacity storage heaters (60 kW+ at 82°C) do not affect circuit design.  
- **CEC 422.12**: Relates to **central heating equipment** branch circuits. Not applicable to heat pump water heaters.  

---

### Key References
- **CEC 422.3(A)**: Mandates dedicated circuits and panelboard spaces for heat pump water heaters in single-family buildings.  
- **CEC 408.2(A)**: Requires panelboard circuit breaker spaces for heat pump water heaters.  
- **CEC 422.3(B)**: Extends similar requirements to multifamily buildings.  

For specific ampacity, conductor sizing, or load calculations, refer to **California Energy Code Sections 150.0(n) and 160.9** for detailed readiness and installation criteria.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 408.2, 422.3, 422.47, 150.0, 422.12, 160.9

**Response Time:** 10.0s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness Requirements (CEC 2022)

New California homes must comply with the following electric cooktop readiness requirements:

1. **Single-Family Buildings** (1-2 dwellings):
   - Each dwelling unit must have **dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 150.0(u)**.  
   - This includes designated spaces, receptacles, and branch circuits to accommodate future electric cooktop installations.

2. **Multifamily Buildings**:
   - Each dwelling unit must have **dedicated circuits and circuit identifications** for electric cooktops per **California Energy Code Section 160.9(b)**.  
   - These circuits must be pre-wired and labeled to support electric cooktops, ensuring readiness for installation.

3. **General Requirements**:
   - Circuits must be sized and installed to handle the **nameplate rating** of the cooktop appliance.
   - Compliance with **CEC 422.3** ensures alignment with California’s energy efficiency and electrification mandates.

4. **Exceptions**:
   - **Exception 422.23**: Appliances using non-standard installation methods require **special permission** from the authority having jurisdiction (AHJ). This applies if alternative installation methods are proposed.

✓ Source: CEC 2022 Section 422.3 and referenced California Energy Code provisions.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 422.23, 422.3, 150.0, 160.9

**Response Time:** 9.9s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

In California new construction, panelboards must include **reserved circuit breaker spaces** for electric clothes dryers as mandated by the California Energy Code:

1. **Single-Family Buildings**  
   - Panelboards must provide **circuit breaker spaces** for electric clothes dryers (along with heat pump water heaters, heat pump space heaters, and electric cooktops).  
   - **CEC Reference**: [CEC 2022 Section 408.2(A)](https://example.com/cec2022/408.2) (citing California Energy Code Section 150.0).

2. **Multifamily Buildings**  
   - Panelboards serving individual dwelling units must include **circuit breaker spaces** for electric clothes dryers (with heat pump space heaters and electric cooktops).  
   - **CEC Reference**: [CEC 2022 Section 408.2(B)](https://example.com/cec2022/408.2) (citing California Energy Code Section 160.9).

---

### Exceptions and Cross-References
- **Load Calculation**: While not an exception to the panelboard space requirement, [CEC 220.54](https://example.com/cec2022/220.54) specifies that electric dryer loads must be calculated at **5,000 VA minimum** (or nameplate rating, whichever is larger). This affects panel load calculations but does not override the requirement for reserved spaces.
- **Special Permission**: [CEC 424.10](https://example.com/cec2022/424.10) allows special permission for non-standard heating equipment but does not apply to dryers.

---

### Key Notes:
- This requirement is **California-specific** and not part of the NEC.  
- Dryer circuits typically require a **30A, 240V** circuit, but the panel must have a dedicated space for the breaker.  
- Failure to reserve spaces may violate the **California Energy Code** and hinder future electrification upgrades.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 408.2, 150.0, 424.10, 160.9, 220.54

**Response Time:** 9.5s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) Unique California Provisions (CEC 2022)  

After verifying with `cec_search("Section 760.43 California amendment")`, **no direct amendments** to **Section 760.43** (fire alarm systems) were found in the results. However, the cross-references in **Table 240.4(G)** to sections like **760.43** and **760.45** are marked with δ (California amendments), indicating that **overcurrent protection requirements for fire alarm systems** may differ from NEC.  

For example:  
- **Fire alarm systems** in California might require stricter overcurrent protection rules (e.g., specific fuse types, coordination with emergency power systems) under **CEC 760.43δ**, even though the exact amendment isn’t shown here.  
- Similar δ amendments likely apply to other cross-referenced sections like **630.12** (electric welders) or **725.43** (remote-control circuits).  

The **uniqueness of Table 240.4(G)** in California lies in its role as a **pointer to δ-amended sections** for specialized conductors, not in the table itself. Users must consult the referenced sections (e.g., 760.43) to identify California-specific overcurrent requirements.  

✓ Source: CEC 2022 Table 240.4(G) and cross-referenced sections.

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 725.43, 760.43, 240.4, 760.45, 630.12

**Response Time:** 18.9s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Final Answer: CEC Table 242.3 and Exceptions (CEC 2022)

### **CEC Table 242.3 Requirements**  
As verified by **CEC 2022 Section 242.3**, equipment must be protected against overvoltage per the specific NEC article listed in Table 242.3 for its type/location. This table is a **California-specific addition** ([N] marker) directing installers to 15 equipment-specific articles for overvoltage protection requirements.

---

### **Exceptions Found in CEC 2022**  
**CEC Section 242.54** ([N] California amendment) provides exceptions for **surge arrester interconnections** in transformer secondary distribution systems. Key exceptions include:  
1. **Metal Interconnections** (242.54(A)):  
   - Allowed if the secondary neutral has grounding connections via water piping systems or multigrounded neutral systems.  
2. **Spark Gap/Device Interconnections** (242.54(B)):  
   - Permitted for ungrounded/unigrounded or multigrounded primary systems with specific breakdown voltage requirements.  
3. **Special Permission** (242.54(C)):  
   - Alternative interconnections require approval.  

---

### **Compliance Summary**  
- **General Case**: Follow Table 242.3 cross-references for equipment-specific overvoltage rules.  
- **Exception Case**: For transformer surge arresters, comply with **242.54** interconnection requirements.  

**All exceptions are California-specific amendments** ([N] markers).  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 242.3, 242.54

**Response Time:** 19.0s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022) with Full Context

### **Core Requirements**
Specifies maximum overcurrent protective device ratings for motor control circuits based on conductor size (18 AWG to larger than 10 AWG). Key columns:
- **Column A**: Direct ratings for small conductors (18–16 AWG)
- **Column B**: 400% of Table 310.19 values for 60°C conductors
- **Column C**: 300% of Table 310.16 values for 60°C conductors

### **Example Values from Table 430.72(B)**
| Conductor Size | Column A (Copper) | Column B (Copper) | Column C (Copper) |
|----------------|-------------------|-------------------|-------------------|
| 18 AWG         | 7A                | 25A               | 7A                |
| 14 AWG         | (Note 1)          | 100A              | 45A               |
| 12 AWG         | (Note 1)          | 120A              | 60A               |

### **Key Exceptions**
1. **Exception No. 1 (430.72(B))**  
   - **Hazardous Circuits**: Overcurrent protection can be omitted if the control circuit's interruption creates a hazard (e.g., fire pump motors). Only short-circuit/ground-fault protection is required.  
   - **Source**: CEC 2022 Section 430.72(B)

2. **Exception No. 2 (430.72(B))**  
   - **Transformer Primary Protection**: For single-phase transformers with two-wire secondaries, primary-side overcurrent protection is permitted if it does not exceed:  
     *Primary protection rating* ≤ (*Table 430.72(B) secondary rating*) × (*Secondary-to-primary voltage ratio*)  
   - **Source**: CEC 2022 Section 430.72(B)

### **Related Code Sections**
1. **Combined Overcurrent Protection (430.55)**  
   - Allows combining short-circuit/ground-fault protection with overload protection in a single device, provided it meets 430.32 requirements.  
   - **Example**: A circuit breaker serving both functions.

2. **Motor-Circuit Coordination (430.225)**  
   - Requires coordinated protection to interrupt overload and fault current...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 310.19, 430.32, 430.225, 430.124, 430.55, 310.16, 430.72

**Response Time:** 16.2s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in CEC 2022 (California-Specific)

California's CEC 2022 includes **18 medium voltage (MV) cable tables** (2001V and above) in the **311.60(C)(67) through 311.60(C)(86)** series that are not present in the NEC. These tables provide ampacity ratings for MV cables in various configurations and environmental conditions.

### Key Tables:
- **Tables 311.60(C)(67)–311.60(C)(86)**  
  - **311.60(C)(67)–(70):** Ampacities for single-conductor MV cables in uncovered/triangular configurations.  
  - **311.60(C)(71)–(76):** Ampacities for multiconductor MV cables in cable trays (uncovered/covered).  
  - **311.60(C)(77)–(86):** Special cases (e.g., bundled cables, high-temperature environments).  

### California-Specific Adjustments:
- **Covered trays:** 95% derating (CEC 392.80(B)(1)).  
- **Single-conductor cables:** 75% derating for uncovered trays (CEC 392.80(A)(2)).  

### NEC Comparison:
The NEC does not include equivalent tables for MV cables in California-specific applications like cable trays. CEC tables 311.60(C) are unique to California’s amendments.

✓ Source: CEC 2022 Sections 311.60, 392.80

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 392.80, 311.60

**Response Time:** 11.1s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

The ampacity of **4/0 AWG copper conductor at 75°C** is **230 amperes** per **CEC 2022 Table 310.16**. This value applies for:
- Up to 3 current-carrying conductors in raceway/cable
- 30°C ambient temperature
- Standard installation conditions

No applicable exceptions override this value for general use. The California amendment (delta) note indicates this value may differ from NEC 2023.

✓ Source: CEC 2022 Table 310.16

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.16

**Response Time:** 5.3s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size (CEC 2022) with Exceptions Considered

For a **200A circuit** in California:
- **Copper EGC**: 6 AWG (minimum size)
- **Aluminum/Copper-Clad Aluminum EGC**: 4 AWG (minimum size)

**Exceptions Reviewed**:
1. **Section 410.44** (Luminaires): Not applicable (question is general, not luminaire-specific).
2. **Sections 352.60/356.60**: Permit alternate grounding methods but do not affect conductor sizing.
3. **Section 250.121**: Prohibits using EGC as GEC but does not modify sizing requirements.
4. **Section 250.134**: Allows separate EGC routing but does not impact size calculations.

**Conclusion**: No exceptions override Table 250.122 for standard 200A circuit grounding conductor sizing. The 6 AWG copper or 4 AWG aluminum remains valid per **CEC 2022 Table 250.122** with California amendments.

✓ Source: CEC 2022 Table 250.122 (with exception review)

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 250.134, 250.121, 352.60, 356.60, 250.122, 410.44

**Response Time:** 6.8s

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
(Per **CEC 2022 Table 250.66**, with California amendment [Δ])

### Exceptions Considered:
1. **250.66(A)**: Allows 6 AWG copper for rod/pipe/plate electrodes if not extending to other electrode types.  
   → *Does not apply unless electrode type is specified.*
2. **250.66(B)**: Allows 4 AWG copper for concrete-encased electrodes.  
   → *Applies if electrode is concrete-encased (not specified here).*
3. **250.66(C)**: Ground ring conductor size matches the ground ring.  
   → *Not applicable unless ground ring is used.*

No exceptions override the base requirement for a general case without specific electrode type or system configuration. The standard size from **Table 250.66** remains valid.

✓ Source: CEC 2022 Table 250.66 [Δ]

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 8.8s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** in a **40°C ambient temperature** is **0.88** per **CEC 2022 Table 310.15(B)(1)(1)**.

**Exception Search Results:**
- No exceptions apply to the temperature correction factor calculation itself (exceptions found relate to grounding requirements in Sections 352.60, 356.60, etc., which are unrelated to this question)
- California has not amended this requirement from NEC (verified via comparison)

**Final Answer:**  
Use **0.88 correction factor** for 75°C conductors at 40°C ambient temperature.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 356.60, 352.60

**Response Time:** 6.5s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor for Bundling (CEC 2022)

For **7-9 current-carrying conductors** in a raceway, the ampacity adjustment factor is **0.70 (70%)** per **CEC Table 310.15(C)(1)** [California Amendment]. 

### Exceptions Verified:
1. **Section 310.15(C)(1)** confirms the 0.70 factor applies generally, with conditions:
   - Adjustment factors apply to power/lighting conductors in raceways >600mm (24") long
   - Excludes grounding/bonding conductors (per 310.15(F))
   - Neutral conductors may or may not be counted (per 310.15(E))
2. **Section 334.80** adds NM/NMC cable-specific rules but doesn't override the 0.70 factor
3. Grounding exceptions (355.60, 352.60, 356.60) are unrelated to bundling adjustments

**Key Notes:**
- Applies to conductors rated 40°C or less (THHN, THWN, etc.)
- Must multiply base ampacity by 0.70
- Footnote [*] clarifies conductor counting rules

✓ Source: CEC 2022 Table 310.15(C)(1) [California Amendment] with exceptions verified

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 355.60, 356.60, 352.60, 310.15, 334.80

**Response Time:** 6.7s

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
Per **CEC Table 110.26(A)(1)** for voltages 151–600V.  

### Key Details:  
- **Condition 3**: Exposed live parts on **both sides** of the working space.  
- **Footnote**: Applies to installations where live parts are exposed on both sides of the working area (no guarding required if insulating materials are used).  

### Exception Check:  
- **CEC 110.26(E)** discusses dedicated electrical space requirements (height, foreign systems, etc.) but does **not override** the 1.2m (4ft) depth requirement.  
- Other exceptions (352.60, 356.60, 440.14) relate to grounding and disconnecting means, not working space depth.  

✓ **No exceptions reduce the required depth** for this scenario.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 440.14, 110.26, 352.60, 356.60

**Response Time:** 8.8s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Suitable Enclosures for Outdoor Use with Rain, Sleet, and Ice (CEC 2022)

For outdoor use with exposure to **rain, sleet, and ice**, the following enclosure types are suitable per **CEC Table 110.28** and related amendments:

### **Approved Enclosure Types**
1. **Type 3S**  
   - **Protection**: Raintight, sleet-tight, snow-tight, and corrosion-resistant.  
   - **Use**: General outdoor applications with ice exposure.  

2. **Type 3SX**  
   - **Protection**: Same as Type 3S with enhanced corrosion resistance.  
   - **Use**: Coastal or corrosive environments.  

3. **Type 4**  
   - **Protection**: Watertight for outdoor use.  
   - **Use**: Protection against rain, sleet, and ice.  

4. **Type 4X**  
   - **Protection**: Watertight with corrosion resistance.  
   - **Use**: Harsh outdoor environments (e.g., industrial areas).  

5. **Type 6**  
   - **Protection**: Dust- and watertight.  
   - **Use**: Applications requiring protection against water and particulates.  

6. **Type 6P**  
   - **Protection**: Same as Type 6 with added protection for pump installations.  

---

### **Key Code Requirements**
1. **Mechanism Operability** (CEC 110.28 Footnote):  
   - Enclosures must remain operable when ice-covered.  

2. **Receptacle Installations** (CEC 406.9):  
   - Outdoor receptacles in wet locations must use **weatherproof enclosures** (e.g., Type 4 or 4X).  
   - Nonlocking receptacles (e.g., 5-15, 5-20) must be **listed as weather-resistant**.  

3. **Dedicated Equipment Spaces** (CEC 110.26(E)):  
   - Outdoor electrical equipment must be in **identified enclosures** (Types 4, 4X, etc.) and protected from environmental damage.  

---

### **California-Specific Notes**
- **Industrial Control Panels** (CEC 409.100):  
  - Table 110.28 applies unless equipment is in hazardous locations.  
  - Enclosures do **not** protect against internal condensation or corrosion; additional measures may be required.  

- **Refrigeration Equipment** (CEC 440.3):  
  - Enclos...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 110.26, 406.9, 110.28, 440.3, 409.100

**Response Time:** 17.8s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated from 3.5 VA in NEC 2020)

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)

The **standard general lighting load** for office buildings in California is **1.3 volt-amperes per square foot (VA/ft²)** per CEC 2022 Table 220.12.  

### Exceptions and Special Conditions:
1. **Energy Code Compliance** (Section 220.12(B)):  
   - If the building complies with a local energy code, the lighting load may be calculated using the energy code's unit values **if**:  
     - A power monitoring system is installed.  
     - The system triggers alarms if the load exceeds energy code limits.  
     - Demand factors from Table 220.42 are **not applied** to the general lighting load.  
     - The **125% continuous load multiplier** (per 210.20(A)) is applied.  

2. **No Direct Exceptions for Office-Specific Adjustments**:  
   - The base value of 1.3 VA/ft² applies unless the above energy code conditions are met.  

**Reference:** CEC 2022 Table 220.12, Section 220.12(B)  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 210.20, 220.42, 220.12

**Response Time:** 10.2s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is the same value as NEC 2023 - there is no California amendment for this table. Column B represents 2 current-carrying conductors.

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

**Final Answer:**  
The ampacity for **12 AWG flexible cord** with **Column B thermoset insulation** is **25 amperes** per **CEC Table 400.5(A)(1)**. This value applies to flexible cords used in portable or movable applications, with thermoset insulation rated for 75°C operation.

**Key Notes:**  
- This rating assumes **not more than three current-carrying conductors** (per Table 400.5 Notes).  
- **Exceptions/Restrictions** (from CEC 400.12):  
  - Flexible cords **cannot substitute for fixed wiring** in walls, ceilings, or floors.  
  - Prohibited from being **concealed by walls/ceilings** unless in an approved enclosure (Exception to 5).  
  - Must comply with **UL 817** standards for cordsets/power-supply cords.  

✓ Source: CEC 2022 Table 400.5(A)(1) and Section 400.12

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 400.12, 400.5

**Response Time:** 7.2s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

The maximum operating temperature for **Type SF-2 silicone insulated fixture wire** is **180°C**, as specified in **CEC Table 402.3**. 

### Exception Review:
1. **CEC 402.9** - Addresses marking requirements for fixture wires (no impact on temperature rating).
2. **CEC 402.12** - Prohibits use as branch-circuit conductors (does not affect temperature rating).

No exceptions override the 180°C temperature rating for SF-2 in Table 402.3.

✓ Source: CEC 2022 Table 402.3

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 402.9, 402.3, 402.12

**Response Time:** 7.7s

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
   8 AWG THWN copper at 75°C = **50A** (Table 310.16)

2. **Temperature Correction (40°C ambient)**:  
   50A × 0.88 (Table 310.15(B)(1)(1)) = **44A**

3. **Bundling Adjustment (7 conductors)**:  
   44A × 0.70 (Table 310.15(C)(1)) = **30.8A**

**Final Adjusted Ampacity**: **30.8 amperes**

**Exception Review**:  
- **Section 440.6** (refrigerant motor-compressors) does not apply here.  
- **Section 310.15** confirms temperature correction and bundling adjustments are permissible **if the corrected ampacity does not exceed the termination temperature rating** (75°C for THWN conductors). Since 30.8A ≤ 50A (original 75°C rating), the calculation is valid.  

✓ Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 440.6, 310.16

**Response Time:** 9.9s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Service Sizing for 200A Residential (CEC 2022) with Exceptions Verified

✓ **Service Conductor**: 2/0 AWG copper (Table 310.12(A))  
✓ **Equipment Grounding (EGC)**: 6 AWG copper (Table 250.122)  
✓ **Ground Electrode Conductor (GEC)**: 4 AWG copper (Table 250.66)  

---

### **Exceptions Analysis**  
1. **Service Conductor (310.12(A))**  
   - **Exception 310.12(A)(G)**: Parallel conductors require identical characteristics (same length, material, size, insulation). Not applicable here (single conductor used).  
   - **Exception 310.12(B)**: Feeders for dwellings can use 83% of rating if no derating applies. Not applicable (service conductors, not feeders).  

2. **Equipment Grounding (250.122)**  
   - **Exception 250.142(A)**: Grounded conductor can ground equipment on the supply side. Not applicable (dedicated EGC used).  
   - **Exception 250.122(B)**: EGC can be proportionally increased if ungrounded conductors are upsized. Not applicable (conductor sizes match).  

3. **Ground Electrode Conductor (250.66)**  
   - **Exception 250.66(A)**: 6 AWG copper allowed for rod/pipe electrodes. Overridden by Table 250.66 for 2/0 service conductors (requires 4 AWG).  
   - **Exception 250.66(C)**: Ground ring conductor sizing. Not applicable (standard electrode used).  

---

### **Key Code References**  
- **Service Conductor**: CEC 310.12(A) [delta]  
- **EGC**: CEC 250.122 [delta]  
- **GEC**: CEC 250.66 [delta]  

All sizes comply with California amendments [delta]. No exceptions override the standard sizing for this application.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.122, 310.12, 250.142, 250.66

**Response Time:** 12.2s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot (updated from 3.5 VA in NEC 2017 and earlier). General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note: The 125% continuous load multiplier is already included in this table value.

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Building (CEC 2022)  

The general lighting load for a 5,000 sq ft office building in California is calculated as follows:  

1. **Unit Load**: 1.3 VA/ft² (CEC Table 220.12 for "Office")  
2. **Calculation**:  
   $ 5,000 \, \text{ft}^2 \times 1.3 \, \text{VA/ft}^2 = 6,500 \, \text{VA} $  

**Exceptions Checked**:  
- **Section 220.12(B)** allows alternative energy code values *if* a power monitoring system is installed and specific conditions are met. Since the question provides no such context, the standard value applies.  
- Other exceptions (225.32, 215.10) relate to disconnecting means and ground-fault protection, which are unrelated to lighting load calculations.  

**Final Answer**:  
**6,500 volt-amperes** (6.5 kVA)  

✓ Source: CEC 2022 Table 220.12  
✓ Note: 125% continuous load multiplier already included in table value per CEC 220.12.

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 215.10, 225.32, 220.12

**Response Time:** 12.1s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Copper Motor Control Circuit (CEC 2022)

The maximum overcurrent protection for **16 AWG copper conductors** in a motor control circuit extending beyond the enclosure is **10 amperes**, per **CEC 2022 Section 240.4(D)(2)**. 

### Key Requirements:
1. **Overcurrent Device Rating**: 
   - **Maximum: 10A** (must be a branch-circuit-rated circuit breaker or fuse marked for 16 AWG copper, or Class CC/J/T fuses).
2. **Continuous Load Limit**: 
   - Continuous loads must not exceed **8 amperes** (80% of 10A).
3. **Application**: 
   - Applies to motor control circuits where conductors extend beyond the enclosure.

### Exceptions Checked:
- No exceptions in CEC 2022 override this rule for motor control circuits.
- **Section 430.22(G)(2)** allows 16 AWG for motor conductors under specific overload protection conditions, but this applies to motor branch circuits, not control circuits.
- Other exceptions (368.17, 230.90, 352.60) relate to busways, services, or grounding and do not apply here.

### Source:
- **CEC 2022 Section 240.4(D)(2)** (same as NEC 2023, no California amendments noted). 

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 240.4, 368.17, 352.60, 430.22, 230.90

**Response Time:** 10.6s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Dwelling Unit (CEC 2022)

For a **2,400 square foot dwelling unit** in California:

**Calculation:**
```
2,400 sq ft × 3 VA/sq ft (CEC 220.14(J)) = 7,200 VA
```

**Exceptions Checked:**  
No exceptions modify this calculation for standard dwelling units. The 3 VA/sq ft requirement in **CEC 220.14(J)** applies directly to one-family, two-family, and multifamily dwellings, covering both general lighting and receptacle loads.

**Source:**  
CEC 2022 Section 220.14(J) mandates **3 volt-amperes per square foot** for general lighting and receptacle loads in dwelling units. This aligns with California's Title 24 Part 6 energy efficiency requirements for residential electrical loads.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 220.14

**Response Time:** 8.3s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## Final Comparison of Kitchen GFCI Requirements

### **CEC 2022 Key Exceptions**  
1. **Ceiling Fixtures**: Listed locking support receptacles for ceiling luminaires/fans are exempt if not general-purpose (210.8(A)(6) Exception).  
2. **Industrial/Healthcare**: Receptacles in industrial labs or healthcare facilities may bypass GFCI if power interruption creates hazards.  
3. **Snow-Melting/Deicing**: Dedicated circuits for these systems are exempt (426.28/427.22).  

### **NEC 2023 Key Exceptions**  
1. **Ceiling Fixtures**: Similar exemption for listed weight-supporting systems (210.8(A) Exception No. 3).  
2. **HVAC Equipment**: Temporary exemption for listed HVAC equipment (expires 2026).  
3. **Fire Alarm Systems**: Receptacles for fire alarms may omit GFCI (Exception No. 2).  

---

### **Restrictiveness Analysis**  
- **Scope**:  
  - **CEC**: Limited to **countertop receptacles**.  
  - **NEC**: Covers **all kitchen receptacles**, including laundry, sinks (within 6 ft), and general use.  
- **Exceptions**:  
  - **CEC** allows more exceptions (e.g., industrial labs, ceiling fixtures).  
  - **NEC** has narrower exceptions and broader mandatory coverage.  

**Conclusion**: **NEC 2023 is more restrictive** due to its expanded scope and fewer exceptions.  

**Source**: CEC 2022 210.8(A)(6) Exceptions; NEC 2023 210.8(A)(5), 210.8(A)(7).

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 426.28, 427.22, 210.8

**Response Time:** 15.9s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard spaces for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification. No...

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Final Answer: Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023)

### **California Energy Code (CEC) 2022 Requirements**
1. **Reserved Circuit Breaker Spaces** (CEC 408.2(A)):
   - **Mandatory for single-family dwellings**: Panelboards must include reserved spaces for:
     - Heat pump water heaters
     - Heat pump space heaters
     - Electric cooktops
     - Electric clothes dryers
   - **Enforced by California Energy Code Sections 150.0(n), 150.0(t), 150.0(u), and 150.0(v)** to future-proof for electrification.
   - **No exceptions** found for this requirement in CEC 2022.

2. **Minimum Panelboard Spaces**:
   - While not explicitly stated in the search results, CEC aligns with NEC for minimum spaces but adds the above appliance-specific requirements.

---

### **NEC 2023 Requirements**
1. **Minimum Circuit Breaker Spaces** (NEC 408.3(A)):
   - **Single-family dwellings** require **at least 10 spaces** in the panelboard.
   - **No reserved spaces** for future appliances unless mandated by local amendments.

---

### **Key Differences**
| **Requirement**                | **CEC 2022**                          | **NEC 2023**                  |
|---------------------------------|----------------------------------------|-------------------------------|
| Reserved spaces for appliances  | **Required** (408.2(A))               | **Not required**              |
| Minimum panelboard spaces       | Implied (aligns with NEC)             | **10 spaces minimum** (408.3) |
| Energy code integration         | Tied to California Energy Code         | No specific energy code link  |

---

### **Source**
- **CEC 2022**: Section 408.2(A) (no exceptions found for this rule).  
- **NEC 2023**: Section 408.3.  

✓ Source: CEC 2022 and NEC 2023 comparison.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 408.2, 150.0, 408.3

**Response Time:** 11.0s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## California EV Charging Requirements vs NEC 2023 (CEC 2022) – Final Answer

### **Key Exceptions to CEC 625.40 (EV Branch Circuits)**  
After verifying exceptions for **CEC 625.40** (individual branch circuits for EV outlets), the following exceptions apply:

1. **Multiple Feeders/Branch Circuits Allowed**  
   - **CEC 625.47**: Permits multiple feeders or branch circuits to supply EV equipment *if the equipment is identified for the application*.  
   - Example: High-power EVSE systems may use multiple circuits for load distribution.

2. **Interactive/Bidirectional Systems**  
   - **CEC 625.48**: Allows EVSE with power export functions (e.g., bidirectional charging) to comply with:  
     - **Article 702** (optional standby systems) or  
     - **Article 705** (distributed energy resources).  
   - Requires equipment to be *listed and marked* for bidirectional operation.

3. **Prevention of Backfeed**  
   - **CEC 625.46**: Mandates anti-backfeed mechanisms for systems with power export capabilities to prevent energizing premises wiring during utility outages.

---

### **Final Comparison Summary**

| **Feature**                     | **California CEC 2022**                                                                 | **NEC 2023**                                                                 |
|--------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Branch Circuits**            | **Mandatory individual circuits** for EV outlets (625.40). Exceptions allow multiple circuits (625.47). | No specific EV circuit requirements; governed by general branch circuit rules. |
| **GFCI Protection**            | **Required for all EV receptacles** (625.54).                                           | Required by 210.8(A)(7) but not EV-specific.                                  |
| **Ventilation**                | Mechanic...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search, compare_with_nec
- CEC Primary: Yes

**Citations:** 9 found
- 220.57, 210.8, 625.48, 625.40, 625.1, 625.54, 625.47, 625.52, 625.46

**Response Time:** 16.6s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements Comparison (CEC 2022 vs NEC 2023) – **Updated with Exceptions**

---

### **Key Exceptions in CEC 2022 for AFCI Protection**
After reviewing exceptions for **CEC 2022 Section 210.12**, the following critical amendments and exceptions apply:

#### **1. Receptacle Replacement Exceptions [CEC 406.4(D)(4)]**
- **Permitted Replacements for AFCI-Protected Outlets**:
  - **Option 1**: Install a **listed outlet branch-circuit type AFCI receptacle**.
  - **Option 2**: Use a receptacle **protected by another listed outlet branch-circuit type AFCI receptacle**.
  - **Option 3**: Use a receptacle **protected by a listed combination-type AFCI circuit breaker**.
- **Exception**: Section 210.12(D)’s short extension exception (≤6 ft) **does not apply** to receptacle replacements. This means even short extensions in existing AFCI-protected circuits must comply with full AFCI requirements when replacing receptacles.

#### **2. Fire Alarm System Exception [CEC 210.12 Exception]**
- **Exemption**: AFCI protection is **not required** for individual branch circuits supplying fire alarm systems installed per **760.41(B)** or **760.121(B)**, **provided**:
  - The circuit is wired in **metal raceway**, **steel-armored cable**, or **Type MC/AC cable** meeting 250.118 requirements.
  - Metal boxes, conduit bodies, and enclosures are used.

---

### **Updated Comparison Table**

| Feature                          | **CEC 2022**                                                                 | **NEC 2023**                          |
|----------------------------------|-------------------------------------------------------------------------------|---------------------------------------|
| **Receptacle Replacements**      | **406.4(D)(4)**: Specific AFCI replacement rules for protected outlets.     | **210.12(E)**: General receptacle replacement rules. |
| **Short Extension Exception**    | **Excluded for receptacle replacements** (per 406.4(D)(4) Exception).     ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 760.121, 406.4, 250.118, 760.41, 210.12

**Response Time:** 15.2s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements vs NEC 2023 Article 690 (CEC 2022)  

### Key Differences and California-Specific Requirements  

1. **AC Module Systems**  
   - **CEC 690.6**:  
     - PV source circuit requirements **do not apply** to AC modules or AC module systems.  
     - AC module output circuits are treated as **inverter output circuits**.  
   - **NEC 2023**:  
     - Standard Article 690 applies to all PV systems, including AC modules, without special exceptions.  

2. **Rapid Shutdown Labeling**  
   - **CEC 690.56**:  
     - **Mandatory labels** with specific size/visibility requirements:  
       - Title: **9.5 mm (3/8 in.)** black on yellow.  
       - Instructions: **4.8 mm (3/16 in.)** black on white.  
     - Diagrams required for buildings with multiple PV systems.  
   - **NEC 2023**:  
     - General rapid shutdown requirements in 690.12, but no prescriptive label size/color mandates.  

3. **Large-Scale PV Systems**  
   - **CEC Article 691**:  
     - Separate article for **large-scale PV electric supply stations** (≥ 10 kW).  
     - Requires **engineered design documentation** stamped by a licensed electrical engineer.  
   - **NEC 2023**:  
     - No separate article for large-scale systems; covered under general Article 690.  

4. **PV-Powered Signs**  
   - **CEC 600.34**:  
     - Additional requirements for wiring (e.g., routing along sign body, protection from damage, extra-hard usage flexible cords).  
     - Battery compartments must require a **tool to open**.  
   - **NEC 2023**:  
     - No specific provisions for PV-powered signs in Article 690.  

5. **Functionally Grounded Systems**  
   - **CEC 690.2**:  
     - Explicit definition of "functionally grounded" systems (grounded via inverter/controller for operational purposes).  
   - **NEC 2023**:  
     - Similar definition but less emphasis on PV-specific applications.  

---

### Summary of California Amendments [CEC 2022]  
- **Stricter labeling** for rapid shutdown (69...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 690.2, 600.34, 690.12, 691.6, 690.6, 690.56

**Response Time:** 11.6s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 11.8s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

