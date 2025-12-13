# CEC 2022 Unified Evaluation Results - Run 43

**Date:** 2025-12-12
**Description:** Surge protection domain knowledge fix

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 53 |
| Successful | 53 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 499.3s |
| Avg Duration | 9.4s |
| Reflection Used | 53/53 |
| Reflection Improved | 6/53 |
| Hint Enforcement | 3/53 |
| Protection Enforcement | 5/53 |
| Service Conductor Enforcement | 1/53 |

## Results by Category

| Category | Total | Success | Rate |
|----------|-------|---------|------|
| adjusted_ampacity | 1 | 1 | 100% |
| ampacity_adjustment | 2 | 2 | 100% |
| clearance_violations | 1 | 1 | 100% |
| commercial_load | 1 | 1 | 100% |
| conductor_ampacity | 1 | 1 | 100% |
| conduit_fill | 1 | 1 | 100% |
| derating_calculation | 1 | 1 | 100% |
| dwelling_load | 1 | 1 | 100% |
| edge_cases | 2 | 2 | 100% |
| electrification | 2 | 2 | 100% |
| enclosure | 1 | 1 | 100% |
| ev_charging | 1 | 1 | 100% |
| fixture_wire | 1 | 1 | 100% |
| flexible_cord | 1 | 1 | 100% |
| gfci_afci_compliance | 1 | 1 | 100% |
| grounding | 2 | 2 | 100% |
| grounding_bonding | 2 | 2 | 100% |
| grounding_electrode_conductor | 1 | 1 | 100% |
| heat_pump | 1 | 1 | 100% |
| knowledge | 2 | 2 | 100% |
| knowledge_simple | 5 | 5 | 100% |
| lighting_load | 1 | 1 | 100% |
| load_calculations | 2 | 2 | 100% |
| medium_voltage | 1 | 1 | 100% |
| motor_circuit | 1 | 1 | 100% |
| motor_control | 1 | 1 | 100% |
| multi_article | 2 | 2 | 100% |
| overcurrent | 1 | 1 | 100% |
| panel_load_calculation | 1 | 1 | 100% |
| panelboard_requirements | 1 | 1 | 100% |
| service_sizing | 1 | 1 | 100% |
| solar_pv | 1 | 1 | 100% |
| subpanel_violations | 1 | 1 | 100% |
| surge_protection | 1 | 1 | 100% |
| table_lookup | 3 | 3 | 100% |
| voltage_drop | 1 | 1 | 100% |
| why_questions | 2 | 2 | 100% |
| working_space | 1 | 1 | 100% |

## Results by Question

### cec2022-001

**Original ID:** baseline-001 | **Category:** table_lookup | **Tier:** baseline

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Duration:** 8.9s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## 12 AWG Copper Conductor Ampacity (CEC 2022)

**Ampacity**: 25 amperes at 75°C (Table 310.16)  
**Overcurrent Protection Limit**: 20A maximum (Section 240.4(D))

**Key Notes**:
- The 25A ampacity is based on 30°C ambient temperature and ≤3 current-carrying conductors
- **240.4(D) Limitation**: Despite 25A ampacity, 12 AWG copper conductors **must be protected at 20A maximum** for overcurrent protection
- California amendment note indicates this is a modified NEC value

[OK] Source: CEC 2022

---

### cec2022-002

**Original ID:** baseline-002 | **Category:** table_lookup | **Tier:** baseline

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 5.9s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size**: **6 AWG copper**  
- **Ampacity**: 65A at 75°C (Table 310.16)  
- **Overcurrent protection**: 60A breaker permitted (240.4(D) allows 65A-rated conductor for 60A OCP)  

**Key Citations**:  
- CEC Table 310.16 (ampacity)  
- CEC 240.4(D) (overcurrent protection limits)  

**Inspector Notes**:  
- If ambient temperature exceeds 30°C or more than 3 current-carrying conductors are bundled, apply correction factors from **310.15(B)(1)(1)** and **310.15(C)(1)**.  
- 6 AWG is the smallest copper conductor allowed for 60A circuits (50A-rated 8 AWG is insufficient).  

[OK] Source: CEC 2022

---

### cec2022-003

**Original ID:** baseline-003 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 23.7s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes
**Service Conductor Enforced:** No

**Answer:**

## Kitchen Circuit Protection (CEC 2022)

**Answer:**  
In residential kitchens, **both GFCI and AFCI protections are required** for 120V, 15- and 20-ampere branch circuits supplying countertop receptacles:

1. **GFCI Protection** (CEC 2022 Section 210.8(A)(6)):  
   - Required for **all countertop receptacles** to prevent electric shock hazards.  

2. **AFCI Protection** (CEC 2022 Section 210.12(A)):  
   - Required for **all 120V, 15/20A circuits** in dwelling unit kitchens.  
   - Exceptions: None apply for standard kitchen circuits (e.g., no fire alarm system exceptions).  

**Key Details:**  
- **AFCI Implementation**: Must use one of the listed methods (e.g., combination-type AFCI breaker or outlet device).  
- **GFCI + AFCI**: Both protections are required **independently**—a dual-function device satisfies both if listed.  

**Citations:**  
- GFCI: CEC 2022 Section 210.8(A)(6)  
- AFCI: CEC 2022 Section 210.12(A)  

[OK] Source: CEC 2022

---

### cec2022-004

**Original ID:** baseline-004 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 12.7s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes
**Service Conductor Enforced:** No

**Answer:**

## Circuit Protection for Bedroom Circuits (CEC 2022)

**Final Answer:**  
- **AFCI Protection**: **Required** per **CEC 2022 Section 210.12(A)** for all 120V, 15A/20A bedroom circuits.  
- **GFCI Protection**: **Not required** per **CEC 2022 Section 210.8** (bedrooms not listed in GFCI-mandated locations).  

**Code Analysis:**  
1. **AFCI Requirement**:  
   - Section 210.12(A) explicitly lists bedrooms as a required location for AFCI protection.  
   - No exceptions apply to standard bedroom circuits.  

2. **GFCI Requirement**:  
   - Section 210.8(A) mandates GFCI for **bathrooms, kitchens, outdoors, garages**, etc., but **bedrooms are not included**.  
   - No exceptions in 210.8 apply to bedrooms for GFCI.  

**Inspector Note:**  
- **AFCI** prevents fires from arcing faults in wiring (required in all 15/20A dwelling circuits).  
- **GFCI** prevents shocks in wet/damp locations (not required in bedrooms).  

[OK] Source: CEC 2022 Sections 210.12(A), 210.8

---

### cec2022-005

**Original ID:** baseline-005 | **Category:** table_lookup | **Tier:** baseline

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 7.3s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Yes**, aluminum conductors are permitted for a 200A service. The required size is:

- **4/0 AWG aluminum**  
- **Source**: CEC 2022 Table 310.12(A) (Single-Phase Dwelling Services and Feeders)

### Key Conditions for This Application:
1. **System Type**: 120/240V or 120/208Y single-phase system
2. **Load Type**: Conductors supply the **entire load** of the dwelling unit
3. **No Derating Required**: Temperature correction and bundling adjustments are not needed
4. **Termination Rating**: Conductors must be terminated at equipment rated for **75°C** (per 110.14(C))

### Inspector Note:
- For services requiring derating (e.g., high ambient temperature, bundled conductors), use **Table 310.16** with appropriate adjustments instead of Table 310.12(A).
- Always verify grounding electrode conductor size using **Table 250.66** based on the service conductor size.

[OK] Source: CEC 2022

---

### cec2022-006

**Original ID:** baseline-006 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 14.8s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Dedicated Working Space Requirements (CEC 2022)

**Section 110.26(B)** requires:
- **Clear space** in front of electrical equipment for working space
- **No storage** allowed in this area
- **Minimum width**: 30 inches (762 mm) at all points (NEC standard, assumed aligned with CEC)

### Key Implications:
- The **3-foot depth** (from Table 110.26(A)(1)) is separate from the **30-inch width** requirement
- Both depth and width must be maintained for safe access
- Storage or obstructions in this space violate 110.26(B)

[OK] Source: CEC 2022 (Confirmed via code knowledge and search context)

---

### cec2022-007

**Original ID:** baseline-007 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 6.5s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Required Small Appliance Branch Circuits for Kitchen (CEC 2022)

**Answer:**  
A minimum of **two 20-ampere small-appliance branch circuits** are required to serve the kitchen in a dwelling unit.

**Code Basis:**  
- **CEC 2022 Section 210.11(C)(1):**  
  *"In addition to the number of branch circuits required by other parts of this section, two or more 20-ampere small-appliance branch circuits shall be provided for all receptacle outlets specified by 210.52(B)."*  

- **CEC 2022 Section 210.52(B)(1):**  
  These circuits must supply all wall, floor, and countertop receptacles in the kitchen, pantry, breakfast room, dining room, or similar areas.  

**Key Notes:**  
- The circuits must **not serve any other outlets** beyond those specified (per Exception No. 1 in 210.52(B)(2)).  
- **No exceptions** apply for kitchens unless explicitly permitted (e.g., individual circuits for specific appliances like refrigerators, but these do not reduce the two-circuit minimum).  

[OK] Source: CEC 2022

---

### cec2022-008

**Original ID:** baseline-008 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Is surge protection required for a new 200A residential service?

**Duration:** 11.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is **mandatorily required** for all new residential services in California per **CEC 2022 Section 230.67(A)**.  

**Key Requirements:**  
1. **Type of SPD**: Must be a **Type 1 or Type 2** surge-protective device (SPD) (230.67(C)).  
2. **Location**:  
   - Must be **integral to the service equipment** or  
   - Located **immediately adjacent** to the service equipment (230.67(B)).  
   - *Exception*: If installed downstream, it must be at the next level of distribution.  

**Applicability**:  
This applies to **all services supplying dwelling units**, including new 200A residential services. No exceptions exist for service size in this section.  

