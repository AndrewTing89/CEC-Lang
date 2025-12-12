# CEC 2022 Unified Evaluation Results - Run 37

**Date:** 2025-12-11
**Description:** No changes - variance test - Retest without code changes to check consistency

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 53 |
| Successful | 53 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 466.4s |
| Avg Duration | 8.8s |
| Reflection Used | 53/53 |
| Reflection Improved | 9/53 |
| Hint Enforcement Triggered | 4/53 |

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

**Duration:** 8.8s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## 12 AWG Copper Conductor Ampacity (CEC 2022)

**Base Ampacity**:  
12 AWG copper at 75°C termination has a base ampacity of **25 amperes** per **Table 310.16**.

**Limiting Rules to Apply**:  
1. **Overcurrent Protection Limit** (240.4(D)):  
   - 12 AWG copper is limited to **20A maximum overcurrent protection** despite its 25A ampacity.  
   - Exception: 240.4(E)-(G) allow 25A OCP for specific applications (e.g., motors, AC units).

2. **Adjustment Factors** (if applicable):  
   - If ambient temperature ≠ 30°C → Apply correction per **310.15(B)**.  
   - If >3 current-carrying conductors → Apply bundling correction per **310.15(C)(1)**.  

**Final Answer**:  
- **Ampacity**: 25A (Table 310.16)  
- **Overcurrent Protection**: Maximum 20A (240.4(D)) unless exceptions apply.  

[OK] Source: CEC 2022

---

### cec2022-002

**Original ID:** baseline-002 | **Category:** table_lookup | **Tier:** baseline

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 4.9s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Conductor Size for 60A Circuit (CEC 2022)

**Minimum conductor size**: **6 AWG copper**  
- **Ampacity**: 65A (Table 310.16)  
- **Overcurrent protection**: Per 240.4(D), 6 AWG copper is permitted for up to **65A** OCP  

**Key Considerations**:  
1. **No exceptions apply** for standard 60A circuits (no special conditions like motor loads or fixture wires)  
2. **Limiting rules**:  
   - 240.4(D) allows 65A OCP for 6 AWG copper (matches ampacity)  
   - 8 AWG (50A) is insufficient for 60A circuits  
3. **Adjustments required if**:  
   - Ambient temperature >30°C (use 310.15(B) correction factors)  
   - More than 3 current-carrying conductors in a raceway (use 310.15(C)(1) bundling factors)  

**Final Answer**: 6 AWG copper is required for a 60A circuit at 75°C.  

[OK] Source: CEC 2022

---

### cec2022-003

**Original ID:** baseline-003 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 10.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## GFCI Protection Requirements in Residential Kitchens (CEC 2022)

**Answer:**  
In residential kitchens, **GFCI protection is required for all 125-volt through 250-volt receptacles installed to serve countertop surfaces**. This requirement is explicitly stated in **CEC 2022 Section 210.8(A)(6)**.

### Key Details:
- **Scope**: Applies to receptacles within **6 feet (1.8 meters)** of the countertop edge.
- **Exceptions**: None specified for standard kitchen countertop receptacles. Specialized equipment (e.g., permanently installed appliances) may have different rules, but countertop receptacles are explicitly covered.
- **Code Reference**:  
  **Section 210.8(A)(6)**: *"Kitchens - where the receptacles are installed to serve the countertop surfaces."*

### Supporting Context:
- **Section 210.52(B)(1)** reinforces that small-appliance branch circuits (which supply countertop receptacles) must serve these GFCI-protected outlets.
- No exceptions in the provided text exempt standard kitchen countertop receptacles from GFCI requirements.

[OK] Source: CEC 2022

---

### cec2022-004

**Original ID:** baseline-004 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 6.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms of new residential construction. This is mandated by **CEC 2022 Section 210.12(A)**, which explicitly includes bedrooms in the list of required locations for AFCI protection.

### Key Details:
- **Required for:** 15A and 20A circuits in bedrooms (and other specified areas like kitchens, living rooms, etc.).
- **Permitted methods:** Combination-type AFCI, branch/feeder-type AFCI, or outlet branch-circuit-type AFCI (see Section 210.12(A)(1)–(6) for installation requirements).
- **Exceptions:** None apply to standard bedroom circuits. Exceptions are limited to specific scenarios like fire alarm systems (not typical residential bedrooms).

**Inspector Note:** Verify that the AFCI protection method complies with the installation conditions (e.g., wiring type, distance limits for outlet-type AFCIs).  

[OK] Source: CEC 2022 Section 210.12(A)

---

### cec2022-005

**Original ID:** baseline-005 | **Category:** table_lookup | **Tier:** baseline

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 18.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Answer:**  
Yes, aluminum conductors are permitted for a 200A service. The required size is **4/0 AWG aluminum** as specified in **Table 310.12** for single-phase dwelling services.

**Citations:**  
- **Section 310.3(B):** Aluminum conductors are permitted for services.  
- **Table 310.12:** Directly lists 4/0 AWG aluminum for 200A single-phase services.  

**Inspector Note:**  
- Verify ambient temperature and bundling adjustments using **Section 310.15** if applicable.  
- Ensure insulation type complies with **Section 310.4(A)** (e.g., THWN, XHHW).  

[OK] Source: CEC 2022

---

### cec2022-006

**Original ID:** baseline-006 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 13.4s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes

**Answer:**

## Final Answer: Working Clearance Depth and Panel Location Restrictions

### **Working Clearance Depth**
The **minimum working clearance depth** required in front of a 120/240V residential electrical panel is **3 feet (900 mm)** per **CEC Table 110.26(A)(1), Condition 1**. This applies to equipment with voltage-to-ground ≤ 150V (standard residential systems).

---

### **Panel Location Restrictions (240.24(D))**
Section **240.24(D)** adds a critical **location restriction**:
- **Overcurrent devices (e.g., panels)** shall **not be located in the vicinity of easily ignitible material**, such as **clothes closets**.  
  This prohibits installing panels in areas where flammable materials (e.g., clothing, paper) are stored.

---

### **Key Takeaways**
1. **Working Clearance Depth**:  
   - **3 feet (900 mm)** in front of the panel (Table 110.26(A)(1)).  
   - **6.5 feet (78 inches)** of vertical clearance above the floor (110.26(A)(2)).  

2. **Panel Location**:  
   - **Prohibited in clothes closets** (240.24(D)).  
   - **Prohibited in bathrooms** of dwelling units (240.24(E)).  

---

### **Inspector Note**
- **Working space depth** (3 ft) and **panel location** (closets/bathrooms) are **separate requirements**.  
- Always verify both:  
  - Clearance depth for safety during maintenance.  
  - Panel location to avoid fire hazards and code violations.  

[OK] Source: CEC 2022 Table 110.26(A)(1) and Section 240.24(D).

---

### cec2022-007

**Original ID:** baseline-007 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 6.5s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Required Small Appliance Branch Circuits for Kitchen (CEC 2022)

**Answer:**  
A minimum of **two 20-ampere small-appliance branch circuits** are required for a kitchen in a dwelling unit.

**Code Basis:**  
- **CEC 2022 Section 210.52(B)(1):** Requires "two or more 20-ampere small-appliance branch circuits" to serve kitchen receptacles, including countertop outlets.  
- **CEC 2022 Section 210.11(C)(1):** Mandates "two or more 20-ampere small-appliance branch circuits" for all receptacle outlets specified in 210.52(B).  

**Key Details:**  
- These circuits must supply **all kitchen countertop receptacles** and **wall/floor receptacles** in the kitchen.  
- **No other outlets** (e.g., laundry, bathroom) may be connected to these circuits.  
- Additional small-appliance circuits are permitted but not required.  

**Exceptions:**  
None apply to reduce the minimum requirement.  

[OK] Source: CEC 2022

---

### cec2022-008

**Original ID:** baseline-008 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Is surge protection required for a new 200A residential service?

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is **required** for a new 200A residential service under **CEC 2022 Section 230.67**.  

### Requirements:
1. **Mandatory SPD Installation**:  
   - All services supplying **dwelling units** must include a **surge-protective device (SPD)** (Section 230.67(A)).  
   - The SPD must be **Type 1 or Type 2** (Section 230.67(C)).  

2. **Location**:  
   - The SPD must be an **integral part of the service equipment** or located **immediately adjacent** to it (Section 230.67(B)).  
   - *Exception*: If not integrated into the service equipment, it can be installed at the next level of distribution downstream toward the load.  

3. **Replacement**:  
   - If the service equipment is replaced, the SPD requirements must still be applied (Section 230.67(D)).  

### Key Notes:
- **Section 230.209** references surge arresters for overhead service conductors but does not override the mandatory SPD requirement in 230.67 for residential services.  
- **Section 695.15** applies specifically to fire pump controllers and is not relevant to general residential services.  

[OK] Source: CEC 2022

---

### cec2022-009

**Original ID:** core-001 | **Category:** multi_article | **Tier:** core

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 11.4s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## Service Conductor Sizing (CEC 2022)

**Required Service Conductors**:  
- **Copper**: 2/0 AWG (Table 310.12(A))  
- **Aluminum**: 4/0 AWG (Table 310.12(A))  

**Key Requirements**:  
1. **Table 310.12(A)** applies to single-phase dwelling services/feeders (120/240V or 120/208Y).  
2. **Aluminum Permissibility**:  
   - Allowed if terminations are **listed for aluminum conductors** (CEC 110.8).  
   - Verify equipment compatibility (e.g., lugs, breakers) with aluminum.  
