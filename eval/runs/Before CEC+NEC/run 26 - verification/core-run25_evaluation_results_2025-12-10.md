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
| Total Duration | 204.4s |
| Avg Duration | 7.6s |
| Exception Search Used | 0/27 |
| NEC Comparison Used | 0/27 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 4.4s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum conductor size**: **6 AWG copper**  
- **Ampacity**: 65A (Table 310.16)  
- **Overcurrent protection**: 60A (per 240.4(D) limit of 65A for 6 AWG)  

**Key Code References**:  
1. **Ampacity**: CEC Table 310.16 (65A for 6 AWG at 75°C)  
2. **Overcurrent protection**: CEC 240.4(D) (65A maximum for 6 AWG copper)  

**Why not 8 AWG?**  
- 8 AWG has 50A ampacity (Table 310.16) – insufficient for 60A circuit  

**Final Check**:  
- 6 AWG meets both ampacity (65A ≥ 60A) and overcurrent protection requirements (60A ≤ 65A limit)  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 5.8s

**Tools Called:** nec_search

**Answer:**

## GFCI Protection in Residential Kitchens (NEC 2023)

**Requirement:**  
Ground-Fault Circuit-Interrupter (GFCI) protection is required for **all 125-volt through 250-volt receptacles in residential kitchens**, including those serving countertop surfaces, sinks, and food preparation areas.  

**Citation:**  
NEC 2023 **Section 210.8(A)(5)** explicitly mandates GFCI protection for kitchens in dwelling units.  

**Key Details:**  
- Applies to receptacles within **6 feet (1.8 meters)** of the top inside edge of kitchen sinks.  
- Covers receptacles on **small-appliance branch circuits** (per 210.52(B)(3)) and other kitchen outlets.  
- Exceptions do not typically apply in standard residential kitchens (e.g., exceptions for industrial or healthcare settings are irrelevant here).  

**[OK] Source: NEC 2023**

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 11.3s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction per **CEC 2022 Section 210.12(A)**.  

### Key Requirements:
- **Scope:** All 120V, single-phase, 15- and 20-ampere branch circuits supplying outlets in dwelling unit bedrooms must have AFCI protection.
- **Permitted Methods:** Protection can be provided via:
  1. **Combination-type AFCI** at the service panel.
  2. **Outlet branch-circuit-type AFCI** at the first outlet, combined with a branch-circuit overcurrent device.
  3. Other listed methods (e.g., supplemental protection combinations).
- **Exceptions:** None apply to standard bedroom circuits. The only exceptions relate to fire alarm systems or specific installation conditions not relevant here.

### Code Reference:
- **CEC 2022 Section 210.12(A):** Explicitly includes bedrooms in the list of required locations for AFCI protection.

[OK] Source: CEC 2022

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 4.8s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Yes**, aluminum conductors are permitted for a 200A service in California.  

### Required Size:
- **4/0 AWG aluminum** (per CEC Table 310.12(A))  
  - Ampacity: 200A @ 75°C  
  - Application: Single-phase dwelling services  

### Grounding Electrode Conductor (GEC):
- **4 AWG copper** or **2/0 AWG aluminum** (per CEC Table 250.66 for 4/0 AWG service conductors)  

### Notes:
1. **Termination Compliance**: Ensure equipment terminals are listed for aluminum conductors (CEC 110.14(D)).  
2. **Temperature Rating**: 75°C rating assumed; verify equipment compatibility.  
3. **No Derating**: This assumes standard conditions (≤3 current-carrying conductors, 30°C ambient).  

[OK] Source: CEC 2022 Tables 310.12(A) and 250.66

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 4.3s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Working Clearance Requirement (CEC 2022)

For a **120/240V residential electrical panel** with **Condition 2** (exposed live parts on one side and grounded parts on the other), the minimum working clearance depth required is:

**900 mm (3 feet)**  
Per CEC 2022 Table 110.26(A)(1), for systems up to 150V to ground.

### Key Details:
- **Voltage range**: 0–150V to ground (covers standard residential 120/240V systems)
- **Condition 2**: Applies when the panel is mounted against a grounded surface (e.g., concrete, brick, or tile wall)
- **Measurement**: From the front of the panel to the nearest obstruction

[OK] Source: CEC 2022 Table 110.26(A)(1)

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 4.4s

**Tools Called:** cec_search

**Answer:**

## Minimum Small Appliance Branch Circuits for Kitchen (CEC 2022)

**Answer:**  
A minimum of **2** 20-ampere small-appliance branch circuits are required for a kitchen per **CEC 2022 Section 210.52(B)(1)** and **210.11(C)(1)**.

