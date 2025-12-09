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
| **Total Duration** | 389.5s |
| **Avg per Question** | 13.0s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2 requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, (4) electric clothes dryers, and (5) electric vehicle charging equipment. This is a California-specific requirem...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements and Reserved Circuit Breaker Spaces in California (CEc_search + cec_exception_search)  

---

### **1. Panelboard Space Requirements (CEC 2022 Section 408.55)**  
**Wire-Bending Space Dimensions**  
- **Top/Bottom**: Sized per **Table 312.6(B)** for the largest conductor, **unless exceptions apply**.  
- **Side**: Sized per **Table 312.6(A)** for the largest conductor.  
- **Back**: Must comply with **Table 312.6(A)** for raceway/cable entries opposite removable covers.  

**Exceptions** (from `cec_exception_search`):  
1. **Exception 1**: For panelboards rated **≤225A** with **≤42 overcurrent devices**, top/bottom space can use **Table 312.6(A)**.  
2. **Exception 3**: If wiring uses **only single 90° bends** (per manufacturer’s wiring diagram), top/bottom space can use **Table 312.6(A)**.  
3. **Exception 4**: If **no conductors terminate** in a top/bottom space, that space can use **Table 312.6(A)**.  

---

### **2. Reserved Circuit Breaker Spaces for Appliances (CEC 2022 Section 408.2)**  
**Mandatory Reserved Spaces**  
California requires **panelboards in single-family dwellings** to include **dedicated circuit breaker spaces** for:  
- Heat pump water heaters  
- Heat pump space heaters  
- Electric cooktops  
- Electric clothes dryers  

**Exceptions** (from `cec_exception_search`):  
- No exceptions override this requirement. The reserved spaces are **mandatory** under California Energy Code (Sections 150.0(n), (t), (u), (v)).  

---

### **3. NEC 2023 Comparison**  
- **Standard NEC**: No mandatory reserved spaces for these appliances unless specified by local amendments.  
- **California CEC**: Adds **future-ready requirements** to support energy efficiency goals (e.g., Title 24 Energy Code).  

---

### **Key Compliance Notes**  
- **Wire-Bending Space**: Use exceptions for smaller panelboards (≤225A, ≤42 devices) or specific wiring methods.  
- **Reserved Spaces**: No exceptions apply—California mandates these spaces fo...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 408.55, 150.0, 408.2, 312.6

**Response Time:** 14.7s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. CEC 408.2 requires panelboard spaces for EV charging equipment. Title 24 also mandates EV charging readiness.

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California Electrical Requirements for EV Charging in New Residential Construction (CEC 2022)  

### **Key CEC 2022 Requirements**  
1. **Dedicated Branch Circuit (625.40)**  
   - Each EV charging outlet **must be supplied by an individual branch circuit** with **no other outlets** on the same circuit.  
   - **Exceptions**:  
     - **625.47**: Allows **multiple feeders/branch circuits** if equipment is identified for the application.  
     - **625.46**: Requires **anti-backfeed protection** for systems with power export capabilities (e.g., bidirectional charging).  

2. **Scope and Compliance (625.1)**  
   - EV systems must comply with:  
     - **CALGreen Chapter 4/5** (new construction/existing buildings).  
     - **UL 2594/2202** safety standards for EV supply equipment.  

3. **Weatherproof Enclosures (625.56)**  
   - Outdoor receptacles must have **weatherproof enclosures** with **extra-duty outlet box hoods** (California-specific requirement).  

4. **GFCI Protection (625.56(D))**  
   - **GFCI protection** is mandatory for all EV receptacles, with **readily accessible reset/indication**.  

---

### **NEC 2023 Comparison**  
- **Similar Requirements**:  
  - NEC 625.40 also mandates **dedicated branch circuits** for EV charging.  
  - NEC 625.56 includes **GFCI protection** and weatherproof enclosures for outdoor receptacles.  

- **California-Specific Additions [CEC]**:  
  - **CALGreen integration** (no NEC equivalent).  
  - **Extra-duty enclosure requirement** for outdoor receptacles (more stringent than NEC).  
  - **Anti-backfeed provisions** (625.46) for bidirectional systems.  

---

### **Exceptions and Overrides**  
- **625.46**: Applies to systems with **power export functions** (e.g., bidirectional charging). Requires anti-backfeed mechanisms unless 625.48 permits otherwise.  
- **625.47**: Permits **multiple feeders/branch circuits** if equipment is identified for such use (e.g., high-capacity systems).  

---

### **Cross-References an...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 625.1, 625.40, 625.46, 625.56, 625.47, 625.48

**Response Time:** 13.0s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California-Specific Solar PV Requirements (CEC 2022)

### **Key CEC 2022 Requirements for Residential Solar PV Systems**
1. **Voltage Limits** (CEC 2022 690.7):
   - **Maximum DC Voltage**: 
     - **600V** for residential systems (vs. 1000V for non-residential).
     - **1500V** permitted for outdoor systems using listed equipment (e.g., ground-mounted arrays).
   - **Voltage Calculation**: Must account for temperature corrections (Table 690.7(A)) and lowest expected ambient temperatures.

2. **Arc-Fault Protection** (CEC 2022 690.11):
   - **Mandatory** for DC circuits ≥80V in **buildings**.
   - **Exceptions**:
     - Systems in **metallic raceways**, **metal-clad cables**, or **underground** installations.
     - Detached structures housing PV equipment (not considered "buildings").

3. **Conductor Sizing** (CEC 2022 690.8):
   - Conductors must be sized for **125% of calculated maximum current** (690.8(B)(1)).
   - Exceptions for systems rated for continuous operation at 100% of their rating.

4. **Stand-Alone Systems** (CEC 2022 690.10):
   - Must comply with **710.15** (standby power systems).

5. **General Requirements** (CEC 2022 690.4):
   - Equipment (inverters, combiners, etc.) must be **listed/evaluated** for the application.
   - Installations must be performed by **qualified personnel**.
   - **No PV equipment in bathrooms**.

---

## NEC 2023 Comparison
- **Voltage Limits**: NEC allows 1000V for residential systems (CEC reduces to 600V for dwellings).
- **Arc-Fault Protection**: NEC requires DC arc-fault protection for systems ≥80V in buildings (same as CEC), but CEC adds exceptions for non-building installations.
- **Conductor Sizing**: NEC uses similar 125% rule but lacks CEC's explicit 600V residential limit.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 690.10, 710.15, 690.11, 690.4, 690.7, 690.8

