# Core (NEC) Evaluation Results - Run 33 (Reflection Bugfix)

**Date:** 2025-12-11
**Changes:** Added reflection/self-verification after initial answer

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 226.5s |
| Avg Duration | 8.4s |
| Reflection Used | 27/27 |
| Reflection Improved | 3/27 |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 6.0s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size

**Reflection:** Yes

**Answer:**

## Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size**: **6 AWG copper**  
- **Ampacity**: 65A at 75°C (Table 310.16)  
- **Meets requirement**: 65A ≥ 60A  

**Key Considerations**:  
1. **Overcurrent Protection**:  
   - Per **240.4(D)**, 6 AWG copper conductors must be protected at **60A maximum** (not 65A), as 240.4(D) limits OCP to 60A for 6 AWG.  

2. **Adjustment Factors**:  
   - If ambient temperature exceeds 30°C or more than 3 current-carrying conductors are bundled, apply correction factors from **310.15(B)** or **310.15(C)(1)**.  

3. **Exceptions**:  
   - No exceptions apply for general 60A circuits.  

**Inspector Note**: Always verify ambient conditions and bundling before finalizing conductor size.  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 10.8s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**Requirement:**  
All **125-volt through 250-volt receptacles** installed in **kitchens** to serve **countertop surfaces** must have **ground-fault circuit-interrupter (GFCI) protection** for personnel.  

**Code Reference:**  
- **CEC 2022 Section 210.8(A)(6)**:  
  *"Kitchens - where the receptacles are installed to serve the countertop surfaces."*  

**Key Details:**  
- Applies to **single-phase branch circuits rated 150 volts or less to ground**.  
- Receptacles must be **readily accessible**.  
- Exceptions (not applicable in standard residential kitchens):  
  - Listed locking receptacles for ceiling luminaires/fans (if not general-purpose).  

**No GFCI Required For:**  
- Receptacles **more than 6 ft from sinks** (covered under separate rules).  
- **Dedicated circuits** for specific appliances if protected per 422.5 (e.g., drinking water coolers).  

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 5.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction per **CEC 2022 Section 210.12(A)**.  

**Details:**  
- **Section 210.12(A)** explicitly lists bedrooms as one of the required locations for arc-fault circuit-interrupter (AFCI) protection.  
- The rule applies to **all 120-volt, single-phase, 15- and 20-ampere branch circuits** supplying outlets or devices in bedrooms.  
- Permitted AFCI protection methods include:  
  1. A **combination-type AFCI** at the service panel.  
  2. A **branch/feeder-type AFCI** at the panel combined with an outlet branch-circuit-type AFCI at the first outlet.  
  3. Other listed combinations (e.g., supplemental protection + outlet AFCI).  

**Exceptions:**  
- No exceptions apply to new construction. The only exceptions relate to:  
  - Fire alarm systems (not applicable here).  
  - Limited modifications/extensions (not relevant for new construction).  

**Inspector Note:**  
Verify the AFCI type and installation location per **210.12(A)(1)-(6)**. Bedrooms must use one of the listed protection methods.  

[OK] Source: CEC 2022 Section 210.12(A)

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 6.7s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_exception_search

**Reflection:** Yes (improved answer)

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

[OK] **Yes**, aluminum conductors are permitted for a 200A service.  
[OK] **Required size**: **4/0 AWG aluminum**  
[OK] **Source**: CEC 2022 Table 310.12(A) (Single-Phase Dwelling Services and Feeders)

### Key Requirements:
1. **Table 310.12(A)** applies to dwelling unit services/feeders with 120/240V or 120/208Y systems.
2. **75°C rating** assumed for service conductors (standard for service entrance conductors).
3. **No temperature correction or bundling adjustments** required per Table 310.12(A) notes.

### Inspector Note:
- For non-dwelling services, use **Table 310.16** instead (more conservative sizing).
- Verify termination compatibility with aluminum (e.g., torque requirements, anti-oxidant use).

[OK] Source: CEC 2022

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 5.5s | **Iterations:** 3

**Tools Called:** cec_lookup_working_space

**Reflection:** Yes

**Answer:**

## Minimum Working Clearance Depth (CEC 2022)

The **minimum depth of working clearance** required in front of a 120/240V residential electrical panel is **3 feet (900 mm)** under **Condition 1** of CEC Table 110.26(A)(1). This applies when:

- Voltage to ground is **120V** (as in a 120/240V split-phase system)
- Exposed live parts are on **one side** of the working space
- No live or grounded parts are on the **other side**, or both sides are effectively guarded

[OK] Source: CEC 2022 Table 110.26(A)(1)