### Key Requirements:
1. **Two or more circuits** must supply all kitchen receptacles (wall, countertop, and floor outlets).
2. **No other outlets** are permitted on these circuits except those specified in exceptions.
3. **Each circuit** must serve only one kitchen (no shared circuits between kitchens).

### Code Citations:
- **CEC 2022 210.52(B)(1)**: Requires not fewer than two small-appliance branch circuits for kitchen receptacles.
- **CEC 2022 210.11(C)(1)**: Mandates two or more 20A small-appliance branch circuits for dwelling units.

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 7.4s

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for 200A Residential Service (NEC 2023)

**Answer:**  
Surge protection is **not universally required** for a new 200A residential service per NEC 2023 **at the service entrance**. However, **surge-protective devices (SPDs)** are **required for feeders** supplying dwelling units under **NEC 215.18(A)(1)**.  

### Key Details:
1. **Service Entrance (200A Service):**  
   - NEC 2023 does **not explicitly mandate** surge protection at the service level for residential services.  
   - **Exception:** Surge arresters/SPDs are permitted on the supply side of the service disconnect (230.94, Exception No. 2) but are not required unless specified by the AHJ or for sensitive equipment.

2. **Feeders to Dwelling Units:**  
   - **NEC 215.18(A)(1):** Requires SPDs on feeders supplying dwelling units (e.g., multi-family buildings). This applies to **feeders**, not the main service entrance itself.

3. **Scope of SPD Requirements:**  
   - **Article 242** governs overvoltage protection, including SPDs for systems ≤1000V. It outlines installation and rating requirements but does not universally mandate SPDs for all services.  
   - **Informational Note (215.18):** Recommends SPDs be installed as close to the load as practical for optimal protection.

### Conclusion:  
For a **residential service entrance**, surge protection is **not required by NEC 2023** unless:  
- The service includes **feeders** to dwelling units (triggering 215.18), or  
- The **AHJ** mandates it, or  
- The installation includes **sensitive equipment** requiring additional protection.  

[OK] Source: NEC 2023 Sections 215.18, 230.94, 242.1

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 5.1s

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size

**Answer:**

## Service Conductor Sizing for 200A Dwelling Upgrade (CEC 2022)

**Required Service Conductor Sizes:**
- **Copper:** 2/0 AWG (per CEC Table 310.12(A))
- **Aluminum:** 4/0 AWG (per CEC Table 310.12(A))

**Key Requirements:**
1. **Table 310.12(A)** applies to single-phase dwelling services/feeders
2. **Aluminum is permitted** for service conductors in California
3. **No temperature correction or bundling adjustments** needed in this scenario
4. **Minimum conductor sizes** based on 75°C terminals (standard for service equipment)

**[OK] Source:** CEC 2022 Table 310.12(A) for dwelling services

**Note:** For California-specific requirements, also check:
- **CEC 408.2** for panelboard space requirements
- **CALGreen** provisions for electrification-ready infrastructure

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 8.9s

**Tools Called:** nec_search

**Answer:**

## NEC Requirements for Multiwire Branch Circuit in Kitchen

### Circuit Breaker Requirements (NEC 210.4)
1. **Simultaneous Disconnection** [210.4(B)]:  
   - All ungrounded (hot) conductors must be disconnected simultaneously at the panel.  
   - **Implementation**: Use a **2-pole circuit breaker** or **handle-tied single-pole breakers** (per 240.15(B)).  
   - *Failure to comply creates shock hazard if only one hot is turned off.*

2. **Phase Configuration**:  
   - Hots must be on **opposite phases** (120/240V system) to balance the neutral current.  
   - Neutral carries **only the unbalanced load** (per 210.4(C)).

### Neutral Termination Requirements
1. **Neutral Must Not Be Switched** [210.4(D)]:  
   - Neutral conductor must connect directly to the **neutral bus** in the panel.  
   - **No switches or circuit breakers** are permitted on the neutral conductor.

2. **Conductor Sizing**:  
   - 12/3 cable (12 AWG conductors) is appropriate for kitchen circuits (typically 20A circuits).  
   - Neutral must be sized to handle potential unbalanced harmonic currents (per Info Note 1 in 210.4).

### Additional Considerations
- **GFCI Protection Required** [210.8(A)(6)]:  
  - All kitchen receptacles must have **ground-fault circuit interrupter (GFCI)** protection.  
  - GFCI can be at the outlet, circuit breaker, or upstream device.

- **AFCI Protection Not Required for Kitchens**:  
  - AFCI protection is not mandated for kitchen circuits (unlike bedrooms, see 210.12).  

---

**Summary of Compliance**:  
- Use a **2-pole breaker** or **handle-tied single-pole breakers** for simultaneous disconnection.  
- Connect the neutral directly to the **neutral bus** (no switching).  
- Ensure **GFCI protection** is installed for all kitchen receptacles.  

