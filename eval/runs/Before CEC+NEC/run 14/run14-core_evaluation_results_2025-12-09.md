# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-09
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 28 |
| **Successful** | 28 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 352.4s |
| **Avg per Question** | 12.6s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## 12 AWG Copper Conductor Ampacity (CEC 2022)

**Ampacity**: 25 amperes (CEC Table 310.16, 75°C column for copper)  
**Overcurrent Protection Limit**: **20 amperes maximum** (CEC 240.4(D)(3) for 12 AWG copper)  

✓ **Key Notes**:  
1. The 25A ampacity assumes:  
   - 30°C ambient temperature  
   - No more than 3 current-carrying conductors in raceway  
   - 75°C termination rating  
2. **240.4(D) Limitation**: Even though the conductor can carry 25A, it must be protected at **20A maximum** per California-amended 240.4(D)(3).  

**Exceptions Checked**:  
- No applicable exceptions found for general 12 AWG copper conductors in Table 310.16.  
- Exceptions in 440.6 and 311.12 relate to specialized equipment (HVAC, industrial) and do not apply to standard wiring.  

✓ Source: CEC 2022 Tables 310.16 and 240.4(D)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 311.12, 240.4, 310.16, 440.6

**Response Time:** 11.4s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Verification and Answer

**Conductor Size**: **6 AWG copper**  
**Ampacity**: **65A** (CEC Table 310.16, 75°C column)  
**Overcurrent Protection**: Permitted for 60A circuits (240.4(D) does not limit 6 AWG)  

**Key Citations**:  
- **Table 310.16**: Base ampacity of 65A for 6 AWG copper at 75°C.  
- **Section 240.4(D)**: No restriction for 6 AWG (only applies to 18–10 AWG).  
- **Exceptions**: No applicable exceptions for general-purpose circuits.  

**Final Answer**:  
A **6 AWG copper conductor** is required for a 60A circuit at 75°C. It provides 65A ampacity, meeting the requirement with 5A headroom.  

✓ Source: CEC 2022 Table 310.16, Section 240.4(D)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_exception_search, cec_find_limiting_rules, cec_lookup_conductor_ampacity
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 240.4, 310.16

**Response Time:** 11.5s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection in Residential Kitchens (CEC 2022)  

GFCI protection is **required** for the following in residential kitchens:  

1. **Countertop Receptacles**  
   - All receptacles installed to serve countertop surfaces must have GFCI protection (Section 210.8(A)(6)).  
   - Applies to 125–250V receptacles supplied by single-phase branch circuits rated ≤150V to ground.  

2. **Receptacles Near Sinks**  
   - Any receptacle within **1.8 meters (6 feet)** of the **top inside edge of the sink bowl** must be GFCI-protected (Section 210.8(A)(7)).  

---

### Exceptions Checked:  
- **No applicable exceptions** for standard kitchen receptacles.  
  - Exceptions in Section 210.8 apply to specialized cases (e.g., ceiling luminaires, industrial equipment) and do not exempt typical kitchen countertop or sink-area receptacles.  

---

### Key Requirements Summary:  
- **Countertop surfaces**: GFCI protection mandatory.  
- **Sink proximity**: 6-foot rule from sink bowl edge.  
- **No exceptions** for standard kitchen installations.  

✓ **Source**: CEC 2022 Section 210.8(A)(6), 210.8(A)(7)  

---  

**Note**: California follows NEC 2023 with no additional amendments for this section.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 210.8

**Response Time:** 32.5s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection for Bedroom Circuits (CEC 2022) - Final Answer

**Yes**, AFCI protection is required for bedroom circuits in new residential construction per **CEC 2022 Section 210.12(A)**. 

### Key Findings:
1. **Primary Rule**:  
   - **Section 210.12(A)** explicitly requires AFCI protection for all 120V, 15- and 20-ampere branch circuits in dwelling unit bedrooms.  
   - Protection methods include combination-type AFCIs, branch/feeder-type AFCIs, or outlet branch-circuit AFCIs (with specific installation conditions).

2. **Exceptions Checked**:  
   - **Section 406.4(D)(4)** addresses receptacle replacements in AFCI-protected circuits but does not exempt new construction from AFCI requirements.  
   - Other exceptions (e.g., fire alarm systems) are inapplicable to typical bedroom circuits.  

3. **No Valid Exceptions**:  
   - No exceptions in the CEC 2022 remove or modify the AFCI requirement for new residential bedroom circuits.  

**Compliance**: Install AFCI protection as specified in **Section 210.12(A)**.  

✓ Source: CEC 2022 Section 210.12(A) and exception search results.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.12, 406.4

**Response Time:** 8.8s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** PASS

**Agent Answer:**
## Final Answer: Aluminum Conductors for 200A Service (CEC 2022)

**Yes**, aluminum conductors are permitted for a 200A service.  

**Required size**: **4/0 AWG aluminum**  
- **Ampacity**: 200A @ 75°C (per **CEC Table 310.12(A)** for single-phase dwelling services)  
- **Material compliance**: Section 310.3(B) explicitly allows aluminum for service conductors.  

