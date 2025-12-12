# Core (NEC) Evaluation Results - Run 27 (Robustness Fixes)

**Date:** 2025-12-10
**Changes:** Expanded keyword detection + similarity fallback + multi-answer guidance

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 196.5s |
| Avg Duration | 7.3s |
| Exception Search Used | 0/27 |
| NEC Comparison Used | 0/27 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled (expanded) |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 5.2s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size**: **6 AWG copper**  
- **Ampacity**: 65A (75°C column, Table 310.16)  
- **Overcurrent protection**: 60A or 65A breaker (per 240.4(D))  

**Why not 8 AWG?**  
- 8 AWG copper has 50A ampacity at 75°C (Table 310.16)  
- **Fails to meet 60A requirement**  

**Key Code References**:  
- **Table 310.16**: Base ampacity values  
- **240.4(D)**: Overcurrent protection limits (6 AWG max 65A)  

**Inspector Note**:  
- If ambient temperature >30°C or >3 current-carrying conductors in raceway, apply correction factors from **310.15(B)** or **310.15(C)(1)**  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 7.7s

**Tools Called:** cec_search

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**GFCI protection is required for all 125–250V receptacles installed to serve countertop surfaces in residential kitchens.**  

### Code Reference:
- **CEC 2022 Section 210.8(A)(6)**:  
  *"Kitchens — where the receptacles are installed to serve the countertop surfaces."*  

### Key Details:
- Applies to **all receptacles** serving **countertop workspaces** (e.g., standard countertop outlets).
- Exceptions for **locking support/mounting receptacles** for ceiling luminaires or fans do **not apply** to standard countertop receptacles.
- No additional exceptions for kitchens in dwelling units (unlike bathrooms, which have separate exceptions).

### Inspector Note:
- Verify GFCI protection is provided via **GFCI breakers** or **GFCI receptacles**.
- Ensure coverage includes **all countertop receptacles**, including those in islands or peninsulas.

[OK] Source: CEC 2022 Section 210.8(A)(6)

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 5.3s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction under CEC 2022.

**Code Reference:**  
- **CEC 2022 Section 210.12(A)** explicitly requires AFCI protection for all 120-volt, single-phase, 15- and 20-ampere branch circuits in dwelling units, including **bedrooms**. 

**Key Details from Section 210.12(A):**  
- Applies to circuits supplying outlets or devices in bedrooms (and other listed rooms like kitchens, living rooms, etc.).  
- Permits six methods for AFCI protection, including:  
  1. Combination-type AFCI at the circuit origin.  
  2. Branch/feeder-type AFCI combined with outlet branch-circuit AFCI.  
  3. Supplemental arc protection circuit breaker with outlet AFCI (under specific conditions).  
  4. Outlet branch-circuit AFCI with overcurrent device (under specific conditions).  
  5. Outlet AFCI in metal raceway systems.  
  6. Outlet AFCI in concrete-encased wiring.  

**Exceptions:**  
- Does **not** apply to circuits dedicated to fire alarm systems (per 760.41(B)/760.121(B)).  
- Does **not** apply to circuits extended by ≤6 ft without additional outlets (per 210.12(D)).  

**Inspector Note:**  
California follows the **same AFCI requirements** as NEC 2023 for bedrooms but adds no unique exceptions. Always verify the first outlet marking and wiring method compliance with 210.12(A)(3)–(6) for alternative installations.  

[OK] Source: CEC 2022

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 4.6s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Yes**, aluminum conductors are permitted for a 200A service in California. The required size is:

- **4/0 AWG aluminum**  
- **Reference**: CEC Table 310.12(A) (Single-Phase Dwelling Services and Feeders)

### Key Requirements:
1. **Application**: For single-phase dwelling services (120/240V or 120/208Y systems).
2. **Insulation**: Conductors must have insulation rated for 75°C (e.g., THW, THWN, or equivalent).
3. **Overcurrent Protection**: 200A service disconnect must comply with 240.60 and 240.61.

### Inspector Note:
- Verify the service is for an entire dwelling unit (Table 310.12(A) applies only to complete load services).
- Confirm no temperature correction or bundling adjustments are required (standard conditions assumed in the table).

[OK] Source: CEC 2022 Table 310.12(A)

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 4.5s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Minimum Working Clearance Depth (CEC 2022)

For a **120/240V residential electrical panel** with **exposed live parts on one side** (no live/grounded parts on the other side), the minimum working clearance depth required is:

**900 mm (3 feet)**  
*Per CEC Table 110.26(A)(1), Condition 1 for 0–150V systems.*

### Key Details:
- **Condition 1** applies to most residential panels where live parts are on one side only.
- This requirement ensures safe access for maintenance and inspection.
- If the panel has live parts on both sides (Condition 3), the clearance increases to **1,050 mm (3.5 ft)**.

[OK] Source: CEC 2022 Table 110.26(A)(1)

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 5.5s

**Tools Called:** cec_search