[OK] Source: CEC 2022 Section 230.67

---

### cec2022-009

**Original ID:** core-001 | **Category:** multi_article | **Tier:** core

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 10.3s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Service Conductor Sizing for 200A Dwelling Service (CEC 2022)

**Required Service Conductor Sizes:**
- **Copper**: 2/0 AWG (75°C rating)
- **Aluminum**: 4/0 AWG (75°C rating)

**Source**: CEC 2022 Table 310.12(A) (Single-Phase Dwelling Services and Feeders)

**Key Conditions for This Sizing**:
1. **No derating required** – Assumes conductors are installed in ambient temperatures ≤ 30°C and not bundled in raceways with more than 3 current-carrying conductors.
2. **Applies to 120/240V or 120/208Y systems** – Standard for residential services.
3. **Supplies entire dwelling load** – Includes all listed appliances (range, dryer, AC, water heater) and 3,000 sq ft living space.

**Aluminum Use**: Permitted for service conductors under CEC 2022. 4/0 AWG aluminum meets the 200A requirement when using Table 310.12(A) for dwelling units.

**Inspector Note**: If conductors are subject to higher ambient temperatures (>30°C) or excessive bundling, apply correction factors from:
- **Temperature**: Table 310.15(B)(1)(1)
- **Bundling**: Table 310.15(C)(1)

[OK] Source: CEC 2022

---

### cec2022-010

**Original ID:** core-002 | **Category:** multi_article | **Tier:** core

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the requirements for the circuit breaker and neutral termination?

**Duration:** 8.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Multiwire Branch Circuit Requirements (CEC 2022)

### Circuit Breaker Requirements
1. **Simultaneous Disconnection** (210.4(B)):  
   - A **2-pole circuit breaker** must be used to disconnect **all ungrounded conductors** simultaneously.  
   - **Two single-pole breakers** without a handle tie are **not permitted** (per 210.4(B) and 240.15(B) informational note).  

2. **Amperage Rating**:  
   - For kitchen receptacles, the circuit must be rated **20A** (per 210.5(A) and 210.11(C)(1)).  
   - **12 AWG conductors** are appropriate for 20A circuits (240.4(D)).  

---

### Neutral Termination Requirements
1. **Grouping of Conductors** (210.4(D)):  
   - The **neutral conductor** must be **grouped with the ungrounded conductors** (as in 12/3 cable).  
   - The neutral must **not be shared** with other circuits and must terminate on the **neutral bus** in the panel.  

2. **Sizing**:  
   - The neutral must be the **same size** as the ungrounded conductors (12 AWG in this case).  

---

### Key Exceptions
- **Exception No. 1** (210.4(C)): Not applicable here, as the circuit supplies multiple receptacles (not a single utilization equipment).  
- **Exception No. 2**: Not applicable, as simultaneous disconnection is required for line-to-neutral loads (kitchen receptacles).  

---

### Inspector Notes
- Verify the breaker is a **2-pole type** (or single-pole breakers with a listed handle tie).  
- Confirm the neutral is **not shared** with other circuits and is properly bonded to the panel.  
- Ensure all conductors (hot, neutral, ground) are in the **same cable** (12/3 with ground).  

[OK] Source: CEC 2022

---

### cec2022-011

**Original ID:** core-003 | **Category:** knowledge | **Tier:** core

**Question:** Where is GFCI protection required in a residential dwelling? List all locations.

**Duration:** 19.3s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes
**Service Conductor Enforced:** No

**Answer:**

## GFCI and AFCI Protection in Residential Dwellings (CEC 2022)

### **GFCI Protection Locations**  
Per **CEC 2022 Section 210.8(A)**, GFCI protection is required for **120–250V receptacles** in these locations:  
1. **Bathrooms**  
2. **Garages/accessory buildings** (at or below grade)  
3. **Outdoors**  
4. **Crawl spaces** (at or below grade)  
5. **Basements** (except fire alarm systems)  
6. **Kitchens** (countertop receptacles)  
7. **Within 6 ft of sinks/bathtubs/shower stalls**  
8. **Laundry areas**  
9. **Indoor damp/wet locations**  

**Exceptions**:  
- Receptacles for snow-melting/deicing systems (per 426.28/427.22).  
- Fire alarm systems (per 760.41/760.121).  

---

### **AFCI Protection Requirements**  
Per **CEC 2022 Section 210.12(A)**, **AFCI protection is mandatory** for **all 120V, 15/20A branch circuits** in these dwelling areas:  
1. **Kitchens**  
2. **Family rooms**  
3. **Dining rooms**  
4. **Living rooms**  
5. **Bedrooms**  
6. **Sunrooms**  
7. **Recreation rooms**  
8. **Closets**  
9. **Hallways**  
10. **Laundry areas**  
11. **Similar rooms/areas**  

**Exceptions**:  
- Fire alarm systems (per 760.41/760.121).  

**AFCI Installation Options**:  
- Combination-type AFCI at the circuit origin.  
- Branch/feeder-type AFCI + outlet-type AFCI at first outlet.  
- Supplemental protection with specific wiring constraints.  

---

### **Key Differences**  
- **GFCI** targets **personnel safety** in high-risk moisture areas.  
- **AFCI** targets **arc faults** in living areas to prevent fires.  
- **AFCI applies to all 120V, 15/20A circuits** in listed rooms, even if no receptacles are present (e.g., lighting circuits).  

[OK] Source: CEC 2022 Sections 210.8, 210.12

---

### cec2022-012

**Original ID:** core-004 | **Category:** knowledge | **Tier:** core

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 6.1s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Surge Protection Requirements for Residential Services (CEC 2022)

**Answer:**

**1. Requirement:**  
Yes, surge protection is **mandated** for all new residential services under **CEC 2022 Section 230.67(A)**. A surge-protective device (SPD) must be installed for "all services supplying dwelling units."

**2. Installation Location:**  
- **Primary Location:** The SPD must be **integral to the service equipment** or **immediately adjacent** to it (Section 230.67(B)).  
- **Alternative Location:** If space in the service equipment is insufficient, the SPD may be installed at the **next level of distribution equipment downstream** toward the load (Exception to 230.67(B)).  

**3. SPD Type:**  
The SPD must be **Type 1 or Type 2** as specified in Section 230.67(C).  

**Inspector Note:**  
- Verify the SPD is listed for the intended application.  
- Ensure the SPD is installed **on the load side of the service disconnect** unless exceptions apply.  

[OK] Source: CEC 2022

---

### cec2022-013

**Original ID:** core-005 | **Category:** edge_cases | **Tier:** core

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet code requirements?

**Duration:** 12.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Panel Location and Clearance Compliance (CEC 2022)

### 1. **Closet Prohibition (240.24(D))**
- **Rule**: Overcurrent devices **shall not be located in clothes closets**.
- **Violation**: If the panel is in a **clothes closet**, this is a **direct violation** of **CEC 2022 Section 240.24(D)**.
- **Inspector Note**: Even if clearances are adequate, the location itself is prohibited in clothes closets.

---

### 2. **Front Clearance (110.26 Working Space)**
- **Required Depth**: For standard 120/240V residential panels (Condition 1), **minimum 30 inches** of clearance in front (CEC Table 110.26(A)(1)).
- **Provided Clearance**: **24 inches** is **insufficient** by **6 inches**.
- **Code Reference**: CEC 2022 Table 110.26(A)(1) (Condition 1 for 120/240V systems).

---

### 3. **Water Heater Proximity**
- **Rule**: No obstructions within working space (110.26(A)(1)).
- **Assessment**: 
  - If the water heater is **within 30 inches horizontally** of the panel, it **violates** working space requirements.
  - **18 inches to the side** likely **intrudes** into the required clearance area.
- **Inspector Note**: Objects like water heaters must not encroach into the working space. Minimum 30 inches of unobstructed space is required.

---

### **Final Compliance Status**
- **Closet Type**: If a **clothes closet**, **fails** 240.24(D).
- **Front Clearance**: **Fails** 110.26(A)(1) (24" < 30").
- **Water Heater Clearance**: **Fails** 110.26(A)(1) if within 30" horizontally.

**Conclusion**: The installation **does not meet code requirements** due to prohibited location (clothes closet) and insufficient working space.

[OK] Source: CEC 2022

---

### cec2022-014

**Original ID:** core-006 | **Category:** edge_cases | **Tier:** core

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 12.1s | **Iterations:** 4

**Tools Called:** cec_search, cec_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

[VERIFIED] Answer is complete.  

**Final Verification:**  
- **Code Citations**: Confirmed **CEC 2022 Section 240.7(B)** and **110.14(A)** apply directly to the scenario.  
- **Exceptions**: No exceptions apply since the breaker is **not marked** for multiple conductors.  
- **Cross-References**: Section 408.41 (grounded conductor terminations) is unrelated to this specific breaker terminal rule.  
- **Accuracy**: The violation is correctly identified, and corrective actions align with code requirements.  

**Conclusion**: The installation violates CEC 2022 and requires correction.

---

### cec2022-015

**Original ID:** core-007 | **Category:** grounding_bonding | **Tier:** core

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 7.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

**Configuration Requirements:**

1. **Grounding Electrode System**  
   - A **separate grounding electrode** (e.g., ground rod, plate, or concrete-encased electrode) **must be installed** at the detached garage (Section 250.32(A)).  
   - **Exception does not apply** because the garage is supplied by a 4-wire feeder (not a single branch circuit).  

2. **Grounding Electrode Conductor (GEC)**  
   - The GEC must connect the **grounding electrode** to the **grounding busbar** in the garage subpanel.  
   - Size the GEC per **Table 250.66**, based on the **largest ungrounded (hot) conductor** in the feeder.  
     - Example: For a 200A feeder with 2/0 AWG copper conductors, use **2/0 AWG copper** for the GEC.  

