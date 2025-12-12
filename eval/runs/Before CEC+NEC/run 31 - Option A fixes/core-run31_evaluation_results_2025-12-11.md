# Core (NEC) Evaluation Results - Run 31 (Option A Fixes)

**Date:** 2025-12-11
**Changes:** Table truncation fix, cross-ref injection, location reminder

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 178.0s |
| Avg Duration | 6.6s |
| Exception Search Used | 0/27 |
| NEC Comparison Used | 0/27 |
| Memory Clearing | Enabled |
| Tool Enforcement | Enabled |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 3.8s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum conductor size**: **6 AWG copper**  
- **Ampacity**: 65A at 75°C (Table 310.16)  
- **Meets requirement**: 65A ≥ 60A  

**Key Considerations**:  
1. **Overcurrent Protection (240.4(D))**:  
   - 6 AWG copper is permitted with up to **65A** overcurrent protection.  
   - A **60A breaker** is acceptable for this circuit.  

2. **Adjustment Factors**:  
   - If ambient temperature exceeds 30°C or more than 3 current-carrying conductors are bundled, apply correction factors from:  
     - **Section 310.15(B)** (temperature)  
     - **Section 310.15(C)(1)** (bundling)  

3. **Exception Check**:  
   - No exceptions apply for general circuits (Section 310.16).  

**Final Answer**: Use **6 AWG copper** with a 60A breaker under standard conditions. Verify correction factors if environmental or installation conditions differ.  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 8.2s

**Tools Called:** cec_search

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**GFCI protection is required for all 125-volt through 250-volt receptacles installed in kitchens to serve countertop surfaces** (CEC 2022 Section 210.8(A)(6)). 

### Key Details:
- **Scope**: Applies to dwelling units (residential homes).
- **Location**: Receptacles serving **countertop surfaces** in kitchens.
- **Protection Type**: Ground-fault circuit-interrupter (GFCI) protection for personnel.
- **Exceptions**: None specified for standard kitchen countertop receptacles. Exceptions in the code (e.g., for dedicated appliance circuits) do not apply here unless the receptacle is part of a specific appliance (see 422.5 for appliance-specific exceptions).

### Code Reference:
- **CEC 2022 Section 210.8(A)(6)**: Mandates GFCI protection for kitchen countertop receptacles.  
- **Cross-reference**: See Section 210.52(C) for countertop receptacle placement requirements (not directly related to GFCI but provides context for outlet locations).

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 6.0s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction in California.  

**Code Reference:**  
- **CEC 2022 Section 210.12(A)** explicitly mandates AFCI protection for all 120V, 15A and 20A branch circuits in dwelling units, including **bedrooms**.  

**Key Details:**  
- Applies to **15- and 20-ampere circuits** supplying outlets or devices in bedrooms.  
- Permits multiple installation methods (e.g., combination-type AFCI at the panel, outlet branch-circuit-type AFCI at the first outlet).  
- Exceptions do not apply to new construction (e.g., no exception for fire alarm systems in this context).  

**Inspector Note:**  
Verify the AFCI type and installation method complies with **210.12(A)(1)–(6)**. For example:  
- A **combination-type AFCI** at the panel is the most common solution.  
- If using an **outlet branch-circuit-type AFCI**, ensure it is installed at the first outlet and marked per code.  

[OK] Source: CEC 2022 Section 210.12(A)

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 3.6s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

[OK] **Yes**, aluminum conductors are permitted for a 200A service.  
[OK] **Required size**: **4/0 AWG aluminum**  
- Ampacity: 200A at 75°C (per CEC Table 310.12(A))  
- Application: Single-phase dwelling service  

**Conditions for Table 310.12(A) use**:  
1. Conductors supply the **entire load** of a dwelling unit  
2. System is **120/240V or 120/208Y single-phase**  
3. **No temperature correction or adjustment factors** apply  

For installations requiring adjustments (e.g., high ambient temperature, bundled conductors), additional derating calculations would be required per CEC 310.15.  

[OK] Source: CEC 2022 Table 310.12(A)

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 3.7s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Minimum Working Clearance Depth (CEC 2022)

**Minimum depth required:** **900 mm (3 feet)**  
- Per **CEC Table 110.26(A)(1)** for 120V systems (Condition 1)  
- Applies to residential panels with nominal voltage ≤ 150V to ground  

**Key Notes:**  
1. This is the **minimum working space depth** in front of the panel (measured from the front of the equipment).  
2. **Conditions:**  
   - *Condition 1* applies when there are exposed live parts on one or both sides of the working space (common for standard residential panels).  
   - See footnotes for *Condition 2/3* if grounded/insulated barriers are present.  
