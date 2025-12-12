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
| **Total Duration** | 366.0s |
| **Avg per Question** | 12.2s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2 requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, (4) electric clothes dryers, and (5) electric vehicle charging equipment. This is a California-specific requirem...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements and Reserved Circuit Breaker Spaces in California Single-Family Dwellings (CEC 2022)

---

### **Panelboard Space Requirements**
Per **CEC 2022 Section 408.55**, panelboards must comply with wire-bending space requirements:
- **Top/Bottom Wire-Bending Space**: Sized per **Table 312.6(B)** for the largest conductor, unless exceptions apply (e.g., panelboards rated ≤ 225A with ≤ 42 overcurrent devices may use Table 312.6(A)).
- **Side Wire-Bending Space**: Sized per **Table 312.6(A)** for the largest conductor.
- **Back Wire-Bending Space**: Must allow for one wire per terminal spacing (Table 312.6(A)) if conductors enter opposite a removable cover.

Additional requirements:
- Panelboards must be mounted in **dead-front enclosures** (Section 408.38).
- Must have a **short-circuit current rating** ≥ available fault current (Section 408.6).

---

### **Reserved Circuit Breaker Spaces for Appliances**
Per **CEC 2022 Section 408.2(A)** (California-specific amendment), single-family dwellings must have **pre-wired circuit breaker spaces** for:
1. **Heat pump water heaters**
2. **Heat pump space heaters**
3. **Electric cooktops**
4. **Electric clothes dryers**

These spaces are required to support future appliance installations as mandated by the California Energy Code (Sections 150.0(n), (t), (u), and (v)).

---

### **Exceptions Checked**
- **No exceptions** were found that modify or override the appliance-specific reserved space requirements in **Section 408.2(A)**.
- Exceptions related to overcurrent protection (408.36), enclosures (408.38), and wire-bending spaces (408.55) do not affect the appliance space requirements.

---

## NEC 2023 Reference
The base NEC **does not require** pre-wired spaces for these appliances. This is a **California-specific amendment** [CEC]. NEC 2023 Article 408 focuses on general panelboard requirements (e.g., wire-bending spaces, short-circuit ratings) but lacks appliance-specific reserved space mandates.

...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 312.6, 408.2, 408.36, 408.38, 408.6, 408.55, 150.0

**Response Time:** 23.8s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. CEC 408.2 requires panelboard spaces for EV charging equipment. Title 24 also mandates EV charging readiness.

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California's EV Charging Requirements (CEC 2022)  

### Key Requirements for New Residential Construction:  

1. **Dedicated Circuits**  
   - **625.40**: Each EV charging outlet must have an **individual branch circuit** with **no other outlets** (no multi-outlet circuits).  

2. **Compliance with CALGreen**  
   - **625.1**: In addition to CEC, EV charging must comply with **CALGreen Chapter 4 & 5** (sustainability standards for new construction).  

3. **Receptacle Enclosures**  
   - **625.56**:  
     - **Wet locations** require **weatherproof enclosures** (e.g., garage with outdoor access).  
     - **GFCI protection** is mandatory for all EV receptacles.  
     - Receptacles must be **listed** and rated **≤250V, ≤50A**.  

4. **Connection Methods**  
   - **625.44**:  
     - **Portable equipment**: Use 15/20A or 30/50A receptacles (125V/250V).  
     - **Fastened-in-place equipment**: Permanently wired or use 50A-rated receptacles.  
     - **Fixed equipment**: Must be **hardwired** (no portable connections).  

5. **Load Management**  
   - **625.42**:  
     - EV loads are **continuous**, so service/feeder sizing must account for 100% of the EV load.  
     - Adjustable settings on fixed equipment require **restricted access** (tool-locked covers, password-protected software).  

---

### Exceptions and Related Sections:  
- **625.46**: Requires **anti-backfeed protection** if the EVSE could energize the premises wiring during utility outages.  
- **625.42**: Clarifies that adjustable settings on fixed equipment must be **restricted to qualified personnel** (e.g., tool-locked enclosures).  

---

