# Core (NEC) Evaluation Results - Run 29 (Tool Name Fixes)

**Date:** 2025-12-10
**Changes:** Fixed import re, tool name mismatches, CEC tools as primary

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 240.0s |
| Avg Duration | 8.9s |
| Exception Search Used | 1/27 |
| NEC Comparison Used | 0/27 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 10.1s

**Tools Called:** cec_lookup_conductor_size, cec_exception_search

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum conductor size**: **6 AWG copper**  
- **Ampacity**: 65A at 75°C (Table 310.16)  
- **Meets requirement**: 65A ≥ 60A  

**Key Notes**:  
1. **8 AWG is insufficient** (50A at 75°C) – fails to meet 60A requirement.  
2. **Overcurrent protection**: Per 240.4(D), 6 AWG copper is protected up to 60A (matches circuit rating).  
3. **No exceptions apply** for general 60A circuits (exceptions in search results relate to specialized equipment like HVAC compressors or multimotor systems).  

**Code References**:  
- Conductor sizing: CEC 2022 Table 310.16  
- Overcurrent limits: CEC 240.4(D)  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 4.8s

**Tools Called:** cec_search

**Answer:**

## GFCI Protection Requirements in Residential Kitchens (CEC 2022)

**GFCI protection is required for the following locations in residential kitchens:**

1. **Countertop Surfaces**  
   - All 125–250V receptacles installed to serve countertop surfaces must have GFCI protection.  
   - **Citation:** CEC 2022 Section 210.8(A)(6)  

2. **Within 1.8 m (6 ft) of Sinks**  
   - Receptacles located within 1.8 meters (6 feet) of the top inside edge of the sink bowl must have GFCI protection.  
   - **Citation:** CEC 2022 Section 210.8(A)(7)  

**Exceptions:**  
- Receptacles for ceiling luminaires or fans are exempt if they are not general-purpose convenience receptacles.  
- Locking support receptacles for ceiling fans/luminaires are exempt if not general-purpose.  

**Inspector Note:** Verify the shortest path measurement from the sink edge to the receptacle (no piercing walls/ceilings). Ensure countertop receptacles are GFCI-protected even if located in adjacent islands or peninsulas.  

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 4.2s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction per **CEC 2022 Section 210.12(A)**.  

### Key Requirements:
- **Scope**: Applies to all 120-volt, single-phase, 15- and 20-ampere branch circuits in dwelling units.
- **Protected Areas**: Includes bedrooms (explicitly listed in Section 210.12(A)).
- **Compliance Options**:  
  - Combination-type AFCI at the circuit origin.  
  - Branch/feeder-type AFCI + outlet branch-circuit AFCI.  
  - Supplemental arc protection + outlet branch-circuit AFCI (with length limitations).  

### Exceptions:
- Not required for fire alarm circuits installed per 760.41(B) or 760.121(B).  

**Source:** CEC 2022 Section 210.12(A).  

[OK] Source: CEC 2022

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 5.1s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Answer:**  
Yes, aluminum conductors can be used for a 200A service. The required size is **4/0 AWG aluminum** per **CEC Table 310.12(A)** (Single-Phase Dwelling Services and Feeders).

---

### Key Details:
1. **Table Reference**:  
   - **CEC Table 310.12(A)** specifies conductor sizes for single-phase dwelling services.  
   - For 200A service, the table directly lists **4/0 AWG aluminum** with a 75°C rating.

2. **Conditions for Use**:  
   - Applies to **120/240V or 120/208Y single-phase systems**.  
   - Conductors must supply the **entire load of the dwelling unit**.  
   - No temperature correction or bundling adjustments are required (per Table 310.12(A) notes).

3. **California-Specific Considerations**:  
   - No additional restrictions in CEC 2022 beyond NEC 2023.  
   - Verify compliance with **Title 24 Part 6** (Energy Efficiency Standards) if applicable.

---

### Optional Copper Alternative:
If copper is preferred, **2/0 AWG copper** is also permitted for 200A service per Table 310.12(A).

---

[OK] Source: CEC 2022

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 4.1s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Minimum Working Clearance Depth (CEC 2022)

The minimum working clearance depth required in front of a 120/240V residential electrical panel is **900 mm (3 feet)** per **CEC Table 110.26(A)(1)** for **Condition 1 or 2**. This applies to systems with voltage to ground ≤ 150V (0–150V range).

