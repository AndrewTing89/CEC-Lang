# Core (NEC) Evaluation Results - Run 1

**Date:** 2025-12-10
**Prompt Version:** v4 - no hardcoded values

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 28 |
| Successful | 28 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 293.3s |
| Avg Duration | 10.5s |
| Exception Search Used | 0/28 |
| NEC Comparison Forced | No |

## Results by Question

### baseline-001

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Duration:** 5.0s | **Exception Search:** No

**Tools Called:** cec_lookup_conductor_ampacity

**Answer:**

## 12 AWG Copper Conductor Ampacity (CEC 2022)

**Ampacity**: 25 amperes at 75°C (CEC Table 310.16)  
**Overcurrent Protection Limit**: 20 amperes (CEC 240.4(D))

[OK] Source: CEC 2022 Table 310.16 and 240.4(D)

---

### Key Notes:
1. **Base Ampacity**: 25A from Table 310.16 for 12 AWG copper at 75°C  
2. **Limiting Rule**: Section 240.4(D) restricts overcurrent protection to **20A maximum** for 12 AWG copper conductors  
3. **California Amendment**: No modification to NEC Table 310.16 values in this case  

Always verify ambient temperature and conductor bundling conditions using Sections 310.15(B) and 310.15(C)(1) if applicable.

---

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 4.1s | **Exception Search:** No

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## 60A Circuit Conductor Sizing (CEC 2022)

**Required Conductor Size**: **6 AWG copper**  
- **Ampacity**: 65A at 75°C (CEC Table 310.16)  
- **Overcurrent Protection**: Maximum 65A (CEC 240.4(D))  

**Key Steps**:  
1. **Base Requirement**: 60A circuit requires conductor with **≥60A ampacity**  
2. **Table 310.16 Lookup**:  
   - 6 AWG copper = 65A (75°C column) ✅  
   - 8 AWG copper = 50A (insufficient) ❌  
3. **Limiting Rule Check**:  
   - CEC 240.4(D) allows 65A OCP for 6 AWG copper (matches requirement)  

**California Amendment Note**: No modifications to NEC Table 310.16 values in CEC 2022 for this application.  

[OK] Source: CEC 2022 Table 310.16 and 240.4(D)

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 14.9s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**Required Locations**:  
1. **All 120V, 15- and 20-ampere receptacles** installed to serve **countertop surfaces** (CEC 210.8(A)(6)).  
2. **Receptacles within 6 feet of a sink** (CEC 210.8(A)(7) and 210.52(C)(5)).  
3. **At least two 20-amp small-appliance branch circuits** must supply countertop receptacles, both with GFCI protection (CEC 210.52(C)(5)).  

**Key Code References**:  
- **CEC 210.8(A)(6)**: Mandates GFCI protection for all kitchen countertop receptacles.  
- **CEC 210.8(A)(7)**: Requires GFCI protection for receptacles within 6 feet of a sink.  
- **CEC 210.52(C)(5)**: Specifies two 20-amp circuits for kitchen countertop loads, both requiring GFCI.  

**California Amendment Note**:  
- No modifications to NEC 210.8(A)(6) in CEC 2022 – follows NEC requirements.  

**Exceptions**:  
- None for standard residential kitchens (Exceptions in 210.8(A)(6) do not apply to kitchens).  

[OK] Source: CEC 2022 Sections 210.8(A)(6), 210.8(A)(7), and 210.52(C)(5)

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 4.3s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Yes**, AFCI protection is **required** for bedroom circuits in new residential construction.  

### Key Requirements:
1. **Scope**:  
   - All **120V, 15- and 20-ampere branch circuits** in dwelling unit **bedrooms** must have AFCI protection (CEC 210.12(A)).  
   - Applies to **outlets and devices** in bedrooms, including receptacles, lighting, and other 120V loads.  

2. **Protection Methods**:  
   - **Combination-type AFCI** at the circuit origin (breaker panel).  
   - **Outlet branch-circuit-type AFCI** at the first outlet, combined with a standard breaker (if conditions in 210.12(A)(4) are met).  
   - **Branch/feeder-type AFCI** with outlet AFCI (per 210.12(A)(2)).  

3. **Exceptions**:  
   - **None** for standard bedroom circuits.  
   - Fire alarm circuits (covered under 760.41(B)) are exempt but not applicable to general bedroom wiring.  

### Code References:
- **CEC 210.12(A)**: Mandates AFCI protection for bedrooms.  
- **No California amendments**: CEC 2022 follows NEC 2020 without modification for this requirement.  

[OK] Source: CEC 2022 Section 210.12(A)

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 10.7s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Yes**, aluminum conductors **can be used** for a 200A service in California. The required size is **4/0 AWG aluminum**.

---

### **Key Code References**
1. **Conductor Sizing**:  
   - **CEC Table 310.12(A)** specifies minimum service conductor sizes for single-phase dwelling services.  
   - For a **200A service**, **4/0 AWG aluminum** is required (ampacity = 200A at 75°C).  

2. **Overcurrent Protection**:  
   - **CEC 240.4(D)** limits overcurrent protection for aluminum conductors:  
     - **4/0 AWG aluminum** is permitted with a **maximum 200A breaker** (no derating required for service conductors).  

3. **California Amendments**:  
   - No modifications to NEC Table 310.12(A) in CEC 2022 for this application.  

---

### **Calculation Verification**
- **Base Requirement**: 200A service requires conductors with **≥200A ampacity**.  
- **Table 310.12(A)**:  
  - 4/0 AWG aluminum = 200A (75°C column) ✅  
  - 3/0 AWG aluminum = 170A (insufficient) ❌  
- **Limiting Rule Check**:  
  - CEC 240.4(D) confirms 200A OCP is allowed for 4/0 AWG aluminum.  

---

### **Grounding Electrode Conductor (GEC) Size**
- Use **Table 250.66** for GEC sizing based on service conductor size:  
  - **4/0 AWG aluminum service conductor** → **2 AWG aluminum GEC** (or 4 AWG copper).  

---

**[OK] Source**: CEC 2022 Table 310.12(A), 240.4(D), and 250.66

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 7.6s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Minimum Working Clearance Depth (CEC 2022)

**Minimum depth required**: **30 inches (762 mm)** in front of a 120/240V residential panel.

---

### **Code Basis**
1. **CEC Table 110.26(A)(1)** specifies working space depths based on voltage and conditions:
   - For **voltage to ground ≤ 250V** (120/240V system) under **Condition 1** (exposed live parts on one side, no live/grounded parts on the other), the minimum depth is **30 inches**.

2. **Condition 1** (CEC 110.26(A)(1)):  
   - Applies to residential panels where live parts are exposed on one side and no live/grounded parts are on the other.  
   - **30 inches** is the standard depth for systems ≤ 250V.

---

### **California Amendments**
- **No modifications** to NEC Table 110.26(A)(1) in CEC 2022.  
- Follows NEC 2020 requirements directly.

