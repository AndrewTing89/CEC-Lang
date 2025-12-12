# Core (NEC) Evaluation Results - Run 34 (Hint Enforcement)

**Date:** 2025-12-11
**Changes:** Hint enforcement + electrode exceptions + 110.26(A)(2) clarification

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 259.4s |
| Avg Duration | 9.6s |
| Reflection Used | 27/27 |
| Reflection Improved | 3/27 |
| Hint Enforcement Triggered | 2/27 |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 9.7s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_exception_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size**: **6 AWG copper**  
- **Ampacity**: 65A (Table 310.16)  
- **Temperature rating**: 75°C  

**Key Notes**:  
1. **8 AWG (50A)** is insufficient for 60A.  
2. **Exceptions** to Table 310.16 exist but apply only to specialized equipment (e.g., hermetic refrigerant compressors, multimotor systems). For general circuits, 6 AWG is correct.  
3. **Limiting rules**:  
   - Verify ambient temperature adjustments (Section 310.15(B)).  
   - Check bundling corrections (Section 310.15(C)(1)).  
   - Confirm overcurrent protection compliance (Section 240.4(D)).  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 6.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**Requirement:**  
All 125-volt through 250-volt receptacles installed in **kitchens to serve countertop surfaces** must have **ground-fault circuit-interrupter (GFCI) protection for personnel** per **CEC 2022 Section 210.8(A)(6)**.

**Key Details:**  
- Applies to **all 15A and 20A receptacles** rated 150 volts or less to ground.  
- Protection must be provided **per 210.8 general requirements** (e.g., readily accessible location).  
- **Exceptions** do not apply to standard countertop receptacles (exceptions cover ceiling luminaires/fans, which are irrelevant here).  

**Code Citation:**  
CEC 2022 Section 210.8(A)(6):  
> *"Kitchens - where the receptacles are installed to serve the countertop surfaces."*

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 6.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Yes**, arc-fault circuit-interrupter (AFCI) protection is required for **all 120-volt, single-phase, 15- and 20-ampere branch circuits** supplying outlets or devices in **bedrooms of dwelling units** per **CEC 2022 Section 210.12(A)**.

### Key Requirements:
- **Applies to**: Bedrooms, living rooms, kitchens, and similar areas in residential construction.
- **Protection Methods**: 
  1. Combination-type AFCI at the panel.
  2. Branch/feeder-type AFCI + outlet branch-circuit AFCI at first outlet.
  3. Supplemental arc protection circuit breaker + outlet AFCI (with conductor length limits).
  4. Outlet branch-circuit AFCI at first outlet (with conductor length limits).
  5. Permitted alternatives for metal raceway or concrete-encased wiring.

### Exceptions:
- **Not required** for fire alarm circuits installed per 760.41(B) or 760.121(B) (if in metal raceway or concrete-encased).

### Inspector Note:
- Verify AFCI type matches the installation method (e.g., combination vs. outlet branch-circuit).
- Mark first outlet boxes as required by 210.12(A)(3)–(6).

[OK] Source: CEC 2022 Section 210.12

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 6.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Answer:**  
Yes, aluminum conductors are permitted for a 200A service.  

**Required Size:**  
- **4/0 AWG aluminum** (per CEC Table 310.12 for single-phase dwelling services).  

**Code References:**  
- **Section 310.3(B):** Aluminum conductors are allowed unless restricted.  
- **Table 310.12:** Specifies 4/0 AWG aluminum for 200A service conductors.  

[OK] Source: CEC 2022

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 13.8s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes

**Answer:**

## Minimum Working Clearance Depth and Dedicated Space (CEC 2022)

### **Working Clearance Depth**
- **Minimum depth**: **3 feet (900 mm)** in front of the panel per **Table 110.26(A)(1)**, Condition 1 (equipment ≤ 600V).  
- **Vertical clearance**: **6.5 feet (78 in)** above the floor where work is performed (110.26(A)(2)).  

---

### **Dedicated Working Space (Section 110.26(B))**
- **Requirement**: The working space must be **dedicated and free from obstructions** (e.g., storage, equipment, or other barriers) to ensure safe operation and maintenance.  
- **Key Provisions**:  
  - The space must remain clear for the full depth of the required working clearance.  
  - No combustible materials or objects shall be stored in this area.  

---

### **Location Restrictions (Section 240.24)**
- **Prohibited locations**:  
  1. **Clothes closets** (240.24(D)).  
  2. **Bathrooms in dwelling units** (240.24(E)).  
  3. **Over steps of a stairway** (240.24(F)).  

---

### **Inspector Note**
- Verify compliance with **all three requirements**:  
  1. **Clearance depth** (3 ft).  
  2. **Vertical clearance** (6.5 ft).  
  3. **Dedicated, obstruction-free space** (110.26(B)).  
- Use `cec_search("110.26(B)")` for additional details on dedicated space requirements.  