3. **Location Restrictions Separate from Clearance:**  
   - Panels must **not** be installed in clothes closets (240.24(D)) or bathrooms of dwelling units (240.24(E)).  
   - Use `cec_search("240.24 panel location")` to verify compliance with these rules.  

[OK] Source: CEC 2022 Table 110.26(A)(1)

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 5.7s

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Answer:**  
A minimum of **two 20-ampere small appliance branch circuits** are required for a kitchen in a dwelling unit.  

**Code Basis:**  
- **CEC 2022 Section 210.11(C)(1)** (implied by cross-reference in 220.52):  
  Requires at least two 20-ampere circuits for small appliances in kitchens, pantries, and dining areas.  
- **CEC 2022 Section 220.52(A):**  
  Specifies each small-appliance branch circuit must be calculated at 1,500 VA for load calculations.  

**Key Notes:**  
- These circuits must serve **receptacles** in the kitchen area (not fixed appliances like ranges or refrigerators).  
- The requirement applies to **dwelling units** (residential) per 220.52.  

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 5.4s

**Tools Called:** cec_search

**Answer:**

## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is **required** for a new 200A residential service under **CEC 2022 Section 230.67**.

### Code Requirements:
1. **Mandatory SPD Installation**  
   - **Section 230.67(A):**  
     *"All services supplying dwelling units shall be provided with a surge-protective device (SPD)."*  
     This explicitly applies to residential services, including a 200A service.

2. **SPD Location**  
   - **Section 230.67(B):**  
     The SPD must be:  
     - An integral part of the service equipment, or  
     - Located immediately adjacent to the service equipment.  
     *Exception:* If installed downstream (closer to the load), it must be at the next level of distribution.

3. **SPD Type**  
   - **Section 230.67(C):**  
     The SPD must be **Type 1 or Type 2** (per UL 1449).  
     - **Type 1:** Installed between the service transformer and service disconnect.  
     - **Type 2:** Installed on the load side of the service disconnect (e.g., at the main panel).

4. **Replacement Requirements**  
   - **Section 230.67(D):**  
     If the service equipment is replaced, the SPD requirements must still be met.

### Exceptions and Notes:
- No exceptions exempt residential services from this requirement.  
- The SPD can be installed downstream (e.g., at a subpanel) if not in the service equipment itself (per 230.67(B) exception).

### Conclusion:
For a **new residential service** in California (CEC 2022), **surge protection is mandatory** under **Section 230.67**. Install a **Type 1 or Type 2 SPD** as specified.

[OK] Source: CEC 2022

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 8.6s

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size

**Answer:**

## Service Conductor Sizing for 200A Dwelling (CEC 2022)

**Required Service Conductor Sizes:**
- **Copper:** 2/0 AWG (180A at 75°C, Table 310.12(A))
- **Aluminum:** 4/0 AWG (155A at 75°C, Table 310.12(A))

**Key Code Requirements:**
1. **Table 310.12(A) Application**  
   - Applies to single-phase dwelling services/feeders with 120/240V or 120/208Y systems  
   - Assumes no temperature correction/adjustment factors (standard ambient conditions)  

2. **California-Specific Considerations**  
   - Aluminum conductors are **permitted** for service entrance conductors (CEC 2022 aligns with NEC 310.12)  
   - No additional CALGreen requirements for conductor material in this application  

3. **Load Verification**  
   - Your calculated load (73.75A after demand factors) is well below 200A service rating  
   - 200A service is **adequate** for 3,000 sq ft dwelling with listed appliances  

4. **Overcurrent Protection**  
   - 2/0 copper (180A rating) with 200A OCPD is **permitted** under 240.4(B) (next standard size allowed for service conductors)  
   - 4/0 aluminum (155A rating) with 200A OCPD is **permitted** under same rule  

**Inspector Note:**  
- Verify ambient temperature and bundling conditions in actual installation. If conductors are in high-temperature areas (>30°C) or bundled with >3 current-carrying conductors, apply correction factors from 310.15(B)(1)(1) and 310.15(C)(1).  

[OK] Source: CEC 2022 Tables 310.12(A), 240.4(B)

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 6.7s

**Tools Called:** cec_search

**Answer:**

## Multiwire Branch Circuit Requirements (CEC 2022)

**Circuit Breaker Requirements:**
- **Simultaneous Disconnection**: Per **210.4(B)**, the disconnecting means (breaker) must simultaneously disconnect **all ungrounded conductors**. This requires a **2-pole breaker** (or single-pole breakers with a listed handle tie) to ensure both hot conductors are disconnected together. Single-pole breakers without coordination are **not permitted**.
- **Exception**: If the circuit supplies only **line-to-neutral loads** (as in this kitchen receptacle application), the exception in **210.4(B)** applies when all ungrounded conductors are opened simultaneously.