**Additional Notes:**
- For **Condition 2** (live parts on one side and grounded parts on the other), the clearance remains 3 ft
- For **Condition 3** (live parts on both sides), the clearance increases to **3.5 ft (1050 mm)**
- Always verify **panel location** separately using CEC 240.24 for prohibited locations (closets, bathrooms)

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 5.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Required Small Appliance Branch Circuits for Kitchen (CEC 2022)

**Answer:**  
A minimum of **two 20-ampere small appliance branch circuits** are required for a kitchen in a dwelling unit.

**Code Basis:**  
- **CEC 2022 Section 210.11(C)(1):**  
  *"In addition to the number of branch circuits required by other parts of this section, two or more 20-ampere small-appliance branch circuits shall be provided for all receptacle outlets specified by 210.52(B)."*  

- **CEC 2022 Section 210.52(B)(1):**  
  *"In the kitchen... the two or more 20-ampere small-appliance branch circuits required by 210.11(C)(1) shall serve all wall and floor receptacle outlets... and receptacle outlets for refrigeration equipment."*

**Key Notes:**  
- The circuits must serve **all kitchen receptacles**, including countertop outlets (per 210.52(C)).  
- **No more than one kitchen** may be served by a single small-appliance branch circuit (Exception No. 2 in 210.52(B)(1)).  
- Additional circuits are permitted but not required (e.g., for heavy loads).

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 5.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is **required** for a new 200A residential service per **CEC 2022 Section 230.67**:

- **Section 230.67(A):** All services supplying dwelling units **must include a surge-protective device (SPD)**.
- **Location:** The SPD must be:
  - An integral part of the service equipment, or
  - Located immediately adjacent to the service equipment.
  - *Exception:* May be installed at the next level of distribution downstream toward the load.
- **Type Required:** Type 1 or Type 2 SPD (per Section 230.67(C)).

**Inspector Note:**  
This requirement applies specifically to **dwelling units**. For non-residential services, surge protection is not mandated unless specified by other articles (e.g., fire pump systems in 695.15 or critical operations in 645.18).

[OK] Source: CEC 2022

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 13.6s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size, cec_lookup_conductor_size, cec_lookup_conductor_size, cec_search, cec_exception_search, cec_search

**Reflection:** Yes (improved answer)

**Answer:**

## Service Conductor Sizing for 200A Upgrade (CEC 2022)

**MULTIPLE VALID OPTIONS:**

**Option A: Dwelling-Specific (Table 310.12(A))**
- **Copper**: 2/0 AWG (200A rating)
- **Aluminum**: 4/0 AWG (200A rating)
- **Applies when**: Conductors supply entire dwelling load (120/240V single-phase)
- **Source**: CEC Table 310.12(A)

**Option B: General Use (Table 310.16)**
- **Copper**: 3/0 AWG (200A rating)
- **Aluminum**: 250 kcmil (205A rating)
- **Applies when**: Non-dwelling or when using general feeder/service tables
- **Source**: CEC Table 310.16

**Inspector Note**: 
- **Aluminum is permitted** for service conductors in California (no statewide ban).
- **Critical check**: Verify installation conditions (ambient temperature, bundling) via:
  - **310.15(B)** (temperature correction)
  - **310.15(C)(1)** (bundling adjustment)
  - **240.4(D)** (overcurrent protection limits)

**Final Recommendation**:
- Use **2/0 copper** or **4/0 aluminum** for dwelling service conductors (Table 310.12(A) is more permissive for residential applications).
- If using Table 310.16 (general), **3/0 copper** or **250 kcmil aluminum** is required.

[OK] Source: CEC 2022

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 8.9s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Answer:**

## Multiwire Branch Circuit Requirements (CEC 2022)

### Circuit Breaker Requirements
1. **Simultaneous Disconnection**: 
   - A multiwire branch circuit **must be protected by a circuit breaker with a handle tie** that simultaneously opens all ungrounded (hot) conductors (CEC 210.4(B), 240.15(B)(1)). 
   - This prevents energizing the neutral conductor if only one hot leg is disconnected, which could create a shock hazard.

2. **Breaker Rating**:
   - For 12 AWG copper conductors (12/3 cable), the maximum overcurrent protection is **20A** (CEC 240.4(D)). 
   - The breaker must be rated for the circuit voltage (e.g., 120/240V for single-phase kitchen circuits).

---

### Neutral Conductor Requirements
1. **Sizing**:
   - The neutral conductor must be **sized to carry the maximum unbalanced load** (CEC 210.4(C)). 
   - For 12/3 cable with 12 AWG hots, the neutral must also be **12 AWG** (same size as hots) unless harmonic currents or other factors require upsizing (see CEC 220.61 for load calculations).