**Answer:**

## Minimum Small Appliance Branch Circuits for Kitchen (CEC 2022)

**Answer:**  
A **minimum of two 20-ampere small-appliance branch circuits** are required to serve the kitchen in a dwelling unit.

**Code References:**  
- **CEC 2022 Section 210.52(B)(1):**  
  *"In the kitchen [...] the two or more 20-ampere small-appliance branch circuits required by 210.11(C)(1) shall serve [...] all countertop outlets [...] No small-appliance branch circuit shall serve more than one kitchen."*  

- **CEC 2022 Section 210.11(C)(1):**  
  *"Dwelling units [...] shall have two or more 20-ampere small-appliance branch circuits [...] for all receptacle outlets specified in 210.52(B)."*

**Key Requirements:**  
1. **Minimum of two circuits** must supply kitchen receptacles (including countertop outlets).  
2. Additional circuits are permitted but not required.  
3. Each small-appliance circuit may also serve other rooms (e.g., dining room) but **only one kitchen** may be served per circuit.  

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 6.9s

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for Residential Service (NEC 2023)

**Answer:**  
Yes, surge protection is required for a new 200A residential service per NEC 2023 **Section 230.67(A)(1)**.  

**Key Details:**  
- **Section 230.67(A)** mandates surge-protective devices (SPD) for services supplying **dwelling units** (among other occupancies).  
- The requirement applies to **all services** for residential occupancies, regardless of service size (e.g., 200A).  
- The SPD must be installed in accordance with NEC guidelines, typically at the service entrance (Type 1 SPD).  

**Citation:**  
NEC 2023, **Section 230.67(A)(1)**: *"All services supplying... dwelling units shall be provided with a surge-protective device (SPD)."*  

[OK] Source: NEC 2023

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 9.5s

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size

**Answer:**

## Service Conductor Sizing for 200A Dwelling (CEC 2022)

**Copper Conductors:**  
- **Size:** 2/0 AWG  
- **Reference:** CEC Table 310.12(A) for single-phase dwelling services  

**Aluminum Conductors:**  
- **Size:** 4/0 AWG  
- **Reference:** CEC Table 310.12(A) for single-phase dwelling services  

**Can Aluminum Be Used?**  
✅ Yes, aluminum is permitted for service conductors in dwellings **if** the 4/0 AWG size is used.  

---

### Key Code Requirements:  
1. **Table 310.12(A)** governs conductor sizing for single-phase dwelling services/feeder conductors.  
2. **No temperature correction or bundling adjustments** are required unless specified in the installation (not mentioned here).  
3. **California amendments** do not override this table for standard dwelling services.  

---

### Inspector Note:  
- Verify the service is a **120/240V or 120/208Y single-phase system** (per Table 310.12(A) notes).  
- Ensure terminations are rated for aluminum if used (110.14(C) applies).  

[OK] Source: CEC 2022

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 7.8s

**Tools Called:** nec_search

**Answer:**

## NEC Requirements for Multiwire Branch Circuit Breaker and Neutral Termination

### Circuit Breaker Requirements:
1. **Simultaneous Disconnection (210.4(B))**  
   - All ungrounded conductors (hots) must be disconnected simultaneously at the panel.  
   - **Implementation**: Use a **2-pole breaker** or **handle-tied single-pole breakers** to ensure both hots are disconnected together.  
   - **Inspector Note**: Handle ties must be approved for the application and cannot be removed after installation.

2. **Phasing**  
   - The two hots must be connected to **opposite phases** (120° apart) in the panel to ensure neutral current cancellation. If both hots are on the same phase, the neutral could carry double the expected current, risking overheating.

---

### Neutral Termination Requirements:
1. **Neutral Sizing**  
   - The neutral conductor must be **12 AWG** (same size as hots) to handle potential unbalanced loads.  
   - **Exception**: If the circuit is balanced (equal current on both hots), the neutral current cancels, but the conductor must still be sized per 210.4(D).

2. **Neutral Termination**  
   - The neutral must terminate **only on the neutral bus** in the panel, not on any other circuit’s neutral.  
   - **Prohibited**: Tying the neutral to another circuit’s neutral (e.g., "backfeeding" neutrals) to avoid overloading or creating parallel paths.

---

### Additional Notes:
- **Load Type**: Kitchen receptacles are typically line-to-neutral loads (210.4(C)), so the MWBC must supply only line-to-neutral loads unless exceptions apply (e.g., single utilization equipment).  
- **Code Reference**:  
  - Breaker requirements: **NEC 210.4(B)**  
  - Neutral grouping/termination: **NEC 210.4(D)** and **NEC 200.4(B)**  

[OK] Source: NEC 2023

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 6.0s

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

According to **NEC 2023 Section 210.8(A)**, GFCI protection is required for all 120–250V receptacles in the following locations within dwelling units:

1. **Bathrooms**  
2. **Garages** and accessory buildings with floors at or below grade (non-habitable, for storage/work areas)  
3. **Outdoors**  
4. **Crawl spaces** at or below grade level  
5. **Kitchens**  
6. **Areas with sinks** and permanent provisions for food preparation, beverage preparation, or cooking  
7. **Sinks** – receptacles within 6 ft (1.8 m) of the top inside edge of the bowl  
8. **Boathouses**  
9. **Bathtubs or shower stalls** – receptacles within 6 ft (1.8 m) of the outside edge  
10. **Laundry areas**  
11. **Indoor damp and wet locations**  

### Exceptions (Not Permitted for GFCI Exemption):
- Receptacles for dedicated equipment (e.g., HVAC, snow-melting) as per 426.28/427.22  
- Premises security systems  
- Weight-supporting ceiling receptacles (WSCR) for lighting/fans (if not for general use)  
- Factory-installed, non-accessible bathroom exhaust fan receptacles  

[OK] Source: NEC 2023 Section 210.8(A)

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 8.3s

**Tools Called:** cec_search

**Answer:**

## Surge Protection for Residential Service (CEC 2022)

**Requirement**:  
Surge protection **is required** for all services supplying dwelling units per **CEC 2022 Section 230.67(A)**.

**Installation Locations**:  
1. **Integral to service equipment** (e.g., within the main service panel)  
   - OR  
2. **Immediately adjacent to service equipment**  
   - OR  
3. **At the next level of distribution downstream** (if not installed in the service equipment)  

**SPD Type**:  
- Must be **Type 1 or Type 2** surge-protective device (SPD) per **230.67(C)**.

**Exception**:  
If not installed in the service equipment, the SPD can be located at downstream distribution equipment (e.g., subpanels) while still complying with code.

[OK] Source: CEC 2022

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 7.6s

**Tools Called:** nec_lookup_working_space

**Answer:**

## Working Space Requirements (NEC 2023)

The installation **meets NEC requirements** based on the following analysis:

1. **Voltage Condition**: 120V (single-phase)
2. **Applicable Condition**: 
   - **Condition 2** applies (exposed live parts on one side, grounded parts on the other side – concrete/brick/tile walls are considered grounded).
3. **Required Working Space Depth**: 
   - **300 mm (12 inches)** per NEC Table 110.26(A)(1) for Condition 2.
4. **Actual Clearance**: 
   - **24 inches** of clearance in front of the panel exceeds the required 12 inches.
   - The 18-inch offset to the side (water heater) does not violate working space requirements, as lateral spacing is not restricted by 110.26.

**Conclusion**: The 24-inch front clearance satisfies NEC 110.26(A)(1) for Condition 2. No violations identified.

[OK] Source: NEC 2023

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 6.9s

**Tools Called:** cec_search

**Answer:**

## Code Violation for Multiple Conductors on a Single Breaker Terminal (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under **CEC 240.15(A)** and **240.5(B)**. Here's the breakdown:

1. **Overcurrent Device Requirement**  
   - **240.15(A)** mandates that "a fuse or an overcurrent trip unit of a circuit breaker shall be connected in series with each ungrounded conductor."  
   - Each conductor must have its own dedicated overcurrent protection. Landing two conductors on a single breaker terminal violates this requirement unless the breaker is explicitly listed for multiple conductors.

2. **Terminal Markings**  
   - The breaker is **not marked for two conductors**, which is critical. **240.5(B)** (and NEC/UL standards) requires terminals to be **listed and marked** for multiple conductors. Without this marking, the installation is non-compliant.

3. **Risk of Poor Connection**  
   - Using a single terminal for two conductors can lead to **loose connections**, increased resistance, and potential overheating. This compromises the circuit's safety and the breaker's ability to interrupt overcurrents effectively.

4. **Permitted Exceptions**  
   - **Fixture wires** (e.g., 14 AWG or larger for 20A circuits) may have limited exceptions under **240.5(B)(2)**, but this applies only to specific low-voltage, short-length applications (e.g., lighting fixtures).  
   - **Parallel conductors** (per 310.10(G)) require separate terminals in each raceway, which is not the case here.

**Corrective Action:**  
- Install a **second 20A breaker** and connect one conductor per terminal.  
- Alternatively, use a **breaker with a listed "two-wire" terminal** (marked for two conductors) if available.

**Inspector Note:** This violation is **readily correctable** but must be addressed to ensure compliance and safety. Always verify terminal markings for multi-conductor applications.

[OK] Source: CEC 2022

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 6.0s

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

### Configuration Requirements:
1. **Separate Neutral and Ground Bars**  
   - In the subpanel, **do not bond** the neutral and ground bars. They must remain isolated (unlike the main panel).  
   - Connect the **equipment grounding conductor (EGC)** from the feeder to the subpanel's ground bar.  
   - Connect the **neutral conductor** from the feeder to the subpanel's neutral bar.  