[OK] Source: CEC 2022

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Required Small Appliance Branch Circuits for Kitchen (CEC 2022)

**Answer:**  
A minimum of **two 20-ampere small-appliance branch circuits** are required to serve all receptacle outlets in a kitchen, including countertop surfaces, wall outlets, and refrigeration equipment.  

**Code Basis:**  
- **CEC 2022 Section 210.52(B)(1):**  
  *"In the kitchen... the two or more 20-ampere small-appliance branch circuits required by 210.11(C)(1) shall serve... all countertop outlets... and receptacle outlets for refrigeration equipment."*  
- **CEC 2022 Section 210.11(C)(1):**  
  *"Dwelling units shall have... two or more 20-ampere small-appliance branch circuits for all receptacle outlets specified by 210.52(B)."*  

**Key Requirements:**  
1. **Minimum Two Circuits:** At least two 20A circuits must supply kitchen receptacles (no exceptions for reducing this number).  
2. **No Shared Circuits:** Each kitchen must have its own dedicated small-appliance circuits (no sharing between kitchens).  
3. **Load Coverage:** These circuits serve countertop outlets, wall/floor receptacles, and refrigeration equipment.  

**Exceptions (Non-Applicable Here):**  
- Additional circuits are permitted but not required.  
- Specific appliance circuits (e.g., refrigerators) may be excluded from load calculations per **220.52 Exception**.  

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 12.3s | **Iterations:** 4

**Tools Called:** cec_search, cec_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## Revised Answer: Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Surge protection **is required** for a new 200A residential service under **CEC 2022 Section 230.67**. This requirement was not captured in the initial search due to an article filter, but a broader search confirmed the mandate.

### Key Code Requirements:
1. **Section 230.67(A)**:  
   *"All services supplying dwelling units shall be provided with a surge-protective device (SPD)."*  
   - **Type**: Must be Type 1 or Type 2 SPD.  
   - **Location**:  
     - Integral to service equipment, or  
     - Located immediately adjacent to service equipment.  
     - **Exception**: SPD may be installed downstream at the next level of distribution if not in service equipment.  

2. **Section 230.67(D)**:  
   If service equipment is replaced, the SPD requirement must still be applied.  

### Additional Context:
- **Section 230.94** allows SPDs to be installed on the supply side of the service disconnect (e.g., for metering or fire alarm systems), but this does not negate the requirement in 230.67.  
- **Section 230.209** permits surge arresters on overhead service conductors but does not replace the SPD requirement for dwelling units.  

### Inspector Note:
- **California mandates SPDs** for residential services in CEC 2022 (Section 230.67), even if the 2023 NEC may have similar language.  
- Verify local amendments, as some jurisdictions may adopt additional requirements.  

[OK] Source: CEC 2022  

[VERIFIED] Answer is complete.

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 7.5s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Service Conductor Sizing (CEC 2022)

**Required Service Conductor Sizes:**
- **Copper:** 2/0 AWG (per Table 310.12(A))
- **Aluminum:** 4/0 AWG (per Table 310.12(A))

**Key Requirements:**
1. **Applicable Table:** CEC Table 310.12(A) for single-phase dwelling services
2. **Conditions Met:**
   - 120/240V single-phase system
   - Conductors supply entire dwelling load
   - No temperature correction/adjustment factors needed
3. **Material Options:** Both copper and aluminum permitted
4. **California Specifics:** Complies with Title 24 Part 6 energy efficiency requirements

**Inspector Note:** 
- For aluminum conductors, verify termination compatibility with 75°C-rated equipment per 110.14(C)
- Verify service calculations meet demand load requirements in 220.82 (not required here since question specifies 200A service)

[OK] Source: CEC 2022

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 8.5s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Multiwire Branch Circuit Requirements (CEC 2022)

### Circuit Breaker Requirements
1. **Simultaneous Disconnection**  
   - **Requirement**: All ungrounded conductors (hots) must be disconnected simultaneously at the panelboard using a **handle tie** or **common-trip breaker** (Section 210.4(B)).  
   - **Implementation**: Use a **2-pole breaker** or two single-pole breakers with a **listed handle tie** to ensure both hots shut off together.  

2. **AFCI Protection**  
   - **Requirement**: Arc-fault circuit interrupter (AFCI) protection is mandatory for kitchen circuits (Section 210.12(A)).  
   - **Implementation**: Install a **combination-type AFCI breaker** or use an outlet-type AFCI at the first receptacle (per 210.12(A)(1)-(6)).  

---

### Neutral Termination Requirements
1. **Neutral Sizing**  
   - **Requirement**: The neutral conductor must be sized to carry the maximum unbalanced load (Section 210.4(C)).  
   - **Implementation**: For a 12/3 cable (12 AWG neutral), the neutral is adequately sized for typical 20A kitchen circuits.  