### Key Details:
- **Voltage Range**: 0–150V (covers standard 120V residential panels)
- **Condition 1**: Exposed live parts on one side with no live parts on the other, or both sides effectively guarded.
- **Condition 2**: Exposed live parts on one side and grounded parts on the other (e.g., concrete/brick walls).
- **Depth Requirement**: 900 mm (3 ft) minimum.

### Inspector Note:
For residential panels, Condition 1 or 2 typically applies. If exposed live parts exist on both sides (Condition 3), the depth increases to **1050 mm (3.5 ft)**. Always verify the installation scenario against the footnotes.

[OK] Source: CEC 2022

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 4.1s

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Minimum Requirement**:  
A **minimum of two 20-ampere small-appliance branch circuits** are required for all receptacle outlets in kitchens, pantries, breakfast rooms, and dining rooms of dwelling units.  

**Code References**:  
- **CEC 2022 Section 210.52(B)(1)**: Mandates "not fewer than two small-appliance branch circuits" for countertop and wall receptacles in kitchens.  
- **CEC 2022 Section 210.11(C)(1)**: Requires "two or more 20-ampere small-appliance branch circuits" for receptacles specified in 210.52(B).  

**Key Details**:  
- These circuits must serve **only** the receptacles in the kitchen and similar areas (no other outlets).  
- Additional circuits are permitted but **not required**.  
- Each circuit must comply with 210.23(A) (no single appliance exceeding 80% of circuit rating).  

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 5.0s

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for Residential Service (NEC 2023)

**Answer:**  
Yes, surge protection is **required** for a new 200A residential service under NEC 2023.  

**Key NEC Section:**  
- **230.67(A)** mandates that *all services supplying dwelling units* must include a **surge-protective device (SPD)**. This applies directly to residential services.  

**Details:**  
- The SPD must be installed to protect the service entrance conductors.  
- The requirement is mandatory (uses "shall be provided"), with no exceptions listed for residential applications.  

**Additional Context:**  
- **215.18(A)** and **225.42(A)** reinforce SPD requirements for feeders supplying similar occupancies, but **230.67(A)** is the primary rule for services.  
- **235.409** permits surge arresters on overhead service conductors but does not override the mandatory SPD requirement in 230.67(A).  

**Inspector Note:**  
Verify the SPD is installed **in or adjacent to the distribution equipment** on the load side of the service disconnect, as specified in **215.18(B)** and **225.42(B)**.  

[OK] Source: NEC 2023

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 6.0s

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size

**Answer:**

## Service Conductor Sizing (CEC 2022)

For a 200A residential service in California:

**Copper Conductors:**  
- **Required Size:** 2/0 AWG  
- **Ampacity:** 175A (Table 310.12(A) for dwelling services)  
- **Protection:** Permitted for 200A service per CEC Table 310.12(A)  

**Aluminum Conductors:**  
- **Required Size:** 4/0 AWG  
- **Ampacity:** 150A (Table 310.12(A) for dwelling services)  
- **Protection:** Permitted for 200A service per CEC Table 310.12(A)  

**Key Requirements:**  
1. **Table 310.12(A)** applies specifically to single-phase dwelling services (120/240V or 120/208Y systems).  
2. **No temperature or bundling adjustments** are required if the conductors are sized per Table 310.12(A).  
3. **Aluminum is permitted** for service conductors in California, provided:  
   - Terminals are rated for aluminum (e.g., CO/ALR markings).  
   - Proper installation practices are followed (e.g., torque specifications, anti-oxidant compound).  

**Inspector Note:**  
- If the service includes additional loads (e.g., EV charging, pool pumps), verify total load calculations per **CEC Article 220** to confirm 200A service adequacy.  
- For non-dwelling applications, use **Table 310.16** instead (more conservative sizing).  

[OK] Source: CEC 2022

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 6.0s

**Tools Called:** nec_search

**Answer:**

## Multiwire Branch Circuit Requirements (NEC 2023)

### Circuit Breaker Requirements
- **Simultaneous Disconnection**: A **2-pole circuit breaker** must be used to disconnect **all ungrounded conductors (hots)** simultaneously (NEC 210.4(B)). This ensures both legs of the multiwire branch circuit (MWBC) are de-energized during maintenance or overcurrent events.
- **Rating**: The breaker must match the conductor ampacity (typically 20A for 12 AWG copper).

### Neutral Termination Requirements
- **Size**: The neutral conductor must be **12 AWG copper** (same size as the hots) to handle potential unbalanced loads (NEC 210.4(C) and 250.122).
- **Termination**: The neutral must terminate on the **neutral (grounded conductor) busbar** in the panel, not on a switch or breaker terminal (NEC 250.147).