2. **Grounding Electrode Conductor (GEC)**  
   - The subpanel **does not require a local grounding electrode** (e.g., ground rod).  
   - The **GEC from the main panel's grounding system** must be extended to the subpanel's ground bar (if required by local amendments, but typically not needed for 4-wire feeders).  

3. **Bonding**  
   - The subpanel's metal enclosure must be bonded to the EGC from the feeder.  
   - All grounding electrodes (e.g., main panel's electrode, subpanel's bonding jumper) must be **bonded together** to prevent voltage differences (per CEC 250.60).  

---

### Key Code References:
- **CEC 250.30(B)(1)**: Grounding electrode conductor sizing for derived systems (not applicable here, as this is a 4-wire feeder, not a separately derived system).  
- **CEC 250.60**: Requires bonding of all grounding electrodes to limit voltage differences.  
- **CEC 250.32(B)**: Detached structures must have the grounding system connected to the feeder's EGC, not a local electrode (unless required by specific exceptions).  

---

### Inspector Note:
- **No separate ground rod is required** for the subpanel if the feeder includes a 4-wire system (neutral + EGC).  
- Ensure the **neutral and ground bars are isolated** in the subpanel to prevent parallel paths for neutral current.  

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 7.0s

**Tools Called:** cec_search, cec_search

**Answer:**

## Main Bonding Jumper vs System Bonding Jumper (CEC 2022)

### **Main Bonding Jumper**
- **Definition**: Connection between the grounded circuit conductor (neutral) and the equipment grounding conductor **at the service** (Section 100).
- **Required When**:
  - Installed at every service to bond the grounded conductor to the equipment grounding conductor.
  - Required for services with a single or multiple enclosures (Section 250.28).
- **Sizing**: Minimum size per Table 250.102(C)(1), based on the largest ungrounded service conductor.

---

### **System Bonding Jumper**
- **Definition**: Connection between the grounded circuit conductor and the supply-side bonding jumper or equipment grounding conductor **at a separately derived system** (Section 100).
- **Required When**:
  - Installed at separately derived systems (e.g., transformers, generators) to bond the system’s grounded conductor to the equipment grounding conductor.
  - Required for systems with multiple enclosures (Section 250.28).
- **Sizing**: Minimum size per Table 250.102(C)(1), based on the largest ungrounded conductor of the separately derived system.

---

### **Key Differences**
| Feature                  | Main Bonding Jumper                     | System Bonding Jumper                     |
|--------------------------|------------------------------------------|-------------------------------------------|
| **Location**             | At the **service**                       | At **separately derived systems**          |
| **Purpose**              | Bonds service neutral to equipment ground | Bonds derived system neutral to equipment ground |
| **Applicable Systems**   | Services (e.g., utility service entrance) | Separately derived systems (e.g., transformers, generators) |
| **Code Reference**        | Section 250.28(D)                        | Section 250.28(D) and 250.168 (for DC systems) |

---

### **Inspector Note**
- **Main bonding jumpers** ensure the service is properly bonded, preventing dangerous voltage differences.
- **System bonding jumpers** ensure separately derived systems are safely referenced to ground, providing a low-impedance path for fault currents.

[OK] Source: CEC 2022

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 5.4s

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

### **1. Required Number of Circuits for Kitchen**
- **Minimum Requirement**: **Two or more 20-ampere small-appliance branch circuits** are required for all receptacle outlets in the kitchen (per **CEC 2022 Section 210.11(C)(1)**).
- **Purpose**: These circuits serve wall, floor, and countertop receptacles in the kitchen, as well as refrigeration equipment.

### **2. Can These Circuits Serve Dining Room Receptacles?**
- **Yes**, per **CEC 2022 Section 210.52(B)(1)**:
  - The two or more small-appliance branch circuits required for the kitchen **may also supply receptacle outlets in the dining room** (and other rooms like family rooms, living rooms, etc.).
  - **Key Condition**: The circuits must not serve more than **one kitchen** (to avoid overloading the circuits).

### **Code Citations**
- **210.11(C)(1)**: Mandates two or more 20A small-appliance branch circuits for kitchens.
- **210.52(B)(1)**: Permits these circuits to serve receptacles in other rooms (e.g., dining room) within the same dwelling unit.

### **Inspector Note**
- Ensure the circuits are **dedicated to small appliances** (e.g., toasters, blenders) and not overloaded with fixed equipment (e.g., microwaves, which may require a dedicated circuit).
- Dining room receptacles served by these circuits must comply with **210.52(A)** spacing requirements (≤6 ft between outlets).

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 4.4s

**Tools Called:** cec_ampacity_with_adjustments

**Answer:**

## Adjusted Ampacity for 12 AWG THHN Conductors (CEC 2022)

**Final Answer:**  
The adjusted ampacity is **19.68A** after applying temperature and bundling corrections.

---

### **Step-by-Step Breakdown:**

1. **Base Ampacity (Table 310.16):**  
   - **12 AWG THHN (90°C)** copper conductors have a base ampacity of **30A** at 30°C.

