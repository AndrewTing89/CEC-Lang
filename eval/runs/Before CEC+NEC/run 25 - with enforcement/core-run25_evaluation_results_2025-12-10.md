# Core (NEC) Evaluation Results - Run 25

**Date:** 2025-12-10
**Changes:** Memory clearing + Tool enforcement

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 221.5s |
| Avg Duration | 8.2s |
| Exception Search Used | 1/27 |
| NEC Comparison Used | 1/27 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 4.6s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size**: **6 AWG copper**  
- **Ampacity**: 65A (Table 310.16 at 75°C)  
- **Overcurrent protection**: Permitted up to 65A (Section 240.4(D))  

**Key Considerations**:  
1. **Base Rule**: Table 310.16 establishes 65A ampacity for 6 AWG copper at 75°C.  
2. **Limiting Rule**: Section 240.4(D) allows 65A OCPD for 6 AWG copper (no conflict with 60A circuit).  
3. **Exceptions**: No applicable exceptions for this application.  

**California vs. NEC**:  
- Same result under NEC 2023 (Table 310.16).  
- No California amendments affect this calculation.  

[OK] Source: CEC 2022 Tables 310.16, 240.4(D)

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 8.1s

**Tools Called:** cec_search

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**GFCI protection is required for all 125-volt through 250-volt receptacles in residential kitchens that serve countertop surfaces**, as specified in **CEC 210.8(A)(6)**. This includes receptacles installed to provide power for appliances or countertop use.

### Key Details:
1. **Scope**: Applies to dwelling units (homes), covering kitchens with countertops.
2. **Exceptions**:
   - Listed locking support and mounting receptacles for ceiling luminaires or fans are exempt **if** they are not general-purpose convenience receptacles. If a general-purpose receptacle is integral to the fixture, GFCI protection is still required.
3. **Additional Context**:
   - Per **210.52(B)(3)**, countertop receptacles must be supplied by small-appliance branch circuits, but this does not override the GFCI requirement in 210.8(A)(6).

### Code Citations:
- **CEC 210.8(A)(6)**: Direct requirement for countertop receptacles.
- **CEC 210.8(A)(10)**: Laundry areas (adjacent to kitchens) also require GFCI, but this is separate from countertop requirements.

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 4.9s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction in California per **CEC 2022 Section 210.12(A)**.  

### Key Requirements:
- **Scope**: All 120V, single-phase, 15- and 20-ampere branch circuits supplying outlets or devices in dwelling unit bedrooms must be protected by AFCI.
- **Permitted Methods**:  
  1. Combination-type AFCI at the circuit origin.  
  2. Branch/feeder-type AFCI combined with outlet branch-circuit AFCI.  
  3. Supplemental arc protection circuit breaker with outlet AFCI (under specific conditions).  
  4. Outlet branch-circuit AFCI at the first outlet (under specific conditions).  

### Exceptions:
- Not required for circuits supplying fire alarm systems (per 760.41(B)/760.121(B)) if installed in metal raceway or armored cable.  
- Extensions ≤6 ft without additional outlets are exempt (210.12(D)).  

**Source**: CEC 2022 Section 210.12(A) and exceptions.  

[OK] Source: CEC 2022

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 3.9s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Yes**, aluminum conductors are permitted for a 200A service. The required size is:

- **4/0 AWG aluminum**  
- **Reference**: CEC Table 310.12(A) (Single-Phase Dwelling Services and Feeders)

### Key Requirements:
1. **Table 310.12(A)** specifies conductor sizes for dwelling services based on service rating.
2. **4/0 AWG aluminum** provides an ampacity of **200A** at 75°C (per the 75°C column in the table).
3. **Conditions of Use**: 
   - No temperature correction factors required (ambient ≤ 30°C).
   - Conductors supply the entire load of the dwelling unit.
   - System is 120/240V or 120/208Y single-phase.

### Additional Notes:
- If temperature corrections or bundling adjustments are needed, recalculate using `cec_ampacity_with_adjustments`.
- For equipment grounding conductor (EGC), refer to **Table 250.122** (e.g., 4 AWG copper or 6 AWG aluminum for 200A service).

[OK] Source: CEC 2022

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 3.5s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Working Clearance Requirement (CEC 2022)

The minimum depth of working clearance required in front of a 120/240V residential electrical panel is **900 mm (3 feet)**. This applies under **Condition 1**, where:

- Exposed live parts are on one side of the working space
- No live or grounded parts are on the other side (e.g., against a non-conductive wall)

**Citation:** CEC 2022 Table 110.26(A)(1) for voltages 0-150V to ground.

[OK] Source: CEC 2022

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 5.2s

