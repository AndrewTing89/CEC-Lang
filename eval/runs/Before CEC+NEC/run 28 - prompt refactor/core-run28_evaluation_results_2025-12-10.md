# Core (NEC) Evaluation Results - Run 28 (Prompt Refactor)

**Date:** 2025-12-10
**Changes:** Prompt refactoring

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 190.8s |
| Avg Duration | 7.1s |
| Exception Search Used | 0/27 |
| NEC Comparison Used | 1/27 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 5.4s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 9.3s

**Tools Called:** cec_search

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**Answer:**  
In residential kitchens, **GFCI protection is required for all 125-volt through 250-volt receptacles installed to serve countertop surfaces** (CEC 2022 **Section 210.8(A)(6)**). This includes receptacles located on or near countertops used for small appliances, cooking, or food preparation.

### Key Details:
1. **Scope**: Applies to dwelling units (residential kitchens).
2. **Exceptions**:  
   - Receptacles for ceiling luminaires or ceiling fans are exempt if they use listed locking support systems (see **Exception to 210.8(A)(10)**).
   - Receptacles integral to a ceiling fan or luminaire still require GFCI protection if they serve general-purpose convenience outlets.
3. **Additional Context**:  
   - Kitchens must also comply with **Section 210.52(B)(1)** for small-appliance branch circuits, which requires two or more 20-amp circuits for countertop and small appliance outlets. These circuits must include GFCI protection per 210.8(A)(6).

### Inspector Note:
- Verify that all countertop receptacles (including those under or beside the counter) are GFCI-protected.
- Ensure GFCI protection covers both 15- and 20-amp receptacles serving countertops.

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 5.6s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction per **CEC 2022 Section 210.12(A)**.  

### Requirements:
- **Scope**: All 120V, single-phase, 15- and 20-ampere branch circuits supplying outlets in dwelling unit bedrooms must have AFCI protection.
- **Compliance Methods**:  
  1. **Combination-type AFCI** at the origin of the branch circuit (e.g., at the panel).  
  2. **Branch/feeder-type AFCI** at the panel combined with an outlet branch-circuit-type AFCI at the first outlet.  
  3. **Supplemental arc protection circuit breaker** with outlet AFCI under specific conditions (e.g., conductor length limits).  
  4. **Outlet branch-circuit-type AFCI** at the first outlet if the circuit wiring is in metal raceway or concrete-encased.  

### Exceptions (Not Applicable to Bedrooms):
- Fire alarm circuits (exempt but not relevant to general bedroom circuits).  

### Inspector Note:
- Verify AFCI protection is installed per the listed methods in **210.12(A)(1)-(6)**.  
- Ensure the first outlet in the circuit is marked if using split-protection methods (e.g., outlet AFCI).  

[OK] Source: CEC 2022 Section 210.12

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 5.1s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 3.9s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 5.2s

**Tools Called:** cec_search

**Answer:**

## Required Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Answer:**  
A minimum of **two 20-ampere small appliance branch circuits** are required for a kitchen in California, as mandated by **CEC 2022 Section 210.11(C)(1)** (adopted from NEC without amendment).

---

### Code Basis:
1. **CEC 2022 Section 210.11(C)(1)**  
   - *"In addition to the required branch circuits, the following branch circuits shall be provided in every dwelling unit:  
     **(C)(1) Small-Appliance Branch Circuits.** At least two 20-ampere small-appliance branch circuits shall be provided for the following:  
     - Countertop outlets in kitchens  
     - Outlets in pantries  
     - Outlets in breakfast bars."*  

2. **Load Calculation Reference (CEC 220.52(A))**  
   - While the load calculation for service/feeder sizing is 1500 VA per circuit (as shown in search results), the **minimum number of circuits** is explicitly defined in **210.11(C)(1)**.  

---

### Inspector Note:
- California has **no amendments** to this requirement from the NEC.  
- The two circuits must be **dedicated to small appliances** (e.g., toasters, blenders) and **not shared** with other circuits.  
- **Exceptions**: None apply for the minimum number of circuits, though additional circuits may be added for convenience.  

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 5.8s

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for Residential Service (NEC 2023)