[OK] Source: NEC 2023

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 8.7s

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

According to **NEC 2023 Section 210.8(A)**, GFCI protection is required for **all 120–250V receptacles** in the following locations within dwelling units:

1. **Bathrooms**  
2. **Garages** and **accessory buildings** with floors at or below grade level (storage/work areas).  
3. **Outdoors** (all exterior receptacles).  
4. **Crawl spaces** at or below grade level.  
5. **Kitchens** (including areas with sinks and food preparation).  
6. **Areas with sinks** for food/preparation within **6 feet** of the sink’s top inside edge.  
7. **Bathtubs or shower stalls** within **6 feet** of the outside edge.  
8. **Laundry areas**.  
9. **Indoor damp or wet locations** (e.g., utility sinks, wet bars).  

**Additional Context**:  
- **Exceptions** apply for specific equipment (e.g., HVAC, snow-melting systems) but do not negate the general requirements above.  
- **Section 210.8(A)(10)** explicitly includes **boathouses** and **unfinished basement areas**.  
- **Section 210.8(A)(11)** expands coverage to **aquariums/bait wells** with receptacles within 6 feet.  

**Source**: NEC 2023 Section 210.8(A) and related amendments.  

[OK] Source: NEC 2023

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 4.9s

**Tools Called:** cec_search

**Answer:**

## Surge Protection for Residential Service (CEC 2022)

**Requirement:**  
Surge protection **is required** for all new residential services per **CEC 2022 Section 230.67**.  

**Installation Locations:**  
1. **Integral to service equipment** (e.g., main panel)  
2. **Immediately adjacent to service equipment**  
3. **Exception**: May be installed at the next level of distribution downstream (e.g., subpanel) if specified  

**SPD Type:**  
Must be **Type 1 or Type 2** surge-protective device (SPD) (CEC 230.67(C)).  

**Additional Note:**  
Type 1 SPDs may be installed on the **supply side of the service disconnect** per **CEC 230.94 Exception No. 2** if coordinated with overcurrent protection.  

[OK] Source: CEC 2022 Sections 230.67, 230.94

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 6.0s

**Tools Called:** nec_lookup_working_space

**Answer:**

## Working Space Requirements (NEC 2023)

The installation **does not meet NEC requirements** for working space clearance:

1. **Front clearance requirement**:  
   For 240V equipment (condition 2 - exposed live parts on one side and grounded parts on the other), NEC Table 110.26(A)(1) mandates **3 feet 6 inches (3.5 ft / 42 in)** of working space.  
   → **24 inches provided is insufficient**.

2. **Side clearance note**:  
   While NEC doesn't specify minimum side clearance for adjacent equipment like water heaters, the 24-inch front clearance violation alone makes the installation non-compliant regardless of side spacing.

**Corrective action**: Increase front clearance to at least 3 feet 6 inches (42 inches) in front of the panel.

[OK] Source: NEC 2023 Table 110.26(A)(1)

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 7.3s

**Tools Called:** cec_search

**Answer:**

## Code Violation for Multiple Conductors on a Single Breaker Terminal (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under **CEC 408.41** and general terminal requirements. Here's the breakdown:

1. **CEC 408.41** explicitly requires:  
   > *"Each grounded conductor shall terminate within the panelboard in an individual terminal that is not also used for another conductor."*  
   The exception only applies to **parallel conductors** with terminals marked for multiple conductors.

2. **Terminal Markings:**  
   Breaker terminals **must be listed/identified** for multiple conductor connections (e.g., "2-wire" marking). Since this terminal is **not marked**, connecting two 12 AWG conductors violates the manufacturer's listing and **110.14(A)** (terminals used in accordance with instructions).

3. **NEC/CEC Consistency:**  
   NEC 110.14(A) and CEC 408.41 both prohibit using terminals for more conductors than they are rated for. This applies to **all circuit breakers**, not just panelboard terminals.

**Corrective Action:**  
- Use a **single conductor per terminal**  
- Or install a breaker with a terminal marked for two conductors (e.g., "2-wire" rated)  

[OK] Source: CEC 2022

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 8.1s

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

For a detached garage subpanel fed by a 4-wire feeder from the house panel, the grounding and bonding configuration must comply with the following CEC requirements:

1. **Neutral and Ground Separation**  
   - The **neutral bus** and **grounding bus** in the subpanel **must be isolated** (not bonded). This prevents ground loops and ensures proper fault current paths.  
   - **Citation**: CEC 250.142(B) (Separate Systems Grounding and Bonding).

2. **Grounding Electrode Connection**  
   - A **separate grounding electrode** (e.g., ground rod) must be installed at the detached garage.  
   - The **grounding electrode conductor** connects the subpanel’s **grounding bus** to this local electrode.  
   - **Citation**: CEC 250.32(B)(2) (Grounding Electrode Conductor for Separate Buildings).