## NEC 2023 Comparison  
- **Similar Requirements**: NEC 625 also mandates dedicated circuits, GFCI protection, and weatherproof enclosures for outdoor EVSE.  
- **Key California Differences**:  
  - **CALGreen compliance** is unique to California (no NEC equivalent).  
  - **Restricted access** for adjustable settings is emphasized in CEC 625.42 (NEC allows ad...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 625.46, 625.44, 625.1, 625.56, 625.42, 625.40

**Response Time:** 11.0s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California-Specific Solar PV Requirements (CEC 2022) with Exceptions

### Key CEC 2022 Requirements for Residential Solar PV Systems

1. **Maximum Voltage Limits**  
   - **CEC 690.7**:  
     - **600V maximum** for PV DC circuits in **one- and two-family dwellings** (vs. 1000V for general buildings).  
     - Temperature correction for crystalline silicon modules must use **Table 690.7(A)**.  
   - **Exception**: Systems outside buildings may use up to 1500V with listed equipment.  

2. **Arc-Fault Protection**  
   - **CEC 690.11**:  
     - **Mandatory** for all PV systems with DC circuits ≥80V.  
     - **Exception**: Non-building systems (e.g., ground-mounted arrays) are exempt if installed in metallic raceways, metal-clad cables, or enclosed metallic trays.  

3. **Overcurrent Protection**  
   - **CEC 690.9**:  
     - Overcurrent devices must protect PV circuits unless:  
       - Conductors have sufficient ampacity for maximum current **and** do not exceed module/power converter ratings.  
       - Conductors ≤3m (10ft) in length are protected at one end (in or out of buildings).  
     - Overcurrent devices must be **listed for PV systems**.  

4. **Branch-Circuit Voltage Limitations**  
   - **CEC 210.6**:  
     - In residential units, branch circuits must not exceed:  
       - **120V** for luminaires and small cord-connected loads.  
       - **277V** for specific luminaires (e.g., LED, discharge lamps).  
       - **600V** for industrial luminaires ≥6.7m (22ft) high.  

5. **Grounding and Bonding**  
   - **CEC 690.43–47**:  
     - Metal PV frames and support structures must be bonded using **listed devices**.  
     - Grounding electrodes for PV arrays must connect to the building’s grounding system per **250.52/250.54**.  

---

### Exceptions and Cross-References  
- **690.9** adds overcurrent protection rules, including exceptions for short conductors and listed devices.  
- **210.6** imposes voltage limits on residential branch circuits (e.g....

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 250.54, 690.11, 250.52, 690.9, 210.6, 690.7, 690.43

**Response Time:** 13.7s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Circuit Requirements for Heat Pump Water Heaters in New Dwellings (CEC 2022)

**California Requirements:**

1. **Individual Branch Circuit (CEC 2022 Section 422.12):**
   - Heat pump water heaters must be supplied by an **individual branch circuit**.
   - Exceptions allow auxiliary equipment (e.g., pumps, valves) to share the circuit.

2. **Overcurrent Protection and Conductor Sizing (CEC 2022 Section 422.13):**
   - For storage-type water heaters (including heat pump models), branch-circuit conductors and overcurrent devices must be sized **not smaller than 125% of the water heater’s rated current**.
   - Example: A 24A-rated heat pump water heater requires conductors and protection rated for at least 30A (24A × 1.25).

3. **Motor-Operated Appliances (CEC 2022 Section 422.11(G)):**
   - Heat pump water heaters with motors require overload protection per **Article 430** (motor circuits) or **Article 440** (air-conditioning equipment).
   - Overcurrent devices must comply with the appliance’s marked rating or follow 150% sizing rules if unmarked.

4. **Temperature-Limiting Controls (CEC 2022 Section 422.47):**
   - Storage-type water heaters must have a **temperature-limiting means** (e.g., trip-free thermostat) to disconnect power if water temperature exceeds safe limits.
   - Exceptions apply for high-capacity (≥60 kW) or low-volume (≤4 L) instantaneous heaters.

---

## NEC 2023 Reference
- **No significant differences** from NEC 2023 for storage-type water heaters (NEC 422.13). California’s 125% sizing rule aligns with NEC.
- California adds **Section 422.47** (temperature-limiting controls) as a state-specific amendment not explicitly required by NEC.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 422.11, 422.13, 422.47, 422.12

**Response Time:** 15.1s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness Requirements (CEC 2022)

**California Requirement:**  
Per **CEC 2022 Section 422.3**, new residential buildings in California must include **dedicated electrical circuits and circuit identifications** for electric cooktops to ensure "readiness." This applies to:

1. **Single-Family Homes** (1–2 dwellings):  
   - Dedicated circuits per **California Energy Code Section 150.0(u)**.  
   - Includes designated spaces, branch circuits, and receptacles for electric cooktops.

2. **Multifamily Buildings**:  
   - Dedicated circuits per **California Energy Code Section 160.9(b)** for each dwelling unit.  

This ensures future electric cooktops can be installed without retrofitting.

---
## NEC 2023 Reference  
The base NEC **does not mandate** dedicated circuits for electric cooktop readiness. California’s requirement is an **amendment added to the CEC** to support electrification goals and appliance readiness.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 150.0, 160.9, 422.3

**Response Time:** 6.8s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryer Circuits in California (CEC 2022)  

**California Requirement (CEC 2022):**  
Per **CEC 2022 Section 408.2(A)** and **408.2(B)**, new construction in California must include **dedicated circuit breaker spaces** in panelboards for electric clothes dryers. This applies to:  
- **Single-family buildings** (including 1–2 dwellings): Dryer circuit breaker space required per California Energy Code §150.0(n), (t), (u), and (v).  
- **Multifamily buildings**: Dryer circuit breaker space required per California Energy Code §160.9(a), (b), and (c).  

This requirement ensures future-ready infrastructure to support energy-efficient appliances like heat pump dryers, even if the dryer is not installed at the time of construction.  

---

### Exceptions Checked via `cec_exception_search(base_rule="408.2", context="electric clothes dryer")  
No exceptions directly modify or override **Section 408.2** requirements for dryer circuit breaker spaces. Related exceptions (e.g., 210.52(F), 220.54) address receptacle locations or load calculations, not panelboard pre-wiring.  

---

## NEC 2023 Reference  
The **NEC 2023** does **not** mandate pre-wiring for future dryers. It only requires:  
- A **240V, 30A circuit** for electric dryers (NEC 210.19(A)(3), 220.54).  
- No specific requirement to reserve panelboard spaces for future dryers.  

Thus, California’s CEC adds a **future-proofing requirement** not present in the national code.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 408.2, 210.19, 220.54, 210.52, 150.0, 160.9

**Response Time:** 9.1s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 240.4(G) Unique California Requirements with Exceptions

**California-Specific Amendment:**
CEC Table 240.4(G) includes **cross-references to California Title 24 Building Code regulations** (Government Code Sections 4450, Health & Safety Code Sections 18949.1, etc.) for overcurrent protection of specialized conductors. These references are **not present in NEC Table 240.4(G)**.

**Key California Additions:**
1. **Regulated Applications:** Directs users to Division of the State Architect regulations for applications in Section 1.9.1 of California Building Code.
2. **Surge Protection Interconnections:** Includes California-specific requirements for surge arrester interconnections (CEC 242.54) not found in NEC.
3. **Expanded Conductor Applications:** The table explicitly lists California-amended applications like fire alarm systems, capacitor circuits, and control circuits with references to state-specific codes.

**Critical Exceptions Affecting Table 240.4(G):**
1. **Surge Arrester Interconnections (242.54):**
   - Requires metal interconnections to secondary grounded conductors or grounding electrode conductors for surge arresters in California.
   - Permits alternative grounding methods for urban water-pipe areas or multigrounded neutral systems.
   - Special permission required for non-standard interconnections.

2. **Auxiliary Grounding Electrodes (250.54):**
   - Permits auxiliary grounding electrodes connected to equipment grounding conductors without bonding requirements, but prohibits using earth as a ground-fault current path.

**NEC vs CEC Difference:**
- NEC Table 240.4(G) only provides general cross-references to NEC articles.
- CEC Table 240.4(G) adds **California-specific regulatory cross-references** to Title 24 and other state codes, making it enforceable in California beyond NEC requirements.

**Exception Analysis:**
- The exceptions in 242.54 and 250.54 modify how overcurrent protection and grounding are applied for specialized systems i...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 250.54, 242.54, 240.4

**Response Time:** 12.6s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC Table 242.3 (California-Specific)  
**Title:** *Other Articles [California Amendment]*  
**Section:** Article 242 (Overvoltage Protection)  

**Description:**  
This California-specific table (marked as **NEW** in the CEC) serves as a cross-reference guide for overvoltage protection requirements. It directs users to other NEC articles that contain additional overvoltage protection (surge protection) requirements for specific equipment types.  

**Key Details:**  
- **Purpose:** Identifies which NEC articles apply to different equipment categories for surge protective device (SPD) installation.  
- **Examples of Equipment Types:**  
  - Class I locations (e.g., hazardous locations)  
  - Class II locations (e.g., commercial/industrial)  
  - Specific systems like PV installations, data centers, etc.  
- **California-Specific:** This table is **not present in the base NEC** and is added to clarify California's enhanced requirements for overvoltage protection in diverse installation scenarios.  

---

### CEC Exceptions Found  
While **Table 242.3 itself does not contain exceptions**, a related California amendment appears in **CEC Section 370.23** (Overcurrent Protection for Cablebus):  
- **Exception:** Overcurrent protection for cablebus is permitted under **240.100 and 240.101** instead of the standard 240.4.  

This shows California adds specific exceptions in related articles (e.g., cablebus overcurrent protection) that may intersect with overvoltage protection requirements.  

---

## NEC 2023 Reference  
The NEC does not include Table 242.3 or the 370.23 exception. California’s amendments add these requirements to address local installation needs.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 370.23, 240.4, 240.101, 240.100, 242.3

**Response Time:** 7.9s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC 2022 Table 430.72(B) - Motor Control Circuit Overcurrent Protection

**CEC 2022 Specification:**
Table 430.72(B) specifies **maximum ratings for overcurrent protective devices** for motor control circuits based on conductor size and installation conditions. Key details:

1. **Protection Methods:**
   - **Column A:** Separate overcurrent protection (when branch-circuit protection insufficient)
   - **Column B:** Branch-circuit protection for conductors **within** motor control equipment
   - **Column C:** Branch-circuit protection for conductors **beyond** motor control equipment

2. **Derating Rules:**
   - Values are derived from:
     - 300% of Table 310.16 (60°C conductors)
     - 400% of Table 310.17 (60°C conductors)
     - 310.15 adjustments for ambient temperature

3. **Critical Exceptions:**
   - **Exception 1:** Fire pump/control circuits may omit overcurrent protection if opening the circuit creates a hazard.
   - **Exception 2:** Transformers <50 VA in motor controllers may use primary-side protection.
   - **Transformer Protection:** Primary current <2A allows 500% of rated primary current for overcurrent devices.

---
## NEC 2023 Reference
NEC 430.72(B) contains similar structure but **lacks California-specific exceptions** for:
- Fire pump control circuits (CEC Exception 1)
- Low-power (<50 VA) control transformers (CEC Exception 2)
- Primary-side protection for specific transformer applications

The NEC version does not explicitly permit the primary-side overcurrent protection for control transformers described in CEC 430.72(C)(3).

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 430.72, 310.15, 310.16, 310.17

**Response Time:** 8.9s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in CEC vs NEC (With Exceptions)

**California-Specific Medium Voltage Tables in CEC 2022:**

1. **Table 305.15(A)**  
   *Minimum cover requirements for medium voltage systems*  
   - **Exception 300.5 [CEC]:** Allows Type MI and MC cables to be installed under buildings without raceways if embedded in concrete or protected per 332.10(6).  
   - This exception expands permitted burial methods for medium voltage cables beyond NEC requirements.

2. **Table 305.3**  
   *Wiring methods for systems over 1000V ac/dc*  
   - **Exception 300.5(D):** Requires protection for conductors emerging from grade (e.g., 2.5m of raceway protection).  
   - NEC lacks this specific protection requirement for medium voltage risers.

3. **Tables 315.10(A)-(B)**  
   *2001-5000V conductor insulation requirements*  
   - **Exception 310.12 [CEC]:** Permits reduced ampacity for dwelling services/feeders (83% of rating).  
   - NEC does not provide equivalent ampacity adjustments for medium voltage dwelling circuits.

---
## NEC 2023 Reference
NEC contains general medium voltage provisions in:
- Article 300 (Wiring Methods)
- Table 310.11 (Up to 600V only)
- Article 700 (Emergency Systems)

**Key CEC Exceptions Affecting Medium Voltage:**
- **300.5:** Expanded burial methods for MI/MC cables under buildings
- **310.12:** Reduced ampacity for dwelling services up to 400A
- **250.86:** Special grounding exemptions for short metal raceways

California's CEC adds specific medium voltage tables and exceptions not found in NEC, particularly for:
- Burial depths (Table 305.15)
- High-voltage insulation (Tables 310.4, 315.10)
- Special wiring methods (Table 305.3)

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 9 found
- 305.15, 305.3, 300.5, 310.11, 310.12, 250.86, 315.10, 310.4, 332.10

**Response Time:** 11.1s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer: Ampacity of 4/0 AWG Copper at 75°C (CEC 2022)

**California Requirement:**
Per **CEC 2022 Table 310.16**, the ampacity of **4/0 AWG copper conductor at 75°C** is **230 amperes** under standard conditions:
- Not more than three current-carrying conductors in the raceway/cable
- Ambient temperature of 30°C (86°F)
- Conductor insulation rated for 75°C

**Exceptions Checked:**
1. **Section 310.12** (Parallel Conductors): Allows parallel conductors in sizes 1/0 AWG and larger. Not applicable here since the question does not involve parallel conductors.
2. **Section 210.19** (Branch Circuit Loads): Requires 125% of continuous loads. This applies to load calculations but does not modify the base ampacity value itself.

**Footnotes to Apply:**
- If ambient temperature ≠ 30°C, apply correction factors from **CEC 310.15(B)**.
- If >3 current-carrying conductors, apply adjustment factors from **CEC 310.15(C)(1)**.
- Overcurrent protection must comply with **CEC 240.4(D)** (e.g., 250A breaker for 230A conductor).

---
## NEC 2023 Reference
No difference from NEC 2023 Table 310.16. The ampacity value of 230A for 4/0 AWG copper at 75°C is identical in both codes.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 310.15, 210.19, 310.16, 240.4, 310.12

**Response Time:** 13.7s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Size (CEC 2022)  

For a **200A circuit** in California, the required equipment grounding conductor (EGC) sizes are:  

- **Copper**: **6 AWG**  
- **Aluminum/Copper-Clad Aluminum**: **4 AWG**  

This is specified in **CEC 2022 Table 250.122**, which includes a California amendment ([CEC]) indicating modifications from the base NEC.  

---

### Exceptions Checked:  
1. **Section 250.121** allows an EGC to also serve as a grounding electrode conductor under specific conditions but does not affect sizing requirements.  
2. **Sections 356.60/352.60** permit alternative installation methods (e.g., separate grounding conductors) but do not override Table 250.122 sizing.  
3. **Section 250.134** allows separate routing of EGCs but does not modify minimum size requirements.  
4. **Section 250.54** permits auxiliary grounding electrodes but does not impact EGC sizing.  

No exceptions apply to the sizing requirements for a 200A circuit.  

---

## NEC 2023 Reference  
NEC 2023 Table 250.122 specifies the same conductor sizes (6 AWG copper, 4 AWG aluminum) for 200A circuits. The California amendment in CEC adds enforceable modifications not present in the national code.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 250.122, 356.60, 250.134, 352.60, 250.54, 250.121

**Response Time:** 7.7s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022)  
For a **3/0 AWG copper service conductor** in California:  

**Primary Requirement:**  
Per **CEC 2022 Table 250.66**, a **4 AWG copper grounding electrode conductor (GEC)** is required. This applies to service conductor sizes of **2/0 or 3/0 AWG** copper.  

**Exceptions Checked:**  
1. **250.66(A)**: If connected to a rod, pipe, or plate electrode **without extending to other electrode types**, the GEC could be reduced to **6 AWG copper**.  
2. **250.66(B)**: If connected to a **concrete-encased electrode**, the GEC could be reduced to **4 AWG copper** (same as table value).  
3. **250.66(C)**: If connected to a **ground ring**, the GEC size matches the ground ring conductor.  

**California Amendment [CEC]:**  
The CEC increases the minimum GEC size compared to NEC for certain service conductor sizes, ensuring enhanced fault current capacity.  

**Key Note:**  
Exceptions in 250.66(A)–(C) **only apply if the electrode type is specified** (e.g., rod, concrete-encased). Since no electrode type was specified in the question, the **4 AWG copper** from Table 250.66 remains the enforceable requirement.  

---
## NEC 2023 Reference  
NEC 2023 Table 250.66 would require a **2 AWG copper GEC** for a 3/0 AWG service conductor. California’s amendment increases the requirement to **4 AWG** for stricter fault current capacity.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 14.7s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)

