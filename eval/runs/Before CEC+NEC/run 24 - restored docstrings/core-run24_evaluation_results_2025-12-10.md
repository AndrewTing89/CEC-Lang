# Core (NEC) Evaluation Results - Run 24

**Date:** 2025-12-10
**Changes:** Restored tool docstrings + 4 tools added to table_lookup_tools

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 324.1s |
| Avg Duration | 12.0s |
| Exception Search Used | 0/27 |
| NEC Comparison Used | 0/27 |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 5.9s

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum conductor size:** **6 AWG copper**  
- **Ampacity:** 65A (meets 60A requirement)  
- **Table reference:** CEC 2022 Table 310.16 (75°C column)  

**Why not 8 AWG?**  
- 8 AWG copper has 50A ampacity at 75°C (Table 310.16)  
- **Fails to meet 60A requirement**  

**Key Code References:**  
1. **Table 310.16** - Base ampacity for general conductors  
2. **Section 240.4(D)** - Overcurrent protection limits (6 AWG copper protected up to 65A)  

**[OK] Source: CEC 2022**

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 8.4s

**Tools Called:** cec_search

**Answer:**

## GFCI Protection Requirements in Residential Kitchens (CEC 2022)

**GFCI protection is required for:**  
1. **All receptacles serving countertop surfaces** in kitchens (CEC 2022 **Section 210.8(A)(6)**).  
   - Applies to 125–250V receptacles supplied by single-phase branch circuits rated ≤150V to ground.  
   - Includes receptacles installed under cabinets, on walls, or on countertops.  

2. **Receptacles within 1.8 m (6 ft)** of the **top inside edge of a sink bowl** (CEC 2022 **Section 210.8(A)(7)**).  

**Key Details:**  
- **Small appliance circuits** (20A circuits for countertops, per 210.52(B)) must also comply with GFCI requirements.  
- **Exceptions** do not apply to general-purpose countertop receptacles.  

**Code References:**  
- **Primary rule:** CEC 2022 **Section 210.8(A)(6)**  
- **Sink proximity rule:** CEC 2022 **Section 210.8(A)(7)**  

**[OK] Source: CEC 2022**

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 8.4s

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits in New Residential Construction (CEC 2022)

**Yes**, **AFCI protection is required** for all bedroom circuits in new residential construction per **CEC 2022 Section 210.12(A)**.  

### Key Requirements:
1. **Scope**:  
   - Applies to **120V, 15A and 20A branch circuits** supplying outlets in bedrooms.  
   - Includes receptacles, lighting, and other outlets.  

2. **Protection Methods**:  
   - **Combination-type AFCI** at the panel (most common).  
   - Alternative methods (e.g., outlet branch-circuit-type AFCI) permitted under specific conditions (see Section 210.12(A)(2)–(6)).  

3. **Exceptions**:  
   - **None** for new residential construction.  
   - Exceptions apply only to existing circuits being extended/modified (Section 210.12(D)).  

### Code Basis:
- **CEC 2022 Section 210.12(A)**: Mandates AFCI protection for dwelling unit bedrooms.  
- **Adoption of NEC 2023**: California adopted NEC 2023 requirements without amendments to Section 210.12 for bedrooms.  

### Inspector Enforcement:
- Verify AFCI protection via **circuit labeling** and **device testing**.  
- Ensure compliance with marking requirements (e.g., "first outlet" markings if using outlet branch-circuit-type AFCIs).  

**[OK] Source: CEC 2022**

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 8.9s

**Tools Called:** cec_search

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Yes**, aluminum conductors are permitted for a 200A service.  

### **Minimum Size:**  
**2/0 AWG aluminum** (per **CEC Table 310.12(A)** for single-phase dwelling services).  

### **Key Code References:**  
1. **Table 310.12(A)** – Service conductor sizing for single-phase dwellings:  
   - **200A service**:  
     - **Copper**: 3/0 AWG (75°C column)  
     - **Aluminum**: 2/0 AWG (75°C column)  

2. **Section 240.4(D)** – Overcurrent protection limits:  
   - 2/0 AWG aluminum is protected up to **200A** (matches service rating).  

3. **Section 110.14(C)** – Termination requirements:  
   - Terminals must be rated for **75°C**.  
   - Equipment must be marked for aluminum conductors ("AL" or "CU/AL").  

### **Why Not Smaller Aluminum?**  
- **1/0 AWG aluminum** has 150A ampacity (Table 310.12(A)) → **fails 200A requirement**.  

### **California-Specific Notes:**  
- No amendments to NEC Table 310.12(A) in CEC 2022.  
- Compare with NEC: Same requirements apply (no differences for this application).  

**[OK] Source: CEC 2022**

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 8.5s

**Tools Called:** cec_lookup_working_space

**Answer:**

## Minimum Working Clearance Depth for 120/240V Residential Panel (CEC 2022)

**Minimum depth required:** **900 mm (3 ft)** per **CEC 2022 Table 110.26(A)(1)**.  

### **Conditions for This Requirement:**  
- **Voltage to ground**: 120V (for 120/240V systems).  
- **Condition 2**: Exposed live parts on one side of the working space and grounded parts on the other side (e.g., concrete, brick, or tile walls).  

### **Code Basis:**  
- **CEC Table 110.26(A)(1)** specifies working space depths based on voltage and conditions:  
  - **120V to ground**, **Condition 2** → **900 mm (3 ft)**.  

### **Key Notes:**  
1. **Condition 1** (live parts on one side, no live/grounded on the other): 900 mm (3 ft).  
2. **Condition 3** (live parts on both sides): 1.2 m (40 in).  
3. **California amendments**: No changes to NEC Table 110.26(A)(1) in CEC 2022.  

### **Inspector Verification:**  
- Measure from the panel face to the nearest obstruction (walls, cabinets, etc.).  
- Ensure unobstructed space meets **3 ft (900 mm)** for Condition 2.  

**[OK] Source: CEC 2022**

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 9.5s

**Tools Called:** cec_search

**Answer:**