2. **Neutral Termination**  
   - **Requirement**: The neutral must terminate at the **neutral busbar** in the panelboard and **not be shared** with other circuits unless specifically permitted (Section 200.4(B)).  
   - **Implementation**: Ensure the neutral is **not shared** with other MWBCs unless all conductors are grouped (per 210.4(D)).  

---

### Key Code Citations
- **Simultaneous Disconnection**: CEC 2022 Section 210.4(B)  
- **AFCI Protection**: CEC 2022 Section 210.12(A)  
- **Neutral Sizing**: CEC 2022 Section 210.4(C)  
- **Neutral Termination**: CEC 2022 Section 200.4(B)  

[OK] Source: CEC 2022

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 7.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (CEC 2022/NEC 2023)

**All 125V–250V receptacles in the following locations require GFCI protection per CEC/NEC 210.8(A):**

1. **Bathrooms**  
2. **Garages and accessory buildings** (floor at or below grade, not habitable)  
3. **Outdoors**  
   - *Exception:* Receptacles for electric snow-melting/deicing (per 426.28/427.22).  
4. **Crawl spaces** (at or below grade).  
5. **Basements**  
   - *Exception:* Receptacles for fire alarm systems (not required).  
6. **Kitchens** (serving countertop surfaces).  
7. **Sinks** (within 6 ft of the bowl’s top inside edge).  
8. **Boathouses**.  
9. **Bathtubs/showers** (within 6 ft of the outside edge).  
10. **Laundry areas**.  
11. **Indoor damp/wet locations**.  

**Additional Notes:**  
- **Exceptions for ceiling luminaires/fans:** Listed locking receptacles for ceiling fixtures don’t require GFCI if the receptacle is integral to the fixture.  
- **Outdoor outlets:** Covered in 210.8(F) (separate from 210.8(A)(3)).  

[OK] Source: CEC 2022/NEC 2023 Section 210.8

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 5.1s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Surge Protection Requirements for Residential Service (CEC 2022)

**Requirement:**  
Surge protection **is required** for all services supplying dwelling units per **CEC 2022 Section 230.67(A)**.

**Installation Location Options:**  
1. **Integral to service equipment** (e.g., main panel)  
2. **Adjacent to service equipment**  
3. **Downstream at next level distribution equipment** (Exception allowed if installed at each subsequent level toward the load)

**SPD Type Requirements:**  
- Must be **Type 1 or Type 2 SPD** (Section 230.67(C))  
- Must comply with **Article 242** (replaces former Articles 280/285) for overvoltage protection  

**Key Notes:**  
- The exception permits non-compliance with the "adjacent to service equipment" rule **only if** SPDs are installed at every downstream distribution level.  
- For replacement service equipment, all SPD requirements still apply (Section 230.67(D)).  

[OK] Source: CEC 2022

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 16.5s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes

**Answer:**

## Final Compliance Determination (CEC 2022)

### 1. **Location Prohibition - 240.24(D)**
- **Rule**: Overcurrent devices **shall not be located in clothes closets** (vicinity of easily ignitible material).
- **Your Case**: Panel installed in a **clothes closet** directly violates this rule.
- **Conclusion**: ❌ **Non-compliant**. No exceptions apply for clothes closet installations.

---

### 2. **Working Space Deficiencies**
- **Front Clearance**: 
  - **Required**: 36 in (900 mm) per Table 110.26(A)(1) for 120V systems.
  - **Your Case**: Only 24 in provided. ❌ **Fails minimum requirement**.
- **Side Clearance**: 
  - **Required**: 30 in depth/width from obstructions (water heater at 18 in is too close).
  - **Your Case**: Water heater violates side clearance. ❌ **Non-compliant**.

---

### 3. **Additional 110.26(B) Considerations**
- **110.26(B) Dedicated Space**: Requires **6.5 ft (78 in)** vertical clearance above the floor in the working space. 
  - Your installation must ensure this vertical space is maintained where a person would stand to work on the panel.
  - **Your Case**: Not explicitly addressed in the query, but must be verified.

---

### 4. **Corrective Actions Required**
1. **Relocate Panel**: Move to a permitted location (not a clothes closet).
2. **Adjust Clearances**:
   - Ensure **36 in front clearance**.
   - Maintain **30 in side clearance** from obstructions like water heaters.
3. **Verify Vertical Space**: Confirm **6.5 ft vertical clearance** per 110.26(B).

---

### Code Citations
- **Location Prohibition**: CEC 240.24(D) ("Clothes closets")
- **Working Space**: CEC 110.26(A)(1) + Table 110.26(A)(1)
- **Vertical Clearance**: CEC 110.26(B)
- **Closet Definition**: CEC 100 ("Clothes closet" as garment storage space)

[OK] Source: CEC 2022

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 9.4s | **Iterations:** 4

**Tools Called:** cec_search, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

[VERIFIED] Answer is complete.  

**Final Answer:**  
Yes, this is a **code violation** under CEC 2022.  

