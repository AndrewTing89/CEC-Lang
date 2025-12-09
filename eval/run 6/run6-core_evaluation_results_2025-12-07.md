# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-07
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 28 |
| **Successful** | 28 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 444.1s |
| **Avg per Question** | 15.9s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer: 12 AWG Copper Conductor at 75°C (CEC 2022)

**Ampacity:**  
12 AWG copper at 75°C has an ampacity of **25 amperes** per CEC 2022 Table 310.16.  

**Overcurrent Protection Limitation:**  
Section 240.4(D)(5) explicitly limits overcurrent protection for 12 AWG copper conductors to **20 amperes maximum**, regardless of the conductor's ampacity. This is a critical safety requirement to prevent overheating and potential fire hazards.  

**Exception Analysis:**  
- No exceptions in CEC 2022 override this 20A limit for 12 AWG copper conductors.  
- Section 240.4(D) explicitly prohibits using overcurrent devices exceeding 20A for 12 AWG copper unless specifically permitted in 240.4(E) or (G) (not applicable here).  

**California-Specific Compliance:**  
- The [CEC amendment] in Table 310.16 directly references Section 240.4(D) for this limitation.  
- No deviations from NEC 2023 exist for this requirement.  

---
## NEC 2023 Reference  
NEC 2023 specifies identical requirements: 25A ampacity (Table 310.16) with 20A overcurrent protection limit per 240.4(D)(5).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 240.4, 310.16

**Response Time:** 11.6s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer (CEC 2022)

**Minimum copper conductor size for a 60A circuit at 75°C:**
- **6 AWG copper** (65A ampacity, meets 60A requirement)
- **Table reference:** CEC 2022 Table 310.16

**Key Code References:**
1. **Ampacity:** Per CEC 2022 Table 310.16, 6 AWG copper at 75°C has a 65A rating.
2. **Overcurrent Protection:** Section 240.4(D) limits 6 AWG copper to a maximum 65A overcurrent device.
3. **Exceptions Checked:** No applicable exceptions found for 310.16 in this scenario. The exceptions related to parallel conductors (310.16(G)) and dwelling services (310.12) do not apply to general branch circuits.

**NEC Comparison:**
- NEC 2023 Table 310.16 specifies identical ampacities for 6 AWG copper (65A at 75°C).
- No difference in conductor sizing requirements between CEC and NEC for this scenario.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 240.4, 310.12, 310.16

**Response Time:** 14.2s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

**California Requirement (CEc 2022):**  
Per **CEc 2022 Section 210.8(A)(6)**, **all 125-volt through 250-volt receptacles installed in kitchens to serve countertop surfaces** must have ground-fault circuit-interrupter (GFCI) protection.  

**Exceptions Checked:**  
After reviewing exceptions via `cec_exception_search(base_rule="210.8(A)(6)", context="kitchen countertop receptacles")`, **no exceptions apply** to override this requirement for kitchen countertop receptacles. The returned exceptions pertain to receptacle spacing, installation locations, and small-appliance circuits but do not modify the GFCI mandate for countertops.  

**NEC 2023 Reference:**  
No difference from NEC 2023. The National Electrical Code also requires GFCI protection for kitchen countertop receptacles per **NEC 210.8(A)(6)**.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 210.8

**Response Time:** 9.9s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection Requirement for Bedroom Circuits (CEC 2022)

**California Requirement (CEC 2022):**  
Yes, **AFCI protection is required** for all 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets in dwelling unit bedrooms per **CEC 2022 Section 210.12(A)**. This includes:

- **Protection Methods**:  
  - Combination-type AFCI at the circuit origin (most common method).  
  - Alternative methods (branch/feeder-type AFCI, supplemental protection systems) under specific conditions.  

- **Exceptions**:  
  1. **Fire alarm circuits** (760.41(B)/760.121(B)) are exempt.  
  2. **Circuit modifications/extensions** ≤6 ft without additional outlets (210.12(D)).  

**NEC 2023 Reference:**  
No difference from NEC 2023. Section 210.12(A) similarly requires AFCI protection for bedroom circuits in dwelling units.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 760.41, 760.121, 210.12

**Response Time:** 8.8s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** PASS

**Agent Answer:**
## California Electrical Code (CEC 2022) Answer

**Yes**, aluminum conductors are permitted for a 200A service in California.  

**Required Size:**  
**4/0 AWG aluminum** conductors are required for a 200A single-phase dwelling service.  

**Code Basis:**  
- **CEc 2022 Table 310.12(A)** (Single-Phase Dwelling Services and Feeders) specifies conductor sizes for services rated 100A through 400A.  
- **Section 310.12(A)** permits sizing service conductors at 83% of the service rating (200A × 0.83 = 166A required ampacity).  
- **Section 310.3(B)** explicitly allows aluminum conductors for this application.  

**Exceptions Checked:**  
- No exceptions to Section 310.12 apply to this scenario. The returned exceptions address installation conditions (e.g., parallel conductors, insulation types) but do not modify the conductor sizing requirements for a standard 200A dwelling service.  