**Neutral Termination Requirements:**
- **Grouping**: Per **210.4(D)** and **200.4(B)**, the **neutral conductor must be grouped with the ungrounded conductors** (hots) at the panel. This ensures the neutral remains connected only when all hots are energized.
- **Sizing**: The neutral conductor must be sized per **Table 310.16** for 12 AWG copper (standard for 20A circuits). For 12/3 cable, the neutral is **12 AWG** and terminates on a **neutral bus bar** in the panel.

**Key Code Citations:**
- **210.4(B)**: Requires simultaneous disconnection of all ungrounded conductors.
- **210.4(D)**: Permits MWBCs to supply line-to-neutral loads (kitchen receptacles) if all hots are disconnected.
- **200.4(B)**: Mandates grouping of grounded (neutral) and ungrounded conductors.

[OK] Source: CEC 2022

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 8.1s

**Tools Called:** cec_search

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (CEC 2022)

**All 125V–250V receptacles in the following locations require GFCI protection per CEC 2022 Section 210.8(A):**

1. **Bathrooms**  
   - All receptacles installed in bathrooms.  
   - *Exception:* Listed locking support/receptacles for ceiling luminaires/fans (if general-purpose receptacles are integral to the fixture, GFCI is required).

2. **Garages and Accessory Buildings**  
   - Receptacles in garages and accessory buildings with floors at or below grade (storage/work areas).  
   - *Exception:* Receptacles for dedicated snow-melting/deicing systems (per 426.28/427.22).

3. **Outdoors**  
   - All outdoor receptacles.  
   - *Exception:* Receptacles for dedicated snow-melting/deicing systems (per 426.28/427.22).

4. **Crawl Spaces**  
   - Receptacles in crawl spaces at or below grade.  
   - *Exception:* None specified for crawl spaces.

5. **Basements**  
   - Receptacles in unfinished basements.  
   - *Exception:* Receptacles for fire alarm/burglar alarm systems (not required to have GFCI).

6. **Kitchens**  
   - Receptacles serving countertop surfaces.  
   - *Exception:* None specified for kitchens.

7. **Sinks**  
   - Receptacles within 6 ft (1.8 m) of the top inside edge of sink bowls.  
   - *Exception:* In industrial labs, receptacles for equipment where power loss creates greater hazards (per 210.8(A)(5), Exception No. 1).

8. **Boathouses**  
   - All receptacles in boathouses.  
   - *Exception:* None specified.

9. **Bathtubs/Shower Stalls**  
   - Receptacles within 6 ft (1.8 m) of the outside edge of bathtubs/shower stalls.  
   - *Exception:* None specified.

10. **Laundry Areas**  
    - All receptacles in laundry areas.  
    - *Exception:* None specified.

11. **Indoor Damp/Wet Locations**  
    - Receptacles in indoor damp or wet locations.  
    - *Exception:* None specified.

**Additional Notes:**  
- **Exceptions for Ceiling Fixtures:** Listed locking support/receptacles for ceiling luminaires/fans are exempt if not general-purpose.  
- **Roof-top Receptacles:** Require GFCI unless not readily accessible (Exception No. 1 to 210.8(D)(3)).  
- **Industrial Establishments:** May use assured equipment grounding conductor programs for specific receptacles (Exception No. 2 to 210.8(D)(4)).

[OK] Source: CEC 2022 Section 210.8(A)–(F)

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 3.9s

**Tools Called:** cec_search

**Answer:**

## Surge Protection Requirements for Residential Service (CEC 2022)

**Requirement:**  
Surge protection is **required** for all services supplying dwelling units per **CEC 2022 Section 230.67(A)**.

**Installation Locations:**  
1. **Integral to service equipment** (e.g., main panel)  
2. **Immediately adjacent** to the service equipment  
3. **Next level distribution equipment downstream** toward the load (per exception in 230.67(B))  

**SPD Type:**  
Must be **Type 1 or Type 2** surge-protective device (SPD) (Section 230.67(C)).

**Inspector Note:**  
If the SPD is not installed in the service equipment itself, it must be located at the first downstream distribution point (e.g., a subpanel). This ensures protection at the service entrance per code.

[OK] Source: CEC 2022

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 5.9s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Panel Clearance and Location Compliance (CEC 2022)