**Key Requirements:**  
1. **Terminal Marking Requirement**  
   - **CEC 2022 Section 110.14(A)** explicitly requires that conductors be connected to terminals in a manner consistent with the terminal's marking. Terminals not marked for multiple conductors (e.g., "2-wire") are limited to one conductor per terminal.  

2. **Breaker Terminal Limitations**  
   - The breaker in question is **not marked for two conductors**, so connecting two 12 AWG conductors violates this rule.  

3. **Relevant Sections**  
   - **CEC 2022 Section 240.91(A)** reinforces conductor protection rules but does not override termination requirements.  

**Exceptions Checked:**  
- No exceptions to **110.14(A)** apply here. Cross-referenced sections (e.g., 215.2, 250.148) address feeder sizing, grounding, or insulation, not terminal markings.  

**Corrective Action:**  
- Use a breaker with a terminal marked for two conductors or install a junction box to combine conductors before termination.  

[OK] Source: CEC 2022

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 9.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### Key Requirements:
1. **Separate Neutral and Ground Buses**  
   - In the subpanel, **neutral and ground must be isolated** (unlike the main panel).  
   - **Neutral bus**: Connects only to the feeder's neutral conductor.  
   - **Ground bus**: Connects to:  
     - Feeder's equipment grounding conductor (EGC).  
     - Local grounding electrode conductor (GEC) to a grounding electrode (e.g., ground rod).  

2. **Grounding Electrode Requirement**  
   - A **separate grounding electrode** (e.g., ground rod) is required at the detached garage per **250.30(A)(4)**.  
   - The grounding electrode conductor (GEC) connects the subpanel’s ground bus to this electrode.  

3. **Feeder Conductors**  
   - **4-wire feeder** includes:  
     - Two ungrounded (hot) conductors.  
     - One grounded (neutral) conductor.  
     - One equipment grounding conductor (EGC).  

4. **Bonding Prohibitions**  
   - **No bonding** of neutral and ground in the subpanel (unlike the main panel).  

5. **Grounding Electrode Conductor Size**  
   - Size the GEC per **Table 250.66** based on the feeder’s ungrounded conductor size.  
     - Example: For a 100A feeder with 3/0 AWG copper ungrounded conductors:  
       - **GEC size**: 4 AWG copper (Table 250.66).  

6. **Equipment Grounding Conductor (EGC)**  
   - Size the EGC per **Table 250.122** based on the overcurrent protection rating.  
     - Example: For a 100A circuit breaker:  
       - **EGC size**: 8 AWG copper (Table 250.122).  

---

### Configuration Summary:
- **Neutral Bus**:  
  - Connected to feeder’s neutral conductor.  
  - **No connection to ground bus**.  

- **Ground Bus**:  
  - Connected to:  
    - Feeder’s EGC.  
    - Local grounding electrode (e.g., ground rod) via GEC.  

- **Grounding Electrode**:  
  - Minimum 2.5 m (8 ft) driven ground rod or equivalent.  

---

### Inspector Notes:
- **Verify isolation** between neutral and ground buses in the subpanel.  
- Ensure the **grounding electrode is installed** at the detached structure.  
- Confirm conductor sizes match **Table 250.66** (GEC) and **Table 250.122** (EGC).  

[OK] Source: CEC 2022 Sections 250.30, 250.66, 250.122

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 9.0s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Main Bonding Jumper**
- **Purpose**: Connects the grounded conductor (neutral) to the equipment grounding conductors **at the service disconnecting means** in a **service installation**.
- **Required by**: 
  - **250.24(B)**: For grounded systems, an unspliced main bonding jumper must connect the grounded conductor to the service disconnecting means enclosure.
  - **250.28(D)**: Sizing based on Table 250.102(C)(1) using the largest ungrounded service conductor.
- **Application**: Used **only at the service** to ensure the grounded conductor and equipment grounding system are bonded at the service point.
- **Example**: In a residential service panel, the main bonding jumper connects the neutral bus to the panel’s metal enclosure.

---

### **System Bonding Jumper**
- **Purpose**: Connects the grounded conductor (neutral) to the equipment grounding conductors **at the source of a separately derived system** (e.g., transformers, generators).
- **Required by**:
  - **250.30(A)(1)**: For separately derived systems, an unspliced system bonding jumper must connect the grounded conductor to the equipment grounding system at the source or first disconnecting means.
  - **250.28(D)**: Sizing also based on Table 250.102(C)(1) using the largest ungrounded conductor of the separately derived system.
- **Application**: Used **at separately derived systems** to ensure the system is properly grounded and bonded independently of the service.
- **Example**: On a 480V to 208V transformer, the system bonding jumper connects the neutral of the secondary winding to the transformer’s metal enclosure.

---