2. **Temperature Correction (Table 310.15(B)(1)(1)):**  
   - Ambient temperature = **50°C**  
   - Correction factor for 90°C insulation at 50°C = **0.82**  
   - **30A × 0.82 = 24.6A**

3. **Bundling Adjustment (Table 310.15(C)(1)):**  
   - **6 current-carrying conductors** in a raceway  
   - Adjustment factor for 6-9 conductors = **0.80**  
   - **24.6A × 0.80 = 19.68A**

4. **Overcurrent Protection Limit (240.4(D)):**  
   - 12 AWG copper is limited to **20A** overcurrent protection, per 240.4(D).  
   - The derated ampacity (19.68A) is **less than 20A**, so the OCPD must not exceed **20A**.

---

### **Key Code References:**
- **Base ampacity**: CEC Table 310.16  
- **Temperature correction**: CEC Table 310.15(B)(1)(1)  
- **Bundling adjustment**: CEC Table 310.15(C)(1)  
- **OCP limit**: CEC 240.4(D)  

---

### **Inspector Note:**  
- The adjusted ampacity (19.68A) is **below the 20A overcurrent limit**, so the circuit must be protected by a **20A breaker**.  
- Ensure the conductor is not used in a location with sustained temperatures above 50°C without additional derating.  

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 6.1s

**Tools Called:** nec_search

**Answer:**

## Why NEC Requires AFCI Protection in Bedrooms and Living Areas (NEC 2023)

### **Requirement**
NEC **Section 210.12** mandates **Arc-Fault Circuit Interrupter (AFCI)** protection for **120-volt, single-phase, 15- and 20-ampere branch circuits** in specific areas, including:
- **Bedrooms** (Section 210.12(C)(1))
- **Living rooms, hallways, closets, and similar spaces**
- **Dormitory units, hotels, and nursing homes** (Section 210.12(C) and (D))

### **Electrical Hazard Prevented**
AFCI protection prevents **electrical fires caused by arc faults**. Arc faults occur when damaged or deteriorated wiring creates high-resistance connections, generating heat and sparks. Common causes include:
- Frayed or damaged cords
- Loose connections
- Overloaded circuits
- Rodent damage

Standard circuit breakers may not detect these arcs (as they don’t always trigger overcurrent), but AFCIs identify the unique electrical signatures of dangerous arcs and **interrupt the circuit within 2 cycles (0.04 seconds)** to prevent ignition.

### **Key Code Provisions**
1. **Protection Scope** (210.12(A)):
   - Requires AFCIs to protect **the entire branch circuit**, using:
     - Combination-type AFCIs (most common)
     - Branch/feeder-type AFCIs with outlet branch-circuit-type AFCIs at the first outlet
     - Supplemental arc protection devices (limited use)

2. **Applicable Locations** (210.12(C)):
   - Bedrooms, living rooms, hallways, and similar areas in **dwelling units**
   - Extended to dormitories, hotels, and nursing home patient rooms

3. **Exceptions**:
   - Not required for fire alarm circuits (Exception No. 1)
   - Temporary extensions (<6 ft, no new outlets) (Exception in 210.12(E))

### **Inspector Note**
- **AFCIs vs. GFCIs**: AFCIs address **fire hazards** (arcs), while GFCIs (Section 210.8) address **shock hazards** (ground faults). Both may be required in the same location.
- **Compliance**: Verify AFCI protection at the **branch circuit origin** or first outlet, with proper labeling and accessible location.

[OK] Source: NEC 2023

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 5.0s

**Tools Called:** cec_search

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

**Why torque specifications are important:**  
Torque specifications ensure proper termination of conductors in panels by:  
1. **Preventing under-torqued connections** (loose connections that cause arcing/overheating)  
2. **Avoiding over-torqued connections** (damaged terminals/conductors)  
3. **Ensuring compliance with manufacturer design** (critical for listed equipment performance)  

**Code requirements location:**  
CEC 2022 **Section 110.14(D)** explicitly requires:  
- Torque values must match **equipment markings** or **manufacturer installation instructions**  
- Use **approved torque tools** or **visual indicators** (shear bolts, breakaway devices) to verify proper torque  
- Contact the **equipment manufacturer** if torque values are not provided  

**Key Code Language:**  
> "Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions... An approved means shall be used to achieve the indicated torque value."  

**Informational Notes:**  
- Examples of approved torque application methods include torque screwdrivers and breakaway-style devices.  
- UL 486A-486B Annex I provides default torque values if manufacturer data is unavailable.  

[OK] Source: CEC 2022 Section 110.14(D)

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 14.6s

**Tools Called:** cec_search

**Answer:**

## Service Load Calculation for Residential Panel (CEC 2022)

### **Step 1: General Lighting and Receptacle Load**
- **Living space**: 3,000 sq ft × 3 VA/sq ft = **9,000 VA**  
  (Per 220.82(C)(1): 3 VA/sq ft for general lighting)