For a 75°C rated conductor at 40°C ambient temperature, the temperature correction factor is **0.88** per CEC 2022 Table 310.15(B)(1).

No exceptions apply to this correction factor for standard installations. The factor is derived directly from the ambient temperature correction table without modifications specific to this scenario.

---
## NEC 2023 Reference
No difference from NEC 2023. The temperature correction factor for 40°C ambient with 75°C conductors is also 0.88 per NEC Table 310.15(B)(1).

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 7.0s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
The ampacity adjustment factor for **7-9 current-carrying conductors** in a raceway per California code is **0.70**, as specified in **CEC 2022 Table 310.15(C)(1)**.

This factor applies to all conductors in the raceway when the number exceeds three current-carrying conductors. The adjustment reduces the allowable ampacity of each conductor to account for heat buildup from closely bundled conductors.

**Key Exceptions:**
- Adjustment factors do not apply to conductors in raceways ≤600 mm (24 in.) long.
- Adjustment factors do not apply to underground conductors with physical protection (e.g., rigid conduit) ≤3.05 m (10 ft) long with ≤4 conductors.
- Specific exceptions for Type AC/MC cables with ≤20 conductors (see 310.15(C)(1)(d)).

---
## NEC 2023 Reference
No difference from NEC 2023. NEC 2023 Table 310.15(C)(1) also specifies a **0.70 adjustment factor** for 7-9 current-carrying conductors in a raceway.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 9.6s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth for 480V Panelboard (Condition 3) - CEC 2022