2. **Grouping/Identification**:
   - The neutral must be **grouped with the corresponding hot conductors** in the panel and marked to avoid confusion (CEC 200.4(B)). 
   - This ensures proper identification during maintenance or troubleshooting.

---

### Key Code Citations
- **Breaker Requirements**: CEC 210.4(B), 240.15(B)(1)  
- **Neutral Sizing**: CEC 210.4(C), 200.4(B)  
- **Conductor Ampacity**: CEC 240.4(D)  

[OK] Source: CEC 2022

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 9.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (CEC 2022)

According to **CEC 2022 Section 210.8**, GFCI protection is required in the following locations for residential dwelling units:

1. **Bathrooms**  
   - All 125–250V receptacles.  
   - *Exception:* Locking receptacles for ceiling fixtures may omit GFCI if integral to the fixture.

2. **Garages and accessory buildings**  
   - Receptacles in attached/detached garages (floor at or below grade).  
   - *Exception:* Receptacles for snow-melting/deicing systems may omit GFCI (per 426.28/427.22).

3. **Outdoors**  
   - All receptacles at grade level.  
   - *Exception:* Receptacles for snow-melting/deicing systems (same as above).

4. **Crawl spaces (at or below grade)**  
   - All receptacles.  
   - *Exception:* None specified.

5. **Basements**  
   - All receptacles (unfinished areas).  
   - *Exception:* Receptacles for fire alarm systems may omit GFCI (per 760.41(B)/760.121(B)).

6. **Kitchens**  
   - Receptacles serving countertop surfaces.  
   - *Exception:* None specified.

7. **Sinks**  
   - Receptacles within **6 ft (1.8 m)** of the top inside edge of the bowl.  

8. **Boathouses**  
   - All receptacles.  

9. **Bathtubs/Showers**  
   - Receptacles within **6 ft (1.8 m)** of the outside edge.  

10. **Laundry areas**  
    - All receptacles.  

11. **Indoor damp/wet locations**  
    - All receptacles in such environments.  

12. **Additional Outdoor Requirements (210.8(F))**  
    - All outdoor receptacles (not covered by exceptions for snow-melting systems).  

---

### Key Exceptions:
- **Fire alarm systems** in basements (210.8(A)(5) Exception).  
- **Dedicated circuits** for snow-melting/deicing (210.8(A)(3) Exception).  
- **Locking receptacles** for ceiling fixtures (210.8(A) Exception).  

---

[OK] Source: CEC 2022 Section 210.8  
[OK] Source: CEC 2022 Section 210.8(F)

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 9.4s | **Iterations:** 4

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Answer:**

## Surge Protection for Residential Services (CEC 2022)

**Requirement:**  
Surge protection is **required** for all residential services supplying dwelling units per **CEC 2022 Section 230.67**.

**Installation Options:**  
1. **Service Equipment Integration**  
   - Must be an **integral part of the service equipment** (e.g., main panel).  
   - OR installed **immediately adjacent** to the service equipment.  

2. **Downstream Installation**  
   - Permitted at the **next level of distribution equipment** (e.g., subpanel) **downstream toward the load** (Exception to 230.67(B)).  

**SPD Type Requirements:**  
- Must be **Type 1 or Type 2** surge-protective device (SPD) (Section 230.67(C)).  

**Additional Notes:**  
- If service equipment is replaced, surge protection must still comply with this section (230.67(D)).  
- Supply-side installation (before service disconnect) is permitted for SPDs under specific conditions (referenced in 230.94 Exception No. 2).  

[OK] Source: CEC 2022

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 7.5s | **Iterations:** 3

**Tools Called:** cec_lookup_working_space

**Reflection:** Yes

**Answer:**

## Panel Clearance and Location Compliance (CEC 2022)

### 1. **Front Clearance Requirement**
- **Required**: 36 inches (3 ft) per CEC Table 110.26(A)(1) for 120V panels (Condition 1).
- **Actual**: 24 inches provided.
- **Conclusion**: **Fails requirement**. Minimum 36 inches of clear working space depth is required in front of the panel.

### 2. **Side Clearance Consideration**
- **Water heater located 18 inches from panel side**:
  - If the side has **no exposed live parts**, 18 inches may be acceptable (NEC/CEC does not specify minimum side clearance unless equipment is on both sides).
  - If the side has **exposed live parts**, 36 inches of clearance is required (Condition 3).