3. **Load Consideration**:  
   - Calculated load (125A) is less than 200A service, so 200A is acceptable.  
   - No temperature/bundling adjustments needed (per question context).  

**Inspector Note**:  
- Confirm equipment is rated for aluminum if used.  
- Verify service entrance conductor sizing matches Table 310.12(A) for dwelling units.  

[OK] Source: CEC 2022

---

### cec2022-010

**Original ID:** core-002 | **Category:** multi_article | **Tier:** core

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the requirements for the circuit breaker and neutral termination?

**Duration:** 8.8s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Multiwire Branch Circuit Requirements for Kitchen Receptacles (CEC 2022)

### Circuit Breaker Requirements
1. **Simultaneous Disconnection**  
   - Per **210.4(B)**, the circuit must use a **double-pole breaker** or **two single-pole breakers with an identified handle tie** to ensure both ungrounded (hot) conductors are disconnected simultaneously.  
   - This prevents energizing the neutral conductor if only one breaker is turned off.  

2. **Breaker Rating**  
   - For 12 AWG copper conductors (12/3 cable), the maximum overcurrent protection is **20A** (per **240.4(D)**).  

---

### Neutral Termination Requirements
1. **Neutral Sizing**  
   - The neutral conductor must be **12 AWG** (same size as the ungrounded conductors) to handle the maximum unbalanced load (per **210.4(C)** and **200.4(A)**).  

2. **Neutral Grouping**  
   - Per **200.4(B)**, the neutral conductor must be **grouped with the ungrounded conductors** in the panel using wire markers, cable ties, or similar methods to avoid confusion with neutrals from other circuits.  

3. **No Overloading**  
   - The neutral must **not carry more than the unbalanced load** (difference between the two hot conductors). Harmonic currents from nonlinear loads (e.g., electronics) must be considered (see **210.4 Informational Note 1**).  

---

### Equipment Grounding Conductor (EGC)
- The **green or bare copper EGC** in the 12/3 cable must be connected to the **grounding bus** in the panel, separate from the neutral bus (per **250.146**).  

---

### Key Code Citations
- **210.4(B)**: Simultaneous disconnection of ungrounded conductors.  
- **210.4(C)**: Neutral conductor sizing for line-to-neutral loads.  
- **200.4(A)**: Neutral conductor dedicated to a single circuit.  
- **240.15(B)(1)**: Handle-tied breakers for MWBCs.  

[OK] Source: CEC 2022

---

### cec2022-011

**Original ID:** core-003 | **Category:** knowledge | **Tier:** core

**Question:** Where is GFCI protection required in a residential dwelling? List all locations.

**Duration:** 7.8s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (CEC 2022)

**All 125–250V receptacles in the following locations require GFCI protection per CEC 2022 Section 210.8(A):**

1. **Bathrooms**  
   - All receptacles.

2. **Garages and Accessory Buildings**  
   - Floor level at or below grade (storage/work areas).  
   - *Exception:* Receptacles for dedicated heating circuits (snow-melting, deicing) may follow 426.28/427.22.

3. **Outdoors**  
   - All receptacles.  
   - *Exception:* Receptacles for dedicated heating circuits (same as above).

4. **Crawl Spaces**  
   - At or below grade level.  

5. **Basements**  
   - All receptacles.  
   - *Exception:* Receptacles for fire alarm systems (not required).

6. **Kitchens**  
   - Receptacles serving countertop surfaces.

7. **Sinks**  
   - Receptacles within 1.8 m (6 ft) of the sink bowl’s top inside edge.

8. **Boathouses**  
   - All receptacles.

9. **Bathtubs/Showers**  
   - Receptacles within 1.8 m (6 ft) of the bathtub or shower stall edge.

10. **Laundry Areas**  
    - All receptacles.

11. **Indoor Damp/Wet Locations**  
    - Receptacles in locations classified as damp or wet.

**Exceptions for Specific Applications:**  
- **Ceiling Fans/Luminaires:**  
  - Listed locking receptacles for ceiling fans or luminaires are exempt if the receptacle is integral to the fixture.  
- **Industrial Exceptions:**  
  - Not applicable in residential dwellings.

**Additional Notes:**  
- **Rooftops:** Receptacles require GFCI unless not readily accessible (e.g., dedicated heating circuits).  
- **Appliances:** Specific appliances (e.g., dishwashers) may have separate GFCI requirements in 422.5, but general receptacle rules apply here.

[OK] Source: CEC 2022 Section 210.8

---

### cec2022-012

**Original ID:** core-004 | **Category:** knowledge | **Tier:** core

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 9.0s | **Iterations:** 4

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Surge Protection for Residential Service (CEC 2022)

**Answer:**  
Surge protection **is required** for all new residential services in California per **CEC 2022 Section 230.67**.  

### Requirements:
1. **Mandatory Installation**:  
   - All services supplying dwelling units **must** include a **surge-protective device (SPD)**.  
   - Applies regardless of service size (including 200A services).  

2. **SPD Type**:  
   - Must be **Type 1 or Type 2 SPD** (UL 1449-compliant).  

3. **Installation Location**:  
   - **Primary location**: SPD must be an integral part of the **service equipment** (main panel).  
   - **Alternative**: If not in the service equipment, it must be installed **immediately adjacent** to it.  
   - **Exception**: SPD can be located at the **next level of distribution downstream** (e.g., subpanel) if no service equipment SPD is present.  

4. **Replacement Rule**:  
   - If service equipment is replaced, a compliant SPD must be installed per 230.67(D).  

---

### Inspector Notes:
- **Section 230.94** allows SPDs to be installed on the **supply side** of the service disconnect if they are Type 1 devices (common for utility-side protection).  
- **Section 230.209** references surge arresters for overhead service conductors but does not override 230.67’s dwelling-specific requirement.  

[OK] Source: CEC 2022 Sections 230.67, 230.94, 230.209.

---

### cec2022-013

**Original ID:** core-005 | **Category:** edge_cases | **Tier:** core

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet code requirements?

**Duration:** 11.7s | **Iterations:** 5

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes

**Answer:**

## Final Code Compliance Assessment (CEC 2022)

**1. Panel Location in Closet:**
- ❌ **Fails 240.24(D):** Panels are **prohibited in clothes closets** regardless of clearance measurements.

**2. Front Clearance (110.26(A)(1)):**
- ❌ **Fails requirement:** 120V equipment requires **minimum 36 inches** of front clearance (only 24 inches provided).

**3. Vertical Clearance (110.26(A)(2)):**
- ⚠️ **Not evaluated:** The question does not specify vertical clearance. Code requires **6.5 ft (78 in)** of vertical working space above the floor where the panel is accessed.

**4. Lateral Clearance (Water Heater):**
- 🟨 **Not addressed by code:** 110.26(A)(1) only specifies front clearance requirements. Lateral spacing (18 inches to water heater) is not a code violation but should consider practical safety and accessibility.

**5. Section 110.26(B) Verification:**
- 🔍 **No applicable content found:** The search confirmed **no specific requirements** in 110.26(B) that apply to this scenario. The section appears to be referenced generically in other articles but contains no standalone provisions affecting this installation.

**Corrective Actions:**
1. Relocate the panel **out of the closet** (per 240.24(D))
2. Provide **minimum 36 inches of front clearance** (per 110.26(A)(1))
3. Verify **vertical clearance meets 6.5 ft** (per 110.26(A)(2))

[OK] Source: CEC 2022 Sections 240.24(D), 110.26(A)(1)

---

### cec2022-014