**Answer:**  
Yes, surge protection is **required** for a new 200A residential service under the 2023 NEC.  

**Code Basis:**  
- **NEC 230.67(A)** explicitly mandates surge-protective devices (SPDs) for **all services supplying dwelling units** (residential homes).  
- This requirement applies directly to the service entrance, not just feeders or branch circuits.  

**Key Details:**  
- **SPD Type:** Must be a Type 1 or Type 2 SPD (per 230.67(C)).  
- **Nominal Discharge Current Rating:** Minimum 10kA (per 230.67(E)).  
- **Installation Location:** The SPD must be installed **in or adjacent to the distribution equipment** connected to the load side of the service disconnect (per 230.67(B)).  

**Inspector Note:**  
- Verify the SPD is listed and labeled in accordance with UL 1449 (Standard for Surge Protective Devices).  
- Ensure the SPD is properly grounded per NEC 250.94 and 250.96.  

[OK] Source: NEC 2023

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 13.3s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 8.9s

**Tools Called:** nec_search

**Answer:**

## NEC Requirements for Multiwire Branch Circuit Breaker and Neutral Termination

### Circuit Breaker Requirements
1. **Simultaneous Disconnection** (NEC 210.4(B)):
   - A **2-pole circuit breaker** must be used to disconnect **all ungrounded (hot) conductors** simultaneously at the panel.
   - **Prohibited**: Using two single-pole breakers without a handle tie (could leave one hot conductor energized while the other is off).

2. **Overcurrent Rating**:
   - For **12 AWG copper conductors**, the maximum overcurrent protection is **20A** (NEC 240.4(D)(3)).

### Neutral Conductor Requirements
1. **Sizing**:
   - The **neutral conductor must be 12 AWG** (same size as the ungrounded conductors) to handle potential unbalanced loads.
   - In multiwire circuits, the neutral carries the **vector difference** of the two hot conductors' currents. If loads are balanced, neutral current cancels out, but the conductor must still be sized for 100% of the circuit rating.

2. **Termination**:
   - The neutral must terminate on the **neutral (grounded) bus bar** in the panel.
   - **No switching allowed**: The neutral is the return path and must remain continuous (NEC 210.4(D)).

3. **Grouping** (NEC 200.4(B)):
   - All conductors of the multiwire circuit (hots and neutral) must be **grouped together** (e.g., in the same 12/3 cable) to prevent accidental disconnection of only one hot conductor.

### Additional Notes
- **Line-to-Neutral Loads Only** (NEC 210.4(C)): This circuit must supply only 120V loads (standard for kitchen receptacles).
- **Harmonic Currents**: While not a concern for typical kitchen receptacles, neutrals in multiwire circuits feeding nonlinear loads (e.g., electronics) must be sized for potential harmonic currents (NEC 310.15(B)(5)(a)).

[OK] Source: NEC 2023

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 6.1s

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

According to **NEC 2023 Section 210.8(A)**, GFCI protection is required for all 120-volt, 15- and 20-ampere receptacles in the following locations within dwelling units:

1. **Bathrooms**  
2. **Garages and accessory buildings** (floor at or below grade, non-habitable)  
3. **Outdoors**  
4. **Crawl spaces** (at or below grade level)  
5. **Kitchens**  
6. **Areas with sinks and food preparation** (e.g., islands, peninsulas)  
7. **Within 6 ft of sinks** (top inside edge of the bowl)  
8. **Bathtubs and shower stalls** (within 6 ft of the outside edge)  
9. **Laundry areas**  
10. **Indoor damp/wet locations**  

**Exceptions** apply for specific equipment (e.g., HVAC, security systems) and dedicated circuits for snow-melting/deicing (see 210.8(A) Ex. 1–4).  

[OK] Source: NEC 2023 Section 210.8(A)

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 5.1s

**Tools Called:** cec_search

**Answer:**

## Surge Protection for Residential Service (CEC 2022)