3. **Feeder Equipment Grounding Conductor (EGC)**  
   - The **EGC** from the house panel (4th wire in the feeder) connects to the subpanel’s **grounding bus**. This provides a low-impedance path for fault currents back to the main panel.  
   - **Citation**: CEC 215.6 (Feeder Equipment Grounding Conductor).

4. **Neutral Conductor**  
   - The **neutral conductor** from the house panel connects to the subpanel’s **neutral bus**. It must **not** be bonded to the grounding bus.  
   - **Citation**: CEC 250.142(A) (Grounding of Separately Derived Systems).

5. **Bonding at Main Panel Only**  
   - The **main panel** is the **only location** where the neutral and grounding systems are bonded. The subpanel must maintain separation.  
   - **Citation**: CEC 250.24(A) (Grounding and Bonding of Services).

---

### Summary Configuration
- **Subpanel Neutral Bus**: Connected to feeder neutral (no bonding to ground).  
- **Subpanel Grounding Bus**: Connected to:  
  - Feeder equipment grounding conductor (EGC).  
  - Local grounding electrode conductor (ground rod).  
- **Ground Rod**: Installed at the detached garage per CEC 250.54.  

This setup ensures compliance with CEC requirements for detached structures and maintains electrical safety.  

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 6.1s

**Tools Called:** cec_search

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
1. **Main Bonding Jumper**  
   - Connects the **grounded circuit conductor** (neutral) to the **equipment grounding conductor** at the **service**.  
   - **Required by**: CEC 250.28 for grounded systems.  
   - **Application**: Used at the **service disconnecting means** to ensure the equipment grounding system is bonded to the grounded conductor.  

2. **System Bonding Jumper**  
   - Connects the **grounded circuit conductor** to the **equipment grounding conductor** at a **separately derived system** (e.g., transformers, generators, or photovoltaic systems).  
   - **Required by**: CEC 250.28 for separately derived systems.  
   - **Application**: Used at the **source of a separately derived system** to bond the system to the equipment grounding conductor.  

---

### **Key Differences**
| Feature                  | Main Bonding Jumper                     | System Bonding Jumper                     |
|--------------------------|------------------------------------------|-------------------------------------------|
| **Location**             | At the **service** (main electrical panel) | At the **source of a separately derived system** (e.g., transformer, generator) |
| **Purpose**              | Bonds grounded conductor to equipment grounding conductor at the service | Bonds grounded conductor to equipment grounding conductor at a separately derived system |
| **Required By**          | CEC 250.28(D)                              | CEC 250.28(D) and 250.102(C)                |

---

### **Sizing Requirements**
Both jumpers are sized per **Table 250.102(C)(1)** based on the largest ungrounded conductor in the system:  
- **Main Bonding Jumper**: Sized for the **service entrance conductors**.  
- **System Bonding Jumper**: Sized for the **largest ungrounded conductor of the separately derived system**.  

**Exceptions/Notes**:  
- If supply conductors exceed 1100 kcmil copper or 1750 kcmil aluminum, the bonding jumper must be at least **12.5% of the largest ungrounded conductor** (CEC 250.102 Note 1).  
- For parallel conductors, the bonding jumper size is based on the **equivalent area** of all parallel sets (CEC 250.102 Note 3).  

---

### **When Each Is Required**
1. **Main Bonding Jumper**  
   - **Required at every service** (CEC 250.28).  
   - Ensures the equipment grounding system is tied to the grounded (neutral) conductor at the service.  

2. **System Bonding Jumper**  
   - **Required at every separately derived system** (CEC 250.28).  
   - Ensures the derived system’s grounded conductor is bonded to its equipment grounding conductor.  

---

### **Installation Requirements**
- Both must be made of **copper, aluminum, copper-clad aluminum, or corrosion-resistant material** (CEC 250.28(A)).  
- Must be connected using methods specified in **CEC 250.8** (e.g., pressure connectors, exothermic welding).  
- **Screw-only jumpers** must have a visible green finish (CEC 250.28(B)).  

---

### **Example Applications**
- **Main Bonding Jumper**: A residential service with 200A service entrance conductors requires a main bonding jumper sized per Table 250.102(C)(1) for 200A.  
- **System Bonding Jumper**: A 480V transformer-derived system with 4/0 AWG secondary conductors requires a system bonding jumper sized per Table 250.102(C)(1) for 4/0 AWG.  

[OK] Source: CEC 2022 Sections 100, 250.28, 250.102

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 5.6s

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