### 3. **Closet Location Restrictions**
- **Critical check**: Panel installed in a **closet**.
  - **240.24(D)**: Prohibits panels in **clothes closets**.
  - **240.24(E)**: Prohibits panels in **bathrooms of dwelling units**.
  - If this is a **general storage closet** (not clothes closet or bathroom), location may be permitted, but **front clearance still fails**.

### 4. **Code Citations**
- Working space depth: **CEC Table 110.26(A)(1)**
- Panel location restrictions: **CEC 240.24(D)(E)**

[OK] Source: CEC 2022

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 5.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Code Violation for Multiple Conductors on a Terminal (CEC 2022)

**Yes, this is a code violation under CEC 2022 Section 110.14(A).**

### Key Requirements:
1. **Terminal Identification**: 
   - Per **CEC 2022 110.14(A)**, *terminals for more than one conductor must be explicitly identified* for this purpose. 
   - The breaker in question is **not marked** for two conductors, violating this requirement.

2. **Risks of Non-Compliance**:
   - Multiple conductors under a single terminal can lead to **poor electrical contact**, **overheating**, and **increased risk of fire**.
   - This practice is generally prohibited unless the terminal is **listed and labeled** for multiple conductors (e.g., "2-wire" or "2-conductor" marked terminals).

3. **Inspector Action**:
   - **Corrective Action Required**: Replace the breaker with one marked for two conductors, or use a **listed wire connector** (e.g., a split bolt or push-in connector) to join the two conductors before connecting to a single terminal.

---

[OK] Source: CEC 2022 Section 110.14(A)

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 7.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### Key Requirements:
1. **Separate Grounding Electrode System**  
   - Install a **local grounding electrode** (e.g., ground rod) at the detached garage per **250.50**.  
   - Bond all grounding electrodes (e.g., rod, metal water pipe) at the garage to form a grounding electrode system.

2. **Grounding Electrode Conductor (GEC)**  
   - Connect the local grounding electrode to the **ground bar** in the garage subpanel using a **GEC** sized per **Table 250.66** based on the largest ungrounded conductor in the feeder.  
   - Example: For a 100A feeder with 3/0 AWG copper conductors, use a **2 AWG copper GEC** (Table 250.66).

3. **Equipment Grounding Conductor (EGC)**  
   - Run an **equipment grounding conductor** with the 4-wire feeder (from house panel to garage subpanel).  
   - Size the EGC per **Table 250.122** based on the overcurrent protection rating (e.g., 10 AWG copper for a 60A circuit).

4. **Neutral and Ground Separation**  
   - **Separate neutral and ground bars** in the subpanel.  
   - Connect the **neutral bar** only to the neutral conductor from the feeder.  
   - Connect the **ground bar** to:  
     - The local GEC (ground rod).  
     - The EGC from the feeder.  

5. **No Neutral-to-Ground Bond**  
   - Do **not bond the neutral and ground bars** in the subpanel (unlike the main service panel). This prevents ground loops and ensures proper fault current paths.

---

### Summary Diagram:
```
House Panel (Main Service)  
   │  
   │ 4-Wire Feeder (2 hots, 1 neutral, 1 EGC)  
   ▼  
Garage Subpanel  
   ├─ Neutral Bar → Neutral Conductor (from feeder)  
   ├─ Ground Bar →  
   │    ├─ Equipment Grounding Conductor (from feeder)  
   │    └─ Grounding Electrode Conductor (to local ground rod)  
   └─ No bond between Neutral and Ground Bars
```

---

### Code Citations:
- **250.32(B)(1)**: Requires an equipment grounding conductor and grounding electrode system for detached structures.  
- **250.50**: Mandates bonding of all grounding electrodes at the detached structure.  
- **250.66**: Sizes the grounding electrode conductor based on feeder conductor size.  
- **250.122**: Sizes the equipment grounding conductor based on overcurrent protection.  

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 6.6s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
1. **Main Bonding Jumper**  
   - **Definition**: Connection between the grounded circuit conductor and the equipment grounding conductor **at the service** (CEC 2022 Section 100).  
   - **Purpose**: Bonds the grounded conductor (neutral) to the equipment grounding system **at the service equipment**.  

2. **System Bonding Jumper**  
   - **Definition**: Connection between the grounded circuit conductor and the supply-side bonding jumper or equipment grounding conductor **at a separately derived system** (CEC 2022 Section 100).  
   - **Purpose**: Bonds the grounded conductor to the equipment grounding system **at the source of a separately derived system** (e.g., transformers, generators).  

---