**Requirement:**  
Surge protection is **required** for all services supplying dwelling units per **CEC 2022 Section 230.67(A)**.  

**Installation Locations:**  
1. **Integral to service equipment** or **immediately adjacent** to it (Section 230.67(B)).  
2. **Exception:** If not integrated into service equipment, it may be installed at the **next level of distribution equipment downstream** toward the load (e.g., a subpanel).  

**SPD Type Requirements:**  
- Must be **Type 1** (line-to-ground protection at the service entrance) or **Type 2** (branch panel protection) per **Section 230.67(C)**.  

**Key Notes:**  
- **Type 1 SPDs** are installed on the **supply side** of the service disconnect (per CEC 230.82(4)).  
- **Type 2 SPDs** are installed on the **load side** of the service disconnect (e.g., in the main panel).  
- Replacement of service equipment requires surge protection to comply with these rules (Section 230.67(D)).  

[OK] Source: CEC 2022

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 6.0s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 5.0s

**Tools Called:** cec_search

**Answer:**

## Code Violation for Multiple Conductors on a Single Terminal (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under **CEC 2022 Section 110.14(A)**.  

**Key Requirements:**  
- Terminals designed to connect **more than one conductor** must be **explicitly identified** for this purpose.  
- The breaker terminal in question is **not marked/approved** for two conductors, violating the requirement that "terminals for more than one conductor... shall be so identified."  

**Code Citation:**  
> **CEC 2022 Section 110.14(A):**  
> *"Terminals for more than one conductor and terminals used to connect aluminum shall be so identified."*  

**Inspector Action:**  
- **Corrective measure:** Use a breaker terminal listed for multiple conductors, or install a **junction box** with a pigtail connection to a single conductor landed on the breaker.  
- **Penalty:** This violates a **mandatory rule** (not an exception), requiring immediate correction.  

[OK] Source: CEC 2022

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 7.1s

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

### Configuration Requirements:
1. **Separate Neutral and Ground Buses**  
   - In the subpanel, **neutral and ground must be isolated** (not bonded).  
   - **Neutral conductor** from the feeder connects to the **neutral bus**.  
   - **Equipment grounding conductor (EGC)** from the feeder connects to the **grounding bus**.  

2. **No Local Grounding Electrode**  
   - A **grounding electrode (e.g., rod, plate)** is **not required** at the detached garage subpanel.  
   - Grounding is provided via the **equipment grounding conductor** in the 4-wire feeder back to the main service.  

3. **Bonding of Metal Parts**  
   - All non-current-carrying metal parts of the subpanel must be **bonded to the grounding bus** (per **250.4(B)(2)**).  

4. **Main Bonding Jumper**  
   - The **main bonding jumper** (connecting neutral and ground) exists **only at the main service**. In the subpanel, neutral and ground remain separate to avoid parallel paths.  

5. **Feeder Grounding Conductor**  
   - The **EGC in the feeder** must be sized per **Table 250.122** based on the overcurrent protection at the subpanel.  

---

### Key Code References:
- **250.24(A)(5)**: Prohibits reconnecting grounded conductors to ground on the load side of the service disconnect (subpanel must not have a local grounding electrode).  
- **250.4(B)(2)**: Requires bonding of non-current-carrying metal parts to establish an effective ground-fault current path.  
- **250.30(B)**: Applies to separately derived systems (not directly applicable here but reinforces grounding principles).  

---

### Inspector Note:
- Verify the **4-wire feeder** includes a **dedicated equipment grounding conductor** (not shared with neutral).  
- Confirm the subpanel is **not bonded to a local grounding electrode** (e.g., no ground rod at the garage).  
- Ensure **neutral and ground buses are isolated** in the subpanel.  

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 5.5s

**Tools Called:** cec_search

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
1. **Main Bonding Jumper**  
   - **Definition**: The connection between the *grounded circuit conductor* (neutral) and the *equipment grounding conductor* at the **service**.  
   - **Required Location**: Installed at the **service equipment** (e.g., main electrical panel).  
   - **Purpose**: Ensures the neutral and equipment grounding system are bonded at the service point.  