**Tools Called:** cec_search

**Answer:**

## Minimum Small Appliance Branch Circuits for Kitchen (CEC 2022)

**Answer:**  
A minimum of **2** 20-ampere small-appliance branch circuits are required for a kitchen per CEC 2022.

**Code Basis:**  
- **CEC 210.52(B)(1):** Requires **not fewer than two** 20-ampere small-appliance branch circuits to serve kitchen receptacles (including countertop outlets).  
- **CEC 210.11(C)(1):** Mandates **two or more** 20-ampere small-appliance branch circuits for dwelling units.  

**Key Requirements:**  
1. Both circuits must supply **all kitchen receptacles** (wall, countertop, and floor outlets).  
2. **No other outlets** are permitted on these circuits (Exception No. 1 and 2 apply to specific cases like clocks or gas appliances).  
3. Each circuit must serve **only one kitchen**.  

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 5.0s

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for Residential Service (NEC 2023)

**Answer:**  
Yes, surge protection is required for a new 200A residential service per **NEC 2023 Section 230.67(A)**. This section mandates surge-protective devices (SPD) for services supplying **dwelling units**, which includes residential services.

### Key Details:
- **Applicability**: Applies to all dwelling units (single-family, multi-family, etc.).
- **SPD Type**: Any listed SPD suitable for the application.
- **Installation**: Must be installed in accordance with Article 285 (SPD requirements).

[OK] Source: NEC 2023

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 13.6s

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, compare_with_nec

**Answer:**

## Service Conductor Sizing for 200A Upgrade (CEC 2022)

### **1. Service Conductor Size**
- **Copper**: **2/0 AWG** (CEC Table 310.12(A))
- **Aluminum**: **4/0 AWG** (CEC Table 310.12(A))

**Notes:**
- Table 310.12(A) applies to single-phase dwelling services/feeders.
- No temperature correction or bundling adjustments required (standard conditions assumed).

---

### **2. Equipment Grounding Conductor (EGC)**
- **Copper**: **6 AWG**
- **Aluminum**: **4 AWG**  
  *(Per CEC Table 250.122 for 200A OCPD)*

---

### **3. Grounding Electrode Conductor (GEC)**
- **Copper**: **4 AWG** (for 4/0 AWG service conductor)
- **Aluminum**: **2 AWG**  
  *(Per CEC Table 250.66 for service conductor size 4/0 AWG)*

---

### **4. Aluminum Use Compliance**
- **Yes**, aluminum is permitted for service conductors (CEC Table 310.12(A)).
- **Key Requirements:**
  - Use **4/0 AWG aluminum** for 200A service.
  - Ensure proper termination at breakers/outlets (anti-oxidant compound and torque compliance).
  - Verify panel compatibility with aluminum conductors (most modern panels are rated for AL/CU).

---

### **5. California vs. NEC Comparison**
- **No amendments** to Table 310.12(A) in CEC 2022 (identical to NEC 2023).
- Aluminum sizing for 200A service is **4/0 AWG** in both codes.

---

### **Final Answer**
- **Service Conductors**: 2/0 AWG copper or 4/0 AWG aluminum.
- **Aluminum is allowed** with proper installation practices.
- **Grounding Conductors**: 6 AWG copper/4 AWG aluminum (EGC), 4 AWG copper/2 AWG aluminum (GEC).

[OK] Source: CEC 2022 Tables 310.12(A), 250.122, 250.66

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 8.0s

**Tools Called:** nec_search

**Answer:**

## NEC Requirements for Multiwire Branch Circuit in Kitchen (NEC 2023)

### Circuit Breaker Requirements:
1. **Simultaneous Disconnection** (NEC 210.4(B)):  
   - The circuit must be protected by a **2-pole circuit breaker** or **single-pole breakers with handle ties** to ensure **all ungrounded (hot) conductors are disconnected simultaneously** at the panel.  
   - This prevents energizing the neutral conductor if only one hot leg is turned off.

2. **Ampere Rating**:  
   - For kitchen receptacles, the branch circuit must be **20 amperes** (NEC 210.52(K)).  
   - The breaker must match the conductor size (12 AWG copper = 20A per NEC Table 310.16).

---

### Neutral Termination Requirements:
1. **Neutral Sizing**:  
   - The **neutral conductor must be 12 AWG** (same size as hots in 12/3 cable) to carry the full unbalanced load between the two hot conductors.  
   - Smaller neutrals are prohibited for multiwire circuits (NEC 210.4(D)).

2. **Grouping Conductors**:  
   - All conductors (hots and neutral) **must remain grouped together** in the same raceway or cable (NEC 210.4(D)).  
   - This prevents neutral current imbalance and ensures proper load sharing.