### Key Notes
- **No Neutral Disconnection**: The neutral conductor is **not disconnected** by the breaker. It remains connected to the panel’s neutral busbar at all times.
- **Load Type**: MWBCs in kitchens must supply only **line-to-neutral loads** (e.g., receptacles) unless exceptions apply (NEC 210.4(C)).

[OK] Source: NEC 2023

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 5.8s

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Locations in Residential Dwellings (NEC 2023)

According to **NEC 2023 Section 210.8(A)**, GFCI protection is required for all 125–250V receptacles in the following locations within dwelling units:

1. **Bathrooms**  
2. **Garages and accessory buildings** (floor at or below grade, non-habitable)  
3. **Outdoors**  
4. **Crawl spaces** (at or below grade)  
5. **Kitchens**  
6. **Areas with sinks and food preparation** (e.g., utility sinks, kitchenettes)  
7. **Sinks** – receptacles within **6 ft (1.8 m)** of the top inside edge of the bowl  
8. **Boathouses**  
9. **Bathtubs/showers** – receptacles within **6 ft (1.8 m)** of the outside edge  
10. **Laundry areas**  
11. **Indoor damp/wet locations**  

---

### Key Notes:
- **Exceptions** exist for specific equipment (e.g., HVAC, security systems) but do not alter the general locations listed above.  
- **Outdoor locations** include patios, decks, and garages.  
- **Damp/wet locations** may include garages, utility rooms, or areas with permanent water sources.  

[OK] Source: NEC 2023

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 8.5s

**Tools Called:** cec_search

**Answer:**

## Surge Protection Requirements for Residential Services (CEC 2022)

**Requirement:**  
Surge protection is **required** for all residential services per **CEC 2022 Section 230.67**.  

**Key Requirements:**  
1. **SPD Type**: Must be **Type 1 or Type 2** surge-protective device (SPD) (230.67(C)).  
2. **Installation Location**:  
   - **Integral to service equipment** or **immediately adjacent** to it (230.67(B)).  
   - **Exception**: SPD may be installed at the **next level distribution equipment downstream** toward the load if not integrated into the service equipment.  

**Example Installation Options:**  
- **Primary Location**: Inside the main service panel (Type 1 or Type 2 SPD).  
- **Alternative**: At a subpanel or distribution panel downstream (if using the exception).  

**Inspector Note:**  
- Verify SPD is listed for the application and meets Type 1/2 requirements.  
- Ensure replacement service equipment still complies with 230.67(D).  

[OK] Source: CEC 2022

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 31.1s

**Tools Called:** nec_search, lookup_working_space

**Answer:**

## Working Space Compliance for 240V Panel (NEC 2023)

### **Front Clearance Requirement**
- **Voltage**: 240V (151-600V range)
- **Condition 2** (live parts on one side, grounded parts on the other):  
  **Minimum depth** = **3 ft 6 in (42 inches)** per Table 110.26(A)(1).  
- **Actual clearance**: 24 inches.  
- **Result**: **Fails**. 24" < 42" required.

---

### **Side Clearance Requirement**
- **Working space width**: Must be **30 inches** (per 110.26(A)(2)) or the panel width, whichever is greater.  
- **Obstruction**: Water heater at 18 inches violates the 30-inch clear width requirement.  
- **Result**: **Fails**. Obstruction within required working space.

---

### **Key Code Violations**
1. **Front clearance** (110.26(A)(1)): 24" < 42" for 240V (Condition 2).  
2. **Side clearance** (110.26(A)(2)): Water heater intrudes into 30-inch working space.  
3. **Obstruction** (110.26(B)): Working space must be free of obstructions.

---

### **Corrective Actions**
1. Increase front clearance to **3 ft 6 in (42 inches)**.  
2. Relocate water heater to provide **30 inches of unobstructed space** to the side of the panel.  

[OK] Source: NEC 2023 Table 110.26(A)(1)

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 3.9s

**Tools Called:** cec_search

**Answer:**

## Code Violation Assessment (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under **CEC 2022 Section 408.41**.  

**Explanation:**  
- **Section 408.41** requires that *each grounded conductor* must terminate in an **individual terminal** not shared with another conductor.  
- The exception allowing multiple conductors on a single terminal **only applies if the terminal is explicitly marked/identified** for this purpose (e.g., "2-wire" or "2-conductor" marking).  
- In your case, the breaker terminal is **not marked for two conductors**, making this installation non-compliant.  