2. **System Bonding Jumper**  
   - **Definition**: The connection between the *grounded conductor* and the *supply-side bonding jumper* or *equipment grounding conductor* at a **separately derived system** (e.g., transformers, generators).  
   - **Required Location**: Installed at the **source of a separately derived system** (e.g., secondary side of a transformer).  
   - **Purpose**: Bonds the grounded conductor to the equipment grounding system at the derived system.  

---

### **Key Differences**
| Feature                  | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|--------------------------|--------------------------------------------------|--------------------------------------------------|
| **Application**          | At the **service** (main electrical panel).      | At **separately derived systems** (e.g., transformers, generators). |
| **Connection Points**    | Grounded conductor (neutral) to equipment grounding conductor. | Grounded conductor to supply-side bonding jumper or equipment grounding conductor. |
| **Code Reference**       | CEC 250.28(D), Table 250.102(C)(1)               | CEC 250.28(D), Table 250.102(C)(1)               |

---

### **Sizing Requirements**
Both jumpers are sized per **Table 250.102(C)(1)** based on the largest ungrounded conductor:  
- **Copper**: Minimum size equals the largest ungrounded conductor (up to 1100 kcmil).  
- **Aluminum**: Minimum size equals the largest ungrounded conductor (up to 1750 kcmil).  
- For larger conductors, sizing follows a 12.5% rule (see Table notes).  

**Example**:  
- For a 400 kcmil copper service conductor, the main bonding jumper must be **400 kcmil copper**.  

---

### **When Each is Required**
1. **Main Bonding Jumper**  
   - **Required**: At every service disconnecting means (250.28).  
   - **Exception**: Not required if the service is supplied via a system where the grounded conductor is bonded at the source (e.g., utility transformer).  

2. **System Bonding Jumper**  
   - **Required**: At the **first point of connection** for all separately derived systems (250.28).  
   - **Examples**:  
     - Secondary side of a transformer.  
     - Output of a generator or photovoltaic system.  

---

### **Inspector Note**
- **Main bonding jumper** ensures the service neutral and equipment grounding system are bonded.  
- **System bonding jumper** ensures the derived system’s grounded conductor is bonded to its equipment grounding system.  
- Both must be made of **copper, aluminum, or corrosion-resistant materials** (250.28(A)).  

[OK] Source: CEC 2022 Sections 100, 250.28, 250.102

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 5.2s

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

**1. Required Number of Circuits for Kitchen:**
- **Minimum Requirement**: **Two or more 20-ampere small-appliance branch circuits** are required for all receptacle outlets in kitchens, pantries, breakfast rooms, and dining rooms (CEC 2022 Section 210.52(B)(1)).  
- **Purpose**: These circuits serve countertop outlets, wall/floor receptacles, and refrigeration equipment in these areas.

**2. Serving Dining Room Receptacles:**
- **Permitted**: Yes, the **same small-appliance branch circuits** serving the kitchen **can also supply receptacles in the dining room** (CEC 2022 Section 210.52(B)(1)).  
- **Limitation**: No small-appliance branch circuit shall serve more than **one kitchen**, but dining room receptacles are explicitly allowed under the same circuits.  

**Key Code Citations**:  
- **210.52(B)(1)**: Requires two+ 20A circuits for kitchens and permits them to serve dining rooms.  
- **210.52(B)(2)**: Prohibits additional non-specified outlets on small-appliance circuits (except for exceptions like clocks or gas appliances).  

**Inspector Note**: Ensure circuits are **not overloaded** and that dining room receptacles are within the same dwelling unit. Additional circuits are permitted but not required.  

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 8.8s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 7.3s

**Tools Called:** nec_search

**Answer:**

## NEC AFCI Requirements and Hazards (NEC 2023)

### Why AFCI Protection is Required for Bedrooms and Living Areas
The NEC mandates **arc-fault circuit interrupter (AFCI)** protection for bedrooms and living areas to **prevent electrical fires caused by dangerous arc faults**. These arcs can occur due to damaged wiring, loose connections, or faulty appliances, and they generate high heat capable of igniting surrounding materials.