### **Key Differences**
| Feature                  | Main Bonding Jumper                     | System Bonding Jumper                     |
|--------------------------|----------------------------------------|------------------------------------------|
| **Location**             | Service disconnecting means            | Source of separately derived system       |
| **System Type**          | Service-supplied systems               | Separately derived systems                |
| **Code Reference**       | 250.24(B), 250.28(D)                   | 250.30(A)(1), 250.28(D)                   |
| **Sizing Table**         | Table 250.102(C)(1)                    | Table 250.102(C)(1)                       |
| **Purpose**              | Bonds service neutral to equipment grounding | Bonds separately derived system neutral to equipment grounding |

---

### **When Each is Required**
- **Main Bonding Jumper**: Required **at every service disconnecting means** for grounded systems (250.24(B)).
- **System Bonding Jumper**: Required **at the source of every separately derived system** (250.30(A)(1)).

[OK] Source: CEC 2022

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 9.6s | **Iterations:** 4

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Small Appliance Branch Circuit Requirements (CEC 2022)

**1. Required Number of Circuits:**
- **Minimum Requirement**: At least **two 20-ampere small-appliance branch circuits** are required for kitchens in dwelling units (CEC 2022 Section 210.11(C)(1)).  
- **Purpose**: These circuits must supply **all wall and floor receptacles**, **countertop outlets**, and **refrigeration equipment** in the kitchen (CEC 2022 Section 210.52(B)(1)).

**2. Serving Dining Room Receptacles:**
- **Permitted**: Yes, the small-appliance branch circuits **can also serve receptacles in the dining room**.  
- **Code Basis**: Section 210.52(B)(3) explicitly allows these circuits to supply receptacles in the kitchen and "other rooms specified in 210.52(B)(1)" (which includes dining rooms).  
- **Limitation**: A small-appliance circuit **shall not serve more than one kitchen**, but it may serve multiple rooms (e.g., kitchen + dining room).

**3. Key Exceptions:**
- **Exception No. 1**: A receptacle for a specific appliance (e.g., refrigerator) may be on an individual branch circuit (15A or higher) (CEC 2022 Section 210.52(B)(1), Exception No. 2).  
- **Exception No. 2**: Receptacles for gas-fired ranges/ovens may be added to small-appliance circuits (CEC 2022 Section 210.52(B)(1), Exception No. 2).

**Inspector Note**: Ensure the circuits are **dedicated to small-appliance loads** and not overloaded with non-small-appliance outlets (e.g., lighting or laundry).  

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 8.3s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator, cec_exception_search, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   12 AWG THHN copper at 90°C = **30A** (Table 310.16)

2. **Temperature Correction**:  
   50°C ambient → **0.82** correction factor (Table 310.15(B)(1)(1))

3. **Bundling Adjustment**:  
   6 conductors → **0.80** adjustment factor (Table 310.15(C)(1))

4. **Final Calculation**:  
   $$
   30A \times 0.82 \times 0.80 = 19.68A \approx \mathbf{19.7A}
   $$

**Final Adjusted Ampacity**: **19.7A**  
**Maximum Overcurrent Protection**: **20A** (per 240.4(D) for 12 AWG copper)

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 7.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## AFCI Protection Requirements in Bedrooms and Living Areas (CEC 2022)

### **Why AFCI Protection is Required**
The NEC (and CEC 2022) mandates **Arc-Fault Circuit Interrupter (AFCI)** protection for 15- and 20-ampere branch circuits in dwelling unit bedrooms, living rooms, and similar areas **to prevent electrical fires caused by arc faults**. This requirement is explicitly stated in **Section 210.12(A)**, which lists these spaces as mandatory for AFCI coverage.

---

### **What Hazard Does AFCI Prevent?**
AFCIs are designed to detect and interrupt **series arcs** (e.g., from damaged cords, loose connections, or deteriorating wiring) that can ignite surrounding materials. Key points from the code:
- **Arc faults** generate high heat (up to 10,000°F) and can start fires in walls, ceilings, or furniture.
- Standard circuit breakers do not reliably detect arcs; AFCIs use advanced electronics to recognize arc signatures.
- **Section 100** defines AFCIs as devices that "function to de-energize the circuit when an arc fault is detected."

---

### **Code Basis**
- **CEC 2022 Section 210.12(A):** Requires AFCI protection for all 120V, 15/20A circuits in dwelling unit areas including:
  - Bedrooms
  - Living rooms
  - Hallways
  - Closets
  - Laundry areas
- **Exceptions:** None apply to typical residential scenarios (e.g., fire alarm systems are excluded but not relevant here).

---

### **Inspector Note**
- AFCI protection is **not interchangeable with GFCI** (which prevents shocks). Both may be required in the same location (e.g., kitchen outlets need both AFCI and GFCI).
- Verify AFCI coverage during inspections by checking the panel for labeled AFCI breakers or outlet-mounted AFCIs.

[OK] Source: CEC 2022

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 5.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

Torque specifications are critical for ensuring **secure, low-resistance electrical connections** in panels and equipment terminations. Improper torque can lead to:
- Loose connections causing arcing and overheating
- Over-tightening damaging terminal components
- Connection failures due to vibration or thermal expansion