### **1. Required Number of Circuits**
- **Minimum Requirement**: **2 or more 20-ampere small-appliance branch circuits** are required for **kitchens**, **pantries**, **breakfast rooms**, **dining rooms**, or similar areas in dwelling units (CEC 210.52(B)(1)).  
- **Purpose**: These circuits serve all wall, countertop, and floor receptacles in these spaces, as well as refrigeration equipment.

---

### **2. Can These Circuits Serve Dining Room Receptacles?**
- **Yes**, per **CEC 210.52(B)(1)**:  
  - The small-appliance branch circuits **can supply receptacles in the dining room** if it is classified as a "similar area" (e.g., part of the same dwelling unit).  
  - **Exception**: No small-appliance branch circuit shall serve more than **one kitchen**, but dining rooms are permitted as part of the same dwelling unit.

---

### **Key Code References**
- **CEC 210.52(B)(1)**: Requires 2+ 20A circuits for small appliances in kitchens/dining areas.  
- **CEC 210.52(B)(3)**: Allows these circuits to supply receptacles in the same kitchen and other rooms (e.g., dining room) specified in 210.52(B)(1).  

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 6.7s

**Tools Called:** cec_ampacity_with_adjustments

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Conductor**: 12 AWG THHN copper  
**Ambient**: 50°C  
**Conductors**: 6 in raceway  

---

### 1. **Base Ampacity**  
From **Table 310.16** (90°C column for THHN):  
**30A** (12 AWG copper at 30°C)

---

### 2. **Temperature Correction**  
Ambient = 50°C → **0.82** correction factor  
(From **Table 310.15(B)(1)(1)** for 90°C insulation)  

---

### 3. **Bundling Adjustment**  
6 conductors → **0.8** adjustment factor  
(From **Table 310.15(C)(1)** for >3 conductors)  

---

### 4. **Final Derated Ampacity**  
$$
30A \times 0.82 \times 0.8 = 19.68A
$$

---

### 5. **Overcurrent Protection Limit**  
**Section 240.4(D)** limits 12 AWG copper to **20A** OCPD.  
Even though derated ampacity is 19.68A, OCPD must not exceed 20A.

---

**Final Answer**:  
- **Adjusted Ampacity**: **19.68A**  
- **Maximum OCPD**: **20A**  

**Citations**:  
- Table 310.16 (base ampacity)  
- Table 310.15(B)(1)(1) (temperature correction)  
- Table 310.15(C)(1) (bundling adjustment)  
- Section 240.4(D) (overcurrent protection limit)  

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 9.3s

**Tools Called:** nec_search

**Answer:**

## Why NEC Requires AFCI Protection in Bedrooms and Living Areas (NEC 2023)

### **Requirement**
The NEC mandates **Arc-Fault Circuit Interrupter (AFCI) protection** for 120-volt, single-phase, 15- and 20-ampere branch circuits in specific locations, including:
- **Bedrooms** (210.12(C)(1))
- **Living rooms** (210.12(C)(2))
- Similar areas like hallways, closets, and bathrooms in dwellings (210.12(C))

This applies to **new installations, modifications, and extensions** of branch circuits in these spaces (210.12(E)).

---

### **Electrical Hazard Prevented**
AFCIs are required to **prevent fires caused by arc faults**. Arc faults occur when damaged or deteriorated wiring creates high-temperature electrical arcs (e.g., from nail punctures, loose connections, or frayed insulation). Standard circuit breakers do not detect arcs but AFCIs do, interrupting the circuit to mitigate fire risks.

---

### **Key NEC References**
- **NEC 210.12(A)**: Outlines approved methods for AFCI protection (e.g., combination-type, branch/feeder-type devices).
- **NEC 210.12(C)**: Explicitly requires AFCI protection in **bedrooms, living rooms, and similar dwelling unit areas**.
- **NEC 210.12(E)**: Ensures AFCI protection remains required during wiring modifications or extensions.

---

### **Rationale**
Bedrooms and living areas are high-traffic zones where wiring is susceptible to damage (e.g., from furniture movement, DIY projects). Arc faults in these areas pose significant fire risks, especially in older wiring systems. AFCIs address this by detecting dangerous arcs while allowing normal operational arcs (e.g., from switches).

[OK] Source: NEC 2023

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 5.2s

**Tools Called:** cec_search

**Answer:**

## Importance of Torque Specifications for Conductor Termination (CEC 2022)

### Why Torque Specifications Matter:
1. **Reliable Electrical Connection**: Proper torque ensures conductors are securely fastened to terminals, minimizing resistance and preventing overheating.
2. **Prevents Damage**: Over-tightening can damage terminals or insulation, while under-tightening creates loose connections that arc and degrade.
3. **Compliance with Safety Standards**: Adhering to manufacturer torque values ensures compliance with code requirements and manufacturer warranties.