### Key NEC Sections:
- **NEC 210.12(A)(1)**: Requires AFCI protection for **bedrooms, living rooms, hallways, and similar areas** in dwelling units.  
- **NEC 210.12(C)**: Extends this requirement to **dormitory units** (bedrooms, living rooms, etc.).  
- **NEC 210.12(D)**: Applies to **hotel/motel guest rooms** and similar occupancies.  

### Electrical Hazard Prevented:
AFCIs detect **series arcs** (e.g., from damaged cords) and **parallel arcs** (e.g., from loose connections), which standard circuit breakers may not interrupt. These arcs can overheat insulation or nearby combustibles, leading to fires. AFCIs mitigate this risk by disconnecting the circuit when an arc is detected.

### Inspector Note:
- **Exceptions** exist for specific cases (e.g., fire alarm circuits, temporary extensions), but the general rule emphasizes fire prevention in high-risk areas.  
- **Informational Notes** reference UL standards (e.g., UL 1699) for AFCI device requirements and NFPA 72 for fire alarm systems.

[OK] Source: NEC 2023

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 5.2s

**Tools Called:** cec_search

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

**Why Torque Specifications Are Important:**  
Proper torque ensures secure, low-resistance electrical connections that can safely carry the expected current without overheating. Incorrect torque can lead to:  
- **Under-torqued connections**: Loose terminations causing arcing, heat buildup, and potential fire hazards.  
- **Over-torqued connections**: Damaged terminals or conductors, leading to mechanical failure or increased resistance.  

**Code Requirements:**  
Found in **CEC 2022 Section 110.14(D)**:  
- **Torque values** must be specified by the equipment manufacturer and documented on the equipment or in installation instructions.  
- **Approved methods** (e.g., torque wrenches, shear bolts, or breakaway devices) must be used to achieve the specified torque.  

**Key Code Language**:  
> *"Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer. An approved means shall be used to achieve the indicated torque value."*  

**Additional Guidance**:  
- If torque values are not provided, contact the equipment manufacturer or reference **UL 486A-486B** for default values.  
- **Informational Notes** reference **NFPA 70B** for best practices in torquing threaded connections.  

[OK] Source: CEC 2022

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 13.0s

**Tools Called:** compare_with_nec

**Answer:**

## Residential Service Load Calculation (CEC 2022)

### Step 1: Calculate Adjusted Loads
**1. Electric Range (CEC 220.50):**
- Nameplate rating: 12,000 VA
- Demand factor for single range: 8,000 VA + 40% of remaining 4,000 VA = **9,600 VA**

**2. Dryer (CEC 220.54):**
- Nameplate rating: 5,500 VA
- Minimum requirement: 5,000 VA
- Use larger value: **5,500 VA**

**3. Small Appliance & Laundry Circuits (CEC 220.52):**
- 2 × 20A circuits (1,500 VA each) = 3,000 VA
- 1 × 20A laundry circuit = 1,500 VA
- Total: **4,500 VA**

**4. General Lighting (CEC 220.12):**
- 3,000 sq ft × 3 VA/sq ft = **9,000 VA**

**5. Central AC (CEC 220.18):**
- 4600 VA (19.2A × 240V)
- Continuous load factor: 4600 × 1.25 = **5,750 VA**

---

### Step 2: Apply Demand Factors
**General Lighting & Small Appliance Load (CEC 220.42):**
- First 3,000 VA @ 100% = 3,000 VA
- Remaining 10,500 VA @ 35% = 3,675 VA
- **Total: 6,675 VA**

---

### Step 3: Total Service Load
| Load Type               | VA       |
|-------------------------|----------|
| Range                   | 9,600    |
| Dryer                   | 5,500    |
| General Lighting        | 6,675    |
| Central AC              | 5,750    |
| **Total**               | **27,525 VA** |

---

### Step 4: Convert to Amperes
$$
\text{Service Load} = \frac{27,525\ \text{VA}}{240\ \text{V}} = 114.69\ \text{A}
$$