---

### **Exceptions**
- **None** for standard residential panels.  
- If the panel has live parts on both sides (Condition 3), depth increases to **36 inches**, but this is not typical for residential applications.

---

**[OK] Source**: CEC 2022 Table 110.26(A)(1) and 110.26(A)(1)

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 7.7s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Minimum Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Answer**: **2** dedicated 20-ampere small appliance branch circuits are required for a kitchen in residential construction.

---

### **Code Basis**
1. **CEC 210.11(C)(1)**:  
   - Mandates **two or more 20-ampere small-appliance branch circuits** for all receptacle outlets in kitchens, pantries, breakfast rooms, and dining rooms.  
   - These circuits must serve **all wall, countertop, and floor receptacles** in these areas (per 210.52(B)(1)).  

2. **CEC 210.52(B)(1)**:  
   - Specifies that small-appliance circuits must **not serve any other outlets** (e.g., laundry, bathroom, or general lighting).  
   - **Exceptions**:  
     - A receptacle for a specific appliance (e.g., refrigerator) may be on an individual circuit (Exception No. 2).  

3. **Load Calculation**:  
   - Each small-appliance circuit is calculated at **1,500 VA** (CEC 220.52(A)).  
   - Two circuits = **3,000 VA** minimum load for kitchen small appliances.  

---

### **California Amendments**
- **No modifications** to NEC 2020 requirements for small-appliance circuits in kitchens.  
- Follows NEC 210.11(C)(1) and 210.52 directly.  

---

### **Key Notes**
- **Coverage**: Includes countertop, wall, and floor receptacles in kitchens.  
- **Exclusions**: Built-in appliances (e.g., ovens) require separate circuits (per 210.52(B)(1)).  

---

**[OK] Source**: CEC 2022 Sections 210.11(C)(1), 210.52(B)(1), and 220.52(A)

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 8.1s | **Exception Search:** No

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for 200A Residential Service (NEC 2023)

**Answer**: **Yes**, surge protection is required for a new **200A residential service** under **NEC 2023**.

---

### **Code Basis**
1. **NEC 230.66**:  
   - **Mandates surge-protective devices (SPDs)** for services rated **100A or more**.  
   - Applies to **all new residential services** (including 200A).  
   - SPD must be **listed** and installed per **UL 1449** (Standard for Surge Protective Devices).  

2. **NEC 230.67(A)**:  
   - Requires SPDs for **dwelling units** (residential services).  
   - Explicitly includes **residential services** in the scope.  

---

### **Installation Requirements**
- **Location**: SPD must be installed **at the service point** (near the service disconnect).  
- **Connections**:  
  - Connected to the **grounded (neutral) conductor** and **grounding electrode system** (per 250.4(A)(1)).  
- **Exceptions**: None for residential services ≥100A.  

---

### **Key Notes**
- **Purpose**: Protects against transient overvoltages (e.g., lightning, utility switching).  
- **Compliance**: SPD must be **listed** and installed per manufacturer instructions.  
- **Existing Services**: Not required unless modified (NEC 90.5(B)).  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 230.66/230.67 in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

**[OK] Source**: NEC 2023 Sections 230.66 and 230.67(A)

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 11.9s | **Exception Search:** No

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size

**Answer:**

## Service Conductor Sizing for 200A Residential Upgrade (CEC 2022)

### **Required Conductor Sizes**
- **Copper**: **2/0 AWG** (per CEC Table 310.12(A))
- **Aluminum**: **4/0 AWG** (per CEC Table 310.12(A))

---

### **Code Basis**
1. **CEC Table 310.12(A)**:  
   - Specifies conductor sizes for **single-phase dwelling services**.  
   - For **200A service**, the minimum sizes are:  
     - **Copper**: 2/0 AWG (75°C column)  
     - **Aluminum**: 4/0 AWG (75°C column)  

2. **Allowable Use of Aluminum**:  
   - **Permitted** for service conductors under CEC 310.12(A) **if sized per the table**.  
   - Aluminum must be **listed for use in service entrance applications** (e.g., AA-8000 series).  

---

### **Key Considerations**
1. **Temperature Rating**:  
   - Use **75°C-rated conductors** (standard for service entrance conductors).  
   - Verify insulation type (e.g., THWN-2, XHHW-2) matches the 75°C rating.  

2. **Load Calculation**:  
   - Your appliances (12kW range, 5.5kW dryer, 4.5kW water heater) are **within 200A service capacity**.  
   - CEC 220.54 and 220.55 apply for range and dryer loads, but **200A service is standard** for homes with these appliances.  

3. **California Amendments**:  
   - **No restrictions** on aluminum for service conductors in CEC 2022.  
   - Follows NEC 310.12(A) directly.  

---

### **Final Answer**
- **Service Conductors**:  
  - **Copper**: 2/0 AWG (200A at 75°C)  
  - **Aluminum**: 4/0 AWG (200A at 75°C)  
- **Aluminum Use**: **Allowed** if conductors are **listed for service entrance** and sized per Table 310.12(A).  

---

**[OK] Source**: CEC 2022 Table 310.12(A) and 310.15(B)(16)

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 11.3s | **Exception Search:** No

**Tools Called:** nec_search

**Answer:**

## Multiwire Branch Circuit Requirements for Kitchen Receptacles (NEC 2023)

### **Circuit Breaker Requirements**
1. **Two-Pole Breaker with Handle Tie or Common Trip**:  
   - **NEC 210.4(B)**: Multiwire branch circuits (MWBCs) must use a **two-pole breaker** with a **handle tie** or **common-trip device** to ensure both ungrounded (hot) conductors are disconnected simultaneously.  
   - **Purpose**: Prevents the neutral from carrying the full load of one circuit if the other is de-energized.  

2. **Breaker Rating**:  
   - **20A** for 12 AWG copper conductors (per NEC 240.4(D)).  

---

### **Neutral Termination Requirements**
1. **Neutral Conductor Sizing**:  
   - **12 AWG** (same size as hots) to carry the **maximum unbalanced load** (NEC 210.4(B)).  
   - **Prohibited**: Reducing the neutral size (e.g., using 14 AWG) for MWBCs.  

2. **Neutral Termination**:  
   - Must be connected to the **neutral bus** in the panel.  
   - **No shared neutrals** with other circuits (NEC 210.52(B)(1)).  

3. **Grounding Conductor**:  
   - **12 AWG** (same size as hots) for equipment grounding (NEC 250.146).  
   - Must terminate on the **equipment grounding conductor (EGC) bus**.  

---

### **Key Code References**
1. **NEC 210.4(B)**:  
   - Mandates handle ties or common-trip breakers for MWBCs.  
   - Requires neutral to be sized for the maximum unbalanced load.  

2. **NEC 210.52(B)(1)**:  
   - Kitchen small-appliance circuits must be **dedicated** and **not share neutrals** with other circuits.  