**Key Conditions:**  
- Applies to **single-phase 120/240V or 120/208YV systems**.  
- Assumes **no temperature correction or bundling adjustments** are required (standard installation).  

---

## NEC 2023 Reference  
No difference from NEC 2023. The National Electrical Code also permits aluminum conductors for dwelling services and uses Table 310.12(A) for sizing. California’s CEC adopts this requirement without amendment.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_size, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.3, 310.12

**Response Time:** 12.4s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Depth of Working Clearance for a 120/240V Residential Panel (CEC 2022)  

**California Requirement (CEC 2022):**  
Per **CEC 2022 Table 110.26(A)(1)**, the minimum depth of working clearance in front of a residential electrical panel operating at 120/240V (≤ 600V) is **914 mm (36 inches)** under **Condition 2**.  

- **Condition 2** applies when:  
  - Exposed live parts are on one side of the working space.  
  - The opposite side has grounded parts (e.g., concrete, brick, or tile walls).  

**Exceptions Checked:**  
1. **Exception No. 2** (CEC 110.26(A)): Allows reduced height (not depth) for existing dwelling units with ≤ 200A panels. Does not affect depth requirement.  
2. **Condition 2** is explicitly covered in the table and remains unchanged.  
3. Other exceptions (e.g., dead-front assemblies, low-voltage systems) do not apply to standard residential panels.  

This requirement ensures safe access for maintenance and complies with **CEC 110.26(A)(1)**.  

---

## NEC 2023 Reference  
No difference from NEC 2023. The **NEC 2023 Table 110.26(A)(1)** specifies the same 36-inch (914 mm) depth for Condition 2 working space for similar residential panels.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 10.6s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
Per **CEC 2022 Section 210.52(B)(1)**, **at least two 20-ampere small-appliance branch circuits** are required to serve all receptacle outlets in a kitchen, including countertop outlets and refrigeration equipment.  

**Key Exceptions:**  
1. **Specific Appliance Circuits**: A receptacle for a specific appliance (e.g., built-in microwave) may be on an individual branch circuit (Exception No. 2).  
2. **Clock/Gas Appliance Receptacles**: Electric clocks or gas appliance receptacles may be on separate circuits (Exception No. 1).  

**Critical Limitations:**  
- These circuits **must supply only the receptacles specified** in 210.52(A) and (B).  
- **No other outlets** (e.g., laundry, bathroom) are permitted on these circuits.  

**NEC Compliance Note**: The requirement for two 20A small-appliance circuits in kitchens is identical in NEC 2023.  

---
## NEC 2023 Reference  
No difference from NEC 2023.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 210.52

**Response Time:** 28.8s

---

### baseline-008: knowledge_simple

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Expected:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirement for Residential Service (NEC 2023) - Final Answer

**NEC 2023 Requirement:**
Per **NEC 2023 Section 230.67(A)**, surge-protective devices (SPDs) are **required** for all services supplying dwelling units (residential occupancies). This applies directly to your 200A residential service.

**Key Details:**
- **Mandatory for:** Dwelling units, dormitory units, hotel/guest rooms, and nursing home patient sleeping rooms.
- **SPD Installation:** Must be provided at the service entrance.
- **No Exceptions Listed:** The requirement is absolute for dwelling units.

**Exception Analysis:**
- **Exceptions to 230.67:** The exceptions (e.g., 230.94, 230.67(B)) address SPD **location** or **installation methods**, not the **requirement itself**.
- **Example:** Exception No. 2 in 230.94 permits SPDs on the supply side of the service disconnect, but this does not negate the SPD requirement—it only specifies where SPDs may be installed.

**Conclusion:**
Yes, **surge protection is required** for a new 200A residential service under NEC 2023. Compliance involves installing an SPD at the service entrance per Section 230.67(A). No exceptions apply to dwelling units in this context.

✓ **Sources: NEC 2023 (primary)**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 2 found
- 230.94, 230.67

**Response Time:** 10.2s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** PASS

**Agent Answer:**
## Service Conductor Sizing (CEC 2022)  

For a **200A service upgrade** in a dwelling unit with the specified loads:  

**Required Conductor Size:**  
- **Aluminum:** 3/0 AWG (175A rating at 75°C)  
- **Copper:** 2/0 AWG (215A rating at 75°C)  

**Key Requirements:**  
1. **Table 310.12(A)** applies for single-phase dwelling services (CEC 2022 310.12(A)).  
2. **83% Rule:** Conductors must have ampacity ≥ 83% of service rating (200A × 0.83 = 166A).  
3. **Aluminum Permitted:** Yes, 3/0 AWG aluminum meets 175A rating (Table 310.12(A)).  
4. **Temperature Rating:** 75°C terminals assumed (common for modern panels).  

**Load Considerations:**  
- Electric range (12kW), dryer (5.5kW), and other loads are already accounted for in standard dwelling service calculations per CEC 220.54 and 220.84.  

**Why 3/0 Aluminum Works:**  
- 3/0 AWG aluminum at 75°C = 175A (Table 310.12(A)).  
- 175A ≥ 166A minimum required (83% of 200A).  
- Aluminum is code-compliant for service conductors when sized per Table 310.12(A).  