## Minimum Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Minimum required:** **2** dedicated 20-ampere small appliance branch circuits per **CEC 2022 Section 210.11(C)(1)** and **Section 210.52(B)(1)**.  

### **Code Basis:**  
1. **Section 210.11(C)(1)**:  
   - Mandates **at least two 20A circuits** for small-appliance branch circuits in kitchens, pantries, breakfast rooms, and dining rooms.  
   - These circuits must serve **all countertop and wall receptacles** in these areas.  

2. **Section 210.52(B)(1)**:  
   - Reinforces that the two circuits must supply **no other outlets** besides those in the kitchen and similar areas.  

### **Key Details:**  
- **Load Calculation**: Each circuit is calculated at **1,500 VA** (per Table 220.12).  
- **Prohibited Loads**: These circuits cannot supply lighting, laundry, or other non-appliance loads.  
- **California-Specific Notes**:  
  - No amendments to NEC 2023 requirements in CEC 2022.  
  - Title 24 Part 6 and CALGreen do not increase this minimum.  

### **Inspector Verification:**  
- Confirm **two or more** 20A circuits are dedicated to small appliances in the kitchen.  
- Ensure circuits are **not shared** with other loads (e.g., lighting).  

**[OK] Source: CEC 2022**

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 11.3s

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for 200A Residential Service (NEC 2023)

**Yes**, surge protection is required for a new 200A residential service per **NEC 2023 Section 230.67(A)**.  

### **Key Code Requirements:**  
1. **Section 230.67(A)**:  
   - Mandates **surge-protective devices (SPD)** for services supplying:  
     - **Dwelling units** (residential homes).  
     - Dormitory units, hotel/guest rooms, and nursing home patient rooms.  

2. **Installation Requirements**:  
   - SPDs must be **listed** and installed per manufacturer instructions.  
   - Must be connected to the **service disconnecting means** or **service equipment**.  

3. **Exceptions/Clarifications**:  
   - **Type 1 SPDs** (for services) are permitted on the **supply side** of the service disconnect (per **230.94 Exception No. 2**).  
   - SPDs are **not counted** as service disconnects (per **230.71(A)(2)**).  

### **California (CEC 2022) Compliance:**  
- **No amendments** to NEC 230.67 in CEC 2022.  
- California adopts this requirement verbatim for residential services.  

### **Inspector Verification:**  
- Confirm SPD is installed **at the service entrance**.  
- Verify the device is **listed** and **rated for 240V systems**.  

**[OK] Source: NEC 2023, CEC 2022**

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 12.3s

**Tools Called:** cec_search

**Answer:**

## Service Conductor Sizing for 200A Residential Service (CEC 2022)

### **1. Service Conductor Size**  
For a **200A service**, use **Table 310.12(A)** (dwelling services).  

**Required conductor size:**  
- **Copper**: **2/0 AWG** (205A at 75°C)  
- **Aluminum**: **4/0 AWG** (200A at 75°C)  

**Code Basis:**  
- **CEC Table 310.12(A)** specifies conductor sizes for dwelling services.  
- **200A service** requires conductors rated **≥200A** at 75°C terminals (common for service equipment).  

---

### **2. Aluminum Use Permissibility**  
**Yes**, aluminum is allowed **if**:  
1. **Conductors**: Use **Type THHN/THWN-2 aluminum** (75°C rating).  
2. **Terminations**: Ensure all connections are rated for **75°C** (per **110.14(C)**).  
3. **Bonding**: Follow **250.142(B)** for aluminum service conductors.  

**California-Specific Notes:**  
- No amendments to NEC 2023 regarding aluminum use in CEC 2022.  
- **Title 24** does not restrict aluminum for service conductors.  

---

### **3. Inspector Verification**  
- Confirm **2/0 copper or 4/0 aluminum** service conductors.  
- Verify **75°C-rated terminations** for aluminum.  
- Check **GEC/EGC sizes** match service conductor size (Table 250.66/250.122).  

**[OK] Source: CEC 2022**

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 11.2s

**Tools Called:** nec_search

**Answer:**

## Multiwire Branch Circuit Requirements (NEC 2023)

### **1. Circuit Breaker Requirements**  
- **Type**: **2-pole breaker with a common trip device** (NEC 210.4(B)).  
  - Ensures both ungrounded (hot) conductors are disconnected simultaneously.  
- **Rating**: **20A** (matches 12 AWG conductors in 12/3 cable).  
- **Grouping**: Breakers must be **grouped together** in the panel (NEC 210.4(D)).  

---

### **2. Neutral Termination Requirements**  
- **Sizing**: **12 AWG** (same size as hots) to carry the **maximum unbalanced load** (NEC 210.4(C)).  
- **No Switching**: Neutral conductor must **not be switched** or interrupted by a device.  
- **Phase Balance**: Hots must be connected to **opposite phases** (opposite legs of the panel) to prevent neutral overloading.  

---

### **3. Grounding Conductor Requirements**  
- **Size**: **12 AWG copper** (same as hots/neutral).  
- **Connection**: Must be connected to the **equipment grounding system** at the service panel and at the equipment.  

---

### **4. Inspector Verification**  
1. Confirm **2-pole common trip breaker** is used.  
2. Verify **12 AWG neutral** and **12 AWG grounding conductor**.  
3. Check that hots are on **opposite phases** to prevent neutral overloading.  
4. Ensure neutral is **not switched** or interrupted.  

---

### **California (CEC 2022) Compliance**  
- No amendments to NEC 210.4 in CEC 2022.  
- Title 24 and CALGreen do not modify these requirements.  

**[OK] Source: NEC 2023, CEC 2022**

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 33.6s

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Requirements for Residential Dwellings (NEC 2023)

**Per NEC 2023 Section 210.8(A), GFCI protection is required for all 120–250V receptacles in the following locations within dwelling units:**