3. **No Overloading**:  
   - The neutral must **not be shared** with other circuits unless sized for combined loads (NEC 250.20(B)).  
   - For this dedicated kitchen circuit, the 12 AWG neutral is sufficient.

---

### Additional Notes:
- **Voltage Consideration**: A 12/3 cable implies a 120V circuit (two hots on different phases and a neutral).  
- **Load Limitation**: The total load on the circuit must not exceed 20A (NEC 210.23(A)).  
- **GFCI Protection**: Required for kitchen receptacles per NEC 210.8(A)(6).

[OK] Source: NEC 2023

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 9.7s

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

According to **NEC 2023 Section 210.8(A)**, GFCI protection is required for all 120–250V receptacles in the following locations in residential dwellings:

1. **Bathrooms**  
2. **Garages** and accessory buildings with floors at or below grade (non-habitable, for storage/work areas)  
3. **Outdoors**  
4. **Crawl spaces** at or below grade level  
5. **Kitchens**  
6. **Areas with sinks** and permanent provisions for food/preparation (e.g., utility sinks)  
7. **Within 6 feet (1.8 m)** of the top inside edge of sink bowls  
8. **Boathouses**  
9. **Within 6 feet (1.8 m)** of bathtubs or shower stalls (outside edge)  
10. **Laundry areas**  
11. **Indoor damp or wet locations**  

---

### Key Notes:
- **Exceptions** apply for specific equipment (e.g., HVAC, snow-melting systems) but do not remove general location requirements.  
- **Additional requirements** in **210.8(D)** expand GFCI to outdoor outlets not covered elsewhere.  
- **AFCI protection** (Section 210.12) is separate and applies to bedrooms, living areas, etc., but is not GFCI.  

[OK] Source: NEC 2023

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 7.3s

**Tools Called:** cec_search

**Answer:**

## Surge Protection Requirements for Residential Services (CEC 2022)

**Answer:**  
The California Electrical Code (CEC 2022) does **not explicitly mandate** surge protection for residential services. However, **NEC Article 285** (adopted by CEC) provides **optional installation guidelines** for surge protective devices (SPDs). Key points:

1. **Permitted Locations for SPDs** (per NEC 285.2):  
   - **Service equipment** (main service panel)  
   - **Branch circuits** (e.g., for sensitive electronics)  
   - **Load side of the main disconnect**  

2. **California-Specific Considerations**:  
   - No CEC amendments explicitly require SPDs for residential services.  
   - Local jurisdictions may adopt additional requirements.  

3. **Best Practice**:  
   - Install SPDs at the **service entrance** for whole-house protection.  
   - Use listed SPDs with **10/350 µs waveform rating** (per NEC 285.2).  

[OK] Source: CEC 2022 (adopting NEC 285)  
[OK] No direct CEC mandate found via `cec_search("surge protection residential service")`

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 10.4s

**Tools Called:** nec_lookup_working_space

**Answer:**

## Working Space Requirements (NEC 2023)

The installation **does not meet NEC requirements** due to insufficient working space:

1. **Front clearance**: 
   - **24 inches provided** vs. **36 inches minimum required** (900 mm/3 ft) per NEC Table 110.26(A)(1) for 120V equipment.
   - This fails the minimum depth requirement regardless of side obstructions.

2. **Side clearance consideration**:
   - The water heater (grounded part) creates **Condition 2** (exposed live parts on one side, grounded parts on the other).
   - **Condition 2 still requires 36 inches of working space depth** in front of the panel.
   - The 18-inch side clearance to the water heater is irrelevant to the **minimum 36-inch front clearance** requirement.

**Key NEC Reference**:  
NEC 2023 Table 110.26(A)(1) mandates **36 inches (3 ft)** of working space in front of electrical equipment for systems up to 150V to ground.

[OK] Source: NEC 2023

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 4.6s

**Tools Called:** nec_search

**Answer:**

## Code Violation Check (NEC 2023)

[OK] **Yes**, this is a code violation under NEC 240.13(B). The terminal is not marked for two conductors, which is required when connecting multiple conductors to a single terminal.

### Key Details:
- **NEC 240.13(B)**: Requires terminals for multiple conductors to be "so designed and identified for such use."
- **Terminal Marking**: The breaker terminal must be explicitly marked/rated for multiple conductor connections (e.g., "2-wire" or similar).
- **Physical Fit ≠ Compliance**: Even if two wires physically fit, they must be connected to a terminal **specifically rated** for that purpose.

[OK] Source: NEC 2023

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 9.7s