**Original ID:** core-006 | **Category:** edge_cases | **Tier:** core

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 6.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Multiple Conductors on a Single Terminal (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under CEC 2022.  

**Explanation:**  
- **Section 110.14(A)** requires that conductors be terminated in a manner that ensures a satisfactory mechanical and electrical connection.  
- **Section 240.5(B)** explicitly permits **two conductors on a single circuit breaker terminal** **only if the terminal is marked to indicate it is designed for two conductors**.  
- Since the breaker in question is **not marked** for two conductors, terminating two 12 AWG conductors on a single terminal violates the code.  

**Inspector Note:**  
This violation poses a risk of poor electrical contact, overheating, or terminal damage. The conductors must be reterminated using terminals marked for multiple conductors or split into separate terminals.  

[OK] Source: CEC 2022

---

### cec2022-015

**Original ID:** core-007 | **Category:** grounding_bonding | **Tier:** core

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 7.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### Key Requirements:
1. **Separate Neutral and Ground Bars**  
   - In the subpanel, **neutral and ground must be isolated** (no bonding). This differs from the main service panel where they are bonded.  
   - **Source**: CEC 250.24(D) and 250.32(B).

2. **Equipment Grounding Conductor (EGC) Size**  
   - The EGC from the house panel to the subpanel must be sized per **Table 250.122** based on the feeder's overcurrent protection rating.  
   - Example: For a 100A feeder, use **8 AWG copper** (Table 250.122).  

3. **Grounding Electrode Conductor (GEC) Size**  
   - The GEC from the subpanel to the local grounding electrode (e.g., ground rod) must be sized per **Table 250.66** based on the largest conductor in the feeder.  
   - Example: For 2/0 AWG copper feeders, use **4 AWG copper** (Table 250.66).  

4. **Local Grounding Electrode Requirement**  
   - A detached structure **must have a grounding electrode** (e.g., ground rod) even if the feeder includes an EGC.  
   - The GEC to this electrode is **not required to be larger than 6 AWG copper** if it connects only to a rod/pipe electrode (250.66(A)).  

5. **No Bonding of Neutral and Ground**  
   - The subpanel’s neutral bus must not be bonded to the enclosure or grounding system. All grounding is provided via the EGC and local electrode.  

---

### Example Configuration for a 100A Feeder:
- **Feeder Conductors**: 3 AWG copper (ungrounded), 3 AWG copper (neutral).  
- **EGC**: 8 AWG copper (Table 250.122 for 100A).  
- **GEC to Ground Rod**: 6 AWG copper (Table 250.66 for 3 AWG feeders).  

---

### Inspector Notes:
- **Verify Separation**: Ensure neutral and ground bars are physically separated in the subpanel.  
- **Check GEC Size**: Confirm the grounding electrode conductor complies with Table 250.66.  
- **Local Grounding**: A ground rod is required even if the feeder includes an EGC.  

[OK] Source: CEC 2022 Sections 250.24, 250.32, 250.66, 250.122

---

### cec2022-016

**Original ID:** core-008 | **Category:** grounding_bonding | **Tier:** core

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 8.2s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
- **Main Bonding Jumper** (CEC 2022 Section 100):  
  Connects the **grounded circuit conductor** to the **equipment grounding conductor** at the **service**.  
  *Purpose*: Ensures electrical continuity between the grounded conductor and equipment grounding at the service point.

- **System Bonding Jumper** (CEC 2022 Section 100):  
  Connects the **grounded conductor** to the **supply-side bonding jumper** or **equipment grounding conductor** at a **separately derived system** (e.g., transformers, generators).  
  *Purpose*: Bonds the system’s grounded conductor to the equipment grounding system at the source of a separately derived system.

---

### **Key Differences**
| Feature | **Main Bonding Jumper** | **System Bonding Jumper** |
|---------|--------------------------|---------------------------|
| **Location** | At the **service** (primary power source). | At the **source of a separately derived system** (e.g., transformer, generator). |
| **Application** | Required for **services** (per 250.28). | Required for **separately derived systems** (per 250.28 and 250.168). |
| **Sizing** | Based on the **largest ungrounded service conductor** (Table 250.102(C)(1)). | Based on the **largest ungrounded conductor of the separately derived system** (Table 250.102(C)(1)). |

---

### **When Each is Required**
1. **Main Bonding Jumper** (CEC 2022 250.28):  
   - **Required** for all **grounded services**.  
   - Must be installed at **each service enclosure** if the service has multiple enclosures (per 250.28(D)(2)).  
   - Example: A residential service with a main panel and a subpanel requires a main bonding jumper in each enclosure.

2. **System Bonding Jumper** (CEC 2022 250.28 and 250.168):  
   - **Required** for **separately derived systems** (e.g., transformers, solar inverters, generators).  
   - Must be installed at the **first disconnecting means** of the derived system.  
   - Example: A 480V-to-208V transformer requires a system bonding jumper at its output panel.

---

### **Sizing Requirements**
Both jumpers are sized using **Table 250.102(C)(1)** based on the largest ungrounded conductor:  
- **Copper Conductors**:  
  - For a 400 kcmil service conductor, the main bonding jumper is **2/0 AWG** (Table 250.102(C)(1)).  
- **Aluminum Conductors**:  
  - For a 600 kcmil service conductor, the system bonding jumper is **1/0 AWG** (Table 250.102(C)(1)).  

**Special Cases**:  
- If conductors exceed 1100 kcmil copper or 1750 kcmil aluminum, the bonding jumper must be at least **12.5% of the largest conductor’s area** (Note 1, Table 250.102(C)(1)).  

---

### **Inspector Notes**
- **Main bonding jumpers** are part of the service and must never be used as a substitute for grounding electrodes.  
- **System bonding jumpers** are critical for separately derived systems to prevent dangerous voltage shifts between systems.  
- Both must be made of **copper, aluminum, or corrosion-resistant materials** (250.28(A)).  

[OK] Source: CEC 2022

---

### cec2022-017

**Original ID:** core-009 | **Category:** load_calculations | **Tier:** core

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 6.5s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

### **1. Required Number of 20A Small Appliance Branch Circuits for a Kitchen**
- **Minimum Requirement**: **At least two 20-ampere small-appliance branch circuits** are required for the kitchen in a dwelling unit.  
- **Code Basis**: CEC 2022 **210.11(C)(1)** mandates this requirement as part of the general receptacle load calculations.  
- **Load Calculation**: Each circuit is calculated at **1,500 volt-amperes (VA)** for load calculations (CEC 220.52(A)).  

### **2. Can These Circuits Serve Dining Room Receptacles?**
- **Yes**, the two 20A small-appliance branch circuits **must also supply receptacles in the kitchen, pantry, and dining room**.  
- **Code Basis**: CEC 2022 **210.11(C)(1)** explicitly includes dining room receptacles within the scope of these circuits.  

### **Key Code References**
- **210.11(C)(1)**: Requires two 20A small-appliance branch circuits for kitchens, pantries, and dining rooms.  
- **220.52(A)**: Specifies the 1,500 VA load per circuit for calculations.  

[OK] Source: CEC 2022

---

### cec2022-018

**Original ID:** core-010 | **Category:** load_calculations | **Tier:** core

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 9.2s | **Iterations:** 6

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   12 AWG THHN copper at 90°C = **30A** (Table 310.16)

2. **Temperature Correction Factor**:  
   Ambient 50°C → 0.82 (Table 310.15(B)(1)(1))

3. **Bundling Adjustment Factor**:  
   6 conductors → 0.8 (Table 310.15(C)(1))

4. **Adjusted Ampacity**:  
   $ 30A \times 0.82 \times 0.8 = 19.68A $

**Final Answer**:  
**19.7A** adjusted ampacity (30A base × 0.82 × 0.8)

[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)

---

### cec2022-019

**Original ID:** core-011 | **Category:** why_questions | **Tier:** core

**Question:** Why is AFCI protection required for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 13.4s | **Iterations:** 4

**Tools Called:** cec_search, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## AFCI Protection Requirements (CEC 2022)

**AFCI protection is required for bedrooms and living areas to prevent electrical fires caused by arc faults.**

### Code Basis:
- **CEC 2022 Section 210.12(A)** mandates AFCI protection for all 120V, 15/20A branch circuits in dwelling units supplying outlets in bedrooms, living rooms, and similar areas.
- **Arc-Fault Circuit Interrupter (AFCI) Definition** (Section 100): A device that detects arc faults and de-energizes the circuit to prevent fire hazards.

### Electrical Hazard Prevented:
Arc faults generate high heat (up to 10,000°F) and can ignite surrounding materials. Common causes include:
- Damaged insulation
- Loose connections
- Overloaded circuits
- Faulty appliances

AFCIs distinguish between normal arcing (e.g., switches) and dangerous arcing (e.g., damaged wiring), interrupting the circuit before a fire starts.

[OK] Source: CEC 2022

---

### cec2022-020

**Original ID:** core-012 | **Category:** why_questions | **Tier:** core

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 5.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

**Why Torque Specifications Are Important:**  
Proper torque ensures secure, low-resistance electrical connections that maintain mechanical integrity and prevent overheating. Under-torqued connections can loosen over time, while over-torqued connections may damage terminals or insulation.

**Code Requirements:**  
1. **CEC 2022 Section 110.14(D)**  
   - Requires tightening torque values to be **indicated on equipment** or in **manufacturer installation instructions**.  
   - Mandates use of an **approved means** (e.g., torque tools, shear bolts, or breakaway devices) to achieve specified torque.  
   - **Informational Notes**:  
     - Contact manufacturers if torque values are not provided.  
     - Refer to UL 486A-486B or NFPA 70B for torque guidance.  

2. **CEC 2022 Section 430.9(C)**  
   - Control circuit devices with screw-type terminals using 14 AWG or smaller copper conductors must be torqued to **at least 0.8 N·m (7 lb-in.)** unless otherwise identified.  

3. **CEC 2022 Section 230.81**  
   - Service conductor connections must use **pressure connectors or clamps**, not solder.  

**Key Principle**: Always follow **manufacturer-specified torque values** to comply with 110.14(D).  

[OK] Source: CEC 2022

---

### cec2022-021

**Original ID:** inspection-001 | **Category:** panel_load_calculation | **Tier:** inspection

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 17.5s | **Iterations:** 4

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Service Load Calculation (CEC 2022)

### Step 1: General Lighting Load (3000 sq ft × 3 VA/sq ft = 9000 VA)  
- **Demand Factor**:  
  - First 3000 VA @ 100% = 3000 VA  
  - Remaining 6000 VA @ 35% = 2100 VA  
  - **Total**: 5100 VA  
  (CEC 220.52(A) with Table 220.42)

### Step 2: Small Appliance & Laundry Circuits  
- **2 × 1500 VA (small appliance) + 1 × 1500 VA (laundry) = 4500 VA**  
  - Included in general lighting load and subjected to demand factors  
  (CEC 220.52(A)(B))

### Step 3: Range Load (12 kW)  
- **8000 VA** (Table 220.55, Column B)  
  (CEC 220.55)

### Step 4: Dryer Load (5.5 kW)  
- **5500 VA** (nameplate rating)  
  (CEC 220.54)

### Step 5: Air Conditioner (4600 VA × 1.25 = 5750 VA)  
- Continuous load multiplier  
  (CEC 220.10(A))

### Step 6: Total Load Calculation  
- **Total Load = 5100 (lighting) + 4500 (appliances) + 8000 (range) + 5500 (dryer) + 5750 (AC) = 28,850 VA**  
- **Convert to Amperes**: 28,850 VA ÷ 240V = **120.21A**

### Step 7: Panel Sizing  
- **200A panel > 120.21A calculated load**  
  (CEC 220.85)

[OK] Source: CEC 2022

---

### cec2022-022

**Original ID:** inspection-002 | **Category:** clearance_violations | **Tier:** inspection

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL code violations.

**Duration:** 20.7s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_lookup_working_space, cec_search, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes

**Answer:**

## Electrical Panel Inspection Violations (CEC 2022)  

### **1. Insufficient Working Space Depth**  
- **Violation**: Panel has **28 inches** of depth clearance in front, but **36 inches (3 ft)** is required for 120V equipment under **Condition 1** (Table 110.26(A)(1)).  
- **Citation**: CEC 2022 Table 110.26(A)(1)  
- **Impact**: Workers cannot safely access the panel for servicing.  

---

### **2. Obstruction in Working Space**  
- **Violation**: Water heater located **16 inches** to the left of the panel intrudes into the required **3 ft (36 in)** working space.  
- **Citation**: CEC 2022 Section 110.26(B) ("Working space shall not be used for storage or obstructions").  
- **Impact**: Creates a hazard by limiting access and increasing risk of accidental contact.  

---

### **3. Potential Vertical Clearance Issue**  
- **Violation**: Panel is mounted at **5 ft height**, but **6.5 ft (78 in)** of vertical clearance is required above the floor in the working space (Section 110.26(A)(2)).  
- **Citation**: CEC 2022 Section 110.26(A)(2)  
- **Note**: If the ceiling height is less than 6.5 ft above the floor, this violates the code. The question does not specify ceiling height, so this violation is **conditional**.  

---

### **4. Panel Location Compliance**  
- **No Violation Identified**: The question does not indicate the panel is in a prohibited location (e.g., clothes closet, bathroom). **Section 240.24(D)** prohibits panels near easily ignitable materials (e.g., clothes closets), but this is not mentioned in the scenario.  

---

### **Summary of Required Corrections**  
1. **Increase depth clearance** to **36 inches** in front of the panel.  
2. **Relocate the water heater** to eliminate obstruction within the working space.  
3. **Verify ceiling height** to ensure **6.5 ft of vertical clearance** above the floor.  

[OK] Source: CEC 2022

---

### cec2022-023

**Original ID:** inspection-005 | **Category:** gfci_afci_compliance | **Tier:** inspection

**Question:** New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide code references.

**Duration:** 10.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Circuit Protection Requirements for Kitchen Installations (CEC 2022)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **GFCI**
- **Code Reference**: CEC 210.8(A)(6)  
  *Kitchens - receptacles installed to serve countertop surfaces must have GFCI protection.*
- **Rationale**: Countertop receptacles are explicitly required to have GFCI protection to prevent electric shock hazards from water exposure.

---

### 2. **Dishwasher (Dedicated 15A Circuit)**
- **Protection Required**: **GFCI**
- **Code Reference**: CEC 422.5(B)(3)  
  *Appliances like dishwashers must have GFCI protection unless exceptions apply.*
- **Rationale**: Dishwashers are listed in 422.5(B)(3) as appliances requiring GFCI protection due to proximity to water sources.

---

### 3. **Garbage Disposal (Dedicated 15A Circuit)**
- **Protection Required**: **GFCI**
- **Code Reference**: CEC 422.5(B)(3)  
  *Same as dishwasher; garbage disposals are moisture-prone appliances requiring GFCI.*
- **Rationale**: Garbage disposals are also listed in 422.5(B)(3) for GFCI protection due to similar water exposure risks.

---

### 4. **Refrigerator (Dedicated 20A Circuit)**
- **Protection Required**: **Standard Breaker (No GFCI)**
- **Code Reference**: CEC 210.8(A)(6) *Exception* and 422.5(B)(3) *Exception*  
  *Refrigerators are exempt from GFCI requirements to prevent unnecessary tripping that could spoil food.*
- **Rationale**: While GFCI is required for countertop circuits, refrigerators are not classified as countertop appliances. They are excluded from 422.5(B)(3) as essential appliances where GFCI tripping could cause safety or operational issues.

---

### Summary Table

| Circuit Type               | Protection Required | Code Reference          |
|---------------------------|---------------------|--------------------------|
| Countertop Receptacles    | GFCI                | 210.8(A)(6)             |
| Dishwasher                | GFCI                | 422.5(B)(3)             |
| Garbage Disposal          | GFCI                | 422.5(B)(3)             |
| Refrigerator              | Standard Breaker    | 210.8(A)(6) Exception   |

---

### Inspector Notes
- **GFCI vs. AFCI**: None of these circuits require **AFCI** protection (210.12 applies only to bedroom circuits).
- **Refrigerator Exception**: Refrigerators are explicitly exempt from GFCI requirements in 422.5(B)(3) due to their critical function.
- **Appliance-Specific Rules**: Always verify appliance type against 422.5(B)(3) for GFCI requirements.

[OK] Source: CEC 2022

---

### cec2022-024

**Original ID:** inspection-006 | **Category:** subpanel_violations | **Tier:** inspection

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 8.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Subpanel Bonding Violations in Detached Garage (CEC 2022)

### **Identified Violations**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation**: 250.24(D) prohibits bonding neutral (grounded) and equipment grounding conductors on the load side of the service disconnect.  
   - **Issue**: The main bonding jumper (connecting neutral and ground bars) is incorrectly installed in the subpanel. This creates parallel paths for fault currents and violates the single-point bonding requirement.  

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: 250.24(D) and 250.32(B)(1) require the neutral (grounded) conductor to be isolated from the equipment grounding system in subpanels.  
   - **Issue**: Bonding the neutral bar to the enclosure creates an unintended path for fault currents and violates the separation of neutral and ground in separately derived systems (subpanels).  

3. **Missing Grounding Electrode Conductor (GEC)**  
   - **Violation**: 250.32(B)(1) mandates a grounding electrode conductor for all buildings/structures supplied by feeders.  
   - **Issue**: No GEC is mentioned connecting the subpanel’s grounding system to a local grounding electrode (e.g., ground rod).  

---

### **Correct Configuration**
1. **Neutral and Ground Bars**  
   - **Neutral Bar**: Connected only to the feeder neutral conductor.  
   - **Ground Bar**: Connected to the feeder equipment grounding conductor and bonded to the subpanel enclosure.  
   - **Isolation**: Neutral and ground bars must be physically separated (no bonding jumper).  

2. **Grounding Electrode Conductor (GEC)**  
   - **Size**: Per Table 250.66, for #2 AWG aluminum feeders:  
     - **Copper**: 6 AWG (CEC Table 250.66).  
     - **Aluminum**: 4 AWG (CEC Table 250.66).  
   - **Connection**: Run from the ground bar to a local grounding electrode (e.g., 8 ft ground rod).  

3. **Equipment Grounding Conductor**  
   - **Size**: Per Table 250.122 for 100A subpanel:  
     - **Copper**: 8 AWG (CEC Table 250.122).  
     - **Aluminum**: 6 AWG (CEC Table 250.122).  
   - **Connection**: Connect the feeder ground conductor to the ground bar (not the neutral bar).  

4. **Enclosure Bonding**  
   - The ground bar must be bonded to the subpanel enclosure (per 250.32(B)(1)), but the neutral bar must remain isolated.  

---

### **Inspector Notes**
- **Violation 1**: Remove the main bonding jumper between neutral and ground bars.  
- **Violation 2**: Disconnect the neutral bar from the enclosure.  
- **Violation 3**: Install a GEC (6 AWG copper or 4 AWG aluminum) from the ground bar to a grounding electrode.  

[OK] Source: CEC 2022 Sections 250.24, 250.32, Table 250.66, Table 250.122

---

### cec2022-025

**Original ID:** inspection-007 | **Category:** conduit_fill | **Tier:** inspection

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 7.3s | **Iterations:** 4

**Tools Called:** cec_lookup_conduit_fill, cec_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Calculation:**
1. **Conduit Fill Limit:**  
   - RMC 1¼" total area = 1.526 sq in (Chapter 9 Table 4)  
   - 40% fill limit = 0.61 sq in  

2. **Conductor Area:**  
   - 10 AWG THHN area = 0.0211 sq in (Chapter 9 Table 5)  

3. **Maximum Conductors:**  
   $$
   \frac{0.61\ \text{sq in}}{0.0211\ \text{sq in/conductor}} = 28.91 \rightarrow \textbf{28 conductors}
   $$

**Verification:**  
- 28 conductors × 0.0211 = 0.5908 sq in (≤ 0.61 sq in limit)  
- Fill percentage = (0.5908 / 1.526) × 100 ≈ **38.7%**  

**Answer:**  
A 1¼-inch RMC conduit can accommodate a maximum of **28** 10 AWG THHN conductors at 40% fill.  

[OK] Source: CEC 2022 Chapter 9 Tables 4 and 5

---

### cec2022-026

**Original ID:** inspection-008 | **Category:** voltage_drop | **Tier:** inspection

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet the 3% maximum recommendation for branch circuits?

**Duration:** 8.8s | **Iterations:** 4

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Voltage Drop Calculation (CEC 2022)

1. **Verify Conductor Resistance**:
   - **CEC 2022 Chapter 9 Table 8** confirms 12 AWG copper conductors have **1.93 Ω/1000ft** (solid) or **1.98 Ω/1000ft** (stranded) at 75°C.
   - The problem states **1.29 Ω/1000ft**, which is **lower than code values**. This suggests either:
     - A temperature correction factor was applied (not mentioned in the problem)
     - A non-standard conductor type
     - A calculation error in the problem statement

2. **Voltage Drop Formula**:
   $$
   VD = \frac{2 \times I \times R \times L}{1000}
   $$
   Where:
   - $ I = 22 \, \text{A} $
   - $ R = 1.29 \, \Omega/\text{1000 ft} $ (as given in problem)
   - $ L = 50 \, \text{ft} $

3. **Calculation**:
   $$
   VD = \frac{2 \times 22 \times 1.29 \times 50}{1000} = \frac{2838}{1000} = 2.84 \, \text{V}
   $$

4. **Percentage Voltage Drop**:
   $$
   \text{Percentage} = \left( \frac{2.84}{120} \right) \times 100 = 2.37\%
   $$

5. **Code Compliance Check**:
   - **3% maximum recommendation** for branch circuits (CEC 210.19(A)(1) Informational Note No. 4)
   - **2.37% ≤ 3%**: ✅ Meets the requirement

6. **Important Note**:
   - The resistance value **1.29 Ω/1000ft** used in this calculation **does not match CEC Table 8 values** for 12 AWG copper (1.93–1.98 Ω/1000ft at 75°C). If using code-compliant values:
     $$
     VD = \frac{2 \times 22 \times 1.93 \times 50}{1000} = 4.25 \, \text{V} \quad (3.54\%)
     $$
     This would **exceed** the 3% recommendation.

**Final Answer**:
- **Voltage Drop**: 2.84 volts (based on problem's resistance value)
- **Percentage**: 2.37%
- **Compliance**: ✅ Meets 3% recommendation **if** the problem's resistance value is correct
- **Code-Compliant Value**: 4.25 volts (3.54%) would exceed 3% using CEC Table 8 values

[OK] Source: CEC 2022 Chapter 9 Table 8

---

### cec2022-027

**Original ID:** inspection-009 | **Category:** derating_calculation | **Tier:** inspection

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 10.6s | **Iterations:** 7

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG TW copper (60°C rating) = **20A** (Table 310.16)

**Step 2: Temperature Correction**  
Ambient = 43°C → 0.71 correction factor (Table 310.15(B)(1)(1))  
20A × 0.71 = **14.2A**

**Step 3: Bundling Adjustment**  
6 conductors → 0.8 adjustment factor (Table 310.15(C)(1))  
14.2A × 0.8 = **11.36A**

**Final Adjusted Ampacity**: **11.36A**

**Code References**:  
- Base ampacity: Table 310.16  
- Temperature correction: Table 310.15(B)(1)(1)  
- Bundling adjustment: Table 310.15(C)(1)  

[OK] Source: CEC 2022

---

### cec2022-028

**Original ID:** inspection-010 | **Category:** grounding_electrode_conductor | **Tier:** inspection

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 4.9s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Minimum Size Copper GEC for 1000 kcmil Service (CEC 2022)

**Answer:**  
The minimum size **copper grounding electrode conductor (GEC)** required is **2/0 AWG**.

**Key Details:**  
- **Service Equivalent Size:** 4 × 250 kcmil = 1000 kcmil (per Table 250.66 footnote [1])  
- **Table Reference:** CEC 2022 Table 250.66, row for "Over 600 through 1100" kcmil service conductors  
- **California Amendment:** Applies (delta symbol noted)  

**Exceptions to Note:**  
If the grounding electrode is:  
- **Ground rod/pipe/plate electrode** → GEC may be reduced to **6 AWG copper** (250.66(A))  
- **Concrete-encased electrode** → GEC may be reduced to **4 AWG copper** (250.66(B))  

**Inspector Note:**  
The 2/0 AWG copper GEC is required unless one of the exceptions applies. Verify the type of grounding electrode used to determine if a smaller size is permitted.  

[OK] Source: CEC 2022

---

### cec2022-029

**Original ID:** cec-001 | **Category:** panelboard_requirements | **Tier:** california_specific

**Question:** What are the panelboard space requirements for single-family dwellings? What appliances must have reserved circuit breaker spaces?

**Duration:** 8.7s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Panelboard Space Requirements and Reserved Circuit Breaker Spaces (CEC 2022)

### **Panelboard Space Requirements for Single-Family Dwellings**
**CEC 2022 Section 408.2(A)** mandates that panelboards in **single-family residential buildings** must include **reserved circuit breaker spaces** for specific appliances as required by the **California Energy Code**. Specifically:
- **Required reserved spaces**: 
  - Heat pump water heaters
  - Heat pump space heaters
  - Electric cooktops
  - Electric clothes dryers

This requirement ensures future-proofing for energy-efficient appliances and aligns with **California Energy Code Sections 150.0(n), 150.0(t), 150.0(u), and 150.0(v)**.

---

### **Reserved Circuit Breaker Spaces for Appliances**
The following appliances **must have dedicated circuit breaker spaces** in panelboards:
1. **Heat Pump Water Heaters**  
2. **Heat Pump Space Heaters**  
3. **Electric Cooktops**  
4. **Electric Clothes Dryers**  

**Source**: CEC 2022 **Section 408.2(A)** for single-family dwellings and **Section 408.2(B)** for multifamily buildings.

---

### **Additional Key Requirements**
- **Panelboard Location Restrictions** (CEC 2022 **Section 240.24**):  
  - Prohibited in **clothes closets** (240.24(D)).  
  - Prohibited in **bathrooms of dwelling units** (240.24(E)).  

---

[OK] Source: CEC 2022

---

### cec2022-030

**Original ID:** cec-002 | **Category:** ev_charging | **Tier:** california_specific

**Question:** What are the electrical requirements for EV charging infrastructure in new residential construction?

**Duration:** 8.8s | **Iterations:** 3

**Tools Called:** cec_search, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Electrical Requirements for EV Charging in New Residential Construction (CEC 2022)

### 1. **Core Requirements from Article 625**
- **Individual Branch Circuits** (625.40):  
  Each EV charging outlet must be supplied by a **dedicated branch circuit** with **no other outlets** on the same circuit.  
  - *Example*: A 50A circuit for a Level 2 charger must be dedicated solely to that charger.

- **Location Requirements** (625.50):  
  EVSE (Electric Vehicle Supply Equipment) must be installed at a height of **≥450mm (18") above floor** (indoor) or **≥600mm (24") above grade** (outdoor).  
  - *Exception*: Portable EVSE is exempt from height requirements.

- **Ventilation** (625.52):  
  Indoor EV charging requires ventilation if equipment is not listed for indoor use. Minimum ventilation rates depend on charger amperage (see Table 625.52(B)(1)(a)/(b)).  
  - *Example*: A 50A, 240V charger requires **24 cfm** of ventilation.

- **Ground-Fault Protection** (625.56):  
  All EV charging receptacles must have **GFCI protection for personnel**.  
  - Reset switches must be **readily accessible**.

---

### 2. **California-Specific Mandates (CALGreen)**
- **EV Readiness** (625.1.1):  
  New residential construction must comply with **CALGreen Chapter 4, Division 4.1** and **Chapter 5, Division 5.1**, which require:  
  - **Pre-wiring** for EV charging in all new single-family homes.  
  - **Dedicated circuits** sized for Level 2 charging (typically 60A–100A).  
  - **Panelboard spaces** reserved for EV circuits (see 408.2(A)/(B)).

---

### 3. **Panelboard Requirements**
- **Dedicated Spaces** (408.2(A)/(B)):  
  Panelboards in new residential buildings must include **circuit breaker spaces** for:  
  - Heat pump water heaters  
  - Electric cooktops  
  - Electric clothes dryers  
  - **EV charging equipment**  
  - *Example*: A 200A panel must have at least **4 dedicated spaces** for these loads.

- **Overcurrent Protection** (408.36):  
  Panelboards must be protected by an overcurrent device **not exceeding the panel’s rating**.  
  - *Exception*: Existing panelboards in residential units may bypass this rule.

---

### 4. **Key Exceptions and Notes**
- **Portable EVSE** (625.44(A)):  
  Portable chargers are allowed without fixed installation requirements (e.g., height restrictions).  
- **Ventilation Exemption** (625.52(A)):  
  Ventilation is not required if equipment is listed for indoor use **or** uses storage batteries.

---

### 5. **Inspector Checklist**
- ✅ Dedicated branch circuit for each EV outlet  
- ✅ GFCI protection on all EV circuits  
- ✅ Panelboard spaces reserved for EV loads  
- ✅ Compliance with CALGreen pre-wiring mandates  
- ✅ Ventilation if charging indoors (per Table 625.52)  
- ✅ EVSE height requirements met  

[OK] Source: CEC 2022, CALGreen, and referenced tables.

---

### cec2022-031

**Original ID:** cec-003 | **Category:** solar_pv | **Tier:** california_specific

**Question:** What are the electrical requirements for solar PV systems on new residential construction?

**Duration:** 10.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## California Solar PV System Requirements (CEC 2022)

### 1. **Rapid Shutdown Requirements (690.12)**
- **Voltage Limits**:  
  - Conductors **outside the array boundary** must drop to ≤30V within 30 seconds.  
  - Conductors **inside the array boundary** must either:  
    - Use a **listed PV hazard control system**, or  
    - Drop to ≤80V within 30 seconds.  
- **Initiation Devices**:  
  - Must be **readily accessible** (e.g., service disconnect, PV disconnect, or dedicated switch).  
  - For multi-system installations, no more than **6 switches/breakers** in a single enclosure.  
- **Labeling**:  
  - Permanent labels at service equipment:  
    - **"SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN"** (yellow background, 9.5mm min. text).  
    - **"RAPID SHUTDOWN SWITCH"** label on the switch (red background, 9.5mm min. text).  

---

### 2. **System Grounding (690.41-43)**
- **Ground-Fault Protection**:  
  - Required for DC circuits >30V or >8A. Exceptions:  
    - ≤2 modules in parallel (non-building locations).  
- **Grounding Configurations**:  
  - Solidly grounded, functionally grounded, or ungrounded systems permitted.  
  - Solidly grounded systems must connect to a grounding electrode per **250.52**.  
- **Equipment Grounding**:  
  - Size per **Table 250.122** based on overcurrent protection (assume 125% of inverter output for sizing).  

---

### 3. **Wiring Methods (690.31)**
- **Conductor Types**:  
  - Use **Type PV** or **DG cable** (UL 4703/3003 listed).  
  - Exposed outdoor runs require **sunlight-resistant insulation** (e.g., RHW-2, USE-2).  
- **Ampacity Adjustments**:  
  - Use **Table 690.31(A)(b)** for 105°C/125°C conductors.  
  - Apply **temperature correction factors** from Table 690.31(A)(a) for ambient >30°C.  
- **Spacing & Support**:  
  - Secure cables every **1.8m (6ft)**.  
  - Exposed runs must be **guarded** or in **Type MC cable**.  

---

### 4. **Labeling & Identification (690.51-56)**
- **Voltage Labels**:  
  - Permanent label at PV disconnect showing **maximum system voltage** (per 690.7).  
- **Circuit Identification**:  
  - DC conductors must be marked with **+/- polarity** (non-green/white insulation).  
  - AC modules: Follow inverter labeling requirements.  

---

### 5. **Additional Requirements**
- **Arc-Fault Protection (690.11)**:  
  - Required for DC circuits ≥80V (unless in metallic raceways or underground).  
- **Location Restrictions**:  
  - No PV equipment in **bathrooms** (690.4(E)).  
  - Disconnects must be **readily accessible** (not in clothes closets).  
- **Stand-Alone Systems**:  
  - Follow **Article 710** for battery-based systems.  

---

### Key Tables for Sizing
- **Table 690.31(A)(b)**: Ampacities for 105°C/125°C conductors.  
- **Table 250.122**: Equipment grounding conductor sizes.  

[OK] Source: CEC 2022

---

### cec2022-032

**Original ID:** cec-004 | **Category:** heat_pump | **Tier:** california_specific

**Question:** What circuit requirements exist for heat pump water heaters in new dwelling units?

**Duration:** 8.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Circuit Requirements for Heat Pump Water Heaters in New Dwellings (CEC 2022)

### **Key Requirements**
1. **Dedicated Circuits**  
   - **Single-family buildings** (1–2 dwellings): Each dwelling unit must have **designated branch circuits** for heat pump water heaters as specified in **California Energy Code Section 150.0(n)**.  
   - **Multifamily buildings**: Each dwelling unit must have **dedicated circuits** per **California Energy Code Section 160.9**.  

2. **Panelboard Provisions**  
   - Panelboards serving dwelling units must include **circuit breaker spaces** for heat pump water heaters (and other appliances) as required by:  
     - **CEC 408.2(A)** (single-family): Circuit breaker spaces for heat pump water heaters, cooktops, and dryers.  
     - **CEC 408.2(B)** (multifamily): Circuit breaker spaces for heat pump water heaters and other appliances.  

3. **Compliance with Energy Code**  
   - Specific circuit sizing, receptacle locations, and identification requirements are detailed in:  
     - **California Energy Code Section 150.0(n)** (single-family).  
     - **California Energy Code Section 160.9** (multifamily).  

---

### **Code Citations**
- **CEC 2022 Section 422.3(A)–(B)**: Mandates dedicated circuits and panelboard spaces for heat pump water heaters in single- and multifamily buildings.  
- **CEC 2022 Section 408.2(A)–(B)**: Requires panelboards to include spaces for heat pump water heaters.  

---

### **Inspector Notes**
- Verify that **circuit breaker spaces** in panelboards comply with the Energy Code provisions.  
- Ensure **dedicated circuits** are labeled and sized per the manufacturer’s specifications and Energy Code.  
- Cross-reference with **California Energy Code Sections 150.0(n) and 160.9** for detailed requirements on circuit ampacity, conductor size, and installation.  

[OK] Source: CEC 2022

---

### cec2022-033

**Original ID:** cec-005 | **Category:** electrification | **Tier:** california_specific

**Question:** What is required for electric cooktop readiness in new homes?

**Duration:** 6.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Electric Cooktop Readiness Requirements (CEC 2022)

**CEC 2022 Section 422.3 mandates electric cooktop readiness in new California homes as follows:**

### **Single-Family Buildings (1–2 Dwellings)**
- **Dedicated circuits and circuit identification** must be provided per **California Energy Code §150.0(u)**.  
- This includes:  
  - **Designated branch circuits** sized for electric cooktop loads (typically 40–50A).  
  - **Labeling** to identify circuits for future installation.  

### **Multifamily Buildings**
- **Dedicated circuits and identification** required per **California Energy Code §160.9(b)**.  
- Same requirements as single-family for circuit sizing and labeling.  

**Key Notes:**  
- The California Energy Code (separate from CEC) specifies exact ampacity and circuit requirements (e.g., 40A minimum for most cooktops).  
- Compliance ensures readiness for future electric cooktop installation without retrofitting.  

[OK] Source: CEC 2022 Section 422.3, California Energy Code referenced provisions.

---

### cec2022-034

**Original ID:** cec-006 | **Category:** electrification | **Tier:** california_specific

**Question:** What are the panelboard requirements for electric clothes dryer circuits in new construction?

**Duration:** 6.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

**Panelboards in new residential construction must include dedicated circuit breaker spaces for electric clothes dryers as mandated by the California Energy Code.**

### Key Requirements:
1. **Single-Family Buildings**  
   - Panelboards must provide circuit breaker spaces for electric clothes dryers per **California Energy Code Section 150.0(n), (t), (u), and (v)**.  
   - Example: A typical 30A, 240V circuit for dryers requires a dedicated 30A breaker space.

2. **Multifamily Buildings**  
   - Panelboards must include spaces for electric clothes dryers as specified in **California Energy Code Section 160.9(a), (b), and (c)**.  
   - Dryer circuits must be sized per load calculations (typically 5,000W for dryers, per NEC 220.54).

3. **General Panelboard Rules**  
   - Overcurrent protection must comply with **408.36**, ensuring the panelboard’s overcurrent device rating does not exceed its design rating.  
   - Grounding requirements are covered in **408.40**, requiring proper bonding of metal frames and terminal bars.

**Inspector Note:** Verify the panelboard’s listed capacity and ensure spaces are reserved for future dryer installations, even if the dryer is not yet installed. California Energy Code mandates these spaces to ensure compliance with efficiency and safety standards.

[OK] Source: CEC 2022, Sections 408.2, 408.36, 408.40

---

### cec2022-035

**Original ID:** cec-007 | **Category:** overcurrent | **Tier:** california_specific

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Duration:** 7.7s | **Iterations:** 4

**Tools Called:** cec_lookup_table, cec_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## CEC Table 240.4(G) Unique California Specifications (CEC 2022)

**Answer:**  
CEC Table 240.4(G) cross-references overcurrent protection requirements for specialized conductors, with **California amendments (δ)** indicating modifications from the NEC. The unique California aspects include:

1. **Fire Alarm Systems**  
   - References **Chapter 9 Tables 12(A) and 12(B)** for fire alarm system conductors (760.43/45).  
   - California may impose stricter sizing or protection rules for fire alarm circuits compared to NEC.

2. **Remote-Control/Signaling Circuits**  
   - Directs to **Chapter 9 Tables 11(A) and 11(B)** for power-limited circuits (725.43/45).  
   - California amendments might adjust ampacity or insulation requirements for these circuits.

3. **Motor-Operated Appliance Circuits**  
   - References **Article 422, Part II** with potential California-specific exceptions for appliances like dishwashers or garbage disposals.

4. **Secondary Tie Conductors**  
   - Applies **450.6** with possible California adjustments for transformer overcurrent protection in commercial/industrial settings.

**Inspector Note:**  
The δ symbol in the CEC indicates where California modified NEC Table 240.4(G). For exact amendments, consult the **CEC delta notes** (California-specific changes) in the full code document, as this table alone does not specify the exact nature of the modifications.

[OK] Source: CEC 2022 Table 240.4(G)

---

### cec2022-036

**Original ID:** cec-008 | **Category:** surge_protection | **Tier:** california_specific

**Question:** What does CEC Table 242.3 specify for installations?

**Duration:** 3.7s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## CEC Table 242.3 Overview (CEC 2022)

**Table 242.3** in the California Electrical Code (CEC) 2022 provides a **cross-reference guide** for overvoltage protection requirements. It specifies which National Electrical Code (NEC) articles contain additional overvoltage protection requirements for specific equipment types. This table is a **California-specific addition** (marked with an "N") not found in the base NEC.

### Key Equipment and Corresponding Articles:
- **Class I locations** → NEC Article 501
- **Elevators/dumbwaiters** → NEC Article 620
- **Emergency systems** → NEC Article 700
- **Fire pumps** → NEC Article 695
- **Information technology equipment** → NEC Article 645
- **Wind electric systems** → NEC Article 694

### Purpose:
This table helps electricians and inspectors quickly identify which specialized NEC articles apply to different installations for overvoltage protection requirements beyond the general rules in **Article 242**.

[OK] Source: CEC 2022 Table 242.3 (California-specific amendment)

---

### cec2022-037

**Original ID:** cec-009 | **Category:** motor_control | **Tier:** california_specific

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Duration:** 10.3s | **Iterations:** 4

**Tools Called:** cec_lookup_table, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022) **WITH EXCEPTIONS**

---

### **Table Structure & Key Values**  
Specifies **maximum overcurrent protective device (OCPD) ratings** for motor control circuits based on:  
- **Conductor size** (18 AWG to larger than 10 AWG)  
- **Columns A, B, C** (installation/configuration):  
  - **Column A**: Direct OCPD limits (e.g., 7A for 18 AWG copper).  
  - **Column B**: 400% of Table 310.19 (60°C) values for larger conductors.  
  - **Column C**: 300% of Table 310.16 (60°C) values for larger conductors.  

---

### **Critical Exceptions**  
1. **Exception No. 1 (430.72(B))**:  
   - **Hazardous control circuits** (e.g., fire pump motors):  
     - Overcurrent protection **may be omitted** if the control circuit’s opening creates a hazard.  
     - Only **short-circuit and ground-fault protection** is required.  

2. **Exception No. 2 (430.72(B))**:  
   - **Transformer-supplied control circuits**:  
     - Permitted to use **primary-side overcurrent protection** for single-phase, two-wire transformers.  
     - OCPD rating must not exceed:  
       $ \text{Secondary OCPD (Table 430.72(B))} \times \frac{\text{Secondary Voltage}}{\text{Primary Voltage}} $.  

---

### **Application Requirements**  
- **Small Conductors (18–12 AWG)**:  
  - Use direct values from Columns A/B/C.  
  - Example: 12 AWG copper in Column B = **120A maximum OCPD**.  

- **Large Conductors (>10 AWG)**:  
  - **Column B**: $ 400\% \times \text{Table 310.19 (60°C)} $.  
  - **Column C**: $ 300\% \times \text{Table 310.16 (60°C)} $.  
  - Example: 8 AWG copper in Column B:  
    1. Table 310.19 (60°C) = 40A.  
    2. $ 40A \times 400\% = 160A $ maximum OCPD.  

---

### **Inspector Notes**  
- **Column A** applies to control circuits **tapped from motor branch-circuit OCPD**.  
- **Columns B/C** apply to circuits requiring **separate overcurrent protection** (e.g., extending beyond motor control enclosures).  
- **Termination Temperature Limits**: Ensure OCPD ratings match conductor termination temperatures (110.14(C)).  

---

### **Cross-Reference Compliance**  
- **Table 310.19**: For Column B calculations (60°C conductors).  
- **Table 310.16**: For Column C calculations (60°C conductors).  

[OK] Source: CEC 2022  
[VERIFIED] Answer is complete.

---

### cec2022-038

**Original ID:** cec-010 | **Category:** medium_voltage | **Tier:** california_specific

**Question:** What medium voltage cable tables exist that are California-specific?

**Duration:** 9.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Medium Voltage Cable Tables in CEC 2022 (California)

The California Electrical Code (CEC) 2022 addresses medium voltage (MV) cables primarily in **Article 311** and **Article 392**, with specific tables for ampacity and installation requirements. Below are the key California-specific medium voltage cable tables and their applications:

---

### **1. Medium Voltage Cable Ampacity Tables**
These tables determine the allowable current-carrying capacity (ampacity) for Type MV cables (2001–35,000 volts nominal):

#### **Table 311.60(C)(75) & 311.60(C)(76)**  
- **Application**: Multiconductor MV cables in cable trays.  
- **Conditions**:  
  - 95% of listed ampacities permitted if cable trays are continuously covered with solid unventilated covers for >1.8 m (6 ft).  
  - Ampacities adjusted for spacing and environmental factors (e.g., ambient temperature).  

#### **Table 311.60(C)(69) & 311.60(C)(70)**  
- **Application**: Single-conductor MV cables in cable trays.  
- **Conditions**:  
  - 75% of ampacities for uncovered trays; 70% if trays are covered >1.8 m (6 ft).  
  - Adjustments for conductor size (≥1/0 AWG) and configuration (e.g., triangular/triplexed).  

#### **Table 311.60(C)(67) & 311.60(C)(68)**  
- **Application**: Single-conductor MV cables in triangular/square configurations.  
- **Conditions**:  
  - Ampacities based on spacing (≥2.15× conductor diameter) and free air circulation.  

---

### **2. Cable Tray Installation Tables**
These tables govern the physical installation of MV cables in cable trays, including fill limits and spacing:

#### **Table 392.22(A) & 392.22(B)**  
- **Application**: Fill limits for multiconductor and single-conductor cables in ladder, ventilated trough, or solid bottom trays.  
- **Key Provisions**:  
  - Maximum allowable fill area based on cable size and tray width.  
  - Special rules for 4/0 AWG or larger cables (single-layer installation).  

#### **Table 392.22(A)(5) & 392.22(A)(6)**  
- **Application**: Ventilated and solid channel cable trays.  
- **Conditions**:  
  - Cross-sectional area limits for multiconductor cables.  

---

### **3. General MV Cable Requirements**
- **Section 311.1**: Scope covers Type MV cables (2001–35,000 volts nominal).  
- **Section 311.60**: Requires engineering supervision or use of listed tables for ampacity determination.  
- **Section 392.80(B)**: Ampacity adjustments for MV cables in trays (e.g., 75% for 600 kcmil+ cables in uncovered trays).  

---

### **California-Specific Notes**
- **Title 24 Compliance**: California mandates additional energy efficiency and safety provisions for MV systems, including derating factors for environmental conditions.  
- **CALGreen Requirements**: May impose stricter guidelines for cable insulation materials and fire resistance in certain applications.  

---

[OK] Source: CEC 2022 (Incorporates NEC with California amendments).

---

### cec2022-039

**Original ID:** cec-011 | **Category:** conductor_ampacity | **Tier:** delta_table

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75°C?

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

**Base ampacity**: **230 amperes** at 75°C (Table 310.16).  

**Important Considerations**:  
1. **Temperature correction**: If ambient temperature ≠ 30°C, apply correction factors from **310.15(B)**.  
2. **Bundling adjustment**: For >3 current-carrying conductors, apply derating from **310.15(C)(1)**.  
3. **Overcurrent protection**: Maximum overcurrent protection per **240.4(D)** is **250A** for 4/0 AWG copper.  

[OK] Source: CEC 2022 Table 310.16 with California amendment.

---

### cec2022-040

**Original ID:** cec-012 | **Category:** grounding | **Tier:** delta_table

**Question:** What size equipment grounding conductor is required for a 200A circuit?

**Duration:** 4.6s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Equipment Grounding Conductor Size for 200A Circuit (CEC 2022)

**Required EGC Size:**
- **Copper**: 6 AWG (200A column in Table 250.122)
- **Aluminum/Copper-Clad Aluminum**: 4 AWG (200A column in Table 250.122)

**Key Notes:**
1. **California Amendment**: The table includes modifications from the base NEC (marked by the delta symbol △).
2. **Footnote Compliance**: 
   - If 250.4(A)(5) or (B)(4) applies (e.g., higher ground fault current requirements), a larger conductor may be needed.
   - Installation restrictions apply (see 250.120 for details like secure connections and mechanical protection).

**Source**: CEC 2022 Table 250.122

[OK] Source: CEC 2022

---

### cec2022-041

**Original ID:** cec-013 | **Category:** grounding | **Tier:** delta_table

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor?

**Duration:** 6.8s | **Iterations:** 4

**Tools Called:** cec_lookup_grounding_conductor, cec_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

[VERIFIED] Answer is complete.  

The answer correctly addresses the GEC size for a 3/0 AWG copper service conductor (4 AWG copper or 2 AWG aluminum) with direct citations to **CEC 2022 Table 250.66**. It includes:  
1. **Size requirements** for both copper and aluminum.  
2. **Exceptions** for electrode types (250.66(A) and 250.66(B)).  
3. **California amendment** note.  
4. **Footnotes** clarifying application conditions.  

The cross-reference to **250.64** in the original tool response relates to *installation* requirements (not sizing), which are outside the scope of the user’s question. Since the user specifically asked about *size*, no further action is required. All claims are supported by code citations, and exceptions were explicitly checked and included.

---

### cec2022-042

**Original ID:** cec-014 | **Category:** ampacity_adjustment | **Tier:** delta_table

**Question:** What is the temperature correction factor for a 75°C rated conductor at 40°C ambient temperature?

**Duration:** 4.4s | **Iterations:** 4

**Tools Called:** cec_lookup_ampacity_adjustment, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

[VERIFIED] Answer is complete. The exceptions found relate to grounding requirements in specific conduit types and do not affect the temperature correction factor calculation for ampacity adjustments. The answer remains valid with the cited correction factor of 0.88 from Table 310.15(B)(1)(1).

---

### cec2022-043

**Original ID:** cec-015 | **Category:** ampacity_adjustment | **Tier:** delta_table

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway?

**Duration:** 4.2s | **Iterations:** 3

**Tools Called:** cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Ampacity Adjustment Factor for Bundling (CEC 2022)

[OK] **Adjustment factor**: 0.70 (70%) for 7-9 current-carrying conductors in a raceway  
[OK] **Source**: CEC Table 310.15(C)(1) [California Amendment]

**Key Details**:
- Applies to conductors rated 40°C or higher (per Table 310.15(C)(1) footnote)
- Conductors must be the same size and type in the raceway
- Adjustment factor reduces ampacity to account for heat buildup

[OK] Source: CEC 2022

---

### cec2022-044

**Original ID:** cec-016 | **Category:** working_space | **Tier:** delta_table

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3?

**Duration:** 15.2s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes

**Answer:**

## Panelboard Location Restrictions (CEC 2022)

After verifying **Section 240.24(D)** through `cec_search`, the CEC 2022 contains the following requirement:

### **240.24(D) – Prohibition in Clothes Closets**
> **Panelboards shall not be installed in clothes closets.**

This section explicitly prohibits the installation of panelboards in **clothes closets** due to safety and accessibility concerns. However, this requirement is **separate from working space depth calculations** and applies only to **location restrictions**.

---

### Key Takeaways:
1. **Working Space Depth**: Still governed by **Table 110.26(A)(1)** (4 ft for 480V, Condition 3).
2. **Location Restriction**: Panelboards **must not** be installed in **clothes closets** (240.24(D)).
3. **Other Location Rules**:  
   - **240.24(E)**: Prohibits panelboards in **bathrooms of dwelling units**.  
   - **110.26(B)**: Requires **dedicated space** above and below equipment (no shelves, etc.).

---

### Final Answer:
- **Minimum working space depth**: **4 ft (1.2 m)** for 480V panelboards under Condition 3 (Table 110.26(A)(1)).  
- **Location restriction**: Panelboards **must not** be installed in **clothes closets** (240.24(D)).

[OK] Source: CEC 2022

---

### cec2022-045

**Original ID:** cec-017 | **Category:** enclosure | **Tier:** delta_table

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?

**Duration:** 4.7s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Suitable Enclosure Types for Outdoor Use (CEC 2022)

**Answer:**  
For outdoor use with rain, sleet, and ice, the suitable enclosure types per Table 110.28 are:  
- **Type 3S** (Rainproof, dusttight, and operable when ice-covered)  
- **Type 3SX** (Same as 3S with additional corrosion protection)  
- **Type 4** (Watertight, dusttight, and operable when ice-covered)  
- **Type 4X** (Same as Type 4 with corrosion protection)  
- **Type 6** (Watertight, dusttight, and operable when ice-covered)  
- **Type 6P** (Same as Type 6 with corrosion protection)  

**Key Requirements:**  
1. **Watertight/Raintight:** Types 4, 4X, 6, and 6P are explicitly "watertight" (footnote [1]), providing protection against sleet and ice.  
2. **Operability in Ice:** All listed types include the requirement that the mechanism must be operable when ice-covered (footnote [*]).  
3. **Dusttight:** These types are also dusttight (footnote [1]), suitable for hazardous locations if needed.  

**Inspector Note:**  
- **Type 3S/3SX** are rainproof but not watertight, making them less suitable for heavy sleet/ice.  
- **Type 4/4X/6/6P** are preferred for severe weather due to their watertight rating.  

[OK] Source: CEC 2022 Table 110.28

---

### cec2022-046

**Original ID:** cec-018 | **Category:** lighting_load | **Tier:** delta_table

**Question:** What is the general lighting load in VA per square foot for office buildings?

**Duration:** 7.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for office buildings is **1.3 volt-amperes per square foot (14 VA/m²)** as specified in **Table 220.12** of the California Electrical Code 2022.

This value includes the 125% continuous load multiplier required by 210.20(A) for lighting calculations. No additional adjustments are required for this base load calculation unless specified by energy codes or demand factors (see 220.42 for demand factors, if applicable).

[OK] Source: CEC 2022 Section 220.12, Table 220.12

---

### cec2022-047

**Original ID:** cec-019 | **Category:** flexible_cord | **Tier:** delta_table

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset)?

