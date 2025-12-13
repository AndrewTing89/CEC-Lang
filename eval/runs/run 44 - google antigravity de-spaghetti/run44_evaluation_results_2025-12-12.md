# CEC 2022 Unified Evaluation Results - Run 44

**Date:** 2025-12-12
**Description:** Google antigravity de-spaghetti

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 53 |
| Successful | 53 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 387.0s |
| Avg Duration | 7.3s |
| Reflection Used | 53/53 |
| Reflection Improved | 3/53 |
| Hint Enforcement | 0/53 |
| Protection Enforcement | 0/53 |
| Service Conductor Enforcement | 0/53 |

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

**Duration:** 5.5s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Ampacity of 12 AWG Copper Conductor (CEC 2022)

**Ampacity**: 25 amperes at 75°C (Table 310.16)  
**Overcurrent Protection Limit**: 20A maximum (Section 240.4(D))  

**Key Conditions**:  
- Ambient temperature: 30°C (86°F)  
- Up to 3 current-carrying conductors in raceway/cable  

**Inspector Note**:  
While the conductor has a 25A ampacity, **240.4(D) limits 12 AWG copper to 20A overcurrent protection**. This is a critical distinction - the ampacity determines the conductor's capacity, but the overcurrent device must follow the smaller value in 240.4(D).  

**Footnotes to Apply**:  
1. For ambient temperatures ≠ 30°C, apply correction factors from **310.15(B)**  
2. For >3 conductors, apply bundling adjustments from **310.15(C)(1)**  
3. For California amendments, see **delta notes** in Table 310.16  

[OK] Source: CEC 2022

---

### cec2022-002

**Original ID:** baseline-002 | **Category:** table_lookup | **Tier:** baseline

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 5.5s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Conductor Size for 60A Circuit (CEC 2022)

**Minimum conductor size**: **6 AWG copper**  
- **Ampacity**: 65A (Table 310.16 at 75°C)  
- **Overcurrent protection**: 60A maximum (per 240.4(D) limitations)  

**Key Code References**:  
1. **Ampacity**: CEC Table 310.16 confirms 6 AWG copper has 65A ampacity at 75°C.  
2. **OCP Limit**: 240.4(D) restricts 6 AWG copper to **60A maximum overcurrent protection**.  

**Inspector Note**:  
- A 60A breaker is required for a 60A circuit.  
- 6 AWG conductor is the **smallest permitted** for this application (8 AWG only provides 50A).  
- No derating needed unless ambient temperature >30°C or >3 current-carrying conductors in a raceway (per footnotes 1 and 2).  

[OK] Source: CEC 2022

---

### cec2022-003

**Original ID:** baseline-003 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 22.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**Requirement:**  
All 125-volt through 250-volt receptacles installed in **kitchens** to serve **countertop surfaces** must have **ground-fault circuit-interrupter (GFCI) protection** for personnel.  

**Code Reference:**  
- **CEC 2022 Section 210.8(A)(6)**:  
  *"Kitchens - where the receptacles are installed to serve the countertop surfaces."*  

**Key Details:**  
- Applies to **dwelling units** (residential) supplied by single-phase branch circuits rated **150 volts or less to ground**.  
- Covers **all receptacles** serving countertop workspaces, including those for small appliances (e.g., blenders, toasters).  

**Exceptions (Not Applicable for Standard Kitchens):**  
- Listed locking receptacles for ceiling luminaires/ceiling fans (if GFCI protection is not required for the luminaire itself).  

**Inspector Note:**  
- This requirement does **not** extend to receptacles in laundry areas, sink areas (covered under separate rules), or other kitchen-specific locations unless explicitly stated.  

[OK] Source: CEC 2022

---

### cec2022-004

**Original ID:** baseline-004 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 6.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for all 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets or devices in bedrooms of new residential construction. This requirement is explicitly stated in **CEC 2022 Section 210.12(A)** for dwelling units.

### Key Details:
- **Required Protection Methods**:  
  - Combination-type AFCI at the circuit origin (most common).  
  - Branch/feeder-type AFCI combined with outlet AFCI at the first outlet.  
  - Supplemental arc protection circuit breaker with outlet AFCI (under specific conditions).  

- **Exceptions**:  
  - Does not apply to fire alarm systems (760.41(B)/760.121(B)).  
  - No exception for standard bedroom circuits.  

- **Applicability**:  
  - Covers **all bedrooms** in dwelling units.  
  - Applies to **new construction** and **modifications/extensions** of existing circuits in bedrooms.  

[OK] Source: CEC 2022 Section 210.12(A)

---

### cec2022-005

**Original ID:** baseline-005 | **Category:** table_lookup | **Tier:** baseline

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 7.5s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Answer:**  
Yes, aluminum conductors can be used for a 200A dwelling service. The required size is **4/0 AWG aluminum** per **CEC Table 310.12(A)**.

**Key Details:**  
- **Table Reference:** CEC 2022 Table 310.12(A) (Dwelling Service/Feeder Conductors)  
- **Conditions:**  
  - Applies to 120/240V or 120/208Y single-phase systems.  
  - No temperature correction or bundling adjustments required.  
  - Conductors supply the **entire load** of the dwelling unit.  

**Inspector Note:**  
If adjustments (e.g., high ambient temperature, multiple conductors in raceway) are required, use **Table 310.16** for adjusted sizing. For standard installations without derating, Table 310.12(A) provides the minimum size.  

[OK] Source: CEC 2022

---

### cec2022-006

**Original ID:** baseline-006 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 4.8s | **Iterations:** 3

**Tools Called:** cec_lookup_working_space

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Minimum Working Clearance Depth (CEC 2022)

The **minimum depth of working clearance** required in front of a 120/240V residential electrical panel is:

**3.0 feet (900 mm)** per **CEC Table 110.26(A)(1), Condition 1** for systems with voltage to ground ≤ 150V.

### Key Details:
- **Voltage range**: 0–150 volts to ground (applies to standard 120/240V residential systems)
- **Condition 1**: Working space with exposed live parts on one side and grounded parts on the other (typical for residential panels)
- **Vertical clearance**: 6.5 feet (78 inches) above the floor is also required per **110.26(A)(2)**, but this is separate from the horizontal depth requirement

### Code Citations:
- **Depth**: CEC 2022 Table 110.26(A)(1)
- **Vertical clearance**: CEC 2022 110.26(A)(2)

[OK] Source: CEC 2022

---

### cec2022-007

**Original ID:** baseline-007 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 6.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Answer:**  
A minimum of **two 20-ampere small-appliance branch circuits** are required for the kitchen area in a dwelling unit.

**Code Basis:**  
- **CEC 210.11(C)(1):** Requires at least two 20-ampere small-appliance branch circuits to supply receptacle outlets in the kitchen, pantry, and dining room.  
- **CEC 220.52(A):** Specifies a 1500 VA load calculation per circuit for these branch circuits, but the **minimum number of circuits is determined by 210.11(C)(1)**.  

**Key Notes:**  
- The two circuits must serve the kitchen, pantry, and dining room areas.  
- This requirement applies regardless of the number of receptacles or square footage.  
- The 1500 VA per circuit value is used for service/feeder load calculations (not the number of circuits).  

[OK] Source: CEC 2022

---

### cec2022-008

**Original ID:** baseline-008 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Is surge protection required for a new 200A residential service?

**Duration:** 5.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is **required** for a new 200A residential service per **CEC 2022 Section 230.67(A)**.  

**Key Requirements:**  
1. **Mandatory SPD**: All services supplying dwelling units must include a **surge-protective device (SPD)**.  
2. **SPD Type**: Must be **Type 1 or Type 2** SPD (Section 230.67(C)).  
3. **Location**:  
   - Integral to service equipment, or  
   - Immediately adjacent to it (Section 230.67(B)).  
   - *Exception*: SPD may be installed at downstream distribution equipment if no other location is feasible.  

**Inspector Note:**  
This requirement applies to **all new residential services** in California. Verify the SPD is listed for the application and installed per manufacturer instructions.  

[OK] Source: CEC 2022 Section 230.67

---

### cec2022-009

**Original ID:** core-001 | **Category:** multi_article | **Tier:** core

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 14.8s | **Iterations:** 5

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size, cec_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Service Conductor Sizing (CEC 2022)

**Required Service Conductor Size for 200A Dwelling Service:**
- **Copper**: 2/0 AWG (75°C column, Table 310.12(A))
- **Aluminum**: 4/0 AWG (75°C column, Table 310.12(A))

**Key Code Requirements:**
1. **Table 310.12(A)** applies specifically to dwelling services and feeders where:
   - No temperature correction or adjustment factors are required
   - Conductors supply the entire load of the dwelling unit
   - System is 120/240V or 120/208Y single-phase

2. **Aluminum Use Permitted**: Yes, aluminum conductors are explicitly allowed for dwelling services per Table 310.12(A) columns.

3. **Inspector Note**: If temperature correction factors (e.g., high ambient temperature) or bundling adjustments apply, recalculate using Table 310.16 and apply correction factors from 310.15(B)(1)(1) and 310.15(C)(1).

[OK] Source: CEC 2022

---

### cec2022-010

**Original ID:** core-002 | **Category:** multi_article | **Tier:** core

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the requirements for the circuit breaker and neutral termination?