**Exceptions Checked:**  
- No exceptions to 310.12(A) apply here. The referenced exceptions (e.g., 230.31, 210.19) relate to different scenarios (e.g., underground conductors, branch circuits) and do not override the dwelling service sizing rules in 310.12(A).  

---
## NEC 2023 Reference  
No difference from NEC 2023. Same conductor sizing applies using NEC Table 310.12(A) for dwelling services.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_size, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 220.54, 210.19, 220.84, 310.12, 230.31

**Response Time:** 17.1s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** PASS

**Agent Answer:**
## California Electrical Code (CEC 2022) Requirements for Multiwire Branch Circuit Breaker and Neutral Termination

**1. Circuit Breaker Requirements:**
- **Simultaneous Disconnection:** Per CEC 210.4(B), all ungrounded conductors (hots) must be disconnected simultaneously using a **2-pole circuit breaker** to ensure both hots are tripped together. This prevents unequal loading and neutral overcurrent risks.
- **Breaker Rating:** For 12 AWG copper conductors (60°C rated), the maximum overcurrent protection is **20A** (CEC 240.4(D)). A 20A 2-pole breaker is required.

**2. Neutral Conductor Requirements:**
- **Sizing:** The neutral must be **12 AWG copper** (same size as hots) to carry unbalanced loads (CEC 210.4(D) with 200.4(B)).
- **Termination:** The neutral must terminate at the **grounded (neutral) bus bar** in the panel and **must not be switched** (CEC 200.4(B)). It cannot be connected to a switch or circuit breaker.
- **Load Type:** The MWBC must supply only **line-to-neutral loads** (e.g., kitchen receptacles). Line-to-line loads require exceptions (210.4(C)).

**3. Grounding Conductor Requirements:**
- The equipment grounding conductor (EGC) must be **12 AWG copper** (CEC Table 250.122 for 20A circuits).

**4. Exceptions Checked:**
- **Exception 210.4(C):** Allows line-to-line loads if all hots are opened simultaneously. Not applicable here (kitchen receptacles are line-to-neutral).
- **Exception 210.18:** Permits multioutlet circuits >50A in industrial settings. Not applicable for residential kitchens.

**5. Additional Notes:**
- Harmonic currents on neutrals are addressed in CEC 210.4(A) informational notes but not a concern for standard kitchen receptacles.
- The grounding conductor must be bonded to the neutral bar per CEC 250.24(B).

---

## NEC 2023 Reference
No difference from NEC 2023. Same requirements apply for multiwire branch circuits, breaker type, and neutral termination.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 6 found
- 210.18, 240.4, 250.24, 250.122, 200.4, 210.4

**Response Time:** 19.8s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Dwellings (NEC 2023)  

**Required Locations (NEC 2023 Section 210.8(A)):**  
GFCI protection is required for all 125–250V receptacles in these dwelling unit locations:  
1. **Bathrooms**  
2. **Garages** (and accessory buildings with floors at or below grade)  
3. **Outdoors**  
4. **Crawl spaces** at or below grade level  
5. **Kitchens**  
6. **Areas with sinks** (food/prep areas)  
7. **Within 1.8 m (6 ft)** of a sink’s top inside edge  
8. **Bathtubs/shower stalls** (within 1.8 m of the edge)  
9. **Boathouses**  
10. **Laundry areas**  
11. **Indoor damp/wet locations**  

---

**Exceptions (NEC 2023):**  
- **Exception No. 1:** Receptacles for dedicated equipment (e.g., snow-melting systems) if not readily accessible.  
- **Exception No. 2:** Premises security system receptacles.  
- **Exception No. 3:** Weight-supporting ceiling receptacles (WSCR) for ceiling fans/luminaires (if general-use receptacles are integral, GFCI still required).  
- **Exception No. 4:** Factory-installed, non-accessible receptacles in bathroom exhaust fans.  

---

## NEC 2023 Reference  
No material changes from prior editions. Requirements align with NEC 2020/2023 for residential GFCI protection.  

✓ **Sources: NEC 2023 (primary)**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 1 found
- 210.8

**Response Time:** 12.5s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirements for 200A Residential Service (CEC 2022)  

**Requirement:**  
Per **CEC 2022 Section 230.67**, surge protection **is required** for all services supplying dwelling units.  

**Installation Locations:**  
1. **Integral to service equipment** (e.g., within the main service panel).  
2. **Immediately adjacent** to the service equipment.  
3. **Downstream at next-level distribution equipment** (e.g., subpanels) if not installed in the service equipment (per **Exception to 230.67(B)**).  

**SPD Type:**  
Must be **Type 1 or Type 2** surge-protective devices (SPDs) as specified in **Section 230.67(C)**.  

**Exceptions:**  
- The SPD need not be in the service equipment if installed downstream toward the load at the next distribution level (Exception to 230.67(B)).  
- Other exceptions in Sections 230.94 and 240.21(D) relate to overcurrent devices and service conductors but do not override the surge protection requirement for dwelling units.  

---