1. **Bathrooms**  
2. **Garages and accessory buildings** (floor at or below grade, non-habitable)  
3. **Outdoors**  
4. **Crawl spaces** (at or below grade level)  
5. **Kitchens**  
6. **Areas with sinks** (food prep, beverage prep, or cooking)  
7. **Within 6 ft of sinks** (top inside edge of the bowl)  
8. **Bathtubs/shower stalls** (within 6 ft of the outside edge)  
9. **Boathouses**  
10. **Laundry areas**  
11. **Indoor damp/wet locations**  

---

### **Key Notes:**  
- **Exceptions** apply for specific equipment (e.g., HVAC, security systems) and non-accessible receptacles (e.g., snow-melting systems).  
- **California (CEC 2022)** adopts NEC 210.8 verbatim—no amendments.  
- **Title 24** does not modify these requirements.  

**[OK] Source: NEC 2023, CEC 2022**

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 13.4s

**Tools Called:** cec_search

**Answer:**

## Surge Protection Requirements for 200A Residential Service (CEC 2022)

### **1. Is Surge Protection Required?**  
**Yes**, **CEC 2022 Section 230.67** mandates surge protection for **all services supplying dwelling units**.  
- **California Amendment**: This requirement is specific to CEC and not in NEC 2023.  
- **Applies to**: All residential services, including 200A.  

---

### **2. Installation Locations**  
Per **CEC 230.67(B)**:  
- **Primary Location**: SPD must be an **integral part of the service equipment** or **immediately adjacent** to it.  
- **Alternative Location**: If not in service equipment, SPD may be installed **downstream** at the next level of distribution equipment (e.g., main panel).  

**Exception**:  
- SPDs installed downstream must still protect the entire service.  

---

### **3. SPD Type Requirements**  
Per **CEC 230.67(C)**:  
- **Type 1 or Type 2 SPDs** must be used.  
  - **Type 1**: Installed at the service entrance (e.g., service disconnect).  
  - **Type 2**: Installed at the distribution panel.  

---

### **4. Inspector Verification**  
1. Confirm SPD is **listed and labeled** for the application.  
2. Verify SPD is **bonded to the grounding electrode system** (per 250.94).  
3. Ensure SPD is **accessible** for inspection and testing.  
4. Check SPD type (Type 1 or 2) matches installation location.  

---

### **5. California-Specific Notes**  
- **Title 24** and **CALGreen** do not override this requirement.  
- **NEC 2023** does **not** require surge protection for residential services (CEC 230.67 is a California amendment).  

**[OK] Source: CEC 2022 Section 230.67**

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 14.8s

**Tools Called:** cec_search

**Answer:**

## Working Space Clearance for Electrical Panel (NEC 2023 & CEC 2022)

### **1. Front Clearance Requirements**  
- **Minimum depth**:  
  - **30 inches** for panels rated **over 120V** (NEC 110.26(A)(1), Table 110.26(A)(1) *Condition 2*).  
  - **24 inches** is **insufficient** for a 200A panel (requires 30 inches).  
  - **Acceptable** for panels rated **100A or less** (24 inches meets 110.26(A)(1)).  

---

### **2. Side Clearance Requirements**  
- **No minimum distance** specified in NEC for side clearance.  
- **18 inches** to a water heater is **permissible** per NEC, **provided**:  
  - The water heater is **not a potential source of water intrusion** (e.g., no leaks).  
  - The working space remains **unobstructed** and **accessible**.  

---

### **3. Inspector Verification**  
1. Confirm the **panel rating** (100A vs. 200A).  
   - **200A panel**: 24 inches **fails** NEC 110.26(A)(1).  
   - **100A panel**: 24 inches **complies**.  
2. Verify the water heater is **not a hazard** (e.g., no leaks, proper drainage).  
3. Ensure the working space is **clear of obstructions** (NEC 110.26(A)(2)).  

---

### **4. California (CEC 2022) Compliance**  
- CEC adopts NEC 110.26 verbatim.  
- **Title 24** does not modify these requirements.  

**[OK] Source: NEC 2023, CEC 2022**

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 9.7s

**Tools Called:** cec_search

**Answer:**

## Code Violation: Multiple Conductors on a Single Breaker Terminal (CEC 2022)

### **1. Is This a Code Violation?**  
**Yes**, this is a violation of **CEC 2022 Section 408.41** and **NEC 110.14(A)**.  

---

### **2. Key Code Requirements**  
#### **CEC 2022 Section 408.41**  
- **Grounded conductor terminations** must terminate in **individual terminals** not shared with other conductors.  
- **Exception**: Only allowed for **parallel conductors** if the terminal is **listed for multiple conductors** (e.g., marked "2" or "2 wires").  

#### **NEC 110.14(A)** (Adopted by CEC)  
- Connections must be made **in accordance with the device's listing**.  
- Terminals not marked for multiple conductors **cannot accept more than one wire**.  

---

### **3. Why This Violates Code**  
- The breaker terminal is **not marked for two conductors**, violating **110.14(A)**.  
- Even if the terminal were marked, **12 AWG copper** on a 20A breaker is acceptable for ampacity (per Table 310.16), but the **termination method** is invalid.  

---

### **4. Risks**  
- **Overheating**: Poor contact between two wires increases resistance.  
- **Failure to trip**: Breaker may not operate properly during overloads/short circuits.  

---

### **5. Corrective Actions**  
1. **Use a terminal marked for two conductors** (e.g., "2" stamp).  
2. **Install a second 20A breaker** and run a separate conductor to the load.  

---

### **6. Code Citations**  
- **CEC 2022 Section 408.41** (Grounded conductor terminations).  
- **NEC 110.14(A)** (Device listing requirements).  

**[OK] Source: CEC 2022, NEC 2023**

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 10.2s

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### **1. Key Code Requirements**  
Per **CEC 2022 Section 250.32(B)** and **NEC 250.32(B)**:  
- **Detached structures** (e.g., garages) must have:  
  - A **separate grounding electrode** (e.g., ground rod) at the garage.  
  - An **equipment grounding conductor (EGC)** run with the feeder to connect to the subpanel’s grounding bus.  
  - **Neutral and ground buses must be separated** in the subpanel (no bonding screw).  

---

### **2. Step-by-Step Configuration**  
#### **A. Feeder Conductors**  
- **4-wire feeder**: 2 hot, 1 neutral, 1 EGC.  