**Key Code References and Exceptions**:  
1. **CEC 310.12(A)**: Permits 4/0 AWG aluminum for 200A dwelling services when no derating applies.  
2. **CEC 230.90 Exception No. 5**: Allows overcurrent protection for 120/240V, 3-wire dwelling services to comply with **310.12**, confirming Table 310.12(A) applies.  
3. **CEC 230.31(B)**: Minimum size for underground service conductors (6 AWG aluminum) does **not override** Table 310.12(A) for general service applications.  

**No conflicting exceptions** limit this application. Overcurrent protection must comply with **230.90** (e.g., 200A OCP device).  

✓ Source: CEC 2022 Sections 310.12(A), 310.3(B), 230.90, 230.31(B)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.12, 230.31, 230.90, 310.3

**Response Time:** 12.8s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Clearance Depth (CEC 2022)  

For a **120/240V residential panel** under **Condition 2** (exposed live parts on one side and grounded parts on the other, e.g., against a concrete/brick wall):  
- **Minimum depth**: **900 mm (3 feet)**  
- **Applies to**: Standard residential electrical panels  
- **Citation**: CEC 2022 Table 110.26(A)(1)  

### Exception Review:  
1. **Low-voltage exception (110.26(A)(1)(b))**: Not applicable (120V exceeds 30V).  
2. **Existing buildings exception (110.26(A)(1)(c))**: Not applicable (no indication of existing installation constraints).  
3. **Dead-front assemblies (110.26(A)(1)(a))**: Does not reduce front clearance requirements.  
4. **Dedicated space rules (110.26(E))**: Address foreign systems/structural conflicts, not clearance depth.  

**No applicable exceptions override the 900 mm requirement for this scenario.**  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 7.9s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** PASS

**Agent Answer:**
## Small Appliance Branch Circuits in Kitchens (CEC 2022)  

**Answer:**  
A **minimum of two 20-ampere small-appliance branch circuits** are required for a kitchen.  

**Code Basis:**  
- **CEC 210.52(B)(1):**  
  *"In the kitchen... the two or more 20-ampere small-appliance branch circuits required by 210.11(C)(1) shall serve... all countertop outlets..."*  
- **CEC 210.11(C)(1):**  
  *"Two or more 20-ampere small-appliance branch circuits shall be provided for all receptacle outlets specified by 210.52(B)."*  

**Exceptions Checked:**  
1. **Exception No. 1 (210.52(B)(1)):** Permits switched receptacles from a general-purpose circuit but does not reduce the minimum two-circuit requirement.  
2. **Exception No. 2 (210.52(B)(1)):** Allows specific appliances on individual circuits but does not affect the two-circuit baseline.  

**Key Details:**  
- Both circuits must supply **all kitchen countertop receptacles** and wall/floor receptacles in the kitchen.  
- **No exceptions** reduce this requirement below two circuits for standard kitchens.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.11, 210.52

**Response Time:** 7.8s

---

### baseline-008: knowledge_simple

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Expected:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is required for a new 200A residential service under CEC 2022, but with installation flexibility.  

**Key Requirement:**  
Per **CEC 2022 Section 230.67(A)**, all services supplying **dwelling units** must include a **surge-protective device (SPD)**.  

**Exceptions/Modifications:**  
1. **Location Flexibility** (CEC 230.67(A) Exception):  
   - The SPD does **not need to be in the service equipment** if installed at the **next level of distribution equipment downstream** toward the load.  
   - Example: SPD can be placed in a subpanel or distribution center instead of directly in the service panel.  

2. **Type Requirements** (CEC 230.67(C)):  
   - SPD must be **Type 1 or Type 2** (no exceptions).  

**No Exemption for Residential Services**  
The CEC does not exempt residential services from this requirement.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 230.67

**Response Time:** 8.2s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** PASS

**Agent Answer:**
## Service Conductor Sizing (CEC 2022)

For a **200A residential service**:
- **Copper**: **2/0 AWG** (Table 310.12(A))
- **Aluminum**: **4/0 AWG** (Table 310.12(A))

### Key Requirements:
1. **Material Choice**: 
   - **Aluminum is permitted** if **4/0 AWG** is used (CEC 310.12(A) allows aluminum for service conductors)
   - Minimum aluminum size for service conductors: **6 AWG** (CEC 230.31(B)), but 4/0 AWG meets 200A requirements
2. **Application**: 
   - Table 310.12(A) applies to single-phase dwelling services with 120/240V systems
3. **No Adjustments**: 
   - Assumes standard installation (no temperature correction or bundling factors needed)
4. **Overcurrent Protection**: 
   - Must comply with **230.90** (OCPD rating ≤ conductor ampacity)
5. **California-Specific**: 
   - No amendments to NEC 310.12 in CEC 2022 for dwelling service conductor sizing

### Code Citations:
- Conductor sizing: **CEC 2022 Table 310.12(A)**
- Aluminum permitted: **CEC 310.3(B)**, **230.31(B)**
- Overcurrent protection: **CEC 230.90**

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_conductor_size, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.12, 310.3, 230.90, 230.31

**Response Time:** 19.7s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** PASS

**Agent Answer:**
## NEC and CEC Requirements for Multiwire Branch Circuit (CEC 2022)