3. **NEC 240.4(D)**:  
   - 12 AWG copper conductors require **20A overcurrent protection**.  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 210.4(B) or 210.52(B)(1).  
- Follows NEC 2023 requirements directly.  

---

### **Summary**
- **Breaker**: 20A two-pole with handle tie or common trip.  
- **Neutral**: 12 AWG, sized for unbalanced load, not shared with other circuits.  
- **Grounding**: 12 AWG, connected to EGC bus.  

**[OK] Source**: NEC 2023 Sections 210.4(B), 210.52(B)(1), and 240.4(D)

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 10.7s | **Exception Search:** No

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

### **Required Locations (NEC 210.8(A))**
1. **Bathrooms**  
2. **Garages and accessory buildings** (floor at or below grade level)  
3. **Outdoors**  
4. **Crawl spaces** (at or below grade level)  
5. **Kitchens**  
6. **Areas with sinks** (permanent provisions for food prep, beverage prep, or cooking)  
7. **Sinks** (receptacles within 6 ft of the top inside edge of the bowl)  
8. **Boathouses**  
9. **Bathtubs or shower stalls** (receptacles within 6 ft of the outside edge)  
10. **Laundry areas**  
11. **Indoor damp and wet locations**  

---

### **Key Code Basis**
- **NEC 210.8(A)**: Mandates GFCI protection for all listed locations in dwelling units.  
- **Exceptions**: Specific exceptions apply (e.g., receptacles for HVAC equipment, security systems), but the **11 locations above are standard requirements**.  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 210.8 in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

**[OK] Source**: NEC 2023 Section 210.8(A)

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 8.8s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Surge Protection Requirements for 200A Residential Service (CEC 2022)

### **Is Surge Protection Required?**
- **Yes, per CEC 2022 Section 230.67**:  
  - **All services supplying dwelling units** must include a **surge-protective device (SPD)**.  
  - This is a **California amendment** (not in NEC) and applies to **all new residential services**.  

---

### **Installation Requirements**
1. **SPD Type**:  
   - Must be **Type 1 or Type 2 SPD** (per CEC 230.67(C)).  
   - **Type 1**: Installed at the service entrance (e.g., main panel).  
   - **Type 2**: Installed downstream (e.g., subpanels, branch circuits).  

2. **Location**:  
   - **Primary Location**: Must be an **integral part of the service equipment** or **immediately adjacent** (CEC 230.67(B)).  
   - **Alternative**: If not in the service equipment, the SPD must be installed at the **next level distribution equipment downstream** (e.g., subpanel).  

3. **Supply-Side Installation**:  
   - Permitted on the **supply side of the service disconnect** if:  
     - It is a **Type 1 SPD** (CEC 230.94, Exception No. 2).  
     - Installed per manufacturer instructions.  

---

### **Code Basis**
- **CEC 2022 Section 230.67**:  
  - Mandates SPDs for all dwelling unit services.  
  - Specifies SPD type, location, and replacement requirements.  
- **CEC 2022 Section 230.94**:  
  - Allows SPDs to be installed on the supply side of the service disconnect if they are Type 1.  

---

### **Key Exceptions**
- **Downstream SPDs**:  
  - If the SPD is not in the service equipment, it must be located at the **next level distribution equipment** (e.g., a subpanel).  
- **Supply-Side SPDs**:  
  - Type 1 SPDs may be installed on the supply side of the service disconnect (per Exception No. 2 in 230.94).  

---

### **Summary**
- **Required**: Surge protection (SPD) for all new residential services in California.  
- **Options**:  
  - **Type 1 SPD** at the service entrance (main panel).  
  - **Type 2 SPD** at subpanels or branch circuits.  
- **Prohibited**: Installing SPDs in locations that violate the "next level downstream" rule unless permitted by exceptions.  

**[OK] Source**: CEC 2022 Sections 230.67 and 230.94

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 28.5s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Working Space Requirements for Electrical Panels (CEC 2022 / NEC 2023)

### **Front Clearance**
- **Service Equipment (Main Panel)**:  
  - **Minimum**: 36 inches (914 mm) per **CEC 110.26(A)(1)(b)**.  
  - **Provided**: 24 inches → **Fails requirement**.  
- **Panelboard (Subpanel)**:  
  - **Minimum**: 30 inches (762 mm) per **CEC 110.26(A)(1)(a)**.  
  - **Provided**: 24 inches → **Fails requirement**.  

---

### **Side Clearance**
- **Service Equipment**:  
  - **Minimum**: 30 inches (762 mm) of clear space on all sides per **CEC 110.26(A)(2)**.  
  - **Provided**: 18 inches to water heater → **Fails requirement**.  
- **Panelboard**:  
  - No specific side clearance, but must be **clear of obstructions** (per **CEC 110.26(A)(3)**).  
  - **Provided**: 18 inches to water heater → **Fails safe clearance**.  

---

### **Key Code References**
1. **CEC 110.26(A)(1)**:  
   - Specifies minimum working space depth:  
     - **36 inches** for service equipment.  
     - **30 inches** for panelboards.  
2. **CEC 110.26(A)(2)**:  
   - Requires **30 inches of clear space** on all sides of service equipment.  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 110.26.  
- Follows NEC 2023 requirements directly.  

---

### **Conclusion**
- **Front clearance**: 24 inches < required 36 inches (service equipment) or 30 inches (panelboard).  
- **Side clearance**: 18 inches < required 30 inches for service equipment.  
- **Result**: **Does not meet CEC/NEC requirements**.  

**[OK] Source**: CEC 2022 Sections 110.26(A)(1) and 110.26(A)(2)

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 9.1s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Code Violation for Multiple Conductors on a Breaker Terminal (CEC 2022)

### **Is This a Code Violation?**
- **Yes**, this is a **code violation** under **CEC 2022 Section 240.4(B)**.  
- **Key Rule**:  
  - **Each conductor must be securely connected to the terminal**.  
  - **Terminals not marked for multiple conductors** must have **only one conductor** per terminal.  

---

### **Code Analysis**
1. **Breaker Terminal Rating**:  
   - The breaker is **not marked for two conductors**.  
   - Per **CEC 240.4(B)**, terminals not marked for multiple conductors **must have only one conductor**.  

2. **Conductor Size**:  
   - 12 AWG copper is **permissible for a 20A circuit** (per **CEC 240.4(D)**).  
   - However, **conductor size alone does not override terminal limitations**.  

3. **Violation**:  
   - Two 12 AWG conductors on a terminal **not rated for two conductors** violates **CEC 240.4(B)**.  

---

### **Code Basis**
- **CEC 2022 Section 240.4(B)**:  
  > "Each conductor shall be securely connected to the terminal. Terminals not marked for multiple conductors shall have only one conductor."  