**Inspector Note:**  
This violation applies specifically to **grounded conductors** (typically neutrals). For **ungrounded conductors** (hot wires), similar rules apply under **110.14(B)** and **240.7** regarding terminal ratings and markings. Always verify terminal markings for any multi-conductor termination.  

[OK] Source: CEC 2022

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 18.0s

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

**Configuration Requirements:**

1. **Isolated Neutral and Ground Bars**  
   - The subpanel **must have separate neutral and ground bars** (no bonding). This prevents parallel neutral paths and ensures proper fault current return.  
   - **Source:** CEC 250.32(B)(1) and 250.24(D).

2. **Equipment Grounding Conductor (EGC)**  
   - The **4th wire (EGC)** from the house panel must connect to the subpanel’s **grounding bar**. This creates a low-impedance path for fault currents back to the main panel.  
   - **Size:** Match the EGC size to the feeder conductor size per Table 250.122.  
   - **Source:** CEC 250.122.

3. **Grounding Electrode Conductor (GEC)**  
   - A **separate GEC** must connect the subpanel’s grounding bar to a **local grounding electrode** (e.g., ground rod, concrete-encased electrode).  
   - **Size:** Use Table 250.66 based on the largest ungrounded feeder conductor.  
   - **Source:** CEC 250.66 and 250.32(A).

4. **No Main Bonding Jumper**  
   - **Do not bond neutral and ground** in the subpanel. This avoids creating a parallel neutral path, which could cause safety hazards or improper operation of overcurrent devices.  
   - **Source:** CEC 250.24(E) and 250.32(B)(2).

5. **Grounding Electrode Requirements**  
   - The detached garage must have its own grounding electrode system (e.g., 8 ft ground rod) connected via the GEC.  
   - **Source:** CEC 250.50 and 250.32(A).

---

**Inspector Note:**  
- Verify the EGC and GEC are sized correctly for the feeder conductors.  
- Ensure the subpanel’s neutral and ground bars are **electrically isolated** (no bonding screw or strap).  
- Confirm the local grounding electrode meets CEC 250.50 (e.g., 8 ft rod, 20 ft wire for Ufer electrode).  

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 8.5s

**Tools Called:** cec_search, cec_search

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions and Key Differences**

| Feature | **Main Bonding Jumper** | **System Bonding Jumper** |
|---------|--------------------------|---------------------------|
| **Application** | Required at **service equipment** (service disconnect) to connect the grounded (neutral) conductor to the equipment grounding conductor. | Required at the **first disconnect** of a **separately derived system** (e.g., transformer, generator, PV system) to connect the grounded conductor to the equipment grounding conductor. |
| **Code Reference** | CEC 250.24(B), 250.28 | CEC 250.30(A)(1) |
| **Purpose** | Bonds service neutral to equipment grounding at the service. | Bonds the grounded conductor of a separately derived system to its equipment grounding at the first disconnect. |
| **Sizing** | Sized per **Table 250.102(C)(1)** based on the largest ungrounded service conductor. | Sized per **Table 250.102(C)(1)** based on the largest ungrounded conductor of the separately derived system. |

---

### **When Each is Required**

#### **Main Bonding Jumper**
- **Required in all service equipment** (CEC 250.24(B)):
  - Connects the grounded (neutral) conductor to the equipment grounding conductor **at the service disconnect**.
  - Ensures the neutral and equipment grounding are bonded at the service point.
- **Example**: A standard residential service panel requires a main bonding jumper to tie the neutral bus to the equipment grounding conductor.

#### **System Bonding Jumper**
- **Required for separately derived systems** (CEC 250.30(A)(1)):
  - Applies to systems like transformers, generators, or photovoltaic systems where the grounding is independent of the main service.
  - Must be installed **at the first disconnect** of the derived system.
- **Example**: A 480V to 208V transformer secondary requires a system bonding jumper at its first disconnect to bond the grounded conductor to the equipment grounding system.

---

### **Sizing Requirements (Both Jumpers)**
- **Table 250.102(C)(1)** governs sizing for both jumpers:
  - For **main bonding jumpers**: Based on the largest ungrounded service conductor.
  - For **system bonding jumpers**: Based on the largest ungrounded conductor of the derived system.
- **Example**: For a 400A service with 500 kcmil ungrounded conductors, the main bonding jumper must be at least 1/0 AWG copper (per Table 250.102(C)(1)).