**Response Time:** 8.9s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Circuit Requirements for Heat Pump Water Heaters in New Dwellings (CEC 2022)

**California Requirement (CEC 2022):**
Per **CEC 2022 Section 422.3(A)** and **408.2(A)**, new single-family dwelling units must include:
1. **Dedicated branch circuits** for heat pump water heaters as specified in **California Energy Code Section 150.0(n)**.
2. **Panelboard circuit breaker spaces** reserved for heat pump water heaters in panelboards serving the dwelling unit (per **CEC 408.2(A)**).

**Exceptions Checked:**
- **Section 422.12** (central heating equipment exceptions) does not apply to heat pump water heaters, as their dedicated circuit requirement is explicitly mandated in 422.3(A).
- **Section 422.11** (overcurrent protection) and **408.36** (panelboard overcurrent protection) do not override the readiness requirements for heat pump water heater circuits.
- No exceptions invalidate the dedicated circuit or panelboard space requirements for heat pump water heaters.

These requirements ensure electrical systems are pre-wired to accommodate heat pump water heaters, aligning with California's energy efficiency standards.

---
## NEC 2023 Reference
The base NEC 2023 does not mandate dedicated circuits or panelboard spaces for heat pump water heaters. This is a **California-specific amendment** [CEC] to promote readiness for energy-efficient appliances.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 408.36, 408.2, 422.12, 422.3, 150.0, 422.11

**Response Time:** 13.5s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness Requirements (CEC 2022)

**California Requirement:**
Per **CEC 2022 Section 408.2**, new residential buildings must include **dedicated circuit breaker spaces** in panelboards for electric cooktops:

1. **Single-Family Buildings** (408.2(A)):
   - Panelboards must have spaces for:
     - Electric cooktops
     - Heat pump water heaters
     - Heat pump space heaters
     - Electric clothes dryers
   - Mandated by California Energy Code Section 150.0(n), (t), (u), and (v)

2. **Multifamily Buildings** (408.2(B)):
   - Panelboards must have spaces for:
     - Electric cooktops
     - Electric clothes dryers
     - Heat pump space heaters
   - Mandated by California Energy Code Section 160.9(a), (b), and (c)

**Exceptions Checked:**
- No exceptions apply to Section 408.2 requirements for electric cooktop readiness. The exceptions found (408.38, 408.36, 408.40) relate to panelboard enclosures, overcurrent protection, and grounding - none modify or exempt the mandatory circuit breaker space requirements for cooktops.

This ensures future-ready electrical infrastructure for electric cooking appliances, aligning with California's clean energy goals.

---
## NEC 2023 Reference
The base NEC 2023 does not include these specific requirements for pre-wiring panelboards for electric cooktops. These are **California-specific amendments** [CEC] to promote electrification of cooking in new construction.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 408.36, 408.40, 408.2, 160.9, 408.38, 150.0

**Response Time:** 8.4s

---

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric clothes dryer branch circuits in single-family dwellings. This is a California-specific requirement for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Panelboard Requirements for Electric Clothes Dryers in California New Construction (CEC 2022)

**California Requirements (CEC 2022):**
1. **Single-Family Buildings** (Section 408.2(A) + 422.3(A)):
   - Panelboards **must include dedicated circuit breaker spaces** for electric clothes dryers.
   - Dryers must have **dedicated circuits and circuit identifications** per California Energy Code §150.0(v).
   - This applies even if the dryer is not immediately installed ("readiness" requirement).

2. **Multifamily Buildings** (Section 408.2(B) + 422.3(B)):
   - Panelboards **must include dedicated circuits** for electric clothes dryers.
   - Dryers must comply with Energy Code §160.9(c) for circuit readiness.

3. **Load Calculations** (Section 220.54):
   - Dryers are calculated at **5000 VA minimum** for load calculations.
   - Demand factors from Table 220.54 apply for multiple dryers.

**Exceptions Found:**
- **210.52(F) Laundry Receptacle Exceptions**:
  - In multifamily buildings, **no receptacle is required** if shared laundry facilities exist for all occupants.
  - In non-one-family dwellings, **no receptacle required** if laundry facilities are not to be installed/permited.
  - *Note: These exceptions apply to receptacle requirements, not the panelboard circuit readiness mandates.*

- **220.54 Load Calculation Exception**:
  - Load calculations use 5000 VA minimum, but this **does not exempt** panelboard readiness requirements.

- **422.23 Special Permission Exception**:
  - Non-standard installations require special permission, but this **does not override** the panelboard readiness requirements.

**Key Takeaway:**  
California's panelboard readiness requirements for dryers are **mandatory in new construction** (single- and multifamily) regardless of immediate appliance installation. Exceptions only apply to receptacle requirements in specific scenarios, not the panelboard circuit provisions.

---
## NEC 2023 Reference
The base NEC 2023 **does not require** pa...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 422.23, 408.2, 160.9, 220.54, 210.52, 422.3, 150.0

**Response Time:** 12.5s

---

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 240.4(G), Table 240.4(G) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Final Answer

**CEC Table 240.4(G) does not contain unique California amendments** in its structure, but **an exception in CEC Section 370.23** provides California-specific overcurrent protection rules for cablebus systems:

- **CEC Exception 370.23**:  
  *"Overcurrent protection shall be permitted in accordance with 240.100 and 240.101"* [CEC].  
  This allows cablebus systems to use the overcurrent protection methods in Sections 240.100/101, which differ from general requirements in 240.4. This exception is unique to California and not present in NEC 2023.

The table itself cross-references to NEC articles (e.g., 760 for fire alarms), but **no [CEC] amendments** were found in those referenced sections. The only California-specific modification is the exception for cablebus systems in 370.23.

---

## NEC 2023 Reference  
NEC 2023 Table 240.4(G) and Section 370.23 (if present) would follow national requirements without the California exception.

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 240.4, 240.100, 240.101, 370.23

**Response Time:** 15.1s

---

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California installations?

**Expected:** CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**CEC Ref:** CEC 242.3, Table 242.3 | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC 2022 Table 242.3 Requirements (California)  
**Verified by CEC 2022 Section 242.3 with Exception Check**  

**Key Provisions:**  
1. **Cross-Reference Function**  
   - Table 242.3 directs users to **specific NEC articles** containing overvoltage protection requirements for equipment types (e.g., Class I locations → Article 501, wind systems → Article 694).  
   - This is a **California-specific addition** (marked [N]) not present in the base NEC.  