**Tools Called:** cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_search, cec_exception_search

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### 1. **Grounding Electrode System**
- **Requirement**: Install a grounding electrode system per **CEC 250.50**.  
  - Bond all grounding electrodes (e.g., ground rods, concrete-encased electrodes) at the garage.  
  - Minimum 2.5 m (8 ft) driven ground rod or equivalent electrode must be installed.  

### 2. **Equipment Grounding Conductor (EGC)**
- **Size**: Based on the overcurrent protection (100A feeder):  
  - **Copper**: 8 AWG (Table 250.122)  
  - **Aluminum**: 6 AWG (Table 250.122)  
- **Connection**: Run with the feeder and connect to:  
  - The **grounding bar** in the subpanel.  
  - The **local grounding electrode system** (via GEC).  

### 3. **Grounding Electrode Conductor (GEC)**
- **Size**: Based on the service conductor size (assume 3/0 AWG copper for a 200A service):  
  - **Copper**: 4 AWG (Table 250.66)  
  - **Aluminum**: 2 AWG (Table 250.66)  
- **Connection**: Bonds the grounding electrode system to the subpanel’s grounding bar.  

### 4. **Neutral and Ground Separation**
- **Critical Rule**: In the subpanel, **separate neutral and ground bars** (no bonding).  
  - Neutrals connect only to the **neutral bar**.  
  - Grounds connect only to the **grounding bar** (via EGC and GEC).  
  - **Bonding is only allowed at the main service panel** (per 250.24).  

### 5. **Key Exceptions and Notes**
- **Exception 250.32(B)(1)**: If the feeder uses a multiwire branch circuit, the grounded (neutral) conductor **must not be connected to the grounding system** in the garage subpanel.  
- **No Neutral-to-Ground Bond**: Per **250.32(B)(1) Exception**, the grounded conductor (neutral) in the garage subpanel **must not be connected to the grounding electrode system**.  

### 6. **Summary Diagram**
```
House Panel (Main Service)
   |
   |--- 4-Wire Feeder (2 hot, 1 neutral, 1 EGC)
   |
Garage Subpanel
   |
   |--- EGC (8 AWG Cu / 6 AWG Al) → Grounding Bar
   |--- GEC (4 AWG Cu / 2 AWG Al) → Ground Rod(s)
   |--- Neutral Bar (isolated from ground bar)
```

### 7. **Code Citations**
- Grounding electrode system: **CEC 250.50**  
- EGC sizing: **CEC 250.122**  
- GEC sizing: **CEC 250.66**  
- Neutral/ground separation: **CEC 250.24, 250.32(B)(1)**  

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 7.0s

**Tools Called:** cec_search, cec_search

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
1. **Main Bonding Jumper** (CEC 2022 Section 100):  
   - Connects the **grounded circuit conductor** (neutral) to the **equipment grounding conductor** at the **service**.  
   - Ensures the service is electrically bonded to equipment grounding.

2. **System Bonding Jumper** (CEC 2022 Section 100):  
   - Connects the **grounded conductor** to the **supply-side bonding jumper** or **equipment grounding conductor** at a **separately derived system** (e.g., transformers, generators).  
   - Ensures the derived system’s grounding is referenced to equipment grounding.

---

### **Key Differences**
| Feature                  | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|--------------------------|--------------------------------------------------|----------------------------------------------------|
| **Application**          | At the **service** (e.g., utility service entrance). | At **separately derived systems** (e.g., transformers, generators). |
| **Purpose**              | Bonds service neutral to equipment grounding.     | Bonds derived system neutral to equipment grounding. |
| **Required Location**    | Service equipment enclosure.                     | First disconnecting means of a separately derived system. |
| **Sizing**               | Per Table 250.102(C)(1), based on largest ungrounded service conductor. | Per Table 250.102(C)(1), based on largest ungrounded conductor of the derived system. |

---

### **When Each is Required**
1. **Main Bonding Jumper** (CEC 2022 250.28):  
   - **Required at every service** to connect the grounded (neutral) conductor to the equipment grounding conductor.  
   - Example: A residential service panel requires a main bonding jumper to tie the neutral bus to the equipment grounding bus.

2. **System Bonding Jumper** (CEC 2022 250.28):  
   - **Required at separately derived systems** (e.g., transformers, solar inverters, generators) to connect the system’s grounded conductor to the equipment grounding system.  
   - Example: A 480V to 208V transformer requires a system bonding jumper at its output to bond the secondary neutral to the equipment grounding conductor.

---

### **Sizing Requirements**
Both jumpers are sized per **Table 250.102(C)(1)** based on the largest ungrounded conductor:  
- For services: Largest service conductor.  
- For derived systems: Largest ungrounded conductor of the derived system.  