### 1. **Working Space Clearance Requirements**
- **Front clearance**: 24 inches provided vs **minimum 36 inches (3 ft)** required for 120V panels per **Table 110.26(A)(1)** (condition 1).  
  ❌ **Fails clearance requirement**.

- **Side clearance**: 18 inches to water heater.  
  - **Minimum width requirement**: 30 inches (110.26(A)(2)).  
  - If the water heater occupies space within this 30-inch width, it **reduces usable working space**.  
  ❌ **Likely fails width requirement** unless the water heater is outside the 30-inch working space.

---

### 2. **Panel Location Restrictions**
- **Closet type**:  
  - If this is a **clothes closet**, **240.24(D)** prohibits panel installation.  
  - If it's a **general storage closet**, location is permitted **only if** working space requirements are met.  
  ❌ **Fails if clothes closet**.

---

### 3. **Code Citations**
- **Working space depth**: CEC Table 110.26(A)(1)  
- **Panel location prohibitions**: CEC 240.24(D) (clothes closets)  
- **Working space width**: CEC 110.26(A)(2)  

---

### ✅ **Compliance Summary**
| Requirement                | Provided | Required | Pass/Fail |
|----------------------------|----------|----------|-----------|
| Front clearance (depth)    | 24"      | 36"      | ❌ Fail     |
| Side clearance (width)     | 18"      | 30"      | ❌ Likely Fail |
| Location (clothes closet?) | N/A      | Prohibited | ❌ Fail if clothes closet |

**Inspector Note**: Even if the closet is not a clothes closet, the **front clearance is insufficient** (24" < 36") and the **side clearance may be inadequate**. Corrective action required:  
1. Increase front clearance to 36".  
2. Ensure 30" of unobstructed width.  
3. Verify closet type (clothes vs. general storage).  

[OK] Source: CEC 2022

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 4.1s

**Tools Called:** cec_search

**Answer:**

## Code Violation: Multiple Conductors on a Single Terminal (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under **CEC 2022 Section 408.41**. The key requirements are:

1. **Section 408.41** requires each grounded conductor to terminate in an **individual terminal** unless:
   - The conductors are **parallel conductors** (not applicable here for a 20A circuit), **and**
   - The terminal is **explicitly marked** for multiple conductors (which this breaker is not).

2. **Exception for parallel conductors** (408.41 Exception):  
   Only applies to **parallel conductors** (typically for large feeders, not 20A branch circuits). Since this is a single 20A breaker, the exception does not apply.

3. **Additional support from 110.14(C):**  
   Termination provisions require conductors to be connected in a manner that ensures a **secure, durable connection**. Using two conductors on an unmarked terminal risks overheating, poor contact, or terminal damage.

**Corrective Action:**  
- Use a **terminal rated for two conductors** (look for markings like "2" or "2 wires").  
- Alternatively, install a **junction box** to split the conductors and land each on a separate terminal.

[OK] Source: CEC 2022 Sections 408.41, 110.14(C)

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 5.4s

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### Key Requirements:
1. **Equipment Grounding Conductor (EGC):**
   - The feeder must include an EGC sized per **Table 250.122** based on the overcurrent protection rating of the feeder.
   - Example: For a 60A feeder, use **10 AWG copper** (from Table 250.122).

2. **Separate Neutral and Ground Bars:**
   - In the subpanel, **do not bond** the neutral and ground bars. They must remain isolated (unlike the main panel).

3. **Grounding Electrode Conductor (GEC):**
   - A separate GEC must connect the subpanel’s grounding system to a local grounding electrode (e.g., ground rod) at the detached garage.
   - Size the GEC per **Table 250.66** based on the largest ungrounded conductor in the feeder.
   - Example: For a 60A feeder with 6 AWG ungrounded conductors, use **8 AWG copper** (Table 250.66).

4. **Bonding the Subpanel Enclosure:**
   - The subpanel enclosure must be bonded to the EGC to ensure a low-impedance path for fault currents.

---

### Code Citations:
- **Section 250.32(B)(2):** Requires a separate GEC for detached structures.
- **Table 250.122:** Minimum EGC sizes for feeders.
- **Table 250.66:** Minimum GEC sizes based on feeder conductor size.
- **Section 250.4(A)(5):** Prohibits bonding neutral and ground in subpanels.

---

### Configuration Summary:
- **Feeder Conductors:** 4-wire (2 ungrounded, 1 grounded, 1 EGC).
- **Subpanel Neutral Bar:** Connected only to the grounded (neutral) conductor from the feeder.
- **Subpanel Ground Bar:** Connected to the EGC (from feeder) and the local GEC (to grounding electrode).
- **No Bonding:** Neutral and ground bars in the subpanel must remain isolated.

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 4.9s