## NEC 2023 Reference  
The NEC (NFPA 70) does **not explicitly require** surge protection for residential services in dwelling units. However, **NEC 230.67** (adopted in CEC) and **NEC Article 242** address overvoltage protection for systems over 1000V, which does not apply here. California’s CEC adds this requirement specifically for dwelling units.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 230.94, 240.21, 230.67

**Response Time:** 8.9s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** PASS

**Agent Answer:**
## CEC 2022 Working Space Requirements Analysis

**Given Scenario:**
- Panel installed in a closet
- 24 inches of front clearance
- Water heater 18 inches to the side

**Relevant CEC 2022 Requirements:**
1. **Minimum Depth (110.26(A)(1)):**
   - For **Condition 2** (exposed live parts on one side and grounded parts on the other), required depth = **30 inches (762 mm)**.
   - **Current clearance:** 24 inches → **Fails depth requirement**.

2. **Minimum Width (110.26(A)(2)):**
   - Width must be the equipment width or **30 inches**, whichever is greater.
   - If the panel is 24 inches wide, **required width = 30 inches**.
   - **Current clearance:** 24 inches → **Fails width requirement**.

3. **Side Clearance Impact:**
   - The water heater at 18 inches to the side reduces usable working space depth further, compounding the violation.

**Exceptions Checked:**
- **Exception 1 (110.26(A)(1)(c)):** Applies to existing buildings replacing equipment with written procedures. **Not applicable** (new installation).
- **Exception 2 (110.26(A)(1)(b)):** Permits smaller spaces for low-voltage equipment (≤30V). **Not applicable** (standard 120/240V panel).
- **Exception 3 (110.26(E)):** Allows control equipment near machinery. **Not applicable** (closet installation).

**Conclusion:**  
The installation **does not meet CEC 2022 requirements**. The working space must be at least **30 inches deep** and **30 inches wide** for a typical residential panel under Condition 2. The current 24-inch front clearance and proximity to the water heater violate these requirements.

---
## NEC 2023 Reference  
(No difference from NEC 2023 requirements)

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 16.5s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Final Code Violation Determination (CEC 2022)

**Conclusion:** This is a **code violation** under **CEC 110.3(B)** and **240.15**. The exceptions reviewed do not permit this installation:

1. **110.3(B) Equipment Listing Violation**:
   - Breaker terminals not marked for multiple conductors cannot legally accept two wires, regardless of ampacity.
   - No exception permits bypassing manufacturer instructions for terminal ratings.

2. **240.15 Overcurrent Protection Violation**:
   - While multiwire circuits are permitted (210.4), this refers to circuit configuration - it does not override terminal rating requirements.
   - The exceptions in 210.4 and 300.3 relate to conductor grouping, not terminal markings.

**Applicable Exceptions Analyzed**:
- 408.41 (grounded conductor terminations) - Not applicable to ungrounded conductors
- 210.4 (multiwire circuits) - Does not override terminal rating requirements
- 200.4 (neutral conductors) - Not applicable to ungrounded conductors
- 230.40 (service conductors) - Not applicable to branch circuits
- 300.3 (conductor installation) - Does not permit multiple conductors on single terminals

**NEC Comparison**:
NEC 2023 has identical requirements in **110.3(B)** and **240.15**. The National Electrical Code also prohibits this practice unless the breaker is specifically marked for multiple conductors.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 230.40, 110.3, 200.4, 210.4, 300.3, 240.15, 408.41

**Response Time:** 33.9s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** PASS

**Agent Answer:**
## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)  
**With Exception Analysis**  

---

### **California Requirement (CEC 2022)**  
For a detached garage subpanel fed by a 4-wire feeder:  

1. **Neutral and Ground Separation**  
   - **No bonding** between neutral and ground buses in the subpanel (per **250.24(A)(5)**).  
   - The grounded (neutral) conductor and equipment grounding conductor **must remain separate**.  

2. **Grounding Electrode at Garage**  
   - A **separate grounding electrode** (e.g., ground rod) must be installed at the garage.  
   - Size the grounding electrode conductor per **Table 250.66** based on the feeder’s largest ungrounded conductor.  

3. **Equipment Grounding Conductor**  
   - The fourth wire (equipment grounding conductor) from the house panel connects to the **grounding bus** in the subpanel.  

4. **Bonding the Subpanel Enclosure**  
   - The metal subpanel enclosure must be bonded to the equipment grounding conductor (per **250.96(A)**).  

5. **Bonding to Main System**  
   - The garage’s grounding electrode must be **bonded** to the main service’s grounding electrode system (per **250.58**).  

---

### **Exceptions Checked**  
- **250.25**: Applies to systems connected on the supply side of the service disconnect (not relevant here).  
- **250.30(C)**: Requires grounding at outdoor sources (not applicable for standard detached garage feeders).  
- **250.142**: Prohibits using the grounded conductor for grounding on the load side (confirms neutral/ground separation is required).  
- **250.54**: Permits auxiliary grounding electrodes but **does not override** the requirement for a dedicated grounding electrode at the garage.  

**No exceptions override the primary grounding/bonding requirements for this scenario.**  