2. **Code Enforcement Use**  
   - Per **CEC 2022 Section 242.3**, equipment must be protected against overvoltage in accordance with the referenced article for its type/location.  
   - Example: Fire pump overvoltage protection requirements are found in **Article 695** (per Table 242.3).  

3. **Scope Context**  
   - Article 242 (Overvoltage Protection) replaces former NEC Articles 280 and 285 in California.  
   - Part II covers surge-protective devices (SPDs) ≤1000V, Part III covers surge arresters >1000V.  

**Full Table Contents:**  
| Equipment | Referenced NEC Article |  
|---------|------------------------|  
| Class I locations | 501 |  
| Class II locations | 502 |  
| Community antenna TV/radio systems | 820 |  
| Critical operations power systems | 708 |  
| Elevators/dumbwaiters/escalators | 620 |  
| Emergency systems | 700 |  
| Equipment >1000V nominal | 490 |  
| Fire pumps | 695 |  
| Industrial machinery | 670 |  
| Information technology equipment | 645 |  
| Modular data centers | 646 |  
| Outdoor overhead conductors >1000V | 399 |  
| Radio/TV equipment | 810 |  
| Receptacles/cord connectors | 406 |  
| Wind electric systems | 694 |  

**Exception Check:**  
- **No direct exceptions** apply to Table 242.3 itself.  
- A related exception exists in **Section 370.23** regarding overcurrent protection for cablebus (not overvoltage), but this does not affect Table 242.3 requirements.  

**NEC 2023 Reference**  
This table **does not exist in the national code**. CEC Table 242.3 is a **Californ...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 242.3, 370.23

**Response Time:** 15.7s

---

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of overcurrent protective devices for motor control circuits based on conductor size and configuration. It includes columns for separate protection, conductors within enclosure, and conductors extending beyond enclosure for both copper and aluminum condu...

**CEC Ref:** CEC 430.72(B), Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## CEC 2022 Table 430.72(B) - Motor Control Circuit Overcurrent Protection  
**With Full Code Context and Exceptions**

---

### **Table Summary**  
Specifies maximum overcurrent protective device ratings (circuit breakers/fuses) for motor control circuits based on conductor size and installation type.  
- **Column A:** General protection for control circuits not extending beyond motor control equipment.  
- **Column B:** Protection for circuits with conductors extending beyond the control equipment enclosure.  
- **Column C:** Reduced protection for continuous-duty control circuits.  

**Example:**  
- **12 AWG copper:**  
  - Column A: (Note 1)  
  - Column B: 120A  
  - Column C: 60A  

---

### **Key Code Requirements and Exceptions**  
1. **General Overcurrent Protection (430.225)**  
   - **Coordination Requirement:** Motor circuits must have coordinated protection to interrupt overload and fault currents.  
   - **Critical Motor Exception:** For motors where interruption creates a greater hazard (e.g., fire pumps), protection can trigger an alarm instead of disconnecting the circuit.  

2. **Overload Protection (430.225(B))**  
   - **Thermal Protection:** Motors must use thermal protectors or external current-sensing devices.  
   - **Automatic Reset Limitation:** Overload devices cannot automatically reset unless restarting poses no hazard.  

3. **Motor Controller as Overload Device (430.39)**  
   - **Permitted Use:** A motor controller can serve as an overload device if it meets Table 430.37 requirements and operates in both starting/running modes (DC) or running mode (AC).  

4. **Control Circuit Transformers (430.72(C))**  
   - **Primary Protection:** Transformers <50 VA in motor controller enclosures need no separate protection.  
   - **Low-Current Transformers:** Primary current <2A allows 500% overcurrent protection.  

5. **Motor Control Centers (430.94)**  
   - **Overcurrent Protection:** Must comply with Article 240. Protection devices cannot ...

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 430.94, 310.16, 310.19, 430.37, 430.39, 110.14, 430.225, 430.72

**Response Time:** 19.4s

---

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**CEC Ref:** CEC 311.60(C), Tables 311.60(C)(67-86) | **NEC Ref:** N/A - CEC only tables

**Status:** PASS

**Agent Answer:**
## Medium Voltage Cable Tables in California (CEc_exception_search Results)

### **Key Exceptions Affecting Medium Voltage Cable Tables**
1. **Ampacity Selection Flexibility** (311.60(A)(2) Exception):
   - Allows using **higher ampacity** for portions of a circuit if the lower ampacity section is ≤ 10 ft (3.0 m) or 10% of total circuit length.
   - Example: A 50 ft circuit with 10 ft of lower ampacity section is acceptable.

2. **Expanded Use of Type MV Cables** (311.32):
   - Permits Type MV cables in **cable trays, raceways, and exposed runs** under specific conditions (e.g., 392.80 for trays).
   - Requires compliance with **392.22(C)** for cable tray installations.

3. **Nonshielded Cable Exceptions** (311.44):
   - Allows nonshielded cables up to **2400V** in industrial settings with qualified personnel.
   - Requires **ozone-resistant insulation** and grounding for nonshielded cables above 2000V.

4. **Direct-Burial Exceptions** (311.36):
   - Permits nonshielded multiconductor cables up to **2400V** with metallic sheaths or armor for direct burial.
   - Airfield lighting cables up to **5000V** may be nonshielded per FAA guidelines.

---

### **Impact on CEC Tables**
- **Table 311.60(C)(67)–(86)** include:
  - **Burial depth derating** (6% per 300 mm depth increase).
  - **Shield grounding adjustments** (single-point vs. multi-point).
  - **Ambient temperature corrections** using specific equations.
- **Section 392.80** adds:
  - **Cable tray fill limits** (e.g., 90% tray width for 4/0 AWG+ cables).
  - **Spacing requirements** (1× cable diameter between conductors).

---

### **NEC Comparison**
- **NEC 2023** lacks:
  - **California-specific derating formulas** (e.g., burial depth adjustments).
  - **Detailed cable tray fill rules** (e.g., 4500 mm² fill limits for 150 mm trays).
  - **Nonshielded cable exceptions** for industrial settings (311.44).
- **NEC 311.60** provides general medium voltage tables but does not address:
  - **Isolated conduit/undergroun...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 392.22, 311.44, 311.36, 311.32, 311.60, 392.80

**Response Time:** 14.7s

---


## CEC Delta Tables

### cec-011: conductor_ampacity

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California Amendment]

**CEC Ref:** CEC Table 310.16 | **NEC Ref:** NEC Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

**California Requirement (CEC 2022):**
The ampacity of **4/0 AWG copper conductor at 75°C** is **230 amperes** per CEC Table 310.16 under standard conditions (30°C ambient, ≤3 current-carrying conductors). 