**Tools Called:** cec_search, cec_search

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
1. **Main Bonding Jumper**  
   - **Definition**: Connection between the grounded circuit conductor and the equipment grounding conductor **at the service** (CEC 2022 Section 100).  
   - **Purpose**: Bonds the grounded conductor (neutral) to the equipment grounding system at the service point.  

2. **System Bonding Jumper**  
   - **Definition**: Connection between the grounded conductor and the supply-side bonding jumper or equipment grounding conductor **at a separately derived system** (CEC 2022 Section 100).  
   - **Purpose**: Bonds the grounded conductor of a separately derived system (e.g., transformer secondary, generator) to its equipment grounding system.  

---

### **Key Differences**
| **Aspect**                | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|---------------------------|--------------------------------------------------|--------------------------------------------------|
| **Location**              | Installed **at the service** (service equipment). | Installed **at a separately derived system** (e.g., transformer, generator). |
| **Application**           | Bonds grounded conductor to equipment grounding at the service. | Bonds grounded conductor to equipment grounding at a separately derived system. |
| **Sizing Reference**      | Table 250.102(C)(1), based on largest service conductor. | Table 250.102(C)(1), based on largest conductor in the derived system. |

---

### **When Each is Required**
1. **Main Bonding Jumper**  
   - **Required at every service** (CEC 2022 Section 250.28).  
   - Must be sized per **Table 250.102(C)(1)** based on the largest ungrounded service conductor.  
   - Example: For a service with 4/0 copper ungrounded conductors, the main bonding jumper must be **4 AWG copper** (see Table 250.102(C)(1)).  

2. **System Bonding Jumper**  
   - **Required at every separately derived system** (CEC 2022 Section 250.28).  
   - Sized per **Table 250.102(C)(1)** based on the largest ungrounded conductor in the derived system.  
   - Example: For a separately derived system with 3/0 aluminum ungrounded conductors, the system bonding jumper must be **4/0 AWG aluminum** (Table 250.102(C)(1)).  

---

### **Material and Installation Requirements**
- Both jumpers must be:  
  - **Material**: Copper, aluminum, copper-clad aluminum, or corrosion-resistant material (CEC 2022 Section 250.28(A)).  
  - **Attachment**: Connected per CEC 250.8 (e.g., pressure connectors, exothermic welding).  
  - **Size**: Minimum size per Table 250.102(C)(1) (see examples above).  

---

### **Inspector Notes**
- **Main bonding jumpers** are **not required** at separately derived systems (use system bonding jumpers instead).  
- **System bonding jumpers** are **not required** at service equipment (use main bonding jumpers instead).  
- Both jumpers must be **unspliced** and installed per CEC 250.28(C) and 250.102(E).  

[OK] Source: CEC 2022 Sections 100, 250.28, 250.102, Table 250.102(C)(1)

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 4.2s

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

**1. Required Number of Circuits:**
- **Minimum Requirement**: **Two or more 20-ampere small-appliance branch circuits** are required for all receptacle outlets in kitchens, including countertop surfaces (Section 210.52(B)(1)).  
- **Source**: CEC 2022 Section 210.11(C)(1) and 210.52(B)(1).

**2. Serving Dining Room Receptacles:**
- **Permitted**: Yes, the small-appliance branch circuits serving the kitchen **may also supply receptacles in the dining room** (Section 210.52(B)(1)).  
- **Condition**: The circuits can serve "other rooms specified in 210.52(B)(1)" (e.g., dining rooms), but **no small-appliance branch circuit shall serve more than one kitchen**.  

**Key Code Citations**:
- **Section 210.52(B)(1)**: Explicitly allows small-appliance branch circuits to serve dining room receptacles.
- **Section 210.11(C)(1)**: Mandates a minimum of two 20-ampere circuits for small-appliance loads in kitchens.

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 5.8s

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   12 AWG THHN copper at 90°C = **30A** (Table 310.16)

2. **Temperature Correction**:  
   50°C ambient → 0.82 correction factor (Table 310.15(B)(1)(1))  
   30A × 0.82 = **24.6A**

3. **Bundling Adjustment**:  
   6 conductors → 0.8 correction factor (Table 310.15(C)(1))  
   24.6A × 0.8 = **19.68A**

4. **Final Adjusted Ampacity**:  
   **19.7A** (rounded to one decimal place)

**Key References**:  
- Base ampacity: Table 310.16  
- Temperature correction: Table 310.15(B)(1)(1)  
- Bundling adjustment: Table 310.15(C)(1)  

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 5.6s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection Requirements in Dwelling Units (CEC 2022)