### **Step 2: Small Appliance and Laundry Circuits**
- **Small appliance circuits**: 2 circuits × 1,500 VA = **3,000 VA**  
  (Per 220.82(C)(2): 1,500 VA per small appliance circuit)
- **Laundry circuit**: 1 circuit × 1,500 VA = **1,500 VA**  
  (Per 220.82(C)(3): 1,500 VA for laundry)

### **Step 3: Apply Demand Factors to General Load**
- **First 3,000 VA**: 100% → **3,000 VA**  
- **Remaining 6,000 VA**: 35% → 6,000 × 0.35 = **2,100 VA**  
  (Per 220.82(C)(1) demand factors)

**Total General Load**:  
3,000 (first 3k) + 2,100 (remaining) + 3,000 (small appliance) + 1,500 (laundry) = **9,600 VA**

---

### **Step 4: Major Appliances**
1. **Electric Range (12 kW)**:  
   - Per Table 220.55, single range ≤12 kW → **8,000 VA**  
   (Demand factor: 8 kW for 12 kW range)

2. **Dryer (5.5 kW)**:  
   - Per 220.54: 5,000 VA + 40% of (5,500 − 5,000) = **5,200 VA**

3. **Air Conditioning (4600 W)**:  
   - Larger of AC or heating load → **4,600 VA**  
   (No heating load specified; AC dominates)

**Total Major Appliances**:  
8,000 (range) + 5,200 (dryer) + 4,600 (AC) = **17,800 VA**

---

### **Step 5: Total Service Load**
- **General Load**: 9,600 VA  
- **Major Appliances**: 17,800 VA  
- **Total Load**: 9,600 + 17,800 = **27,400 VA**

---

### **Step 6: Convert to Amperes**
- **Service Voltage**: 240V  
- **Service Load Current**: 27,400 VA ÷ 240V = **114.17 A**

---

### **Conclusion**
- **200A Panel Adequacy**:  
  The calculated service load (114.17 A) is **well below** the 200A panel rating.  
  **[OK] Source: CEC 2022 Article 220 (Part IV)**

**Inspector Note**: The 200A panel is **adequately sized** for the connected loads using the optional method (220.82). No upgrades are required.

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 14.3s

**Tools Called:** nec_search, nec_lookup_working_space

**Answer:**

## Electrical Panel Inspection Violations (NEC 2023)

### 1. **Insufficient Working Space Depth (NEC 110.26(A)(1))**  
- **Violation**: The working space depth is **28 inches**, but **36 inches (3 ft)** is required for 120V panels under Condition 2 (exposed live parts on one side, grounded parts on the other).  
- **Citation**: *NEC 110.26(A)(1) and Table 110.26(A)(1)*.  
- **Inspector Note**: Depth must be measured from the panel to the point of exposure to live parts. For 120V residential panels, 36 inches is required under Condition 2.

---

### 2. **Obstruction in Working Space (NEC 110.26(B))**  
- **Violation**: The **water heater located 16 inches from the panel** intrudes into the required working space.  
- **Citation**: *NEC 110.26(B)*.  
- **Inspector Note**: Working space must be **clear of storage or obstructions**. The water heater violates this requirement, creating a safety hazard during maintenance.

---

### 3. **Height of Working Space (NEC 110.26(A)(3))**  
- **Violation**: The panel is mounted at **5 feet (60 inches)**, but the working space must extend **2.0 meters (6.56 feet)** vertically from the floor.  
- **Citation**: *NEC 110.26(A)(3)*.  
- **Inspector Note**: The working space must be clear from the floor to **6.56 feet**. If the panel’s height exceeds this, additional clearance above the panel is required.

---

### 4. **Width of Working Space (NEC 110.26(A)(2))**  
- **Violation**: The working space width is **30 inches** (assumed minimum for the panel), but the water heater reduces usable width.  
- **Citation**: *NEC 110.26(A)(2)*.  
- **Inspector Note**: The width must be **at least 30 inches** and allow **90-degree door opening**. The water heater blocks this requirement.

---

### Summary of Violations  
| Violation Type               | Code Section       | Required Fix                          |  
|------------------------------|--------------------|---------------------------------------|  
| Insufficient depth           | 110.26(A)(1)       | Increase depth to 36 inches           |  
| Obstruction (water heater)   | 110.26(B)          | Relocate water heater outside working space |  
| Height clearance violation   | 110.26(A)(3)       | Ensure 6.56 ft vertical clearance     |  
| Width obstruction            | 110.26(A)(2)       | Remove obstruction to maintain 30-inch width |  

[OK] Source: NEC 2023

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 8.4s

**Tools Called:** nec_search

**Answer:**

## Circuit Protection Requirements (NEC 2023)

### 1. **Countertop Receptacles (2 x 20A circuits)**
- **Protection**: **GFCI + AFCI**
- **References**:
  - **GFCI**: NEC 210.8(A)(6) (kitchen countertop receptacles)
  - **AFCI**: NEC 210.12(A) (required for all dwelling unit circuits except exceptions)