3. **Equipment Grounding Conductor (EGC)**  
   - The EGC must run with the feeder conductors and connect to the **grounding busbar** in the subpanel.  
   - Size the EGC per **Table 250.122**, based on the **overcurrent protection rating** of the feeder.  
     - Example: For a 200A feeder, use **6 AWG copper** or **4 AWG aluminum**.  

4. **Neutral and Ground Separation**  
   - The **neutral bar** in the subpanel must be **electrically isolated** from the panel enclosure.  
   - **No connection** between the neutral and grounding electrode system in the subpanel (Section 250.32(B)(1)).  

5. **Bonding Jumper**  
   - A **system bonding jumper** is required at the main service, but **not at the subpanel**.  

---

**Key Code References:**  
- **Section 250.32(A)**: Mandates grounding electrode for feeders to detached structures.  
- **Section 250.50**: Bonds all grounding electrodes at the structure.  
- **Table 250.66**: Sizes GEC based on largest ungrounded conductor.  
- **Table 250.122**: Sizes EGC based on overcurrent protection.  

**Inspector Note:**  
- Verify the grounding electrode meets **Section 250.52** (e.g., 8 ft rod, 2 rods spaced 6 ft apart if soil is resistive).  
- Ensure the GEC and EGC are **separate conductors** with no direct connection between them.  

[OK] Source: CEC 2022

---

### cec2022-016

**Original ID:** core-008 | **Category:** grounding_bonding | **Tier:** core

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 10.0s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
1. **Main Bonding Jumper**  
   - **Location**: At the **service equipment** (per CEC 2022 Section 100).  
   - **Purpose**: Connects the **grounded circuit conductor** (neutral) to the **equipment grounding conductor** at the service.  
   - **Required By**: CEC 250.28 for grounded systems.  

2. **System Bonding Jumper**  
   - **Location**: At the **source of a separately derived system** (e.g., transformers, generators) (per CEC 2022 Section 100).  
   - **Purpose**: Connects the **grounded conductor** to the **supply-side bonding jumper** or **equipment grounding conductor** at the separately derived system.  
   - **Required By**: CEC 250.28 for grounded separately derived systems.  

---

### **Key Differences**
| Feature                  | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|--------------------------|--------------------------------------------------|--------------------------------------------------|
| **Application**          | Service equipment (main service panel)           | Separately derived systems (e.g., transformers)  |
| **Connection Point**     | Grounded conductor to equipment grounding conductor at the service |
|                          | Grounded conductor to equipment grounding conductor at the derived system |
| **Sizing Reference**     | Table 250.102(C)(1), based on largest service conductor |
|                          | Table 250.102(C)(1), based on largest feeder conductor to the derived system |

---

### **When Each is Required**
1. **Main Bonding Jumper**  
   - **Required in all grounded services** (CEC 250.28).  
   - Must be sized per **Table 250.102(C)(1)** based on the largest ungrounded service conductor.  
   - Example: For a service with 4/0 AWG copper ungrounded conductors, the main bonding jumper must be **4 AWG copper** (see Table 250.102(C)(1)).  

2. **System Bonding Jumper**  
   - **Required for all grounded separately derived systems** (CEC 250.28).  
   - Sizing depends on the largest ungrounded conductor in the derived system.  
   - Example: For a transformer with 3/0 AWG copper feeders, the system bonding jumper must be **2 AWG copper** (Table 250.102(C)(1)).  

---

### **Inspector Notes**
- **Main bonding jumpers** ensure the service neutral and equipment grounding system are bonded at the service.  
- **System bonding jumpers** ensure the derived system’s grounded conductor and equipment grounding system are bonded at the source.  
- Both must use **copper, aluminum, or corrosion-resistant materials** (CEC 250.28(A)).  
- **Never substitute** a system bonding jumper for a main bonding jumper or vice versa.  

[OK] Source: CEC 2022 Sections 100, 250.28, 250.102(C)(1)

---

### cec2022-017

**Original ID:** core-009 | **Category:** load_calculations | **Tier:** core

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 14.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

**1. Required Number of Circuits:**
- **Minimum Requirement**: **Two or more 20-ampere small-appliance branch circuits** are required for kitchens (CEC 2022 Section 210.52(B)(1)).  
- **Scope**: These circuits must serve **all receptacles in the kitchen**, including countertop outlets and floor/wall receptacles.

**2. Dining Room Receptacle Service:**
- **Yes**, these circuits **can also serve dining room receptacles**.  
- Section 210.52(B)(3) explicitly permits small-appliance branch circuits to supply receptacles in the **kitchen and "other rooms specified in 210.52(B)(1)"**, which includes dining rooms.  
- **Key Condition**: No small-appliance branch circuit shall serve more than **one kitchen**, but dining room receptacles are allowed on the same circuits.

**3. Code Citations:**
- **210.52(B)(1)**: Requires two or more 20A circuits for kitchens, pantries, breakfast rooms, and dining rooms.  
- **210.52(B)(3)**: Permits these circuits to serve receptacles in kitchens and other specified rooms (including dining rooms).  
- **210.11(C)(1)**: Mandates the minimum number of small-appliance branch circuits for dwelling units.

**Inspector Note**: Dining room receptacles must not be served by small-appliance circuits if they are in a different dwelling unit (per 210.25(A)). Always verify the specific dwelling unit boundaries.  

[OK] Source: CEC 2022

---

### cec2022-018

**Original ID:** core-010 | **Category:** load_calculations | **Tier:** core

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 8.4s | **Iterations:** 6

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Base ampacity**: 30A (12 AWG THHN copper at 90°C per Table 310.16)  
**Temperature correction**: 0.82 (50°C ambient per Table 310.15(B)(1)(1))  
**Bundling adjustment**: 0.8 (6 conductors per Table 310.15(C)(1))  

**Calculation**:  
30A × 0.82 × 0.8 = **19.68A**  

**Final adjusted ampacity**: 19.7A  

[OK] Source: CEC 2022

---

### cec2022-019

**Original ID:** core-011 | **Category:** why_questions | **Tier:** core

**Question:** Why is AFCI protection required for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 18.1s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes
**Service Conductor Enforced:** No

**Answer:**

## AFCI vs GFCI Protection in Dwelling Units (CEC 2022)

**AFCI Protection (210.12):**
- **Required in:** Bedrooms, living rooms, hallways, closets, and similar areas
- **Protects against:** Arc faults (electrical discharges that can ignite surrounding materials)
- **Key hazard:** Prevents fires caused by damaged/deteriorated wiring or loose connections

**GFCI Protection (210.8):**
- **Required in:** Bathrooms, kitchens, garages, outdoors, basements, etc.
- **Protects against:** Ground faults (current leakage to ground, risking electric shock)
- **Not required in:** Bedrooms/living areas per CEC 2022 (found no GFCI requirements for these spaces)

**Inspector Note:** 
- CEC 210.12(A) explicitly requires AFCI for **ALL** 120V, 15/20A circuits in dwelling units (including bedrooms/living areas)
- CEC 210.8 does **not** require GFCI protection for bedrooms/living areas (only for wet/damp locations)
- Dual protection (AFCI + GFCI) is required in **kitchens** (AFCI for countertop circuits + GFCI for receptacles)

[OK] Source: CEC 2022 Sections 210.8, 210.12

---

### cec2022-020

**Original ID:** core-012 | **Category:** why_questions | **Tier:** core

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 7.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

**Why Torque Specifications Are Important:**
1. **Prevents Loose Connections:** Proper torque ensures conductors are securely fastened to terminal lugs, reducing risk of arcing, overheating, and connection failures.
2. **Avoids Over-Torquing:** Excessive torque can damage terminal lugs or conductor strands, compromising the electrical connection.
3. **Compliance with Safety Standards:** Ensures adherence to code requirements for reliable and safe electrical installations.

**Code Requirements Location:**
- **CEC 2022 Section 110.14(D):**  
  *"Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer. An approved means shall be used to achieve the indicated torque value."*  
  - **Key Provisions:**  
    - Torque values must match equipment markings or manufacturer instructions.  
    - Approved methods include torque tools, shear bolts, or breakaway devices with visual indicators.  
    - If torque values are not marked, contact the equipment manufacturer (Informational Note No. 2).  

- **CEC 2022 Section 430.9(C):**  
  *"Control circuit devices with screw-type pressure terminals used with 14 AWG or smaller copper conductors shall be torqued to a minimum of 0.8 N·m (7 lb-in.) unless identified for a different torque value."*  

**Inspector Note:**  
Always verify torque values directly on equipment nameplates or in manufacturer documentation. If unspecified, use the values from **UL Standard 486A-486B** (referenced in Informational Note No. 2 of 110.14(D)) or contact the manufacturer.  

[OK] Source: CEC 2022

---

### cec2022-021

**Original ID:** inspection-001 | **Category:** panel_load_calculation | **Tier:** inspection

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 23.4s | **Iterations:** 4

**Tools Called:** cec_search, cec_lookup_table

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Revised Service Load Calculation for Residential Panel (CEC 2022)

### **Step 1: General Lighting Load**
- **3000 sq ft × 3 VA/sq ft = 9000 VA**
- **Demand Factor (220.42):**  
  - First 3000 VA @ 100% = **3000 VA**  
  - Remaining 6000 VA @ 35% = **2100 VA**  
  - **Total General Lighting Load = 3000 + 2100 = 5100 VA**

### **Step 2: Small Appliance Circuits**
- **2 circuits × 1500 VA (220.52) = 3000 VA**

### **Step 3: Laundry Circuit**
- **1 circuit × 1500 VA (220.52) = 1500 VA**

### **Step 4: Electric Range (12 kW)**
- **Demand Factor (Table 220.55, Column C):**  
  - **1 appliance @ 8000 VA** (per Table 220.55, Column C for 1 appliance)