---

### **Key Exceptions**
1. **Multiple Enclosures**:
   - For services with multiple enclosures (CEC 250.28(D)(2)), each enclosure’s main bonding jumper must be sized based on the largest ungrounded conductor serving that enclosure.
2. **Separately Derived Systems with Multiple Enclosures**:
   - A single system bonding jumper at the source is permitted if sized for the equivalent largest conductor (CEC 250.28(D)(3)).
3. **Small Derived Systems**:
   - For Class 1–3 circuits from transformers ≤ 1000 VA, the system bonding jumper may be 14 AWG copper or 12 AWG aluminum (CEC 250.30(A)(1), Exception No. 3).

---

### **Inspector Note**
- **Main bonding jumpers** are **never required on the load side** of the service disconnect (CEC 250.24(A)(5)).
- **System bonding jumpers** must be **unspliced** and installed **at the first disconnect** of the derived system to prevent parallel paths for fault current.

[OK] Source: CEC 2022

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 4.9s

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

**Minimum Required Circuits:**  
At least **two 20-ampere small-appliance branch circuits** are required for the kitchen (Section 210.11(C)(1)).

**Dining Room Receptacles:**  
Yes, these circuits **can also serve dining room receptacles**. Section 210.52(B)(1) explicitly includes dining rooms in the list of areas that small-appliance branch circuits must serve. The same two circuits serving the kitchen are permitted to supply receptacles in the dining room, provided:
- The circuits are part of the same dwelling unit
- The circuits comply with the 20-ampere rating and load limitations (Section 210.23)
- The circuits are not already serving more than one kitchen (Section 210.52(B)(3))

**Key Code Citations:**
- **210.11(C)(1):** Requires two+ 20A small-appliance circuits for receptacles in kitchens, dining rooms, etc.
- **210.52(B)(1):** Permits small-appliance circuits to serve multiple rooms including kitchens and dining rooms
- **210.23:** Limits small-appliance circuits to only serve receptacles specified in 210.52

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 9.1s

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   12 AWG THHN copper at 90°C = **30A** (Table 310.16)

2. **Ambient Temperature Correction (50°C)**:  
   Correction factor = **0.82** (Table 310.15(B)(1)(1))  
   Adjusted ampacity = 30A × 0.82 = **24.6A**

3. **Bundling Adjustment (6 conductors)**:  
   Correction factor = **0.80** (Table 310.15(C)(1))  
   Final adjusted ampacity = 24.6A × 0.80 = **19.7A**

4. **Overcurrent Protection Limit**:  
   Section 240.4(D) limits 12 AWG copper to **20A maximum overcurrent protection**.

**Final Answer**:  
The adjusted ampacity is **19.7A**, but overcurrent protection is limited to **20A** per CEC 2022.  

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 5.3s

**Tools Called:** nec_search

**Answer:**

## Why NEC Requires AFCI Protection in Bedrooms and Living Areas (NEC 2023)

**Requirement Source:**  
NEC 210.12 mandates AFCI (Arc-Fault Circuit Interrupter) protection for 120V, 15A–20A branch circuits in **bedrooms, living rooms, hallways, and similar areas** of dwellings (Section 210.12(B)(1)–(5)).

---

### **Electrical Hazard Prevented**  
AFCI protection is required to **prevent electrical fires caused by arc faults**. Arc faults occur when electrical current leaks through damaged or degraded wiring, creating high-temperature arcs that can ignite surrounding materials. Common causes include:  
- Damaged appliance cords  
- Loose or corroded connections  
- Nails or screws piercing wires in walls  
- Frayed insulation in outlets or switches  

Standard circuit breakers do **not detect arcs** (they only respond to overcurrents). AFCIs use advanced electronics to identify the unique electrical signatures of dangerous arcs and **interrupt the circuit within milliseconds**, preventing fires.

---

### **Key NEC Provisions**  
1. **Scope of Protection** (NEC 210.12):  
   - Applies to **bedrooms, living rooms, hallways, closets, and similar areas** in residential units.  
   - Requires protection from the **branch circuit origin** (e.g., a combination-type AFCI breaker) or at the **first outlet** (e.g., an outlet branch-circuit-type AFCI receptacle).  

2. **Exceptions**:  
   - Not required for **fire alarm systems** (760.41(B)/760.121(B)) or **arc welding equipment** (until 2025).  
   - Minor extensions (<6 ft) without new outlets are exempt (Section 210.12(E) Exception).  