### 2. **Dishwasher (15A dedicated circuit)**
- **Protection**: **GFCI + AFCI**
- **References**:
  - **GFCI**: NEC 210.8(A)(6) (appliances in kitchen areas)
  - **AFCI**: NEC 210.12(A) (no exception for dishwashers)

### 3. **Garbage Disposal (15A dedicated circuit)**
- **Protection**: **GFCI + AFCI**
- **References**:
  - **GFCI**: NEC 210.8(A)(6) (appliances in kitchen areas)
  - **AFCI**: NEC 210.12(A) (no exception for garbage disposals)

### 4. **Refrigerator (20A dedicated circuit)**
- **Protection**: **Standard breaker (no GFCI or AFCI)**
- **References**:
  - **GFCI Exception**: NEC 210.8(A)(4) Exception No. 2 (refrigerators exempt from GFCI)
  - **AFCI Exception**: NEC 210.12(B) (single receptacle for refrigerator is exempt from AFCI)

---

**Inspector Note**: The refrigerator circuit qualifies for exceptions in both GFCI and AFCI requirements due to its dedicated single-receptacle configuration. All other circuits require both GFCI and AFCI protection per NEC 2023.

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 7.2s

**Tools Called:** cec_search

**Answer:**

## Subpanel Bonding Violations and Correct Configuration (CEC 2022)

### **Identified Violations**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation**: Section 250.32(B)(1) explicitly prohibits connecting the grounded (neutral) conductor to the equipment grounding conductor or grounding electrode in a detached structure. Bonding these bars creates a parallel path for neutral current, increasing shock risk and causing improper operation of GFCI devices.  
   - **Correct Action**: **Separate neutrals and grounds** in the subpanel. The neutral bar must be isolated from the ground bar and enclosure. Bonding is only permitted at the **main service panel**.

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: Section 250.24(D) requires the neutral conductor to be isolated from the enclosure in subpanels. Bonding the neutral bar to the enclosure creates an unintended grounding path, violating the "single point of bonding" rule.  
   - **Correct Action**: **Disconnect the neutral bar from the enclosure**. Neutrals should only connect to the neutral bar, which must not be bonded to any grounding components.