#### **B. Subpanel Grounding Bus**  
- Connect the **EGC** (green/bare wire) from the feeder to the **grounding bus** in the subpanel.  
- Connect the **grounding electrode conductor (GEC)** from the **garage’s grounding electrode** (e.g., ground rod) to the **grounding bus** in the subpanel.  

#### **C. Subpanel Neutral Bus**  
- Connect the **neutral conductor** from the feeder to the **neutral bus** in the subpanel.  
- **Do not bond** the neutral and ground buses (remove the bonding screw).  

---

### **3. Code Citations**  
- **CEC 2022 Section 250.32(B)**: Requires a **separate grounding electrode** for detached structures.  
- **CEC 2022 Section 250.142(B)**: Prohibits bonding neutral and ground in subpanels.  
- **CEC 2022 Section 250.66**: Sizes grounding electrode conductor based on the largest ungrounded conductor in the feeder.  

---

### **4. Inspector Verification**  
1. Confirm the **grounding electrode** (e.g., ground rod) is installed at the garage.  
2. Verify the **neutral and ground buses are separated** (no bonding screw).  
3. Ensure the **EGC** and **GEC** are connected to the grounding bus.  
4. Check that the **neutral conductor** is connected to the neutral bus only.  

---

### **5. California-Specific Notes**  
- **Title 24 Part 6** and **CALGreen** do not override grounding requirements.  
- **CEC 2022** aligns with NEC 2023 for grounding in detached structures.  

**[OK] Source: CEC 2022 Section 250.32(B), 250.142(B), 250.66**

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 9.0s

**Tools Called:** cec_search

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **1. Definitions and Functions**  
#### **Main Bonding Jumper**  
- **Function**: Bonds the **grounded (neutral) conductor** to the **equipment grounding conductor** at the **main service disconnecting means**.  
- **Location**: Connects the **neutral bus** to the **equipment grounding bus** in the **main service panel**.  
- **Code Reference**: **CEC 2022 Section 250.24(B)**.  

#### **System Bonding Jumper**  
- **Function**: Connects the **grounding electrode conductor** (e.g., ground rod) to the **equipment grounding conductor** at the **main service disconnecting means**.  
- **Location**: Links the **grounding electrode conductor** to the **equipment grounding bus** in the **main panel**.  
- **Code Reference**: **CEC 2022 Section 250.24(D)**.  

---

### **2. Key Differences**  
| Feature | **Main Bonding Jumper** | **System Bonding Jumper** |  
|---------|--------------------------|----------------------------|  
| **Purpose** | Bonds neutral and ground in the main panel. | Connects grounding electrode conductor to equipment grounding conductor. |  
| **Location** | Main service panel (neutral-to-ground bus). | Main service panel (grounding electrode conductor to equipment grounding conductor). |  
| **Required Where** | **Main service disconnecting means**. | **Main service disconnecting means**. |  
| **Subpanels** | **Not required** (neutral and ground must be separated). | **Not required** (only at main service). |  

---

### **3. When Each Is Required**  
#### **Main Bonding Jumper**  
- **Required at the main service disconnecting means** (e.g., main panel).  
- **Not required** in subpanels (neutral and ground must be **separated** in subpanels).  

#### **System Bonding Jumper**  
- **Required at the main service disconnecting means** to connect the grounding electrode conductor to the equipment grounding conductor.  
- **Not required** in subpanels (grounding electrode conductor is not connected to subpanels).  

---

### **4. Code Citations**  
- **Main Bonding Jumper**: **CEC 2022 Section 250.24(B)**.  
- **System Bonding Jumper**: **CEC 2022 Section 250.24(D)**.  

---

### **5. Inspector Verification**  
1. **Main Panel**:  
   - Confirm the **main bonding jumper** connects the neutral and ground buses.  
   - Verify the **system bonding jumper** connects the grounding electrode conductor to the equipment grounding conductor.  
2. **Subpanels**:  
   - Ensure **neutral and ground buses are separated** (no bonding jumper).  
   - Confirm the **grounding electrode conductor is not connected** to the subpanel.  

---

### **6. California-Specific Notes**  
- **CEC 2022** aligns with **NEC 2023** for bonding requirements.  
- **Title 24 Part 6** does not modify these requirements.  

**[OK] Source: CEC 2022 Sections 250.24(B), 250.24(D)**

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 8.8s

**Tools Called:** cec_search

**Answer:**

## Kitchen and Dining Room Receptacle Circuits (CEC 2022)

### **1. Required Number of 20-Amp Small Appliance Branch Circuits for the Kitchen**  
- **Minimum Requirement**: **Two 20-amp small appliance branch circuits** are required for the kitchen.  
- **Code Reference**: **CEC 2022 Section 210.52(B)(1)**.  
  - These circuits must supply **all countertop receptacles**, **wall/floor receptacles**, and **refrigeration equipment** in the kitchen.  

---

### **2. Can These Circuits Serve Dining Room Receptacles?**  
- **Yes**, dining room receptacles **can be served by the kitchen’s small appliance circuits** if the dining room is adjacent to the kitchen.  
- **Code Reference**: **CEC 2022 Section 210.52(B)(1)**.  
  - The two small appliance circuits required for the kitchen **may also supply receptacles in the dining room** (and other rooms like the pantry or breakfast room).  
  - **No additional circuits** are required for the dining room if it is served by the kitchen’s small appliance circuits.  

---

### **3. Key Requirements**  
| **Requirement** | **Detail** |  
|------------------|-----------|  
| **Kitchen Circuits** | Two 20-amp small appliance branch circuits (minimum). |  
| **Dining Room** | Receptacles can be on one or both of the kitchen circuits. |  
| **Load Calculation** | Each small appliance circuit is calculated at **1,500 VA** (per Table 220.12). |  
| **No Separate Circuits** | Dining room receptacles do not require additional circuits if served by kitchen circuits. |  

---