### **Why AFCI Protection is Required**
The California Electrical Code (CEC 2022), following NEC requirements, mandates **arc-fault circuit interrupter (AFCI)** protection for 15- and 20-ampere branch circuits in dwelling units (bedrooms, living rooms, etc.) to **prevent electrical fires caused by arc faults** (Section 210.12(A)). 

### **Electrical Hazard Prevented**
AFCIs detect **series arcs** (high-resistance arcs) that occur in damaged or degraded wiring, such as:
- Frayed or damaged cords
- Loose connections
- Overloaded circuits
- Deteriorated insulation

These arcs generate **localized high heat** (up to 10,000°F) capable of igniting nearby combustible materials (e.g., wood, fabric). Unlike standard circuit breakers, AFCIs distinguish between harmless arcs (e.g., from switches) and dangerous arcs, interrupting the circuit to prevent fires.

---

### **Key Code Requirements**
- **Scope**: Applies to all 120V, single-phase circuits in **bedrooms, living rooms, kitchens, hallways, etc.** (Section 210.12(A)).
- **Protection Methods**: Requires one of six approved configurations (e.g., combination-type AFCIs at the panel or outlet branch-circuit AFCIs at the first outlet).
- **Exceptions**: 
  - Fire alarm circuits in metal raceways (Section 210.12(A) Exception).
  - Short extensions (≤6 ft) without additional outlets (Section 210.12(D)).

---

### **Technical Basis**
- **UL 1699 Standard**: Defines AFCI performance requirements to detect arcing faults while avoiding nuisance tripping.
- **NFPA 70E**: Recognizes arc faults as a leading cause of electrical fires in residential settings.

---

[OK] Source: CEC 2022 Section 210.12, UL 1699, and NFPA 70E

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 4.6s

**Tools Called:** cec_search

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

Torque specifications are critical for ensuring **secure, low-resistance electrical connections** in panels and equipment. Improper torque can lead to:
- Loose connections causing arcing and overheating
- Excessive tightening damaging terminals or conductors
- Violations of code requirements for safe operation

### Requirements Location in CEC 2022
**Primary requirement**:  
**Section 110.14(D)** - *Terminal Connection Torque*  
- Mandates torque values be **as indicated on equipment** or in manufacturer instructions  
- Requires use of **approved torque tools** or methods (e.g., shear bolts, breakaway devices)  
- Informational notes reference:  
  - UL 486A-486B for default torque values  
  - NFPA 70B for maintenance guidance  

**Supplemental requirement**:  
**Section 430.9(C)** - *Control Circuit Devices*  
- Requires **minimum 0.8 N·m (7 lb-in.)** torque for screw-type terminals with 14 AWG or smaller copper conductors  

---

### Key Code Language from 110.14(D)
> "Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer. An approved means shall be used to achieve the indicated torque value."

**Informational Notes**:
1. Approved methods include torque tools, shear bolts, or breakaway devices with visual indicators.
2. Contact manufacturers if torque values are not marked on equipment.
3. Refer to UL 486A-486B and NFPA 70B for additional guidance.

---

### Practical Implications
- **Always verify torque values** on equipment nameplates or in documentation.
- Use **calibrated torque tools** to avoid over/under-tightening.
- Follow **manufacturer-specific instructions** for specialty equipment.

[OK] Source: CEC 2022 Sections 110.14(D), 430.9(C)

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 19.9s

**Tools Called:** cec_search

**Answer:**

## Service Load Calculation (CEC 2022)

### Step 1: General Lighting Load  
**3000 sq ft × 3 VA/sq ft = 9000 VA**  
*(CEC 220.12(A))*

### Step 2: Small Appliance Circuits  
**2 circuits × 1500 VA = 3000 VA**  
*(CEC 220.52)*

### Step 3: Laundry Circuit  
**1 circuit × 1500 VA = 1500 VA**  
*(CEC 220.52)*

### Step 4: Electric Range  
**12 kW × 0.67 demand factor = 8000 VA**  
*(CEC Table 220.55, Column C for 12 kW)*

### Step 5: Dryer Load  
**5.5 kW = 5000 VA + (500 VA × 0.5) = 5250 VA**  
*(CEC 220.54)*

### Step 6: Air Conditioner (Continuous Load)  
**4600 VA × 1.25 = 5750 VA**  
*(CEC 220.18(B) for continuous loads)*

---

### Total Calculated Load  
**9000 + 3000 + 1500 + 8000 + 5250 + 5750 = 32,500 VA**  

### Convert to Amperes  
**32,500 VA ÷ 240 V = 135.4 A**  

---