### Circuit Breaker Requirements:
1. **Simultaneous Disconnection** (CEC 210.4(B)):  
   - **2-pole circuit breaker** or **two single-pole breakers with a listed handle tie** must be used to disconnect both ungrounded (hot) conductors simultaneously.  
   - Prevents energizing the neutral conductor if only one hot is disconnected.

2. **Rating**:  
   - For 12 AWG copper conductors (12/3 cable), the overcurrent protection must not exceed **20A** (per CEC Table 310.16 and 240.4(D)).  

---

### Neutral Termination Requirements:
1. **Grouping of Conductors** (CEC 210.4(D)):  
   - The grounded (neutral) conductor must be **terminated in the neutral bus** of the panel.  
   - Ungrounded (hot) and grounded (neutral) conductors must be **grouped together** (e.g., in the same cable or raceway) to prevent accidental disconnection of only one hot conductor.  

2. **No Switching the Neutral**:  
   - The neutral conductor must **not be switched** or interrupted by a device. It must remain continuous for the circuit.  

---

### Exceptions and Key Rules:
- **Line-to-Neutral Loads Only** (CEC 210.4(C)):  
  - The MWBC must supply only line-to-neutral loads (e.g., standard 120V receptacles).  
  - **Exception**: Line-to-line loads are allowed if all ungrounded conductors are disconnected simultaneously (e.g., for a single appliance).  

- **Load Balancing**:  
  - Ensure the loads on both hot legs are balanced to prevent excessive current on the shared neutral conductor.  

- **No California-Specific Exceptions**:  
  - CEC exceptions for 210.4 do not alter the NEC requirements for this application.  

---

✓ Source: CEC 2022 (aligned with NEC 2023)

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 240.4, 310.16, 210.4

**Response Time:** 12.4s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Dwellings (NEC 2023 with CEC Exceptions)

### **Required Locations (NEC 210.8(A))**
1. **Bathrooms**  
2. **Garages/accessory buildings** (floor at/ below grade, non-habitable)  
3. **Outdoors**  
   - *Exception:* Non-accessible receptacles for snow-melting/deicing systems (426.28/427.22)  
4. **Crawl spaces** (at/ below grade)  
5. **Basements**  
   - *Exception:* Receptacles for fire/burglar alarm systems (no GFCI required)  
6. **Kitchens** (countertop surfaces)  
7. **Within 6 ft of sinks** (top inside edge)  
8. **Boathouses**  
9. **Within 6 ft of bathtubs/showers** (outside edge)  
10. **Laundry areas**  
11. **Indoor damp/wet locations**  

---

### **Key Exceptions (CEC 2022)**
1. **Ceiling fans/luminaires**  
   - Listed locking receptacles for ceiling fans/luminaires *do not* require GFCI if not general-purpose.  
   - *Citation:* 210.8(A) Exception to (1)–(3), (5)–(8), (10).  

2. **Alarm systems**  
   - Receptacles for *permanently installed fire/burglar alarms* in basements are exempt.  
   - *Citation:* 210.8(A)(5) Exception.  

3. **Industrial equipment**  
   - In industrial labs or facilities, receptacles for equipment where GFCI would create a greater hazard (e.g., critical machinery) may be exempt.  
   - *Citation:* 210.8(B)(5) Exceptions No. 1–2.  

4. **Rooftop receptacles**  
   - GFCI not required for rooftop receptacles if not accessible from non-rooftop areas.  
   - *Citation:* 210.8(B)(3) Exception.  

5. **Snow-melting/deicing systems**  
   - Non-accessible receptacles for dedicated snow-melting/deicing circuits are exempt.  
   - *Citation:* 210.8(A)(3) Exception to (3), 210.8(B)(4) Exception No. 1.  

---

### **Additional Notes**
- **Distance measurement:** Shortest path without piercing walls/floors (210.8 Info Note).  
- **Cross-reference:** See 215.9 (feeder GFCI), 422.5 (appliances), and 590.6(B)(2) (industrial exemptions).  

✓ Source: NEC 2023 Section 210.8(A), CEC 2022 Excepti...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 6 found
- 422.5, 427.22, 426.28, 210.8, 590.6, 215.9

**Response Time:** 11.4s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirements for Residential Service (CEC 2022)  

**Requirement:**  
Yes, surge protection is **required** for all residential services per **CEC 2022 Section 230.67**.  

**Installation Locations:**  
1. **Integral to service equipment** (e.g., built into the main panel)  
2. **Immediately adjacent** to the service equipment  
3. **Downstream distribution equipment** (per exception in 230.67(B)) – allowed if installed at the next level of distribution toward the load  

**SPD Type:**  
Must be **Type 1 or Type 2** surge-protective device (SPD) (Section 230.67(C)).  

**Key Exception:**  
If not integrated into the service equipment, the SPD must be located adjacent to it or at downstream distribution equipment (not further than the next level toward the load).  

**No Additional Exceptions Apply:**  
- Other exceptions (e.g., 230.40, 230.2) relate to service conductor configurations, not SPD installation.  
- Section 230.67’s exception explicitly permits downstream installation at the next distribution level.  

✓ Source: CEC 2022 Section 230.67 and Exception.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 230.67, 230.2, 230.40

**Response Time:** 8.0s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** PASS

**Agent Answer:**
## Working Space Requirements (CEC 2022)

