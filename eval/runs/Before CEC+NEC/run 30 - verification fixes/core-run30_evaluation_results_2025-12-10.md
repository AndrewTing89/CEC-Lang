# Core (NEC) Evaluation Results - Run 30 (Verification Fixes)

**Date:** 2025-12-10
**Changes:** Enhanced Step 4, correction factor verification, auto-retry on hallucination

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 237.9s |
| Avg Duration | 8.8s |
| Exception Search Used | 0/27 |
| NEC Comparison Used | 0/27 |
| Hallucination Retries | 0/27 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 3.9s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size**: **6 AWG copper**  
- **Ampacity**: 65A at 75°C (meets 60A requirement)  
- **Table reference**: CEC Table 310.16  

**Key Notes**:  
1. **8 AWG is insufficient** (50A at 75°C) – fails to meet 60A requirement.  
2. **Overcurrent protection**: Per **240.4(D)**, a 60A breaker is acceptable for 6 AWG copper (65A ampacity).  
3. **Adjustments required if**:  
   - Ambient temperature >30°C (use **310.15(B)** correction factors).  
   - More than 3 current-carrying conductors (use **310.15(C)(1)** bundling factors).  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 12.7s

**Tools Called:** cec_search

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**GFCI protection is required for all 125–250V receptacles in residential kitchens that serve countertop surfaces** (CEC 2022 Section 210.8(A)(6)). This includes:

- **Countertop receptacles**: Any outlet installed to serve the countertop work surface must have GFCI protection.
- **Receptacles within 1.8 m (6 ft)** of a sink bowl edge also require GFCI protection (Section 210.8(A)(7)), though this applies to sinks in general, not exclusively kitchens.

### Key Requirements:
1. **Scope**: Applies to dwelling units (residential homes).
2. **Circuit Type**: Covers 15- and 20-ampere branch circuits (standard for kitchen countertop outlets).
3. **Exceptions**: 
   - Locking receptacles for ceiling luminaires/fans (if not general-purpose) may be exempt.
   - Receptacles for fire alarm systems (covered under 760.41(B)).

### Supporting Sections:
- **210.52(B)(3)**: Countertop receptacles are part of the required small-appliance branch circuits (two 20A circuits minimum for kitchens).
- **210.11(C)(1)**: These circuits must supply all countertop outlets and other kitchen receptacles.

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 4.9s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction in California.  

**Code Reference:**  
- **CEC 2022 Section 210.12(A)** mandates arc-fault circuit-interrupter (AFCI) protection for all 120-volt, single-phase, 15- and 20-ampere branch circuits in dwelling units, including bedrooms.  

**Key Details:**  
- **Required Protection Methods:**  
  1. Combination-type AFCI at the origin of the branch circuit.  
  2. Branch/feeder-type AFCI combined with outlet branch-circuit-type AFCI at the first outlet.  
  3. Supplemental arc protection circuit breaker with outlet branch-circuit AFCI (with specific conditions).  
  4. Outlet branch-circuit AFCI at the first outlet (with specific conditions).  

- **Exceptions:**  
  - Not applicable for new construction; exceptions pertain to modifications/extensions or specific wiring methods (not relevant here).  

**Inspector Note:**  
Verify the AFCI type and installation location per 210.12(A)(1)–(6). Ensure the first outlet box is marked if using outlet branch-circuit AFCIs.  

[OK] Source: CEC 2022

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 5.4s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Answer:**  
Yes, aluminum conductors can be used for a 200A service. The required size is **4/0 AWG aluminum** at 75°C, as specified in **CEC Table 310.12(A)** for single-phase dwelling services.

---

### Key Details:
1. **Applicable Table**:  
   - **CEC Table 310.12(A)** (Single-Phase Dwelling Services and Feeders)  
   - This table is specific to dwelling units with 120/240V or 120/208Y systems.