---

## NEC 2023 Reference  
- **NEC 250.32(B)** requires a grounding electrode at the detached structure.  
- **NEC 250.24(A)(5)** similarly prohibits bonding neutral and ground in ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 9 found
- 250.24, 250.25, 250.66, 250.142, 250.30, 250.32, 250.54, 250.96, 250.58

**Response Time:** 12.4s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** PASS

**Agent Answer:**
## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022 with Exceptions)

### **Main Bonding Jumper**
- **Definition**: Connects the grounded (neutral) conductor to the equipment grounding conductor **at the service equipment** (main panel).
- **Required Location**: **Service disconnecting means** (per CEC 2022 Section 250.28).
- **Key Requirements**:
  - Sizing: Based on Table 250.102(C)(1) using the largest ungrounded service conductor.
  - Exceptions:
    - For services with **multiple enclosures** (per 230.71(B)), each enclosure’s main bonding jumper is sized based on the largest conductor serving it (250.28(D)(2)).
    - If the main bonding jumper is a **wire or busbar**, the grounding electrode conductor can connect to the equipment grounding terminal (250.24(B)(4)).
- **When Required**: Always required at the **service** (main electrical entrance).

---

### **System Bonding Jumper**
- **Definition**: Connects the grounded conductor to the equipment grounding conductor **at the source of a separately derived system** (e.g., transformers, generators).
- **Required Location**: **Source of a separately derived system** (per CEC 2022 Section 250.30).
- **Key Requirements**:
  - Sizing: Based on Table 250.102(c)(1) using the largest ungrounded conductor of the derived system.
  - Exceptions:
    - For **Class 1/2/3 circuits** from transformers ≤1000 VA, the jumper need not be larger than 14 AWG copper or 12 AWG aluminum (250.30(A)(1)(3)).
    - If the derived system source is in equipment listed as service equipment, the service’s grounding electrode conductor can be reused (250.30(A)(4) Exception).
    - For **parallel systems**, the jumper can be installed at the paralleling switchgear instead of each source (250.30(A)(1) Exception).
- **When Required**: Required for **separately derived systems** (e.g., transformers, solar inverters).

---

### **Key Exceptions**
1. **Main Bonding Jumper**:
   - For **dual-fed services** in a common enclosure, a single groun...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 250.24, 250.102, 230.71, 250.30, 250.36, 250.28, 450.6

**Response Time:** 13.3s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]

**Required Small Appliance Branch Circuits for a Kitchen:**
Per CEC 2022 Section 210.11(C)(1), **at least two 20-ampere small-appliance branch circuits** are required to serve all receptacle outlets in the kitchen, including countertop, wall, and floor outlets.

**Serving Dining Room Receptacles:**
Yes, these circuits **can also serve receptacles in the dining room**. Section 210.52(B)(1) explicitly permits small-appliance branch circuits to supply receptacles in "kitchen, pantry, breakfast room, dining room, or similar areas." 

**Key Exceptions and Limitations:**
1. **No Other Outlets Allowed** (Section 210.52(B)(2)):  
   - These circuits shall have **no other outlets** except:
     - Receptacles for specific appliances on individual circuits (Exception No. 2).
     - Clocks or supplemental equipment on general-purpose circuits (Exception No. 1).

2. **Single Kitchen Limitation** (Section 210.52(B)(3)):  
   - No small-appliance branch circuit shall serve more than **one kitchen**.

3. **Permitted Additional Loads**:
   - Refrigeration equipment and countertop outlets are included in the coverage (Section 210.52(B)(1)).

---

## NEC 2023 Reference
No difference from NEC 2023. The requirements for small-appliance branch circuits in kitchens and their extension to dining rooms are identical in NEC 2023 Section 210.52(B)(1).

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.11

**Response Time:** 10.3s

---

### core-010: load_calculations

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Expected:** Base ampacity: 30A at 90°C (Table 310.16). Temperature correction factor: 0.82 for 50°C (Table 310.15(B)(1)). Bundling adjustment: 0.80 for 6 conductors (Table 310.15(C)(1)). Adjusted ampacity = 30A × 0.82 × 0.80 = 19.68A, approximately 20A.

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- 6 current-carrying conductors in a single conduit
- 12 AWG THHN copper conductors (90°C rated)
- Ambient temperature: 50°C

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):  
   12 AWG THHN copper at 90°C = **30 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)(1)):  
   50°C ambient → **0.82 factor**

3. **Bundling Adjustment** (CEC 2022 Table 310.15(C)(1)):  
   6 conductors → **0.80 factor**

4. **Final Calculation**:  
   ```python
   30A × 0.82 × 0.80 = 19.68 amperes
   ```

**Final Answer:**  
The adjusted ampacity is **19.7 amperes** after applying both temperature and bundling corrections per CEC 2022 Sections 310.15(B)(1)(1) and 310.15(C)(1).

**Exception Check:**  
No applicable exceptions were found for this scenario in CEC 2022. The adjustments for temperature (Section 310.15[B]) and bundling (Section 310.15[C]) apply as calculated.

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