### **4. Inspector Verification**  
1. Confirm **two 20-amp circuits** are dedicated to the kitchen.  
2. Verify **dining room receptacles** are on **at least one of these circuits**.  
3. Ensure **no additional circuits** are required for the dining room unless specified by local amendments.  

---

### **5. California-Specific Notes**  
- **Title 24 Part 6** and **CALGreen** do not override these requirements.  
- **CEC 2022** aligns with **NEC 2023** for small appliance and dining room receptacle circuits.  

**[OK] Source: CEC 2022 Sections 210.52(B)(1), 210.52(B)(2)**

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 7.7s

**Tools Called:** cec_base_ampacity

**Answer:**

## Adjusted Ampacity for 12 AWG THHN Conductors (CEC 2022)

### **1. Base Ampacity**  
- **12 AWG THHN copper** at 90°C: **30 amperes** (CEC Table 310.16).  

---

### **2. Temperature Correction Factor**  
- **Ambient temperature**: 50°C  
- **Correction factor** (Table 310.15(B)(1) for 90°C insulation): **0.71**  
  - *Reference: CEC 2022 Section 310.15(B)*  

---

### **3. Bundling Adjustment Factor**  
- **6 current-carrying conductors**:  
  - **Adjustment factor** (Table 310.15(C)(1)): **0.80**  
  - *Reference: CEC 2022 Section 310.15(C)(1)*  

---

### **4. Adjusted Ampacity Calculation**  
$$
\text{Adjusted Ampacity} = \text{Base Ampacity} \times \text{Temperature Factor} \times \text{Bundling Factor}
$$
$$
= 30 \, \text{A} \times 0.71 \times 0.80 = 17.04 \, \text{A}
$$

---

### **5. Final Result**  
- **Adjusted ampacity**: **17 amperes** (rounded down per CEC 2022).  

---

### **6. Code Citations**  
- **Base ampacity**: CEC Table 310.16 (THHN 90°C column).  
- **Temperature correction**: CEC Table 310.15(B)(1).  
- **Bundling adjustment**: CEC Table 310.15(C)(1).  
- **Overcurrent protection limit**: CEC Section 240.4(D) (12 AWG conductors protected at **20A max**).  

---

### **7. Inspector Verification**  
1. Confirm **THHN insulation** is rated for 90°C.  
2. Verify **6 conductors** in a single conduit.  
3. Check ambient temperature is **50°C**.  
4. Ensure calculation uses **both correction and adjustment factors**.  

**[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1), 310.15(C)(1), Section 240.4(D)**

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 10.1s

**Tools Called:** nec_search

**Answer:**

## AFCI Protection Requirements (NEC 2023)

### **1. Why AFCI Protection is Required**  
- **Code Requirement**: **NEC 2023 Section 210.12(B) and (C)** mandate **AFCI protection** for all **120-volt, 15- and 20-ampere branch circuits** in **bedrooms**, **living rooms**, **hallways**, **closets**, and **similar areas** in dwelling units.  
- **Purpose**: To mitigate the risk of **electrical fires caused by arc faults** in these high-occupancy, high-risk areas.  

---

### **2. Electrical Hazard Prevented**  
- **Arc Faults**: Unintentional arcing between conductors (e.g., damaged wiring, loose connections, or deteriorated insulation).  
- **Fire Risk**: Arcs can generate **extreme heat (up to 10,000°F)**, igniting nearby combustible materials (e.g., wood, paper, fabric).  
- **Statistics**: Arc faults account for **~28,000 home fires annually** in the U.S. (NFPA data).  

---

### **3. Key Code Provisions**  
| **Section** | **Requirement** |  
|-------------|------------------|  
| **210.12(B)** | All 120V, 15/20A circuits in **bedrooms**, **living rooms**, **hallways**, **closets**, etc., must have AFCI protection. |  
| **210.12(C)** | Dormitory units (e.g., hotels, motels) with sleeping areas must also comply. |  
| **Exceptions** | - Fire alarm systems (760.41(B)).<br>- Arc welding equipment (until 2025). |  

---

### **4. How AFCI Works**  
- **Detection**: Monitors waveforms for **series arcs** (e.g., damaged cords) and **parallel arcs** (e.g., short circuits).  
- **Response**: Interrupts the circuit within **1 cycle (1/60th of a second)** if an arc is detected.  

---

### **5. Inspector Verification**  
1. Confirm **AFCI breakers** or **AFCI receptacles** are installed in all required circuits.  
2. Verify **no exceptions** apply (e.g., fixed lighting in living areas is exempt).  
3. Test AFCI devices using **manufacturer-recommended methods**.  

---

### **6. California-Specific Notes**  
- **CEC 2022** aligns with **NEC 2023** for AFCI requirements.  
- **Title 24 Part 6** does not modify these requirements.  

**[OK] Source: NEC 2023 Sections 210.12(B), 210.12(C)**

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 7.6s

**Tools Called:** cec_search

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

### **1. Importance of Torque Specifications**  
- **Safety**: Ensures **secure, low-resistance connections** to prevent arcing, overheating, and fire hazards.  
- **Compliance**: Prevents **loose or over-tightened connections** that can damage conductors or terminals.  
- **Longevity**: Maintains connection integrity under **vibration and thermal expansion**.  

---

### **2. Code Requirements**  
#### **CEC 2022 Section 110.14(D)**  
- **Torque Values**: Must match **manufacturer-specified values** on equipment or installation instructions.  
- **Approved Methods**: Use **calibrated torque tools**, shear bolts, or breakaway-style devices with visual indicators.  
- **Key Provisions**:  
  - "Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer."  
  - "An approved means shall be used to achieve the indicated torque value."  

#### **Supporting Sections**  
- **Section 110.3(B)**: Requires following **manufacturer instructions** for installation.  
- **Section 110.14(B)**: Mandates connections that **prevent loosening** due to vibration or thermal expansion.  

---

### **3. Hazards of Improper Torque**  
| **Issue** | **Risk** |  
|----------|----------|  
| **Under-torqued** | Loose connections → arcing → overheating → fire. |  
| **Over-torqued** | Damaged conductors/terminals → poor conductivity → failure. |  