**Example**:  
- A service with 400 kcmil copper ungrounded conductors requires a **3/0 AWG copper** main bonding jumper (Table 250.102(C)(1)).  
- A transformer with 2/0 AWG secondary conductors requires a **1/0 AWG copper** system bonding jumper.

---

### **Material and Installation**
- Both must be **copper, aluminum, copper-clad aluminum, or corrosion-resistant material** (CEC 250.28(A)).  
- Must be connected per **250.8** (e.g., pressure connectors, exothermic welding).  
- Screws used as jumpers must have a **visible green finish** (250.28(B)).

---

### **Summary**
- **Main bonding jumper**: For services, bonds neutral to equipment ground.  
- **System bonding jumper**: For derived systems, bonds derived system neutral to equipment ground.  
- Both ensure safety by preventing dangerous voltage differences and completing the fault current path.

[OK] Source: CEC 2022

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 5.0s

**Tools Called:** nec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens (NEC 2023)

### Required Number of Circuits:
- **Minimum Requirement**: **Two 20-ampere small-appliance branch circuits** are required for all receptacles in the kitchen, pantry, breakfast room, and **dining room** (NEC 210.52(B)(1)).  
- **Additional Circuits**: More than two circuits are permitted but not required (NEC 210.52(B)(3)).

### Dining Room Receptacles:
- **Yes**, these circuits **can serve dining room receptacles**.  
  NEC 210.52(B)(1) explicitly includes dining rooms as part of the areas served by small-appliance branch circuits.

### Key Restrictions:
1. **No Other Outlets**: Small-appliance branch circuits **shall not serve any outlets outside the specified areas** (NEC 210.52(B)(2)).  
   - Exception: Receptacles for specific appliances (e.g., clocks, gas range accessories) are allowed.
2. **Single Kitchen Service**: No small-appliance branch circuit may serve more than **one kitchen** (NEC 210.52(B)(3)).

### Summary:
- **Kitchen**: 2+ 20A circuits required.  
- **Dining Room**: Permitted on these circuits.  
- **Other Areas**: Not allowed (e.g., living rooms, bedrooms).

[OK] Source: NEC 2023

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 12.2s

**Tools Called:** cec_ampacity_with_adjustments

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Conductor**: 12 AWG copper THHN  
**Ambient**: 50°C  
**Conductors**: 6 in raceway  

### 1. Base Ampacity (Table 310.16)  
- **THHN (90°C column)**: **30A**

### 2. Temperature Correction (Table 310.15(B)(1)(1))  
- **50°C ambient**: **×0.82**  
- **30A × 0.82 = 24.6A**

### 3. Bundling Adjustment (Table 310.15(C)(1))  
- **6 conductors**: **×0.8**  
- **24.6A × 0.8 = 19.68A**

### 4. Overcurrent Protection Limit (240.4(D))  
- **12 AWG copper**: **Maximum 20A OCPD**  
- **Final ampacity limited to 20A** (per 240.4(D))

---

**Final Answer**:  
**Adjusted ampacity = 19.68A**, but **must be protected at 20A maximum** per 240.4(D).

[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1), 240.4(D)

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 6.4s

**Tools Called:** nec_search

**Answer:**

## Why NEC Requires AFCI Protection in Bedrooms and Living Areas (NEC 2023)

### **Requirement**
Per **NEC 210.12(B)**, all 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets in **bedrooms, living rooms, and similar areas** in dwelling units must have **AFCI protection**. This includes:
- Bedrooms
- Living rooms
- Hallways
- Closets
- Similar locations

### **Purpose: Electrical Hazard Prevented**
AFCI (Arc-Fault Circuit Interrupter) protection is required to **prevent electrical fires caused by arc faults** in branch circuits. Arc faults occur when there is a broken circuit that allows high-energy arcs to form, often due to:
- Damaged or degraded wiring
- Loose connections
- Overloaded circuits
- Faulty appliances

These arcs can ignite surrounding materials (e.g., wood, insulation, fabric), leading to fires. AFCIs detect dangerous arcing conditions and de-energize the circuit before a fire can start.

### **Key Details from NEC**
- **Section 210.12(A)** outlines acceptable methods for AFCI protection (e.g., combination-type, branch/feeder-type, outlet branch-circuit-type).
- **Exceptions** apply for specific systems (e.g., fire alarm circuits, arc welding equipment until 2025).
- **Informational Notes** reference UL standards (e.g., UL 1699) and NFPA 72 for additional guidance on AFCI types and fire alarm systems.