**Response Time:** 14.7s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## CEC 2022 Requirement for AFCI Protection in Bedrooms and Living Areas

**CEc_search Result:**  
CEc 2022 Section 210.12 mandates **AFCI (Arc-Fault Circuit Interrupter)** protection for **15- and 20-ampere branch circuits** in dwelling units, including:
- Bedrooms  
- Living rooms  
- Hallways  
- Closets  
- Bathrooms  
- Similar areas  

**Exceptions Identified via cec_exception_search:**  
1. **Fire alarm systems** installed per 760.41(B) or 760.121(B) are exempt if wired with metal raceway, MC cable, etc.  
2. **Temporary extensions** ≤6 ft (1.8 m) without additional outlets (e.g., minor repairs) are exempt.  

---

### Electrical Hazard Prevented  
AFCI protection prevents **electrical fires caused by arc faults**, which occur due to damaged wiring, loose connections, or degraded insulation. Common scenarios include:  
- Nails piercing cables in walls  
- Frayed cords in high-traffic areas  
- Overloaded outlets in living spaces  

Arc faults generate high heat and sparks, igniting nearby combustibles. AFCIs detect these abnormal arcs and interrupt the circuit before a fire starts.  

---

### CEC vs. NEC Comparison  
The **CEc 2022** mirrors **NEC 2023** requirements for AFCI protection in bedrooms and living areas. No significant amendments exist in California’s code for this section. Both codes:  
- Require listed combination-type or branch/feeder-type AFCIs  
- Permit similar installation methods (e.g., outlet branch-circuit AFCIs)  
- Share identical exceptions for fire alarm systems and temporary wiring  

---

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 760.41, 760.121, 210.12

**Response Time:** 13.0s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Final Answer: Torque Specifications for Conductor Termination (CEC 2022)

**Key Requirements:**
1. **General Torque Compliance**  
   Per **CEC 2022 Section 110.14(D):**  
   - Torque values must match equipment markings or manufacturer instructions.  
   - Approved methods (e.g., torque tools, shear bolts) are required to achieve specified torque.  
   - *No exceptions apply to this requirement.*  

2. **Control Circuit Devices**  
   Per **CEC 2022 Section 430.9(C):**  
   - Screw-type terminals for 14 AWG or smaller copper conductors must be torqued to **0.8 N·m (7 lb-in.)** unless otherwise identified.  
   - *No exceptions override this specific torque value.*  

**Why It Matters:**  
- Ensures low-resistance connections to prevent overheating and arcing.  
- Aligns with NEC 2023 (Section 110.14(D)) but adds California-specific clarity for control circuits.  

**NEC 2023 Reference:**  
- Same general torque requirements apply.  
- California’s CEC 430.9(C) explicitly specifies the **0.8 N·m (7 lb-in.)** minimum for control devices, which is not explicitly detailed in NEC.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 430.9, 110.14

**Response Time:** 9.9s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Service Load Calculation per CEC 2022 Article 220  
**With California-Specific Exceptions Applied**

---

### **Step 1: General Lighting Load**  
- **3000 sq ft × 3 VA/sq ft** = **9000 VA**  
  *(CEC 220.52(A) - 3 VA per sq ft for general lighting)*  

---

### **Step 2: Small Appliance Circuits**  
- **2 circuits × 1500 VA** = **3000 VA**  
  *(CEC 220.52(B) - 1500 VA per 20A small appliance circuit)*  

---

### **Step 3: Laundry Circuit**  
- **1 circuit × 1500 VA** = **1500 VA**  
  *(CEC 220.52(C) - 1500 VA for laundry circuit)*  

---

### **Step 4: Range Load (Demand Factor Applied)**  
- **12 kW range → 8000 VA**  
  *(CEC 220.55 Table - Single range of 12 kW or more uses 8000 VA demand)*  

---

### **Step 5: Dryer Load**  
- **5.5 kW dryer → 5000 VA**  
  *(CEC 220.54 - Electric dryers use 5000 VA regardless of actual rating)*  

---

### **Step 6: Central AC Load**  
- **4600 W (4600 VA)**  
  *(Given - 4-ton AC at 240V = 4600 VA)*  

---

### **Step 7: Apply Demand Factors**  
1. **General Lighting + Small Appliance + Laundry**  
   - Total: **9000 + 3000 + 1500 = 13,500 VA**  
   - **First 3000 VA @ 100%** = **3000 VA**  
   - **Remaining 10,500 VA @ 35%** = **3675 VA**  
   - **Adjusted Total** = **6675 VA**  
   *(CEC 220.52 Demand Factor)*  

2. **Add Fixed Appliances**  
   - **Range**: 8000 VA  
   - **Dryer**: 5000 VA  
   - **AC**: 4600 VA  
   - **Total Fixed Loads** = **17,600 VA**  

3. **Total Service Load**  
   - **6675 VA (adjusted general) + 17,600 VA (fixed)** = **24,275 VA**  

---

### **Step 8: Convert to Amperes**  
- **Service Voltage**: 240V  
- **Total Load**: 24,275 VA ÷ 240V = **101.15A**  