**Critical Exceptions Checked:**
1. **Section 310.12** (Dwelling services/feeders):  
   - Allows reduced ampacity (83% of service rating) for dwelling units.  
   - **Does not apply here** unless this conductor is part of a dwelling service/feeder.

2. **Section 210.19(A)(1)** (Continuous loads):  
   - Requires conductors to be sized at 125% of continuous loads.  
   - If this 4/0 conductor serves continuous loads, the usable ampacity would be **230A × 0.8 = 184A**.

3. **Sections 310.15(B/C)** (Adjustment factors):  
   - Temperature corrections (Table 310.15[B][1]) and bundling derates (Table 310.15[C][1]) apply if ambient temperature >30°C or >3 conductors.  
   - **No adjustments needed** for the given conditions.

**Conclusion:**  
The 230A value is valid for general use under standard conditions. For dwelling services, continuous loads, or non-standard installations, additional adjustments/requirements apply.

---
## NEC 2023 Reference
NEC 2023 specifies the **same 230A ampacity** for 4/0 AWG copper at 75°C in Table 310.16. California's amendment here does not modify the base NEC value for this specific conductor size and temperature rating.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.16, 310.12, 210.19, 310.15

**Response Time:** 11.0s

---

### cec-012: grounding

**Question:** What size equipment grounding conductor is required for a 200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122 [California Amendment]

**CEC Ref:** CEC Table 250.122 | **NEC Ref:** NEC Table 250.122

**Status:** PASS

**Agent Answer:**
## Equipment Grounding Conductor Requirement (CEC 2022)  

For a **200A circuit** in California, the required equipment grounding conductor (EGC) sizes are:  

- **Copper**: **6 AWG**  
- **Aluminum/Copper-Clad Aluminum**: **4 AWG**  

This is specified in **CEC 2022 Table 250.122**, which includes a California amendment ([CEC]).  

---

### Exceptions Checked:  
1. **Section 250.121** (Grounding electrode conductor use): Does not apply here, as the question focuses on EGC sizing, not electrode conductor use.  
2. **Sections 356.60/352.60** (Separate EGC in conduit): Allow exceptions for DC circuits or separately run EGCs. Not applicable unless the installation meets these specific conditions.  
3. **Section 250.134** (Separately run EGCs): Permits separate EGCs for fixed equipment or DC circuits. No such conditions were specified in the question.  
4. **Section 250.54** (Auxiliary grounding electrodes): Permits additional electrodes but does not affect EGC sizing.  

No exceptions modify the standard sizing for a typical 200A circuit.  

---

## NEC 2023 Reference  
No difference in grounding conductor sizing for 200A circuits. NEC 2023 Table 250.122 also specifies 6 AWG copper or 4 AWG aluminum.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 250.54, 356.60, 250.134, 250.122, 352.60, 250.121

**Response Time:** 9.4s

---

### cec-013: grounding

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66 [California Amendment]

**CEC Ref:** CEC Table 250.66 | **NEC Ref:** NEC Table 250.66

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Size (CEC 2022)  

**California Requirement:**  
For a **3/0 AWG copper service conductor**, the minimum grounding electrode conductor (GEC) size is **4 AWG copper** per **CEC 2022 Table 250.66**. This applies to single-phase services where the largest ungrounded service-entrance conductor is in the **2/0–3/0 AWG** range.  

**Exceptions Checked:**  
1. **250.66(A)**: If connected to a **rod, pipe, or plate electrode** (e.g., 250.52(A)(5) or (A)(7)), the GEC can be reduced to **6 AWG copper** **if it does not extend to other electrode types** requiring larger conductors.  
2. **250.66(B)**: If connected to a **concrete-encased electrode** (250.52(A)(3)), the GEC can be reduced to **4 AWG copper** (same as the table value).  
3. **250.66(C)**: If connected to a **ground ring** (250.52(A)(4)), the GEC size matches the ground ring conductor.  

**Key Notes:**  
- The **standard size is 4 AWG copper** unless specific exceptions apply (e.g., rod/pipe/plate electrode with no other electrode connections).  
- California amendment ([delta] symbol) confirms this requirement aligns with NEC but emphasizes local enforcement.  

---
## NEC 2023 Reference  
NEC 2023 Table 250.66 also specifies **4 AWG copper** for 2/0–3/0 AWG service conductors. **No difference from NEC 2023** in this case.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 250.66, 250.52

**Response Time:** 9.0s

---

### cec-014: ampacity_adjustment

**Question:** What is the temperature correction factor for a 75C rated conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(B)(1)(1) | **NEC Ref:** NEC Table 310.15(B)(1)

**Status:** PASS

**Agent Answer:**
## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** in a **40°C ambient temperature** is:

**0.88** per CEC 2022 Table 310.15(B)(1)(1)

This factor reduces the conductor's ampacity to account for the elevated ambient temperature.

**Key Exceptions/Notes:**
- Exception 2 in CEC 310.15 emphasizes that corrected ampacity must not exceed termination temperature limits (per 110.14(C)). This ensures the adjusted ampacity doesn't exceed the temperature rating of equipment terminations.
- Engineering supervision is permitted for non-tabled conductor sizes (310.14(B)).

---
## NEC 2023 Reference
No difference from NEC 2023. Same temperature correction factor applies per NEC Table 310.15(B)(1)(1).

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.14, 310.14, 310.15

**Response Time:** 8.0s

---

### cec-015: ampacity_adjustment

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California Amendment]

**CEC Ref:** CEC Table 310.15(C)(1) | **NEC Ref:** NEC Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity Adjustment Factor (CEC 2022)

For **7-9 current-carrying conductors** in a raceway, the ampacity adjustment factor is **0.70** per **CEC 2022 Table 310.15(C)(1)**. This factor reduces the allowable ampacity of each conductor to account for heat buildup from multiple conductors in close proximity.

**Key Notes:**
- Applies to conductors rated 60°C, 75°C, or 90°C (depending on insulation type)
- Factor remains 0.70 regardless of conductor material (copper/aluminum)
- **No exceptions apply** to this requirement for 7-9 conductors in general raceway installations