### **Key Differences**
| **Aspect**                | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|---------------------------|--------------------------------------------------|----------------------------------------------------|
| **Location**              | At the **service equipment** (e.g., service panel). | At the **source of a separately derived system** (e.g., transformer secondary, generator output). |
| **Application**           | Required for **services** (per 250.28).          | Required for **separately derived systems** (per 250.28 and 250.32). |
| **Sizing**                | Sized per **Table 250.102(C)(1)** based on the largest ungrounded service conductor. | Sized per **Table 250.102(C)(1)** based on the largest ungrounded conductor of the separately derived system. |
| **Code Reference**        | CEC 2022 Sections 250.28, 250.102               | CEC 2022 Sections 250.28, 250.32, 250.102         |

---

### **When Each is Required**
1. **Main Bonding Jumper**  
   - **Required in all services** (250.28(D)).  
   - Must be installed **at each service enclosure** if the service has multiple enclosures (250.28(D)(2)).  

2. **System Bonding Jumper**  
   - **Required in all grounded separately derived systems** (250.28(D), 250.32(B)).  
   - Must be installed **at the source of the derived system** (e.g., transformer, generator) to ensure the grounded conductor is bonded to the equipment grounding system.  

---

### **Sizing Example (Table 250.102(C)(1))**
For a service with **400 kcmil copper ungrounded conductors**:  
- **Main Bonding Jumper**: 2/0 copper (per Table 250.102(C)(1)).  

For a separately derived system with **350 kcmil aluminum ungrounded conductors**:  
- **System Bonding Jumper**: 1/0 copper (per Table 250.102(C)(1)).  

---

### **Inspector Note**
- **Main bonding jumpers** are part of the **service grounding system**.  
- **System bonding jumpers** are part of the **separately derived system grounding**.  
- Both must comply with material, attachment, and sizing requirements in **250.28** and **250.102**.  

[OK] Source: CEC 2022 Sections 100, 250.28, 250.32, 250.102

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 7.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Required Number of Circuits:**  
At least **two 20-ampere small-appliance branch circuits** are required for a kitchen, as mandated by **CEC 220.52(A)** (referencing **210.11(C)(1)**). These circuits are dedicated to supplying receptacles in the kitchen, pantry, and dining room.

**Dining Room Receptacles:**  
Yes, these circuits **can also serve dining room receptacles**, provided the dining room is part of the dwelling unit and the receptacles are for general use (not for fixed appliances). This is permitted under **210.11(C)(1)**, which allows small-appliance circuits to serve multiple areas, including kitchens and dining rooms.

**Code Citations:**  
- **220.52(A):** Requires 1500 VA per small-appliance circuit for load calculations.  
- **210.11(C)(1):** Specifies the minimum number of small-appliance circuits (typically two for kitchens).  

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 9.5s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator, cec_exception_search, cec_exception_search, cec_exception_search

**Reflection:** Yes (improved answer)

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   12 AWG THHN copper at 90°C = **30A** (Table 310.16 with California amendment)

2. **Bundling Adjustment**:  
   6 current-carrying conductors → **0.80 factor** (Table 310.15(C)(1))

3. **Temperature Adjustment**:  
   50°C ambient → **0.82 factor** (Table 310.15(B)(1)(1))

4. **Final Calculation**:  
   $$
   30A \times 0.80 \times 0.82 = 19.68A
   $$

**Final Adjusted Ampacity**: **19.68A** (round to **20A** for practical application)

---

**Citations**:  
- Base ampacity: CEC 2022 Table 310.16 (with California amendment)  
- Bundling factor: CEC 2022 Table 310.15(C)(1)  
- Temperature factor: CEC 2022 Table 310.15(B)(1)(1)  

**Inspector Note**:  
- The adjusted ampacity (19.68A) must be rounded **down** to the nearest standard overcurrent protection size (20A maximum per 240.4(D)).  
- Ensure the final ampacity complies with 240.4(D) limitations for 12 AWG copper (20A max OCP).  

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 6.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## AFCI Protection Requirements in Dwelling Units (CEC 2022)

### **Why AFCI Protection is Required**
The **National Electrical Code (NEC)** and **California Electrical Code (CEC) 2022** mandate **arc-fault circuit interrupter (AFCI) protection** for 120V, 15- and 20-ampere branch circuits in dwelling units (bedrooms, living rooms, kitchens, etc.) as outlined in **Section 210.12**. This requirement applies to prevent electrical fires caused by **arc faults** in wiring systems.

### **Electrical Hazard Prevented**
AFCIs are specifically designed to detect and interrupt **dangerous arc faults**, which are a leading cause of electrical fires in residential buildings. Arc faults occur due to:
- Damaged or degraded insulation
- Loose or broken conductor connections
- Overloaded circuits
- Faulty appliances or wiring