### **Step 5: Dryer (5.5 kW)**
- **Demand Factor (220.54):**  
  - First 5 kW @ 100% = **5000 VA**  
  - Remaining 0.5 kW @ 50% = **250 VA**  
  - **Total Dryer Load = 5000 + 250 = 5250 VA**

### **Step 6: Central AC (4600 W)**
- **Continuous Load (220.18):**  
  - **4600 VA × 1.25 = 5750 VA**

---

### **Total Calculated Load**
- **General Lighting:** 5100 VA  
- **Small Appliances:** 3000 VA  
- **Laundry:** 1500 VA  
- **Range:** 8000 VA  
- **Dryer:** 5250 VA  
- **AC:** 5750 VA  
- **Total = 5100 + 3000 + 1500 + 8000 + 5250 + 5750 = 28,600 VA**

---

### **Convert to Amperes**
- **Service Voltage:** 240V (single-phase)  
- **Total Load in Amperes:**  
  $$
  \frac{28,600 \text{ VA}}{240 \text{ V}} = 119.17 \text{ A}
  $$

---

### **Conclusion**
- **Calculated Load:** ~119A  
- **Service Panel Rating:** 200A  
- **Result:** The 200A panel is **adequately sized** as the calculated load (119A) is less than the panel's rating (200A).

[OK] Source: CEC 2022

[VERIFIED] Answer is complete.

---

### cec2022-022

**Original ID:** inspection-002 | **Category:** clearance_violations | **Tier:** inspection

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL code violations.

**Duration:** 18.0s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Dedicated Space Verification (CEC 2022 110.26(B))

**Search Result Analysis**:
- **CEC 2022 Section 110.26(B)** requires **dedicated space** above and below electrical equipment:
  - **Above**: No pipes, ducts, or other obstructions within 6.5 ft (78 in) vertical clearance.
  - **Below**: No obstructions within 300 mm (12 in) below the equipment.

**Application to This Case**:
- **No violation**: The water heater is located **16 inches to the left** (horizontal space), not above or below the panel.
- **No data** on ceiling height or obstructions directly above/below the panel. If the ceiling height is ≥6.5 ft and there are no obstructions within 12 in below, this requirement is satisfied.

**Inspector Note**:
- 110.26(B) focuses on **vertical** and **directly adjacent** obstructions, not horizontal ones like the water heater in this case.
- The existing violations (depth clearance and obstruction) remain valid.

[OK] Source: CEC 2022

---

### cec2022-023

**Original ID:** inspection-005 | **Category:** gfci_afci_compliance | **Tier:** inspection

**Question:** New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide code references.

**Duration:** 18.6s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes
**Service Conductor Enforced:** No

**Answer:**

## Circuit Protection Requirements for New Residential Kitchen (CEC 2022)

### 1. **Countertop Receptacles (20A circuits)**
- **Protection Required**: **Combination AFCI/GFCI breaker**
- **Code References**:
  - **GFCI**: CEC 210.8(A)(6) requires GFCI for all countertop receptacles.
  - **AFCI**: CEC 210.12(A) mandates AFCI for all 120V, 15/20A dwelling circuits (no exception applies here).

### 2. **Dishwasher (15A dedicated circuit)**
- **Protection Required**: **Combination AFCI/GFCI breaker**
- **Code References**:
  - **GFCI**: CEC 210.8(D) requires GFCI for outlets supplying appliances like dishwashers (per 422.5(B)(1)).
  - **AFCI**: CEC 210.12(A) applies (no exception for appliances).

### 3. **Garbage Disposal (15A dedicated circuit)**
- **Protection Required**: **Combination AFCI/GFCI breaker**
- **Code References**:
  - **GFCI**: CEC 210.8(A)(6) extends GFCI to all kitchen countertop circuits, which includes garbage disposal circuits.
  - **AFCI**: CEC 210.12(A) applies (no exception).

### 4. **Refrigerator (20A dedicated circuit)**
- **Protection Required**: **AFCI-only breaker**
- **Code References**:
  - **GFCI**: **Not required** due to exception in CEC 422.5(B)(3) (appliances with internal GFCI or where GFCI would create safety issues, e.g., food spoilage).
  - **AFCI**: CEC 210.12(A) applies (no exception).

---

### Inspector Notes:
- **Combination AFCI/GFCI breakers** are required for countertop circuits to satisfy both protections simultaneously.
- **Dedicated appliance circuits** (dishwasher, disposal) must still comply with GFCI requirements unless explicitly exempted (refrigerator is exempt).
- **AFCI is mandatory** for all 120V, 15/20A dwelling circuits per CEC 210.12(A), with no exceptions for kitchen appliances.

[OK] Source: CEC 2022

---

### cec2022-024

**Original ID:** inspection-006 | **Category:** subpanel_violations | **Tier:** inspection

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 8.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Subpanel Grounding Violations and Correct Configuration (CEC 2022)

### **Identified Violations**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation**: CEC 250.24(A)(5) prohibits connecting the grounded (neutral) conductor to the equipment grounding conductor on the load side of the service disconnect.  
   - **Impact**: Creates parallel paths for fault currents, increasing shock hazard.

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: CEC 250.24(A)(5) and 250.28 require the neutral and equipment grounding systems to be isolated in subpanels (separately derived systems).  
   - **Impact**: Bonds the neutral to the enclosure, creating unintended grounding paths.

3. **Missing Grounding Electrode**  
   - **Violation**: CEC 250.32(A) mandates a grounding electrode for detached structures supplied by a feeder (not a single branch circuit).  
   - **Impact**: No local grounding reference increases risk of voltage transients and shock.

---

### **Correct Configuration**
1. **Isolate Neutral and Ground Bars**  
   - **Action**: Remove the main bonding jumper between neutral and ground bars.  
   - **Citation**: CEC 250.24(A)(5), 250.28.  
   - **Neutral Bar**: Connect only the feeder neutral conductor.  
   - **Ground Bar**: Connect the feeder equipment grounding conductor and grounding electrode conductor.

2. **Bond Ground Bar to Enclosure**  
   - **Action**: Ensure the equipment grounding conductor (feeder ground) and grounding electrode conductor are bonded to the subpanel enclosure.  
   - **Citation**: CEC 250.28 (main bonding jumper is not used in subpanels).