**Exception Analysis:**
- Exception 310.15(C)(1)(d) allows 60% adjustment for >20 conductors in cable trays, but this does not apply to 7-9 conductors
- Exception 310.15(C)(1)(b) excludes short raceways (<24") from adjustment requirements, but this is a general case
- No other exceptions modify the 0.70 factor for 7-9 conductors in standard raceway applications

---
## NEC 2023 Reference
No difference from NEC 2023. The bundling adjustment factor for 7-9 conductors is also **0.70** per NEC Table 310.15(C)(1).

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 10.2s

---

### cec-016: working_space

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**CEC Ref:** CEC Table 110.26(A)(1) | **NEC Ref:** NEC Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Space Depth (CEC 2022)  
For a 480V panelboard under **Condition 3** (exposed live parts on both sides), the minimum working space depth is **1.2 meters (4 feet)** per **CEC 2022 Table 110.26(A)(1)**.  

### Exceptions Checked:  
1. **Exception No. 2** (110.26(A)(1)): Permits reduced height (less than 2.0m/6.5ft) for existing dwelling units with service equipment ≤ 200A.  
   - **Does not apply** here (no mention of existing dwelling or service equipment size).  
2. **Dead-Front Assemblies** (110.26(A)(1)(a)): Allows reduced space if equipment has no renewable parts on the back.  
   - **Not applicable** to general panelboards.  
3. **Low Voltage** (110.26(A)(1)(b)): Permits smaller spaces for ≤ 30V RMS.  
   - **Not applicable** (480V system).  

No exceptions override the 4-foot requirement for this scenario.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The working space depth for 480V under Condition 3 remains **4 feet** per NEC Table 110.26(A)(1).  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 8.7s

---

### cec-017: enclosure

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28 [California Amendment]

**CEC Ref:** CEC Table 110.28 | **NEC Ref:** NEC Table 110.28

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered (CEC 2022)

**Suitable Enclosures for Outdoor Use with Rain, Sleet, and Ice:**  
As previously identified, **Type 3S, 3SX, 3X, 4, 4X, 6, and 6P** enclosures are suitable per CEC 2022 Table 110.28.  

**Additional Requirements from Exceptions:**  
1. **Installation Compliance (110.26(E)(2)):**  
   - Outdoor enclosures must be **installed in identified enclosures** (e.g., marked for outdoor use).  
   - Provide **protection from accidental contact** by unauthorized personnel or vehicles.  
   - Ensure **no foreign systems** (piping, ducts) are located in the dedicated equipment space (1.8 m/6 ft height).  

2. **Working Clearance:**  
   - Maintain **working space clearance** per 110.26(A) around outdoor equipment.  

**No Exceptions Override Enclosure Types:**  
The exceptions do not modify the enclosure type requirements from Table 110.28 but add **installation and location-specific rules** that must be followed alongside the enclosure selection.  

---

## NEC 2023 Reference  
No difference from NEC 2023. Table 110.28 and exception requirements are identical between CEC 2022 and NEC 2023.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_table, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 110.26, 110.28

**Response Time:** 15.2s

---

### cec-018: lighting_load

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

**Expected:** 3.5 VA per square foot per CEC 2022 Table 220.12 [California Amendment]

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load for Office Buildings (CEC 2022)

**California Requirement (CEC 2022 Table 220.12):**  
- **Office buildings** require a general lighting load of **1.3 volt-amperes per square foot (14 VA/m²)**. This value includes the 125% continuous load multiplier from 210.20(A).  

**Exceptions Checked:**  
1. **Section 220.12(B)** allows alternative energy code calculations if:  
   - A power monitoring system is installed.  
   - Demand factors from 220.42 are not applied.  
   - The 125% continuous load multiplier is still required.  
   *This does not override the base 1.3 VA/ft² value but provides an alternative compliance path under specific conditions.*  

2. **Other exceptions** (230.2, 225.32) relate to service configurations and disconnect locations, which do not affect lighting load calculations.  

**No exceptions directly modify the 1.3 VA/ft² value for office buildings.**  

---
## NEC 2023 Reference  
No difference from NEC 2023. The general lighting load for office buildings remains **1.3 VA/ft²** in the national code as well.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 220.12, 225.32, 230.2, 210.20, 220.42

**Response Time:** 11.7s

---

### cec-019: flexible_cord

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1) [California Amendment]

**CEC Ref:** CEC Table 400.5(A)(1) | **NEC Ref:** NEC Table 400.5(A)(1)

**Status:** PASS

**Agent Answer:**
## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

**California Requirement (CEC 2022):**
Per **CEC 2022 Table 400.5(A)(1)**, the ampacity for 12 AWG flexible cord with **Column B thermoset** insulation is **25 amperes**. This applies to two-conductor cords where only two conductors are current-carrying (as noted in table footnotes).

**Key Code References:**
- **CEC 2022 Section 400.5(A):** Establishes ampacity tables for flexible cords.
- **Table 400.5(A)(1):** Specifies 25A for 12 AWG Column B thermoset.

**Exceptions/Adjustments:**
1. **Temperature Corrections:** If ambient temperature ≠ 30°C (86°F), apply correction factors from **Table 310.15(B)(1)** matching the cord's temperature rating.
2. **Conductor Count Adjustments:** For more than three current-carrying conductors, use **Table 400.5(A)(3)** adjustment factors.
3. **Prohibited Uses:** Flexible cords cannot substitute for fixed wiring (Section 400.12(1)) or be concealed in walls/ceilings (Section 400.12(2)).

**Exception Analysis:**
- **Section 400.5(A):** Confirms temperature correction and bundling adjustment requirements apply if conditions differ from standard (30°C, ≤3 conductors).
- **Section 400.12:** Restricts flexible cord use but does not affect ampacity values directly.

---
## NEC 2023 Reference
No difference from NEC 2023. The same ampacity of 25A for 12 AWG Column B thermoset flexible cord is specified in NEC Table 400.5(A)(1).

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_table, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 400.12, 310.15, 400.5

**Response Time:** 13.7s

---

### cec-020: fixture_wire

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California Amendment]

**CEC Ref:** CEC Table 402.3 | **NEC Ref:** NEC Table 402.3

**Status:** PASS

**Agent Answer:**
## Maximum Operating Temperature for Type SF-2 Silicone Insulated Fixture Wire (CEC 2022)

**California Requirement (CEC 2022):**  
The maximum operating temperature for Type SF-2 silicone insulated fixture wire is **105°C**, as specified in NEC 2023 Table 310.4(A) and adopted without amendment in California per CEC 2022 Section 310.14(A)(3). This rating reflects the inherent properties of silicone insulation and is not modified by California-specific exceptions.

**Exception Analysis:**  
- Searched **CEC 2022 Section 310.14** for exceptions related to Type SF-2 temperature ratings.  
- **No exceptions** were found that alter the 105°C rating for Type SF-2 conductors.  
- The exceptions in 310.14 address conductor types for specific locations (dry/damp/wet), sunlight resistance, and parallel conductor rules—none pertain to temperature ratings of silicone-insulated wire.