**California Requirement:**
Per CEC 2022 Table 110.26(A)(1), the **minimum working space depth** for equipment operating at **480V** under **Condition 3** (exposed live parts on both sides of the working space) is:

**1.2 meters (4 feet)**

This applies to voltage ranges of 151–600V and is specified in CEC Section 110.26(A)(1).

---

### Exceptions Checked:
1. **Dead-Front Assemblies** (110.26(A)(1)(a)):  
   - Not applicable here unless the panelboard is a dead-front assembly with rear access only for non-electrical parts.

2. **Low Voltage Permission** (110.26(A)(1)(b)):  
   - Only applies to systems ≤30V AC/RMS, 42V peak, or 60V DC. Not applicable to 480V.

3. **Existing Buildings** (110.26(A)(1)(c)):  
   - Allows Condition 2 clearances for panelboards in existing buildings. Does not reduce depth requirements for Condition 3.

4. **Battery Systems** (Exception No. 1):  
   - Applies only to battery systems on open racks. Not relevant here.

5. **Existing Dwelling Units** (Exception No. 2):  
   - Permits reduced height (not depth) for service equipment ≤200A in existing dwellings. Does not affect depth requirement.

---

## NEC 2023 Reference
No difference from NEC 2023. The same 1.2 m (4 ft) requirement applies under NEC Table 110.26(A)(1) for Condition 3 at 480V.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 10.7s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