---

### **Inspector Note**  
- **AFCI vs. GFCI**: AFCIs prevent fires from arcs; GFCIs (210.8) protect against electric shock. Both may be required in the same location (e.g., a kitchen outlet needs both).  
- **Testing**: AFCI devices must be tested monthly using the "test" button to ensure functionality.  

[OK] Source: NEC 2023

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 4.5s

**Tools Called:** cec_search

**Answer:**

## Torque Specifications for Conductor Termination (CEC 2022)

Torque specifications are critical for ensuring **secure, low-resistance electrical connections** that prevent overheating, arcing, and potential fire hazards. Proper torque ensures the conductor maintains its rated ampacity without exceeding termination temperature limits, which could degrade insulation or damage equipment.

### Key Requirements:
1. **Torque Values**  
   - **Section 110.14(D)** mandates that terminal connection torque values must be **as indicated on the equipment** or in the manufacturer’s installation instructions.  
   - Approved methods to achieve torque include:  
     - Torque tools  
     - Shear bolts  
     - Breakaway-style devices with visual indicators  

2. **Temperature Coordination**  
   - **Section 110.14(C)** requires conductor ampacity to align with termination temperature ratings (e.g., 60°C or 75°C). Exceeding these limits voids the conductor’s ampacity derating calculations.  

3. **Compliance with Standards**  
   - Informational Notes reference **UL 486A-486B** (torque values for connectors) and **NFPA 70B** (maintenance practices for threaded connections).  

### Why It Matters:
- **Safety**: Improper torque causes loose connections, leading to heat buildup and failure.  
- **Code Compliance**: Ensures adherence to CEC’s coordination of conductor ampacity, termination ratings, and equipment marking (Section 110.14).  

[OK] Source: CEC 2022 Sections 110.14(C), 110.14(D)

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 9.3s

**Tools Called:** nec_search

**Answer:**

## Service Load Calculation for Residential Panel (NEC 2023)

### **Given Loads**
1. **Electric Range**: 12 kW (40A circuit)  
2. **Clothes Dryer**: 5.5 kW (30A circuit)  
3. **Small Appliance Circuits**: 2 × 20A (1500 VA each)  
4. **Laundry Circuit**: 1 × 20A (1500 VA)  
5. **General Lighting**: 3000 sq ft × 3 VA/ft² = 9000 VA  
6. **Air Conditioner**: 4600 W (19.2A at 240V)  

---

### **Step 1: General Lighting and Receptacle Load**  
- **General Lighting**: 3000 sq ft × 3 VA/ft² = **9000 VA**  
- **Small Appliance Circuits**: 2 × 1500 VA = **3000 VA**  
- **Laundry Circuit**: 1 × 1500 VA = **1500 VA**  
- **Total General Load**: 9000 + 3000 + 1500 = **13,500 VA**  

---

### **Step 2: Fixed Appliance Loads**  
- **Electric Range**: 12,000 VA (no demand factor applied in optional method)  
- **Clothes Dryer**: 5,500 VA (no demand factor applied in optional method)  
- **Air Conditioner**: 4,600 VA (no demand factor applied in optional method)  
- **Total Fixed Load**: 12,000 + 5,500 + 4,600 = **22,100 VA**  

---

### **Step 3: Apply Demand Factors (Optional Method, NEC 220.82)**  
- **First 10,000 VA**: 100% → **10,000 VA**  
- **Remaining Load**: (13,500 + 22,100) - 10,000 = **25,600 VA**  
- **40% of Remaining Load**: 25,600 × 0.4 = **10,240 VA**  
- **Total Service Load**: 10,000 + 10,240 = **20,240 VA**  

---

### **Step 4: Convert to Amperes**  
$$
\text{Service Load (A)} = \frac{20,240 \text{ VA}}{240 \text{ V}} = 84.3 \text{ A}
$$

---

### **Conclusion**  
- **Calculated Service Load**: **84.3 A**  
- **Main Breaker Rating**: **200 A**  

The 200A panel is **adequately sized** for the calculated load. The service load (84.3A) is well below the 200A rating, providing ample capacity for future expansion and safety margins.  

[OK] Source: NEC 2023 Article 220.82 (Optional Method)

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 10.1s

**Tools Called:** cec_lookup_working_space, lookup_working_space

**Answer:**

## Electrical Panel Inspection Violations (NEC 2023)