### Key Requirements:
1. **General Torque Requirements**  
   - **Section 110.14(D)** mandates tightening torque values must match equipment markings or manufacturer instructions.  
   - Approved methods include torque tools, shear bolts, or breakaway devices with visual indicators.  
   - *Informational Note 2*: Contact the equipment manufacturer if torque values are not provided.  

2. **Control Circuit Devices**  
   - **Section 430.9(C)** requires screw-type terminals for 14 AWG or smaller copper conductors to be torqued to **minimum 0.8 N·m (7 lb-in.)** unless otherwise identified.  

3. **Temperature Coordination**  
   - Section 110.14(C) requires conductor ampacity to align with termination temperature ratings (e.g., 60°C or 75°C), which indirectly affects torque requirements by dictating proper conductor selection.  

### Inspector Note:
Always verify torque values directly on equipment or in manufacturer documentation. Use calibrated torque tools for compliance, especially in high-vibration or high-temperature environments.  

[OK] Source: CEC 2022 Sections 110.14(D), 430.9(C)

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 21.8s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Service Load Calculation (CEC 2022)

### Step 1: Calculate Individual Loads
1. **Electric Range (12kW):**  
   - Demand factor per **CEC Table 220.55 Column C** (single range): **8,000 W**  
   - Source: CEC 220.55, Note 1 (no adjustment for 12 kW rating)  

2. **Dryer (5.5kW):**  
   - Nameplate rating used per **CEC 220.54**  
   - Load: **5,500 W**  
   - Source: CEC 220.54  

3. **Small Appliance Circuits (2 × 20A):**  
   - 1,500 VA per circuit per **CEC 220.52(B)**  
   - Load: **2 × 1,500 = 3,000 VA**  
   - Source: CEC 220.52(B)  

4. **Laundry Circuit (20A):**  
   - 1,500 VA per **CEC 220.52(C)**  
   - Load: **1,500 VA**  
   - Source: CEC 220.52(C)  

5. **General Lighting (3,000 sq ft):**  
   - 3 VA/sq ft per **CEC 220.12(A)**  
   - Load: **3,000 × 3 = 9,000 VA**  
   - Source: CEC 220.12(A)  

6. **Central AC (4600W):**  
   - Continuous load: **4,600 W × 1.25 = 5,750 W** per **CEC 220.18(A)**  
   - Source: CEC 220.18  

---

### Step 2: Total Service Load Calculation
$$
\begin{align*}
\text{Total Load} &= 8,000 \, (\text{Range}) + 5,500 \, (\text{Dryer}) + 3,000 \, (\text{Small Appliance}) \\
&\quad + 1,500 \, (\text{Laundry}) + 9,000 \, (\text{Lighting}) + 5,750 \, (\text{AC}) \\
&= 32,750 \, \text{VA}
\end{align*}
$$

---

### Step 3: Convert to Amperes
$$
\text{Service Load (A)} = \frac{32,750 \, \text{VA}}{240 \, \text{V}} = 136.46 \, \text{A}
$$

---

### Step 4: Verify Panel Adequacy
- **Calculated Load:** 136.46 A  
- **Panel Rating:** 200 A  
- **Conclusion:** 200 A panel exceeds the calculated load (136.46 A) and complies with **CEC 220.85** (service size must be ≥ calculated load).  

[OK] Source: CEC 2022

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 11.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Electrical Panel Inspection Violations (CEC 2022)

### 1. **Insufficient Working Space Depth**
- **Violation**: 28-inch depth clearance is **less than the required 36 inches (3 ft)** for panels operating at ≤150V (Table 110.26(A)(1), Condition 1/2/3).
- **Code Reference**: CEC 2022 Section 110.26(A)(1) and Table 110.26(A)(1).

### 2. **Water Heater Intrusion into Dedicated Electrical Space**
- **Violation**: The water heater is located **within the dedicated electrical space** (16 inches from the panel), violating the requirement for clear, unobstructed working space.
- **Code Reference**: CEC 2022 Section 110.26(E)(1)(a) prohibits foreign systems (e.g., water heater piping) in the dedicated space (width × depth × height of the panel + 6 ft vertically).

### 3. **Working Space Height Deficiency**
- **Violation**: The panel is mounted at **5 feet height**, but the working space must extend **from the floor to 6.5 feet (2.0 m)** or the height of the equipment, whichever is greater. If the panel’s height exceeds 6.5 feet, the working space is insufficient.
- **Code Reference**: CEC 2022 Section 110.26(A)(3).

### 4. **Surface-Mounted Panel Location**
- **Violation**: Surface-mounted panels must ensure the working space is **clear of obstructions**. The water heater’s proximity violates this requirement.
- **Code Reference**: CEC 2022 Section 110.26(E)(1)(a) and 110.26(A).

---