**California Requirement (CEC 2022 Table 110.28):**  
For outdoor use with exposure to rain, sleet, and ice, the suitable enclosure types are:  
- **Raintight Enclosures**: Types 3, 3S, 3SX, 3X  
- **Watertight Enclosures**: Types 4, 4X, 6, 6P  

**Key Notes:**  
1. **Raintight Enclosures** (Types 3, 3S, 3SX, 3X) protect against rain, sleet, and ice but not full submersion.  
2. **Watertight Enclosures** (Types 4, 4X, 6, 6P) provide protection against water ingress from all directions, including severe weather.  
3. **Operability in Ice**: Mechanisms must remain operable when ice-covered (per CEC 110.28).  

**Exception Analysis:**  
- No exceptions to Table 110.28 override the specified enclosure types for outdoor use.  
- Exceptions in Sections 110.70, 110.26(E), and 110.31 address installation practices (e.g., dedicated spaces, access control) but do not modify the enclosure type requirements.  

**CEC 2022 References:**  
- Section 110.28 (Table 110.28) defines enclosure types for environmental conditions.  
- Section 409.100 reinforces the use of Table 110.28 for industrial control panels.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The same enclosure types (3, 3S, 3SX, 3X, 4, 4X, 6, 6P) are specified in NEC Table 110.28 for outdoor use with rain, sleet, and ice.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 409.100, 110.28, 110.70, 110.26, 110.31

**Response Time:** 10.9s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 3.5 VA per square foot per CEC 2022 Table 220.12 [California Amendment]

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## Final Answer: General Lighting Load for Office Buildings (CEC 2022)

### **California Requirement (CEC 2022):**
The general lighting load for **office buildings** is determined using **Table 220.12** of the CEC 2022. This table specifies unit loads in **volt-amperes per square foot (VA/ft²)** for non-dwelling occupancies. For office buildings, the base NEC value is **1 VA/ft²**, but California amendments (marked with [CEC]) may adjust this. However, the exact value for office buildings is not explicitly shown in the retrieved tool results. You must consult **Table 220.12** directly in the CEC document for the precise VA/ft² value.

**Key Notes:**
- The 125% continuous load multiplier from **210.20(A)** is already included in Table 220.12 values.
- **Exceptions to 220.12** (e.g., energy code compliance with monitoring systems) do not override the base unit load values but provide alternative calculation methods under specific conditions.

---

### **NEC 2023 Reference**
- **NEC 2023 Table 220.12** specifies **1 VA/ft²** for office buildings. California’s CEC may adjust this value, but the base NEC requirement remains unchanged unless modified by local amendments.

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 220.12, 210.20

**Response Time:** 16.2s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1) [California Amendment]

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022  

**California Requirement (CEC 2022):**  
Per **CEC 2022 Table 400.5(A)(1)**, the ampacity for a **12 AWG flexible cord with Column B thermoset insulation** (two-conductor configuration) is **15 amperes** at an ambient temperature of 30°C (86°F).  

**Key Exceptions and Limitations:**  
1. **Permitted Uses Only** (CEC 400.10):  
   - Flexible cords must be used only for specific applications (e.g., pendants, portable appliances, moving parts).  
   - **Not permitted** as a substitute for fixed wiring or in concealed locations (e.g., walls, ceilings).  