### Final Verification  
- **200A panel rating** exceeds calculated load of **135.4A**  
- **No exceptions apply** (not a school, restaurant, or existing load calculation)  
- **All loads accounted for per CEC 220.52–220.55**  

[OK] **Conclusion**: The 200A panel is adequately sized.  

[OK] Source: CEC 2022

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 6.0s

**Tools Called:** cec_search

**Answer:**

## Electrical Panel Working Space Violations (CEC 2022)

**1. Insufficient Working Space Depth**  
- **Measured**: 28 inches  
- **Required**: 42 inches (3 ft 6 in.) for 151–600V equipment under **Condition 2** (exposed live parts on one side, grounded parts on the other).  
- **Citation**: CEC Table 110.26(A)(1)  

**2. Insufficient Working Space Height**  
- **Measured**: 5 feet  
- **Required**: 6.5 feet (2.0 m) unless in an existing dwelling with ≤200A service (not specified here).  
- **Citation**: CEC 110.26(A)(3)  

**3. Obstruction in Working Space**  
- **Issue**: Water heater located 16 inches from the panel violates the requirement for **clear, unobstructed space** in front of the panel.  
- **Citation**: CEC 110.26(A)(3) (working space must be clear for safe operation).  

**4. Panel Mounting Height**  
- **Issue**: Panel mounted at 5 feet height may restrict access to the full 6.5-foot working space height requirement.  
- **Citation**: CEC 110.26(A)(3)  

---

**Inspector Note**:  
- The water heater must be relocated **at least 42 inches away** from the panel to comply with depth requirements.  
- The panel must be raised to **6.5 feet** or the working space extended vertically.  
- Ensure no storage or obstructions exist within the required working space.  

[OK] Source: CEC 2022

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 9.9s

**Tools Called:** cec_search

**Answer:**

## Circuit Protection Requirements for New Residential Kitchen (NEC 2023)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **Combination AFCI/GFCI Breaker**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI protection required for all 125V–250V receptacles serving countertop surfaces.  
  - **210.12(A)(1)**: AFCI protection required for all branch circuits in dwelling units (no exception for countertops).  

---

### 2. **Dishwasher (Dedicated 15A Circuit)**
- **Protection Required**: **GFCI + AFCI**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI protection required if the dishwasher is connected via a receptacle. If hardwired, GFCI may not apply (see **422.5(B)** for appliance-specific exceptions).  
  - **210.12(A)(1)**: AFCI required unless the circuit is dedicated to a specific appliance listed in exceptions (dishwasher is **not** listed).  

---

### 3. **Garbage Disposal (Dedicated 15A Circuit)**
- **Protection Required**: **GFCI + AFCI**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI required if connected via a receptacle. If hardwired, GFCI may not apply (see **422.5(B)**).  
  - **210.12(A)(1)**: AFCI required (no exception for garbage disposals).  

---

### 4. **Refrigerator (Dedicated 20A Circuit)**
- **Protection Required**: **AFCI Only**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI **not required** for refrigerators (exception for "specific appliances" in **210.8(A)(10)**).  
  - **210.12(A)(1)**: AFCI required (no exception for refrigerators).  

---

### Key Notes:
- **GFCI Exceptions**: Appliances like refrigerators are exempt from GFCI if they are **permanently hardwired** and not connected via a receptacle (NEC 210.8(A)(10)).  
- **AFCI Exceptions**: Only circuits for **ranges, ovens, water heaters, and space heaters** are exempt from AFCI (NEC 210.12(A)(1)).  
- **Combination AFCI/GFCI Breakers**: Required for countertop circuits to satisfy both protections simultaneously.  

[OK] Source: NEC 2023

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 6.9s

**Tools Called:** cec_search

**Answer:**

## Subpanel Bonding Violations and Correct Configuration (CEC 2022)

### **Identified Violations**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation**: CEC 250.142(B) requires **separate neutral and ground bars** in subpanels (not service panels). Bonding them creates parallel paths for neutral current, risking equipment damage and shock hazards.  
   - **Inspector Note**: (1) explicitly bonds neutral and ground bars with a main bonding jumper, which is **only permitted in the main service panel**.

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: CEC 250.142(B) mandates the **neutral bar must not be bonded to the enclosure** in subpanels. This creates an unintended ground path for neutral current.  
   - **Inspector Note**: (3) bonds the neutral bar to the metal enclosure, violating this rule.

3. **Ground Bar Bonded to Enclosure via Multiple Paths**  
   - **Violation**: While bonding the ground bar to the enclosure (2) is correct, **multiple bonds** (e.g., ground bar to enclosure and neutral bar to enclosure) create redundant paths for fault current, violating CEC 250.142(B).