Unlike standard circuit breakers, AFCIs detect high-resistance arcs (which do not necessarily trip overcurrent protection) and interrupt the circuit before heat from the arc can ignite surrounding materials.

### **Key Code Requirements (CEC 2022 Section 210.12)**
- **Coverage**: All 120V, single-phase, 15- and 20-ampere branch circuits in dwelling units supplying outlets in bedrooms, living rooms, kitchens, hallways, and similar areas.
- **Protection Methods**: 
  - Combination-type AFCIs (most common)
  - Branch/feeder-type AFCIs
  - Outlet branch-circuit-type AFCIs (installed at the first outlet)
- **Exceptions**: 
  - Fire alarm circuits (per 760.41(B)/760.121(B)) if installed in metal raceways or encased in concrete.

### **Inspector Note**
AFCI protection is **not required** for:
- Circuits supplying fixed lighting or appliances (e.g., ranges, dryers) unless modified/extended.
- Circuits in commercial or industrial occupancies.

[OK] Source: CEC 2022

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

Torque specifications are critical for ensuring **secure, low-resistance electrical connections** in panels and equipment. Improper torque can lead to:
- Loose connections causing overheating/arcing
- Increased resistance leading to voltage drop
- Connection failures under load
- Fire hazards

### Code Requirements Location:
**CEC 2022 Section 110.14(D)** explicitly requires:
> "Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer. An approved means shall be used to achieve the indicated torque value."

**Key Requirements:**
1. **Manufacturer Specifications** (110.14(D)):
   - Torque values must match equipment markings or installation instructions
   - Approved means include torque tools, shear bolts, or breakaway devices with visual indicators

2. **Control Circuit Devices** (430.9(C)):
   - Screw-type terminals with 14 AWG or smaller copper conductors require **minimum 0.8 N·m (7 lb-in.)** torque unless otherwise identified

3. **Informational Notes** (110.14(D)):
   - Contact equipment manufacturers if torque values aren't marked
   - Refer to UL 486A-486B Annex I for default torque values
   - Follow NFPA 70B for threaded connection maintenance

[OK] Source: CEC 2022 Sections 110.14(D), 430.9(C)

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 18.4s | **Iterations:** 4

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Service Load Calculation (CEC 2022 - NEC Article 220)

### **1. General Lighting, Small Appliance, and Laundry Circuits**
- **General Lighting**: 3,000 sq ft × 3 VA/sq ft = **9,000 VA**  
- **Small Appliance Circuits**: 2 circuits × 1,500 VA = **3,000 VA**  
- **Laundry Circuit**: 1 circuit × 1,500 VA = **1,500 VA**  
- **Total**: 9,000 + 3,000 + 1,500 = **13,500 VA**  
- **Demand Factor (220.43)**:  
  - First 3,000 VA at 100% = **3,000 VA**  
  - Remaining 10,500 VA at 35% = **3,675 VA**  
  - **Total**: 3,000 + 3,675 = **6,675 VA**  

### **2. Electric Range (12 kW)**
- **Demand Factor (220.55)**: 8,000 VA (per Table 220.55 for a single range ≥12 kW)  
- **Total**: **8,000 VA**  

### **3. Dryer (5.5 kW)**
- **Demand Factor (220.54)**: 5,500 VA (actual load, as it exceeds 5,000 VA)  
- **Total**: **5,500 VA**  

### **4. Central AC (4-ton, 19.2A @ 240V)**
- **VA**: 19.2A × 240V = **4,608 VA**  
- **Noncoincident Load (220.60)**: AC is noncoincident with heating (no heating load specified), so **4,608 VA** used.  

### **5. Total Service Load**
- **Sum**: 6,675 (general) + 8,000 (range) + 5,500 (dryer) + 4,608 (AC) = **24,783 VA**  
- **Convert to Amps**: 24,783 VA ÷ 240V = **103.26A**  

### **6. Panel Adequacy**
- **200A Panel**: The calculated load (**103.26A**) is **well below** the 200A rating.  
- **Inspector Note**: The 200A panel is **adequately sized** for the installed loads.  

[OK] Source: CEC 2022 (NEC Article 220)

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 9.5s | **Iterations:** 3

**Tools Called:** cec_lookup_working_space

**Reflection:** Yes

**Answer:**

## Electrical Panel Inspection Violations (CEC 2022)

### 1. **Insufficient Working Space Depth**  
- **Violation**: Panel has **28 inches** of depth clearance in front.  
- **Requirement**: Minimum **36 inches (3 ft)** required for 120V panels (CEC Table 110.26(A)(1), Condition 1).  
- **Citation**: CEC 2022 110.26(A)(1).  