2. **Temperature and Bundling Derating:**  
   - If ambient temperature exceeds 30°C, apply **temperature correction factors** from **Table 310.15(B)(1)**.  
   - For more than three current-carrying conductors, apply **adjustment factors** from **Table 400.5(A)(3)**.  

3. **Insulation Limitations:**  
   - Column B thermoset cords are rated for 60°C operation. Exceeding this temperature rating is prohibited (CEC 400.5(B)).  

**NEC 2023 Reference:**  
No difference from NEC 2023. The ampacity and derating requirements are identical.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.15, 400.5, 400.10

**Response Time:** 23.0s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

**California Requirement (CEC 2022):**  
Type SF-2 silicone insulated fixture wire is permitted for use in luminaires and similar equipment where enclosed or protected (per CEC 402.10). However, **the maximum operating temperature is not explicitly specified in CEC 2022** for this conductor type. The general temperature limitation rule (CEC 310.14) applies, which prohibits exceeding the conductor's designated temperature rating based on its insulation type.

**NEC 2023 Reference:**  
NEC 402.8(A) specifies that Type SF-2 fixture wire has a **temperature rating of 105°C**. Since CEC 2022 contains no amendments to this requirement, California adopts the national code value.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 402.8, 402.10, 310.14

**Response Time:** 8.4s

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

1. **Base Ampacity** (CEC 2022 Table 310.16):
   8 AWG copper, 75°C column = **50 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   40°C ambient, 75°C conductor = **0.88 factor**