### **Why Bedrooms and Living Areas?**
These areas are high-risk because:
1. **High electrical usage**: Multiple devices plugged in, increasing the chance of overloads or faults.
2. **Flexible wiring**: Frequent use of extension cords or portable heaters, which can stress wiring.
3. **Occupant safety**: Fires in these areas pose direct risk to occupants, especially during sleep or relaxation.

### **[OK] Source**: NEC 2023 Section 210.12

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 9.3s

**Tools Called:** cec_search

**Answer:**

## Importance of Torque Specifications in Conductor Termination (CEC 2022)

### Why Torque Specifications Matter:
1. **Ensures Proper Connection**: Correct torque prevents loose connections, reducing risk of arcing, overheating, and fire hazards.
2. **Prevents Damage**: Over-tightening can damage terminals or insulation; under-tightening creates poor conductivity.
3. **Compliance with Safety Standards**: Mandated by CEC to align with equipment manufacturer requirements and industry best practices (e.g., UL 486A-486B, NFPA 70B).

---

### Code Requirements:
#### **CEC 2022 Section 110.14(D)**  
- **Torque Values**: Tightening torque must match values indicated on equipment or in manufacturer instructions.  
- **Approved Methods**: Use torque tools, shear bolts, or breakaway devices with visual indicators to verify proper torque.  
- **Informational Notes**:  
  - Contact manufacturers if torque values are unspecified.  
  - Refer to Annex I of UL 486A-486B for default torque values.  
  - See NFPA 70B for maintenance guidance on threaded connections.  

#### **CEC 2022 Section 430.9(C)** (Example of Application-Specific Requirement)  
- Control circuit devices with screw-type terminals for 14 AWG or smaller copper conductors must be torqued to **0.8 N·m (7 lb-in.)** unless otherwise marked.  

---

### Key Takeaways:
- **Primary Reference**: CEC **110.14(D)** governs general torque requirements for all conductor terminations.  
- **Secondary References**: Sections like **430.9(C)** provide specific torque values for specialized equipment (e.g., motor control circuits).  
- **Compliance**: Always follow manufacturer torque specifications and use calibrated tools to achieve them.  

[OK] Source: CEC 2022

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 16.4s

**Tools Called:** cec_search

**Answer:**

## Residential Service Load Calculation (CEC 2022)

### **1. General Lighting Load** (CEC Table 220.12)  
- **3000 sq ft × 3 VA/sq ft = 9000 VA**  

### **2. Small Appliance & Laundry Circuits** (CEC 220.52)  
- **2 × 1500 VA (small appliances) + 1 × 1500 VA (laundry) = 4500 VA**  

### **3. Range Load** (CEC Table 220.55)  
- **12 kW range → 8000 VA (demand factor)**  

### **4. Dryer Load** (CEC Table 220.54)  
- **5.5 kW dryer → 5000 VA (minimum demand)**  

### **5. Air Conditioning Load**  
- **4600 VA (19.2A × 240V)**  

---

### **Demand Factors Applied**  
1. **General Lighting/Receptacle Load**:  
   - First 3000 VA @ 100% = **3000 VA**  
   - Remaining 10,500 VA @ 35% = **3675 VA**  
   - **Total: 3000 + 3675 = 6675 VA**  

2. **Range & Dryer**:  
   - **8000 VA (range) + 5000 VA (dryer) = 13,000 VA**  

3. **Air Conditioning**:  
   - **4600 VA**  

---

### **Total Calculated Load**  
```
6675 VA (adjusted lighting/receptacle)  
+ 13,000 VA (range + dryer)  
+ 4600 VA (AC)  
= **24,275 VA**
```

### **Convert to Amperes**  
```
24,275 VA ÷ 240V = **101.15 A**
```

---

### **Conclusion**  
- **200A panel is adequately sized** (101A < 200A).  
- **No overloading** of the main breaker.  
- **Complies with CEC 220.84** (standard method for dwelling units).  

[OK] Source: CEC 2022 (no California amendments to NEC Article 220 service load calculations identified).

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 7.4s

**Tools Called:** nec_lookup_working_space

**Answer:**

## Electrical Panel Inspection Violations (NEC 2023)

1. **Insufficient Depth Clearance**  
   - **Requirement**: Minimum 36 inches (3 ft) depth per NEC 110.26(A)(1) for 151–600V panels.  
   - **Violation**: Panel has only 28 inches depth.  

2. **Obstruction in Working Space**  
   - **Requirement**: Working space must be **clear of obstructions** (NEC 110.26(A)(2)).  
   - **Violation**: Water heater located 16 inches from panel within working space.  

3. **Inadequate Panel Height**  
   - **Requirement**: Live parts must be **at least 6.5 ft (78 in)** above floor (NEC 110.26(A)(2)).  
   - **Violation**: Panel mounted at 5 ft (60 in), placing live parts below required height.  