2. **Conditions for Use**:  
   - The conductors must supply the **entire load** of the dwelling unit.  
   - No temperature correction or bundling adjustments are required (as per the table's notes).  

3. **California-Specific Compliance**:  
   - CEC 2022 incorporates NEC 2023 with amendments. No additional restrictions on aluminum conductors are specified in California for this application.  

4. **Grounding Electrode Conductor (GEC)**:  
   - If needed, refer to **CEC Table 250.66** for the GEC size based on the 4/0 AWG service conductor.  

---

[OK] Source: CEC 2022

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 7.8s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Minimum Working Clearance Depth (CEC 2022)

The minimum working clearance depth required in front of a 120/240V residential electrical panel is **3 feet (900 mm)** per **CEC Table 110.26(A)(1)** for **Condition 1**. 

### Conditions Applicable:
- Exposed live parts on one side of the working space and **grounded parts** on the other side (e.g., metal panel enclosure).
- Concrete, brick, or tile walls are considered grounded.

### Code Reference:
- **CEC 2022 Table 110.26(A)(1)** (aligns with NEC 2023 Table 110.26(A)(1) with no California amendments in this section).

[OK] Source: CEC 2022

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 5.2s

**Tools Called:** cec_search

**Answer:**

## Minimum Small Appliance Branch Circuits for Kitchen (CEC 2022)

**Answer:**  
A minimum of **2** 20-ampere small appliance branch circuits are required for a kitchen in a dwelling unit.

**Code Basis:**  
- **CEC 220.52(A)** requires 1500 VA per small-appliance branch circuit, referencing **210.11(C)(1)**.  
- **NEC 210.11(C)(1)** (adopted in CEC) mandates **at least two** 20A small-appliance branch circuits for kitchens.  

**Inspector Note:**  
California does not amend this requirement from NEC. The two circuits must serve countertop and dining area receptacles, with no single circuit covering the entire kitchen.  

[OK] Source: CEC 2022 (incorporates NEC 2023)

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 5.4s

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for Residential Service (NEC 2023)

**Answer:**  
Yes, surge protection is required for a new 200A residential service under **NEC 2023 Section 230.67(A)**. This section mandates that all services supplying dwelling units (residential services) must include a **surge-protective device (SPD)**.  

### Key Details:
- **Applicability**: Applies to services for dwelling units, dormitory units, guest rooms, and specific healthcare facilities.
- **Installation Location**: The SPD must be installed **in or adjacent to distribution equipment**, connected to the **load side of the service disconnecting means**.
- **Informational Note**: Surge protection is most effective when installed closest to the branch circuit, but the code requires it at the service level for residential occupancies.

**Source:** NEC 2023 Section 230.67(A)  

[OK] Source: NEC 2023

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 8.6s

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size

**Answer:**

## Service Conductor Sizing (CEC 2022)

**For 200A residential service:**
- **Copper conductors**: 2/0 AWG (Table 310.12(A))
- **Aluminum conductors**: 4/0 AWG (Table 310.12(A))

**Key Requirements:**
1. **Table 310.12(A)** applies to single-phase dwelling services/feeders with:
   - 120/240V or 120/208Y systems
   - No temperature correction/adjustment factors needed
   - Conductors supplying entire dwelling load

2. **California-Specific Notes:**
   - CALGreen requires EV readiness (240V circuit) in new construction, but this is an upgrade
   - No additional amendments affecting conductor sizing in this scenario

**Inspector Note:** If conductors will be exposed to elevated temperatures (>30°C ambient) or bundled in raceways with >3 current-carrying conductors, derating factors from **Table 310.15(B)(1)(1)** and **310.15(C)(1)** would require larger conductors.

[OK] Source: CEC 2022

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 6.6s

**Tools Called:** nec_search

**Answer:**

## Multiwire Branch Circuit Requirements (NEC 2023)

### Circuit Breaker Requirements
1. **Simultaneous Disconnection** (NEC 210.4(B)):  
   - All ungrounded (hot) conductors must be disconnected simultaneously at the panel.  
   - **Implementation**: Use a **2-pole circuit breaker** rated for the circuit (typically 20A for kitchen small-appliance circuits).  
   - **Inspector Note**: Single-pole breakers with handle ties are *not* permitted for MWBCs (NEC 210.4(B) Exception does not apply here).

2. **Breaker Rating**:  
   - For kitchen small-appliance branch circuits (210.52(B)), the breaker must be **20A**.

---

### Neutral Termination Requirements
1. **Neutral Sizing**:  
   - The neutral conductor must be the **same size as the ungrounded conductors** (12 AWG in this case).  
   - **NEC Reference**: 210.4(D) requires the grounded (neutral) conductor to be grouped with the ungrounded conductors.

2. **Proper Connection**:  
   - The neutral must terminate **only on the neutral busbar** in the panel.  
   - **No sharing** with other circuits unless permitted by 210.4(B) (not applicable here).

3. **Load Balance**:  
   - The neutral carries the *difference* in current between the two hot conductors.  
   - If the circuit supplies only line-to-neutral loads (as required by 210.4(C)), the neutral size remains 12 AWG.

---

### Key Code Citations
- **Simultaneous Disconnection**: NEC 210.4(B)  
- **Neutral Sizing**: NEC 210.4(D)  
- **Kitchen Circuit Requirements**: NEC 210.52(B)  

[OK] Source: NEC 2023

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 5.8s

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

**Locations requiring GFCI protection per NEC 210.8(A):**

1. **Bathrooms**  
   - All 125–250V receptacles.  
   *(Exception: Receptacles for listed HVAC equipment or security systems may omit GFCI.)*

2. **Garages and Accessory Buildings**  
   - Receptacles in garages and accessory buildings with floors at or below grade (storage/work areas).  
   *(Exception: Receptacles for snow-melting/deicing systems may omit GFCI.)*

3. **Outdoors**  
   - All outdoor receptacles.  
   *(Exception: Rooftop receptacles not readily accessible may omit GFCI.)*

4. **Crawl Spaces**  
   - Receptacles in crawl spaces at or below grade.  

5. **Kitchens**  
   - Receptacles in kitchens (including countertops and food-prep areas).  

6. **Areas with Sinks**  
   - Receptacles within **6 ft (1.8 m)** of the top inside edge of a sink bowl.  

7. **Bathtubs/Showers**  
   - Receptacles within **6 ft (1.8 m)** of the outside edge of a bathtub or shower stall.  

8. **Laundry Areas**  
   - All receptacles in laundry rooms.  

9. **Indoor Damp/Wet Locations**  
   - Receptacles in areas classified as damp or wet (e.g., near swimming pools, hot tubs).  

10. **Boathouses**  
    - Receptacles in boathouses.  

---

**Additional Notes:**  
- **Exceptions**: Specific exceptions apply for equipment like HVAC systems, security systems, or industrial-grade appliances (see NEC 210.8(A) for full details).  
- **Crawl Spaces**: GFCI required for lighting outlets in crawl spaces (NEC 210.11(C)).  
- **Outdoor Outlets**: Explicitly covered in 210.8(A)(3).  

[OK] Source: NEC 2023, Section 210.8(A) and related exceptions.

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 4.2s

**Tools Called:** cec_search

**Answer:**

## Surge Protection for 200A Residential Service (CEC 2022)

**Requirement**:  
Surge protection is **required** for all services supplying dwelling units per **CEC 2022 Section 230.67(A)**.  

**Installation Locations**:  
1. **Integral to service equipment** (e.g., main panel)  
2. **Immediately adjacent to service equipment**  
3. **Next level distribution equipment downstream** (Exception to 230.67(B))  

**Allowed Equipment Types**:  
- **Type 1 or Type 2 SPDs** (Section 230.67(C))  
- May also include **surge arresters** (Section 230.209) for overhead services  

**Supply-Side Installation**:  
Per **Section 230.82(4)**, Type 1 SPDs are permitted on the supply side of the service disconnect.  

[OK] Source: CEC 2022

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 5.1s

**Tools Called:** lookup_working_space

**Answer:**

## Working Space Clearance (NEC 2023)

The installation **does not meet NEC requirements** for working space clearance. Here's the breakdown:

1. **Required Depth**:  
   - For 120V equipment (0-150V range), **36 inches (3 ft)** is required under **Condition 1** (no grounded parts on the opposite side of the panel).  
   - If grounded parts (like a water heater) are on the opposite side, **Condition 2** applies, requiring **30 inches (2.5 ft)**.

2. **Actual Clearance**:  
   - **24 inches** of front clearance is **less than the minimum 30–36 inches** required, regardless of the water heater's position.

3. **Water Heater Proximity**:  
   - The 18-inch offset of the water heater does not satisfy NEC requirements. The working space must be unobstructed **in front of the panel** (not to the side).  

**Conclusion**: The panel violates NEC 110.26(A)(1) due to insufficient working space depth. Minimum clearance must be **30–36 inches**, depending on the presence of grounded parts on the opposite side.

[OK] Source: NEC 2023

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 8.1s

**Tools Called:** cec_search, cec_search

**Answer:**

## Multiple Conductors on a Single Breaker Terminal (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under CEC 2022.  

**Key Requirements:**  
1. **Section 408.41** explicitly requires that *each grounded conductor terminate in an individual terminal within a panelboard*.  
   - Exception: Only applies to **parallel conductors** (e.g., 1/0 AWG or larger) terminated in a single terminal if the terminal is identified for multiple conductors.  
   - Your case involves **12 AWG conductors**, which are not parallel conductors.  

2. **Section 240.21(B)(2)** and **240.21(C)** address conductor taps and transformer secondary conductors but do not permit multiple conductors on a single overcurrent device termination unless specifically allowed (not applicable here).  

3. **Section 110.14(A)** (general NEC/CEC principle): Conductors must be terminated in a way that ensures a *mechanically and electrically secure connection*. Using two conductors on a terminal not rated for this risks poor contact, overheating, or terminal damage.  

**Inspector Note:**  
Breaker terminals marked for multiple conductors (e.g., "2-wire" or "2-conductor") are required for this installation. For 12 AWG copper, use a single conductor per terminal. If multiple conductors are needed, install a second breaker or use a listed multi-wire termination device.  

[OK] Source: CEC 2022 Sections 408.41, 240.21, 110.14(A)

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 6.0s

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### Key Requirements:
1. **Grounding Electrode System**  
   - A **local grounding electrode** (e.g., ground rod) **must be installed** at the detached garage (Section 250.32(A)).  
   - The **grounding electrode conductor (GEC)** connects this electrode to the **grounding bus** in the garage subpanel (Section 250.32(E)).  

2. **Equipment Grounding Conductor (EGC)**  
   - The **4-wire feeder** includes an **equipment grounding conductor** (4th wire) that runs from the **house panel** to the **garage subpanel**.  
   - This EGC connects to the **grounding bus** in the garage subpanel (Section 250.32(B)(1)).  

3. **Neutral and Ground Separation**  
   - In the **garage subpanel**, **neutral and ground must be isolated** (not bonded). Bonding occurs **only at the main service panel** (Section 250.24(B)).  

4. **Sizing Requirements**  
   - **EGC size**: Based on the feeder’s overcurrent protection (e.g., 100A feeder → 8 AWG copper, per Table 250.122).  
   - **GEC size**: Based on the largest ungrounded conductor (e.g., 100A feeder → 8 AWG copper, per Table 250.66).  

5. **No Neutral-to-Ground Bond in Subpanel**  
   - The **neutral bus** in the subpanel must remain **electrically isolated** from the grounding system (Section 250.32(B)(1)).  

---

### Diagram Summary:
```
House Panel
├── Ungrounded (Hot) Conductors → Garage Subpanel
├── Grounded (Neutral) Conductor → Garage Subpanel (connected to neutral bus)
├── Equipment Grounding Conductor (EGC) → Garage Subpanel (connected to grounding bus)
Garage Grounding Electrode (Rod)
└── Grounding Electrode Conductor (GEC) → Garage Subpanel (connected to grounding bus)
```

---

### Inspector Notes:
- **Verify** the GEC is **bonded to a grounding electrode** (e.g., 8 ft ground rod) at the garage.  
- **Confirm** the EGC is sized per Table 250.122 and the GEC per Table 250.66.  
- **Ensure** neutral and ground buses are **separated** in the subpanel.  

[OK] Source: CEC 2022 Sections 250.32, 250.66, 250.122

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 6.8s

**Tools Called:** cec_search, cec_search

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
1. **Main Bonding Jumper**  
   - **CEC 2022 Section 100**: Connects the *grounded circuit conductor* to the *equipment grounding conductor* **at the service**.  
   - Ensures the service neutral (grounded conductor) is bonded to the equipment grounding system.

2. **System Bonding Jumper**  
   - **CEC 2022 Section 100**: Connects the *grounded conductor* to the *supply-side bonding jumper* or *equipment grounding conductor* **at a separately derived system** (e.g., transformers, generators).  
   - Bonds the system neutral to the equipment grounding system at the source of a separately derived system.

---

### **When Each is Required**
- **Main Bonding Jumper**  
  - **Required at every service** (CEC 2022 250.28).  
  - Used in **service equipment** to ensure the grounded conductor (neutral) is bonded to the equipment grounding conductor.  
  - **Example**: A residential service panel requires a main bonding jumper to connect the neutral bus to the equipment grounding bus.

- **System Bonding Jumper**  
  - **Required at every separately derived system** (CEC 2022 250.28, 250.168).  
  - Used in **separately derived systems** (e.g., transformers, solar inverters, generators) to bond the grounded conductor to the equipment grounding system.  
  - **Example**: A 480V to 208V transformer requires a system bonding jumper at its secondary side to connect the neutral to the equipment grounding conductor.

---

### **Sizing Requirements**
Both jumpers are sized using **Table 250.102(C)(1)** based on the largest ungrounded conductor in the system:  
- **Copper Conductors**:  
  - For example, if the largest ungrounded conductor is 350 kcmil copper, the bonding jumper must be **1/0 AWG copper**.  
- **Aluminum Conductors**:  
  - For example, if the largest ungrounded conductor is 500 kcmil aluminum, the bonding jumper must be **3/0 AWG aluminum**.  

**Notes**:  
- If conductors are larger than 1100 kcmil copper or 1750 kcmil aluminum, additional rules apply (see Table 250.102(C)(1) Notes 1–3).  
- Material must match the system (copper, aluminum, or copper-clad aluminum).

---

### **Key Differences**
| Feature                  | Main Bonding Jumper                     | System Bonding Jumper                     |
|--------------------------|-----------------------------------------|-------------------------------------------|
| **Location**             | At the **service**                      | At the **separately derived system**      |
| **Application**          | Service equipment (e.g., utility service) | Separately derived systems (e.g., transformers, generators) |
| **Code Reference**       | CEC 2022 250.28, 250.102                | CEC 2022 250.28, 250.168, 250.102         |

---

### **Inspector Note**
- **Main bonding jumpers** are part of the service installation and ensure the service neutral is bonded to the equipment grounding system.  
- **System bonding jumpers** are critical for separately derived systems to prevent dangerous voltage shifts between the grounded conductor and equipment.  
- Both must be sized per Table 250.102(C)(1) and installed per 250.28(D).  

[OK] Source: CEC 2022

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 4.9s

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

**1. Required Number of Circuits:**
- **Minimum Requirement**: **Two 20-ampere small-appliance branch circuits** are required for all receptacle outlets in kitchens, pantries, breakfast rooms, and dining rooms (CEC 2022 Section 210.52(B)(1)).  
- **No Other Outlets**: These circuits shall have **no other outlets** except those specified (e.g., countertop, wall, and floor receptacles in covered areas).

**2. Serving Dining Room Receptacles:**
- **Permitted**: Yes, these small-appliance branch circuits **can also serve dining room receptacles**.  
- **Code Basis**: Section 210.52(B)(1) explicitly allows the circuits to supply receptacle outlets in the same kitchen **and other rooms** (including dining rooms) specified in the section.  
- **Limitation**: A small-appliance branch circuit **shall not serve more than one kitchen** (prevents a single circuit from serving multiple kitchens).

---

### Inspector Notes:
- **Dining Room Inclusion**: The dining room is explicitly listed in Section 210.52(B)(1) as a space where small-appliance circuits can serve receptacles.  
- **No Overloading**: Ensure the circuits are not overloaded by adhering to the 20-ampere rating and avoiding additional non-specified outlets.  
- **California-Specific**: CEC 2022 aligns with NEC 2023 for this requirement, with no amendments affecting this rule.

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 6.6s

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   12 AWG THHN copper at 90°C = **30A** (Table 310.16)

2. **Temperature Correction**:  
   50°C ambient → 0.82 factor (Table 310.15(B)(1)(1))  
   30A × 0.82 = **24.6A**

3. **Bundling Adjustment**:  
   6 conductors → 0.8 factor (Table 310.15(C)(1))  
   24.6A × 0.8 = **19.68A**

4. **Final Adjusted Ampacity**:  
   **19A** (rounded down per 310.15(B)(2)(a))

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 6.0s

**Tools Called:** nec_search

**Answer:**

## Why NEC Requires AFCI Protection in Bedrooms and Living Areas (NEC 2023)

### **Requirement**
The NEC mandates **arc-fault circuit interrupter (AFCI) protection** for all 120-volt, single-phase, 15- and 20-ampere branch circuits in **bedrooms, living rooms, and similar areas** of dwelling units (NEC 210.12(B), (C)). This includes:
- Bedrooms
- Living rooms
- Hallways
- Closets
- Bathrooms
- Similar rooms

### **Electrical Hazard Prevented**
AFCIs are designed to **detect and interrupt arc faults**, which are a leading cause of electrical fires in residential buildings. Arc faults occur when damaged or degraded wiring creates a high-resistance path, generating heat and sparks that can ignite surrounding materials. Common causes include:
- Damaged cords or outlets
- Loose connections
- Overloaded circuits
- Rodent damage to wiring

### **Key Code Provisions**
- **NEC 210.12(A)**: Specifies acceptable methods for AFCI protection (e.g., combination-type, branch/feeder-type, outlet branch-circuit-type).
- **NEC 210.12(B)/(C)**: Extends AFCI requirements to dormitory units, guest rooms in hotels/motels, and nursing home patient sleeping rooms.
- **Exceptions**: Allow exemptions for fire alarm systems (760.41(B)/760.121(B)) and temporary arc welding circuits (until 2025).

### **Inspector Note**
AFCIs differ from GFCIs (ground-fault protection for personnel safety). While GFCIs protect against shocks, AFCIs focus on **fire prevention** by detecting series arcs (common in damaged wiring) and parallel arcs (short circuits). The requirement reflects data showing that 44% of home electrical fires are caused by wiring issues, with bedrooms and living areas being high-risk zones due to frequent use of portable devices and aging infrastructure.

[OK] Source: NEC 2023

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 5.2s

**Tools Called:** cec_search

**Answer:**

## Torque Specifications for Conductor Termination (CEC 2022)

Torque specifications are critical for conductor terminations in panels to ensure **secure, low-resistance connections** that prevent overheating, arcing, and equipment damage. Improper torque (too loose or too tight) can lead to:

- **Loose connections**: Increased resistance → heat → potential fire hazards
- **Over-torqued connections**: Damaged terminals/conductors → poor conductivity → failure

### Requirements Location
The CEC 2022 mandates torque specifications in **Section 110.14(D)** with key details:

1. **Torque Values**  
   - "Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer."  
   - **Source**: CEC 2022 Section 110.14(D)

2. **Approved Methods**  
   - Requires use of "an approved means" (e.g., torque tools, shear bolts, or breakaway devices with visual indicators) to achieve specified torque.  
   - **Source**: CEC 2022 Section 110.14(D) Informational Note 1

3. **Manufacturer Guidance**  
   - If torque values aren't marked on equipment, consult the manufacturer or refer to **UL 486A-486B** standards.  
   - **Source**: CEC 2022 Section 110.14(D) Informational Note 2

4. **Additional Context**  
   - For control circuit devices with screw-type terminals using 14 AWG or smaller copper conductors, a **minimum torque of 0.8 N·m (7 lb-in.)** is required unless otherwise specified.  
   - **Source**: CEC 2022 Section 430.9(C)

---

### Inspector Note
Always verify torque values directly on the equipment or in the manufacturer’s documentation. Relying on assumptions (e.g., "standard" torque values) is not compliant with CEC 110.14(D). Use calibrated torque tools for critical connections (e.g., service panels, motor controllers).

[OK] Source: CEC 2022

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 11.8s

**Tools Called:** cec_search

**Answer:**

## Service Load Calculation for Residential Panel (CEC 2022)

### **Step 1: General Lighting and General Use Circuits**
- **3000 sq ft × 3 VA/ft²** = **9,000 VA**  
- **Small appliance circuits**: 2 × 1,500 VA = **3,000 VA**  
- **Laundry circuit**: 1 × 1,500 VA = **1,500 VA**  
- **Total general load**: **13,500 VA**  

---

### **Step 2: Appliance Loads**
1. **Electric Range (12 kW)**  
   - **Demand factor per Table 220.55**: 8,000 VA  

2. **Dryer (5.5 kW)**  
   - **Nameplate rating**: 5,500 VA  

3. **Central AC (4600 W)**  
   - **Noncoincident with heating** (no heating mentioned): **4,600 VA**  

---

### **Step 3: Total Load Before Demand Factors**
- **General load**: 13,500 VA  
- **Range**: 8,000 VA  
- **Dryer**: 5,500 VA  
- **AC**: 4,600 VA  
- **Total**: **21,600 VA**  

---

### **Step 4: Apply Demand Factors (NEC 220.55)**
- **First 10,000 VA**: 100% → **10,000 VA**  
- **Remaining 11,600 VA**: 40% → **4,640 VA**  
- **Total after demand factors**: **14,640 VA**  

---

### **Step 5: Convert to Amperes**
- **Service voltage**: 240V  
- **Service load**: 14,640 VA ÷ 240V = **61 A**  

---

### **Conclusion**
- **Calculated service load**: **61 A**  
- **200A panel rating**: **Adequately sized** (61 A << 200 A)  

[OK] Source: CEC 2022 (NEC Article 220)

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 7.9s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Electrical Panel Inspection Violations (CEC 2022)

### 1. **Insufficient Depth Clearance**  
- **Violation**: NEC 110.26(A)(1) requires **36 inches (3 ft)** of depth clearance for working space in front of a 240V panel (Condition 1).  
- **Measured**: 28 inches (<< 36 inches).  
- **Citation**: CEC 2022 Table 110.26(A)(1).  

### 2. **Obstruction in Working Space**  
- **Violation**: NEC 110.26(A)(2) mandates **clear working space** free of obstructions.  
- **Issue**: Water heater located **16 inches left** of the panel intrudes into the required 36-inch depth clearance.  
- **Citation**: CEC 2022 110.26(A)(2).  

### 3. **Height Clearance (Potential Violation)**  
- **Requirement**: NEC 110.26(A)(1) specifies **6.5 feet (78 inches)** of headroom.  
- **Measured**: Panel mounted at **5 feet (60 inches)** height.  
- **Assessment**: If ceiling height is **< 6.5 feet**, this violates the headroom requirement. Confirm ceiling height to verify.  
- **Citation**: CEC 2022 110.26(A)(1).  

---

**Summary of Violations**:  
- Depth clearance insufficient (28" < 36").  
- Obstruction (water heater) in working space.  
- Potential headroom violation (if ceiling < 6.5').  

[OK] Source: CEC 2022

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 15.9s

**Tools Called:** nec_search

**Answer:**

## Circuit Protection Requirements (NEC 2023)

### 1. **Countertop Receptacles (2 x 20A circuits)**
- **Protection**: **Combination AFCI/GFCI breaker**  
- **NEC References**:  
  - **210.8(A)(5)**: GFCI required for all kitchen receptacles.  
  - **210.12(A)**: AFCI required for all branch circuits in dwelling units.  

### 2. **Dishwasher (15A dedicated circuit)**
- **Protection**: **Combination AFCI/GFCI breaker**  
- **NEC References**:  
  - **210.8(A)(5)**: GFCI required for kitchen receptacles.  
  - **210.12(A)**: AFCI required for all branch circuits.  

### 3. **Garbage Disposal (15A dedicated circuit)**
- **Protection**: **Combination AFCI/GFCI breaker**  
- **NEC References**:  
  - **210.8(A)(5)**: GFCI required for kitchen receptacles.  
  - **210.12(A)**: AFCI required for all branch circuits.  

### 4. **Refrigerator (20A dedicated circuit)**
- **Protection**: **Standard AFCI breaker**  
- **NEC References**:  
  - **210.8(A)(5)**: GFCI **not required** for refrigerators (Exception No. 2 in 210.8(A) allows dedicated circuits for specific appliances without GFCI).  
  - **210.12(A)**: AFCI required for all branch circuits.  

---

### Key Notes:
- **GFCI Exceptions**: Refrigerator circuits are exempt from GFCI under **210.8(A) Exception No. 2** if dedicated to a single appliance.  
- **AFCI Requirement**: All branch circuits in dwelling units require AFCI per **210.12(A)**.  
- **Combination AFCI/GFCI Breakers**: Used where both protections are required (e.g., countertop, dishwasher, disposal circuits).  

[OK] Source: NEC 2023

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 20.8s

**Tools Called:** cec_search

**Answer:**

## Subpanel Grounding Violations and Correct Configuration (CEC 2022)

### **Identified Violations**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation**: CEC 250.32(B)(1) requires **separate neutral and ground bars** in subpanels (not service panels). Bonding them creates a parallel path for neutral current, increasing shock hazard.  
   - **Correct**: Neutral and ground bars must be **electrically isolated** in subpanels.

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: CEC 250.121(B) prohibits bonding the neutral to the metal enclosure. This creates unintended grounding paths and risks equipment damage.  
   - **Correct**: Neutral bar should only connect to the **feeder neutral conductor**.

3. **Ground Bar Bonded to Metal Enclosure via Main Bonding Jumper**  
   - **Violation**: CEC 250.32(D)(1) prohibits connecting the grounded (neutral) conductor to the grounding electrode or enclosure in subpanels. The main bonding jumper belongs **only in the main service panel**.  
   - **Correct**: Ground bar connects to the **feeder equipment grounding conductor (EGC)** and **local grounding electrode** (if required).

---

### **Correct Configuration for Detached Garage Subpanel**
1. **Neutral Bar**  
   - Connects **only** to the **feeder neutral conductor** (from main panel).  
   - Must be **electrically isolated** from ground bar and metal enclosure.  

2. **Ground Bar**  
   - Connects to:  
     - **Feeder EGC** (4th wire in 4-wire feeder).  
     - **Local grounding electrode system** (e.g., ground rod) via a **separate grounding electrode conductor** (per CEC 250.50/250.53).  
   - Must be **isolated** from neutral bar and metal enclosure.  

3. **Metal Enclosure**  
   - Bonded **only** to the **ground bar** via the feeder EGC.  
   - No connection to neutral bar.  

4. **Grounding Electrode Requirement**  
   - **Required**: CEC 250.32(A) mandates a grounding electrode system for detached structures unless supplied by a single branch circuit (not the case here).  
   - Use a **minimum 2.5 m (8 ft) ground rod** (CEC 250.52(A)(5)) bonded to the subpanel ground bar.  

---

### **Key Code References**
- **CEC 250.32(B)(1)**: Grounded systems supplied by feeders must have **no connection** between grounded (neutral) conductor and grounding electrode or enclosure.  
- **CEC 250.121(B)**: Structural metal frames cannot serve as equipment grounding conductors.  
- **CEC 250.58**: All grounding electrodes for a structure must be **bonded together** as a single system.  

---

### **Inspector Note**  
The subpanel in a detached structure must function as a **derived system** with independent grounding. Bonding neutrals and grounds creates a shock hazard and violates CEC’s requirement for isolated grounding in subpanels. Always verify the grounding electrode is installed and sized per CEC Table 250.66 (based on feeder conductor size).  

[OK] Source: CEC 2022

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 17.4s

**Tools Called:** lookup_conduit_fill

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (NEC 2023)

**Calculation Steps:**

1. **Conduit Total Area:**  
   From NEC Table 4 (Chapter 9):  
   - 1¼" RMC = **1.526 sq in**

2. **40% Fill Limit (for 3+ conductors):**  
   - 40% of 1.526 = **0.6104 sq in**

3. **Conductor Area per 10 AWG THHN:**  
   From NEC Table 5 (Chapter 9):  
   - 10 AWG THHN = **0.0211 sq in/conductor**

4. **Maximum Conductors:**  
   - 0.6104 ÷ 0.0211 = **28.91** → **28 conductors** (round down)

**Final Answer:**  
A 1¼" RMC can contain **28** 10 AWG THHN conductors at 40% fill.  

**Verification:**  
- Total conductor area: 28 × 0.0211 = 0.5908 sq in  
- Fill percentage: 0.5908 ÷ 1.526 = **38.7%** (≤ 40% allowed)  

[OK] Source: NEC 2023 Chapter 9 Tables 4 and 5

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 26.8s

**Tools Called:** python_calculator, python_calculator, cec_search

**Answer:**

## Voltage Drop Calculation (CEC 2022)

1. **Voltage Drop Formula**:
   $$
   VD = 2 \times I \times R \times \frac{L}{1000}
   $$
   Where:
   - $ I = 22A $
   - $ R = 1.29\ \Omega/1000ft $
   - $ L = 50ft \times 2 = 100ft $ (round trip)

2. **Calculation**:
   $$
   VD = 2 \times 22 \times 1.29 \times \frac{50}{1000} = 2.838\ \text{volts}
   $$
   $$
   \%VD = \left( \frac{2.838}{120} \right) \times 100 = 2.365\%
   $$

3. **Code Compliance**:
   - **CEC 2022 Section 210.19(A)**: Informational Note 3 recommends **≤3%** voltage drop for branch circuits (incorporates NEC 2023).
   - **CEC 2022 Section 647.4(D)**: More restrictive 1.5% for special systems (not applicable here).
   - **Result**: 2.37% ≤ 3% → ✅ **Compliant**

[OK] Source: CEC 2022 (incorporates NEC 2023)

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 13.0s

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG TW copper at 60°C → **20A** (Table 310.16)

**Step 2: Temperature Correction**  
Ambient 43°C → Correction factor = **0.71** (Table 310.15(B)(1)(1))  
20A × 0.71 = **14.2A**

**Step 3: Bundling Adjustment**  
6 conductors → Adjustment factor = **0.8** (Table 310.15(C)(1))  
14.2A × 0.8 = **11.36A**

**Final Adjusted Ampacity**  
**11.36A** (Round down to **11A** for practical application)

**Code References**  
- Base ampacity: Table 310.16  
- Temperature correction: Table 310.15(B)(1)(1)  
- Bundling adjustment: Table 310.15(C)(1)  

[OK] Source: CEC 2022

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 5.1s

**Tools Called:** cec_lookup_grounding_conductor

**Answer:**

## Minimum Size Copper GEC for Parallel Service Conductors (CEC 2022)

**Service Conductor Configuration**:  
4 × 250 kcmil copper conductors per phase = **1000 kcmil equivalent** (per phase)  

**Grounding Electrode Conductor (GEC) Requirement**:  
- **Copper GEC size**: **2/0 AWG**  
- **Aluminum/Copper-Clad Aluminum GEC size**: 4/0 AWG (not required here)  

**Code Reference**:  
CEC 2022 **Table 250.66** with California amendment (Δ) applied.  

**Key Notes**:  
1. The equivalent service conductor size for parallel conductors is calculated by summing the cross-sectional areas (4 × 250 kcmil = 1000 kcmil).  
2. Footnote 1 of Table 250.66 confirms this method for multiple parallel service-entrance conductors.  
3. California amendments may modify NEC requirements, but in this case, the GEC sizing aligns with the national code.  

[OK] Source: CEC 2022

---