---

### **California-Specific Exceptions Checked**  
- **CEC 220.53** (Appliance demand factors): Excludes cooking equipment, dryers, and AC—no impact here.  
- **CEC 220.51** (Fixed space heating): Not applicable (no electric space heating listed).  
- **CEC 220.85** (Two dwelling units): Not applicable (single-family residence).  

---...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search, nec_search
- CEC Primary: Yes

**Citations:** 6 found
- 220.53, 220.52, 220.54, 220.51, 220.85, 220.55

**Response Time:** 24.4s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## California Electrical Code (CEC) Violations Identified

**1. Insufficient Working Space Depth**  
- **CEC 2022 Section 110.26(A)(1)**  
  - *Requirement:* Minimum depth for panels in Condition 2 (exposed live parts on one side, grounded on the other) is **34 inches** (Table 110.26(A)(1)).  
  - *Violation:* Panel has **28 inches depth**, which is **6 inches less** than required.  
  - *No applicable exceptions* override this requirement.  

**2. Storage in Working Space**  
- **CEC 2022 Section 110.26(B)**  
  - *Requirement:* Working space **must not be used for storage**.  
  - *Violation:* Water heater located **16 inches within the working space** violates this rule.  
  - *No exceptions* permit storage in working space.  

**3. Inadequate Vertical Clearance**  
- **CEC 2022 Section 110.26(A)(3)**  
  - *Requirement:* Working space must extend **2.0 meters (6 ft 6 in)** vertically from the floor.  
  - *Violation:* Panel mounted at **5 ft (60 in)** leaves **only 26 inches** of vertical space above the panel. If the panel height exceeds 5 ft, total vertical clearance is insufficient.  

**4. Obstruction of Working Space**  
- **CEC 2022 Section 110.26(A)(6)**  
  - *Requirement:* Floor/grade in working space must be **level and unobstructed**.  
  - *Violation:* Water heater placement **obstructs the working space** and could impede access/egress.  

**5. Dedicated Electrical Space Violation**  
- **CEC 2022 Section 110.26(E)(1)(a)**  
  - *Requirement:* A **dedicated space** of **width × depth × height** (equipment dimensions + 1.8 m/6 ft) must be free of foreign systems.  
  - *Violation:* Water heater intrudes into this dedicated space.  

---

## Summary of Violations  
| Violation | CEC Section | Description |  
|----------|-------------|-------------|  
| 1 | 110.26(A)(1) | Depth insufficient (28 in < 34 in required) |  
| 2 | 110.26(B) | Storage (water heater) in working space |  
| 3 | 110.26(A)(3) | Vertical clearance likely inadequate |  
| 4 | 110.2...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search, nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 18.4s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## Revised Circuit Protection Requirements (NEC 2023 with Exceptions)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Required Protection:** **GFCI Breaker**  
- **NEC Reference:** 210.8(A)(6)  
- **Exception Check:** No exceptions override this requirement for countertop receptacles.  
- **Rationale:** All countertop receptacles **must** have GFCI protection per 210.8(A)(6). Exceptions like 210.52(B)(2) relate to receptacle placement, not GFCI requirements.

---

### 2. **Dishwasher (Dedicated 15A Circuit)**
- **Required Protection:** **Standard Breaker**  
- **NEC Reference:** 210.8(A)(6) Exception No. 1  
- **Exception Check:** Confirmed by 210.52(B)(1) Exception No. 2 (fixed appliance on dedicated circuit).  
- **Rationale:** Fixed appliances like dishwashers **do not require GFCI** if installed in non-accessible locations.

---

### 3. **Garbage Disposal (Dedicated 15A Circuit)**
- **Required Protection:** **Standard Breaker**  
- **NEC Reference:** 210.8(A)(6) Exception No. 1  
- **Exception Check:** 210.52(B)(1) Exception No. 2 applies to fixed appliances.  
- **Rationale:** Garbage disposals on dedicated circuits **do not require GFCI** if installed in non-accessible locations.

---

### 4. **Refrigerator (Dedicated 20A Circuit)**
- **Required Protection:** **Standard Breaker**  
- **NEC Reference:** 210.12 (AFCI) and 210.8 (GFCI)  
- **Exception Check:** No exceptions apply to AFCI/GFCI exemptions for refrigerators.  
- **Rationale:** Refrigerator circuits are **exempt from AFCI** (210.12) and **not required for GFCI** (210.8).

---

## Final Summary with Exceptions Verified