---

### **Correct Configuration**
1. **Separate Neutral and Ground Bars**  
   - **Neutral Bar**: Connect only the **feeder neutral conductor** (from main panel). Do **not bond** to ground bar or enclosure.  
   - **Ground Bar**: Connect:  
     - **Feeder ground conductor** (from main panel).  
     - **Grounding electrode conductor (GEC)** (to local grounding electrode in detached garage).  

2. **Metal Enclosure Bonding**  
   - Bond the **ground bar to the metal enclosure** (2) per CEC 250.104(B).  
   - **Do not bond the neutral bar to the enclosure** (3 is incorrect).  

3. **Main Bonding Jumper**  
   - **Remove the main bonding jumper** in the subpanel. This is only required in the **main service panel** (CEC 250.24(B)).  

4. **Feeder Connections**  
   - **Feeder Neutral**: Connect to the **neutral bar** (no bond to ground).  
   - **Feeder Ground**: Connect to the **ground bar** (with GEC also connected).  

---

### **Code Citations**
- **CEC 250.24(B)**: Requires the main bonding jumper only in the service disconnecting means.  
- **CEC 250.142(B)**: Prohibits bonding neutral and ground in subpanels; mandates separate bars.  
- **CEC 250.104(B)**: Requires bonding the metal enclosure to the grounding system.  

[OK] Source: CEC 2022

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 4.3s

**Tools Called:** cec_lookup_conduit_fill

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Calculation Steps:**

1. **Conduit Total Area**  
   - RMC 1¼" = **1.526 in²** (Chapter 9 Table 4)  
   - 40% fill limit = **0.61 in²** (Chapter 9 Table 1)  

2. **Conductor Area**  
   - 10 AWG THHN = **0.0211 in²** (Chapter 9 Table 5)  

3. **Maximum Conductors**  
   - $ \frac{0.61\ \text{in²}}{0.0211\ \text{in²/conductor}} = 28.91 $  
   - **28 conductors** (round down per NEC 300.15(B)(2)(a))  

**Verification:**  
- 28 conductors × 0.0211 in² = **0.5908 in²** (4.1% of conduit area)  
- 29 conductors would exceed 40% fill (0.6119 in² > 0.61 in²).  

**Answer:**  
**28 conductors** is the maximum number of 10 AWG THHN permitted in 1¼" RMC.  

[OK] Source: CEC 2022 Chapter 9 Tables 4, 5, and 1.

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 14.6s

**Tools Called:** python_calculator, python_calculator, cec_search

**Answer:**

## Voltage Drop Verification (CEC 2022)

1. **Code Reference**:
   - **Section 210.19(A) Informational Note No. 3**: Recommends voltage drop limits for efficiency:
     - **Branch circuit only**: ≤ 3% (our result: 2.37% ✓)
     - **Feeder + branch circuit**: ≤ 5%

2. **Special Cases**:
   - **Section 647.4(D)** applies to technical equipment systems (e.g., healthcare facilities) with stricter 1.5% limit, but this is **not applicable** to general branch circuits.

3. **Conclusion**:
   - The 2.37% voltage drop **meets NEC/CEC recommendations** for standard branch circuits.
   - No code violation exists for this installation.

[OK] Source: CEC 2022 Sections 210.19, 647.4

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 5.6s

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG TW copper at 60°C: **20A** (Table 310.16)

**Step 2: Temperature Correction**  
Ambient 43°C → 60°C conductor:  
**×0.71** (Table 310.15(B)(1)(1))

**Step 3: Bundling Adjustment**  
6 current-carrying conductors:  
**×0.80** (Table 310.15(C)(1))

**Final Calculation**:  
20A × 0.71 × 0.80 = **11.36A**

**Answer**:  
Adjusted ampacity = **11.36 amperes** after applying both correction factors.

[OK] Source: CEC 2022

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 6.5s

**Tools Called:** cec_lookup_grounding_conductor

**Answer:**

## Minimum Size Copper GEC for Parallel Service Conductors (CEC 2022)

**Equivalent Service Conductor Size**: 1000 kcmil copper (4 × 250 kcmil parallel conductors)  
**Minimum Copper GEC Size**: **2/0 AWG**  

**Calculation Basis**:  
- Per CEC Table 250.66, for service conductors **over 600 kcmil through 1100 kcmil**, the required copper GEC is **2/0 AWG**.  
- Footnote [1] confirms parallel conductor sums are valid for equivalent size determination.  

**California Amendment**: Δ symbol indicates California-specific adjustments to the base NEC.  

[OK] Source: CEC 2022 Table 250.66

---