**Duration:** 5.2s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Ampacity of 12 AWG Flexible Cord (Column B Thermoset) - CEC 2022

The ampacity for a **12 AWG flexible cord** with **Column B thermoset insulation** (Types S, SJ, etc.) is **25 amperes** under normal ambient conditions (30°C/86°F), as specified in **CEC 2022 Table 400.5(A)(1)**.

### Key Details:
- **Column B** applies to **two-conductor cords** or multiconductor cords where only **two conductors are current-carrying**.
- This rating assumes the cord is used in accordance with **Article 400** and **Table 400.5** conditions.
- For different conductor counts or ambient temperatures, additional adjustments may apply (see 400.5 and 400.13).

[OK] Source: CEC 2022 Table 400.5(A)(1)

---

### cec2022-048

**Original ID:** cec-020 | **Category:** fixture_wire | **Tier:** delta_table

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire?

**Duration:** 10.2s | **Iterations:** 5

**Tools Called:** cec_lookup_fixture_wire, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Maximum Operating Temperature for Type SF-2 (CEC 2022)

[OK] **Maximum operating temperature**: 200°C (392°F)  
- Confirmed by **CEC 2022 Table 402.3** (fixture wire specifications)  
- Cross-verified in **Section 620.11(A)(1)** (elevator conductor requirements)  
- Supported by **Table 310.4(A)** (FEPB insulation at 200°C for special applications)  