**1. Insufficient Working Space Depth**  
- **Measured**: 28 inches  
- **Required**: 36 inches (3 ft) per **NEC Table 110.26(A)(1)** for 120V panels  
- **Violation**: Fails to meet minimum depth requirement  

**2. Inadequate Working Space Width**  
- **Measured**: 30 inches  
- **Required**: Panel width + 12 inches on each side (minimum 54 inches total) per **NEC 110.26(A)(1)**  
- **Violation**: Insufficient width for safe access  

**3. Obstruction in Working Space**  
- **Issue**: Water heater located 16 inches from panel  
- **Requirement**: **NEC 110.26(B)** mandates working space must be **clear of all obstructions**  
- **Violation**: Water heater violates clearance requirement  

**4. Inadequate Headroom**  
- **Measured**: 5 ft (60 inches)  
- **Required**: Minimum 6.5 ft (78 inches) per **NEC 110.26(A)(2)**  
- **Violation**: Panel is mounted too low  

---

**Inspector Note**: All violations must be corrected before energizing the panel. The water heater must be relocated outside the working space, panel height adjusted to 6.5 ft, and working space dimensions increased to 36 inches depth and 54 inches width.  

[OK] Source: NEC 2023

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 8.1s

**Tools Called:** nec_search

**Answer:**

## Circuit Protection Requirements (NEC 2023)

### 1. **Countertop Receptacles (2 x 20A circuits)**
- **Protection Required**: **Combination AFCI/GFCI breaker**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI required for all kitchen countertop receptacles.  
  - **210.12(A)**: AFCI required for all 120V, 15/20A branch circuits in dwelling units (except garages, etc.).  

---

### 2. **Dishwasher (15A dedicated circuit)**
- **Protection Required**: **Combination AFCI/GFCI breaker**  
- **NEC References**:  
  - **210.8(E)**: GFCI required for receptacles serving specific appliances (e.g., dishwashers).  
  - **210.12(A)**: AFCI required for all 120V, 15/20A branch circuits in dwelling units.  

---

### 3. **Garbage Disposal (15A dedicated circuit)**
- **Protection Required**: **Combination AFCI/GFCI breaker**  
- **NEC References**:  
  - **210.8(E)**: GFCI required for receptacles serving specific appliances (e.g., garbage disposals).  
  - **210.12(A)**: AFCI required for all 120V, 15/20A branch circuits in dwelling units.  

---

### 4. **Refrigerator (20A dedicated circuit)**
- **Protection Required**: **AFCI breaker only**  
- **NEC References**:  
  - **210.8(E) Exception**: A dedicated circuit for a specific appliance (e.g., refrigerator) is **permitted to omit GFCI** if it is a 15A or 20A circuit.  
  - **210.12(A)**: AFCI required for all 120V, 15/20A branch circuits in dwelling units.  

---

### Summary Table
| Circuit Type               | Protection Required         | NEC Sections Cited                     |
|---------------------------|-----------------------------|----------------------------------------|
| Countertop (20A)          | AFCI + GFCI                 | 210.8(A)(6), 210.12(A)                 |
| Dishwasher (15A)          | AFCI + GFCI                 | 210.8(E), 210.12(A)                    |
| Garbage Disposal (15A)    | AFCI + GFCI                 | 210.8(E), 210.12(A)                    |
| Refrigerator (20A)        | AFCI only                   | 210.8(E) Ex., 210.12(A)                |

[OK] Source: NEC 2023

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 5.6s

**Tools Called:** cec_search

**Answer:**

## Subpanel Grounding and Bonding Violations (CEC 2022)

**Identified Violations:**

1. **Neutral and Ground Bars Bonded Together (Inspector Note 1)**  
   - **Violation:** CEC 2022 **250.32(B)** and **250.24(D)** require subpanels to have **separate neutral and ground bars**. The main bonding jumper (which connects neutral and ground) is **only permitted in the main service panel**.  
   - **Correct Configuration:**  
     - Neutral and ground bars must be **electrically isolated** in the subpanel.  
     - The **feeder neutral** connects to the neutral bar.  
     - The **feeder equipment grounding conductor (EGC)** connects to the ground bar.  
     - The ground bar is bonded to the metal enclosure (per 250.4(A)(3)), but **not the neutral bar**.