### Code Requirements:
- **CEC 2022 Section 110.14(D)**:  
  - Requires torque values to be as indicated on equipment or in manufacturer instructions.  
  - Mandates use of approved tools (e.g., torque screwdrivers, breakaway devices) to achieve specified torque.  
  - *Informational Note*: Contact manufacturers for torque values if not provided.  

- **CEC 2022 Section 430.9(C)** (Specific Application):  
  - For control circuit devices with screw-type terminals using 14 AWG or smaller copper conductors:  
    - Minimum torque of **0.8 N·m (7 lb-in.)** unless otherwise identified.  

### Key Takeaways:
- Always follow **manufacturer-specified torque values**.  
- Use **torque tools** to ensure proper tightening.  
- Refer to **110.14(D)** for general requirements and **430.9(C)** for control circuit applications.  

[OK] Source: CEC 2022

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 18.6s

**Tools Called:** nec_search

**Answer:**

## Service Load Calculation (NEC 2023)

### 1. **General Lighting Load**  
Per NEC Table 220.12 (dwelling units):  
3 VA/sq ft × 3000 sq ft = **9000 VA**

### 2. **Small Appliance Circuits**  
2 circuits × 1500 VA (NEC 220.52(B)) = **3000 VA**  
1 laundry circuit × 1500 VA = **1500 VA**  
**Total:** 3000 + 1500 = **4500 VA**

### 3. **Demand Factors (NEC Table 220.45)**  
Total general lighting + small appliance load:  
9000 + 4500 = **13,500 VA**  
Apply demand factors:  
- First 3000 VA @ 100% = **3000 VA**  
- Remaining 10,500 VA @ 35% = **3675 VA**  
**Adjusted total:** 3000 + 3675 = **6675 VA**

### 4. **Electric Range**  
12 kW × 83% demand factor (NEC 220.55) = **9960 VA**

### 5. **Electric Dryer**  
5.5 kW × 100% demand factor (NEC 220.54) = **5500 VA**

### 6. **Central AC**  
4600 W × 125% (continuous load) = **5750 VA**

### 7. **Total Load Calculation**  
**Total VA:**  
6675 (adjusted lighting/appliances) + 9960 (range) + 5500 (dryer) + 5750 (AC) = **27,885 VA**  

**Convert to Amperes:**  
27,885 VA ÷ 240 V = **116.2 A**

### 8. **Service Size Verification**  
- **Calculated Load:** 116.2 A  
- **Available Service:** 200 A  

**Conclusion:** The 200A panel is **adequately sized** as the calculated load (116.2A) is less than the 200A service capacity.  

[OK] Source: NEC 2023

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 5.9s

**Tools Called:** nec_lookup_working_space

**Answer:**

## Electrical Panel Working Space Violations (NEC 2023)

**Identified Violations:**

1. **Insufficient Depth Clearance**  
   - **Measured:** 28 inches  
   - **Required:** Minimum 36 inches (3 ft) per NEC 110.26(A)(1) for panels rated ≤ 120V  
   - **Citation:** NEC 110.26(A)(1), Table 110.26(A)(1)

2. **Obstruction in Working Space**  
   - Water heater located 16 inches from panel (within required 36-inch depth clearance zone)  
   - **Citation:** NEC 110.26(B) requires working space to be "clear of all obstructions"

3. **Height Compliance**  
   - Panel mounted at 5 ft (center of working space)  
   - **Compliant:** Within required 4.5 ft to 5.5 ft range (NEC 110.26(A)(2))

---

**Key Requirements from NEC 110.26:**
- **Depth:** 36 inches minimum for panels rated ≤ 150V  
- **Width:** Minimum 30 inches or width of equipment, whichever is greater  
- **Height:** 6.5 ft minimum headroom (not specified in question, assume compliant)  
- **Clearance:** No obstructions in working space (water heater violates this)

[OK] Source: NEC 2023

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 10.7s

**Tools Called:** nec_search

**Answer:**

## Circuit Protection Requirements (NEC 2023)

### 1. **Countertop Receptacles (20A Circuits)**
- **Protection Required**: **GFCI + AFCI** (combination breaker)
- **NEC References**:
  - **210.8(A)(1)**: GFCI protection required for all countertop receptacles.
  - **210.12(A)**: AFCI protection required for all branch circuits in dwelling units (no exception for countertop circuits).

### 2. **Dishwasher (15A Dedicated Circuit)**
- **Protection Required**: **GFCI**
- **NEC References**:
  - **210.8(A)(1)**: GFCI protection required for receptacles in kitchens (appliances included).
  - **210.52(B)(1) Exception No. 2**: Permits dedicated circuits for specific appliances, but GFCI still applies if in a kitchen.