- **CEC 2022 Section 240.4(D)**:  
  > "The ampacity of the conductor shall not be less than the value required by 240.4(D)."  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 240.4(B) in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Corrective Action**
- **Replace the breaker** with one **marked for two conductors** (e.g., "2-wire" or "2-conductor" marked terminal).  
- **Or**: Use a **single conductor** per terminal.  

---

**[OK] Source**: CEC 2022 Section 240.4(B)

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 11.2s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

### **Key Requirements**
1. **Separate Neutral and Ground Buses**:  
   - **Neutral Bus**: Connect the **neutral conductor** from the 4-wire feeder to the **neutral bus**.  
   - **Grounding Bus**: Connect the **equipment grounding conductor (EGC)** from the feeder and the **grounding electrode conductor (GEC)** from the garage’s grounding electrode to the **grounding bus**.  
   - **No bonding jumper**: The neutral and grounding buses **must not be bonded** in the subpanel (per **CEC 250.24(D)**).  

2. **Grounding Electrode System**:  
   - A **separate grounding electrode** (e.g., ground rod) is required in the detached garage (per **CEC 250.32**).  
   - The **GEC** from the garage’s electrode must connect to the **grounding bus** in the subpanel.  

3. **Feeder Conductors**:  
   - The 4-wire feeder includes:  
     - Two ungrounded (hot) conductors.  
     - One grounded (neutral) conductor.  
     - One equipment grounding conductor (EGC).  

---

### **Step-by-Step Configuration**
1. **Subpanel Neutral Bus**:  
   - Connect the **neutral conductor** from the feeder to the **neutral bus**.  
   - **Do not bond** the neutral bus to the grounding bus.  

2. **Subpanel Grounding Bus**:  
   - Connect the **EGC** from the feeder to the grounding bus.  
   - Connect the **GEC** from the garage’s grounding electrode to the grounding bus.  

3. **Grounding Electrode (Garage)**:  
   - Install a **minimum 8 ft (2.4 m) ground rod** (per **CEC 250.52(A)(1)**).  
   - Size the **GEC** per **CEC Table 250.66** based on the feeder conductor size.  

---

### **Code Basis**
- **CEC 250.24(D)**:  
  - Requires the **grounding electrode conductor** to connect to the **grounding bus** in the subpanel.  
  - Prohibits bonding the neutral and grounding buses in the subpanel.  
- **CEC 250.32**:  
  - Mandates a **separate grounding electrode** for each detached structure.  
- **CEC 250.52(A)(1)**:  
  - Specifies grounding electrode requirements (e.g., ground rod size, depth).  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 250.24(D) or 250.32 in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Example Sizing (Based on Feeder Conductor Size)**
- **Feeder Conductors**: 6 AWG copper.  
  - **GEC Size**: 4 AWG copper (per **CEC Table 250.66**).  

---

### **Summary**
- **Neutral and ground buses must be separated** in the subpanel.  
- **Grounding electrode conductor** connects to the grounding bus.  
- **No bonding jumper** between neutral and ground in the subpanel.  
- **Ground rod** required in the detached garage.  

**[OK] Source**: CEC 2022 Sections 250.24(D), 250.32, and 250.52(A)(1)

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 15.1s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
1. **Main Bonding Jumper** (CEC 2022 Section 100):  
   - Connects the **grounded circuit conductor** (neutral) to the **equipment grounding conductor** at the **service equipment**.  
   - Ensures a single point of bonding in the service.  

2. **System Bonding Jumper** (CEC 2022 Section 100):  
   - Connects the **grounded conductor** of a **separately derived system** (e.g., transformer, generator, PV inverter) to the **equipment grounding conductor** or **supply-side bonding jumper**.  

---

### **Key Differences**

| **Feature**               | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|--------------------------|--------------------------------------------------|--------------------------------------------------|
| **Location**             | **Service equipment** (main panel)              | **Separately derived systems** (e.g., transformers, generators) |
| **Purpose**              | Bonds **neutral** to **equipment grounding conductor** at the service | Bonds **grounded conductor** to **equipment grounding conductor** in derived systems |
| **Required By**          | **CEC 250.24(D)**                                | **CEC 250.4(A)(5)**                              |
| **Sizing**               | Per **Table 250.102(C)(1)** based on service conductor size | Per **Table 250.102(C)(1)** based on derived system conductor size |

---

### **When Each Is Required**

#### **Main Bonding Jumper**
- **Required in all service equipment** (main panel) to connect the **neutral bus** to the **equipment grounding conductor** (EGC).  
- **Code Basis**:  
  - **CEC 250.24(D)**: "The grounded conductor shall be bonded to the equipment grounding conductor at the service."  
  - **CEC 250.28(D)**: Sizes the jumper based on the largest ungrounded service conductor.  

#### **System Bonding Jumper**
- **Required in separately derived systems** (e.g., transformers, generators, photovoltaic systems) to connect the **grounded conductor** of the derived system to the **equipment grounding conductor**.  
- **Code Basis**:  
  - **CEC 250.4(A)(5)**: "The grounded conductor of a separately derived system shall be connected to the equipment grounding conductor."  
  - **CEC 705.12(D)(2)**: For PV systems, the system bonding jumper is required at the inverter.  

---

### **Sizing Requirements**
- **Main Bonding Jumper**:  
  - Size per **Table 250.102(C)(1)** based on the **largest ungrounded service conductor**.  
  - Example: For a 200A service with 3/0 AWG conductors, the main bonding jumper must be **1/0 AWG copper**.  

- **System Bonding Jumper**:  
  - Size per **Table 250.102(C)(1)** based on the **largest ungrounded conductor** in the derived system.  
  - Example: For a 480V transformer with 1/0 AWG secondary conductors, the system bonding jumper must be **1/0 AWG copper**.  

---

### **Code Basis**
- **Main Bonding Jumper**:  
  - **CEC 250.24(D)**: Single point of bonding at the service.  
  - **CEC 250.28(D)**: Sizing requirements.  

- **System Bonding Jumper**:  
  - **CEC 250.4(A)(5)**: Required for separately derived systems.  
  - **CEC 250.102(C)(1)**: Sizing table.  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 250.24(D) or 250.4(A)(5) in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Example Scenarios**

#### **Main Bonding Jumper**
- **Application**: A 200A main service panel.  
- **Action**: Connect the neutral bus to the grounding bus using a **1/0 AWG copper** jumper (per Table 250.102(C)(1)).  

#### **System Bonding Jumper**
- **Application**: A 480V transformer with 1/0 AWG secondary conductors.  
- **Action**: Connect the transformer’s grounded conductor to the equipment grounding conductor using a **1/0 AWG copper** jumper.  

---

### **Summary**
- **Main Bonding Jumper**: Bonds neutral to ground **at the service** (required by **CEC 250.24(D)**).  
- **System Bonding Jumper**: Bonds grounded conductor to ground **in derived systems** (required by **CEC 250.4(A)(5)**).  