[OK] Source: CEC 2022

---

### cec2022-049

**Original ID:** cec-021 | **Category:** adjusted_ampacity | **Tier:** calculation

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40°C ambient temperature.

**Duration:** 10.8s | **Iterations:** 6

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Base ampacity**: 50A (8 AWG THWN copper at 75°C)  
**Temperature correction factor**: 0.88 (40°C ambient)  
**Bundling correction factor**: 0.7 (7 conductors)  

**Calculation**:  
$$
50A \times 0.88 \times 0.7 = 30.8A
$$

**Final adjusted ampacity**: **30.8 amperes**  

**Citations**:  
- Base ampacity: CEC 2022 Table 310.16  
- Temperature correction: Table 310.15(B)(1)(1)  
- Bundling correction: Table 310.15(C)(1)  

**Inspector Note**:  
- California amendments apply to Tables 310.15(B)(1)(1) and 310.15(C)(1).  
- The adjusted ampacity must comply with 240.4(D) overcurrent protection limits if applicable.  

[OK] Source: CEC 2022

---

### cec2022-050

**Original ID:** cec-022 | **Category:** service_sizing | **Tier:** calculation

**Question:** Size the conductors, EGC, and GEC for a 200A residential service using copper conductors.

**Duration:** 13.1s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Service Sizing (CEC 2022)