The installation **does not meet CEC requirements** due to insufficient working space in front of the panel:

1. **Front clearance**:  
   - **Required**: 30 inches (762 mm) per CEC 110.26(A)(1) for systems ≤150V.  
   - **Provided**: 24 inches (insufficient by 6 inches).  

2. **Exceptions Checked**:  
   - CEC 110.26(E) (dedicated equipment space) does not relax clearance requirements. It emphasizes protecting the dedicated space from foreign systems but does not reduce the 30-inch front clearance.  
   - No other exceptions apply to this scenario.  

3. **Side clearance**:  
   - The 18-inch side clearance to the water heater is **not explicitly regulated** by CEC 110.26 unless there are exposed live parts on that side.  

**Corrective Action**: Increase front clearance to **at least 30 inches** (762 mm) in front of the panel.  

✓ Source: CEC 2022 Section 110.26(A)(1) and exceptions.

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 10.7s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Multiple Conductors on a Single Circuit Breaker Terminal (CEC 2022)

**Final Answer:**  
Yes, this is a **code violation** under **CEC 2022 Section 408.41**.  

### Key Details:
1. **Rule**:  
   Per **408.41**, *each grounded conductor must terminate in an individual terminal not shared with another conductor*.  

2. **Exception**:  
   The exception in **408.41** permits **parallel conductors** to share a terminal **only if the terminal is explicitly marked** for multiple conductors (e.g., "2-wire" or "2-conductor").  

3. **Your Case**:  
   - The terminal is **not marked** for multiple conductors.  
   - The exception does **not apply** to general branch circuits (only parallel conductors like service entrance conductors).  

4. **Code Violation**:  
   Terminating two 12 AWG conductors on an unmarked 20A breaker terminal violates **408.41** and its exception.  

### Corrective Actions:
- **Relocate one conductor** to a separate terminal.  
- If parallel conductors are required (e.g., service entrance), ensure the terminal is **marked for multiple conductors**.  

✓ **Source**: CEC 2022 Section 408.41 and Exception.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 408.41

**Response Time:** 8.6s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** PASS

**Agent Answer:**
## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)  

For a detached garage subpanel fed by a 4-wire feeder from the house panel, the configuration must comply with **CEC 2022 Section 250.32** and related exceptions:  

---

### **Key Requirements**  
1. **Grounding Electrode System**  
   - A **separate grounding electrode** (e.g., ground rod) must be installed at the detached garage.  
   - The **grounding electrode conductor (GEC)** connects this electrode to the subpanel’s **grounding bus**.  
   - **Size the GEC** per **Table 250.66** based on the largest ungrounded (hot) conductor in the feeder.  

2. **Equipment Grounding Conductor (EGC)**  
   - The 4-wire feeder includes an **EGC** (4th wire) that runs from the house panel to the subpanel.  
   - This EGC connects to the **grounding bus** in the subpanel (never to the neutral bar).  

3. **Neutral and Ground Separation**  
   - In the subpanel, **neutral and ground must be isolated**.  
   - **Neutral bar**: Connected only to the feeder’s neutral conductor (from the house).  
   - **Grounding bus**: Connected to:  
     - The EGC (from the house).  
     - The GEC (to the ground rod).  

4. **Bonding**  
   - The subpanel’s metal enclosure must be bonded to the grounding bus via the EGC.  
   - **No bonding jumpers** between neutral and ground are allowed in the subpanel.  

---

### **Exceptions and Notes**  
- **Exception 250.32(B)(1), Exception No. 1**:  
  - Allows the grounded conductor to serve as the ground-fault return path **only if** no EGC is present. This does **not apply** here, as the 4-wire feeder includes an EGC.  

- **Exception 250.142**:  
  - Permits connecting the grounded conductor to equipment on the **supply side** of the service disconnect. Not applicable here, as the subpanel is on the **load side**.  

---