### 2. **Obstruction in Working Space**  
- **Violation**: Water heater located **16 inches** from the panel’s left side.  
- **Requirement**: Working space must be **clear of obstructions** (pipes, ducts, etc.) within the required depth (36 inches).  
- **Citation**: CEC 2022 110.26(A)(4).  

### 3. **Insufficient Panel Height**  
- **Violation**: Panel mounted at **5 ft** height.  
- **Requirement**: Minimum **6.5 ft (78 in)** height from floor to bottom of panel for equipment ≤ 600V (CEC 110.26(A)(2)).  
- **Citation**: CEC 2022 110.26(A)(2).  

---

### Additional Notes:  
- **Width Clearance**: 30 inches meets the minimum 30-inch requirement (Table 110.26(A)(1)).  
- **Location Check**: Panel in a garage is permitted unless prohibited by 240.24 (closets/bathrooms). No violation here.  

[OK] Source: CEC 2022

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 11.8s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Circuit Protection Requirements for Kitchen Installations (NEC 2023)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **GFCI + AFCI**
- **NEC References**:
  - **210.8(A)(6)**: All 125–250V receptacles installed to serve countertop surfaces in kitchens require **GFCI protection**.
  - **210.12(A)**: All branch circuits in dwelling units require **AFCI protection** unless exempted (no exemption applies here).

### 2. **Dishwasher (Dedicated 15A Circuit)**
- **Protection Required**: **GFCI + AFCI**
- **NEC References**:
  - **210.8(A)(6)**: Receptacles for small appliances (including dishwashers) in kitchens require **GFCI protection**.
  - **210.12(A)**: Requires **AFCI protection** for all branch circuits in dwelling units.

### 3. **Garbage Disposal (Dedicated 15A Circuit)**
- **Protection Required**: **GFCI + AFCI**
- **NEC References**:
  - **210.8(A)(6)**: Receptacles for small appliances (including garbage disposals) in kitchens require **GFCI protection**.
  - **210.12(A)**: Requires **AFCI protection** for all branch circuits in dwelling units.

### 4. **Refrigerator (Dedicated 20A Circuit)**
- **Protection Required**: **AFCI Only**
- **NEC References**:
  - **210.8(A)(6) Exception No. 2**: A receptacle for a specific appliance (e.g., refrigerator) on an individual branch circuit is **not required to have GFCI protection** if the appliance is listed and installed per manufacturer instructions.
  - **210.12(A)**: Requires **AFCI protection** for all branch circuits in dwelling units (no exemption applies here).

---

**Inspector Note**: 
- **GFCI** is mandatory for countertop and small-appliance circuits in kitchens to prevent electric shock.
- **AFCI** is required for all circuits in dwelling units to reduce fire hazards from arcing faults.
- The **refrigerator** is exempt from GFCI due to the risk of food spoilage if the circuit trips, but **AFCI remains mandatory**.

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 6.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Subpanel Grounding Violations in Detached Garage (CEC 2022)

### **Identified Violations**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation**: CEC 250.24(D) requires **separate neutral and ground bars** in subpanels (not main service). Bonding them creates parallel paths for neutral current, risking equipment damage and shock hazards.  
   - **Correct Configuration**: Neutral and ground bars must be **electrically isolated** in the subpanel.  

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: CEC 250.142(A) mandates that **only the equipment grounding conductor (EGC)** connects to the enclosure. Bonding the neutral bar to the enclosure creates unintended grounding paths.  
   - **Correct Configuration**: Neutral bar must remain **unbonded** from the enclosure.  

3. **Main Bonding Jumper Installed**  
   - **Violation**: CEC 250.24(D) prohibits a main bonding jumper in subpanels. This is reserved for the **main service panel** only.  
   - **Correct Configuration**: Remove the main bonding jumper.  

---

### **Correct Grounding Configuration for Detached Garage Subpanel**
1. **Feeder Conductors**  
   - **4-wire feeder**: 2 hots, 1 neutral, 1 ground (as installed).  

2. **Subpanel Internal Bonding**  
   - **Neutral Bar**: Connected **only to the feeder neutral**. No bonding to ground bar or enclosure.  
   - **Ground Bar**:  
     - Bonded to the **metal enclosure** (✓ correct).  
     - Connected to the **feeder ground wire** (✓ correct).  
     - Connected to the **grounding electrode conductor (GEC)** from the subpanel’s grounding electrode (e.g., rod, plate).  