### 3. **Garbage Disposal (15A Dedicated Circuit)**
- **Protection Required**: **GFCI**
- **NEC References**:
  - **210.8(A)(1)**: GFCI protection required for all kitchen receptacles, including dedicated circuits for appliances.

### 4. **Refrigerator (20A Dedicated Circuit)**
- **Protection Required**: **Standard Breaker (No AFCI/GFCI)**
- **NEC References**:
  - **210.12(A) Exception No. 2**: Exempts fixed appliances (like refrigerators) from AFCI requirements.
  - **210.8(A)(6)**: No GFCI requirement for refrigerators (listed appliances in non-damp locations).

---

### Summary Table

| Circuit Type               | Protection Required       | NEC References                                  |
|----------------------------|---------------------------|-------------------------------------------------|
| Countertop Receptacles     | GFCI + AFCI               | 210.8(A)(1), 210.12(A)                          |
| Dishwasher                 | GFCI                      | 210.8(A)(1), 210.52(B)(1) Exception No. 2       |
| Garbage Disposal           | GFCI                      | 210.8(A)(1), 210.52(B)(1) Exception No. 2       |
| Refrigerator               | Standard Breaker          | 210.12(A) Exception No. 2, 210.8(A)(6)          |

[OK] Source: NEC 2023

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 6.3s

**Tools Called:** cec_search

**Answer:**

## Subpanel Grounding Violations and Correct Configuration (CEC 2022)

### **Identified Violations**
1. **Neutral and ground bars bonded together**  
   - **Violation**: CEC 250.146(D) and 250.24(D) require **separate neutrals and grounds** in subpanels (unlike main panels). Bonding creates a parallel neutral path, risking shock and equipment damage.  
   - **Correct**: Neutral and ground bars must be **electrically isolated** in subpanels.

2. **Neutral bar bonded to metal enclosure**  
   - **Violation**: CEC 408.40 prohibits connecting **neutral bars** to the enclosure. Neutrals must remain isolated from equipment grounding paths.  
   - **Correct**: Neutral bar must be **insulated** from the enclosure.

3. **Ground bar bonded to metal enclosure**  
   - **Violation**: While CEC 250.104(A) requires equipment grounding, the **ground bar itself** should not be bonded to the enclosure. Grounding conductors must terminate at the ground bar, which connects to the grounding electrode via the feeder's equipment grounding conductor (EGC).  
   - **Correct**: Ground bar must be **isolated** from the enclosure. The EGC connects to the ground bar, and the ground bar connects to the grounding electrode (e.g., rod, water pipe).

---

### **Correct Subpanel Configuration**
1. **Feeder Conductors**  
   - **Hot wires**: #2 AWG aluminum (2 conductors)  
   - **Neutral**: #2 AWG aluminum (connected to **neutral bar**)  
   - **Ground**: #2 AWG aluminum (connected to **ground bar**)  

2. **Internal Connections**  
   - **Neutral bar**:  
     - Connected **only** to the feeder neutral.  
     - **Isolated** from the enclosure and ground bar.  
   - **Ground bar**:  
     - Connected to the feeder ground.  
     - Connected to the grounding electrode via a **separate grounding conductor** (per CEC 250.53).  
     - **Isolated** from the enclosure and neutral bar.  

3. **Enclosure Bonding**  
   - The metal enclosure is bonded to the **ground bar** via a **separate bonding jumper** (CEC 250.104(A)).  
   - **No direct bonds** between enclosure and neutral bar.  

---

### **Key Code References**
- **CEC 250.146(D)**: Requires isolated equipment grounding conductors for feeders to subpanels.  
- **CEC 250.24(D)**: Prohibits bonding neutrals and grounds in subpanels.  
- **CEC 408.40**: Equipment grounding conductors must terminate at a dedicated ground bar, not neutral bars.  
- **CEC 250.53**: Grounding electrode conductor must connect to the ground bar, not the neutral bar.  

[OK] Source: CEC 2022

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 5.7s

**Tools Called:** nec_conduit_fill_calculator

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (NEC 2023)

**Calculation:**
1. **Conduit Area:**  
   RMC 1¼" = **1.526 sq in** (NEC Table 4)  
   40% fill limit = 1.526 × 0.40 = **0.6104 sq in**

2. **Conductor Area:**  
   10 AWG THHN = **0.0211 sq in** (NEC Table 5)

3. **Maximum Conductors:**  
   0.6104 ÷ 0.0211 ≈ **28.91** → **28 conductors** (round down)

**Verification:**  
28 conductors × 0.0211 sq in = **0.5908 sq in** (40% fill = 0.6104 sq in)  
Fill percentage = (0.5908 ÷ 1.526) × 100 ≈ **38.7%** (within 40% limit)

[OK] Source: NEC 2023 Chapter 9 Tables 4 and 5

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 15.3s