---

**Source**: NEC 2023 Sections 110.26(A)(1) and 110.26(A)(2).  
[OK] Source: NEC 2023

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 9.2s

**Tools Called:** nec_search

**Answer:**

## Circuit Protection Requirements (NEC 2023)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **Combination AFCI/GFCI Breaker**
- **References**:
  - **GFCI**: NEC 210.8(A)(5) (kitchen receptacles require GFCI protection).
  - **AFCI**: NEC 210.12 (all dwelling unit branch circuits require AFCI protection).

### 2. **Dishwasher (15A Dedicated Circuit)**
- **Protection Required**: **Combination AFCI/GFCI Breaker**
- **References**:
  - **GFCI**: NEC 210.8(A)(5) (appliances in kitchens require GFCI if connected via receptacle; even if hardwired, dedicated circuits in kitchens often require GFCI).
  - **AFCI**: NEC 210.12 (all dwelling unit circuits require AFCI).

### 3. **Garbage Disposal (15A Dedicated Circuit)**
- **Protection Required**: **Combination AFCI/GFCI Breaker**
- **References**:
  - **GFCI**: NEC 210.8(A)(5) (same as above).
  - **AFCI**: NEC 210.12.

### 4. **Refrigerator (20A Dedicated Circuit)**
- **Protection Required**: **Combination AFCI/GFCI Breaker**
- **References**:
  - **GFCI**: NEC 210.8(A)(5) (receptacles in kitchens require GFCI, even for dedicated appliances).
  - **AFCI**: NEC 210.12.

---

### Key Notes:
- **Combination AFCI/GFCI breakers** are required for all circuits where both protections apply.
- **Exceptions**: None apply here. All kitchen circuits (including dedicated appliance circuits) require both GFCI and AFCI under NEC 2023.

[OK] Source: NEC 2023

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 13.3s

**Tools Called:** cec_search, cec_search

**Answer:**

## Subpanel Inspection in Detached Garage (CEC 2022)

### **Identified Violations:**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation:** CEC 250.24(B) prohibits bonding the neutral and ground bars in subpanels. This creates a parallel path for current, risking equipment damage and shock hazards.  
   - **Correct Configuration:** Neutral and ground bars must be **electrically isolated** in subpanels (bonded only in the **main service panel** per CEC 250.24(B)).

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation:** CEC 250.142(A) requires the **neutral bar to be isolated** from the enclosure in subpanels. Bonding it to the enclosure creates a ground loop and unsafe fault current paths.  
   - **Correct Configuration:** Neutral bar must be **isolated** from the enclosure. Only the **ground bar** should be bonded to the enclosure (CEC 250.142(B)).

3. **Main Bonding Jumper Installed in Subpanel**  
   - **Violation:** CEC 250.24(B) restricts the main bonding jumper to the **main service panel only**. Its presence in a subpanel violates this rule.  
   - **Correct Configuration:** Remove the main bonding jumper. The **grounding electrode conductor** (GEC) connects only to the main panel.

---