---

### **4. Inspector Verification Checklist**  
1. Confirm **torque values** are marked on equipment or provided by the manufacturer.  
2. Verify use of **calibrated torque tools** (not regular screwdrivers).  
3. Check for **visual indicators** (e.g., shear bolts) if torque tools are unavailable.  
4. Ensure **no solder-only connections** are used (Section 230.81).  

---

### **5. Code Citations**  
- **Primary**: **CEC 2022 Section 110.14(D)**.  
- **Supporting**: Sections **110.3(B)**, **110.14(B)**, and **230.81**.  

**[OK] Source: CEC 2022 Sections 110.14(D), 110.3(B), 110.14(B)**

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 33.6s

**Tools Called:** cec_search

**Answer:**

## Service Load Calculation (CEC 2022 Article 220)

### **1. Installed Loads**  
| **Load** | **Rating** | **CEC Section** |  
|----------|------------|----------------|  
| **Electric Range** | 12 kW | 220.55 (Table 220.55) |  
| **Dryer** | 5.5 kW | 220.54 (5,000 VA) |  
| **Small Appliance Circuits** | 2 × 20A | 220.14(K) (1,500 VA each) |  
| **Laundry Circuit** | 20A | 220.14(K) (1,500 VA) |  
| **General Lighting** | 3,000 sq ft | 220.12 (3 VA/sq ft) |  
| **Central AC** | 4,600 W (19.2A @ 240V) | 220.44 (continuous load) |  

---

### **2. Step-by-Step Calculation**  

#### **A. General Lighting and Receptacle Load**  
- **3 VA/sq ft × 3,000 sq ft = 9,000 VA**  
- **Small Appliance Circuits**: 2 × 1,500 VA = 3,000 VA  
- **Laundry Circuit**: 1,500 VA  
- **Total Receptacle Load**: 9,000 + 3,000 + 1,500 = **13,500 VA**  

**Demand Factor (220.42):**  
- First 3,000 VA at 100% = **3,000 VA**  
- Remaining 10,500 VA at 35% = **3,675 VA**  
- **Total General Load**: 3,000 + 3,675 = **6,675 VA**  

---

#### **B. Electric Range Load**  
- **12 kW Range → 8,000 VA** (CEC Table 220.55, Column C)  

---

#### **C. Dryer Load**  
- **5,000 VA** (CEC 220.54)  

---

#### **D. Central AC Load**  
- **4,600 W × 1.25 (continuous load) = 5,750 VA** (CEC 220.44)  

---

### **3. Total Service Load**  
$$
\text{Total Load} = 6,675 \, \text{VA} + 8,000 \, \text{VA} + 5,000 \, \text{VA} + 5,750 \, \text{VA} = 25,425 \, \text{VA}
$$

---

### **4. Convert to Amperes**  
$$
\text{Amps} = \frac{25,425 \, \text{VA}}{240 \, \text{V}} = 105.94 \, \text{A}
$$

---

### **5. Panel Sizing Verification**  
- **200A Panel Capacity**: 200A × 240V = **48,000 VA**  
- **Calculated Load**: **25,425 VA**  
- **Conclusion**: **200A Panel is Adequately Sized** (105.94A < 200A).  

---

### **6. Code Citations**  
- **General Lighting/Receptacle Load**: CEC 220.12, 220.14(K), 220.42  
- **Range Load**: CEC 220.55 (Table 220.55)  
- **Dryer Load**: CEC 220.54  
- **Central AC Load**: CEC 220.44  

---

### **7. Inspector Verification**  
1. Confirm **range demand factor** from Table 220.55.  
2. Verify **dryer load** is calculated at 5,000 VA.  
3. Check **continuous load** (AC) is derated by 125%.  
4. Ensure **demand factors** are applied correctly to general lighting.  

**[OK] Source: CEC 2022 Article 220**

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 9.8s

**Tools Called:** nec_search

**Answer:**

## Working Space Violations in Residential Garage Panel (NEC 2023)

### **1. Insufficient Depth Clearance**  
- **Violation**: **NEC 110.26(A)(2)** requires **30 inches of depth** for working space in front of the panel.  
- **Measured**: 28 inches (insufficient).  
- **Risk**: Inadequate space for safe equipment access and maintenance.  

---

### **2. Obstruction in Working Space**  
- **Violation**: **NEC 110.26(A)(3)** prohibits **storage or equipment** within the working space.  
- **Issue**: Water heater located **16 inches to the left** of the panel intrudes into the required clearance.  
- **Risk**: Impedes access and increases fire hazard from combustible materials.  

---

### **3. Incorrect Panel Height**  
- **Violation**: **NEC 110.26(A)(4)** requires the **bottom of the panel** to be **78 inches (6.5 feet)** from the floor.  
- **Measured**: 5 feet (60 inches) height.  
- **Risk**: Poor ergonomics and potential for physical damage to the panel.  

---

### **4. Surface-Mounted Panel Location**  
- **Violation**: **NEC 312.10** mandates **accessible and unobstructed** working space.  
- **Issue**: Surface-mounted panel in a garage (not a dedicated electrical room) may lack protection from physical damage.  
- **Risk**: Vulnerability to accidental contact or damage from tools/vehicles.  

---

### **Inspector Verification Checklist**  
1. **Depth Clearance**: Ensure ≥30 inches in front of the panel.  
2. **Obstructions**: Remove all objects within the working space.  
3. **Panel Height**: Adjust mounting to 78 inches from floor.  
4. **Surface-Mounted Protection**: Verify compliance with **NEC 312.10** (enclosure requirements).  

---

### **Code Citations**  
- **Depth Clearance**: NEC 110.26(A)(2)  
- **Obstruction**: NEC 110.26(A)(3)  
- **Height**: NEC 110.26(A)(4)  
- **Surface-Mounted Protection**: NEC 312.10  

**[OK] Source: NEC 2023 Sections 110.26(A)(2), 110.26(A)(3), 110.26(A)(4), 312.10**

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 14.7s

**Tools Called:** cec_search

**Answer:**