**Tools Called:** python_calculator, python_calculator, cec_lookup_conductor_resistance, cec_search

**Answer:**

## Voltage Drop Calculation (CEC 2022)

**Given:**  
- **Current (I):** 22A  
- **Conductor Resistance (R):** 1.29 Ω/1000ft (user-provided) vs. **1.98 Ω/1000ft** (CEC Table 8 for 12 AWG copper at 75°C)  
- **Distance (L):** 50ft one-way  

---

### **1. Voltage Drop Calculation**  
**Using User-Provided Resistance (1.29 Ω/1000ft):**  
$$
VD = \frac{2 \times I \times R \times L}{1000} = \frac{2 \times 22 \times 1.29 \times 50}{1000} = 2.84 \, \text{V}
$$  
$$
\%VD = \left( \frac{2.84}{120} \right) \times 100 = 2.36\%
$$  
**Result:**  
- **Voltage Drop:** 2.84V  
- **Percentage Drop:** 2.36%  
- **Compliance:** ✅ Meets **3% max** (CEC 210.19(A)(1) Note 4).  

---

### **2. Using CEC-Standard Resistance (1.98 Ω/1000ft):**  
$$
VD = \frac{2 \times 22 \times 1.98 \times 50}{1000} = 4.36 \, \text{V}
$$  
$$
\%VD = \left( \frac{4.36}{120} \right) \times 100 = 3.63\%
$$  
**Result:**  
- **Voltage Drop:** 4.36V  
- **Percentage Drop:** 3.63%  
- **Compliance:** ❌ **Exceeds 3% max** (CEC 210.19(A)(1) Note 4).  

---

### **Key Findings**  
1. **Discrepancy in Resistance:**  
   - User-provided resistance (1.29 Ω/1000ft) is **lower** than CEC Table 8 value (1.98 Ω/1000ft for 12 AWG copper at 75°C).  
   - This likely reflects a different temperature rating (e.g., 60°C vs. 75°C).  

2. **Code Compliance:**  
   - If using **CEC-standard resistance**, the voltage drop (3.63%) **exceeds** the 3% recommendation.  
   - If using **user-provided resistance**, the voltage drop (2.36%) is **within limits**.  

3. **Recommendation:**  
   - Verify conductor temperature rating and use the correct resistance value from **CEC Chapter 9 Table 8**.  
   - For 12 AWG copper at 75°C, **1.98 Ω/1000ft** is the correct value.  

---

**[OK] Source:** CEC 2022 Chapter 9 Table 8, 210.19(A)(1) Note 4

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 12.3s

**Tools Called:** cec_base_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_ampacity_with_adjustments

**Answer:**

## Final Adjusted Ampacity Calculation (CEC 2022)

**Given**:  
- 6 current-carrying 12 AWG TW (60°C) copper conductors  
- Ambient temperature: 43°C (110°F)  

---

### 1. **Base Ampacity**  
From **CEC Table 310.16**:  
- 12 AWG copper at 60°C → **20A**  

---

### 2. **Temperature Correction Factor**  
From **CEC Table 310.15(B)(1)(1)**:  
- 60°C conductors at 43°C ambient → **0.71**  

---

### 3. **Bundling Adjustment Factor**  
From **CEC Table 310.15(C)(1)**:  
- 6 conductors in raceway → **0.80**  

---

### 4. **Final Calculation**  
$$
\text{Adjusted Ampacity} = 20A \times 0.71 \times 0.80 = 11.36A
$$

---

### 5. **Overcurrent Protection Check**  
From **CEC 240.4(D)**:  
- 12 AWG copper is permitted for **up to 20A** overcurrent protection.  
- Final adjusted ampacity (11.36A) ≤ 20A → **Compliant**  

---

**Final Answer**:  
**11.36 amperes** after applying temperature and bundling adjustments.  

[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1), and 240.4(D)

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 5.4s

**Tools Called:** nec_lookup_grounding_conductor

**Answer:**

## Minimum Size Copper GEC for 1000 kcmil Service Conductors (NEC 2023)

**Answer:**  
The minimum size **copper** grounding electrode conductor (GEC) required is **2/0 AWG**.

**Calculation Steps:**  
1. **Equivalent Service Conductor Size**:  
   Four parallel 250 kcmil conductors per phase = 4 × 250 kcmil = **1000 kcmil** (per NEC 250.66 footnote 1).

2. **NEC Table 250.66 Reference**:  
   For service conductors **over 600 kcmil through 1100 kcmil**, the minimum copper GEC size is **2/0 AWG** (per Table 250.66).

**Citations:**  
- NEC 2023 Table 250.66  
- NEC 250.66 (footnote 1): Equivalent size calculation for parallel conductors  

[OK] Source: NEC 2023

---