**[OK] Source**: CEC 2022 Sections 250.24(D), 250.4(A)(5), and Table 250.102(C)(1)

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 9.1s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

### **Number of Required Circuits**
- **Minimum Requirement**:  
  - **Two 20-ampere small appliance branch circuits** are required for the **kitchen** (per **CEC 210.11(C)(1)**).  
  - These circuits must serve **countertop receptacles**, **wall/floor receptacles**, and **refrigeration equipment** in the kitchen.  

---

### **Can These Circuits Serve Dining Room Receptacles?**
- **Yes**, the two small appliance branch circuits **can also serve dining room receptacles** (per **CEC 210.52(B)(1)**).  
- **Key Rule**:  
  - The circuits must **not serve more than one kitchen** (per **CEC 210.52(B)(1)**).  
  - Dining room receptacles are explicitly permitted to be on the same circuits as kitchen small appliance circuits.  

---

### **Code Basis**
1. **CEC 210.11(C)(1)**:  
   > "In addition to the number of branch circuits required by other parts of this section, two or more 20-ampere small-appliance branch circuits shall be provided for all receptacle outlets specified by 210.52(B)."  

2. **CEC 210.52(B)(1)**:  
   > "The two or more small-appliance branch circuits specified in 210.52(B)(1) shall have no other outlets... Additional small-appliance branch circuits shall be permitted to supply receptacle outlets in the kitchen and other rooms specified in 210.52(B)(1)."  

3. **CEC 220.52(A)**:  
   - Requires **1500 VA per small appliance branch circuit** for load calculations.  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 210.11(C)(1) or 210.52(B)(1) in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Example Configuration**
- **Kitchen**:  
  - Two 20-amp circuits for countertop, wall, and floor receptacles.  
- **Dining Room**:  
  - Receptacles (e.g., for a dining room table) must be on **one of the two kitchen circuits**.  

---

### **Summary**
- **Two 20-amp small appliance branch circuits** are required for the kitchen.  
- These circuits **can also serve dining room receptacles**.  
- **Prohibited**: Using these circuits for other areas (e.g., living rooms).  

**[OK] Source**: CEC 2022 Sections 210.11(C)(1), 210.52(B)(1), and 220.52(A)

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 11.2s | **Exception Search:** No

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Answer:**

## Adjusted Ampacity for 12 AWG THHN Conductors (CEC 2022)

### **Step-by-Step Calculation**

1. **Base Ampacity (Table 310.16)**:  
   - **12 AWG THHN** in the **90°C column** = **30A** (per CEC Table 310.16).  

2. **Ambient Temperature Correction (Table 310.15(B)(1)(1))**:  
   - **Ambient temperature**: 50°C.  
   - **Correction factor for 90°C insulation**: **0.82** (per CEC Table 310.15(B)(1)(1)).  

3. **Bundling Adjustment (Table 310.15(C)(1))**:  
   - **6 current-carrying conductors** in a single conduit.  
   - **Adjustment factor**: **0.80** (per CEC Table 310.15(C)(1)).  

4. **Final Calculation**:  
   ```
   Adjusted Ampacity = Base Ampacity × Temp Correction × Bundling Adjustment  
   = 30A × 0.82 × 0.80  
   = **19.68A**
   ```

---

### **Code Basis**
- **CEC 310.16**: Base ampacity for 12 AWG THHN.  
- **CEC 310.15(B)(1)(1)**: Ambient temperature correction for 50°C.  
- **CEC 310.15(C)(1)**: Bundling adjustment for 6 conductors.  
- **CEC 240.4(D)**: Overcurrent protection limit for 12 AWG conductors (20A maximum).  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 310.15(B)(1)(1) or 310.15(C)(1) in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Final Answer**
- **Adjusted Ampacity**: **19.68A** (rounded to **19.7A** for practical use).  
- **Overcurrent Protection**: Per **CEC 240.4(D)**, 12 AWG conductors are limited to **20A** overcurrent protection.  

**[OK] Source**: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1), and 240.4(D)

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 9.6s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## AFCI Protection in Bedrooms and Living Areas (CEC 2022)

### **Why AFCI Protection is Required**
- **Code Requirement**:  
  - **CEC 210.12(A)** mandates **AFCI protection** for all **120V, 15- and 20-ampere branch circuits** in dwelling units that supply outlets in **bedrooms, living rooms, family rooms, and similar areas**.  
  - This requirement is based on fire safety data showing arc faults are a leading cause of electrical fires in residential buildings.  

---

### **Electrical Hazard Prevented**
- **Arc Faults**:  
  - Arc faults occur when electrical current leaks through damaged or degraded insulation (e.g., frayed cords, loose connections, overloaded circuits), creating high-temperature arcs.  
  - These arcs can ignite nearby combustible materials (e.g., wood, paper, fabric), leading to **electrical fires**.  

- **AFCI Function**:  
  - Detects **series arcs** (e.g., in damaged cords) and **parallel arcs** (e.g., between hot and neutral).  
  - Interrupts the circuit **before** the arc generates enough heat to start a fire.  

---

### **Code Basis**
1. **CEC 210.12(A)**:  
   > "All 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets or devices installed in dwelling unit kitchens, family rooms, dining rooms, living rooms, bedrooms, and similar areas shall be protected by a listed combination-type arc-fault circuit interrupter."  

2. **CEC 100 (Definition of AFCI)**:  
   > An AFCI is a device that "recognizes characteristics unique to arcing and functions to de-energize the circuit when an arc fault is detected."  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 210.12 in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Key Differences from GFCI**
- **GFCI** protects against **shock hazards** (ground faults).  
- **AFCI** protects against **fire hazards** (arc faults).  

---

### **Summary**
- **Requirement**: AFCI protection for bedrooms and living areas to prevent **electrical fires** caused by arc faults.  
- **Hazard Mitigated**: Fires from damaged wiring, loose connections, or overloaded circuits.  

**[OK] Source**: CEC 2022 Sections 210.12 and 100

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 9.1s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

### **Why Torque Specifications Are Important**
1. **Prevent Overheating and Fires**:  
   - Improper torque (over- or under-tightened) increases resistance at connections, leading to **excessive heat** and potential **fires**.  
   - Proper torque ensures **low-resistance, stable connections**.  

2. **Compliance with Device Ratings**:  
   - Termination points (e.g., panel lugs, breakers) are rated for specific torque values. Deviating from these values **voids the device's listing** and creates a safety hazard.  

3. **Arcing and Corrosion Prevention**:  
   - Loose connections can cause **arcing**, which degrades insulation and increases fire risk.  
   - Proper torque minimizes **oxidation and corrosion** at connection points.  

---

### **Code Requirements**
1. **CEC 110.14(D)**:  
   > "Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer. An approved means shall be used to achieve the indicated torque value."  
   - **Approved means** include torque tools, shear bolts, or breakaway-style devices with visual indicators.  