### Summary of Violations:
1. **Depth clearance < 36 inches** (Table 110.26(A)(1)).
2. **Foreign equipment (water heater) in dedicated space** (Section 110.26(E)(1)(a)).
3. **Working space height < 6.5 feet** (Section 110.26(A)(3)).

---

### Inspector Notes:
- **Depth Fix**: Increase clearance to **36 inches** (3 ft) in front of the panel.
- **Water Heater Fix**: Relocate the water heater **at least 36 inches away** from the panel or install a physical barrier.
- **Height Fix**: Ensure the working space extends **6.5 feet vertically** from the floor, or adjust panel height if necessary.

[OK] Source: CEC 2022

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 13.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Circuit Protection Requirements for New Residential Kitchen (NEC 2023)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **Combination AFCI/GFCI**
- **NEC References**:
  - **210.8(A)(6)**: GFCI protection required for all kitchen countertop receptacles.
  - **210.12(A)**: AFCI protection required for all 120V, 15A/20A branch circuits in dwelling units.

### 2. **Dishwasher (Dedicated 15A Circuit)**
- **Protection Required**: **Combination AFCI/GFCI**
- **NEC References**:
  - **210.8(A)(6)**: GFCI protection required for receptacles in kitchens (appliances like dishwashers).
  - **210.12(A)**: AFCI protection required for all 120V, 15A/20A branch circuits.

### 3. **Garbage Disposal (Dedicated 15A Circuit)**
- **Protection Required**: **Combination AFCI/GFCI**
- **NEC References**:
  - **210.8(A)(6)**: GFCI protection required for receptacles in kitchens (appliances like garbage disposals).
  - **210.12(A)**: AFCI protection required for all 120V, 15A/20A branch circuits.

### 4. **Refrigerator (Dedicated 20A Circuit)**
- **Protection Required**: **AFCI Only**
- **NEC References**:
  - **210.12(A)**: AFCI protection required for all 120V, 15A/20A branch circuits.
  - **422.5(A)**: Refrigerators are not listed in 422.5(A), so GFCI is **not required** (exception for appliances not covered by 422.5(A)).

---

### Key Notes:
- **Combination AFCI/GFCI Breakers** are required for circuits needing both protections (countertop, dishwasher, disposal).
- **AFCI Only** is sufficient for the refrigerator circuit due to the absence of GFCI requirements under 422.5(A).
- **Exceptions**: Refrigerators are not explicitly listed in 422.5(A), so GFCI is not mandated. This aligns with industry practice to avoid food spoilage risks from unintended GFCI trips.

[OK] Source: NEC 2023

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 7.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Subpanel Grounding Violations and Correct Configuration (CEC 2022)

### **Identified Violations**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation**: Section 250.32(B)(1) requires the *equipment grounding conductor* to connect to the grounding electrode system but **not** to the neutral. Bonding neutral and ground bars in a subpanel creates a parallel ground path and violates the "separately derived system" grounding rules.  
   - **Correct Action**: Isolate the neutral and ground bars in the subpanel. The neutral bar should only connect to the feeder neutral conductor, and the ground bar should only connect to the equipment grounding conductor and grounding electrode.

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: Section 250.32(B)(1) prohibits connecting the neutral to the metal enclosure in a subpanel. This creates a direct bond between neutral and ground, which is only permitted at the **main service panel** (Section 250.24(B)).  
   - **Correct Action**: Remove the bonding jumper between the neutral bar and the metal enclosure. The neutral bar must remain electrically isolated from the enclosure in a subpanel.

3. **Missing Grounding Electrode at Detached Structure**  
   - **Violation**: Section 250.32(A) mandates a **separate grounding electrode** (e.g., ground rod) at the detached garage unless the subpanel is supplied by a single branch circuit (not the case here).  
   - **Correct Action**: Install a grounding electrode (e.g., 8 ft copper rod) at the detached garage. Connect it to the ground bar via a grounding electrode conductor sized per Table 250.66 (based on feeder conductor size).

---

### **Correct Configuration**
1. **Feeder Conductors**  
   - **Hot/Neutral**: #2 AWG aluminum (2 hots, 1 neutral) connected to the neutral bar.  
   - **Ground**: #2 AWG aluminum (equipment grounding conductor) connected to the ground bar.  

2. **Panel Bonding**  
   - **Ground Bar**: Bonded to the metal enclosure (per 250.142(B)).  
   - **Neutral Bar**: Isolated from the ground bar and enclosure.  