3. **Adjustment Factor** (CEC 2022 Table 310.15(C)(1)):
   7 current-carrying conductors = **0.70 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 50 × 0.88 × 0.70 = 30.8 amperes
   ```

**Final Answer: 30.8 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

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

**Response Time:** 12.1s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]

**Service Conductors:**  
For a 200A residential service in California using copper conductors:  
- **Size:** 4/0 AWG copper  
- **Ampacity:** 230A at 75°C (per CEC 2022 Table 310.16)  
- **Rationale:** 4/0 AWG provides sufficient ampacity (230A) to meet the 200A service requirement while accounting for standard ambient temperature (30°C) and up to three current-carrying conductors.  

**Key Exceptions Checked:**  
- **Section 310.12 (Single-Phase Dwelling Services):** Allows service conductors to be sized at 83% of the service rating (200A × 83% = 166A). 4/0 AWG (230A) complies with this exception if no adjustment/correction factors apply.  
- **Section 210.19 (Branch Circuit Ampacity):** Not applicable here, as this addresses service conductors, not branch circuits.  

**Equipment Grounding Conductor (EGC):**  
- **Size:** 4 AWG copper  
- **Reference:** CEC Table 250.122 (for a 200A overcurrent device).  

**Grounding Electrode Conductor (GEC):**  
- **Size:** 4 AWG copper  
- **Reference:** CEC Table 250.66 (minimum size for a 200A service with a ground rod electrode).  

**Key Considerations:**  
1. **Ampacity Derating:** If ambient temperature exceeds 30°C or there are more than three current-carrying conductors in a raceway, apply correction factors from CEC Sections 310.15(B) and 310.15(C)(1).  
2. **Overcurrent Protection:** Section 240.4(D) limits overcurrent protection for small conductors, but 4/0 AWG with 230A ampacity complies with 200A protection.  

No CEC exceptions override these requirements.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The same conductor, EGC, and GEC sizes apply under NEC Tables 310.16, 250.122, and 250.66.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 310.15, 250.122, 210.19, 310.16, 240.4, 310.12, 250.66

**Response Time:** 12.7s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 3.5 VA per square foot. General lighting load = 5,000 sq ft x 3.5 VA/sq ft = 17,500 VA (17.5 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)  
**For a 5,000 sq ft office building:**  

1. **Base Calculation (CEC 2022 Table 220.12):**  
   - Office occupancies require **1.5 VA/ft²** [CEC 220.12(A)].  
   - Total load:  
     $$
     5,000 \, \text{ft}^2 \times 1.5 \, \text{VA/ft}^2 = 7,500 \, \text{VA}
     $$  

2. **Continuous Load Multiplier:**  
   - The **125% multiplier** for continuous loads (per 210.20(A)) is **already included** in Table 220.12 values [CEC 220.12 Note].  

3. **Exception for Energy Code Compliance (CEC 220.12(B)):**  
   - If the building complies with a local energy code, the lighting load may be calculated using energy code values **instead of Table 220.12**.  
   - **Conditions required:**  
     - Power monitoring system with alarms for load exceedance.  
     - No demand factors from 220.42 applied.  
     - 125% continuous load multiplier still required.  

**Final General Lighting Load:** **7,500 VA** (default method).  
*Alternative method under 220.12(B) available if energy code compliance conditions are met.*  

---
## NEC 2023 Reference  
No difference from NEC 2023. NEC Article 220.12 uses identical unit loads for office occupancies (1.5 VA/ft²).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 220.12, 210.20, 220.42

**Response Time:** 10.2s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Copper in Motor Control Circuits (CEC 2022)

**CEC Requirement:**
- **16 AWG copper conductors** in motor control circuits are permitted under **CEC 430.22(G)(2)** for motors with full-load current ratings between **5.5A and 8A**.
- **Maximum overcurrent protection** is governed by **CEC 240.4(D)(2)(2)**, which limits 16 AWG copper to **15A** overcurrent protection devices.

**Key Conditions:**
1. The motor must have **Class 10 or 10A overload protection** (per 430.32).
2. Overcurrent protection must comply with **240.4(D)(2)(2)** (15A for 16 AWG copper).
3. The circuit must be protected per **430.52** (motor circuit overcurrent protection).

**NEC 2023 Reference:**
- No difference from NEC 2023. Same requirements apply for 16 AWG copper in motor control circuits.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 430.32, 430.52, 430.22, 240.4

**Response Time:** 10.0s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## Final General Lighting Load Calculation (CEC 2022)

**California Requirement (CEC 2022 Section 220.82(B)(1)):**
For a single dwelling unit, the general lighting load is calculated at **3 volt-amperes per square foot (33 VA/m²)**. 

**Calculation:**
- Floor area = 2,400 sq ft  
- General lighting load = 2,400 sq ft × 3 VA/sq ft = **7,200 volt-amperes**

**Exception Analysis:**
- **Section 220.85** (two dwelling units): Not applicable (single dwelling unit).
- **Section 220.12** (non-dwelling occupancies): Not applicable (dwelling unit).
- **Section 220.52** (small-appliance/laundry circuits): These loads are *added to* the general lighting load but do not modify the base 3 VA/sq ft calculation.
- **Section 220.40** (feeder/service calculations): Not applicable to this specific general lighting load calculation.

No exceptions modify the base 3 VA/sq ft requirement for this scenario.

---
## NEC 2023 Reference
No difference from NEC 2023. The national code also specifies 3 VA/ft² for dwelling unit general lighting loads per NEC 2023 Section 220.82(B)(1).

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 220.52, 220.40, 220.12, 220.85, 220.82

**Response Time:** 9.7s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## Final Answer: CEC 2022 vs NEC 2023 Kitchen GFCI Requirements  

### **CEC 2022 Exceptions**  
1. **Listed locking receptacles** for ceiling luminaires/fans (if not general-purpose).  
2. **Receptacles for fire alarm systems** (not GFCI-protected).  

### **NEC 2023 Exceptions**  
1. **HVAC equipment** (until 2026).  
2. **Security systems**.  
3. **Factory-installed, non-accessible receptacles** in bathroom exhaust fans.  

---

### **Restrictiveness Comparison**  
**CEC 2022 is more restrictive** because:  
- It allows **fewer exceptions** (only 2 vs. NEC’s 3+).  
- It **does not permit temporary exemptions** (e.g., HVAC).  
- Its scope is narrowly focused on **countertop receptacles**, while NEC includes broader kitchen areas.  

---

### **Key Code Citations**  
- **CEC 2022**: 210.8(A)(6) (kitchen countertop GFCI), exceptions in 210.8.  
- **NEC 2023**: 210.8(A)(5) (kitchen GFCI), exceptions in 210.8.  

---

### **NEC 2023 Reference**  
No difference in core kitchen GFCI requirements, but NEC permits more exceptions.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 210.8

**Response Time:** 16.8s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2 requires reserved panelboard spaces for heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers, and EV charging equipment. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

### **California Electrical Code (CEC 2022) Panelboard Requirements**
1. **Mandatory Pre-Wiring for Appliances**  
   - **CEC 408.2(A)** requires single-family panelboards to include dedicated spaces for heat pump water heaters, space heaters, electric cooktops, and dryers.  
   - **Exception:** No exceptions apply to this appliance-specific pre-wiring requirement.  

2. **Wire-Bending Space Exceptions**  
   - **CEC 408.55(A)** allows reduced wire-bending space (per Table 312.6(A)) for panelboards rated ≤225A with ≤42 overcurrent devices.  
   - **Example:** A 200A panelboard with 40 circuit breakers qualifies for this exception.  

3. **Enclosure Exceptions**  
   - **CEC 408.38** permits non-dead-front panelboards if accessible only to qualified personnel (e.g., in utility rooms).  

4. **Overcurrent Protection Exceptions**  
   - **CEC 408.36** allows two main breakers (combined ≤ panelboard rating) for panelboards with ≤42 overcurrent devices.  

---

### **NEC 2023 Comparison**
- **No appliance pre-wiring mandates** exist in NEC for single-family dwellings.  
- Wire-bending, enclosure, and overcurrent rules align with CEC but **lack California’s specific exceptions** (e.g., 42-overcurrent-device limit in 408.55).  

---

### **Key Takeaways**
- **California’s CEC 408.2(A)** uniquely requires pre-wiring for energy-efficient appliances, ensuring future readiness.  
- **Exceptions in CEC 408.55 and 408.36** provide flexibility for smaller panelboards and existing installations, reducing space/overcurrent requirements under specific conditions.  
- **NEC remains neutral** on appliance pre-wiring, leaving it to local amendments.  

This comparison highlights California’s proactive approach to electrification while maintaining alignment with NEC for core panelboard design rules.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 312.6, 408.36, 408.2, 408.38, 408.55

**Response Time:** 12.1s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## Updated Comparison with Exceptions

---

### **Exceptions Affecting CEC EV Requirements**

#### **1. CEC 625.46 - Loss of Primary Source**
- **Requirement**:  
  EV systems must prevent backfeeding to premises wiring when utility power is lost, unless permitted by **625.48** (power export systems).  
- **Impact**:  
  Adds safety layer for bidirectional systems (e.g., solar + EV).  
- **NEC Comparison**:  
  NEC 705.61 addresses anti-islanding for PV systems but does not explicitly require backfeed prevention for EVs.  

---

#### **2. CEC 225.30(A)(7) - Multiple Feeders for EV Systems**
- **Exception**:  
  Allows **multiple branch circuits/feeds** for EV charging systems if:  
  - Listed/identified for multi-circuit use.  
  - Installed per 225.30(A)(7).  
- **Example**:  
  Apartment complexes with multiple EV circuits per unit.  
- **NEC Comparison**:  
  NEC 225.30(A)(7) is identical, but CEC integrates it into EV-specific rules (625.40).  

---

### **Revised Key Differences Table**

| **Requirement**               | **CEC 2022**                                                                 | **NEC 2023**                          |
|-------------------------------|-------------------------------------------------------------------------------|----------------------------------------|
| **Backfeed Prevention**       | Required by 625.46 (anti-backfeed on utility loss)                            | Addressed in 705.61 (PV only)           |
| **Multiple EV Circuits**      | Permitted via 225.30(A)(7) for multi-unit systems                            | Same exception exists but less integrated with EV rules |
| **CALGreen Compliance**       | Mandatory for new construction (625.1)                                       | Not applicable                         |
| **Weatherproof Enclosures**   | Required for wet-location EV receptacles (625.56)                          | No specific requirement                |
| **Truck Parking Systems**     | Dedicated article...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 7 found
- 625.46, 625.1, 625.56, 225.30, 625.48, 705.61, 625.40

**Response Time:** 18.6s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## **CEC 2022 vs NEC 2023 AFCI Protection Requirements for Dwelling Units**

---

### **California Electrical Code (CEC 2022) Requirements**  
**Section 210.12(A) Dwelling Units**  
- **Scope**: All 120V, single-phase, 15- and 20-ampere branch circuits supplying outlets in kitchens, family rooms, bedrooms, and similar areas **must** have AFCI protection.  
- **Permitted Methods**:  
  1. **Combination-type AFCI** (protects entire circuit).  
  2. **Branch/feeder-type AFCI + outlet branch-circuit AFCI** (at first outlet).  
  3. **Supplemental arc protection circuit breaker + outlet AFCI** (with conductor length limits: 50 ft for 14 AWG, 70 ft for 12 AWG).  
  4. **Outlet branch-circuit AFCI + overcurrent device** (with same length limits).  
  5. **Outlet AFCI at first outlet** if branch circuit uses metal raceway, MC cable, or is encased in ≥2 in. concrete.  
  6. **Outlet AFCI at first outlet** for nonmetallic conduit.  

**Exceptions**:  
- **Fire alarm circuits** (installed per 760.41(B) or 760.121(B)) are exempt if in metal raceway or MC cable.  
- **Branch circuit extensions ≤6 ft** (1.8 m) without additional outlets (excluding enclosures/junction boxes).  

---

### **NEC 2023 Requirements**  
**Section 210.12(A) Dwelling Units**  
- **Scope**: Same as CEC—15- and 20-ampere circuits in kitchens, living areas, bedrooms, etc., require AFCI protection.  
- **Permitted Methods**:  
  1. **Combination-type AFCI**.  
  2. **Branch/feeder-type AFCI + outlet AFCI** (at first outlet).  
  3. **Outlet branch-circuit AFCI** (at first outlet) if branch circuit uses metal raceway or MC cable.  

**Exceptions**:  
- **Receptacle replacements**: If replacing a receptacle in an AFCI-protected circuit, NEC 404.22(C)(4) allows:  
  - Outlet branch-circuit AFCI receptacle.  
  - Receptacle protected by an outlet branch-circuit AFCI.  
  - Receptacle protected by a combination-type AFCI breaker.  

---

### **Key Differences (CEC vs NEC)**  
1. **Additional CEC Permitted Methods...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 404.22, 760.121, 210.12, 760.41

**Response Time:** 12.8s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## California Solar PV Requirements vs NEC 2023 Article 690

**California (CEC 2022) Specific Requirements:**
1. **Arc-Fault Protection (690.11):**  
   - DC arc-fault protection required for PV systems ≥80Vdc.  
   - **Exception:** Systems in metallic raceways, metal-clad cables, or underground installations may skip arc-fault protection.  
   - [CEC] Adds fire mitigation plans for non-compliant systems (691.10).

2. **Energy Storage Systems (690.71):**  
   - Must comply with **Article 706** for energy storage integration.  
   - [CEC] Explicitly ties PV systems to energy storage requirements.

3. **Connections to Other Sources (690.59):**  
   - Follows **Article 705 (Part I/II)** and **Article 712** for hybrid systems.  
   - [CEC] Emphasizes compliance with California-specific interconnection rules.

4. **Stand-Alone Systems (690.10):**  
   - Follows **Article 710** for off-grid systems.  
   - [CEC] Permits exceptions for non-building installations (e.g., ground-mounted arrays).

---

**NEC 2023 Article 690 Focus:**  
- Defines general PV system requirements (e.g., DC circuits, module connections).  
- No explicit arc-fault exceptions for non-building installations.  
- Energy storage integration referenced in **Article 706** but not explicitly tied to PV systems.  

---

**Key Differences:**  
1. **Arc-Fault Exceptions:** CEC allows exemptions for non-building installations; NEC requires protection universally.  
2. **Interconnection Rules:** CEC mandates compliance with **Article 705/712** for hybrid systems, while NEC provides broader guidance.  
3. **Fire Mitigation Plans:** CEC requires documentation for non-compliant systems (691.10); NEC lacks this requirement.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 691.10, 690.11, 690.59, 690.71, 690.10

**Response Time:** 9.3s

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