2. **CEC 110.3(B)**:  
   > "All connections and splices shall be torqued to the manufacturer’s specifications."  
   - Mandates use of **torque tools** (not hand tools) for all conductor terminations.  

3. **CEC 110.14(C)**:  
   - Specifies that **aluminum conductors** must use torque-rated devices and anti-oxidant compound (for California, see **Title 24 Part 6** for additional mandates).  

---

### **California (CEC 2022) Considerations**
- **Title 24 Part 6** (Energy Efficiency):  
  - Requires **torque-rated devices** for all panel and breaker connections to ensure long-term reliability.  
- **CALGreen**:  
  - No direct amendments to torque requirements but emphasizes energy-efficient, code-compliant installations.  

---

### **Key Code Sections**
1. **CEC 110.14(D)**: Torque values per manufacturer specifications.  
2. **CEC 110.3(B)**: Torque to manufacturer specifications.  
3. **CEC 110.14(C)**: Aluminum conductor requirements.  

---

### **Practical Implications**
- **Torque Tools Required**:  
  - Use **calibrated torque screwdrivers/wrenches** (e.g., 5–25 in-lbs range).  
- **Manufacturer Instructions**:  
  - Always follow the **panel/breaker manufacturer’s torque values** (typically 8–12 in-lbs for residential panels).  

---

### **Summary**
- **Why Important**: Prevents overheating, arcing, and fire hazards by ensuring secure, low-resistance connections.  
- **Code Basis**: CEC 110.14(D), 110.3(B), and 110.14(C).  
- **California Mandates**: Title 24 Part 6 requires torque-rated devices for compliance.  

**[OK] Source**: CEC 2022 Sections 110.14(D), 110.3(B), and 110.14(C)

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 12.6s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Service Load Calculation for Residential Panel (CEC 2022)

### **Given Loads**
1. **Electric Range**: 12 kW (40A breaker)  
2. **Dryer**: 5.5 kW (30A breaker)  
3. **Small Appliance Circuits**: 2 × 20A (1800 VA each)  
4. **Laundry Circuit**: 1 × 20A (1800 VA)  
5. **General Lighting**: 3000 sq ft × 3 VA/sq ft = 9000 VA  
6. **Central AC**: 4600 W (19.2A at 240V)  

---

### **Step 1: General Lighting Load**  
- **Per CEC Table 220.12**: 3 VA/sq ft × 3000 sq ft = **9000 VA**  

---

### **Step 2: Small Appliance and Laundry Circuits**  
- **Small Appliance Circuits**: 2 × 1800 VA = **3600 VA**  
- **Laundry Circuit**: 1 × 1800 VA = **1800 VA**  
- **Total**: 3600 + 1800 = **5400 VA**  

---

### **Step 3: Electric Range Demand**  
- **Per CEC 220.55**:  
  - First 8 kW at 100% = **8000 VA**  
  - Remaining 4 kW × 40% = **1600 VA**  
  - **Total**: 8000 + 1600 = **9600 VA**  

---

### **Step 4: Dryer Demand**  
- **Per CEC 220.54**: 5.5 kW × 100% = **5500 VA**  

---

### **Step 5: Central AC Load**  
- **Continuous Load**: 4600 W × 125% = **5750 VA**  

---

### **Step 6: Total Load Calculation**  
1. **Sum All Loads**:  
   - General Lighting: 9000 VA  
   - Small Appliance/Laundry: 5400 VA  
   - Range: 9600 VA  
   - Dryer: 5500 VA  
   - AC: 5750 VA  
   - **Total**: **35,250 VA**  

2. **Apply Standard Method (CEC 220.40)**:  
   - First 10,000 VA at 100% = **10,000 VA**  
   - Remaining 25,250 VA × 40% = **10,100 VA**  
   - **Total Service Load**: 10,000 + 10,100 = **20,100 VA**  

---

### **Step 7: Convert to Amperes**  
- **Service Load in Amperes**:  
  $$
  \frac{20,100 \text{ VA}}{240 \text{ V}} = 83.75 \text{ A}
  $$

---

### **Conclusion**  
- **200A Panel**: The calculated load is **83.75A**, well within the 200A main breaker capacity.  
- **Code Compliance**:  
  - **CEC 220.55**: Range demand factor applied.  
  - **CEC 220.54**: Dryer demand factor applied.  
  - **CEC 220.40**: Standard method for load calculation.  

---

### **California (CEC 2022) Considerations**  
- **No amendments** to NEC 220.55/220.54/220.40 in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Final Answer**  
- **Service Load**: **83.75A**  
- **200A Panel**: **Adequately sized** (83.75A < 200A).  

**[OK] Source**: CEC 2022 Sections 220.55, 220.54, and 220.40

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 10.2s | **Exception Search:** No

**Tools Called:** cec_search

**Answer:**

## Residential Panel Working Space Violations (CEC 2022)

### **Identified Violations**
1. **Insufficient Depth Clearance**  
   - **Violation**: Panel depth clearance is **28 inches**, but **30 inches** is required.  
   - **Code**: **CEC 110.26(A)(2)**  
     > "The depth of the working space in front of the equipment shall be the depth of the equipment or 30 in (762 mm), whichever is greater."  

2. **Obstruction in Working Space**  
   - **Violation**: A **water heater** is located **16 inches** to the left within the working space.  
   - **Code**: **CEC 110.26(A)(3)**  
     > "The working space shall be clear of obstructions."  

3. **Insufficient Height Clearance**  
   - **Violation**: Panel is mounted at **5 feet (60 inches)** height, but **6.5 feet (78 inches)** is required.  
   - **Code**: **CEC 110.26(A)(2)**  
     > "The working space shall extend from the grade, floor, or platform to a height of 2.0 m (6 1/2 ft) or the height of the equipment, whichever is greater."  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 110.26 in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Summary of Violations**
| **Violation**               | **Code Section** | **Required** | **Actual** |
|-----------------------------|------------------|--------------|------------|
| Depth clearance             | 110.26(A)(2)     | 30 inches    | 28 inches  |
| Obstruction in working space| 110.26(A)(3)     | Clear        | Water heater within 16 inches |
| Height clearance            | 110.26(A)(2)     | 6.5 feet     | 5 feet     |

---

### **Corrective Actions**
1. **Increase depth clearance** to **30 inches** in front of the panel.  
2. **Relocate the water heater** outside the working space (minimum 30 inches from panel).  
3. **Raise the panel** to **6.5 feet (78 inches)** height.  

**[OK] Source**: CEC 2022 Section 110.26

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 11.9s | **Exception Search:** No

**Tools Called:** nec_search

**Answer:**

## Circuit Protection Requirements for Kitchen Installations (NEC 2023)

### **1. Countertop Receptacles (20A Circuits)**
- **Required Protection**: **GFCI**  
- **NEC Reference**: **210.8(A)(5)**  
  > "All 125-volt, single-phase, 15- and 20-ampere receptacles installed in kitchens shall have ground-fault circuit-interrupter (GFCI) protection for personnel."  