## Required Protection for Kitchen Circuits (NEC 2023)

### **1. Countertop Receptacles (20A Circuits)**  
- **Protection**: **GFCI + AFCI**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI required for all kitchen countertop receptacles.  
  - **210.12(A)**: AFCI required for all branch circuits in dwelling units (no exception for countertops).  
- **Rationale**: Countertop circuits serve small appliances and are not exempt from AFCI.  

---

### **2. Dishwasher (Dedicated 15A Circuit)**  
- **Protection**: **GFCI**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI required for all kitchen receptacles (including dishwashers).  
  - **210.12(A) Exception 2**: Dedicated circuits for specific appliances (e.g., refrigerators) are exempt from AFCI. Dishwashers are **not** explicitly exempt.  
- **Rationale**: Dishwasher is a fixed appliance but not listed in AFCI exceptions. **AFCI is still required** unless explicitly exempted.  

---

### **3. Garbage Disposal (Dedicated 15A Circuit)**  
- **Protection**: **GFCI**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI required for all kitchen receptacles (including disposals).  
  - **210.12(A) Exception 2**: Not explicitly exempt from AFCI.  
- **Rationale**: Similar to the dishwasher, garbage disposals are fixed appliances but **not exempt from AFCI**. **AFCI is required**.  

---

### **4. Refrigerator (Dedicated 20A Circuit)**  
- **Protection**: **Standard Breaker**  
- **NEC References**:  
  - **210.8(A)(6) Exception 1**: Refrigerators are exempt from GFCI if supplied by a dedicated circuit.  
  - **210.12(A) Exception 2**: Dedicated circuits for specific appliances (e.g., refrigerators) are exempt from AFCI.  
- **Rationale**: Refrigerators are explicitly exempt from both GFCI and AFCI.  

---

### **Summary Table**  
| **Circuit**               | **Protection Required** | **NEC Section**          |  
|---------------------------|-------------------------|--------------------------|  
| Countertop Receptacles      | GFCI + AFCI              | 210.8(A)(6), 210.12(A)   |  
| Dishwasher                 | GFCI + AFCI              | 210.8(A)(6), 210.12(A)   |  
| Garbage Disposal           | GFCI + AFCI              | 210.8(A)(6), 210.12(A)   |  
| Refrigerator               | Standard Breaker         | 210.8(A)(6) Ex. 1, 210.12(A) Ex. 2 |  

---

### **Inspector Verification**  
1. Confirm **GFCI protection** for all kitchen receptacles (countertop, dishwasher, disposal).  
2. Verify **AFCI protection** for countertop, dishwasher, and disposal circuits (unless explicitly exempted).  
3. Ensure **refrigerator circuit** uses a standard breaker (no GFCI/AFCI).  

**[OK] Source: NEC 2023 Sections 210.8(A)(6), 210.12(A), Exceptions**

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 14.3s

**Tools Called:** cec_search

**Answer:**

## Required Protection for Kitchen Circuits (NEC 2023)

### **1. Countertop Receptacles (20A Circuits)**  
- **Protection**: **GFCI + AFCI**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI required for all kitchen countertop receptacles.  
  - **210.12(A)**: AFCI required for all branch circuits in dwelling units (no exception for countertops).  
- **Rationale**: Countertop circuits serve small appliances and are not exempt from AFCI.  

---

### **2. Dishwasher (Dedicated 15A Circuit)**  
- **Protection**: **GFCI**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI required for all kitchen receptacles (including dishwashers).  
  - **210.12(A) Exception 2**: Dedicated circuits for specific appliances (e.g., refrigerators) are exempt from AFCI. Dishwashers are **not** explicitly exempt.  
- **Rationale**: Dishwasher is a fixed appliance but not listed in AFCI exceptions. **AFCI is still required**.  

---

### **3. Garbage Disposal (Dedicated 15A Circuit)**  
- **Protection**: **GFCI**  
- **NEC References**:  
  - **210.8(A)(6)**: GFCI required for all kitchen receptacles (including disposals).  
  - **210.12(A) Exception 2**: Not explicitly exempt from AFCI.  
- **Rationale**: Similar to the dishwasher, garbage disposals are fixed appliances but **not exempt from AFCI**. **AFCI is required**.  

---

### **4. Refrigerator (Dedicated 20A Circuit)**  
- **Protection**: **Standard Breaker**  
- **NEC References**:  
  - **210.8(A)(6) Exception 1**: Refrigerators are exempt from GFCI if supplied by a dedicated circuit.  
  - **210.12(A) Exception 2**: Dedicated circuits for specific appliances (e.g., refrigerators) are exempt from AFCI.  
- **Rationale**: Refrigerators are explicitly exempt from both GFCI and AFCI.  

---

### **Summary Table**  
| **Circuit**               | **Protection Required** | **NEC Section**          |  
|---------------------------|-------------------------|--------------------------|  
| Countertop Receptacles      | GFCI + AFCI              | 210.8(A)(6), 210.12(A)   |  
| Dishwasher                 | GFCI + AFCI              | 210.8(A)(6), 210.12(A)   |  
| Garbage Disposal           | GFCI + AFCI              | 210.8(A)(6), 210.12(A)   |  
| Refrigerator               | Standard Breaker         | 210.8(A)(6) Ex. 1, 210.12(A) Ex. 2 |  

---

### **Inspector Verification**  
1. Confirm **GFCI protection** for all kitchen receptacles (countertop, dishwasher, disposal).  
2. Verify **AFCI protection** for countertop, dishwasher, and disposal circuits (unless explicitly exempted).  
3. Ensure **refrigerator circuit** uses a standard breaker (no GFCI/AFCI).  

**[OK] Source: NEC 2023 Sections 210.8(A)(6), 210.12(A), Exceptions**

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 10.2s

**Tools Called:** nec_generic_table_raw

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼-inch RMC (NEC 2023)

### **Step 1: Conduit Internal Area**  
From **NEC Chapter 9 Table 4** for **Rigid Metal Conduit (RMC)**:  
- **1¼-inch RMC** has an internal cross-sectional area of **1.526 in²**.