---

### Final Determination
- **Calculated Load:** 114.7A
- **Main Breaker Rating:** 200A

**Conclusion:** The 200A main breaker is **adequately sized** for the calculated load of 114.7A. The service has sufficient capacity to handle all connected loads with room for future expansion.

[OK] Source: CEC 2022

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 11.2s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 7.5s

**Tools Called:** nec_search

**Answer:**

## Circuit Protection Requirements (NEC 2023)

### 1. **Countertop Receptacles (2 x 20A circuits)**
- **Protection Required**: **GFCI**  
- **NEC Reference**: **210.8(A)(6)**  
  - *Kitchen countertop receptacles must have GFCI protection for personnel safety.*

### 2. **Dishwasher (15A Dedicated Circuit)**
- **Protection Required**: **GFCI**  
- **NEC Reference**: **210.8(A)(7)**  
  - *Receptacles for dishwashers require GFCI protection.*

### 3. **Garbage Disposal (15A Dedicated Circuit)**
- **Protection Required**: **Standard Breaker**  
- **NEC Reference**: **No specific GFCI requirement**  
  - *NEC 2023 does not mandate GFCI for garbage disposals unless installed in wet locations (not applicable here).*

### 4. **Refrigerator (20A Dedicated Circuit)**
- **Protection Required**: **AFCI**  
- **NEC Reference**: **210.12(A)**  
  - *All branch circuits in dwelling units require AFCI protection unless exempted (refrigerators are not exempt).*

---

**Inspector Note**:  
- **GFCI** is mandatory for countertop and dishwasher circuits to prevent electric shock in wet/damp environments.  
- **AFCI** is required for the refrigerator circuit to mitigate arc faults in dwelling unit branch circuits.  
- **Garbage disposal** circuits remain standard unless local amendments apply.  

[OK] Source: NEC 2023

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 8.6s

**Tools Called:** cec_search

**Answer:**

## Subpanel Grounding Violations in Detached Garage (CEC 2022)

### Identified Violations:
1. **Missing Grounding Electrode**  
   - **Violation**: No grounding electrode system installed at the detached structure.  
   - **Code**: CEC 250.32(A) requires a grounding electrode system for buildings supplied by feeders/branch circuits.  
   - **Exception**: Only waived for single-branch circuits (not applicable here).  

2. **Bonded Neutral and Ground Bars**  
   - **Violation**: Neutral and ground bars are bonded together with a main bonding jumper.  
   - **Code**: CEC 250.32(B)(1) prohibits connecting the grounded (neutral) conductor to the grounding electrode system in subpanels.  
   - **Correct**: Neutral and ground must be isolated in subpanels (bonding only occurs at the main service).  

3. **Neutral Bar Bonded to Enclosure**  
   - **Violation**: Neutral bar is bonded to the metal subpanel enclosure.  
   - **Code**: CEC 250.121(B) prohibits using the building’s metal frame as a grounding conductor.  
   - **Correct**: Neutral must only connect to the neutral bar; enclosure bonding is reserved for grounding electrode conductor (GEC).  

---

### Correct Configuration:
1. **Grounding Electrode Requirement**  
   - Install a **separate grounding electrode** (e.g., ground rod) at the detached garage per **CEC 250.50**.  
   - Connect the **grounding electrode conductor** (GEC) from the electrode to the **ground bar** in the subpanel (not the neutral bar).  

2. **Neutral and Ground Separation**  
   - **Neutral bar**: Connect only the feeder neutral conductor.  
   - **Ground bar**: Connect:  
     - Feeder equipment grounding conductor (EGC).  
     - Grounding electrode conductor (GEC) from the ground rod.  
   - **No bonding** between neutral/ground bars or to the enclosure.  

3. **Equipment Grounding**  
   - The #2 AWG aluminum feeder ground wire (EGC) must connect to the **ground bar** (already correct per inspector’s note #4).  

---