**1. Service Conductors**  
- **Size**: 2/0 AWG copper  
- **Source**: CEC Table 310.12(A) (Dwelling Service/Feeder)  
- **Applies when**: Supplying entire load of a dwelling unit with 120/240V single-phase system  

**2. Equipment Grounding Conductor (EGC)**  
- **Size**: 6 AWG copper  
- **Source**: CEC Table 250.122 (for 200A overcurrent device)  

**3. Grounding Electrode Conductor (GEC)**  
- **Size**: 4 AWG copper  
- **Source**: CEC Table 250.66 (based on 2/0 AWG service conductor)  

**Inspector Note**:  
- Table 310.12(A) provides dwelling-specific conductor sizes (permissive).  
- Table 310.16 would require 250 kcmil copper for 200A (more conservative).  
- California mandates Title 24 compliance for residential grounding electrode systems (Section 250.50).  

[OK] Source: CEC 2022

---

### cec2022-051

**Original ID:** cec-023 | **Category:** commercial_load | **Tier:** calculation

**Question:** Calculate the general lighting load for a 5,000 square foot office building.

**Duration:** 4.7s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## General Lighting Load Calculation for Office Building (CEC 2022)

**Calculation:**
1. **Unit Load for Office**: 1.3 VA/ft² (from Table 220.12)
2. **Building Area**: 5,000 ft²
3. **Total Lighting Load**:  
   $ 5,000 \, \text{ft}^2 \times 1.3 \, \text{VA/ft}^2 = 6,500 \, \text{VA} $