**Duration:** 8.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Multiwire Branch Circuit Requirements (CEC 2022)

### Circuit Breaker Requirements:
1. **Simultaneous Disconnection** (210.4(B)):  
   - All ungrounded conductors (hot wires) must be disconnected simultaneously using **handle-tied single-pole circuit breakers** (240.15(B)(1)).  
   - This prevents the neutral from becoming energized if only one hot leg is disconnected.  

2. **Breaker Rating**:  
   - For 12 AWG copper conductors (12/3 cable), the maximum overcurrent protection is **20A** (240.4(D)).  

---

### Neutral Termination Requirements:
1. **Neutral Continuity** (210.4(D) & 200.4(B)):  
   - The grounded (neutral) conductor must remain **uninterrupted** and connected directly to the panel’s neutral bus.  
   - **No switches or disconnects** are permitted on the neutral conductor of a multiwire branch circuit.  

2. **Load Balance**:  
   - The neutral carries the **difference in current** between the two hot legs. For kitchen receptacles, ensure balanced loads to minimize neutral current.  

---

### Key Code Citations:
- **210.4(B)**: Requires simultaneous disconnection of all ungrounded conductors.  
- **210.4(D)**: Neutral conductor must be grouped with ungrounded conductors.  
- **240.15(B)(1)**: Handle-tied breakers for MWBCs serving line-to-neutral loads.  
- **240.4(D)**: OCP limit for 12 AWG conductors (20A maximum).  

[OK] Source: CEC 2022

---

### cec2022-011

**Original ID:** core-003 | **Category:** knowledge | **Tier:** core

**Question:** Where is GFCI protection required in a residential dwelling? List all locations.

**Duration:** 8.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## GFCI Protection Required Locations in Residential Dwellings (CEC 2022)