3. **Ground Bar Bonded to Enclosure Without Proper Grounding Electrode Connection**  
   - **Violation**: While bonding the ground bar to the enclosure is acceptable (Section 250.92(A)), the grounding electrode conductor (GEC) must also be connected to a grounding electrode (e.g., rod, plate) per Section 250.50. If this connection is missing, the system lacks proper grounding.  
   - **Correct Action**: Ensure the **grounding electrode conductor** (sized per Table 250.66 based on the largest ungrounded conductor, e.g., #2 AWG aluminum) is connected to a compliant grounding electrode.

4. **Feeder Ground Wire Connected Only to Ground Bar**  
   - **Violation**: Section 250.122 requires the equipment grounding conductor (EGC) to be sized based on the overcurrent protection (100A in this case). For aluminum, Table 250.122 specifies a minimum of **#6 AWG** for a 100A circuit. If the feeder ground is undersized (e.g., #8 AWG), it violates ampacity requirements.  
   - **Correct Action**: Verify the **EGC size** matches Table 250.122 for 100A (e.g., #6 AWG aluminum).

---

### **Correct Subpanel Configuration**
1. **Neutral Bar**  
   - **Isolated from ground bar and enclosure**.  
   - **Feeder neutral** connects only to the neutral bar.  
   - **No bonding jumpers** between neutral bar and ground/enclosure.

2. **Ground Bar**  
   - **Bonded to the metal enclosure** (per Section 250.92(A)).  
   - **Feeder ground** connects to the ground bar.  
   - **Grounding electrode conductor** (GEC) connects the ground bar to a compliant grounding electrode (e.g., 8 ft rod).

3. **Grounding Electrode Conductor (GEC)**  
   - **Size**: Per Table 250.66 for #2 AWG aluminum ungrounded conductor: **#6 AWG copper** or **#4 AWG aluminum**.  
   - **Connection**: Directly to the grounding electrode (Section 250.50).

4. **Equipment Grounding Conductor (EGC)**  
   - **Size**: Per Table 250.122 for 100A OCPD: **#6 AWG copper** or **#4 AWG aluminum**.  
   - **Connection**: From ground bar to main panel.

---

### **Summary of Fixes**
- **Remove bonding jumper** between neutral and ground bars.  
- **Disconnect neutral bar from enclosure**.  
- **Verify GEC and EGC sizes** per Tables 250.66 and 250.122.  
- **Install grounding electrode** if missing (Section 250.50).  

[OK] Source: CEC 2022 Sections 250.32, 250.24, 250.50, 250.66, 250.122

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 4.4s

**Tools Called:** nec_conduit_fill_calculator

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (NEC 2023)

**Conduit Fill Calculation:**

1. **Conduit Area (RMC 1¼"):**
   - Total area: **1.526 sq in** (NEC Chapter 9 Table 4)
   - 40% fill limit: **0.61 sq in** (40% of 1.526)

2. **Conductor Area (10 AWG THHN):**
   - Area per conductor: **0.0211 sq in** (NEC Chapter 9 Table 5)

3. **Maximum Conductors:**
   - Calculation: 0.61 ÷ 0.0211 = **28.91**
   - **Final Answer:** **28 conductors** (round down to nearest whole number)

**Verification:**
- 28 conductors × 0.0211 sq in = **0.5908 sq in** (59.08% of 1.526 sq in)
- Fill percentage: **38.7%** (within 40% limit)

**Key Notes:**
- 40% fill applies to 3–24 conductors (NEC 300.15(B)(2)(a))
- 28 conductors is the maximum allowed in 1¼" RMC
- 3 conductors requested: **YES** (uses only 4.1% of fill capacity)

[OK] Source: NEC 2023 Chapter 9 Tables 4 and 5

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 9.4s

**Tools Called:** python_calculator, cec_search

**Answer:**

## Voltage Drop Calculation (CEC 2022)

1. **Voltage drop formula**:  
   $$
   VD = \frac{2 \times I \times R \times L}{1000} = \frac{2 \times 22 \times 1.29 \times 50}{1000} = 2.84 \, \text{V}
   $$

2. **Percentage drop**:  
   $$
   \text{Percentage} = \left( \frac{2.84}{120} \right) \times 100 = 2.37\%
   $$

3. **Code Compliance Check**:  
   - **NEC 210.19(A)(1) Informational Note No. 4**: Recommends **3% maximum** for branch circuits.  
   - **CEC 2022 Section 647.4(D)**:  
     - **Fixed equipment**: Voltage drop **≤ 1.5%** (2.37% exceeds this).  
     - **Cord-connected equipment**: Voltage drop **≤ 1%** (not applicable here).  

4. **Conclusion**:  
   - **NEC**: Meets 3% recommendation.  
   - **CEC 2022**: **Does NOT meet** the stricter 1.5% requirement for fixed equipment.  

[OK] Source: CEC 2022

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 13.9s

**Tools Called:** cec_base_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_ampacity_with_adjustments

**Answer:**

## Final Adjusted Ampacity Calculation (CEC 2022)

**Given**:  
- 6 current-carrying 12 AWG TW copper conductors  
- Ambient temperature: 43°C (110°F)  

---

### **Step 1: Base Ampacity**  
From **Table 310.16** for 12 AWG copper at 60°C (TW insulation):  
**20A**  

---

### **Step 2: Temperature Correction Factor**  
From **Table 310.15(B)(1)(1)** for 43°C ambient:  
**0.71**  

---

### **Step 3: Bundling Adjustment Factor**  
From **Table 310.15(C)(1)** for 6 conductors:  
**0.80**  

---

### **Step 4: Final Calculation**  
$$
20A \times 0.71 \times 0.80 = 11.36A
$$

---

### **Final Result**  
**Adjusted ampacity: 11.36 amperes**  

---

### **Key Code References**  
- **Base ampacity**: CEC Table 310.16  
- **Temperature correction**: CEC Table 310.15(B)(1)(1)  
- **Bundling adjustment**: CEC Table 310.15(C)(1)  
- **Overcurrent protection limit**: CEC 240.4(D) (12 AWG max 20A OCP)  

---

### **Inspector Notes**  
1. The derated ampacity (11.36A) is **less than** the overcurrent protection limit (20A per 240.4(D)), so the OCP device remains compliant.  
2. Ensure the **actual load** does not exceed 11.36A to avoid overheating.  
3. Verify ambient temperature measurements in the attic, as sustained temperatures above 43°C may require additional cooling or larger conductors.  

[OK] Source: CEC 2022

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 4.6s

**Tools Called:** nec_lookup_grounding_conductor

**Answer:**

## Minimum Size Copper GEC for 1000 kcmil Service (NEC 2023)

**Answer:**  
The minimum size copper grounding electrode conductor (GEC) required is **2/0 AWG** per NEC Table 250.66.

**Calculation Details:**  
1. **Equivalent Service Conductor Size**:  
   Four parallel 250 kcmil conductors per phase = 4 × 250 kcmil = **1000 kcmil equivalent** (per Note 1 in table footnotes).

2. **Table 250.66 Lookup**:  
   For service conductors over 600 kcmil through 1100 kcmil, the minimum copper GEC size is **2/0 AWG**.

**Key Code Requirements:**  
- NEC 250.66: Grounding electrode conductor size must match the largest ungrounded service-entrance conductor.  
- Footnote 1: Parallel conductors require summing conductor areas to determine equivalent size.  

[OK] Source: NEC 2023 Table 250.66

---