**Key Notes:**
- The 125% continuous load multiplier from 210.20(A) is **already included** in the unit load value per Table 220.12.
- No additional demand factors apply for general lighting load calculations per Article 220.

[OK] Source: CEC 2022 Table 220.12

---

### cec2022-052

**Original ID:** cec-024 | **Category:** motor_circuit | **Tier:** calculation

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure?

**Duration:** 12.9s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit (CEC 2022)

**Answer:**  
The maximum overcurrent protection for 16 AWG copper conductors in a motor control circuit is **10A**, per **Table 430.72(B)**.

**Key Code References:**  
1. **430.72(B)**: Directly specifies 10A maximum OCP for 16 AWG copper in motor control circuits.  
2. **430.72(A)**: Requires motor control circuit conductors to be no smaller than 16 AWG copper.  
3. **240.4(D)**: General overcurrent rules do not apply here due to the specific exception in 430.72(B).  

**Inspector Note:**  
- 16 AWG is only permitted for motor control circuits (not general branch circuits).  
- Verify the application meets all motor control circuit requirements in Article 430.  

[OK] Source: CEC 2022

---

### cec2022-053

**Original ID:** cec-025 | **Category:** dwelling_load | **Tier:** calculation

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit.

**Duration:** 7.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## General Lighting Load Calculation (CEC 2022)

**Calculation:**  
For dwelling units, the general lighting load is calculated at **3 volt-amperes per square foot** (CEC 2022 Section 220.14(J)).  

$$
2,400 \, \text{ft}^2 \times 3 \, \text{VA/ft}^2 = 7,200 \, \text{VA}
$$

**Result:**  
The general lighting load for a 2,400 ft² dwelling unit is **7,200 volt-amperes**.  

[OK] Source: CEC 2022 Section 220.14(J)

---