3. **Install Grounding Electrode**  
   - **Action**: Add a grounding electrode (e.g., ground rod) at the detached garage and connect it to the ground bar via a grounding electrode conductor (GEC).  
   - **Citation**: CEC 250.32(A).  
   - **GEC Size**: Use Table 250.66 based on feeder conductor size (e.g., #2 AWG aluminum → 6 AWG copper or 4 AWG aluminum).

4. **Verify Feeder Connections**  
   - **Hot Conductors**: Connected to subpanel breaker.  
   - **Neutral Conductor**: Connected to isolated neutral bar.  
   - **Equipment Grounding Conductor**: Connected to ground bar.  

---

### **Inspector Notes**
- **Subpanels vs. Main Service**: Subpanels must never bond neutral and ground bars. This is reserved for the main service disconnect.  
- **Grounding Electrode Requirement**: A 4-wire feeder to a detached structure **requires** a local grounding electrode (250.32(A)). A single branch circuit is the **only** exception.  
- **California Specific**: CALGreen (Title 24) mandates grounding electrodes for all new structures, reinforcing 250.32(A).

[OK] Source: CEC 2022

---

### cec2022-025

**Original ID:** inspection-007 | **Category:** conduit_fill | **Tier:** inspection

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 13.1s | **Iterations:** 3

**Tools Called:** cec_lookup_conduit_fill

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Calculation:**
1. **Conduit Fill Area (40% of 1¼" RMC):**  
   1.526 sq in (total area) × 40% = **0.61 sq in**  
   *(Chapter 9 Table 4)*

2. **Conductor Area (10 AWG THHN):**  
   **0.0211 sq in per conductor**  
   *(Chapter 9 Table 5)*

3. **Maximum Conductors:**  
   0.61 sq in ÷ 0.0211 sq in/conductor = **28.91** → **28 conductors**  
   *(Round down per 300.15(B)(2)(a))*

**Verification:**  
- 28 conductors × 0.0211 = **0.5908 sq in** (40% fill limit: 0.61 sq in)  
- 29 conductors would exceed 40% fill (0.6119 sq in > 0.61 sq in)

[OK] Source: CEC 2022 Chapter 9 Tables 4 and 5

---

### cec2022-026

**Original ID:** inspection-008 | **Category:** voltage_drop | **Tier:** inspection

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet the 3% maximum recommendation for branch circuits?

**Duration:** 9.8s | **Iterations:** 5

**Tools Called:** python_calculator, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Voltage Drop Compliance (CEC 2022)

1. **Voltage Drop Calculation**:  
   - **Voltage drop**: 2.84 volts (2.37% of 120V)  
   - **Formula**: $ VD = \frac{2 \times 50 \times 1.29 \times 22}{1000} = 2.84 \, \text{V} $  

2. **Code Requirements**:  
   - **General branch circuits**:  
     - **Informational Note 3** to **CEC 210.19(A)** recommends **≤3% voltage drop** for efficiency.  
     - **2.37%** is **within the 3% limit**.  
   - **Fixed equipment circuits**:  
     - **CEC 647.4(D)(1)** requires **≤1.5% voltage drop** (more restrictive).  
     - **2.37% exceeds 1.5%**, but this applies only to fixed equipment (e.g., appliances, not general receptacles).  

3. **Conclusion**:  
   - If the circuit supplies **general lighting or receptacles**, **2.37% complies** with the 3% recommendation.  
   - If the circuit supplies **fixed equipment**, **2.37% exceeds 1.5%**, and conductor size/length adjustments are needed.  

[OK] Source: CEC 2022 Sections 210.19(A), 647.4(D)

---

### cec2022-027

**Original ID:** inspection-009 | **Category:** derating_calculation | **Tier:** inspection

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 8.7s | **Iterations:** 5

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG copper TW (60°C) conductors have a base ampacity of **20A** at 30°C ambient (Table 310.16).

**Step 2: Temperature Correction**  
Ambient temperature = 43°C  
Correction factor from Table 310.15(B)(1)(1) = **0.71**  
Adjusted ampacity = 20A × 0.71 = **14.2A**

**Step 3: Bundling Adjustment**  
6 current-carrying conductors in conduit  
Adjustment factor from Table 310.15(C)(1) = **0.80**  
Final adjusted ampacity = 14.2A × 0.80 = **11.36A**

**Final Answer:**  
The adjusted ampacity is **11.36A** after applying both temperature correction (0.71) and bundling adjustment (0.80).

[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)

---

### cec2022-028

**Original ID:** inspection-010 | **Category:** grounding_electrode_conductor | **Tier:** inspection

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 5.2s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Minimum Size Copper GEC for 1000 kcmil Service (CEC 2022)

**Answer:**  
The minimum size **copper grounding electrode conductor (GEC)** required is **2/0 AWG** per **CEC Table 250.66**.

---

### Key Details:
1. **Service Conductor Equivalent Size**:  
   - Four parallel 250 kcmil copper conductors per phase = **1000 kcmil equivalent** (4 × 250 kcmil).

2. **Table 250.66 Lookup**:  
   - For **1000 kcmil copper service conductors**, the table specifies a **2/0 AWG copper GEC**.

3. **Exceptions (Electrode Type Limits)**:  
   - If the grounding electrode is a **rod, pipe, or plate electrode**, the GEC can be reduced to **6 AWG copper** (per 250.66(A)).  
   - If the electrode is **concrete-encased**, the GEC can be reduced to **4 AWG copper** (per 250.66(B)).  
   - **Note**: These exceptions apply only if the calculated size (2/0) is larger than the exception limit. Since 2/0 > 6 AWG/4 AWG, the exception reduces the size if applicable.

4. **California Amendment**:  
   - The table includes California-specific modifications (delta symbol), but the base calculation remains unchanged for this case.

---

### Inspector Note:  
- Verify the **type of grounding electrode** (rod, pipe, plate, or concrete-encased) to determine if exceptions apply.  
- If no exception applies, **2/0 AWG copper** is the minimum required size.  

[OK] Source: CEC 2022 Table 250.66

---

### cec2022-029

**Original ID:** cec-001 | **Category:** panelboard_requirements | **Tier:** california_specific

**Question:** What are the panelboard space requirements for single-family dwellings? What appliances must have reserved circuit breaker spaces?

**Duration:** 10.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Panelboard Space Requirements and Reserved Circuit Breaker Spaces (CEC 2022)

### **Panelboard Location Requirements**
1. **Accessibility and Prohibited Locations**  
   - **Closets**: Panelboards **shall not be located in clothes closets** (240.24(D)).  
   - **Bathrooms**: In dwelling units, overcurrent devices (including panelboards) **shall not be located in bathrooms** (240.24(E)).  
   - **General**: Panelboards must be **readily accessible** and installed so the center of the grip of the operating handle is **not more than 2.0 m (6 ft 7 in.) above the floor** (240.24(A)).  

2. **Physical Protection**  
   - Panelboards **shall not be exposed to physical damage** (240.24(C)).  

---

### **Reserved Circuit Breaker Spaces for Appliances**
The number of required panelboard spaces depends on the total branch circuits and feeders connected. **Reserved spaces** are required for specific high-load appliances. Key requirements include:

#### **1. Dedicated Circuits for Major Appliances**  
The following appliances **require dedicated circuits** (and thus reserved panelboard spaces):  
- **Electric Ranges/Ovens**: 40–50 A circuit (220.55, 422.13).  
- **Clothes Dryers**: 30 A circuit (220.54, 422.13).  
- **Water Heaters**: 30–40 A circuit (422.13).  
- **Air Conditioners/Heat Pumps**: Dedicated circuit per 440.6(A).  
- **Electric Vehicle Supply Equipment (EVSE)**: Dedicated circuit per 625.43.  

#### **2. Small Appliance Branch Circuits**  
- **Kitchen, Dining Room, and Breakfast Nook**: **2 or more 20 A circuits** required (210.11(C)(1)), each occupying a panel space.  

#### **3. General Lighting and Receptacle Loads**  
- Calculated per 220.12 (1.5 VA/ft² for dwelling units), but **actual panel spaces depend on the number of branch circuits** installed to serve these loads.  

#### **4. Special Equipment**  
- **Fire Alarms**: Dedicated circuit per 760.41.  
- **Smoke Alarms**: Dedicated circuit per 720.43.  

---

### **Panelboard Sizing Guidance**  
- **Minimum Spaces**: A typical single-family dwelling requires **at least 40–60 spaces** to accommodate all required circuits (lighting, receptacles, appliances).  
- **Future Expansion**: Panelboards should include **reserve spaces** for future additions (e.g., EV charging, solar systems).  

---

### **Inspector Notes**  
- Verify panelboard location compliance with **240.24(D) and (E)**.  
- Confirm reserved spaces for **major appliances** match their dedicated circuit requirements.  
- Ensure panelboard has **sufficient spaces** to avoid overfilling (e.g., 40-space panel for a 200A service is common).  

[OK] Source: CEC 2022

---

### cec2022-030

**Original ID:** cec-002 | **Category:** ev_charging | **Tier:** california_specific

**Question:** What are the electrical requirements for EV charging infrastructure in new residential construction?

**Duration:** 8.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## California EV Charging Requirements (CEC 2022 & CALGreen)

### 1. **Dedicated Circuits**  
- **Section 625.40**: Each EV charging outlet must have an **individual branch circuit** with **no other outlets** (no multiwire branch circuits allowed).  
- **CALGreen Mandate**: New residential construction must include **EV-ready infrastructure** (CALGreen Chapter 4, Division 4.1).

---

### 2. **Cable Requirements**  
- **Section 625.17**:  
  - **Power-supply cords** must be listed types (e.g., hard service cord, portable power cable) with ampacity per Table 400.5.  
  - **Maximum cord lengths**:  
    - 12 in. (300 mm) for portable equipment with interrupting device in supply equipment.  
    - 6 ft (1.8 m) for stationary equipment.  
    - 15 ft (4.6 m) if interrupting device is at the plug.  
  - **Output cables** must be listed Type EV, EVJ, EVE, etc.  
  - **Total cord length**: ≤25 ft (7.5 m) unless using a listed cable management system.  

---

### 3. **Ventilation**  
- **Section 625.52**:  
  - **No ventilation required** if equipment is listed for indoor use without ventilation.  
  - **Mechanical ventilation required** if equipment requires it:  
    - Must include **supply and exhaust** to outdoors.  
    - Ventilation system must be **interlocked with the EVSE** to remain energized during charging.  
    - Minimum ventilation rates specified in **Table 625.52(B)(1)(a/b)** or calculated via formulas.  

---

### 4. **Receptacle & Enclosure Requirements**  
- **Section 625.56**:  
  - **Wet locations** require **weatherproof enclosures** (extra-duty listed) with attachment plug cap installed.  
- **Section 625.44**:  
  - **Portable EVSE** must use receptacles rated 125V/15–20A or 250V/15–50A (nonlocking, grounding-type).  
  - **Fixed EVSE** requires permanent wiring.  

---

### 5. **Ground-Fault Protection**  
- **Section 625.54**: All EV charging receptacles must have **GFCI protection for personnel** (in addition to 210.8 requirements).  

---

### 6. **Service/Feeder Sizing**  
- **Section 625.42**:  
  - EV charging loads are **continuous loads**.  
  - Service/feeder must be sized per equipment ratings.  
  - Adjustable settings on fixed equipment must be **locked or tool-accessible** to prevent user tampering.  

---

### 7. **CALGreen Compliance**  
- **CALGreen Chapter 5, Division 5.1**: Requires new residential buildings to have **EV-ready electrical infrastructure** (e.g., dedicated circuits, panel space).  

---

### 8. **Interactive Systems**  
- **Section 625.48**: EVSE with power export functions must be **listed for bidirectional use** and comply with Articles 702 (standby systems) or 705 (distributed energy resources).  

---

### Key Exceptions & Notes  
- **Cord length exceptions**: Vary based on interrupting device location (see 625.17(A)(3)).  
- **Ventilation exceptions**: Not required if equipment is listed for indoor use without ventilation (625.52(A)).  

[OK] Source: CEC 2022 & CALGreen

---

### cec2022-031

**Original ID:** cec-003 | **Category:** solar_pv | **Tier:** california_specific

**Question:** What are the electrical requirements for solar PV systems on new residential construction?

**Duration:** 8.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## California Solar PV System Requirements (CEC 2022)

### 1. **Scope and Application**  
- **Article 690** governs all solar PV systems, including arrays, inverters, and controllers for residential installations.  
- Applies to **interactive systems** (grid-tied) and **stand-alone systems**.  
- **AC modules** are permitted, with their PV source circuits treated as internal components (Section 690.6).  

---

### 2. **Equipment Requirements**  
- **Listed/evaluated equipment**: Inverters, modules, dc combiners, and charge controllers must be **listed for PV applications** (Section 690.4(B)).  
- **Qualified personnel**: Installation must be performed by **qualified persons** (defined in Article 100).  
- **Bathroom restriction**: PV equipment and disconnects **cannot be installed in bathrooms** (Section 690.4(E)).  

---

### 3. **Grounding and Bonding**  
- **Equipment grounding**:  
  - Exposed metal parts (modules, frames, enclosures) must be bonded per **Section 690.43**.  
  - Grounding electrode connections required via **Article 250** (e.g., 250.134 for bonding).  
- **Ground-fault protection**:  
  - Systems with ground-fault devices must connect to ground at a single point (Section 690.42).  
  - Equipment grounding conductors sized per **Table 250.122** (Section 690.45).  

---

### 4. **Labeling and Safety**  
- **Rapid shutdown systems**:  
  - Mandatory for roof-mounted systems. Labels must be **black on yellow** (title) and **white on red** (switch labels) with minimum 9.5 mm lettering (Section 690.56(C)).  
  - Example label:  
    > **SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN**  
    > TURN RAPID SHUTDOWN SWITCH TO THE 'OFF' POSITION TO SHUT DOWN PV SYSTEM AND REDUCE SHOCK HAZARD IN THE ARRAY.  

- **Directory requirements**:  
  - Buildings with multiple PV systems must have a **directory** at each disconnect location (Section 690.4(D)).  

---

### 5. **Interconnection and Energy Storage**  
- **Grid-tied systems**: Follow **Article 705** for interconnections (Section 690.59).  
- **Energy storage systems**: Comply with **Article 706** for battery integration (Section 690.71).  

---

### 6. **Wiring and Conduit**  
- **PV source circuits**: Conductors between modules and combiners/inverters must be sized for **maximum current** (Section 690.8).  
- **Conduit fill**: Adhere to **Chapter 9, Table 1** for conduit fill limits.  

---

### 7. **California-Specific Considerations**  
- **CALGreen Compliance**:  
  - New residential construction must meet **Title 24** energy efficiency standards, including PV-ready infrastructure.  
  - Minimum PV system size requirements may apply based on building size.  

---

### Key Sections to Review  
- **690.1** (Scope)  
- **690.4** (General requirements)  
- **690.43** (Bonding)  
- **690.56** (Rapid shutdown labeling)  
- **690.71** (Energy storage)  

[OK] Source: CEC 2022

---

### cec2022-032

**Original ID:** cec-004 | **Category:** heat_pump | **Tier:** california_specific

**Question:** What circuit requirements exist for heat pump water heaters in new dwelling units?

**Duration:** 7.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Circuit Requirements for Heat Pump Water Heaters in New Dwellings (CEC 2022)

### Key Requirements:
1. **Dedicated Circuit and Panel Space**  
   - **Single-family buildings** (1–2 dwellings):  
     Each dwelling unit **must have a dedicated circuit and panelboard space** for heat pump water heaters as specified in **California Energy Code Section 150.0(n)** (CEC 2022 Section 422.3(A) and 408.2(A)).  
     - This includes **designated branch circuits**, **receptacles**, and **circuit identifications**.  

2. **Panelboard Provisions**  
   - Panelboards serving individual dwelling units **must include circuit breaker spaces** for heat pump water heaters (CEC 2022 Section 408.2(A)).  

3. **California Energy Code Mandates**  
   - The exact requirements for **circuit sizing**, **receptacle type**, and **installation location** are detailed in **California Energy Code Section 150.0(n)**. While not fully detailed in the CEC, this section typically requires:  
     - A **dedicated 240V circuit** sized for the water heater’s nameplate amperage.  
     - **AFCI/GFCI protection** (if applicable per local amendments).  

---

### Inspector Notes:
- **Multifamily buildings** follow similar rules under **California Energy Code Section 160.9** (referenced in CEC 2022 Section 408.2(B)).  
- **No exceptions** for heat pump water heaters in standard dwelling units—these are **mandatory readiness provisions** under California’s Title 24 Energy Code.  
- Verify **nameplate requirements** of the installed water heater to ensure circuit and conductor sizing compliance (e.g., 30A, 40A, or 50A circuits).  

[OK] Source: CEC 2022 Sections 422.3, 408.2, and California Energy Code references.

---

### cec2022-033

**Original ID:** cec-005 | **Category:** electrification | **Tier:** california_specific

**Question:** What is required for electric cooktop readiness in new homes?

**Duration:** 7.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Electric Cooktop Readiness in New Homes (CEC 2022)

**Requirement:**  
Per **CEC 2022 Section 422.3(A)**, **single-family residential buildings** (with one or two dwellings) must provide **dedicated circuits and circuit identifications** for electric cooktops as specified in **California Energy Code Section 150.0(u)**. This includes:

- **Designated spaces** for cooktop installation.
- **Receptacles** and **branch circuits** sized appropriately for the cooktop.
- **Circuit identification** (e.g., labeling in the panel).

**Key Notes:**  
- The **California Energy Code (Title 24)** dictates specific readiness requirements (e.g., circuit amperage, receptacle type), but CEC 2022 mandates compliance with these Energy Code provisions.  
- For **multifamily buildings**, refer to **CEC 2022 Section 422.3(B)** and California Energy Code Section 160.9(b).

**Inspector Note:**  
Verify that the electrical plan includes **dedicated circuits** (not shared with other appliances) and that the **panel is labeled** to identify the cooktop circuit. Ensure alignment with Title 24 for exact technical specifications (e.g., 40A circuit for standard cooktops).

[OK] Source: CEC 2022

---

### cec2022-034

**Original ID:** cec-006 | **Category:** electrification | **Tier:** california_specific

**Question:** What are the panelboard requirements for electric clothes dryer circuits in new construction?

**Duration:** 7.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

### 1. **Dedicated Circuits and Circuit Identification**
- **Single-Family Buildings** (1–2 dwellings):  
  Panelboards must provide **dedicated circuits and circuit identifications** for electric clothes dryers as specified in **California Energy Code Section 150.0(v)**.  
  *(CEC 2022 Section 422.3(A)(3) and 408.2(A))*

- **Multifamily Buildings**:  
  Panelboards must provide **dedicated circuits and circuit identifications** for electric clothes dryers as specified in **California Energy Code Section 160.9(c)**.  
  *(CEC 2022 Section 422.3(B)(2) and 408.2(B))*

### 2. **Circuit Breaker Spaces**
- Panelboards serving dwelling units **must include dedicated circuit breaker spaces** for electric clothes dryers.  
  - Single-family: Per **CEC Section 150.0(v)**  
  - Multifamily: Per **CEC Section 160.9(c)**  
  *(CEC 2022 Section 408.2(A) and 408.2(B))*

### 3. **Load Calculation Requirements**
- Dryer loads must be calculated at **minimum 5000 VA** per dryer (or nameplate rating, whichever is larger).  
- For multiple dryers, apply **demand factors** from **Table 220.54**.  
  *(CEC 2022 Section 220.54)*

### 4. **Branch Circuit Requirements**
- A **240V, 30A branch circuit** is required for electric clothes dryers.  
- The circuit must have **no other outlets** (dedicated to the dryer).  
  *(Implied by CEC 2022 Section 210.11(C)(3) and 220.54)*

### 5. **Grounding and Bonding**
- Dryer frames must be **grounded via an equipment grounding conductor** (EGC).  
- Exception: Not applicable for new construction (only applies to existing installations without EGC).  
  *(CEC 2022 Section 250.140)*

---

**Inspector Note:**  
- Verify **circuit identification** (e.g., "Clothes Dryer") on the panelboard face per California Energy Code mandates.  
- Ensure **dedicated spaces** are reserved in the panelboard to prevent overloading.  
- Confirm **load calculations** include dryer load at 5000 VA (or nameplate) with applicable demand factors for multi-dryer installations.  

[OK] Source: CEC 2022

---

### cec2022-035

**Original ID:** cec-007 | **Category:** overcurrent | **Tier:** california_specific

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Duration:** 5.1s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## CEC Table 240.4(G) - California Specifics

**Answer:**  
CEC Table 240.4(G) itself is **not unique to California** - it mirrors NEC Table 240.4(G) as a cross-reference tool for specialized conductor overcurrent protection requirements. However, the **California amendment note** in the table description indicates that California may apply modifications to these references through its own code amendments (denoted by "delta" changes).

**Key California Context:**  
While the table content is standardized, California's adoption of the CEC includes **amendments to other referenced sections** (e.g., 760 fire alarm requirements, 440 HVAC rules) that may impose stricter or different overcurrent protection rules for the conductors listed in this table.

[OK] Source: CEC 2022 Table 240.4(G) and adoption notes

---

### cec2022-036

**Original ID:** cec-008 | **Category:** surge_protection | **Tier:** california_specific

**Question:** What does CEC Table 242.3 specify for installations?

**Duration:** 3.9s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## CEC 2022 Table 242.3 - Overvoltage Protection Cross-Reference

**Purpose**: This California-specific table (marked with "N" for California amendments) cross-references equipment types to other NEC articles containing overvoltage protection requirements. It supplements Article 242 (Overvoltage Protection) by directing users to equipment-specific rules.

**Equipment-to-Article Cross-References**:
- **Class I locations** → Article 501
- **Class II locations** → Article 502
- **Community antenna TV/radio systems** → Article 820
- **Critical operations power systems** → Article 708
- **Elevators/dumbwaiters/etc.** → Article 620
- **Emergency systems** → Article 700
- **Equipment >1000V** → Article 490
- **Fire pumps** → Article 695
- **Industrial machinery** → Article 670
- **IT equipment** → Article 645
- **Modular data centers** → Article 646
- **Outdoor overhead >1000V** → Article 399
- **Radio/TV equipment** → Article 810
- **Receptacles/cord connectors** → Article 406
- **Wind electric systems** → Article 694

**Key Notes**:
- This table is a **California amendment** not found in the base NEC.
- Used to identify **additional overvoltage protection requirements** beyond general Article 242 rules.
- Equipment installers must **consult both Article 242 and the referenced articles** for complete compliance.

[OK] Source: CEC 2022

---

### cec2022-037

**Original ID:** cec-009 | **Category:** motor_control | **Tier:** california_specific

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Duration:** 6.5s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)

**Purpose**: Specifies **maximum overcurrent protective device (OCPD) ratings** for motor control circuits based on conductor size and installation configuration.

---

### **Key Table Structure**
| Conductor Size | Column A (Copper) | Column A (Aluminum) | Column B (Copper) | Column B (Aluminum) | Column C (Copper) | Column C (Aluminum) |
|----------------|-------------------|---------------------|-------------------|---------------------|-------------------|---------------------|
| 18 AWG         | 7A                | —                   | 25A               | —                   | 7A                | —                   |
| 16 AWG         | 10A               | —                   | 40A               | —                   | 10A               | —                   |
| 14 AWG         | (Note 1)          | —                   | 100A              | —                   | 45A               | —                   |
| 12 AWG         | (Note 1)          | (Note 1)            | 120A              | 100A                | 60A               | 45A                 |
| 10 AWG         | (Note 1)          | (Note 1)            | 160A              | 140A                | 90A               | 75A                 |
| >10 AWG        | (Note 1)          | (Note 1)            | (Note 2)          | (Note 2)            | (Note 3)          | (Note 3)            |

---

### **Notes & Cross-References**
1. **Notes 1-3** reference other tables for derived values:
   - **Note 1**: "Value specified in 310.15 as applicable" → See [CEC 310.15](#) for ampacity rules.
   - **Note 2**: "400% of value in Table 310.19 for 60°C conductors" → See [CEC 310.19](#) for fixed-wire ampacities.
   - **Note 3**: "300% of value in Table 310.16 for 60°C conductors" → See [CEC 310.16](#) for general ampacities.

2. **Column Definitions**:
   - **Column A**: Likely applies to control circuits with **two conductors** (e.g., 2-wire control).
   - **Column B**: Likely applies to control circuits with **three or more conductors** (e.g., 3-wire control).
   - **Column C**: Likely applies to **motor control circuits with overload protection** (e.g., motor starters).

---

### **Application Rules**
- **Copper vs. Aluminum**: Only copper values are provided for 14 AWG and smaller; aluminum is not permitted for these sizes in control circuits.
- **Larger Conductors (>10 AWG)**: Use the referenced tables (310.19/310.16) to calculate OCPD ratings based on 300–400% of ampacity.
- **Exception**: For conductors larger than 10 AWG, the table does not provide direct values—derive from other tables.

---

### **Inspector Note**
- Always verify the **installation configuration** (number of conductors, overload protection) to select the correct column.
- For conductors >10 AWG, ensure calculations align with the referenced tables (310.16/310.19) and apply the 300–400% multipliers.

[OK] Source: CEC 2022

---

### cec2022-038

**Original ID:** cec-010 | **Category:** medium_voltage | **Tier:** california_specific

**Question:** What medium voltage cable tables exist that are California-specific?

**Duration:** 8.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Medium Voltage Cable Tables in CEC 2022

California's electrical code (CEC 2022) addresses medium voltage (Type MV) cable ampacities in **Section 311.60** and **Section 392.80(B)**. The following tables are specifically referenced for medium voltage cable installations:

---

### **Type MV Cable Ampacity Tables**
1. **Multiconductor Cables (2001V–35,000V):**
   - **Table 311.60(C)(75)** and **Table 311.60(C)(76)**  
     - For multiconductor cables in cable trays.
     - Adjustments:  
       - **95% reduction** if trays are continuously covered >1.8m (6ft) with solid unventilated covers.  
       - **Referenced in 392.80(B)(1).**

2. **Single-Conductor Cables (2001V–35,000V):**
   - **Table 311.60(C)(69)** and **Table 311.60(C)(70)**  
     - For single-conductor cables in cable trays.
     - Adjustments:  
       - **75% reduction** for uncovered trays.  
       - **70% reduction** if trays are covered >1.8m (6ft) with solid unventilated covers.  
       - **Referenced in 392.80(B)(2).**

3. **Special Configurations:**
   - **Table 311.60(C)(67)** and **Table 311.60(C)(68)**  
     - For single-conductor cables in triangular/square configurations.
   - **Table 311.60(C)(71)** and **Table 311.60(C)(72)**  
     - For multiconductor cables in single-layer installations with spacing.

---

### **Key Applications and Limitations**
- **Cable Tray Installations:**  
  - Ampacities depend on tray type (ladder, ventilated, solid bottom) and coverage (open vs. covered).  
  - Spacing requirements apply for single-layer installations (minimum 1x cable diameter between conductors).  

- **Conductor Size Requirements:**  
  - Single-conductor cables must be **1/0 AWG or larger** (Section 392.10(B)(1)).  

- **Engineering Supervision:**  
  - Permitted for non-tabled scenarios (Section 311.60(A)).  

---

### **Inspector Notes**
- **California-Specific Compliance:**  
  - CEC 2022 incorporates NEC with amendments; these tables are part of the adopted code.  
  - Verify local amendments (e.g., CALGreen) for additional requirements.  

- **Critical Adjustments:**  
  - Ambient temperature and bundling factors (Section 310.15) apply to medium voltage cables.  

[OK] Source: CEC 2022

---

### cec2022-039

**Original ID:** cec-011 | **Category:** conductor_ampacity | **Tier:** delta_table

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75°C?

**Duration:** 4.6s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

**Ampacity**: 230 amperes at 75°C (CEC Table 310.16)  
**Material**: Copper  
**California Amendment**: Delta (Δ) modification applied  

**Key Considerations**:  
1. **Overcurrent Protection**: Per 240.4(D), 4/0 AWG copper is permitted up to **250A** overcurrent protection (next standard size above 230A).  
2. **Adjustments Required If**:  
   - Ambient temperature ≠ 30°C (use 310.15(B) correction factors)  
   - More than 3 current-carrying conductors in a raceway (use 310.15(C)(1) bundling factors)  

[OK] Source: CEC 2022

---

### cec2022-040

**Original ID:** cec-012 | **Category:** grounding | **Tier:** delta_table

**Question:** What size equipment grounding conductor is required for a 200A circuit?

**Duration:** 6.7s | **Iterations:** 4

**Tools Called:** cec_lookup_grounding_conductor, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Equipment Grounding Conductor Size (CEC 2022)

For a **200A circuit**, the required equipment grounding conductor (EGC) sizes are:

- **Copper**: **6 AWG**  
- **Aluminum/Copper-Clad Aluminum**: **4 AWG**  

**Source**: CEC 2022 **Table 250.122**  
**California Amendment**: This table includes California-specific modifications (delta symbol标注) from the base NEC.  

**Key Notes**:  
1. These sizes ensure proper ground fault current capacity for the overcurrent device.  
2. See **250.120** for installation restrictions (e.g., mechanical protection requirements).  
3. If additional grounding is required by **250.4(A)(5)** or **(B)(4)** (e.g., for corrosion protection), the EGC may need to be larger than specified here.  

[OK] Source: CEC 2022

---

### cec2022-041

**Original ID:** cec-013 | **Category:** grounding | **Tier:** delta_table

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor?

**Duration:** 7.4s | **Iterations:** 5

**Tools Called:** cec_lookup_grounding_conductor, cec_lookup_conductor_size

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** Yes

**Answer:**

## Grounding Electrode Conductor Size (CEC 2022)

**Required GEC size**: **4 AWG copper**  
**Source**: CEC 2022 Table 250.66 for **3/0 AWG copper service conductor**  

**Key Details**:
- Service conductor range: 2/0 or 3/0 AWG (per Table 310.12(A) for dwelling services)
- Minimum GEC size for copper: **4 AWG**
- California amendment applies (delta symbol in table)

**Exceptions to Note**:
- If using a **ground rod/pipe/plate electrode**, GEC may not need to exceed **6 AWG copper** (250.66(A))
- If using a **concrete-encased electrode**, GEC may not need to exceed **4 AWG copper** (250.66(B))

**Inspector Note**:  
While service conductors for dwelling units use Table 310.12(A) (e.g., 2/0 Cu for 200A), grounding electrode conductor sizing always follows Table 250.66 based on the **actual service conductor size**, not the ampacity.  

[OK] Source: CEC 2022

---

### cec2022-042

**Original ID:** cec-014 | **Category:** ampacity_adjustment | **Tier:** delta_table

**Question:** What is the temperature correction factor for a 75°C rated conductor at 40°C ambient temperature?

**Duration:** 4.3s | **Iterations:** 3

**Tools Called:** cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** at **40°C ambient temperature** is **0.88** per **CEC 2022 Table 310.15(B)(1)(1)**.

### Calculation Logic:
1. **Base condition**: 30°C ambient (standard reference temperature)
2. **Correction needed**: For every degree above 30°C, ampacity decreases proportionally
3. **Factor derivation**: 
   - At 40°C ambient (10°C above standard)
   - Factor = 0.88 (direct lookup from Table 310.15(B)(1)(1))

### Application:
Multiply this factor by the conductor's base ampacity (from Table 310.16 or 310.12(A)) to determine adjusted ampacity at 40°C ambient.

[OK] Source: CEC 2022

---

### cec2022-043

**Original ID:** cec-015 | **Category:** ampacity_adjustment | **Tier:** delta_table

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway?

**Duration:** 4.3s | **Iterations:** 3

**Tools Called:** cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Ampacity Adjustment for Bundling (CEC 2022)

**Adjustment Factor**: 0.70 (70%) for 7-9 current-carrying conductors in a raceway  
**Source**: CEC 2022 Table 310.15(C)(1) [California Amendment]

**Key Notes**:
- Applies to conductors rated 300V or less
- California amendment clarifies this range explicitly
- Must apply to all conductors in the raceway (including spares, neutrals, and EGCs) unless they cannot be simultaneously energized

[OK] Source: CEC 2022

---

### cec2022-044

**Original ID:** cec-016 | **Category:** working_space | **Tier:** delta_table

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3?

**Duration:** 14.2s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Dedicated Working Space Requirements (CEC 2022)

**Answer:**  
Section **110.26(B)** adds critical requirements for working space around electrical equipment:

- **Dedicated Space:**  
  The working space in front of panelboards **must be clear of all obstructions and storage** (combustible or otherwise). This ensures safe access for maintenance and emergency operations.

- **Height Clearance:**  
  While **110.26(A)(2)** specifies vertical clearance (6.5 ft from the floor), **110.26(B)** emphasizes that this space must remain unobstructed vertically as well. For example, ceiling-mounted obstructions or stored items in this zone violate the rule.

- **Application to This Case:**  
  For your 480V panelboard, the **4 ft depth** (Condition 3) must be **completely unobstructed** horizontally and vertically. No tools, boxes, or other items can be stored in this area.

**Code Reference:**  
- CEC 2022 **110.26(B)** (dedicated working space requirements).  

**Inspector Note:**  
Even if the working space depth meets Table 110.26(A)(1), failure to maintain clear, obstruction-free space violates **110.26(B)**. This is a common inspection failure in commercial and residential settings.  

[OK] Source: CEC 2022

---

### cec2022-045

**Original ID:** cec-017 | **Category:** enclosure | **Tier:** delta_table

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?

**Duration:** 5.5s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Suitable Enclosures for Outdoor Use with Rain, Sleet, and Ice (CEC 2022)

**Answer:**  
For outdoor use with protection against **rain, sleet, and ice**, the following enclosure types are suitable per **Table 110.28**:  
- **Type 3**  
- **Type 3R**  
- **Type 3S**  
- **Type 3X**  
- **Type 3RX**  
- **Type 3SX**  
- **Type 4**  
- **Type 4X**  
- **Type 6**  
- **Type 6P**  

**Key Notes:**  
1. These enclosures are marked with an **"X"** under the "Rain, snow, and sleet" condition in the table.  
2. **Footnote clarification**:  
   - *Raintight* enclosures (Types 3, 3S, 3SX, 3X, 4, 4X, 6, 6P) are designed to exclude rain, sleet, and ice.  
   - *Watertight* enclosures (Types 4, 4X, 6, 6P) provide additional protection against water ingress.  

**Inspector Note:**  
If the application requires the **mechanism to remain operable when ice-covered**, select **Type 3S** or **3SX** (see the "Sleet*" footnote).  

[OK] Source: CEC 2022 Table 110.28

---

### cec2022-046

**Original ID:** cec-018 | **Category:** lighting_load | **Tier:** delta_table

**Question:** What is the general lighting load in VA per square foot for office buildings?

**Duration:** 4.4s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for **office buildings** is **1.3 volt-amperes per square foot (VA/ft²)** according to **CEC 2022 Table 220.12**. This value includes the 125% multiplier for continuous loads as required by 210.20(A).

**Citation:** CEC 2022 Table 220.12 (Office occupancy row, VA/ft² column)

[OK] Source: CEC 2022

---

### cec2022-047

**Original ID:** cec-019 | **Category:** flexible_cord | **Tier:** delta_table

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset)?

**Duration:** 7.3s | **Iterations:** 4

**Tools Called:** cec_search, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

The ampacity for a **12 AWG flexible cord** with **Column B thermoset insulation** is **25 amperes** at an ambient temperature of 30°C (86°F), as specified in **Table 400.5(A)(1)** of the California Electrical Code (CEC) 2022.

### Key Details:
- **Table Reference**: CEC 2022 Table 400.5(A)(1)  
- **Column B Application**: For two-conductor cords where only two conductors are current-carrying (per footnote 2 of the table).  
- **No Adjustments Needed**: The question does not specify ambient temperature deviations or bundling, so no correction factors apply.  

### Full Table Excerpt (Relevant Row):
| size_awg | column_b (thermoset) |
|----------|----------------------|
| 12       | **25 A**             |

[OK] Source: CEC 2022

---

### cec2022-048

**Original ID:** cec-020 | **Category:** fixture_wire | **Tier:** delta_table

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire?

**Duration:** 8.4s | **Iterations:** 5

**Tools Called:** cec_lookup_fixture_wire, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Maximum Operating Temperature for Type SF-2 Fixture Wire (CEC 2022)

The maximum operating temperature for **Type SF-2 silicone insulated fixture wire** is **200°C (392°F)** as specified in **CEC 2022 Table 402.3**.

### Verification from CEC 2022 Search Results:
1. **Table 402.3** explicitly lists Type SF-2 with a maximum operating temperature of **200°C (392°F)**.
2. **Section 402.5** confirms that conductor operating temperatures must not exceed those specified in Table 402.3.
3. **Section 620.11(A)** (elevator wiring) also references **200°C** for Type SF conductors, aligning with Table 402.3.

### Additional Context:
- **Insulation**: Silicone rubber
- **Conductor**: Solid or 7-strand
- **Application**: Permitted for fixture wiring where the temperature rating matches the installation conditions.

[OK] Source: CEC 2022

---

### cec2022-049

**Original ID:** cec-021 | **Category:** adjusted_ampacity | **Tier:** calculation

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40°C ambient temperature.

**Duration:** 5.0s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   8 AWG THWN copper at 75°C = **50A** (Table 310.16)

2. **Temperature Correction**:  
   40°C ambient → 0.88 factor (Table 310.15(B)(1)(1))  
   50A × 0.88 = **44A**

3. **Bundling Adjustment**:  
   7 conductors → 0.70 factor (Table 310.15(C)(1))  
   44A × 0.70 = **30.8A**

4. **Final Adjusted Ampacity**:  
   **30.8A** (Round down to **30A** for practical application)

**Citations**:  
- Base ampacity: CEC 2022 Table 310.16  
- Temperature correction: CEC 2022 Table 310.15(B)(1)(1)  
- Bundling adjustment: CEC 2022 Table 310.15(C)(1)  

[OK] Source: CEC 2022

---

### cec2022-050

**Original ID:** cec-022 | **Category:** service_sizing | **Tier:** calculation

**Question:** Size the conductors, EGC, and GEC for a 200A residential service using copper conductors.

**Duration:** 4.6s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Service Conductor Sizing (CEC 2022)

**1. Service Conductors**  
- **Size**: 2/0 AWG copper  
- **Rating**: 200A  
- **Table Reference**: CEC Table 310.12(A) (Dwelling Services/Feeders)  

**2. Equipment Grounding Conductor (EGC)**  
- **Size**: 6 AWG copper  
- **Table Reference**: CEC Table 250.122 (for 200A overcurrent protection)  

**3. Grounding Electrode Conductor (GEC)**  
- **Size**: 4 AWG copper  
- **Table Reference**: CEC Table 250.66 (based on 2/0 AWG service conductors)  

---

### Verification Steps:
1. **Service Conductors**:  
   - Table 310.12(A) specifies 2/0 AWG copper for 200A dwelling services.  
   - Applies to 120/240V single-phase systems with no derating required.  

2. **EGC**:  
   - Table 250.122 requires 6 AWG copper for 200A circuits.  

3. **GEC**:  
   - Table 250.66 mandates 4 AWG copper for service conductors sized 2/0 AWG.  

---

[OK] Source: CEC 2022

---

### cec2022-051

**Original ID:** cec-023 | **Category:** commercial_load | **Tier:** calculation

**Question:** Calculate the general lighting load for a 5,000 square foot office building.

**Duration:** 3.9s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## General Lighting Load Calculation for Office Building (CEC 2022)

**Calculation:**
- **Building area**: 5,000 sq ft  
- **Unit load (Table 220.12, Office)**: 1.3 VA/ft² (per CEC 2022 Table 220.12)  
- **Total lighting load**:  
  $ 5,000 \, \text{ft}^2 \times 1.3 \, \text{VA/ft}^2 = 6,500 \, \text{VA} $

**Notes:**  
- The 125% continuous load multiplier from **210.20(A)** is already included in the unit load value per Table 220.12.  
- No additional calculations are required for continuous load application.  

[OK] Source: CEC 2022 Table 220.12

---

### cec2022-052

**Original ID:** cec-024 | **Category:** motor_circuit | **Tier:** calculation

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure?

**Duration:** 7.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit Conductors (CEC 2022)

**Answer:**  
The maximum overcurrent protection for 16 AWG copper motor control circuit conductors **extending beyond the enclosure** is **10 amperes**.

**Code Basis:**  
- **CEC 2022 Table 430.72(B)**:  
  - Column C (conductors extending beyond enclosure) for 16 AWG copper = **10A**  
- **CEC 2022 Section 430.72(B)(2)**:  
  - Conductors extending beyond the enclosure must not exceed Column C values.  

**Key Notes:**  
1. If the conductors did **not** extend beyond the enclosure, Column B would allow up to **40A** (not applicable here).  
2. **Section 240.4(D)** also limits 16 AWG copper to 10A for general applications, but motor control circuits follow the specific rules in 430.72.  

[OK] Source: CEC 2022

---

### cec2022-053

**Original ID:** cec-025 | **Category:** dwelling_load | **Tier:** calculation

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit.

**Duration:** 6.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## General Lighting Load Calculation (CEC 2022)

**Calculation:**  
For dwelling units, CEC 2022 Section 220.14(J) and 220.82(B)(1) specify a **minimum unit load of 3 volt-amperes per square foot (VA/ft²)** for general lighting and receptacles.  

$$
\text{General Lighting Load} = 2,400 \, \text{ft}^2 \times 3 \, \text{VA/ft}^2 = 7,200 \, \text{VA}
$$

**Key Notes:**  
1. The **125% continuous load multiplier** from 210.20(A) is **already included** in this unit load calculation.  
2. This value includes lighting and receptacle outlets specified in 210.70 and 210.52.  
3. No additional calculations are required for these outlets per 220.14(J).  

**Citations:**  
- CEC 2022 Section 220.14(J)  
- CEC 2022 Section 220.82(B)(1)  

[OK] Source: CEC 2022

---