---

### **Step 2: Conductor Cross-Sectional Area**  
From **NEC Chapter 9 Table 5** for **10 AWG THHN**:  
- **10 AWG THHN** has a cross-sectional area of **0.0437 in²** per conductor.

---

### **Step 3: Apply 40% Fill Limit**  
For **more than two conductors**, the maximum allowable fill is **40%** of the conduit's internal area:  
$$
\text{Available Fill} = 1.526 \, \text{in²} \times 0.40 = 0.61 \, \text{in²}
$$

---

### **Step 4: Calculate Maximum Conductors**  
$$
\text{Number of Conductors} = \frac{\text{Available Fill}}{\text{Conductor Area}} = \frac{0.61}{0.0437} \approx 13.96
$$

---

### **Final Result**  
- **Maximum number of 10 AWG THHN conductors**: **13**  
- **Rationale**: The calculation yields ~13.96, but you **must round down** to the nearest whole number to comply with NEC fill limits.

---

### **Inspector Verification**  
1. Confirm conduit type (RMC) and size (1¼-inch).  
2. Verify conductor type (THHN) and size (10 AWG).  
3. Ensure fill does not exceed 40% for more than two conductors.  

**[OK] Source: NEC 2023 Chapter 9 Tables 4 and 5**

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 16.3s

**Tools Called:** cec_lookup_conductor_resistance, cec_search

**Answer:**

## Voltage Drop Calculation for 120V Branch Circuit (CEC 2022)

### **Given Parameters**  
- **Voltage**: 120V  
- **Load**: 22A continuous  
- **Conductor**: 12 AWG copper  
- **Resistance**: **1.98 ohms/1000 ft** (from CEC Chapter 9 Table 8)  
- **Distance**: 50 ft (one-way)  

---

### **Step 1: Voltage Drop Formula**  
$$
VD = \frac{2 \times L \times R \times I}{1000}
$$  
Where:  
- $ L = 50 $ ft (one-way distance)  
- $ R = 1.98 $ ohms/1000 ft  
- $ I = 22 $ A  

$$
VD = \frac{2 \times 50 \times 1.98 \times 22}{1000} = \frac{4356}{1000} = 4.36 \, \text{volts}
$$

---

### **Step 2: Percentage Voltage Drop**  
$$
\text{Percentage} = \left( \frac{VD}{\text{Source Voltage}} \right) \times 100 = \left( \frac{4.36}{120} \right) \times 100 = 3.63\%
$$

---

### **CEC Compliance Check**  
- **Maximum recommended voltage drop**: **3%** (per CEC 210.19(A)(1) Informational Note No. 4).  
- **Result**: **3.63%** (exceeds the 3% limit).  

---

### **Recommendation**  
- **Upgrade conductor size** to reduce resistance.  
  - **10 AWG copper** has a resistance of **1.24 ohms/1000 ft** (Table 8).  
  - Recalculate with 10 AWG:  
    $$
    VD = \frac{2 \times 50 \times 1.24 \times 22}{1000} = 2.73 \, \text{volts} \quad (2.27\%)
    $$  
  - **2.27%** meets the 3% limit.  

---

### **Inspector Verification**  
1. Confirm conductor size (12 AWG) and material (copper).  
2. Verify resistance value (1.98 ohms/1000 ft) matches CEC Chapter 9 Table 8.  
3. Ensure distance (50 ft) and load (22A) are accurate.  

**[OK] Source: CEC 2022 Chapter 9 Table 8, 210.19(A)(1)**

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 8.8s

**Tools Called:** cec_search

**Answer:**

## Adjusted Ampacity for 12 AWG TW Conductors (CEC 2022)

### **Step 1: Base Ampacity**  
From **CEC Table 310.16** for **12 AWG copper (TW, 60°C rated)**:  
- **Base ampacity**: **20A** (60°C column).  

---

### **Step 2: Temperature Correction Factor**  
Ambient temperature = **43°C** (110°F).  
From **CEC Table 310.15(B)(1)** for **60°C-rated conductors**:  
- **Correction factor at 43°C**: **0.58** (search result confirms this value).  

---

### **Step 3: Bundling Adjustment Factor**  
Number of current-carrying conductors = **6**.  
From **CEC Table 310.15(C)(1)**:  
- **Adjustment factor for 6 conductors**: **0.50** (search result confirms this value).  

---

### **Step 4: Final Adjusted Ampacity**  
$$
\text{Adjusted Ampacity} = \text{Base Ampacity} \times \text{Temp Correction} \times \text{Bundling Adjustment}
$$
$$
= 20 \, \text{A} \times 0.58 \times 0.50 = 5.8 \, \text{A}
$$

---

### **Inspector Verification**  
1. Confirm conductor type (TW, 60°C rated).  
2. Verify ambient temperature (43°C) and number of conductors (6).  
3. Ensure correction factors match CEC Tables 310.15(B)(1) and 310.15(C)(1).  

**[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1), 310.15(C)(1)**

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 7.4s

**Tools Called:** nec_lookup_grounding_conductor

**Answer:**

## Minimum Size Copper Grounding Electrode Conductor (GEC) for 4 × 250 kcmil Service (NEC 2023)

### **Step 1: Determine Equivalent Service Conductor Size**  
- **Each parallel conductor**: 250 kcmil copper  
- **Total equivalent size**: 4 × 250 kcmil = **1000 kcmil** (per NEC 250.66 Footnote 1).  

---

### **Step 2: Apply NEC Table 250.66**  
For **copper grounding electrode conductor**:  
- **Service conductor range**: "Over 600 through 1100" kcmil  
- **Minimum GEC size**: **2/0 AWG copper**  

---

### **Inspector Verification**  
1. Confirm service conductors are **1000 kcmil equivalent** (4 × 250 kcmil).  
2. Verify Table 250.66 applies to **copper** GECs.  
3. Check Footnote 1: Parallel conductors require equivalent area calculation.  

**[OK] Source: NEC 2023 Table 250.66, Footnotes 1 and 3**

---