- **Rationale**: Countertop receptacles are required to have GFCI protection due to proximity to water sources and potential shock hazards.

---

### **2. Dishwasher (Dedicated 15A Circuit)**
- **Required Protection**: **Standard Breaker**  
- **NEC Reference**: **210.8(B)(2)**  
  > "GFCI protection shall not be required for receptacles supplying fixed electric space-heating appliances, central air-conditioning equipment, or fixed electric heating, air-conditioning, and refrigeration equipment."  
- **Rationale**: Dishwashers are classified as fixed appliances and are exempt from GFCI requirements.

---

### **3. Garbage Disposal (Dedicated 15A Circuit)**
- **Required Protection**: **Standard Breaker**  
- **NEC Reference**: **210.8(B)(2)**  
  > "GFCI protection shall not be required for receptacles supplying fixed electric heating, air-conditioning, and refrigeration equipment."  
- **Rationale**: Garbage disposals are fixed appliances and do not require GFCI protection.

---

### **4. Refrigerator (Dedicated 20A Circuit)**
- **Required Protection**: **Standard Breaker**  
- **NEC References**:  
  - **210.8(B)(2)**: Exempts fixed refrigeration equipment from GFCI.  
  - **210.12(A)**: Exempts fixed refrigeration equipment from AFCI.  
- **Rationale**:  
  - **GFCI**: Not required for fixed refrigeration equipment.  
  - **AFCI**: Not required for fixed refrigeration equipment (exempt under 210.12(A)).  

---

### **Summary Table**
| **Circuit**               | **Protection Type** | **NEC Section**       |
|---------------------------|---------------------|------------------------|
| Countertop receptacles    | GFCI                | 210.8(A)(5)           |
| Dishwasher                | Standard            | 210.8(B)(2)           |
| Garbage disposal          | Standard            | 210.8(B)(2)           |
| Refrigerator              | Standard            | 210.8(B)(2), 210.12(A)|

---

### **Key Notes**
- **GFCI vs. AFCI**:  
  - **GFCI** protects against ground faults (shock hazards).  
  - **AFCI** protects against arc faults (fire hazards).  
- **Fixed Appliances**: Dishwashers, garbage disposals, and refrigerators are exempt from GFCI and AFCI requirements when installed as fixed equipment.  
- **Code Compliance**: All circuits meet NEC 2023 requirements for residential kitchens.  

**[OK] Source**: NEC 2023 Sections 210.8 and 210.12

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 9.9s | **Exception Search:** No

**Tools Called:** nec_search

**Answer:**

## Subpanel Grounding Violations in Detached Garage (NEC 2023)

### **Identified Violations**
1. **Bonding of Neutral and Ground Bars**  
   - **Violation**: Neutral and ground bars are bonded together with a main bonding jumper.  
   - **Code**: **NEC 250.32(B)**  
     > "In a separately derived system, the grounding electrode conductor shall be connected to the grounding electrode and to the equipment grounding conductor. The neutral and ground must be separated in a subpanel."  
   - **Impact**: Creates a parallel path for neutral current through the ground, risking ground loops and improper GFCI operation.  

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: Neutral bar is bonded to the metal enclosure.  
   - **Code**: **NEC 250.24(D)**  
     > "The neutral conductor shall not be connected to the equipment grounding conductor in a subpanel."  
   - **Impact**: Allows neutral current to flow through the ground, creating a shock hazard and violating the requirement for isolated neutral in subpanels.  

3. **Ground Bar Bonded to Metal Enclosure**  
   - **Violation**: Ground bar is bonded to the metal enclosure.  
   - **Code**: **NEC 250.142(B)**  
     > "The equipment grounding conductor shall be connected to the grounding electrode system and the equipment grounding conductor system."  
   - **Impact**: While bonding the ground bar to the enclosure is acceptable, the neutral bar should never be bonded to the enclosure.  

---

### **Correct Configuration**
| **Component**               | **Correct Connection**                                                                 |
|----------------------------|----------------------------------------------------------------------------------------|
| **Neutral Bar**             | Connected **only** to the feeder neutral conductor. No bonding to ground or enclosure. |
| **Ground Bar**              | Connected to:                                                                          |
|                            | - Feeder equipment grounding conductor (EGC)                                           |
|                            | - Grounding electrode system (e.g., ground rod, water pipe)                          |
|                            | - **Not bonded to neutral bar**                                                      |
| **Metal Enclosure**         | Bonded **only to the ground bar** (via bonding screw).                                 |

---

### **Key Code Requirements**
1. **NEC 250.32(B)**:  
   - Grounding electrode conductor must connect to the grounding electrode and equipment grounding conductor.  
   - **Neutral and ground must be separated in subpanels**.  

2. **NEC 250.24(D)**:  
   - Neutral conductor must **not** be connected to the equipment grounding conductor in a subpanel.  

3. **NEC 250.142(B)**:  
   - Equipment grounding conductor must connect to the grounding electrode system and equipment grounding conductor system.  

---

### **Summary of Violations**
| **Violation**                          | **Code Section** | **Required Fix**                                      |
|----------------------------------------|------------------|--------------------------------------------------------|
| Neutral and ground bars bonded         | 250.32(B)        | Remove bonding jumper between neutral and ground bars. |
| Neutral bar bonded to metal enclosure  | 250.24(D)        | Disconnect neutral bar from enclosure.               |
| Ground bar bonded to metal enclosure   | 250.142(B)       | Ensure ground bar is bonded to grounding electrode.  |

---

### **Corrected Diagram**
```
Feeder Neutral → Neutral Bar (No bonding to ground or enclosure)
Feeder Ground → Ground Bar → Grounding Electrode System
Metal Enclosure → Bonded to Ground Bar (via bonding screw)
```

**[OK] Source**: NEC 2023 Sections 250.32(B), 250.24(D), and 250.142(B)

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 9.4s | **Exception Search:** No

**Tools Called:** nec_lookup_table

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼-Inch RMC (NEC 2023)

### **Step 1: Conduit Internal Area**
- **Conduit Type**: Rigid Metal Conduit (RMC)  
- **Size**: 1¼ inches (1.25 in.)  
- **Internal Cross-Sectional Area**:  
  - **NEC Table 4 (Chapter 9)**:  
    - RMC 1¼-inch internal area = **1.363 in²**  

---

### **Step 2: Conductor Cross-Sectional Area**
- **Conductor Type**: 10 AWG THHN  
- **Cross-Sectional Area**:  
  - **NEC Table 5 (Chapter 9)**:  
    - 10 AWG THHN = **0.0511 in²** per conductor  

---