3. **Grounding Electrode System**  
   - **GEC**: Must connect to a **separate grounding electrode** (e.g., ground rod) at the detached garage (CEC 250.32(B)).  

---

### **Key Code References**
- **CEC 250.24(D)**: Neutral conductor in subpanels must not connect to grounding electrode or equipment grounding conductors.  
- **CEC 250.142(A)**: Equipment grounding conductors must connect to the enclosure, but neutrals must remain isolated.  
- **CEC 250.32(B)**: Detached structures require a **separate grounding electrode** for the subpanel.  

[OK] Source: CEC 2022

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 11.7s | **Iterations:** 3

**Tools Called:** cec_lookup_conduit_fill

**Reflection:** Yes

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Calculation:**
1. **Conduit Fill Limit:**  
   - RMC 1¼" total area = 1.526 in² (Chapter 9 Table 4)  
   - 40% fill limit = 1.526 × 0.40 = **0.61 in²**

2. **Conductor Area:**  
   - 10 AWG THHN area = 0.0211 in² (Chapter 9 Table 5)

3. **Maximum Conductors:**  
   - 0.61 ÷ 0.0211 ≈ **28.91** → **28 conductors** (round down)

**Verification:**  
- 28 × 0.0211 = **0.5908 in²** (≤ 0.61 in² fill limit)  
- 3 conductors requested: 3 × 0.0211 = 0.0633 in² (4.1% fill) → ✅ Fits

**Answer:**  
A 1¼-inch RMC can accommodate **up to 28** of the 10 AWG THHN conductors at 40% fill. The requested 3 conductors are well within this limit.

[OK] Source: CEC 2022 Chapter 9 Tables 4 & 5

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 15.1s | **Iterations:** 6

**Tools Called:** python_calculator, python_calculator, cec_search

**Reflection:** Yes

**Answer:**

## Voltage Drop Verification (CEC 2022)

**Code References:**
1. **CEC 2022 Section 647.4(D):**  
   - Fixed equipment: Voltage drop ≤ 1.5% on branch circuits  
   - Combined feeder + branch: ≤ 2.5%  
   - *This applies to specific systems (e.g., sensitive equipment) with stricter limits.*

2. **CEC 2022 Section 210.19(A) Informational Note 3:**  
   - General branch circuits: Recommend ≤ 3% voltage drop at farthest outlet  
   - Combined feeder + branch: Recommend ≤ 5% total drop  
   - *This is the standard NEC/CEC recommendation for typical branch circuits.*

**Conclusion:**  
- Your calculation (2.37% drop) meets the **general recommendation** in **210.19(A)** (≤ 3%).  
- The stricter 1.5% limit in **647.4(D)** applies to specialized systems (not this case).  

**Final Answer:**  
- **Voltage drop:** 2.84 volts (2.37%)  
- **Compliance:** ✅ Meets CEC/NEC recommendation (≤ 3% for branch circuits)  

[OK] Source: CEC 2022

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 7.5s | **Iterations:** 5

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG TW copper conductors at 60°C rating:  
**20A** (Table 310.16)

**Step 2: Temperature Correction**  
Ambient temperature = 43°C  
Correction factor = **0.71** (Table 310.15(B)(1)(1))

**Step 3: Bundling Adjustment**  
6 current-carrying conductors in conduit  
Adjustment factor = **0.80** (Table 310.15(C)(1))

**Step 4: Final Calculation**  
Adjusted ampacity = 20A × 0.71 × 0.80 = **11.36A**

**Final Answer:**  
The adjusted ampacity is **11.36 amperes** after applying both correction factors.

[OK] Source: CEC 2022

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 5.1s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Answer:**

## Minimum Size Copper GEC for Parallel Service Conductors (CEC 2022)

**Answer:**  
The minimum size **copper grounding electrode conductor (GEC)** required is **2/0 AWG**.

**Calculation Steps:**  
1. **Equivalent Service Conductor Size:**  
   Four parallel sets of 250 kcmil copper = 4 × 250 kcmil = **1000 kcmil equivalent** (per Table 250.66 Footnote [1]).

2. **Table 250.66 Lookup:**  
   For copper conductors in the range **"Over 600 through 1100" kcmil**, the minimum GEC size is **2/0 AWG** (per CEC Table 250.66).

**Citations:**  
- **CEC Table 250.66** (with California amendment noted)  
- **Footnote [1]**: Confirms equivalent size calculation for parallel conductors.  

**Inspector Note:**  
- The GEC size is determined by the **total equivalent area** of all parallel service conductors.  
- California amendments (delta) may modify NEC requirements, but this result already incorporates local rules.  

[OK] Source: CEC 2022

---