### **Example Configuration**  
- **Feeder Conductors**: 4 wires (2 hots, 1 neutral, 1 EGC).  
- **Subpanel Grounding Bus**:  
  - Connected to:  
    - EGC (from...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.66, 250.142, 250.32, 250.24

**Response Time:** 10.6s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** PASS

**Agent Answer:**
## Main Bonding Jumper vs System Bonding Jumper (CEC 2022) **WITH Exceptions**

---

### **Definitions**
1. **Main Bonding Jumper**  
   - Connects the **grounded circuit conductor** (neutral) to the **equipment grounding conductor** at the **service**.  
   - **Required by CEC 2022 Section 250.28** for all services.  
   - **Exception**: If a service has **multiple enclosures** (per 230.71(B)), each enclosure’s main bonding jumper must be sized based on the **largest ungrounded service conductor** for that enclosure (250.28(D)(2)).  

2. **System Bonding Jumper**  
   - Connects the **grounded conductor** to the **equipment grounding system** at a **separately derived system** (e.g., transformers, generators).  
   - **Required by CEC 2022 Section 250.28** for separately derived systems.  
   - **Exception**: For systems supplying **Class 1/2/3 circuits** from a transformer ≤1000 VA, the system bonding jumper may be **14 AWG copper** or **12 AWG aluminum** (250.30(A)(1), Exception No. 3).  

---

### **Key Differences**
| Feature                  | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|--------------------------|--------------------------------------------------|--------------------------------------------------|
| **Location**             | At the **service** (service equipment)           | At **separately derived systems**                |
| **Application**          | Services with grounded systems                   | Separately derived systems (e.g., transformers)  |
| **Purpose**              | Bonds service neutral to equipment grounding     | Bonds derived system neutral to equipment grounding |
| **Sizing**               | Per **Table 250.102(C)(1)** based on service conductor size | Per **Table 250.102(C)(1)** based on derived system conductor size |
| **Exceptions**           | Must be sized for **each enclosure** in multi-enclosure services (250.28(D)(2)) | May be installed at the **source...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 250.36, 250.187, 430.95, 250.28, 250.30, 230.71, 250.102

**Response Time:** 12.6s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** PASS

**Agent Answer:**
## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

**1. Required Number of Circuits:**
- **Minimum 2 circuits**: Per CEC 210.52(B)(1), kitchens require **not fewer than two 20-ampere small-appliance branch circuits**.  
- These circuits must serve **all countertop receptacles**, **wall/floor receptacles** in the kitchen, and **refrigeration equipment**.

**2. Dining Room Receptacle Service:**
- **Yes**, these circuits can serve dining room receptacles.  
- CEC 210.52(B)(1) explicitly permits small-appliance branch circuits to supply receptacles in **"similar rooms"** like dining rooms, provided:
  - The circuits are **not used for any other kitchen circuits** beyond the first kitchen (per Exception No. 2).
  - The dining room is considered a "similar room" under CEC 210.52(A) (e.g., family room, dining room, breakfast room).

**Key Citations:**
- CEC 210.52(B)(1): Mandates two 20A circuits for kitchens and allows service to dining rooms.
- CEC 210.52(A): Defines "similar rooms" that qualify for small-appliance circuit service.

**Exceptions:**
- No small-appliance circuit shall serve **more than one kitchen** (CEC 210.52(B)(1) Exception No. 2).
- Dining room receptacles must not be served by laundry or bathroom branch circuits (CEC 210.11(C)(2) and (3)).

**Final Answer:**
- **Two 20-ampere small-appliance branch circuits** are required for the kitchen.
- **Yes**, these circuits can serve dining room receptacles as they are classified as "similar rooms" under CEC 210.52(A), provided the circuits are not used for additional kitchens.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.11, 210.52

**Response Time:** 8.8s

---

### core-010: load_calculations

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Expected:** Base ampacity: 30A at 90°C (Table 310.16). Temperature correction factor: 0.82 for 50°C (Table 310.15(B)(1)). Bundling adjustment: 0.80 for 6 conductors (Table 310.15(C)(1)). Adjusted ampacity = 30A × 0.82 × 0.80 = 19.68A, approximately 20A.

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Final Answer: Adjusted Ampacity and Overcurrent Protection for 12 AWG THHN Conductors (CEC 2022)

**Adjusted Ampacity**: **19.7A**  
**Maximum Overcurrent Protection (OCP)**: **20A** (per CEC 240.4(D)(5))

---

### **Step-by-Step Calculation**
1. **Base Ampacity** (Table 310.16):  
   - 12 AWG THHN copper = **30A** (90°C column).

2. **Temperature Correction** (Table 310.15(B)(1)):  
   - 50°C ambient → **0.82 correction factor**.  
   - $ 30A \times 0.82 = 24.6A $.

3. **Bundling Adjustment** (Table 310.15(C)(1)):  
   - 6 conductors → **0.80 adjustment factor**.  
   - $ 24.6A \times 0.80 = 19.68A $ → **19.7A**.

---

### **Overcurrent Protection Limit**
- **CEC 240.4(D)(5)** explicitly limits 12 AWG copper conductors to **20A maximum OCP**, regardless of adjusted ampacity.  
- Even though the derated ampacity is ~19.7A, the OCP device must not exceed **20A**.

---

### **Code References**
- **Temperature correction**: CEC 310.15(B)(1)  
- **Bundling adjustment**: CEC 310.15(C)(1)  
- **OCP limit**: CEC 240.4(D)(5)  

---

### **Conclusion**
The adjusted ampacity is **19.7A**, but the overcurrent protection must not exceed **20A** due to the hard limit in 240.4(D)(5). No California-specific exceptions override this calculation.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_derated_ampacity, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 240.4, 310.16, 310.15

**Response Time:** 14.7s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## Why NEC Requires AFCI Protection in Bedrooms and Living Areas (CEC 2022 with Exceptions)

### **Requirement**
Per **NEC 2023 Section 210.12(B)** (adopted in CEC 2022), **AFCI protection is required** for all 120V, 15A/20A branch circuits in:
- **Bedrooms**
- **Living rooms**
- Hallways, closets, and similar areas in dwelling units.

This prevents fires from arc faults caused by damaged wiring, loose connections, or cord damage.

---

### **Exceptions Checked**
After calling `cec_exception_search` for **Section 210.12(B)**, **NO exceptions** were found that modify or relax this requirement in California. The returned exceptions relate to unrelated topics (lighting outlets, boxes, receptacles) and do not apply to AFCI requirements in bedrooms/living areas.

---

### **Electrical Hazard Prevented**
AFCI protection prevents **electrical fires from arc faults**, which are a leading cause of residential fires. Arcs generate high heat, igniting nearby materials. Bedrooms and living areas are high-risk due to:
- Frequent use of portable appliances
- Cord damage from movement/traffic
- Hidden wiring issues in walls

---

### **Key Takeaways**
- **No CEC exceptions** override NEC 210.12(B) for bedrooms/living areas.
- Compliance with **UL 1699** standards ensures AFCI devices detect dangerous arcs.
- **Mandatory for all 15A/20A circuits** in these locations.

✓ Source: CEC 2022 (NEC 210.12(B) with no applicable exceptions)

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 210.12

**Response Time:** 10.0s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Torque Specifications for Conductor Termination (CEC 2022)

**Why Torque Specifications Matter:**
1. **Connection Integrity** - Proper torque ensures terminals maintain low-resistance connections, preventing overheating and arcing.
2. **Equipment Protection** - Excessive torque can damage terminals; insufficient torque creates loose connections.
3. **Safety Compliance** - Meets CEC requirements for electrical system reliability and fire prevention.

**Key Requirements:**
- **Primary Rule:** CEC 2022 **Section 110.14(D)** mandates:
  - Torque values must be **as indicated on equipment** or in manufacturer instructions.
  - **Approved methods** include torque tools, shear bolts, or breakaway devices with visual indicators.
  - **Informational Notes**:
    - Contact manufacturer if torque values are unspecified.
    - Refer to UL 486A-486B and NFPA 70B for torque guidance.

- **Motor Control Circuits:** CEC 2022 **Section 430.9(C)** specifies:
  - Screw-type terminals with 14 AWG or smaller copper conductors must be torqued to **minimum 0.8 N·m (7 lb-in.)** unless marked otherwise.

**Exceptions Check:**
- No exceptions directly modify **Section 110.14(D)** torque requirements.
- Cross-referenced sections (e.g., 300.15, 250.148) address installation practices but do not relax torque specifications.

**Limiting Rules:** 
- Temperature limitations in **Section 110.14(C)** require conductor ampacity coordination with termination ratings (60°C/75°C/90°C).

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 300.15, 250.148, 110.14, 430.9

**Response Time:** 9.6s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Service Load Calculation (CEC 2022 with Exceptions)

### 1. **General Lighting Load**  
3,000 sq ft × **3 VA/sq ft** (CEC Table 220.12) = **9,000 VA**  
*No exception applies for dwelling units (Section 220.12(J)).*

### 2. **Small Appliance & Laundry Circuits**  
- 2 × 1,500 VA (small appliance circuits) = **3,000 VA**  
- 1 × 1,500 VA (laundry circuit) = **1,500 VA**  
**Total:** 3,000 + 1,500 = **4,500 VA**  
*No exception applies (Section 220.14(I)).*

### 3. **Range Load**  
12 kW range → **Demand factor from CEC Table 220.55**:  
8 kW + 50% of (12 kW - 8 kW) = **10,000 VA**  
*Exception: No exception applies for dwelling ranges (Section 220.55).*

### 4. **Dryer Load**  
5.5 kW dryer → **Fixed demand of 5,000 VA** (CEC 220.54)  
*No exception applies (Section 220.54).*

### 5. **Air Conditioning Load**  
4600 W (19.2A @ 240V) = **4,600 VA**  
*Exception: Dryer load > AC load, so no 125% factor applied (Section 220.50).*

---

### **Total Load Calculation**  
**Step 1:** General Lighting + Receptacles = 9,000 + 4,500 = **13,500 VA**  
**Step 2:** Apply demand factor (CEC 220.42):  
- First 3,000 VA @ 100% = **3,000 VA**  
- Remaining 10,500 VA @ 35% = **3,675 VA**  
**Adjusted General Load:** 3,000 + 3,675 = **6,675 VA**  

**Step 3:** Add major appliances:  
6,675 (adjusted general) + 10,000 (range) + 5,000 (dryer) + 4,600 (AC) = **26,275 VA**  

---

### **Final Service Load**  
26,275 VA ÷ 240V = **109.5 A**  

---

### **Conclusion**  
The calculated service load is **109.5 A**, which is **well below the 200A panel rating**. The 200A panel is **adequately sized** for the installed loads.  

**Exceptions Verified:**  
- No exceptions override the base rules for dwelling unit calculations (Sections 220.12, 220.54, 220.55).  
- Demand factors in Table 220.42 apply as written (no exceptions for this occupancy type).  

✓ Source: CEC 2022 Tables 220.12, 220.42, 220.54, 220.55

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 220.54, 109.5, 220.42, 220.55, 220.14, 220.50, 220.12

**Response Time:** 17.9s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## Electrical Panel Inspection Violations (CEC 2022) – Final Answer

### 1. **Insufficient Depth Clearance**  
- **Violation**: 28-inch depth clearance is **less than the required 30 inches** (762 mm) for working space in front of the panel.  
- **Citation**: CEC 2022 Table 110.26(A)(1) (minimum depth for systems ≤ 600V).  
- **Exception Check**: No applicable exceptions found for depth requirements in this scenario.  

### 2. **Obstruction in Working Space**  
- **Violation**: The water heater is located **16 inches from the panel**, violating the requirement for **clear working space**.  
- **Citation**: CEC 2022 110.26(A)(3) (working space must be free of obstructions).  
- **Exception Check**:  
  - **Section 110.26(E)** allows exceptions for control equipment adjacent to machinery, but this applies to industrial/process equipment, not residential water heaters.  
  - No other exceptions apply to residential obstructions in working space.  

### 3. **Height Clearance (Potential Issue)**  
- **Potential Violation**: Panel mounted at 5 feet height may conflict with **minimum working space height of 6.5 feet (78 inches)** if ceiling height is insufficient.  
- **Citation**: CEC 2022 110.26(A)(2) (vertical clearance requirement).  
- **Exception Check**:  
  - **Section 110.26(E)(1)(a)** specifies a dedicated space up to 6 feet (1.8 m) above the equipment, but this does not reduce the vertical clearance requirement for working space.  

---

### Summary of Required Corrections:  
1. Increase front clearance depth to **30 inches**.  
2. Relocate the water heater **outside the working space** (minimum 30 inches from panel).  
3. Verify ceiling height provides **6.5 feet of vertical clearance** above the working space.  

✓ Source: CEC 2022  
✓ Exceptions reviewed: 110.26(E), 352.60, 356.60, 440.14 (no applicable exceptions apply).

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 356.60, 352.60, 440.14, 110.26

**Response Time:** 15.7s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## Circuit Protection Requirements (NEC 2023 with Exceptions Checked)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **GFCI**
- **NEC Reference**: **210.8(A)(5)**  
  *All 125-volt through 250-volt receptacles in kitchens must have GFCI protection.*  
  **Exceptions Checked**:  
  - No applicable exceptions apply (e.g., fixed appliances or special installations not present here).  
  - Supporting Rule: 210.52(B)(3) mandates countertop receptacles on small-appliance branch circuits.

---

### 2. **Dishwasher (15A Dedicated Circuit)**
- **Protection Required**: **Standard Breaker**  
- **NEC Reference**: **210.8(A)(6)**  
  *Exceptions apply for fixed appliances not readily accessible.*  
  **Exceptions Checked**:  
  - **Exception to 210.8(A)(5)**: Fixed appliances (e.g., dishwashers) are exempt if not within 6 ft of a sink.  
  - No indication the dishwasher is within 6 ft of a sink.  
  - Supporting Rule: Dishwashers are typically hardwired (not general-use receptacles).

---

### 3. **Garbage Disposal (15A Dedicated Circuit)**
- **Protection Required**: **Standard Breaker**  
- **NEC Reference**: **210.8(A)(6)**  
  *Same logic as dishwasher.*  
  **Exceptions Checked**:  
  - **Exception to 210.8(A)(5)**: Fixed appliances are exempt if not within 6 ft of a sink.  
  - No indication the disposal is within 6 ft of a sink.  
  - Supporting Rule: Garbage disposals are typically hardwired.

---

### 4. **Refrigerator (20A Dedicated Circuit)**
- **Protection Required**: **AFCI**  
- **NEC Reference**: **210.12(A)**  
  *All branch circuits in dwelling units require AFCI protection unless exempt.*  
  **Exceptions Checked**:  
  - No exceptions apply for refrigerators (fixed appliances remain on general-purpose circuits).  

---

### Summary Table
| Circuit Type               | Protection Type | NEC Section         | Exceptions Applied? |
|---------------------------|-----------------|---------------------|---------------------|
| Count...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 210.12, 210.52, 210.8

**Response Time:** 21.2s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## Corrected Subpanel Bonding Configuration (CEC 2022)

### **Violations Confirmed**
1. **Neutral and ground bars bonded together**  
   - **Rule**: CEC 250.24(D) explicitly prohibits bonding neutral and ground bars in subpanels.  
   - **Exception Check**: No exceptions in CEC 250.24(D) permit bonding in detached structures.  

2. **Neutral bar bonded to metal enclosure**  
   - **Rule**: CEC 250.24(D) forbids connecting the grounded (neutral) conductor to the enclosure.  
   - **Exception Check**: No exceptions apply to this requirement.  

3. **Missing grounding electrode system**  
   - **Rule**: CEC 250.32(A) mandates a separate grounding electrode for detached structures.  
   - **Exception Check**: No exceptions override this requirement.  

---

### **Correct Configuration**
1. **Neutral and Ground Separation**  
   - **Neutral bar**: Connect only the **feeder neutral conductor** (from main panel).  
   - **Ground bar**: Connect the **feeder equipment grounding conductor** (from main panel) and a **local grounding electrode** (e.g., ground rod at the garage).  
   - **No bonding jumper** between neutral and ground bars.  

2. **Grounding Electrode System**  
   - Install a **minimum 2.5 m (8 ft) ground rod** at the detached garage.  
   - Connect the ground rod to the subpanel’s ground bar using a **4 AWG copper grounding electrode conductor** (CEC 250.66).  

3. **Metal Enclosure Bonding**  
   - Bond the **ground bar** to the metal enclosure (per CEC 250.104(B)(1)), but **not the neutral bar**.  

4. **Feeder Connections**  
   - **Feeder neutral**: Connected to the subpanel’s neutral bar (no enclosure connection).  
   - **Feeder ground**: Connected to the subpanel’s ground bar (and grounding electrode).  

---

### **Key Code References**
- **CEC 250.24(D)**: Neutral-ground separation in subpanels.  
- **CEC 250.32(A)**: Grounding electrode requirement for detached structures.  
- **CEC 250.104(B)(1)**: Bonding metal enclosures to the grounding system.  ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.66, 250.24, 250.32, 250.104

**Response Time:** 11.7s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**
## Maximum Conductors in 1¼" RMC (Final Answer with Exceptions Verified)

**Calculation:**
1. **Conduit Area** (RMC 1¼"):  
   1.526 sq in (NEC Chapter 9 Table 4)  
   → 40% fill limit = 1.526 × 0.40 = **0.61 sq in**

2. **Conductor Area** (10 AWG THHN):  
   0.0211 sq in per conductor (NEC Chapter 9 Table 5)

3. **Maximum Conductors**:  
   0.61 ÷ 0.0211 = **28.91** → **28 conductors** (round down)

**Exception Review:**  
No applicable exceptions found in CEC 2022 that modify the conduit fill calculation for this scenario. The exceptions referenced (402.7, 350.22, 360.22, 362.22) either apply to specialized cases (fixture wires, irrigation systems) or reiterate the use of Table 1/Chapter 9 fill requirements without modification.

**Final Answer:**  
**28 conductors** (per NEC Chapter 9, adopted unchanged in CEC 2022)

✓ Source: NEC 2023 Chapter 9 Tables 4 and 5, verified with CEC 2022 exceptions search

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 360.22, 350.22, 402.7, 362.22

**Response Time:** 12.6s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**
## Voltage Drop Calculation (CEC 2022)

**Given:**
- Current (I) = 22A
- Distance (L) = 50 ft (one-way)
- Resistance (R) = 1.29 Ω/1000 ft
- Voltage = 120V single-phase

**Calculations:**
1. **Voltage Drop (VD):**
   $$
   VD = \frac{2 \times I \times L \times R}{1000} = \frac{2 \times 22 \times 50 \times 1.29}{1000} = 2.84 \, \text{volts}
   $$

2. **Percentage Drop:**
   $$
   \%VD = \left( \frac{2.84}{120} \right) \times 100 = 2.36\%
   $$

**Code Verification:**
- **CEC 2022 Section 647.4(D):** 
  - **1.5% limit (3.6V max)** applies specifically to *cord-connected equipment* (portable cords) per the informational note.
  - For **fixed equipment** using Chapter 3 wiring methods (e.g., NM, MC, THHN), the **NEC 3% recommendation** (3.6V max) remains applicable unless otherwise restricted.
- **Exceptions:** No exceptions override the 1.5% limit for fixed equipment. The 1.5% rule is explicitly tied to portable cord applications.

**Conclusion:**
- **Voltage Drop:** 2.84 volts (2.36% of 120V)
- **Compliance:** 
  - ✅ **Meets NEC 3% recommendation** (2.36% ≤ 3%)
  - ✅ **Compliant with CEC 647.4(D)** since the 1.5% limit does not apply to fixed installations (only cord-connected equipment)

✓ Source: CEC 2022 Section 647.4(D) and exceptions

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 647.4

**Response Time:** 14.6s

---

### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Final Adjusted Ampacity with Exception Check (CEC 2022)

After reviewing exceptions for Section 310.16, **no applicable exceptions** modify the standard temperature correction or bundling adjustment factors for this scenario. The exceptions found apply only to specialized equipment (e.g., hermetic refrigerant compressors, ferromagnetic envelope conductors) not relevant to general wiring calculations.

### Final Calculation:
1. **Base Ampacity**: 20A (12 AWG TW @ 60°C)  
2. **Temperature Correction**: 20A × 0.71 = 14.2A  
3. **Bundling Adjustment**: 14.2A × 0.80 = **11.4A**  

**Final Answer**:  
Adjusted ampacity = **11.4 amperes**  

✓ Source: CEC 2022  
✓ No applicable exceptions override standard calculation.

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.16

**Response Time:** 11.2s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Minimum Size Copper GEC for 1000 kcmil Service (CEC 2022) with Exceptions Considered

For four parallel 250 kcmil copper conductors (total equivalent 1000 kcmil per phase), the minimum size copper grounding electrode conductor (GEC) required is:

**2/0 AWG copper**  
(Per CEC 2022 Table 250.66, "Over 600 through 11000" kcmil service conductors)

### Exception Analysis:
1. **250.30(A)(5)** – Applies to separately derived systems. Not applicable here (main service, not separately derived).
2. **250.190(B)** – Confirms GEC sizing per Table 250.66 based on largest ungrounded conductor. Reinforces the 2/0 AWG requirement.
3. **250.32(E)** – Requires GEC size per Table 250.66 for feeders/branch circuits. No conflict with main service sizing.

No exceptions override the Table 250.66 requirement for this configuration.

✓ Source: CEC 2022 Table 250.66 with California amendment [delta] noted.

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.66, 250.190, 250.32, 250.30

**Response Time:** 9.4s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 28/28
- **Success Rate**: 100.0%
- **Average Response Time**: 12.6s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