| Circuit Type               | Protection Required | NEC Section(s)                | Exceptions Applied              |
|---------------------------|---------------------|-------------------------------|----------------------------------|
| Countertop Receptacles     | GFCI Breaker        | 210.8(A)(6)                   | None                             |
| Dishwasher (Dedica...

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 3 found
- 210.52, 210.8, 210.12

**Response Time:** 17.2s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## Corrected Subpanel Grounding/Bonding Configuration (CEC 2022)

**Violations Confirmed (No Applicable Exceptions Found):**

1. **Main Bonding Jumper Installed**  
   - **Violation:** CEC 250.24(D) requires the main bonding jumper **only at the service disconnect**. Subpanels must **separate neutrals and grounds**.  
   - **Correction:** Remove the main bonding jumper. Connect **neutral conductors to the neutral bar** and **grounding conductors to the ground bar**.

2. **Neutral Bar Bonded to Enclosure**  
   - **Violation:** CEC 250.4(A)(5) prohibits neutral-to-enclosure bonds in subpanels. This creates a **parallel current path** and risks equipment damage.  
   - **Correction:** Isolate the neutral bar from the enclosure. Only the **ground bar** should be bonded to the metal enclosure via the equipment grounding conductor.

3. **Neutral-to-Ground Bond via Enclosure**  
   - **Violation:** CEC 250.24(A)(5) prohibits grounding electrode connections on the load side of the service disconnect. The neutral-to-enclosure bond creates an **unintended ground-neutral bond**.  
   - **Correction:** Ensure **no electrical connection between neutral and ground bars or enclosure** in the subpanel.

---

**NEC 2023 Comparison**  
- **NEC 250.24(D):** Same requirement—no main bonding jumper in subpanels.  
- **NEC 250.4(A)(5):** Same grounding/bonding rules for equipment.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 250.24, 250.4

**Response Time:** 12.7s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**
## Final Answer with CEC 2022 Exceptions Considered

**Maximum Conductors in RMC 1¼" (California):**  
**28 conductors** of 10 AWG THHN (same as NEC calculation)

**Exception Analysis:**
- CEC 314.16(B)(1) Exception: Allows omitting equipment grounding conductors or fixture wires from calculations if they originate from a domed luminaire.  
  → **Does NOT apply** to this commercial installation scenario.

- No other exceptions in returned results modify the 40% fill requirement for RMC 1¼" conduit.

**Code Compliance:**  
CEC 2022 Section 314.16(B) confirms the 40% fill limit for 3 or more conductors. No California amendments affect this calculation.

✓ Sources: CEC 2022 (California), NEC 2023 (reference)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 314.16

**Response Time:** 15.2s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**
## Final Compliance Determination (CEC 2022)

**Voltage Drop Result:**  
- Calculated: **2.37%**  
- **CEC 2022 Limit:** 1.5% (Section 647.4(D)) → ❌ **Non-compliant**  
- **NEC 2023 Recommendation:** ≤3% (210.19(A) Informational Note) → ✅ Acceptable  

**Exception Analysis:**  
- **No applicable exceptions** were found for general branch circuits in residential/commercial applications.  
- **647.3** (separately derived 120V systems) applies only to **commercial/industrial** occupancies with **qualified supervision** for noise reduction in sensitive electronics. Not applicable here.  
- Other exceptions (625.46, 640.7) relate to EV systems and grounding, which are unrelated to this scenario.  

**Conclusion:**  
The installation **violates CEC 2022** due to excessive voltage drop (2.37% > 1.5%). While NEC 2023 accepts this as compliant, California's stricter CEC requirements render it **non-compliant**.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 647.3, 625.46, 210.19, 647.4, 640.7

**Response Time:** 19.8s

---

### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- Conductor: 12 AWG TW (60°C rated) copper
- Number of CCCs: 6
- Ambient temperature: 43°C (110°F)

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):
   12 AWG copper, 60°C column = **20 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   43°C ambient, 60°C conductor = **0.71 factor**

3. **Bundling Adjustment** (CEC 2022 Table 310.15(C)(1)):
   6 current-carrying conductors = **0.80 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 20 × 0.71 × 0.80 = 11.36 amperes
   ```

**Final Answer: 11.36 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

No exceptions to these derating requirements were found.

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

**Response Time:** 10.5s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Minimum Grounding Electrode Conductor Size (CEC 2022)

**Given:**
- Four parallel 250 kcmil copper service-entrance conductors per phase
- Total equivalent area: 4 × 250 kcmil = **1000 kcmil per phase**

**CEC 2022 Table 250.66 Analysis:**
1. **Service-Entrance Conductor Size:** 1000 kcmil copper
2. **Corresponding GEC Size:** **3/0 AWG copper** (per Table 250.66)

**Key Requirements:**
- Per CEC 250.66, the grounding electrode conductor must be sized based on the **total area of the largest service-entrance conductor**.
- For parallel conductors, the total area is summed (4 × 250 kcmil = 1000 kcmil).
- Table 250.66 specifies **3/0 AWG copper** as the minimum GEC for 1000 kcmil service conductors.

**Exception Analysis:**
- Exceptions in 250.66(A)-(C) allow smaller conductors if connected to specific electrodes (rods, concrete-encased, or ground rings). However, since the question does not specify the electrode type, the general rule in Table 250.66 applies.

**Final Answer:**  
The minimum required copper grounding electrode conductor (GEC) size is **3/0 AWG** per CEC 2022 Table 250.66.

---
## NEC 2023 Reference  
No difference from CEC 2022. NEC 2023 Table 250.66 matches California requirements for this calculation.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 37.1s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 25/28
- **Success Rate**: 100.0%
- **Average Response Time**: 15.9s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