3. **Grounding Electrode System**  
   - Install a grounding electrode (e.g., ground rod) at the detached garage.  
   - Connect the electrode to the ground bar using a grounding electrode conductor sized per Table 250.66 (for #2 AWG aluminum feeder, use **#6 AWG copper** or **#4 AWG aluminum**).  

4. **Bonding Jumper**  
   - Remove any bonding jumper between neutral and ground bars.  

---

### **Key Code References**
- **250.32(B)(1)**: Requires equipment grounding conductor to connect to grounding electrode but **not** to neutral in subpanels.  
- **250.24(B)**: Neutral-to-ground bond is only permitted at the **main service panel**.  
- **250.50**: Mandates grounding electrode installation at detached structures.  
- **250.66**: Grounding electrode conductor sizing based on largest ungrounded feeder conductor.  

[OK] Source: CEC 2022

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 13.3s | **Iterations:** 3

**Tools Called:** cec_lookup_conduit_fill

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Calculation Steps:**

1. **Conduit Total Area**  
   From Chapter 9 Table 4:  
   RMC 1¼" = **1.526 in²**

2. **Allowable Fill (40%)**  
   40% of 1.526 in² = **0.6104 in²**  
   (Per NEC 300.15(B)(2)(a) for 3–24 conductors)

3. **Conductor Area**  
   From Chapter 9 Table 5:  
   10 AWG THHN = **0.0211 in²/conductor**

4. **Maximum Conductors**  
   0.6104 in² ÷ 0.0211 in²/conductor ≈ **28.91**  
   → **28 conductors** (round down to nearest whole number)

**Final Answer:**  
**28 conductors** can be installed in 1¼" RMC at 40% fill.  

[OK] Source: CEC 2022 Chapter 9 Tables 4 and 5

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 12.8s | **Iterations:** 6

**Tools Called:** python_calculator, python_calculator, cec_search

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Voltage Drop Verification (CEC 2022)

1. **Voltage Drop Calculation**:
   - **Formula**: $ VD = \frac{2 \times I \times R \times L}{1000} $
   - **Values**:
     - $ I = 22 \, \text{A} $
     - $ R = 1.29 \, \Omega/\text{1000ft} $
     - $ L = 50 \, \text{ft} $
   - **Result**: $ VD = \frac{2 \times 22 \times 1.29 \times 50}{1000} = 2.84 \, \text{V} $

2. **Percentage Drop**:
   - $ \text{Percentage} = \left( \frac{2.84}{120} \right) \times 100 = 2.37\% $

3. **Code Compliance**:
   - **CEC 2022 Section 210.19(A)**:  
     Informational Note 3 recommends **≤3% voltage drop** for branch circuits to ensure efficient operation.  
     - **Actual**: 2.37% ✅ **Meets requirement**

4. **Additional Considerations**:
   - **Section 647.4(D)** applies stricter limits (1.5% for fixed equipment), but this is a general branch circuit, not fixed equipment or cord-connected loads.  
   - **No conflicts** with other sections (e.g., 250.122 for grounding).

**Final Answer**:  
The voltage drop is **2.84 volts (2.37%)**, which complies with the CEC 2022 recommendation of ≤3% for branch circuits.

[OK] Source: CEC 2022

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 8.1s | **Iterations:** 5

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG TW copper at 60°C = **20A** (Table 310.16)

**Step 2: Temperature Correction**  
Ambient 43°C → 60°C conductors = **×0.71** (Table 310.15(B)(1)(1))  
20A × 0.71 = **14.2A**

**Step 3: Bundling Adjustment**  
6 current-carrying conductors = **×0.80** (Table 310.15(C)(1))  
14.2A × 0.80 = **11.36A**

**Final Adjusted Ampacity**  
**11.36 amperes** after applying both correction factors

**Code References**  
- Base ampacity: Table 310.16  
- Temperature correction: Table 310.15(B)(1)(1)  
- Bundling adjustment: Table 310.15(C)(1)  

[OK] Source: CEC 2022

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 4.9s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No

**Answer:**

## Minimum Size Copper GEC for 1000 kcmil Service (CEC 2022)

**Answer:**  
The minimum size **copper grounding electrode conductor (GEC)** required is **2/0 AWG**.

---

**Calculation Steps:**  
1. **Equivalent Service Conductor Size**  
   Four parallel 250 kcmil conductors per phase:  
   $ 4 \times 250\ \text{kcmil} = 1000\ \text{kcmil} $  
   (Per NEC/CEC Table 250.66, Footnote [1]: Sum areas for parallel conductors.)

2. **Table 250.66 Lookup**  
   For **1000 kcmil copper service conductors**, Table 250.66 specifies:  
   - **Copper GEC**: **2/0 AWG**  
   - **Aluminum/Copper-Clad GEC**: **4/0 AWG**  

3. **Exceptions**  
   If the grounding electrode is:  
   - **Ground rod, pipe, or plate**: GEC may be reduced to **6 AWG copper** (250.66(A)).  
   - **Concrete-encased electrode**: GEC may be reduced to **4 AWG copper** (250.66(B)).  
   *(Not applicable unless electrode type is specified.)*

---

**Code References:**  
- CEC 2022 **Table 250.66** (Grounding Electrode Conductor Sizes)  
- CEC 2022 **250.66(A)** and **250.66(B)** (Electrode Type Exceptions)  

[OK] Source: CEC 2022

---