2. **Neutral Bar Bonded to Metal Enclosure (Inspector Note 3)**  
   - **Violation:** CEC 2022 **250.24(D)** prohibits bonding the neutral to the subpanel enclosure. This creates a parallel path for fault currents, risking equipment damage and shock hazards.  
   - **Correct Configuration:**  
     - The **neutral bar must remain isolated** from the enclosure.  
     - Only the **ground bar** is bonded to the enclosure (per 250.4(A)(3)).

3. **Ground Bar Bonded to Enclosure (Inspector Note 2)**  
   - **Compliant:** This is correct per **250.4(A)(3)**. The ground bar must be bonded to the metal enclosure to ensure a low-impedance fault current path.

---

**Correct Subpanel Configuration for Detached Garage (CEC 2022):**

1. **Neutral Bar:**  
   - Connected only to the **feeder neutral conductor**.  
   - **Isolated from the ground bar and enclosure**.  

2. **Ground Bar:**  
   - Connected to the **feeder equipment grounding conductor** (from main panel).  
   - Bonded to the **metal enclosure** (per 250.4(A)(3)).  
   - Connected to a **separate grounding electrode** (e.g., ground rod) per **250.50** if required by local amendments.  

3. **Main Bonding Jumper:**  
   - **Removed** from the subpanel. Only present in the **main service panel** (per 250.24(B)).  

---

**Inspector Note:**  
- The **feeder ground wire connected to the ground bar** (Note 4) and **feeder neutral connected to the neutral bar** (Note 5) are compliant.  
- The critical errors are the **bonding of neutral/ground bars** and **neutral bar to enclosure**.  

[OK] Source: CEC 2022 Sections 250.24, 250.32, 250.4

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 4.7s

**Tools Called:** lookup_conduit_fill

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (NEC 2023)

**Calculation Steps:**

1. **Conduit Fill Area (40% of total area):**  
   - RMC 1¼" total area = 1.526 in² (NEC Table 4)  
   - 40% fill limit = 1.526 × 0.40 = **0.6104 in²**

2. **Conductor Cross-Sectional Area:**  
   - 10 AWG THHN = 0.0211 in² (NEC Table 5)

3. **Maximum Conductors:**  
   - 0.6104 ÷ 0.0211 ≈ **28.91** → **28 conductors** (round down)

**Verification for 3 Conductors:**  
- Total area used = 3 × 0.0211 = 0.0633 in²  
- Fill percentage = (0.0633 ÷ 1.526) × 100 ≈ **4.1%** (well within 40% limit)

**Final Answer:**  
**28** is the maximum number of 10 AWG THHN conductors permitted in 1¼" RMC.  

[OK] Source: NEC 2023 Chapter 9 Tables 4 and 5

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 11.1s

**Tools Called:** python_calculator, python_calculator, cec_search

**Answer:**

## Voltage Drop Verification (CEC 2022)

1. **Calculation Summary**:
   - **Voltage Drop**: 2.84 V (2.37% of 120V)
   - **NEC Recommendation**: ≤ 3% for branch circuits (per 210.19(A)(1) FPN)
   - **CEC Specific Rule**:  
     - **Section 647.4(D)**:  
       - Fixed equipment: ≤ 1.5% branch circuit drop  
       - Combined feeder/branch: ≤ 2.5%  
     - **Applies to**: Low-voltage technical systems (e.g., 60/120V 3-wire)  

2. **Application to This Case**:
   - The circuit is a **standard 120V single-phase branch circuit**, not a low-voltage technical system (Section 647.4 applies to specialized systems like 60/120V 3-wire).  
   - **General branch circuits** follow NEC recommendations (≤ 3%) unless restricted by CEC-specific rules.  

3. **Conclusion**:
   - **2.37% voltage drop** is **within NEC/CEC limits** for general branch circuits.  
   - No stricter CEC rules apply to this configuration.  

[OK] Source: CEC 2022 (incorporates NEC 2023)

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 7.1s

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   12 AWG TW copper at 60°C = **20A** (Table 310.16)

2. **Temperature Correction**:  
   Ambient = 43°C → Correction factor = **0.71** (Table 310.15(B)(1)(1))  
   Adjusted: 20A × 0.71 = **14.2A**

3. **Bundling Adjustment**:  
   6 conductors in conduit → Adjustment factor = **0.80** (Table 310.15(C)(1))  
   Final adjusted ampacity: 14.2A × 0.80 = **11.36A**

**Final Answer**:  
The adjusted ampacity is **11.36A** after applying both temperature correction and bundling adjustment factors.

[OK] Source: CEC 2022

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 34.9s

**Tools Called:** cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor

**Answer:**



---