**All 125V–250V receptacles in the following locations require GFCI protection per [CEC 210.8(A)](https://up.codes/2022-cec/article-210#210.8):**

1. **Bathrooms**  
   - **210.8(A)(1)**  
   - *Exception:* Locking receptacles for ceiling fans/luminaires may omit GFCI if the general-purpose receptacle is GFCI-protected.

2. **Garages and Accessory Buildings**  
   - **210.8(A)(2)**  
   - Applies to buildings with floors at/below grade (storage/work areas only).

3. **Outdoors**  
   - **210.8(A)(3)**  
   - *Exception:* Receptacles for snow-melting/deicing systems (per 426.28/427.22) may omit GFCI if not readily accessible.

4. **Crawl Spaces (at/below grade)**  
   - **210.8(A)(4)**  

5. **Basements**  
   - **210.8(A)(5)**  
   - *Exception:* Receptacles for fire alarm systems (per 760.41/760.121) may omit GFCI.

6. **Kitchens – Countertop Surfaces**  
   - **210.8(A)(6)**  

7. **Sinks**  
   - **210.8(A)(7)**  
   - Receptacles within 6 ft (1.8 m) of the sink bowl’s top inside edge.

8. **Boathouses**  
   - **210.8(A)(8)**  

9. **Bathtubs/Shower Stalls**  
   - **210.8(A)(9)**  
   - Receptacles within 6 ft (1.8 m) of the bathtub/shower stall’s outside edge.

10. **Laundry Areas**  
    - **210.8(A)(10)**  

11. **Indoor Damp/Wet Locations**  
    - **210.8(A)(11)**  

---

**Additional Notes:**  
- **Exceptions for Special Cases:**  
  - Locking receptacles for ceiling fans/luminaires (see 210.8(A)(1) exception).  
  - Receptacles for dedicated snow-melting/deicing systems (210.8(A)(3) exception).  
  - Fire alarm system receptacles (210.8(A)(5) exception).  

**Inspector Tip:** Verify that all listed locations comply with **210.8(A)(1)–(11)** and check for applicable exceptions. Non-compliance risks electrical shock hazards in high-risk areas.  

[OK] Source: CEC 2022

---

### cec2022-012

**Original ID:** core-004 | **Category:** knowledge | **Tier:** core

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 5.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Surge Protection for Residential Service (CEC 2022)

**Requirement:**  
Surge protection **is required** for all new residential services in California per **CEC 2022 Section 230.67(A)**.  

**Installation Location:**  
- **Primary location:** Must be an **integral part of the service equipment** or **immediately adjacent** to it (230.67(B)).  
- **Exception:** If not feasible, it can be installed at the **next level of distribution equipment downstream** toward the load (e.g., a subpanel).  

**SPD Type:**  
- Must be **Type 1 or Type 2** surge-protective devices (230.67(C)).  

**Replacement Rule:**  
- If service equipment is replaced, surge protection must comply with all requirements of 230.67(D).  

[OK] Source: CEC 2022

---

### cec2022-013

**Original ID:** core-005 | **Category:** edge_cases | **Tier:** core

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet code requirements?

**Duration:** 9.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Panel Location and Clearance Compliance (CEC 2022)

### 1. **Panel in a Closet**  
**Violation of 240.24(D):**  
- **Rule:** Overcurrent devices (panels) **shall not be located in the vicinity of easily ignitible material**, such as in **clothes closets**.  
- **Your Case:** If the closet is a **clothes closet** (storage for garments/apparel), this violates the code.  
- **Exception:** Not applicable—no exceptions allow panels in clothes closets.  

---

### 2. **Front Clearance (24 Inches)**  
**Violation of 110.26(A)(1):**  
- **Rule:** Working space depth in front of panels depends on voltage and condition:  
  - **Condition 1 (General):** Minimum **30 inches** for 120/240V panels (Table 110.26(A)(1)).  
  - **Your Case:** 24 inches is **insufficient** for standard working space.  

---

### 3. **Water Heater Proximity (18 Inches to Side)**  
- **No Direct Rule Violation:**  
  - Lateral clearance (side-to-side) is **not specified** in the code.  
  - However, **working space must be clear of obstructions** (110.26(A)(3)).  
  - **18 inches** to the side is acceptable **if** it does not block access or create a hazard.  

---

### **Final Answer**  
1. **Panel in a clothes closet:** ❌ **Non-compliant** (240.24(D)).  
2. **Front clearance (24 inches):** ❌ **Non-compliant** (110.26(A)(1)).  
3. **Water heater location:** ✅ **Compliant** (no code violation identified).  

**Corrective Actions:**  
- Relocate the panel **away from clothes closets**.  
- Ensure **minimum 30 inches of front clearance** for working space.  

[OK] Source: CEC 2022

---

### cec2022-014

**Original ID:** core-006 | **Category:** edge_cases | **Tier:** core

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 5.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Multiple Conductors on a Single Breaker Terminal (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under **CEC 2022 Section 408.41**.  

### Key Requirements:
- **Section 408.41** mandates that **each grounded conductor** must terminate in an **individual terminal** not shared with another conductor.  
- **Exception**: Only permitted if the terminal is **explicitly marked** for multiple conductors (e.g., "2-wire" or "2-conductor" marking).  

### Violation Details:
- The breaker terminal in question is **not marked** for two conductors.  
- Terminating two 12 AWG conductors on a single terminal violates the requirement for individual termination points.  

### Corrective Action:
- **Option 1**: Replace the breaker with one explicitly marked for two conductors (e.g., "2-wire" terminal).  
- **Option 2**: Use a **junction box** to combine the two conductors into a single conductor before connecting to the breaker.  

[OK] Source: CEC 2022 Section 408.41

---

### cec2022-015

**Original ID:** core-007 | **Category:** grounding_bonding | **Tier:** core

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 6.1s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### Key Requirements:
1. **Grounding Electrode Requirement**  
   - **250.32(A)** mandates a grounding electrode system at the detached garage because it is supplied by a 4-wire feeder (not a single branch circuit).  
   - **Exception does not apply** (4-wire feeder > single branch circuit).  

2. **Grounding Electrode Conductor (GEC)**  
   - Connect the subpanel’s grounding electrode conductor to a **local grounding electrode** (e.g., ground rod, concrete-encased electrode).  
   - **Size**: Determined by the largest ungrounded conductor in the feeder using **Table 250.66**.  
     - Example: For a 2/0 AWG copper feeder, GEC must be **4 AWG copper** (see Table 250.66).  

3. **Equipment Grounding Conductor (EGC)**  
   - Run an EGC with the feeder conductors to the subpanel.  
   - **Size**: Based on the feeder’s overcurrent protection (e.g., 200A service) using **Table 250.122**.  
     - Example: 200A overcurrent protection requires **4 AWG copper** EGC.  

4. **Subpanel Configuration**  
   - **Separate neutrals and grounds**: Per **250.24(D)**, the subpanel must have **no bonding between neutral and ground**.  
   - Connect the EGC to the subpanel’s **ground bar**.  
   - Connect the GEC to the subpanel’s **grounding electrode system** (local ground rod).  

5. **Bonding**  
   - The subpanel’s metal enclosure must be bonded to the EGC.  
   - **250.58** requires all grounding electrodes at the garage to be bonded together (e.g., ground rod + water pipe if present).  

---

### Example Sizing (Assuming 2/0 AWG Copper Feeder):
- **Feeder conductors**: 2/0 AWG copper (200A service).  
- **EGC**: 4 AWG copper (Table 250.122 for 200A).  
- **GEC**: 4 AWG copper (Table 250.66 for 2/0 AWG ungrounded conductor).  

---

### Inspector Notes:
- **No shared neutral/ground**: The subpanel must not bond neutral and ground (unlike the main panel).  
- **Local grounding electrode**: A minimum 8-ft ground rod (250.52(A)(5)) is required unless another electrode (e.g., concrete-encased) is used.  
- **Bonding jumpers**: If multiple grounding electrodes are present, bond them with a minimum 6 AWG copper conductor (250.58).  

[OK] Source: CEC 2022 Sections 250.32, 250.66, 250.122, 250.24(D)

---

### cec2022-016

**Original ID:** core-008 | **Category:** grounding_bonding | **Tier:** core

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 6.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions and Requirements**
1. **Main Bonding Jumper**  
   - **Definition**: The connection between the *grounded circuit conductor* (neutral) and the *equipment grounding conductor* at the **service** (Section 100).  
   - **Purpose**: Bonds the neutral and equipment grounding system at the service point to ensure safety and proper fault current paths.  
   - **Required**: **At every service** (Section 250.28(D)).  

2. **System Bonding Jumper**  
   - **Definition**: The connection between the *grounded circuit conductor* and the *supply-side bonding jumper* or *equipment grounding conductor* at a **separately derived system** (e.g., transformers, generators) (Section 100).  
   - **Purpose**: Bonds the neutral and grounding system at the source of a separately derived system.  
   - **Required**: **At every separately derived system** (Section 250.28(D)).  

---

### **Key Differences**
| Feature                  | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|--------------------------|---------------------------------------------------|----------------------------------------------------|
| **Location**             | Service equipment (e.g., service panel)           | Separately derived system (e.g., transformer, generator) |
| **Application**          | Services only                                    | Separately derived systems only                    |
| **Connection**           | Grounded conductor → Equipment grounding conductor | Grounded conductor → Supply-side bonding jumper      |
| **Code Reference**       | Section 250.28(D)                                | Section 250.28(D)                                  |

---

### **Sizing Requirements**
Both jumpers are sized per **Table 250.102(C)(1)** based on the largest ungrounded conductor in the system:  
- **Copper Conductors**:  
  - For 350 kcmil copper ungrounded conductors → 1/0 AWG copper jumper.  
  - For 600 kcmil copper ungrounded conductors → 2/0 AWG copper jumper.  
- **Aluminum Conductors**:  
  - For 900 kcmil aluminum ungrounded conductors → 3/0 AWG aluminum jumper.  

**Notes**:  
- If ungrounded conductors exceed 1100 kcmil copper or 1750 kcmil aluminum, sizing rules in **Notes 1–3** of Table 250.102(C)(1) apply.  
- Jumpers must be copper, aluminum, or corrosion-resistant materials (Section 250.28(A)).  

---

### **Inspector Notes**
- **Main bonding jumpers** are **never required** at separately derived systems (only system bonding jumpers).  
- **System bonding jumpers** are **never required** at services (only main bonding jumpers).  
- Verify jumper sizes match the largest ungrounded conductor in the system using Table 250.102(C)(1).  

[OK] Source: CEC 2022 Sections 100, 250.28, 250.102, Table 250.102(C)(1)

---

### cec2022-017

**Original ID:** core-009 | **Category:** load_calculations | **Tier:** core

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 6.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

**1. Required Number of Circuits for Kitchen:**
- **Minimum Requirement**: **Two or more 20-ampere small-appliance branch circuits** are required for all receptacle outlets in kitchens, pantries, breakfast rooms, and similar areas (CEC 2022 **210.11(C)(1)** and **210.52(B)(1)**).

**2. Serving Dining Room Receptacles:**
- **Permitted**: Yes, the small-appliance branch circuits serving the kitchen **may also supply receptacle outlets in the dining room** (CEC 2022 **210.52(B)(1)** explicitly allows this).
- **Key Condition**: The circuits must not serve more than **one kitchen**, but dining room receptacles are permitted as part of the "similar area" designation.

**Inspector Note**: 
- The two small-appliance circuits must **not serve any other loads** (e.g., laundry, bathroom, or lighting) except as allowed by exceptions.
- Dining room receptacles are considered part of the "similar area" and are explicitly included in the scope of 210.52(B)(1).

[OK] Source: CEC 2022

---

### cec2022-018

**Original ID:** core-010 | **Category:** load_calculations | **Tier:** core

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 8.9s | **Iterations:** 7

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator, python_calculator

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Base ampacity**: 30A (12 AWG THHN copper at 90°C, Table 310.16)  
**Temperature correction**: 0.82 (50°C ambient, Table 310.15(B)(1)(1))  
**Bundling correction**: 0.8 (6 conductors, Table 310.15(C)(1))  

**Calculation**:  
$$
30A \times 0.82 \times 0.8 = 19.68A
$$

**Final adjusted ampacity**: **19.68 amperes**  

[OK] Source: CEC 2022 Sections 310.15(B)(1)(1), 310.15(C)(1)

---

### cec2022-019

**Original ID:** core-011 | **Category:** why_questions | **Tier:** core

**Question:** Why is AFCI protection required for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 7.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## AFCI Protection in Bedrooms and Living Areas (CEC 2022)

**Requirement**:  
AFCI protection is required for all 120V, 15- and 20-ampere branch circuits in dwelling units supplying outlets in **bedrooms, living rooms, and similar areas** (Section 210.12(A)). This includes family rooms, dining rooms, parlors, libraries, dens, sunrooms, recreation rooms, closets, hallways, and laundry areas.

**Electrical Hazard Prevented**:  
AFCI protection prevents **electrical fires caused by arc faults**. Arc faults occur when damaged or deteriorated wiring creates high-temperature electrical arcs (e.g., from frayed cords, loose connections, or nail penetration). These arcs can ignite surrounding materials, leading to fires.

**Code Basis**:  
- **Section 210.12(A)** explicitly mandates AFCI protection for dwelling unit branch circuits in the listed areas.  
- **UL 1699** (referenced in informational notes) defines standards for AFCI devices to detect and interrupt dangerous arcs while allowing harmless arcs (e.g., from switches or motors).  

**Key Details**:  
- **Permitted Methods**: Includes combination-type AFCIs, outlet branch-circuit-type AFCIs, or system combination-type AFCIs (see 210.12(A)(1)–(6)).  
- **Exceptions**: Not required for fire alarm circuits (Exception to 210.12(A)) or short extensions (≤6 ft) without additional outlets (Exception to 210.12(D)).  

**Inspector Note**:  
AFCIs target **series arcs** (e.g., broken wires) and **parallel arcs** (e.g., short circuits), which are common precursors to electrical fires. GFCI protection (Section 210.8) addresses ground faults separately but does not detect arc faults.  

[OK] Source: CEC 2022

---

### cec2022-020

**Original ID:** core-012 | **Category:** why_questions | **Tier:** core

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 6.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

**Why Torque Specifications Matter:**
1. **Ensures Proper Connection Integrity**  
   Correct torque values prevent loose connections that could cause:
   - Increased resistance → overheating → fire hazards
   - Arcing at terminals → equipment damage
   - Intermittent electrical contact → equipment failure

2. **Coordinates with Temperature Ratings**  
   Per **110.14(C)**, conductor ampacity must not exceed the lowest temperature rating of any connected termination. Proper torque ensures the termination can sustain its rated temperature without degradation.

3. **Manufacturer Compliance**  
   **110.14(D)** requires terminal connections to use torque values specified by equipment manufacturers. This ensures compatibility with terminal design (e.g., set-screw vs. bolted connections).

4. **Prevents Mechanical Damage**  
   Over-torquing can damage terminal threads or conductor strands, while under-torquing allows movement and oxidation.

---

**Code Requirements Location:**
1. **General Torque Requirements**  
   - **CEC 2022 Section 110.14(D):**  
     *"Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer."*  
     - **Informational Note 1:** Acceptable torque application methods include calibrated torque tools, shear bolts, or breakaway devices.  
     - **Informational Note 2:** Contact manufacturers if torque values aren't marked on equipment.

2. **Specific Motor Controller Requirements**  
   - **CEC 2022 Section 430.9(C):**  
     *"Control circuit devices with screw-type pressure terminals used with 14 AWG or smaller copper conductors shall be torqued to a minimum of **0.8 N·m (7 lb-in.)** unless identified for a different torque value."*

3. **Cablebus Termination Requirements**  
   - **CEC 2022 Section 370.20(B):**  
     Requires "approved terminating means" for cablebus conductors, referencing **110.14(C)** for temperature coordination.

---

**Inspector Note:**  
Always verify torque values directly on equipment nameplates or in manufacturer documentation. The **0.8 N·m (7 lb-in.)** minimum in **430.9(C)** applies only to small conductors in control circuits—larger power circuits require manufacturer-specific values from **110.14(D)**.

[OK] Source: CEC 2022

---

### cec2022-021

**Original ID:** inspection-001 | **Category:** panel_load_calculation | **Tier:** inspection

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 15.1s | **Iterations:** 4

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Residential Service Load Calculation (CEC 2022)

### Step 1: General Lighting Load  
- **3000 sq ft × 3 VA/sq ft** = **9000 VA** (Table 220.12 for dwelling units)  

### Step 2: Small Appliance and Laundry Circuits  
- **2 × 1500 VA** (small appliances) + **1 × 1500 VA** (laundry) = **4500 VA** (220.52)  

### Step 3: Range Demand  
- **12 kW range** → **8850 VA** (Table 220.55 Column B: 3 kW + 9 kW × 65% = 8.85 kW)  

### Step 4: Dryer Demand  
- **5.5 kW dryer** = **5500 VA** (100% of nameplate rating)  

### Step 5: Air Conditioning  
- **4600 VA** (19.2A × 240V)  

---

### Step 6: Apply Demand Factors  
**General Lighting Load**:  
- First 3000 VA @ 100% = **3000 VA**  
- Remaining 6000 VA @ 35% = **2100 VA**  
- **Total General Load** = 3000 + 2100 = **5100 VA**  

**Total Service Load**:  
- General Load: **5100 VA**  
- Range: **8850 VA**  
- Dryer: **5500 VA**  
- AC: **4600 VA**  
- **Total** = 5100 + 8850 + 5500 + 4600 = **24,050 VA**  

---

### Step 7: Convert to Amperes  
- **24,050 VA ÷ 240V** = **100.2 A**  

---

### Final Determination  
- **200A panel** is **adequately sized** (100.2 A < 200A).  

[OK] Source: CEC 2022

---

### cec2022-022

**Original ID:** inspection-002 | **Category:** clearance_violations | **Tier:** inspection

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL code violations.

**Duration:** 8.9s | **Iterations:** 3

**Tools Called:** cec_lookup_working_space

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Electrical Panel Inspection Violations (CEC 2022)

**1. Insufficient Working Space Depth (110.26(A)(1))**
- **Required**: 36 inches (3 ft) depth for 120V panels (Condition 1)
- **Actual**: 28 inches depth
- **Violation**: Fails minimum working space clearance in front of panel

**2. Obstruction Within Working Space (110.26(A)(3))**
- **Issue**: Water heater located 16 inches from panel side
- **Requirement**: Working space must be clear of obstructions
- **Violation**: Water heater intrudes into required working space

**3. Vertical Clearance (110.26(A)(2))**
- **Required**: 78 inches (6' 6") vertical clearance above floor
- **Panel Height**: 60 inches (5 ft) mounting height
- **Uncertain**: Need ceiling height verification
- **Potential Violation**: If ceiling height < 78 inches above floor where work occurs

**4. Panel Location (240.24 Prohibitions)**
- **No violation**: Question does not indicate panel is in a clothes closet or bathroom

**Inspector Notes**:
- 110.26(A)(1) requires 36" depth for all 120V panels (Condition 1)
- 110.26(A)(3) mandates clear working space on all sides of equipment
- 240.24(D) and (E) would apply if panel were in prohibited locations

[OK] Source: CEC 2022

---

### cec2022-023

**Original ID:** inspection-005 | **Category:** gfci_afci_compliance | **Tier:** inspection

**Question:** New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide code references.

**Duration:** 12.1s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Circuit Protection Requirements for Kitchen Installations (CEC 2022)

### 1. **Countertop Receptacles (20A Circuits)**
- **Protection Required**: **Combination AFCI/GFCI Breaker**
- **Code References**:
  - **GFCI**: CEC 210.8(A)(6) requires GFCI protection for all receptacles serving countertop surfaces.
  - **AFCI**: CEC 210.12(A) mandates AFCI protection for all 120V, 15–20A receptacles in dwelling units, including countertop circuits.

### 2. **Dishwasher (15A Dedicated Circuit)**
- **Protection Required**: **GFCI Breaker**
- **Code References**:
  - **GFCI**: CEC 210.8(A)(6) applies to countertop receptacles, but dishwashers are also covered under CEC 422.5(B) for appliances near sinks. GFCI is required due to proximity to water sources.
  - **AFCI**: Exempt under CEC 210.12(A) Exception No. 1 (dedicated appliance circuits).

### 3. **Garbage Disposal (15A Dedicated Circuit)**
- **Protection Required**: **GFCI Breaker**
- **Code References**:
  - **GFCI**: CEC 210.8(A)(6) and 422.5(B) apply due to proximity to sinks and appliance classification.
  - **AFCI**: Exempt under CEC 210.12(A) Exception No. 1 (dedicated appliance circuits).

### 4. **Refrigerator (20A Dedicated Circuit)**
- **Protection Required**: **Standard Breaker**
- **Code References**:
  - **GFCI**: Not required (CEC 210.8(A)(6) excludes fixed appliances not in wet locations).
  - **AFCI**: Exempt under CEC 210.12(A) Exception No. 1 (dedicated appliance circuits).

---

**Inspector Note**: 
- **Countertop circuits** require both **AFCI and GFCI** due to their location and general use.
- **Dedicated appliance circuits** (dishwasher, garbage disposal) require **GFCI** but are **exempt from AFCI** under CEC 210.12(A) Exception No. 1.
- **Refrigerator circuits** are **exempt from both GFCI and AFCI** as they are fixed appliances not in wet locations and fall under dedicated appliance exceptions.

[OK] Source: CEC 2022

---

### cec2022-024

**Original ID:** inspection-006 | **Category:** subpanel_violations | **Tier:** inspection

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 9.8s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Subpanel Bonding Violations and Correct Configuration (CEC 2022)

### **Identified Violations:**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation:** Section 250.24(D) requires **neutral and ground bars to be separated** in subpanels (not the main service panel). Bonding them creates a parallel path for fault current, violating 250.24(A)(5) ("grounded conductor shall not be reconnected to ground on the load side of the service disconnect").  
   - **Correct Action:** Remove the main bonding jumper connecting neutral and ground bars. Install an **insulated neutral bar** and a **dedicated equipment grounding bar**.

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation:** Section 250.24(D) prohibits bonding the neutral bar to the enclosure in subpanels. This creates an unintended ground path and violates 250.24(A)(5).  
   - **Correct Action:** Isolate the neutral bar from the enclosure. Only the equipment grounding bar should be bonded to the enclosure (per 250.142(B)).

3. **Main Bonding Jumper Installed in Subpanel**  
   - **Violation:** The main bonding jumper (which connects neutral and ground in the **main service panel**) must **not** be present in subpanels.  
   - **Correct Action:** Remove the main bonding jumper entirely from the subpanel.

---

### **Correct Configuration for Detached Garage Subpanel:**
1. **Neutral Bar:**  
   - Connected **only** to the feeder neutral conductor.  
   - **Isolated** from the equipment grounding bar and metal enclosure.  

2. **Equipment Grounding Bar:**  
   - Connected to the feeder equipment grounding conductor (#2 AWG copper or equivalent per Table 250.122 for 100A).  
   - Bonded to the metal subpanel enclosure (per 250.142(B)).  

3. **Grounding Electrode Conductor (GEC):**  
   - Required per **250.32(A)** for detached structures (unless fed by a single branch circuit).  
   - Connects the subpanel’s equipment grounding bar to a **local grounding electrode** (e.g., ground rod).  

4. **Feeder Connections:**  
   - **Hot conductors:** Connected to the subpanel’s breaker.  
   - **Neutral conductor:** Connected to the isolated neutral bar.  
   - **Equipment grounding conductor:** Connected to the equipment grounding bar.  

---

### **Key Code References:**
- **250.24(D):** Neutral and ground must be separated in subpanels.  
- **250.24(A)(5):** Prohibits reconnecting neutral to ground on the load side of the service.  
- **250.32(A):** Detached structures require a grounding electrode unless fed by a single branch circuit.  
- **250.142(B):** Equipment grounding conductors must connect to the enclosure, but neutral must remain isolated.  

[OK] Source: CEC 2022

---

### cec2022-025

**Original ID:** inspection-007 | **Category:** conduit_fill | **Tier:** inspection

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_lookup_conduit_fill

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Calculation:**
1. **Conduit Fill Limitation**  
   - RMC 1¼" total area: **1.526 in²** (Chapter 9 Table 4)  
   - 40% fill for ≥2 conductors:  
     $ 1.526 \, \text{in²} \times 0.40 = 0.61 \, \text{in²} $

2. **Conductor Area**  
   - 10 AWG THHN area: **0.0211 in²** (Chapter 9 Table 5)

3. **Maximum Conductors**  
   $ \frac{0.61 \, \text{in²}}{0.0211 \, \text{in²/conductor}} = 28.91 $  
   → **28 conductors** (round down to nearest whole number)

**Verification:**  
- 28 conductors × 0.0211 in² = **0.5908 in²** (4.1% of total conduit area)  
- 29 conductors would exceed 40% fill (0.6119 in² > 0.61 in²).

**Answer:**  
A 1¼-inch RMC can accommodate a **maximum of 28** 10 AWG THHN conductors at 40% fill.

[OK] Source: CEC 2022 Chapter 9 Tables 4 and 5

---

### cec2022-026

**Original ID:** inspection-008 | **Category:** voltage_drop | **Tier:** inspection

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet the 3% maximum recommendation for branch circuits?

**Duration:** 9.9s | **Iterations:** 5

**Tools Called:** python_calculator, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Voltage Drop Verification (CEC 2022)

**Code Reference**:  
CEC 2022 **210.19(A) Informational Note No. 3** explicitly states:  
> "Conductors for branch circuits... sized to prevent a voltage drop exceeding **3%** at the farthest outlet... provide reasonable efficiency of operation."

**Calculation Result**:  
- **Voltage drop**: 2.84 volts (2.37% of 120V)  
- **Code requirement**: ≤ 3% for branch circuits  

**Conclusion**:  
✅ The 2.37% voltage drop **meets the 3% maximum recommendation** for branch circuits per CEC 2022.  

[OK] Source: CEC 2022

---

### cec2022-027

**Original ID:** inspection-009 | **Category:** derating_calculation | **Tier:** inspection

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 6.3s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

### Step 1: Base Ampacity
- **12 AWG TW copper at 60°C**: 20A (Table 310.16)  
  *Source: CEC 2022 Table 310.16*

---

### Step 2: Temperature Correction Factor  
Ambient temperature = 43°C  
- **Correction factor for 60°C conductors at 43°C**:  
  - Table 310.15(B)(1)(1) shows 0.82 at 40°C and 0.71 at 45°C.  
  - **Use 0.82** (next lower temperature per code requirements).  
  *Source: CEC 2022 Table 310.15(B)(1)(1)*

---

### Step 3: Bundling Adjustment Factor  
6 current-carrying conductors in conduit:  
- **Adjustment factor**: 0.80 (Table 310.15(C)(1) for 4–6 conductors).  
  *Source: CEC 2022 Table 310.15(C)(1)*

---

### Step 4: Final Calculation  
$$
\text{Adjusted Ampacity} = 20A \times 0.82 \times 0.80 = 13.12A
$$

---

### Step 5: Overcurrent Protection Check  
- **240.4(D)** limits 12 AWG copper to **20A maximum OCP**.  
- Final adjusted ampacity (13.12A) is **less than 20A**, so compliant.  

---

### Final Answer  
**Adjusted ampacity**: **13.1A** (rounded to one decimal place).  

[OK] Source: CEC 2022

---

### cec2022-028

**Original ID:** inspection-010 | **Category:** grounding_electrode_conductor | **Tier:** inspection

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 5.7s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Minimum Size Copper GEC for 1000 kcmil Service Conductors (CEC 2022)

**Answer:**  
The minimum size copper grounding electrode conductor (GEC) required is **2/0 AWG**.

**Calculation Steps:**  
1. **Equivalent Service Conductor Size:**  
   Four parallel 250 kcmil conductors = 4 × 250 kcmil = **1000 kcmil** (per phase).  

2. **Table 250.66 Reference:**  
   For service conductors over 600 kcmil through 1100 kcmil, the minimum copper GEC size is **2/0 AWG** (per CEC 2022 Table 250.66).  

3. **Exceptions:**  
   - If the grounding electrode is a **ground rod, pipe, or plate electrode**, the GEC may be reduced to **6 AWG copper** (250.66(A)).  
   - If the grounding electrode is a **concrete-encased electrode**, the GEC may be reduced to **4 AWG copper** (250.66(B)).  
   *Note: These exceptions apply only if the specific electrode type is used.*  

**Inspector Note:**  
- The California amendment (delta) modifies the base NEC requirements, but Table 250.66 remains applicable as provided.  
- Verify the grounding electrode type to determine if exceptions apply.  

[OK] Source: CEC 2022 Table 250.66

---

### cec2022-029

**Original ID:** cec-001 | **Category:** panelboard_requirements | **Tier:** california_specific

**Question:** What are the panelboard space requirements for single-family dwellings? What appliances must have reserved circuit breaker spaces?

**Duration:** 6.9s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Panelboard Space Requirements and Reserved Circuit Breaker Spaces (CEC 2022)

### **Panelboard Space Requirements for Single-Family Dwellings**
According to **CEC 2022 Section 408.2(A)**, panelboards in single-family residential buildings (including one or two dwellings) **must be provided with circuit breaker spaces** for the following appliances:
1. **Heat pump water heaters**
2. **Heat pump space heaters**
3. **Electric cooktops**
4. **Electric clothes dryers**

This requirement is mandated by the **California Energy Code (CEC) Section 150.0(n), (t), (u), and (v)** to ensure readiness for energy-efficient appliances.

---

### **Reserved Circuit Breaker Spaces for Appliances**
The same section (408.2(A)) explicitly requires **designated circuit breaker spaces** in panelboards to accommodate these appliances. Additionally:
- **Heat pump space heaters** must have **designated spaces, receptacles, and branch circuits** as specified in **CEC 2022 Section 440.3(E)** (referencing California Energy Code Section 150.0(t)).

---

### **Key Code Citations**
- **CEC 2022 Section 408.2(A)**: Mandates reserved spaces for heat pump water heaters, heat pump space heaters, electric cooktops, and dryers in single-family dwellings.
- **CEC 2022 Section 440.3(E)**: Requires designated spaces for heat pump space heaters in single-family buildings.

[OK] Source: CEC 2022

---

### cec2022-030

**Original ID:** cec-002 | **Category:** ev_charging | **Tier:** california_specific

**Question:** What are the electrical requirements for EV charging infrastructure in new residential construction?

**Duration:** 8.1s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Electrical Requirements for EV Charging in New Residential Construction (CEC 2022)

### 1. **Electrical Installation (Article 625)**
- **Dedicated Circuits**: Each EV charging outlet must be supplied by an **individual branch circuit** with **no other outlets** (625.40).
- **Location Requirements**:
  - Indoor EVSE must be installed **≥ 18 in. above the floor**.
  - Outdoor EVSE must be installed **≥ 24 in. above grade** (625.50).
- **GFCI Protection**: All AC receptacles used for EV power export must have **GFCI protection for personnel** (625.60(D)).
- **Weatherproof Enclosures**: Receptacles in wet locations require **weatherproof enclosures** with extra-duty ratings (625.56).

---

### 2. **California Mandates (CALGreen/Title 24)**
- **EV Readiness**: New residential buildings must provide **at least one EV-ready circuit** per dwelling unit (CALGreen Chapter 5, Division 5.1).
- **Minimum Circuit Requirements**:
  - **120V, 20A circuit** or **240V, 40A circuit** must be installed and labeled for future EV charging.
  - Circuit must include a **receptacle** or **hardwired connection** (Title 24, Part 6, Section 5.1).
- **Panelboard Spaces**: Panelboards must reserve **at least two spaces** for future EV charging circuits (408.2).

---

### 3. **Overcurrent and Grounding**
- **Overcurrent Protection**: EV supply equipment must be protected by an overcurrent device rated per the manufacturer’s labeling (625.42).
- **Grounding**: EVSE grounding must comply with 250.122 for equipment grounding conductors.

---

### 4. **Special Conditions**
- **Bidirectional Charging**: Systems with power export functionality must comply with Article 705 for interconnections (625.48).
- **Load Management**: Adjustable settings on fixed-in-place EVSE require **restricted access** to prevent user tampering (625.42).

---

### Inspector Notes:
- **CALGreen Compliance**: Verify EV-ready circuits are installed per Title 24, even if not immediately used for charging.
- **Labeling**: All EV circuits must be clearly labeled at the service panel.
- **Future-Proofing**: Ensure panelboards have reserved spaces and adequate capacity for EV loads.

[OK] Source: CEC 2022, CALGreen, Title 24

---

### cec2022-031

**Original ID:** cec-003 | **Category:** solar_pv | **Tier:** california_specific

**Question:** What are the electrical requirements for solar PV systems on new residential construction?

**Duration:** 10.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Electrical Requirements for Solar PV Systems in New Residential Construction (CEC 2022)

### 1. **Rapid Shutdown Requirements (690.12)**
- **Controlled Conductors**: PV DC circuits and inverter output circuits within the array boundary (305 mm/1 ft) must reduce voltage to ≤80V within 30 seconds. Outside the boundary, voltage must drop to ≤30V within 30 seconds.
- **Initiation Devices**: A readily accessible switch (outside the building for single-family homes) must initiate shutdown. For multiple systems, no more than six switches/breakers in a single enclosure are allowed.
- **Labeling**: Permanent labels with "SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN" (yellow background, black text, 9.5 mm min. height) must be installed at service equipment locations.

### 2. **Wiring Methods (690.31)**
- **Conductor Types**: Use listed PV wire (UL 4703) or DG cable (UL 3003). For outdoor runs, single-conductor cables must be sunlight-resistant (e.g., USE-2, RHW-2).
- **Ampacity Adjustments**: Apply temperature correction factors from **Table 690.31(A)(a)** and base ampacities from **Table 690.31(A)(b)** (e.g., 10 AWG PV wire has 50A ampacity at 125°C).
- **Labeling**: All PV DC circuits in accessible locations must be marked "PHOTOVOLTAIC POWER SOURCE" (white on red, 9.5 mm min. height).

### 3. **Grounding and Bonding (690.41–43, 690.47)**
- **System Grounding**: Solidly grounded systems must connect the grounded conductor to a grounding electrode via a conductor sized per **250.166**.
- **Equipment Bonding**: PV module frames and support structures must be bonded using listed bonding devices. Metal support structures must have bonding jumpers between sections.
- **Grounding Electrode**: PV arrays must connect to the building’s grounding electrode system per **250.52**. Ground-mounted arrays may use their support structure as a grounding electrode if it meets **250.52** requirements.

### 4. **Arc-Fault Protection (690.11)**
- **DC Arc-Fault Protection**: Required for PV systems with DC circuits ≥80V. Exceptions apply for systems in metallic raceways, metal-clad cables, or underground installations.

### 5. **Labeling and Identification (690.53–55)**
- **Maximum DC Voltage Label**: Install a permanent label at the PV disconnect or inverter showing the highest DC voltage (calculated per **690.7**).
- **Polarity Marking**: DC conductors must be marked with "+" or "POSITIVE" (non-green/white/gray) and "-" or "NEGATIVE" (non-green/white/gray/ red).

### 6. **Overcurrent and Disconnect Requirements (690.9, 690.15)**
- **Overcurrent Protection**: PV source circuits must be protected per **690.9(B)**. Disconnecting means for electronic converters (e.g., inverters) must be readily accessible and labeled.

### 7. **Stand-Alone Systems (690.10)**
- If the PV system is part of a stand-alone setup, follow **710.15** for wiring requirements.

---

**Inspector Note**: California mandates rapid shutdown compliance for all PV systems on buildings (690.12). Verify labels are installed per **690.56(C)** and that arc-fault protection is present for DC circuits ≥80V. Use **Table 690.31(A)(b)** for conductor sizing and apply temperature derates from **Table 690.31(A)(a)**.

[OK] Source: CEC 2022

---

### cec2022-032

**Original ID:** cec-004 | **Category:** heat_pump | **Tier:** california_specific

**Question:** What circuit requirements exist for heat pump water heaters in new dwelling units?

**Duration:** 11.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Circuit Requirements for Heat Pump Water Heaters in New Dwellings (CEC 2022)

### 1. **Overcurrent Protection and Conductor Sizing**
- **Section 422.13**:  
  - Fixed storage-type water heaters (≤ 450 L/120 gal) must have **branch-circuit overcurrent devices and conductors sized not smaller than 125% of the water heater's rated current**.  
  - Example: A 12A heater requires a minimum 15A OCPD (12A × 1.25 = 15A).  

- **Section 422.11(A)**:  
  - Branch-circuit overcurrent devices must comply with **240.4** (standard sizes: 15A, 20A, 30A, etc.).  
  - If the appliance is marked with a protective device rating, the OCPD **must not exceed** this value.  

### 2. **Individual Branch Circuit Requirement**
- **Section 422.12** (by implication):  
  - Storage-type water heaters typically require an **individual branch circuit** (dedicated to the appliance).  

### 3. **Temperature-Limiting Controls**
- **Section 422.47**:  
  - All storage water heaters must have a **temperature-limiting means** (e.g., trip-free thermostat) to disconnect power if water temperature exceeds safe limits.  
  - Exceptions apply for high-capacity (≥ 60 kW) or high-temperature (≥ 82°C/180°F) heaters.  

### 4. **California-Specific Considerations**
- **CALGreen/Title 24**:  
  - California mandates **EV-ready infrastructure** and **energy efficiency** standards for new dwellings. While not explicitly mentioned in the search results, Title 24 may require additional provisions for heat pump water heaters (e.g., dedicated circuits for high-efficiency models).  

---

**Inspector Note**:  
- Verify the water heater's **nameplate rating** and ensure the OCPD matches 125% of this value (per 422.13).  
- Confirm the circuit is **dedicated** and sized per 310.16 (considering termination temperatures in 110.14(C)).  
- For heat pump water heaters with compressors, check **Article 440** for motor overload protection requirements (not included in this search).  

[OK] Source: CEC 2022

---

### cec2022-033

**Original ID:** cec-005 | **Category:** electrification | **Tier:** california_specific

**Question:** What is required for electric cooktop readiness in new homes?

**Duration:** 8.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Electric Cooktop Readiness in New Homes (CEC 2022)

**Requirements for Single-Family Residential Buildings (1–2 dwellings):**  
Per **CEC 2022 Section 422.3(A)(2)**, each dwelling unit must have:  
- **Dedicated circuits** and **circuit identifications** as specified in **California Energy Code Section 150.0(u)**.  

**Key Implications:**  
1. **Dedicated Circuit**: A dedicated circuit means the cooktop must have its own branch circuit not shared with other appliances.  
2. **Circuit Identification**: The circuit must be clearly labeled in the panel (e.g., "Electric Cooktop") for easy identification.  
3. **Amperage and Wiring**:  
   - Typically requires a **240V circuit** with a **30A–40A breaker**, depending on the cooktop’s nameplate rating.  
   - Conductors must match the breaker size (e.g., **10 AWG copper** for 30A, **8 AWG copper** for 40A).  
4. **Receptacle Type**: A **NEMA 10-30R** or **14-30R** receptacle is standard for electric cooktops.  

**Multifamily Buildings:**  
Per **CEC 2022 Section 422.3(B)(1)**, multifamily units must also provide dedicated circuits per **California Energy Code Section 160.9(b)**.  

**Inspector Note:**  
- Verify the circuit is **not shared** with other loads (e.g., microwave, outlets).  
- Confirm the **breaker is labeled** at the panel.  
- Check wiring size and type (e.g., THHN/THWN) matches the cooktop’s requirements.  

[OK] Source: CEC 2022

---

### cec2022-034

**Original ID:** cec-006 | **Category:** electrification | **Tier:** california_specific

**Question:** What are the panelboard requirements for electric clothes dryer circuits in new construction?

**Duration:** 6.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

### **Key Requirements**
1. **Circuit Breaker Spaces**  
   - **Single-family buildings** (1–2 dwellings): Panelboards **must include dedicated circuit breaker spaces** for electric clothes dryers as specified in **California Energy Code Section 150.0(n), (t), (u), and (v)**.  
   - **Multifamily buildings**: Panelboards **must include dedicated circuit breaker spaces** for electric clothes dryers as specified in **California Energy Code Section 160.9(a), (b), and (c)**.  

2. **Code Reference**  
   - **CEC 2022 Section 408.2(A) & 408.2(B)** mandate these requirements for single-family and multifamily buildings, respectively.  

3. **Additional Context**  
   - These provisions ensure panelboards are pre-wired to accommodate electric dryer circuits, aligning with energy efficiency and safety standards in new construction.  

[OK] Source: CEC 2022

---

### cec2022-035

**Original ID:** cec-007 | **Category:** overcurrent | **Tier:** california_specific

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Duration:** 6.5s | **Iterations:** 4

**Tools Called:** cec_lookup_table, cec_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## CEC Table 240.4(G) Unique California Provisions

**Unique California Feature**:  
The table includes **California amendments (δ)** that modify the National Electrical Code (NEC). These amendments are specific to California and may add, remove, or alter overcurrent protection requirements for the listed conductor applications.

**Key Content**:  
The table cross-references specialized conductor types (e.g., fire alarm, welder, capacitor circuits) to their respective NEC articles/sections for overcurrent protection rules. California's δ amendments may adjust these references or requirements.

**Example of California-Specific Impact**:  
- For **fire alarm circuits** (referenced to Article 760), California might impose stricter overcurrent protection rules via δ amendments.
- For **remote-control circuits** (Article 725), δ could modify allowed conductor types or OCPD ratings.

**Inspector Note**:  
Always check the **δ amendments** in the California Code Supplement for deviations from NEC requirements when applying Table 240.4(G). These amendments are not included in standard NEC tables.

[OK] Source: CEC 2022 Table 240.4(G) and California amendments (δ)

---

### cec2022-036

**Original ID:** cec-008 | **Category:** surge_protection | **Tier:** california_specific

**Question:** What does CEC Table 242.3 specify for installations?

**Duration:** 4.4s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## CEC Table 242.3 Specifications (CEC 2022)

**Table 242.3** in the California Electrical Code (CEC) 2022 is a **cross-reference table** for Article 242 (Overvoltage Protection). It identifies **equipment types** and directs users to **other NEC articles** where additional overvoltage protection requirements apply. This table is a **California-specific addition** (marked with an "N" for new/local amendments) not found in the base NEC.

---

### Key Equipment Types and Referenced Articles:
- **Class I locations** → Article 501  
- **Class II locations** → Article 502  
- **Community antenna TV/radio systems** → Article 820  
- **Critical operations power systems** → Article 708  
- **Elevators/dumbwaiters/escalators** → Article 620  
- **Emergency systems** → Article 700  
- **Equipment >1000V** → Article 490  
- **Fire pumps** → Article 695  
- **Industrial machinery** → Article 670  
- **IT equipment** → Article 645  
- **Modular data centers** → Article 646  
- **Outdoor overhead conductors >1000V** → Article 399  
- **Radio/TV equipment** → Article 810  
- **Receptacles/cord connectors** → Article 406  
- **Wind electric systems** → Article 694  

---

### Purpose:
This table helps electricians and inspectors **locate overvoltage protection requirements** for specific equipment types by cross-referencing to the appropriate NEC article. For example:
- Overvoltage protection for **emergency systems** (e.g., exit signs, emergency lighting) must comply with **Article 700**.
- **Fire pump installations** require overvoltage protection per **Article 695**.

---

### Inspector Note:
- Always verify the referenced articles for **detailed requirements** (Table 242.3 only provides cross-references).
- This table is **California-specific** (not in NEC), so it applies to all electrical installations in California governed by the CEC.

[OK] Source: CEC 2022 Table 242.3

---

### cec2022-037

**Original ID:** cec-009 | **Category:** motor_control | **Tier:** california_specific

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Duration:** 5.6s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)

**Purpose**: Specifies **maximum overcurrent protective device (OCPD) ratings** for motor control circuits based on conductor size and installation configuration.

---

### **Table Structure**
- **Columns**:
  - **Column A**: Directly sized to conductor ampacity (per 310.15).
  - **Column B**: 400% of conductor ampacity (per 310.19 for 60°C conductors).
  - **Column C**: 300% of conductor ampacity (per 310.16 for 60°C conductors).

- **Conductor Sizes**: 18 AWG to larger than 10 AWG (copper and aluminum where applicable).

---

### **Key Values**
| Conductor Size | Column A (Copper) | Column B (Copper) | Column C (Copper) |
|----------------|-------------------|-------------------|-------------------|
| 18 AWG         | 7A                | 25A               | 7A                |
| 16 AWG         | 10A               | 40A               | 10A               |
| 14 AWG         | (Note 1)          | 100A              | 45A               |
| 12 AWG         | (Note 1)          | 120A              | 60A               |
| 10 AWG         | (Note 1)          | 160A              | 90A               |
| >10 AWG        | (Note 2)          | (Note 2)          | (Note 3)          |

---

### **Footnotes**
1. **Notes 1–3** direct to referenced tables for larger conductors:
   - **>10 AWG**: 
     - Column B = 400% of **Table 310.19** (60°C conductors).
     - Column C = 300% of **Table 310.16** (60°C conductors).

---

### **Application Notes**
- **Aluminum conductors** are only listed for sizes 12 AWG and larger (10 AWG and smaller show "—").
- For conductors **larger than 10 AWG**, calculate OCPD ratings using:
  - **Column B**: 400% of 310.19 values.
  - **Column C**: 300% of 310.16 values.
- Always verify conductor ampacity from referenced tables (310.16/310.19) before applying multipliers.

---

[OK] Source: CEC 2022 Table 430.72(B) and cross-references.

---

### cec2022-038

**Original ID:** cec-010 | **Category:** medium_voltage | **Tier:** california_specific

**Question:** What medium voltage cable tables exist that are California-specific?

**Duration:** 5.6s | **Iterations:** 3

**Tools Called:** search_tables

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Medium Voltage Cable Tables in CEC 2022

The following California Electrical Code (CEC 2022) tables specifically address medium voltage cable applications (typically 2001V and above):

1. **Table 315.10(A)**  
   - **Purpose**: Conductor application and insulation ratings for voltages **2001V and higher**  
   - **Key Data**: Lists insulation types, maximum operating temperatures, and applicable voltage ranges for medium/high voltage cables  
   - **Citation**: CEC Article 315.10(A)  

2. **Table 315.60(C)(10)**  
   - **Purpose**: Ampacities for **three-conductor aluminum cables** in isolated conduit in air  
   - **Application**: Medium voltage underground or overhead installations  
   - **Citation**: CEC Article 315.60(C)(10)  

3. **Table 315.60(C)(13)**  
   - **Purpose**: Ampacities for **three-conductor copper cables** in underground electrical ducts (one cable per duct)  
   - **Application**: Buried medium voltage cable runs  
   - **Citation**: CEC Article 315.60(C)(13)  

4. **Table 315.60(C)(5)**  
   - **Purpose**: Ampacities for **three-conductor copper cables** isolated in air  
   - **Application**: Overhead or aerial medium voltage installations  
   - **Citation**: CEC Article 315.60(C)(5)  

5. **Table 315.60(C)(6)**  
   - **Purpose**: Ampacities for **three-conductor aluminum cables** isolated in air  
   - **Application**: Overhead systems requiring aluminum conductors  
   - **Citation**: CEC Article 315.60(C)(6)  

6. **Table 315.60(C)(9)**  
   - **Purpose**: Ampacities for **three-conductor copper cables** in isolated conduit in air  
   - **Application**: Conduit-protected medium voltage runs  
   - **Citation**: CEC Article 315.60(C)(9)  

---

### California-Specific Notes:
- These tables are derived from **NEC Article 315** and adopted directly into CEC 2022 without amendments.  
- For **California-specific medium voltage requirements**, check:  
  - **Title 24 Part 6** (CALGreen) for energy efficiency provisions  
  - **Article 220** for load calculations impacting cable sizing  
  - **Article 250** for grounding and bonding requirements  

[OK] Source: CEC 2022

---

### cec2022-039

**Original ID:** cec-011 | **Category:** conductor_ampacity | **Tier:** delta_table

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75°C?

**Duration:** 5.0s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

**Ampacity**: **230 amperes** at 75°C (Table 310.16)

**Key Considerations**:
1. **Ambient Temperature**: This value assumes 30°C ambient temperature. If different, apply correction factors from **310.15(B)**.
2. **Conductor Count**: For more than 3 current-carrying conductors, apply bundling correction from **310.15(C)(1)**.
3. **Overcurrent Protection**: Per **240.4(D)**, 4/0 AWG copper is permitted up to **250A** overcurrent protection (ampacity of 230A must not exceed this limit).

[OK] Source: CEC 2022

---

### cec2022-040

**Original ID:** cec-012 | **Category:** grounding | **Tier:** delta_table

**Question:** What size equipment grounding conductor is required for a 200A circuit?

**Duration:** 4.3s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Equipment Grounding Conductor Size for 200A Circuit (CEC 2022)

**Required EGC Size:**
- **Copper**: 6 AWG
- **Aluminum/Copper-Clad Aluminum**: 4 AWG

**Source**: CEC 2022 Table 250.122  
**California Amendment**: Δ symbol indicates modifications from NEC in this table  

**Notes:**
1. These sizes apply to general installations. If special conditions apply (e.g., DC systems, high ground fault currents), refer to 250.4(A)(5) or (B)(4) for potential upsizing.
2. Installation restrictions (e.g., mechanical protection, routing) are covered in 250.120.

[OK] Source: CEC 2022

---

### cec2022-041

**Original ID:** cec-013 | **Category:** grounding | **Tier:** delta_table

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor?

**Duration:** 4.6s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Grounding Electrode Conductor Size (CEC 2022)

For a **3/0 AWG copper service conductor**, the required grounding electrode conductor (GEC) size is:

- **4 AWG copper**  
- **2 AWG aluminum/copper-clad aluminum**  

**Source:** CEC 2022 Table 250.66  

---

### Key Notes:
1. **California Amendment**: The table includes a California-specific modification (marked with a delta symbol) that may affect grounding electrode requirements. Always verify local amendments for exact compliance.

2. **Electrode Type Exceptions**:
   - If using a **ground rod, pipe, or plate electrode**, the GEC can be reduced to **6 AWG copper** or **4 AWG aluminum** (per 250.66(A)).
   - For a **concrete-encased electrode**, the GEC can be as small as **4 AWG copper** (per 250.66(B)).

3. **Application**: This applies to AC systems and ensures the GEC can carry fault current to the grounding electrode. If the service has parallel conductors, calculate the equivalent size as per Table 250.66 footnote [1].

---

[OK] Source: CEC 2022

---

### cec2022-042

**Original ID:** cec-014 | **Category:** ampacity_adjustment | **Tier:** delta_table

**Question:** What is the temperature correction factor for a 75°C rated conductor at 40°C ambient temperature?

**Duration:** 3.5s | **Iterations:** 3

**Tools Called:** cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Temperature Correction Factor (CEC 2022)

The temperature correction factor for a **75°C rated conductor** at **40°C ambient temperature** is **0.88** per **CEC Table 310.15(B)(1)(1)**.

[OK] Source: CEC 2022

---

### cec2022-043

**Original ID:** cec-015 | **Category:** ampacity_adjustment | **Tier:** delta_table

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway?

**Duration:** 5.3s | **Iterations:** 3

**Tools Called:** cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Ampacity Adjustment Factor for Bundling (CEC 2022)

**Adjustment Factor**: **0.7 (70%)** for 7-9 current-carrying conductors in a raceway  
**Source**: CEC 2022 Table 310.15(C)(1) [California Amendment]

**Key Notes**:
- This factor reduces the ampacity values from tables like 310.16 when multiple conductors are bundled
- Applies to **all conductors in the same raceway**, including spares and neutrals (per Table footnote)
- California amendment note confirms this applies to California's adoption of NEC 2020 Table 310.15(C)(1)

[OK] Source: CEC 2022

---

### cec2022-044

**Original ID:** cec-016 | **Category:** working_space | **Tier:** delta_table

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3?

**Duration:** 5.3s | **Iterations:** 3

**Tools Called:** cec_lookup_working_space

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Minimum Working Space Depth for 480V Panelboard (CEC 2022)

**Minimum depth**: **1.2 meters (4 feet)** per **CEC Table 110.26(A)(1)** for 480V under **Condition 3** (exposed live parts on both sides of the working space).

---

### Key Details:
- **Voltage range**: 151–600 volts
- **Condition 3**: Applies when there are exposed live parts on **both sides** of the working space (e.g., front and back of a panel with live components accessible from both sides).
- **Vertical clearance**: 6.5 feet (78 inches) above the floor is also required per **110.26(A)(2)** for working space height.

---

### Inspector Notes:
- This requirement **only addresses clearance depth** (horizontal space in front of equipment). For panel **location restrictions** (e.g., prohibited in closets/bathrooms), see **240.24(D) and (E)**.
- If live parts are on **one side** (Condition 1) or **both sides with insulation barriers** (Condition 2), the required depth is **0.9 meters (3 feet)**.

[OK] Source: CEC 2022 Table 110.26(A)(1)

---

### cec2022-045

**Original ID:** cec-017 | **Category:** enclosure | **Tier:** delta_table

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?

**Duration:** 5.2s | **Iterations:** 3

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

### Key Notes:
1. **Operability in Ice**: If the enclosure mechanism must remain operable when ice-covered (e.g., switches, breakers), **Type 3S** or **Type 3SX** are required (see footnote [*]).  
2. **Terminology**:  
   - "Raintight" applies to Types 3, 3S, 3SX, 3X, 4, 4X, 6, and 6P.  
   - "Watertight" applies to Types 4, 4X, 6, and 6P (provide additional protection against water ingress).  
3. **Corrosion Resistance**: For environments with corrosive agents, select **Type 3X**, **3RX**, **3SX**, **4X**, **6P**, or **3SX** (marked with "X" under the "Corrosive agents" row).  

**Source**: CEC 2022 Table 110.28  

[OK] Source: CEC 2022

---

### cec2022-046

**Original ID:** cec-018 | **Category:** lighting_load | **Tier:** delta_table

**Question:** What is the general lighting load in VA per square foot for office buildings?

**Duration:** 4.2s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for **office buildings** is **1.3 VA per square foot** (14 VA/m²). This value includes the 125% multiplier for continuous loads as required by **210.20(A)**.

**Source:** CEC 2022 Table 220.12 (Non-Dwelling Occupancies)  
**Footnote d:** Banks are classified as office-type occupancies.

[OK] Source: CEC 2022

---

### cec2022-047

**Original ID:** cec-019 | **Category:** flexible_cord | **Tier:** delta_table

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset)?

**Duration:** 6.7s | **Iterations:** 4

**Tools Called:** cec_lookup_table, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Ampacity of 12 AWG Flexible Cord (Column B Thermoset)

**Answer:**  
The ampacity of a 12 AWG flexible cord with thermoset insulation in **Column B** (two-conductor cords) is **25 amperes** at 30°C ambient temperature.

**Source:**  
CEC 2022 Table 400.5(A)(1) - Ampacity for Flexible Cords and Flexible Cables  
- Column B applies to two-conductor cords (footnote 2)  
- 12 AWG thermoset cord: 25A (per table)

[OK] Source: CEC 2022

---

### cec2022-048

**Original ID:** cec-020 | **Category:** fixture_wire | **Tier:** delta_table

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire?

**Duration:** 9.1s | **Iterations:** 5

**Tools Called:** cec_lookup_fixture_wire, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Maximum Operating Temperature for Type SF-2 Fixture Wire (CEC 2022)

After verifying with **CEC 2022 Table 402.3** via `cec_search`, **Type SF-2 silicone insulated fixture wire is not explicitly listed** in the referenced table data. The closest matching entries in the table are:

- **Type KF-2**: 200°C (392°F) with aromatic polyimide tape insulation  
- **Type PF**: 200°C (392°F) with fluorinated ethylene propylene insulation  

The initial lookup tool response for "SF-2" may have referenced a **California-specific amendment** or a non-standard designation. However, **Table 402.3 in the CEC 2022 does not include SF-2** in the provided search results. 

For accurate compliance, confirm the wire type designation (e.g., KF-2 or PF) and cross-reference with **CEC 2022 Section 402.3** or consult California-specific amendments for any additions to Table 402.3.

[OK] Source: CEC 2022

---

### cec2022-049

**Original ID:** cec-021 | **Category:** adjusted_ampacity | **Tier:** calculation

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40°C ambient temperature.

**Duration:** 8.1s | **Iterations:** 5

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

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
   $ 50A \times 0.88 = 44A $

3. **Bundling Adjustment**:  
   7 conductors in raceway → 0.70 factor (Table 310.15(C)(1))  
   $ 44A \times 0.70 = 30.8A $

**Final Adjusted Ampacity**: **30.8A**  
(CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1))

[OK] Source: CEC 2022

---

### cec2022-050

**Original ID:** cec-022 | **Category:** service_sizing | **Tier:** calculation

**Question:** Size the conductors, EGC, and GEC for a 200A residential service using copper conductors.

**Duration:** 4.8s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## 200A Residential Service Sizing (CEC 2022)

**1. Service Conductors**  
- **Size**: 2/0 AWG copper  
- **Table Reference**: CEC 2022 Table 310.12(A) (Dwelling Services/Feeders)  
- **Conditions**:  
  - Single-phase 120/240V system  
  - No temperature correction or bundling adjustments required  
  - Supplies entire dwelling load  

**2. Equipment Grounding Conductor (EGC)**  
- **Size**: 6 AWG copper  
- **Table Reference**: CEC 2022 Table 250.122  
- **Limiting Rule**: 240.4(D) confirms 6 AWG copper is permitted for 200A OCPD  

**3. Grounding Electrode Conductor (GEC)**  
- **Size**: 4 AWG copper  
- **Table Reference**: CEC 2022 Table 250.66 (based on 2/0 AWG service conductor)  
- **Exceptions**:  
  - If using **ground rod/pipe/plate electrode** (250.66(A)): Minimum 6 AWG copper allowed  
  - If using **concrete-encased electrode** (250.66(B)): Minimum 4 AWG copper allowed  

**California Amendments**:  
- Delta (Δ) symbols in tables indicate modifications from NEC for California-specific requirements.  

[OK] Source: CEC 2022

---

### cec2022-051

**Original ID:** cec-023 | **Category:** commercial_load | **Tier:** calculation

**Question:** Calculate the general lighting load for a 5,000 square foot office building.

**Duration:** 4.0s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## General Lighting Load Calculation for Office Building (CEC 2022)

**Calculation Steps:**

1. **Unit Load from Table 220.12:**  
   - **Occupancy Type:** Office  
   - **Unit Load:** 1.3 VA/ft² (from CEC Table 220.12, imperial column)

2. **Total Area:**  
   - 5,000 square feet

3. **General Lighting Load:**  
   $$
   5,000 \, \text{ft}^2 \times 1.3 \, \text{VA/ft}^2 = 6,500 \, \text{VA}
   $$

4. **Continuous Load Adjustment:**  
   - The 125% multiplier for continuous loads (per 210.20(A)) is **already included** in the unit load values from Table 220.12. No additional calculation required.

**Final Answer:**  
- **General Lighting Load:** 6,500 VA  

**Citations:**  
- CEC 2022 Table 220.12 (Unit Load: 1.3 VA/ft² for office)  
- CEC 2022 210.20(A) (Continuous load multiplier included in table values)  

[OK] Source: CEC 2022

---

### cec2022-052

**Original ID:** cec-024 | **Category:** motor_circuit | **Tier:** calculation

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure?

**Duration:** 6.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit (CEC 2022)

For **16 AWG copper conductors in a motor control circuit that extend beyond the enclosure**, the maximum overcurrent protection is determined by **Column C of Table 430.72(B)**:

- **16 AWG copper** → **10 amperes** (Column C)

### Code Citations:
- **CEC 2022 Section 430.72(B)(2)**: Conductors extending beyond the motor control equipment enclosure require overcurrent protection not exceeding Column C values.
- **Table 430.72(B)**: Directly specifies 10A for 16 AWG copper in Column C.

[OK] Source: CEC 2022

---

### cec2022-053

**Original ID:** cec-025 | **Category:** dwelling_load | **Tier:** calculation

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit.

**Duration:** 7.6s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No
**Service Conductor Enforced:** No

**Answer:**

## General Lighting Load for Dwelling Unit (CEC 2022)

**Answer:**  
The general lighting load for a 2,400 square foot dwelling unit is **7,200 volt-amperes (VA)**.

**Calculation:**  
- **Unit Load**: 3 VA/ft² (standard for dwelling units per CEC/NEC 220.12(A))  
- **Total Load**:  
  $$
  2,400 \, \text{ft}^2 \times 3 \, \text{VA/ft}^2 = 7,200 \, \text{VA}
  $$

**Notes:**  
- **Table 220.12** applies to **non-dwelling occupancies** (e.g., offices, retail).  
- For **dwelling units**, the CEC/NEC uses a **3 VA/ft²** baseline (not listed in Table 220.12).  
- No 125% multiplier applies here (Table 220.12’s 125% note is for **continuous loads** in non-dwelling occupancies).  

[OK] Source: CEC 2022 (based on NEC 220.12(A) for dwelling units).

---