### **Correct Subpanel Configuration:**
1. **Feeder Connections:**  
   - **Hot wires (#2 AWG aluminum):** Connected to the subpanel breaker.  
   - **Feeder neutral:** Connected to the **neutral bar** (isolated from ground bar).  
   - **Feeder ground:** Connected to the **ground bar** (bonded to the enclosure).  

2. **Ground Bar:**  
   - Bonded to the **metal enclosure** (CEC 250.142(B)).  
   - Connected to the **equipment grounding conductor** from the main panel.  

3. **Neutral Bar:**  
   - **Isolated** from the ground bar and enclosure.  
   - Connected only to the **feeder neutral conductor**.  

4. **Main Bonding Jumper:**  
   - **Removed** from the subpanel. Present only in the **main service panel** (CEC 250.24(B)).  

---

### **Summary of Fixes:**
- **Remove bonding between neutral and ground bars.**  
- **Remove bonding between neutral bar and enclosure.**  
- **Remove main bonding jumper.**  
- **Ensure ground bar is bonded to enclosure** and connected to the equipment grounding conductor.  

[OK] Source: CEC 2022 Sections 250.24(B), 250.142(A)(B)

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 4.6s

**Tools Called:** nec_conduit_fill_calculator

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (NEC 2023)

**Calculation:**
1. **Conduit Data (NEC Table 4):**  
   - 1¼" RMC total area = **1.526 sq in**  
   - 40% fill limit (for >2 conductors) = **0.61 sq in**  

2. **Conductor Data (NEC Table 5):**  
   - 10 AWG THHN area = **0.0211 sq in/conductor**  

3. **Maximum Conductors:**  
   $$
   \frac{0.61\ \text{sq in}}{0.0211\ \text{sq in/conductor}} = 28.91 \rightarrow \lfloor 28.91 \rfloor = \mathbf{28\ conductors}
   $$

**Verification:**  
- 28 conductors occupy:  
  $$
  28 \times 0.0211 = 0.5908\ \text{sq in} \ (\text{96.9% of 40% fill limit})
  $$  
- 29 conductors would exceed 40% fill:  
  $$
  29 \times 0.0211 = 0.6119\ \text{sq in} \ (\text{100.3% of 40% fill limit}) \rightarrow \text{Not allowed}
  $$

**Answer:**  
**28** is the maximum number of 10 AWG THHN conductors permitted in 1¼" RMC at 40% fill.  

[OK] Source: NEC 2023 Chapter 9 Tables 4 and 5

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 10.3s

**Tools Called:** cec_lookup_conductor_resistance, cec_search

**Answer:**

## Voltage Drop Calculation (CEC 2022)

**Given:**
- Voltage: 120V single-phase
- Load: 22A continuous
- Conductor: 12 AWG copper (stranded)
- One-way distance: 50 ft
- Resistance: 1.98 Ω/1000 ft (from CEC Table 8)

**1. Voltage Drop (VD):**
$$
VD = \frac{2 \times L \times R \times I}{1000} = \frac{2 \times 50 \times 1.98 \times 22}{1000} = 4.36 \, \text{volts}
$$

**2. Percentage Drop:**
$$
\%VD = \left( \frac{4.36}{120} \right) \times 100 = 3.63\%
$$

**3. NEC Compliance:**
- **3% maximum** for branch circuits (CEC 210.19(A) Informational Note No. 3)
- **3.63% > 3%** → **Does NOT meet** recommendation

**Code Reference:**  
CEC 210.19(A) Informational Note No. 3 explicitly states the 3% voltage drop recommendation for branch circuits. The calculation aligns with the resistance value from CEC Chapter 9 Table 8.

**Recommendation:** Use **10 AWG copper conductors** (resistance = 1.24 Ω/1000 ft) to reduce voltage drop to **2.73%**, which complies with the 3% limit.

[OK] Source: CEC 2022

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 16.4s

**Tools Called:** cec_base_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_ampacity_with_adjustments

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

### 1. **Base Ampacity**  
12 AWG copper (TW, 60°C rating) = **20A**  
(CEC Table 310.16)

### 2. **Temperature Correction Factor**  
Ambient = 43°C → **0.71**  
(CEC Table 310.15(B)(1)(1))

### 3. **Bundling Adjustment Factor**  
6 conductors → **0.80**  
(CEC Table 310.15(C)(1))

### 4. **Final Calculation**  
$$
20A \times 0.71 \times 0.80 = 11.36A
$$

### **Final Answer**  
**11.36 amperes** (rounded to **11A** for practical application)  

### ⚠️ Additional Notes  
- **Overcurrent Protection**: Per CEC 240.4(D), 12 AWG copper is limited to **20A** overcurrent protection. The adjusted ampacity (11.36A) is less restrictive than the OCP limit.  
- **Application**: The conductors must be protected at or below 11.36A, but the OCP device cannot exceed 20A (per 240.4(D)).  

[OK] Source: CEC 2022 with California amendments  
[OK] Applied temperature correction (0.71) and bundling adjustment (0.80)  
[OK] Verified via CEC Tables 310.16, 310.15(B)(1)(1), and 310.15(C)(1)

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 5.3s

**Tools Called:** nec_lookup_grounding_conductor

**Answer:**

## Minimum Size Copper Grounding Electrode Conductor (GEC) for 1000 kcmil Service Conductors

**Answer:**  
The minimum size copper grounding electrode conductor (GEC) required is **2/0 AWG**.

**Calculation Steps:**  
1. **Equivalent Service Conductor Size:**  
   Four parallel sets of 250 kcmil copper conductors per phase:  
   $ 4 \times 250 \, \text{kcmil} = 1000 \, \text{kcmil} $.

2. **NEC Table 250.66 Reference:**  
   For service conductors sized **Over 600 through 1100 kcmil**, the minimum copper GEC size is **2/0 AWG** (per NEC 2023 Table 250.66).

3. **Footnote Verification:**  
   - Footnote [1] confirms that parallel conductors are summed to determine equivalent size.  
   - Footnote [3] directs to installation restrictions in 250.64, but sizing is confirmed by Table 250.66.

**Citations:**  
- NEC 2023 Table 250.66  
- NEC 250.64 (installation restrictions)  

[OK] Source: NEC 2023

---