### **Step 3: Maximum Fill Calculation**
- **Fill Limit**: 40% for **more than two conductors** (NEC 300.15(B)(2)(a)).  
- **Formula**:  
  $$
  \text{Maximum Conductors} = \frac{\text{Conduit Area} \times 40\%}{\text{Conductor Area}} = \frac{1.363 \times 0.40}{0.0511}
  $$
- **Calculation**:  
  $$
  \frac{0.5452}{0.0511} \approx 10.67
  $$
- **Final Answer**: **10 conductors** (round down to the nearest whole number).  

---

### **Step 4: Verify with NEC Table 1 (Chapter 9)**
- **NEC Table 1**:  
  - For **more than two conductors**, the maximum fill is **40%** of the conduit area.  
  - This aligns with the calculation above.  

---

### **Summary**
| **Parameter**               | **Value**         |
|----------------------------|-------------------|
| Conduit Area (RMC 1¼")       | 1.363 in²         |
| Conductor Area (10 AWG THHN) | 0.0511 in²        |
| 40% Fill Limit              | 0.5452 in²        |
| Maximum Conductors          | **10**            |

---

### **Final Answer**
**10 conductors** of 10 AWG THHN can be installed in a 1¼-inch RMC conduit.  

**[OK] Source**: NEC 2023 Chapter 9 Tables 4 and 5

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 12.0s | **Exception Search:** No

**Tools Called:** nec_lookup_table, search_tables, nec_lookup_table

**Answer:**

## Voltage Drop Calculation for 120V Single-Phase Circuit (NEC 2023)

### **Given Parameters**
- **Voltage (V)**: 120V  
- **Load Current (I)**: 22A (continuous)  
- **Conductor Size**: 12 AWG copper  
- **Resistance (R)**: **1.29 ohms/1,000 ft** (provided in question)  
- **Distance (L)**: 50 ft (one-way)  

---

### **Voltage Drop Formula**
For **single-phase** circuits:  
$$
VD = \frac{2 \times I \times R \times L}{1000}
$$

---

### **Calculation**
$$
VD = \frac{2 \times 22 \, \text{A} \times 1.29 \, \Omega/\text{1,000 ft} \times 50 \, \text{ft}}{1000}
$$
$$
VD = \frac{2 \times 22 \times 1.29 \times 50}{1000} = \frac{2838}{1000} = 2.84 \, \text{volts}
$$

---

### **Percentage Voltage Drop**
$$
\%VD = \left( \frac{2.84}{120} \right) \times 100 = 2.37\%
$$

---

### **NEC Compliance Check**
- **NEC Recommendation**: Maximum 3% voltage drop for branch circuits (NEC 210.19(A)(1)).  
- **Result**: **2.37%** < 3% → **Compliant**.

---

### **Critical Note**
The resistance value of **1.29 ohms/1,000 ft** for 12 AWG copper was **provided in the question**, but **NEC Chapter 9 Table 8** (which contains conductor resistance values) could not be retrieved from the database. Standard NEC values for 12 AWG copper are typically **1.98 ohms/1,000 ft** (60°C column). If the correct resistance is used:  
$$
VD = \frac{2 \times 22 \times 1.98 \times 50}{1000} = 4.356 \, \text{volts} \, (3.63\%)
$$  
This would still meet the 3% recommendation.  

---

### **Final Answer**
- **Voltage Drop**: **2.84 volts** (using provided resistance)  
- **Percentage Drop**: **2.37%**  
- **NEC Compliance**: **Yes** (2.37% ≤ 3%)  

**[OK] Source**: NEC 2023 Section 210.19(A)(1) (Voltage Drop Recommendation)  

**Important**: Verify the correct resistance value from **NEC Chapter 9 Table 8** for precise compliance.

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 8.9s | **Exception Search:** No

**Tools Called:** cec_lookup_conductor_ampacity

**Answer:**

## Adjusted Ampacity for 12 AWG TW Conductors (CEC 2022)

### **Step 1: Base Ampacity**
- **Conductor Type**: 12 AWG TW (60°C rated)  
- **Base Ampacity**: **20A** (CEC Table 310.16, 60°C column)  

---

### **Step 2: Temperature Correction Factor**
- **Ambient Temperature**: 110°F (43°C)  
- **Correction Factor**:  
  - **CEC Table 310.15(B)(1)(1)** → **0.58** (for 60°C conductors at 43°C)  

---

### **Step 3: Bundling Adjustment Factor**
- **Number of Conductors**: 6 current-carrying conductors in the same raceway  
- **Adjustment Factor**:  
  - **CEC Table 310.15(B)(2)(a)** → **0.50** (for 6 conductors)  

---

### **Step 4: Final Adjusted Ampacity**
$$
\text{Adjusted Ampacity} = \text{Base Ampacity} \times \text{Temperature Correction} \times \text{Bundling Adjustment}
$$
$$
= 20 \, \text{A} \times 0.58 \times 0.50 = 5.8 \, \text{A}
$$

---

### **Summary**
| **Factor**               | **Value** |
|--------------------------|-----------|
| Base Ampacity (60°C)     | 20A       |
| Temperature Correction   | 0.58      |
| Bundling Adjustment      | 0.50      |
| **Final Adjusted Ampacity** | **5.8A**  |

---

### **CEC Compliance**
- **CEC 310.15(B)(1)(1)**: Temperature correction for ambient temperatures above 30°C.  
- **CEC 310.15(B)(2)(a)**: Bundling adjustment for more than 3 current-carrying conductors.  

---

### **Final Answer**
The adjusted ampacity is **5.8A**, significantly reduced due to high ambient temperature and bundling.  

**[OK] Source**: CEC 2022 Tables 310.16, 310.15(B)(1)(1), and 310.15(B)(2)(a)

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 10.3s | **Exception Search:** No

**Tools Called:** nec_lookup_table

**Answer:**

## Minimum Size Copper GEC for 4 × 250 kcmil Service (NEC 2023)

### **Step 1: Equivalent Service Conductor Size**
- **Parallel Conductors**: 4 × 250 kcmil = **1000 kcmil** (total equivalent area)  
- **Material**: Copper  

---

### **Step 2: Apply NEC Table 250.66**
- **NEC Table 250.66** specifies GEC size based on service conductor size.  
- **For 1000 kcmil copper service conductors**:  
  - **GEC Size**: **2/0 AWG copper** (from the "Copper" column in the table for "Over 600 through 1100" kcmil).  

---

### **Step 3: Verify Parallel Conductor Rule**
- **NEC 250.66(A)**: For parallel service conductors, the GEC size is based on the **total equivalent area** of all parallel conductors.  
- **Calculation**: 4 × 250 kcmil = 1000 kcmil → Matches the "Over 600 through 1100" kcmil range in Table 250.66.  

---

### **Final Answer**
- **Minimum GEC Size**: **2/0 AWG copper**  
- **NEC Reference**: Table 250.66 for 1000 kcmil service conductors  

**[OK] Source**: NEC 2023 Table 250.66

---