**Key Code References:**  
- CEC 2022 Section 310.14(A)(3): General temperature limitation rule  
- NEC 2023 Table 310.4(A): Type SF-2 rated for 105°C (no CEC amendment)  

---
## NEC 2023 Reference  
No difference from NEC 2023. Type SF-2 remains rated for 105°C in both codes.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.14, 310.4

**Response Time:** 10.8s

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
- Conductor: 8 AWG THWN copper (75°C rated)
- Number of CCCs: 7
- Ambient temperature: 40°C

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):
   8 AWG copper, 75°C column = **50 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   40°C ambient, 75°C conductor = **0.82 factor**

3. **Adjustment Factor** (CEC 2022 Table 310.15(C)(1)):
   7 current-carrying conductors = **0.70 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 50 × 0.82 × 0.70 = 28.7 amperes
   ```

**Final Answer: 28.7 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1). No exceptions to these derating requirements were found in the CEC 2022 text.

---
## NEC 2023 Reference
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.16, 310.15

**Response Time:** 11.1s

---

### cec-022: service_sizing

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG copper (per CEC Table 250.66 for 3/0 service conductors).

**CEC Ref:** CEC Tables 310.16, 250.122, 250.66 | **NEC Ref:** NEC Tables 310.16, 250.122, 250.66

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

### **1. Service Conductors (2/0 AWG Copper)**
- **Primary Rule:** CEC 2022 Table 310.12(A)  
- **Exceptions Checked:**  
  - **Parallel Conductors (310.12(G)):** Not applicable (single conductor used).  
  - **Temperature/Adjustment Factors:** No corrections needed (standard 75°C rating).  
  - **Corrosive Conditions (310.12(F)):** Not specified in scenario.  
- **California Amendment:** Table 310.12(A) explicitly modified for dwelling services.  

---

### **2. Equipment Grounding Conductor (6 AWG Copper)**
- **Primary Rule:** CEC 2022 Table 250.122  
- **Exceptions Checked:**  
  - **250.121(A):** EGC cannot serve as GEC unless installed per 250.6(A) (not applicable here).  
  - **250.134:** Separate EGC required (applies).  
- **California Amendment:** Table 250.122 modified for EGC sizing.  

---

### **3. Grounding Electrode Conductor (4 AWG Copper)**
- **Primary Rule:** CEC 2022 Table 250.66  
- **Exceptions Checked:**  
  - **250.54:** Auxiliary electrodes permitted but not required (not applicable).  
  - **250.121(B):** Building metal frame cannot be used as GEC (separate conductor required).  
- **California Amendment:** Table 250.66 modified for GEC sizing.  

---

## NEC 2023 Reference  
- **Service Conductors:** NEC Table 310.12(A) matches CEC.  
- **EGC/GEC:** NEC Tables 250.122 and 250.66 are identical to CEC in this case.  

✓ **Sources: CEC 2022 (California), NEC 2023 (comparison)**  
[California amendments apply to Tables 250.122 and 250.66.]

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 250.6, 310.12, 250.66, 250.54, 250.134, 250.122, 250.121

**Response Time:** 14.1s

---

### cec-023: commercial_load

**Question:** Calculate the general lighting load for a 5,000 square foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 3.5 VA per square foot. General lighting load = 5,000 sq ft x 3.5 VA/sq ft = 17,500 VA (17.5 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)  
**For a 5,000 sq ft office building:**  

1. **Unit Load from CEC Table 220.12:**  
   - Per CEC 2022 Table 220.12, **office buildings** require **3.5 volt-amperes per square foot (VA/ft²)**.  

2. **Base Load Calculation:**  
   $$
   5,000 \, \text{sq ft} \times 3.5 \, \text{VA/ft²} = 17,500 \, \text{VA}
   $$  

3. **Continuous Load Adjustment:**  
   - CEC 220.12 includes the **125% multiplier for continuous loads** in its unit load values (per 210.20(A)), so no additional adjustment is needed.  

**Final General Lighting Load:**  
**17,500 volt-amperes (VA)** or **17.5 kilovolt-amperes (kVA)**  

---

### Exception Analysis  
- **CEC 220.12(B) Energy Code Exception:**  
  Allows using energy code-specified unit loads **if** a power monitoring system is installed with alarms/load-reduction capabilities. Since the question provides **no evidence of energy code compliance** or monitoring systems, this exception **does not apply**.  

- Other exceptions (422.23, 424.10, 220.85) relate to appliances, heating equipment, or multi-unit dwellings and are **not relevant** to this office lighting calculation.  

---

## NEC 2023 Reference  
No difference from NEC 2023. The unit load for office buildings is also **3.5 VA/ft²** per NEC Table 220.12.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 220.12, 422.23, 220.85, 210.20, 424.10

**Response Time:** 15.9s

---

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**CEC Ref:** CEC Table 430.72(B) | **NEC Ref:** N/A - CEC only table

**Status:** PASS

**Agent Answer:**
## Maximum Overcurrent Protection for 16 AWG Copper Motor Control Circuit Conductors (CEC 2022)

**California Requirement (CEC 2022):**  
For motor control circuits using **16 AWG copper conductors** that extend beyond the enclosure, the overcurrent protection is governed by **CEC 2022 Section 430.72(B)** and **CEC 2022 Table 240.4(D)**:

1. **Motor Control Circuit Exception (Section 430.72(B)):**  
   Conductors in motor control circuits are permitted to be protected by the motor's **overload protective device**. If the 16 AWG conductors are connected **on the load side of a motor overload device**, **no separate overcurrent protection is required** for the conductors. This aligns with the exception in Section 460.8(B) for capacitors connected to motor overload devices.

2. **General Overcurrent Protection (Section 650.8):**  
   If the conductors are not protected by the motor's overload device, their overcurrent protection must not exceed their ampacity. While 16 AWG is not explicitly listed in Table 240.4(D), **Section 650.8** specifies that 20–28 AWG conductors require protection up to **6 amperes**. By extension, 16 AWG conductors in control circuits should also be protected at **6 amperes** to comply with California's amendments.

3. **Cross-Reference to Motor Control Centers (Section 430.94):**  
   Motor control centers must have overcurrent protection not exceeding the rating of the common power bus. This reinforces that motor control circuits rely on the main overcurrent device for protection.

**Final Answer:**  
- If the 16 AWG conductors are on the **load side of a motor overload device**, **no separate overcurrent protection is required** (per CEC 430.72(B)).  
- If not protected by the motor's overload device, the maximum overcurrent protection is **6 amperes** (based on CEC 650.8 for small conductors).

---

## NEC 2023 Reference  
NEC 2023 aligns with this requirement, specifying that motor control circuit conductors are protected by the motor's ov...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 460.8, 240.4, 430.94, 650.8, 430.72

**Response Time:** 15.0s

---

### cec-025: dwelling_load

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA (7.2 kVA).

**CEC Ref:** CEC Table 220.12 | **NEC Ref:** NEC Table 220.12

**Status:** PASS

**Agent Answer:**
## General Lighting Load Calculation (CEC 2022)

**California Requirement (CEC 2022 Section 220.14(J)):**
For dwelling units, the minimum general lighting and receptacle load is calculated at **3 volt-amperes per square foot (33 VA/m²)** of floor area. This includes all general-use receptacles and lighting outlets per 210.11(C)(1) and (C)(2).

**Calculation:**
- Floor area = 2,400 ft²  
- Load = 3 VA/ft² × 2,400 ft² = **7,200 volt-amperes (VA)**  

**Exception Analysis:**  
No exceptions to Section 220.14(J) apply for this calculation. The cross-referenced sections (220.12, 220.52, etc.) address non-dwelling units, small-appliance circuits, or other load types—not the general lighting load for dwelling units.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The general lighting load for dwelling units is also calculated at **3 VA/ft²** per NEC 220.14(J).  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 220.12, 210.11, 220.14, 220.52

**Response Time:** 9.7s

---


## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**CEC Ref:** CEC 210.8(A) | **NEC Ref:** NEC 210.8(A)

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

### **California Electrical Code (CEC 2022) Key Exceptions**
1. **No Exceptions for Countertop Receptacles**:  
   CEC 210.8(A)(6) explicitly requires GFCI protection for **all** kitchen countertop receptacles. Exceptions like those for "listed combination devices" (e.g., integrated appliances) **do not apply** to countertop receptacles in kitchens.  

2. **Limited Exceptions in Related Sections**:  
   - **210.8(A)(5)**: Allows exceptions for fire alarm systems in basements, but this does not apply to kitchens.  
   - **210.52(C)(1) Exception**: Exempts receptacles directly behind ranges or sinks, but **only for wall-line spacing**, not GFCI requirements.  

3. **Strict Receptacle-Level GFCI**:  
   CEC mandates **individual receptacles** must have GFCI protection (no circuit-level exceptions for kitchens).  

---

### **NEC 2023 Exceptions**
1. **Permits Listed Combination Devices**:  
   NEC 210.8(A)(6) allows exceptions for **listed combination devices** (e.g., countertop receptacles integrated into appliances like microwaves).  

2. **Circuit-Level GFCI Protection**:  
   NEC permits GFCI protection at the **circuit level** (e.g., a GFCI breaker) instead of individual receptacles.  

3. **Flexibility in Spacing**:  
   NEC uses a **1.7 m² (18 ft²)** rule for countertop receptacles, which allows fewer GFCI-protected outlets compared to CEC’s 24-inch wall-line spacing.  

---

### **Final Determination**
**CEC 2022 is more restrictive** than NEC 2023 for kitchen GFCI requirements:  
- **No exceptions** for countertop receptacles in CEC.  
- **Stricter spacing rules** (24-inch wall-line vs. 1.7 m² per receptacle).  
- **Receptacle-level GFCI required**, while NEC allows circuit-level protection.  

**Conclusion**: California’s CEC enforces broader and stricter GFCI requirements for kitchens, with no exceptions for countertop receptacles.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 210.8, 210.52

**Response Time:** 16.0s

---

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022 and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2 requires reserved panelboard spaces for heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers, and EV charging equipment. NEC 2023 has NO such requirement. This is a significant California-specific difference for building electrification.

**CEC Ref:** CEC 408.2 | **NEC Ref:** NEC 408 (no equivalent requirement)

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements Comparison (CEC 2022 vs NEC 2023) - Final Answer

### **California Electrical Code (CEC 2022) Requirements**
1. **Reserved Circuit Breaker Spaces**  
   - **Section 408.2(A)**: Single-family dwellings must have **dedicated circuit breaker spaces** for:  
     - Heat pump water heaters  
     - Heat pump space heaters  
     - Electric cooktops  
     - Electric clothes dryers  
   - **California-Specific Amendment** [CEC]: This requirement is added by California Energy Code Section 150.0 and does not exist in NEC 2023.  

2. **Wire-Bending Space Sizing**  
   - **Section 408.55**:  
     - **Top/Bottom Bending Space**: Sized per Table 312.6(B) for the largest conductor.  
     - **Exceptions**:  
       - For panelboards rated **≤225A with ≤42 overcurrent devices**, top/bottom space can use Table 312.6(A).  
       - If side space uses Table 312.6(B), top/bottom can use Table 312.6(A).  
       - Single 90° bends allow Table 312.6(A) sizing.  
       - Unused spaces can use Table 312.6(A).  

3. **Panelboard Rating**  
   - **Section 408.30**: Minimum rating must match the calculated feeder capacity per Article 220.  

---

### **NEC 2023 Comparison**
1. **Reserved Circuit Breaker Spaces**  
   - **NEC 2023 does not require** pre-wiring for future appliances like heat pump water heaters or electric cooktops.  
   - California’s requirement in **408.2(A)** is a **local amendment** not found in the national code.  

2. **Wire-Bending Space Sizing**  
   - **NEC 2023 Section 312.6**:  
     - Similar to CEC 408.55, but **exceptions are less flexible**:  
       - No exception for panelboards with ≤42 devices.  
       - No exception for single 90° bends.  
       - Exceptions apply only to specific panelboard designs (not general).  

3. **Panelboard Rating**  
   - **NEC 2023 Section 408.30**: Matches CEC 2022—minimum rating must align with feeder calculations.  

---

### **Key Exceptions Checked**
- **Section 408.36 (Overcurrent Prot...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 408.36, 408.55, 408.2, 408.30, 312.6, 408.38, 150.0

**Response Time:** 15.3s

---

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging infrastructure in new construction, requiring dedicated circuits, conduit, and panel capacity. NEC 2023 Article 625 only provides installation rules for EV charging equipment but does not mandate installation. California leads with proactive requireme...

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625

**Status:** PASS

**Agent Answer:**
## Updated Analysis with Exceptions

### **Exceptions to CEC 625.40 (EV Branch Circuit Requirements)**

#### **Exception 625.46: Loss of Primary Power**
- **Requirement**: Systems must prevent backfeeding into premises wiring when utility power is lost, unless compliant with **625.48** (interactive systems).  
- **Impact**: This exception adds a safety layer for grid-tied EV systems, ensuring no unintended energy flow during outages.  
- **NEC Comparison**: NEC 705.12 covers similar anti-backfeed requirements for distributed energy resources but does not specifically address EV systems.  

#### **Exception 625.47: Multiple Feeders/Branch Circuits**
- **Permit**: Allows multiple feeders/branch circuits to supply EV equipment **if the equipment is identified for the application**.  
- **Example**: A commercial EV charging station with multiple Level 2 chargers could use this exception to share a common feeder.  
- **NEC Comparison**: NEC 210.19(A) allows shared circuits for EVSE if rated for the load, but CEC 625.47 adds equipment-specific identification requirements.  

---

### **Revised CEC vs NEC Summary**

| **Aspect**               | **CEC 2022**                                                                 | **NEC 2023**                          |  
|--------------------------|------------------------------------------------------------------------------|---------------------------------------|  
| **Branch Circuit**        | Dedicated circuit (625.40) **except** for 625.47 (multiple circuits allowed if equipment is identified). | Permits shared circuits (210.23).    |  
| **Backfeeding Prevention** | Mandatory via 625.46.                                                       | Addressed in 705.12 (general DER).   |  
| **Ventilation**           | Required for indoor charging (625.52).                                     | No specific requirements.              |  
| **GFCI Protection**       | All EV receptacles (625.54).                                     ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 10 found
- 210.23, 625.40, 625.54, 625.46, 210.8, 625.52, 625.48, 210.19, 625.47, 705.12

**Response Time:** 18.9s

---

### cec-029: afci

**Question:** Compare the AFCI protection requirements between CEC 2022 and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for 120V, 15/20A branch circuits in kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and similar rooms. The requirements are largely similar between the two codes.

**CEC Ref:** CEC 210.12 | **NEC Ref:** NEC 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirements Comparison: CEC 2022 vs NEC 2023 for Dwelling Units

---

### **CEC 2022 Requirements (California Electrical Code)**
**Section 210.12(A)** mandates AFCI protection for **15- and 20-ampere branch circuits** in dwelling units for outlets in:
- Kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, and similar spaces.

**Permitted AFCI Installation Methods**:
1. **Combination-type AFCI** at the circuit origin.
2. **Branch/feeder-type AFCI** + outlet branch-circuit AFCI at first outlet.
3. **Supplemental arc protection circuit breaker** + outlet AFCI (with conductor length limits).
4. **Outlet branch-circuit AFCI** at first outlet (with wiring continuity requirements).
5. **Outlet AFCI** permitted with metal raceway/conduit between overcurrent device and first outlet.
6. **Outlet AFCI** allowed if wiring is concrete-encased.

**Exceptions**:
- **Fire alarm circuits**: No AFCI required if installed per 760.41(B)/760.121(B) and in metal raceway.
- **Short extensions**: No AFCI required for extensions ≤ 1.8 m (6 ft) without additional outlets (excluding splicing devices).

---

### **NEC 2023 Requirements (National Electrical Code)**
**NEC 210.12(A)** aligns closely but with **key differences**:
- **Coverage**: Same 15/20A circuits in kitchens, family rooms, bedrooms, etc., but **NEC excludes laundry areas** from mandatory AFCI protection (covered in CEC 210.12(A)).
- **Permitted Methods**: NEC allows:
  - **Combination-type AFCI** at the circuit origin (same as CEC).
  - **Outlet branch-circuit AFCI** at the first outlet (similar to CEC methods 4–6 but without CEC’s concrete/encased wiring exception).
- **No Exception for Short Extensions**: NEC does not include the CEC’s 1.8 m (6 ft) extension exception.
- **No Specific Wiring Requirements**: NEC does not specify conductor length limits or metal raceway exceptions for alternative AFCI installations (unlike CEC 210.12(A)(3...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 760.121, 210.12, 760.41

**Response Time:** 14.1s

---

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Expected:** California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements (rapid shutdown, arc-fault protection, grounding). The key difference is California requires solar installation; NEC only covers how to install it safely.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690

**Status:** PASS

**Agent Answer:**
## Final Answer: California (CEC 2022) vs NEC 2023 Solar PV Requirements  

### **Key CEC 2022 Provisions**  
1. **Voltage Limits**  
   - **CEC 690.7**:  
     - Max DC voltage: **1000V** for building-mounted systems, **600V** for residential (1-2 family).  
     - Outdoor systems (non-building) with listed equipment ≤1500V are exempt from Parts II/III of Article 490.  
   - **NEC 2023**: General 1000V DC limit with no residential voltage restriction.  

2. **Arc-Fault Protection**  
   - **CEC 690.11**:  
     - Requires listed PV arc-fault circuit interrupters for DC circuits ≥80V.  
     - **Exception**: Non-building systems in metallic raceways/cables or underground are exempt.  
   - **NEC**: No exception for non-building systems.  

3. **Voltage Calculations**  
   - **CEC 690.7(A)**: Mandates temperature-corrected open-circuit voltage using **Table 690.7(A)** for crystalline modules.  

4. **Grounding**  
   - **CEC 690.43-47**:  
     - Bonding jumpers required between metallic support structures.  
     - Permits building metal frames as grounding electrodes for PV arrays.  

---

### **Exceptions & Cross-References**  
- **690.7 Exception**: Outdoor systems ≤1500V may bypass overcurrent protection rules in Article 490 (Section 690.9).  
- **Overcurrent Protection**:  
  - **690.9(A)(1)**: No overcurrent protection required if conductor ampacity ≥ max circuit current and source currents ≤ device rating.  
  - **690.9(A)(4)**: Outdoor conductors in metallic raceways may be protected at one end (e.g., near inverter).  

---

### **California-Specific Amendments [CEC]**  
- **Voltage Restrictions**: Stricter residential limit (600V vs. NEC’s 1000V).  
- **Arc-Fault Exemptions**: Unique exception for non-building systems in metallic raceways.  
- **Grounding Flexibility**: Permits use of building metal frames as grounding electrodes.  

---

### **Summary**  
California’s CEC 2022 adds **voltage restrictions**, **arc-fault exemptions for outdoor systems**, and...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 690.9, 690.11, 690.7, 690.43

**Response Time:** 15.9s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 30/30
- **Success Rate**: 100.0%
- **Average Response Time**: 13.0s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