### Inspector Notes Analysis:
- **Note 1 (Bonded neutral/ground bars)**: ❌ Violation. Remove bonding jumper.  
- **Note 2 (Ground bar bonded to enclosure)**: ✅ Acceptable if GEC connects to ground bar.  
- **Note 3 (Neutral bar bonded to enclosure)**: ❌ Violation. Disconnect neutral bar from enclosure.  
- **Note 4 (EGC connected to ground bar)**: ✅ Correct.  
- **Note 5 (Neutral connected to neutral bar)**: ✅ Correct.  

---

### Summary of Fixes:
| **Issue**                     | **Correction**                                  | **Code Reference**       |
|-------------------------------|--------------------------------------------------|--------------------------|
| Missing grounding electrode   | Install ground rod and connect to ground bar     | CEC 250.32(A), 250.50    |
| Bonded neutral/ground bars    | Remove bonding jumper; isolate neutral/ground bars | CEC 250.32(B)(1)         |
| Neutral bar bonded to enclosure| Disconnect neutral bar from enclosure            | CEC 250.121(B)           |

[OK] Source: CEC 2022

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 5.3s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 11.5s

**Tools Called:** cec_lookup_conductor_resistance, cec_search

**Answer:**

## Voltage Drop Calculation Verification (CEC 2022)

1. **Voltage Drop Calculation**:  
   - **Formula**:  
     $$
     VD = \frac{2 \times L \times R \times I}{1000} = \frac{2 \times 50 \times 1.98 \times 22}{1000} = 4.36 \, \text{V}
     $$
   - **Percentage**:  
     $$
     \frac{4.36}{120} \times 100 = 3.63\%
     $$

2. **Code Compliance Check**:  
   - **CEC 210.19(A)(1) Informational Note No. 3** explicitly states:  
     *"Voltage drop exceeding 3% at the farthest outlet is not recommended for branch circuits."*  
   - **Section 647.4(D)** applies stricter limits (1.5% for fixed equipment), but this is a general branch circuit, not a high-voltage system.  

3. **Conclusion**:  
   - **3.63%** exceeds the **3% maximum** recommended by CEC 210.19(A)(1).  

**Final Answer**:  
The voltage drop of **3.63%** does **not** meet the NEC/CEC recommendation of ≤3% for branch circuits.  

[OK] Source: CEC 2022

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 4.5s

**Tools Called:** cec_ampacity_with_adjustments

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Conductor**: 12 AWG copper  
**Insulation**: TW (60°C rated)  
**Ambient Temperature**: 43°C  
**Number of Conductors**: 6  

---

### **Step 1: Base Ampacity**  
- **Source**: CEC Table 310.16 (60°C column)  
- **Value**: **20A**  

---

### **Step 2: Temperature Correction Factor**  
- **Ambient Temperature**: 43°C  
- **Correction Factor**: **0.71** (CEC Table 310.15(B)(1)(1))  

---

### **Step 3: Bundling Adjustment Factor**  
- **Number of Conductors**: 6  
- **Adjustment Factor**: **0.8** (CEC Table 310.15(C)(1))  

---

### **Step 4: Final Derated Ampacity**  
$$
\text{Derated Ampacity} = 20A \times 0.71 \times 0.8 = 11.36A
$$

---

### **Limiting Rule Check**  
- **Section 240.4(D)**:  
  - 12 AWG copper is limited to **20A** overcurrent protection.  
  - **Note**: The derated ampacity (11.36A) is less than the OCPD limit (20A), so the conductor is adequately protected.  

---

### **Final Answer**  
- **Adjusted Ampacity**: **11.36A**  
- **Overcurrent Protection Limit**: **20A maximum** (per 240.4(D))  

---

**Citations**:  
- Base Ampacity: CEC Table 310.16  
- Temperature Correction: CEC Table 310.15(B)(1)(1)  
- Bundling Adjustment: CEC Table 310.15(C)(1)  
- OCP Limit: CEC 240.4(D)  

[OK] Source: CEC 2022

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 5.6s

**Tools Called:** None

**Answer:**

Error: name 're' is not defined

---

