# CEC 2022 Unified Evaluation Results - Run 41

**Date:** 2025-12-12
**Description:** Tool-level fixes for cec2022-045 and cec2022-051

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 53 |
| Successful | 53 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 601.9s |
| Avg Duration | 11.4s |
| Reflection Used | 53/53 |
| Reflection Improved | 5/53 |
| Hint Enforcement | 4/53 |
| Protection Enforcement | 5/53 |

## Results by Category

| Category | Total | Success | Rate |
|----------|-------|---------|------|
| adjusted_ampacity | 1 | 1 | 100% |
| ampacity_adjustment | 2 | 2 | 100% |
| clearance_violations | 1 | 1 | 100% |
| commercial_load | 1 | 1 | 100% |
| conductor_ampacity | 1 | 1 | 100% |
| conduit_fill | 1 | 1 | 100% |
| derating_calculation | 1 | 1 | 100% |
| dwelling_load | 1 | 1 | 100% |
| edge_cases | 2 | 2 | 100% |
| electrification | 2 | 2 | 100% |
| enclosure | 1 | 1 | 100% |
| ev_charging | 1 | 1 | 100% |
| fixture_wire | 1 | 1 | 100% |
| flexible_cord | 1 | 1 | 100% |
| gfci_afci_compliance | 1 | 1 | 100% |
| grounding | 2 | 2 | 100% |
| grounding_bonding | 2 | 2 | 100% |
| grounding_electrode_conductor | 1 | 1 | 100% |
| heat_pump | 1 | 1 | 100% |
| knowledge | 2 | 2 | 100% |
| knowledge_simple | 5 | 5 | 100% |
| lighting_load | 1 | 1 | 100% |
| load_calculations | 2 | 2 | 100% |
| medium_voltage | 1 | 1 | 100% |
| motor_circuit | 1 | 1 | 100% |
| motor_control | 1 | 1 | 100% |
| multi_article | 2 | 2 | 100% |
| overcurrent | 1 | 1 | 100% |
| panel_load_calculation | 1 | 1 | 100% |
| panelboard_requirements | 1 | 1 | 100% |
| service_sizing | 1 | 1 | 100% |
| solar_pv | 1 | 1 | 100% |
| subpanel_violations | 1 | 1 | 100% |
| surge_protection | 1 | 1 | 100% |
| table_lookup | 3 | 3 | 100% |
| voltage_drop | 1 | 1 | 100% |
| why_questions | 2 | 2 | 100% |
| working_space | 1 | 1 | 100% |

## Results by Question

### cec2022-001

**Original ID:** baseline-001 | **Category:** table_lookup | **Tier:** baseline

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Duration:** 17.1s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## 12 AWG Copper Conductor Ampacity (CEC 2022)

**Base Ampacity**: 25 amperes at 75°C (Table 310.16)  
**Overcurrent Protection Limit**: 20 amperes maximum (Section 240.4(D))  

### Key Considerations:
1. **Ambient Temperature Correction**  
   - If ambient temperature exceeds 30°C, apply correction factors from **310.15(B)**  
   - Example: At 40°C ambient, multiply by 0.88 (Table 310.15(B)(1)(1))

2. **Bundling Adjustment**  
   - For more than 3 current-carrying conductors, apply derating from **310.15(C)(1)**  
   - Example: 4-6 conductors → 0.80 adjustment factor

3. **California-Specific Rule**  
   - Section **240.4(D)** explicitly limits 12 AWG copper to **20A maximum overcurrent protection**  
   - This creates a "more restrictive" rule than the 25A ampacity

**Final Answer**:  
A 12 AWG copper conductor has a 25A ampacity at 75°C, but **must be protected by a 20A overcurrent device** per CEC 2022. Additional derating may apply for ambient temperature or conductor bundling.

[OK] Source: CEC 2022

---

### cec2022-002

**Original ID:** baseline-002 | **Category:** table_lookup | **Tier:** baseline

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size**: **6 AWG copper**  
- **Ampacity**: 65A at 75°C (Table 310.16)  
- **Meets requirement**: 65A ≥ 60A  

**Key Code References**:  
- **Base ampacity**: CEC Table 310.16  
- **OCP limit**: 240.4(D) permits 65A OCP for 6 AWG copper  

**Inspector Note**:  
- 8 AWG (50A) is insufficient for 60A circuits.  
- Verify ambient temperature and conductor bundling (per 310.15(B)(1) and 310.15(C)(1)) if non-standard conditions apply.  

[OK] Source: CEC 2022

---

### cec2022-003

**Original ID:** baseline-003 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 11.3s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes

**Answer:**

## GFCI and AFCI Protection in Residential Kitchens (CEC 2022)

### **GFCI Protection Requirement**
- **Required for**: All 125–250V receptacles serving **countertop surfaces** in kitchens (CEC 2022 **Section 210.8(A)(6)**).  
- **No exceptions** apply for standard countertop receptacles in kitchens.

---

### **AFCI Protection Requirement**
- **Required for**: All **120V, 15/20A branch circuits** in dwelling units, including **kitchens** (CEC 2022 **Section 210.12(A)**).  
- **Key Details**:  
  - Covers circuits supplying outlets in kitchens, family rooms, dining rooms, etc.  
  - Exceptions:  
    - Fire alarm systems (not applicable here).  
    - Specific conduit/enclosure modifications (not relevant for standard kitchen circuits).  

---

### **Combined Requirements**
- **Kitchen countertop receptacles** must comply with **both GFCI and AFCI** protection.  
- **No conflicts**: GFCI and AFCI serve different safety purposes and can be implemented together (e.g., a **CAFCI** device provides both protections).  

[OK] Source: CEC 2022 Sections **210.8(A)(6)** and **210.12(A)**

---

### cec2022-004

**Original ID:** baseline-004 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 13.9s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes

**Answer:**

## AFCI and GFCI Protection for Bedroom Circuits (CEC 2022)

**Final Answer:**  
- **AFCI Protection**: **Required** for all 120V, 15/20A bedroom circuits per **CEC 210.12(A)**.  
- **GFCI Protection**: **Not required** for standard bedroom receptacles (per **CEC 210.8** does not list bedrooms as GFCI-required locations).  

---

### **AFCI Requirements (CEC 210.12(A))**  
- **Applies to**: All 120V, 15/20A circuits in dwelling units, including **bedrooms, living rooms, hallways, etc.**  
- **Permitted Methods**:  
  1. Combination-type AFCI at the circuit origin.  
  2. Branch/feeder + outlet AFCI (with marking at first outlet).  
  3. Supplemental arc protection + outlet AFCI (limited conductor lengths).  
  4. Outlet AFCI + branch-circuit OCPD (limited conductor lengths).  
  5. Outlet AFCI with metal raceway/conduit.  
  6. Outlet AFCI with concrete-encased wiring.  
- **Exception**: Fire alarm systems (not applicable to general bedroom circuits).  

---

### **GFCI Requirements (CEC 210.8)**  
- **GFCI is NOT required** for standard bedroom receptacles.  
- **GFCI is required** in these locations (not typically in bedrooms):  
  - Bathrooms  
  - Garages/outdoors  
  - Kitchens (countertops)  
  - Sinks (within 6 ft)  
  - Crawlspaces/basements  
  - Laundry areas  

---

### **Inspector Note**  
- **AFCI vs. GFCI**:  
  - **AFCI** prevents fires from arcing faults (required in bedrooms).  
  - **GFCI** prevents shocks from ground faults (required in wet/damp locations).  
- **Compliance**: Ensure AFCI protection is installed per 210.12(A) methods. GFCI is unnecessary for standard bedroom circuits unless receptacles are in a GFCI-mandated location (e.g., a bathroom within the bedroom).  

[OK] Source: CEC 2022

---

### cec2022-005

**Original ID:** baseline-005 | **Category:** table_lookup | **Tier:** baseline

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 9.6s | **Iterations:** 4

**Tools Called:** cec_search, cec_lookup_conductor_ampacity

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Answer:**  
Yes, aluminum conductors can be used for a 200A service. The required size is **250 kcmil aluminum** at 75°C, based on Table 310.16 ampacity.

---

### **Step-by-Step Verification:**

1. **Material Permissibility:**  
   - **CEC 2022 Section 310.3(B)** explicitly allows aluminum conductors for service applications.  
   - **CEC 2022 Section 230.31(B)** specifies a minimum size of 6 AWG aluminum for underground service conductors, but this does not limit overhead or other installations.

2. **Ampacity Determination:**  
   - **Table 310.16** (General Use Ampacity) is used for sizing service conductors.  
   - For **200A**, the minimum aluminum conductor size with a 75°C termination rating is **250 kcmil** (200A at 75°C).  

3. **Termination Temperature Compliance:**  
   - **Section 110.14(C)** requires conductors to be sized based on the lowest termination temperature rating (typically 75°C for service equipment).  
   - 250 kcmil aluminum at 75°C provides **200A ampacity**, matching the 200A service requirement.

4. **Overcurrent Protection Compliance:**  
   - **Section 240.4(D)** allows 200A overcurrent protection for 250 kcmil aluminum (ampacity = 200A).  

---

### **Final Answer:**  
- **Conductor Material:** Aluminum (permitted by 310.3(B))  
- **Size:** 250 kcmil aluminum (200A at 75°C, Table 310.16)  

[OK] Source: CEC 2022

---

### cec2022-006

**Original ID:** baseline-006 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 15.6s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes
**Protection Enforced:** No

**Answer:**

## Dedicated Working Space (CEC 2022)

**Section 110.26(B):**  
*The working space required by 110.26(A) shall be provided in addition to the clear space required by 240.24(D) and 240.24(E).*

### Key Details:
- **Dedicated Space:** The working space in front of the panel must be **clear of all obstructions** (e.g., no storage, furniture, or other equipment).
- **Vertical Clearance:** Requires **6.5 feet (78 inches)** of vertical space above the floor where a person would stand to work on the equipment (not the panel's mounting height).
- **Horizontal Clearance:** The 3-foot depth (from Table 110.26(A)(1)) must be maintained **in all directions** around the panel, including above and below (if applicable).

### Why This Matters:
Even if the depth requirement is met, failing to provide **unobstructed vertical and horizontal space** violates the code. This ensures safe access for maintenance and emergency operations.

[OK] Source: CEC 2022 (Section 110.26(B))

---

### cec2022-007

**Original ID:** baseline-007 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 7.1s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Number of 20-Ampere Small Appliance Branch Circuits for a Kitchen (CEC 2022)

**Answer:**  
A minimum of **two 20-ampere small-appliance branch circuits** are required for the kitchen area of a dwelling unit.  

**Code Basis:**  
- **CEC 2022 Section 210.11(C)(1):**  
  *"In addition to the lighting and general-use receptacle branch circuits required by 210.7, at least two 20-ampere small-appliance branch circuits shall be provided for the kitchen, including the dining room and pantry areas."*  

**Key Details:**  
- These circuits must serve **all wall and floor receptacles** in the kitchen, as well as **countertop receptacles**.  
- The load for each circuit is calculated at **1,500 volt-amperes** (per 220.52(A)), but the **number of circuits is mandated by 210.11(C)(1)**.  

[OK] Source: CEC 2022

---

### cec2022-008

**Original ID:** baseline-008 | **Category:** knowledge_simple | **Tier:** baseline

**Question:** Is surge protection required for a new 200A residential service?

**Duration:** 6.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is **required** for a new 200A residential service under **CEC 2022 Section 230.67**.  

### Key Requirements:
1. **Mandatory SPD Installation**  
   - **Section 230.67(A):** All services supplying dwelling units *must* include a **surge-protective device (SPD)**.  
   - **Type Requirement (C):** The SPD must be **Type 1** (service entrance) or **Type 2** (branch panel).  

2. **Location**  
   - **Section 230.67(B):** The SPD must be:  
     - An integral part of the service equipment, or  
     - Installed immediately adjacent to it.  
   - *Exception:* If located downstream (e.g., at branch panels), it must still comply with all SPD requirements.  

3. **Replacement Compliance**  
   - **Section 230.67(D):** If the service equipment is replaced, the SPD requirements apply to the new installation.  

### Additional Notes:
- **Section 230.94** permits SPDs on the supply side of the service disconnect but does not override the mandatory requirement in 230.67 for dwelling units.  
- **Section 230.209** references surge arresters for overhead service conductors but does not replace SPD requirements for residential services.  

**Inspector Note:** Verify the SPD is listed for the application and installed per manufacturer instructions.  

[OK] Source: CEC 2022

---

### cec2022-009

**Original ID:** core-001 | **Category:** multi_article | **Tier:** core

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 14.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Service Conductor Sizing for 200A Service (CEC 2022)

### Load Calculation Summary
1. **General Lighting/Receptacles**: 3,000 sq ft × 3 VA/ft² = **9,000 VA**
2. **Small Appliance Circuits**: 3 circuits × 1,500 VA = **4,500 VA**
3. **Range**: 12 kW (12,000 VA) → **8,000 VA** (per Table 220.55 demand factor)
4. **Dryer**: 5.5 kW → **5,000 VA** (minimum 5 kW per 220.54)
5. **Water Heater**: 4.5 kW = **4,500 VA**
6. **Central AC**: 4 tons ≈ **8,000 VA** (estimated 2 kW/ton)

**Total Load**:  
9,000 + 4,500 + 8,000 + 5,000 + 4,500 + 8,000 = **39,000 VA**  
Demand Factor: 100% first 10 kVA + 40% remainder = **21,600 VA**  
**Service Size**: 21,600 VA ÷ 240V = **90A** (minimum service size), but user is upgrading to **200A**.

---

### Conductor Sizing
**Required Ampacity**: 200A (per service rating).

#### **Copper Conductors**  
- **4/0 AWG**: 200A at 75°C (Table 310.12(A) for dwelling units).  
- **Minimum Size**: 8 AWG (Section 230.31(B)), but 4/0 is required for 200A.

#### **Aluminum Conductors**  
- **250 kcmil**: 200A at 75°C (Table 310.12(A)).  
- **Minimum Size**: 6 AWG (Section 230.31(B)), but 250 kcmil is required for 200A.

---

### Final Answer
- **Service Conductors**:  
  - **Copper**: **4/0 AWG** (200A at 75°C)  
  - **Aluminum**: **250 kcmil** (200A at 75°C)  
- **Allowable Material**: **Yes**, aluminum is permitted if using 250 kcmil.  

**Source**: CEC 2022 Sections 220.82, 230.31(B), Tables 220.55, 310.12(A)  

[OK] Source: CEC 2022

---

### cec2022-010

**Original ID:** core-002 | **Category:** multi_article | **Tier:** core

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the requirements for the circuit breaker and neutral termination?

**Duration:** 13.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Multiwire Branch Circuit Requirements (CEC 2022)

### Circuit Breaker Requirements
1. **Simultaneous Disconnection**  
   - **Section 210.4(B)**: The disconnecting means (breaker) must **simultaneously disconnect all ungrounded (hot) conductors**.  
   - **Implementation**: Use a **2-pole breaker** or **handle-tied single-pole breakers** to ensure both hot conductors are disconnected together. This prevents the neutral from carrying unbalanced current if only one hot is disconnected.

2. **Phase Configuration**  
   - The two hot conductors must be connected to **opposite phases (legs)** of the panel. This ensures neutral current cancellation (per standard electrical practice, though not explicitly stated in CEC 2022).

---

### Neutral Termination Requirements
1. **Grouping Conductors**  
   - **Section 210.4(D)**: All conductors (hot, neutral, and ground) of the multiwire branch circuit must be **grouped together** (e.g., in the same cable or raceway).  
   - **12/3 Cable Compliance**: The 12/3 cable (two hots, one neutral, one ground) satisfies this requirement by design.

2. **Neutral Load Capacity**  
   - The neutral conductor must be sized to carry the **maximum unbalanced load** (per standard practice). For 12 AWG copper conductors, the neutral is also 12 AWG, which is appropriate for a 20A circuit.

3. **No Overloading**  
   - The neutral must **not be shared** with other circuits unless they are part of the same multiwire branch circuit (per **Section 210.4(C)**). Overloading the neutral can cause overheating.

---

### Additional Requirements
- **Line-to-Neutral Loads Only** (Section 210.4(C)):  
  The circuit must supply only line-to-neutral loads (e.g., 120V receptacles). This applies to kitchen receptacles.
- **No Exceptions for Kitchens**:  
  Exceptions in 210.4(C) (e.g., single utilization equipment) do not apply here, as the circuit serves multiple receptacles.

---

[OK] Source: CEC 2022

---

### cec2022-011

**Original ID:** core-003 | **Category:** knowledge | **Tier:** core

**Question:** Where is GFCI protection required in a residential dwelling? List all locations.

**Duration:** 20.8s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes

**Answer:**

## GFCI and AFCI Protection Requirements in Residential Dwellings (CEC 2022)

---

### **GFCI Protection (Section 210.8)**  
**Required for all 120–250V receptacles in these locations:**  
1. Bathrooms  
2. Garages/accessory buildings (at or below grade)  
3. Outdoors  
4. Crawl spaces (at or below grade)  
5. Basements  
6. Kitchens (countertop surfaces)  
7. Sinks (within 6 ft of bowl edge)  
8. Boathouses  
9. Bathtubs/showers (within 6 ft of edge)  
10. Laundry areas  
11. Indoor damp/wet locations  

**Exceptions:**  
- Receptacles for fire alarm systems (per 760.41/760.121).  
- Listed locking receptacles for ceiling fans/luminaires (not general-purpose).  

---

### **AFCI Protection (Section 210.12)**  
**Required for all 120V, 15/20A branch circuits in these areas:**  
1. Kitchens  
2. Family rooms  
3. Dining rooms  
4. Living rooms  
5. Parlors  
6. Libraries  
7. Dens  
8. Bedrooms  
9. Sunrooms  
10. Recreation rooms  
11. Closets  
12. Hallways  
13. Laundry areas  
14. Similar rooms/areas  

**Exceptions:**  
- Branch circuits supplying fire alarm systems installed per 760.41(B) or 760.121(B).  

---

### **Key Notes**  
- **Dual Protection:** Circuits in kitchens, bathrooms, laundry areas, etc., often require **both GFCI and AFCI** protection.  
- **AFCI Installation Options:**  
  - Combination-type AFCI at the panel.  
  - Outlet branch-circuit AFCI at the first outlet (with specific wiring constraints).  
- **Fire Alarm Systems:** Exempt from AFCI/GFCI requirements if installed per 760.41/760.121.  

[OK] Source: CEC 2022 Sections 210.8, 210.12

---

### cec2022-012

**Original ID:** core-004 | **Category:** knowledge | **Tier:** core

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Surge Protection Requirements for Residential Service (CEC 2022)

**Requirement:**  
Yes, surge protection is **required** for all new residential services per **CEC 2022 Section 230.67(A)**.

**Installation Locations:**  
1. **Integral to service equipment** (e.g., main panel)  
2. **Immediately adjacent to service equipment**  
3. **Downstream at next level distribution equipment** (Exception allowed if installed at each subsequent level toward the load)

**SPD Type:**  
Must be **Type 1 or Type 2** surge-protective device (SPD) per **230.67(C)**.

**Inspector Note:**  
- Verify SPD is listed for use in services (UL 1449 standard).  
- Confirm location complies with "immediately adjacent" requirement unless using the downstream exception.  

[OK] Source: CEC 2022

---

### cec2022-013

**Original ID:** core-005 | **Category:** edge_cases | **Tier:** core

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet code requirements?

**Duration:** 18.7s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes
**Protection Enforced:** No

**Answer:**

## Panel Installation in Closet (CEC 2022) - Final Answer

**1. Working Space Clearance (Front):**  
- **Required:** 36 inches (3 ft) per Table 110.26(A)(1) for 120V equipment.  
- **Provided:** 24 inches.  
- **Conclusion:** ❌ **Fails** minimum working space depth requirement.  

**2. Panel Location in Closet:**  
- **CEC 240.24(D):** Prohibits panelboards in **clothes closets**.  
- **Clarification:** If this is a **clothes closet**, the installation is **non-compliant** regardless of clearance. General storage closets may be allowed if working space requirements are met, but clothes closets are explicitly prohibited.  

**3. Section 110.26(B) Check:**  
- **Search Result:** No specific "110.26(B)" section exists in CEC 2022. The closest is **110.26(A)** (working space depth/height) and **110.26(B)** is not a defined subsection. The referenced "Spaces About Electrical Equipment" (110.26) emphasizes general access and maintenance requirements already addressed in the working space depth (110.26(A)(1)).  

**4. Water Heater Proximity (Side Clearance):**  
- **No specific code requirement** for lateral clearance to water heaters. However, working space must not be obstructed (110.26(A)(1)).  
- **18 inches** is likely acceptable unless the water heater impedes access to the panel.  

---

### Code Citations:  
- **Working space depth:** CEC Table 110.26(A)(1)  
- **Closet prohibition:** CEC 240.24(D)  

[OK] Source: CEC 2022  

**Inspector Note:**  
- If this is a **clothes closet**, the panel must be relocated.  
- If it’s a **general storage closet**, fix the 24" front clearance to meet 36" minimum.  
- **110.26(B)** does not exist in CEC 2022; all requirements are covered under 110.26(A).

---

### cec2022-014

**Original ID:** core-006 | **Category:** edge_cases | **Tier:** core

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 8.5s | **Iterations:** 4

**Tools Called:** cec_search, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

[VERIFIED] Answer is complete.  

The exceptions to **110.3(B)** found in the search do not apply to the scenario of connecting multiple conductors to a single terminal. The relevant exception would require the terminal to be explicitly marked for multiple conductors, which is not the case here. The answer remains accurate under **CEC 2022 Section 110.3(B)**.

---

### cec2022-015

**Original ID:** core-007 | **Category:** grounding_bonding | **Tier:** core

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 8.4s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

### Configuration Requirements:
1. **No Grounding Electrode Required**  
   - The subpanel in the detached garage **must not** have a local grounding electrode (e.g., ground rod). Grounding is provided through the **4-wire feeder** from the main panel (CEC 250.24(D)).

2. **Separate Neutral and Ground Bars**  
   - **Neutral (grounded) conductor** from the main panel connects to the **neutral bar** in the subpanel.  
   - **Equipment grounding conductor (EGC)** from the main panel connects to the **grounding bar** in the subpanel.  
   - **No bonding** between neutral and ground bars in the subpanel (CEC 250.4(A)(3)).  

3. **Bonding of Metal Parts**  
   - All metal parts of the subpanel (enclosure, busbars) must be bonded to the **equipment grounding conductor** from the main panel (CEC 250.4(A)(2)).  

4. **Grounding Electrode Conductor (GEC)**  
   - The GEC is only required at the **main service**. The subpanel derives its grounding through the EGC in the feeder (CEC 250.24(D)).  

---

### Key Code References:
- **CEC 250.24(D):** Prohibits reconnecting the grounded (neutral) conductor to a grounding electrode on the load side of the service disconnect.  
- **CEC 250.30(B):** Applies to separately derived systems (not this case), but reinforces the need for proper bonding.  
- **CEC 250.4(A)(3):** Requires bonding of equipment to establish an effective ground-fault current path.  

---

### Inspector Note:
- Verify the feeder includes a **4-wire configuration** (two ungrounded, one grounded, one EGC).  
- Confirm the subpanel’s **neutral and ground bars are isolated** (not bonded together).  
- Ensure no local ground rods or electrodes are connected to the subpanel.  

[OK] Source: CEC 2022

---

### cec2022-016

**Original ID:** core-008 | **Category:** grounding_bonding | **Tier:** core

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 7.3s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### **Definitions**
- **Main Bonding Jumper** (CEC 2022 Section 100):  
  Connects the **grounded circuit conductor** (neutral) to the **equipment grounding conductor** at the **service**. Ensures electrical continuity between the grounded conductor and the equipment grounding system at the service entrance.

- **System Bonding Jumper** (CEC 2022 Section 100):  
  Connects the **grounded conductor** to the **supply-side bonding jumper** or **equipment grounding conductor** at a **separately derived system** (e.g., transformers, generators). Bonds the grounded conductor of the derived system to its equipment grounding system.

---

### **Key Differences**
| Feature | **Main Bonding Jumper** | **System Bonding Jumper** |
|---------|--------------------------|---------------------------|
| **Application** | At the **service** (utility connection) | At **separately derived systems** (e.g., transformers, generators) |
| **Purpose** | Bonds grounded conductor to equipment grounding conductor **at the service** | Bonds grounded conductor to equipment grounding conductor **at a separately derived system** |
| **Required By** | CEC 250.28(D) for services | CEC 250.28(D) for separately derived systems |
| **Sizing** | Based on the **largest ungrounded service conductor** (Table 250.102(C)(1)) | Based on the **largest ungrounded conductor** of the derived system (Table 250.102(C)(1)) |

---

### **When Each Is Required**
1. **Main Bonding Jumper**  
   - **Required at every service** (CEC 250.28).  
   - Used to ensure the grounded conductor (neutral) is bonded to the equipment grounding system **at the service point**.  
   - Example: A residential service panel requires a main bonding jumper to connect the neutral bus to the grounding electrode conductor.

2. **System Bonding Jumper**  
   - **Required at every separately derived system** (CEC 250.28).  
   - Used to bond the grounded conductor of the derived system to its equipment grounding system.  
   - Example: A 480V-to-208V transformer requires a system bonding jumper to connect its secondary neutral to the equipment grounding conductor.

---

### **Sizing Requirements**
Both jumpers are sized per **Table 250.102(C)(1)** based on the largest ungrounded conductor in the system.  
Example:  
- For a service with **4/0 AWG copper service conductors**, the main bonding jumper must be **4 AWG copper** (Table 250.102(C)(1)).  
- For a separately derived system with **350 kcmil aluminum conductors**, the system bonding jumper must be **2/0 AWG copper** (Table 250.102(C)(1)).

---

### **Inspector Notes**
- **Main bonding jumpers** are **not required** at separately derived systems (use system bonding jumpers instead).  
- **System bonding jumpers** are **not required** at services (use main bonding jumpers instead).  
- Both must be made of **copper, aluminum, copper-clad aluminum, or corrosion-resistant material** (CEC 250.28(A)).  
- Screws used as bonding jumpers must have a **visible green finish** (CEC 250.28(B)).

[OK] Source: CEC 2022

---

### cec2022-017

**Original ID:** core-009 | **Category:** load_calculations | **Tier:** core

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 5.8s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

**Minimum Required Circuits:**  
- **2 circuits**: CEC 2022 Section 210.11(C)(1) requires **at least two 20-ampere small-appliance branch circuits** for all receptacle outlets in kitchens, including countertop and wall receptacles.

**Dining Room Receptacles:**  
- **Yes**, these circuits can also serve dining room receptacles.  
  - Per CEC 2022 Section 210.52(B)(1), small-appliance branch circuits serving kitchens **shall also be permitted to supply receptacle outlets in other rooms** specified in 210.52(B)(1) (including dining rooms).  
  - **Limitation**: No small-appliance branch circuit shall serve more than **one kitchen** (CEC 210.52(B)(1)).

**Key Requirements:**  
1. **Dedicated Use**: These circuits must serve only the specified small-appliance receptacles (kitchen countertops, dining room, etc.) and **not** general lighting or other loads (CEC 210.23(A) exceptions).  
2. **Load Calculation**: Each circuit is calculated at 1,500 VA (CEC 220.52(A)).  

[OK] Source: CEC 2022

---

### cec2022-018

**Original ID:** core-010 | **Category:** load_calculations | **Tier:** core

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 5.5s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

1. **Base Ampacity**:  
   12 AWG THHN copper at 90°C = **30A** (Table 310.16)

2. **Temperature Correction**:  
   50°C ambient → 0.82 correction factor (Table 310.15(B)(1)(1))  
   30A × 0.82 = **24.6A**

3. **Bundling Adjustment**:  
   6 current-carrying conductors → 0.8 adjustment factor (Table 310.15(C)(1))  
   24.6A × 0.8 = **19.7A**

**Final Adjusted Ampacity**: **19.7 amperes**

[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)

---

### cec2022-019

**Original ID:** core-011 | **Category:** why_questions | **Tier:** core

**Question:** Why is AFCI protection required for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 13.5s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes

**Answer:**

## AFCI vs. GFCI Protection in Dwelling Units (CEC 2022)

**Clarification of Requirements:**

1. **AFCI Protection (Section 210.12):**  
   - **Required for:** All 120V, 15/20A circuits in bedrooms, living rooms, hallways, and similar areas.  
   - **Purpose:** Prevents **electrical fires** caused by arc faults (e.g., damaged wiring, loose connections).  

2. **GFCI Protection (Section 210.8):**  
   - **Not required** for general receptacles in bedrooms or living rooms.  
   - **Required in specific locations:** Bathrooms, kitchens (countertops), outdoors, garages, and within 6 ft of sinks or bathtubs.  
   - **Purpose:** Prevents **electrical shocks** from ground faults (e.g., water contact, appliance malfunctions).  

**Inspector Note:**  
- **AFCI** addresses *fire hazards* from arcs in wiring.  
- **GFCI** addresses *shock hazards* from current leakage to ground.  
- **No overlap requirement** for GFCI in bedrooms/living areas unless they contain wet locations (e.g., a bathroom within the living space).  

[OK] Source: CEC 2022

---

### cec2022-020

**Original ID:** core-012 | **Category:** why_questions | **Tier:** core

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 6.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

**Why Torque Specifications Are Important:**
1. **Prevents Loose Connections** – Proper torque ensures conductors are securely fastened, reducing risk of arcing, overheating, and connection failure.
2. **Avoids Over-Tightening** – Excessive torque can damage terminals, conductors, or insulation, compromising electrical integrity.
3. **Manufacturer Requirements** – Equipment is designed with specific torque values to ensure compatibility with termination hardware and conductor types.

**Code Requirements:**
- **CEC 2022 Section 110.14(D)** explicitly requires:
  - Torque values must match those indicated on equipment or in manufacturer instructions.
  - Approved methods (e.g., torque tools, shear bolts) must be used to achieve specified torque.
  - If torque values are not marked, contact the equipment manufacturer for guidance.

- **CEC 2022 Section 430.9(C)** adds:
  - Control circuit devices with screw-type terminals using 14 AWG or smaller copper conductors must be torqued to **minimum 0.8 N·m (7 lb-in.)** unless otherwise specified.

**Key Citations:**
- **110.14(D)** – General requirement for terminal connection torque.
- **430.9(C)** – Specific requirement for control circuit devices.
- **Informational Notes**:
  - UL 486A-486B Annex I provides torque values if manufacturer data is unavailable.
  - NFPA 70B offers guidance on torquing threaded connections.

[OK] Source: CEC 2022

---

### cec2022-021

**Original ID:** inspection-001 | **Category:** panel_load_calculation | **Tier:** inspection

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 14.2s | **Iterations:** 4

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Service Load Calculation (CEC 2022)

### Step 1: General Lighting Load  
- **3000 sq ft × 3 VA/sq ft** = **9000 VA**  
  *(CEC 220.12(A) for dwelling units)*  

### Step 2: Small Appliance Circuits  
- **2 circuits × 1500 VA** = **3000 VA**  
  *(CEC 220.12(B) for small appliance circuits)*  

### Step 3: Laundry Circuit  
- **1 circuit × 1500 VA** = **1500 VA**  
  *(CEC 220.12(C) for laundry circuits)*  

### Step 4: Range Load (Demand Factor Applied)  
- **12,000 VA range**  
  - First 10,000 VA at 100% = **10,000 VA**  
  - Remaining 2,000 VA at 40% = **800 VA**  
  - **Total range load** = **10,800 VA**  
  *(CEC 220.55 for ranges)*  

### Step 5: Dryer Load  
- **5,500 VA dryer** (100% of nameplate rating)  
  *(CEC 220.54 for dryers)*  

### Step 6: Air Conditioning Load  
- **4600 VA AC** (larger of heating/AC)  
  *(CEC 220.60 for heating/AC)*  

### Step 7: Total Load Calculation  
**Total VA** =  
9000 (lighting) + 3000 (small appliance) + 1500 (laundry) + 10,800 (range) + 5,500 (dryer) + 4,600 (AC) = **34,400 VA**  

### Step 8: Convert to Amperes  
- **Service voltage** = 240V (standard for residential)  
- **Total amps** = 34,400 VA ÷ 240V ≈ **143.3A**  

### Final Determination  
- **200A service panel** is **adequately sized** (143.3A ≤ 200A).  
- **Minimum service size** for dwelling units is 100A (CEC 220.82), so 200A exceeds requirements.  

[OK] Source: CEC 2022

---

### cec2022-022

**Original ID:** inspection-002 | **Category:** clearance_violations | **Tier:** inspection

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL code violations.

**Duration:** 96.6s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search, cec_search, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes
**Protection Enforced:** No

**Answer:**

## Verification of 110.26(B) (CEC 2022)

**Section 110.26(B) Prohibition:**  
> *"Working space required by this section shall not be used for storage. When normally enclosed live parts are exposed for inspection or servicing, the working space, if in a passageway or general open space, shall be suitably guarded."*

**Application to This Case:**  
- The **water heater located 16 inches within the working space** violates the "no storage" rule in 110.26(B).  
- Even if the panel is enclosed, the water heater obstructs the required clear working space.  

**Inspector Note:**  
This obstruction creates a **safety hazard** by limiting access and increasing fire risk. The violation is **not conditional**—storage is strictly prohibited in working spaces regardless of panel status.  

---

### Final Code Violations (Confirmed):  
1. **Working space depth** (28 in < 36 in required) – **110.26(A)(1)**  
2. **Obstruction in working space** (water heater) – **110.26(B)**  
3. **Vertical clearance** (verify ceiling height ≥ 6.5 ft) – **110.26(A)(3)**  

No additional violations from 110.26(B) beyond the obstruction issue.  

[OK] Source: CEC 2022

---

### cec2022-023

**Original ID:** inspection-005 | **Category:** gfci_afci_compliance | **Tier:** inspection

**Question:** New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide code references.

**Duration:** 23.9s | **Iterations:** 5

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** Yes

**Answer:**

## Circuit Protection Requirements for Kitchen Installations (CEC 2022)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **CAFCI (Combination Arc-Fault + GFCI)**
- **Code References**:
  - **GFCI**: CEC 2022 **210.8(A)(6)** (kitchen countertop receptacles require GFCI).
  - **AFCI**: CEC 2022 **210.12(A)** (all 120V, 15/20A dwelling circuits require AFCI).

### 2. **Dishwasher (Dedicated 15A Circuit)**
- **Protection Required**: **CAFCI**
- **Code References**:
  - **GFCI**: CEC 2022 **210.8(A)(6)** (appliances in kitchens require GFCI).
  - **AFCI**: CEC 2022 **210.12(A)** (no exception for appliances).

### 3. **Garbage Disposal (Dedicated 15A Circuit)**
- **Protection Required**: **CAFCI**
- **Code References**:
  - **GFCI**: CEC 2022 **210.8(A)(6)** (appliances in kitchens require GFCI).
  - **AFCI**: CEC 2022 **210.12(A)** (no exception for appliances).

### 4. **Refrigerator (Dedicated 20A Circuit)**
- **Protection Required**: **AFCI Only**
- **Code References**:
  - **GFCI**: **Not required** if the receptacle is **not within 1.8 m (6 ft)** of a sink (CEC 2022 **210.8(A)(7)**).
  - **AFCI**: CEC 2022 **210.12(A)** (required for all 120V, 15/20A dwelling circuits).

---

### Inspector Notes:
- **CAFCI Breakers**: Use combination arc-fault + GFCI breakers for countertop, dishwasher, and garbage disposal circuits.
- **Refrigerator Exception**: GFCI is **not required** if the receptacle is **not within 6 ft of a sink**. AFCI is still required.
- **AFCI Exceptions**: No exceptions apply for AFCI in dwelling units (only fire alarm systems are exempt, which is irrelevant here).

[OK] Source: CEC 2022

---

### cec2022-024

**Original ID:** inspection-006 | **Category:** subpanel_violations | **Tier:** inspection

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 7.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Subpanel Grounding and Bonding Violations (CEC 2022)

### **Identified Violations:**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation:** CEC 2022 Section 250.4(B)(1) requires **separate neutrals and grounds** in subpanels (not service equipment). Bonding these bars creates a parallel ground path and risks objectionable current on grounding conductors.  
   - **Correct Configuration:** Neutral and ground bars must be **electrically isolated** in subpanels. The main bonding jumper (which connects neutral and ground) is **only permitted in the main service** (CEC 250.24(B)).

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation:** CEC 250.104(A) mandates that **only the equipment grounding conductor** (not neutral) connects to the enclosure. Bonding the neutral bar to the enclosure creates a ground loop and violates the requirement for a single, intentional bonding point.  
   - **Correct Configuration:** The **ground bar** (not neutral bar) must be bonded to the metal enclosure. Neutrals should only connect to the main service panel.

3. **Main Bonding Jumper Installed in Subpanel**  
   - **Violation:** The main bonding jumper (which connects neutral and ground) is **only allowed in the main service** (CEC 250.24(B)). Its presence in a subpanel creates a duplicate bonding point, risking ground faults.  
   - **Correct Configuration:** Remove the main bonding jumper from the subpanel. Neutrals in the subpanel must **only connect to the feeder neutral** (which ties back to the main panel’s neutral bar).

---

### **Correct Subpanel Configuration for Detached Garage:**
1. **Neutral and Ground Separation**  
   - **Neutral Bar:** Connected only to the **feeder neutral conductor** (from main panel).  
   - **Ground Bar:** Connected to:  
     - **Feeder ground conductor** (from main panel).  
     - **Grounding electrode conductor** (e.g., #6 copper to ground rod).  
   - **No bonding** between neutral and ground bars.

2. **Enclosure Bonding**  
   - The **ground bar** is bonded to the metal enclosure via a **screw or bonding jumper** (CEC 250.104(A)).  
   - **Neutral bar** remains **unbonded** to the enclosure.

3. **Grounding Electrode System**  
   - A **separate grounding electrode** (e.g., ground rod) is required for the detached subpanel (CEC 250.32(B)).  
   - The grounding electrode conductor (GEC) connects the ground bar to the electrode (size per CEC Table 250.66 based on feeder size).

---

### **Inspector Notes:**
- **Violation (1):** Neutral-ground bonding in subpanel creates a parallel path for fault currents.  
- **Violation (2):** Neutral-to-enclosure bonding risks energizing the enclosure during faults.  
- **Violation (3):** Main bonding jumper in subpanel violates CEC 250.24(B).  

**Corrected Configuration:**  
- Neutral and ground bars **separated**.  
- Ground bar bonded to enclosure and connected to grounding electrode.  
- Neutral bar isolated and connected only to feeder neutral.  

[OK] Source: CEC 2022 Sections 250.24, 250.4, 250.104

---

### cec2022-025

**Original ID:** inspection-007 | **Category:** conduit_fill | **Tier:** inspection

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 11.0s | **Iterations:** 3

**Tools Called:** cec_lookup_conduit_fill

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Calculation:**
1. **Conduit Fill Limitation**  
   - RMC 1¼" total area: **1.526 sq in** (Chapter 9 Table 4)  
   - 40% fill limit for multiple conductors:  
     $ 1.526 \times 0.40 = 0.61 \, \text{sq in} $

2. **Conductor Area**  
   - 10 AWG THHN area: **0.0211 sq in** (Chapter 9 Table 5)

3. **Maximum Conductors**  
   $ \frac{0.61}{0.0211} = 28.91 $ → **28 conductors** (rounded down)

**Verification:**  
- Total conductor area: $ 28 \times 0.0211 = 0.5908 \, \text{sq in} $  
- Fill percentage: $ \frac{0.5908}{1.526} \times 100 = 38.7\% $ (≤ 40% allowed)

**Answer:**  
**28 conductors** can be installed in 1¼" RMC at 40% fill.

[OK] Source: CEC 2022 Chapter 9 Tables 4 and 5

---

### cec2022-026

**Original ID:** inspection-008 | **Category:** voltage_drop | **Tier:** inspection

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet the 3% maximum recommendation for branch circuits?

**Duration:** 8.8s | **Iterations:** 5

**Tools Called:** python_calculator, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Voltage Drop Compliance (CEC 2022)

**Voltage drop calculation**:  
- **2.84 volts (2.37%)** as calculated above  

**Code verification**:  
- **CEC 2022 Section 210.19(A)** (Informational Note 3) explicitly states:  
  > *"Conductors for branch circuits... sized to prevent a voltage drop exceeding 3 percent at the farthest outlet... provide reasonable efficiency of operation."*  

**Conclusion**:  
- **2.37% voltage drop** is **within the 3% recommendation** for branch circuits.  
- This installation complies with CEC 2022 efficiency guidelines.  

[OK] Source: CEC 2022

---

### cec2022-027

**Original ID:** inspection-009 | **Category:** derating_calculation | **Tier:** inspection

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 9.1s | **Iterations:** 6

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG TW copper conductors at 60°C: **20A** (Table 310.16)

**Step 2: Temperature Correction**  
Ambient temperature = 43°C  
Correction factor from Table 310.15(B)(1)(1): **0.71**

**Step 3: Bundling Adjustment**  
6 current-carrying conductors  
Adjustment factor from Table 310.15(C)(1): **0.80**

**Step 4: Combined Calculation**  
Adjusted ampacity = 20A × 0.71 × 0.80 = **11.36A**

**Final Answer:**  
The adjusted ampacity is **11.36 amperes** after applying both temperature correction and bundling adjustment factors.

[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)

---

### cec2022-028

**Original ID:** inspection-010 | **Category:** grounding_electrode_conductor | **Tier:** inspection

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Minimum Size Copper GEC for 1000 kcmil Service (CEC 2022)

**Answer:**  
The minimum size copper grounding electrode conductor (GEC) required is **2/0 AWG** per **CEC Table 250.66**.

**Key Details:**  
- **Service Conductor Equivalent Size:** 1000 kcmil (4 × 250 kcmil parallel conductors)  
- **Table 250.66 Reference:** For service conductors "Over 600 through 1100 kcmil," the required copper GEC is **2/0 AWG**.  

**Exceptions (Not Applicable Here):**  
- If the grounding electrode is a **ground rod, pipe, or plate electrode**, the GEC could be reduced to **6 AWG copper** (per 250.66(A)).  
- If the grounding electrode is **concrete-encased**, the GEC could be reduced to **4 AWG copper** (per 250.66(B)).  

Since the electrode type is unspecified, the general requirement of **2/0 AWG copper** applies.  

[OK] Source: CEC 2022 Table 250.66

---

### cec2022-029

**Original ID:** cec-001 | **Category:** panelboard_requirements | **Tier:** california_specific

**Question:** What are the panelboard space requirements for single-family dwellings? What appliances must have reserved circuit breaker spaces?

**Duration:** 7.9s | **Iterations:** 3

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Panelboard Space Requirements and Reserved Circuit Breaker Spaces (CEC 2022)

### **Panelboard Space Requirements for Single-Family Dwellings**
1. **Reserved Circuit Breaker Spaces** (CEC 2022 Section 408.2(A)):
   - Panelboards in **single-family residential buildings** must include dedicated circuit breaker spaces for:
     - **Heat pump water heaters**
     - **Heat pump space heaters**
     - **Electric cooktops**
     - **Electric clothes dryers**
   - These requirements are specified in the **California Energy Code Section 150.0(n), (t), (u), and (v)**.

2. **Maximum Number of Overcurrent Devices** (CEC 2022 Section 408.54):
   - Panelboards must have **physical barriers** to prevent exceeding the manufacturer-rated number of overcurrent devices.
   - A 2-pole breaker counts as **2 devices**, and a 3-pole breaker counts as **3 devices**.

3. **Overcurrent Protection** (CEC 2022 Section 408.36):
   - Panelboards must be protected by an overcurrent device rated **no higher than the panelboard’s rating**.
   - Exceptions allow protection via two main breakers/fuses (combined rating ≤ panelboard rating), but such panelboards cannot exceed **42 overcurrent devices**.

---

### **Appliances Requiring Reserved Circuit Breaker Spaces**
The following appliances **must have dedicated circuit breaker spaces** in single-family dwellings:
- **Heat pump water heaters** (for energy-efficient water heating)
- **Heat pump space heaters** (for heating systems)
- **Electric cooktops** (ranges or cooktops)
- **Electric clothes dryers** (clothes dryers)

These requirements are **California-specific amendments** under the **California Energy Code** to ensure compatibility with energy-efficient appliances.

---

### **Key Code Citations**
- **CEC 2022 Section 408.2(A)**: Mandates reserved spaces for listed appliances in single-family dwellings.
- **CEC 2022 Section 408.54**: Limits overcurrent device count to prevent panelboard overloading.
- **California Energy Code Section 150.0(n), (t), (u), (v)**: Specifies appliance types and energy efficiency requirements.

[OK] Source: CEC 2022

---

### cec2022-030

**Original ID:** cec-002 | **Category:** ev_charging | **Tier:** california_specific

**Question:** What are the electrical requirements for EV charging infrastructure in new residential construction?

**Duration:** 9.4s | **Iterations:** 3

**Tools Called:** cec_search, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Electrical Requirements for EV Charging in New Residential Construction (CEC 2022)

### 1. **Code Compliance Mandates**
- **CEC Article 625** governs EV charging systems, with additional requirements from **CALGreen Code (Chapter 4/5)** for new construction.  
- **625.1.1** explicitly requires compliance with CALGreen for EV infrastructure in residential buildings.

---

### 2. **Dedicated Branch Circuits**
- **625.40**: Each EV charging outlet **must be supplied by an individual branch circuit** with **no other outlets** on the circuit.  
- **Exception**: Not applicable—this rule has no exceptions for residential EV circuits.

---

### 3. **EVSE Location & Installation**
- **625.50**: EVSE must be installed for **direct electrical coupling** to the vehicle.  
  - **Indoor locations**: EVSE coupling means must be at least **450 mm (18 in.) above the floor**.  
  - **Outdoor locations**: Minimum height of **600 mm (24 in.) above grade**.  
  - **Portable EVSE** (per 625.44(A)) is exempt from height requirements.  

- **625.56**: Outdoor EVSE receptacles must have **weatherproof enclosures** rated for wet locations. Enclosures must remain weatherproof even when the attachment plug is removed.

---

### 4. **Ground-Fault Protection**
- **625.60(D)**: **All EVSE receptacles require GFCI protection** for personnel safety.  
- **Exception**: None—GFCI is mandatory for all EV charging circuits.

---

### 5. **Ventilation Requirements**
- **625.52**: Indoor EV charging areas require ventilation if equipment is listed as needing it.  
  - **Ventilation rates** depend on **supply voltage/current** and number of EVs (see Tables 625.52(B)(1)(a) and (b)).  
  - Example: A 240V, 50A circuit for 1 EV requires **9.7 m³/min (342 cfm)** ventilation.  
  - **Interlock requirement**: Ventilation systems must remain energized during charging.

---

### 6. **Panelboard Space Allocation**
- **408.2(A/B)**: California Energy Code mandates **dedicated circuit breaker spaces** in panelboards for:  
  - Heat pump water heaters  
  - Heat pump space heaters  
  - Electric cooktops  
  - Electric clothes dryers  
- **Impact on EV circuits**: Panelboards must include **additional spaces** for EV charging circuits as per load calculations (Article 220).

---

### 7. **Overcurrent Protection**
- **625.48**: EVSE with power export capabilities (bidirectional charging) must be **listed and marked** for the application.  
- **Overcurrent protection** must match the EVSE rating and account for maximum fault current (per 625.60(C)).

---

### 8. **Special Considerations**
- **CALGreen Compliance**: New residential buildings must include **EV-ready infrastructure** (e.g., dedicated circuits and panel spaces) even if EVSE is not yet installed.  
- **Wire Management**: Conduit and panel wiring must accommodate EV circuits, adhering to **Chapter 9 fill requirements** and **312.6(B) bending space** standards.

---

### Summary of Key Tables
- **Table 625.52(B)(1)(a/b)**: Ventilation rates for indoor EV charging (cubic meters/feet per minute).  
- **Table 312.6(B)**: Minimum wire-bending space for panelboard terminations (critical for EV circuit wiring).

---

[OK] Source: CEC 2022, CALGreen Code

---

### cec2022-031

**Original ID:** cec-003 | **Category:** solar_pv | **Tier:** california_specific

**Question:** What are the electrical requirements for solar PV systems on new residential construction?

**Duration:** 11.1s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## California Electrical Code (CEC 2022) Requirements for Solar PV Systems in New Residential Construction

### 1. **Scope and General Requirements**  
- **Article 690.1** applies to all solar PV systems, including arrays, inverters, and controllers. Systems must be **listed/evaluated equipment** (690.4(B)) and installed by **qualified personnel** (690.4(C)).  
- **Interactive systems** (grid-tied) and **stand-alone systems** are permitted.  

---

### 2. **Rapid Shutdown Requirements**  
- **690.12** mandates rapid shutdown to reduce shock hazards for firefighters:  
  - **Voltage limits**:  
    - **Outside array boundary (305 mm/1 ft)**: ≤30V within 30 seconds.  
    - **Inside array boundary**: ≤80V within 30 seconds **or** use a listed PV hazard control system.  
  - **Initiation device**: Must be **readily accessible** (e.g., service disconnect, PV disconnect, or labeled switch).  
  - **Exception**: Ground-mounted systems in detached structures (solely for PV equipment) are exempt.  

---

### 3. **Grounding and Bonding**  
- **690.42–690.45**:  
  - **System grounding**: Connect to grounding electrode system per **250.50/250.52**.  
  - **Equipment bonding**: All non-current-carrying metal parts (module frames, support structures) must be bonded per **690.43**.  
  - **Grounding conductor sizing**: Use **Table 250.122** based on overcurrent protection (assume 125% of inverter output for sizing).  

---

### 4. **Wiring Methods and Conductors**  
- **690.31**:  
  - **Conductor types**: Use **Type PV** or **distributed generation (DG) cable** listed for outdoor use.  
  - **Ampacity adjustments**:  
    - Apply **Table 690.31(A)(a)** correction factors for ambient temperature.  
    - Use **Table 690.31(A)(b)** ampacities for 105°C–125°C conductors (e.g., 12 AWG XLPE: 39A at 30°C).  
  - **Protection**:  
    - DC circuits >30V must be in **metal raceways**, **Type MC cable**, or **metal enclosures**.  
    - Exposed DC conductors require **3 mm (1/8 in.) guarding** or protection from physical damage.  

---

### 5. **Arc-Fault Circuit Protection**  
- **690.11**:  
  - **DC circuits ≥80V** must have **listed PV arc-fault circuit interrupters**.  
  - **Exception**: DC circuits in metallic raceways, MC cable, or underground are exempt.  

---

### 6. **Labeling and Identification**  
- **690.56**:  
  - **Rapid shutdown labels**: Permanent labels at service equipment locations with diagrams showing shutdown devices.  
  - **PV circuit identification**: DC conductors must be marked with **+/- polarity** (not green, white, or gray).  
- **690.53**:  
  - **Voltage labels**: Indicate maximum PV system voltage at disconnects or inverters.  

---

### 7. **Special Requirements for Residential Systems**  
- **AC modules** (690.6): Treated as internal components; output circuits follow inverter rules.  
- **Stand-alone systems** (690.10): Follow **Article 710** for battery-based systems.  
- **Multiple PV systems**: Install a **directory** per **705.10** at each disconnect location.  

---

### 8. **Key Tables for Sizing**  
- **Table 690.31(A)(a)**: Temperature correction factors (e.g., 0.89 at 40°C for 105°C conductors).  
- **Table 690.31(A)(b)**: Ampacities for PV conductors (e.g., 12 AWG XLPE: 39A at 30°C).  

---

### Inspector Notes  
- Verify **rapid shutdown initiation device location** (outside for single-family homes).  
- Check **grounding electrode connections** and bonding of module frames.  
- Ensure **arc-fault protection** is installed for DC circuits ≥80V.  

[OK] Source: CEC 2022

---

### cec2022-032

**Original ID:** cec-004 | **Category:** heat_pump | **Tier:** california_specific

**Question:** What circuit requirements exist for heat pump water heaters in new dwelling units?

**Duration:** 11.2s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Circuit Requirements for Heat Pump Water Heaters in New Dwelling Units (CEC 2022)

### 1. **Branch Circuit Sizing**
- **Minimum sizing**: 125% of the water heater's nameplate rating (CEC 2022 **422.13**).  
  Example: A 12A heater requires a circuit rated for at least 15A (12A × 1.25).  
- **Conductor sizing**: Use Table 310.16 for ampacity based on termination temperature (typically 75°C).  
- **Overcurrent protection**:  
  - If the appliance is marked with a specific overcurrent rating, use that value (422.11(A)).  
  - If unmarked, protection shall not exceed 150% of the appliance's rated current (422.11(E)).  
    Example: A 12A heater allows up to 18A OCP (12A × 1.5), but standard breakers require rounding down to 15A or up to 20A (if 18A is unavailable).  

### 2. **Dedicated Circuit Requirement**
- Heat pump water heaters must be supplied by an **individual branch circuit** (422.10(A)).  
- No other loads may be connected to this circuit.  

### 3. **Disconnecting Means**
- The branch-circuit switch or circuit breaker must serve as the disconnecting means and comply with:  
  - **Visibility/Accessibility**: Within sight of the heater or lockable in the open position (422.31).  
  - **Indicating type**: Switches/circuit breakers must show "on" or "off" status (422.35).  

### 4. **Nameplate Compliance**
- The appliance must have a visible nameplate with voltage, amperage, and wattage (422.60(A)).  
- Use the nameplate rating for load calculations (220.55 for ranges is not applicable here).  

### 5. **Additional Considerations**
- **Temperature-limiting means**: Required for storage-type heaters (422.47), but this is a safety feature, not a circuit requirement.  
- **GFCI Protection**: Not explicitly required for water heaters unless located in specific areas (e.g., garages). Check **210.8(D)** for GFCI requirements in dwelling units.  

---

**Inspector Note**: Always verify the appliance's nameplate for manufacturer-specific requirements (422.60). For example, a heat pump water heater rated 15A at 240V would require:  
- **Conductors**: 10 AWG copper (30A ampacity at 75°C, Table 310.16).  
- **Overcurrent protection**: 20A breaker (15A × 1.5 = 22.5A; next standard size is 20A).  

[OK] Source: CEC 2022

---

### cec2022-033

**Original ID:** cec-005 | **Category:** electrification | **Tier:** california_specific

**Question:** What is required for electric cooktop readiness in new homes?

**Duration:** 7.1s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Electric Cooktop Readiness in New Homes (CEC 2022)

**Requirement:**  
New residential construction in California must provide **dedicated circuits and circuit identifications** for electric cooktops as follows:

### Single-Family Buildings (1–2 Dwellings)  
- **CEC 2022 Section 422.3(A)**  
  Each dwelling unit must have:  
  - Dedicated circuits and circuit identifications per **California Energy Code Section 150.0(u)**.  

### Multifamily Buildings  
- **CEC 2022 Section 422.3(B)**  
  Each dwelling unit must have:  
  - Dedicated circuits and circuit identifications per **California Energy Code Section 160.9(b)**.  

**Key Notes:**  
- The California Energy Code (referenced in CEC) mandates specific circuit sizing, labeling, and panelboard requirements for cooktop readiness.  
- Compliance ensures future installation of electric cooktops without retrofitting.  

[OK] Source: CEC 2022

---

### cec2022-034

**Original ID:** cec-006 | **Category:** electrification | **Tier:** california_specific

**Question:** What are the panelboard requirements for electric clothes dryer circuits in new construction?

**Duration:** 18.8s | **Iterations:** 4

**Tools Called:** cec_search, cec_lookup_conductor_size

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Panelboard Requirements for Electric Clothes Dryer Circuits (CEC 2022)

**Key Requirements:**

1. **Circuit Breaker Spaces:**
   - **Single-Family Buildings:** Panelboards must include a dedicated circuit breaker space for electric clothes dryers as specified in **California Energy Code Section 150.0**.  
   - **Multifamily Buildings:** Panelboards must include a dedicated circuit breaker space for electric clothes dryers as specified in **California Energy Code Section 160.9(a), (b), and (c)**.  
   - **CEC Reference:** [CEC 2022 Section 408.2(A) and 408.2(B)].

2. **Circuit Sizing:**
   - Dryer circuits must be sized per **NEC 220.54** (typically 30A for residential dryers) and use **4-wire cord and receptacle (240V, 30A)**.  
   - Conductors must be **10 AWG copper** (for 30A circuits) per **Table 310.16**.  

3. **Overcurrent Protection:**
   - Panelboards must be protected by an overcurrent device not exceeding the panelboard’s rating (see **Section 408.36**).  
   - Dryer circuits must comply with **240.6(A)** for standard ratings (e.g., 30A breaker).  

4. **Grounding and Bonding:**
   - Panelboards must have a grounded conductor termination per **Section 408.41**.  
   - Equipment grounding conductors must be connected as required by **Section 408.40**.  

**Inspector Note:** Verify compliance with California Energy Code sections (150.0/160.9) for exact space requirements. Dryer circuits must not share spaces with other high-load appliances unless permitted by code.  

[OK] Source: CEC 2022

---

### cec2022-035

**Original ID:** cec-007 | **Category:** overcurrent | **Tier:** california_specific

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Duration:** 5.7s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## CEC Table 240.4(G) Unique California Provisions

**Answer:**  
CEC Table 240.4(G) itself is not uniquely modified in California (it mirrors NEC Table 240.4(G)), but the **California delta amendment** adds critical context for specific applications referenced in the table. The key California-specific implications are:

1. **Fire Alarm Systems (760.43/760.121):**  
   California mandates stricter overcurrent protection requirements for fire alarm circuits, including specific provisions for battery-backed systems and emergency communication pathways. These are detailed in **CEC 760.43** and **760.121**, which are cross-referenced in Table 240.4(G).

2. **Air-Conditioning/Refrigeration Equipment (440, Parts III, VI):**  
   California's energy efficiency standards (Title 24) influence overcurrent protection for HVAC systems, requiring compliance with both NEC 440 and additional CA energy codes.

3. **Delta Amendment Note:**  
   The table includes a footnote indicating California amendments (delta) to NEC requirements. While the table itself doesn't show modifications, the referenced sections (e.g., 760 for fire alarms) contain California-specific additions.

**Inspector Note:** Always verify cross-referenced sections (like 760.43) for California amendments when applying Table 240.4(G) to specialized systems. The table acts as a guide to where CA-specific rules may apply.

[OK] Source: CEC 2022

---

### cec2022-036

**Original ID:** cec-008 | **Category:** surge_protection | **Tier:** california_specific

**Question:** What does CEC Table 242.3 specify for installations?

**Duration:** 5.5s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## CEC 2022 Table 242.3 - Overvoltage Protection Cross-Reference

**Table 242.3** in the California Electrical Code (CEC) 2022 provides a cross-reference for **overvoltage protection requirements** by equipment type. It directs users to specific NEC articles where additional overvoltage protection rules apply. This table is a **California-specific addition** (marked with an "N") not found in the base NEC.

---

### **Equipment Types and Referenced Articles**
| Equipment Type | Referenced Article |
|----------------|-------------------|
| Class I locations | 501 |
| Class II locations | 502 |
| Community antenna television and radio distribution systems | 820 |
| Critical operations power systems | 708 |
| Elevators, dumbwaiters, escalators, moving walks, platform lifts, and stairway chairlifts | 620 |
| Emergency systems | 700 |
| Equipment over 1000 volts, nominal | 490 |
| Fire pumps | 695 |
| Industrial machinery | 670 |
| Information technology equipment | 645 |
| Modular data centers | 646 |
| Outdoor overhead conductors over 1000 volts | 399 |
| Radio and television equipment | 810 |
| Receptacles, cord connectors, and attachment plugs (caps) | 406 |
| Wind electric systems | 694 |

---

### **Key Notes**
1. **Purpose**: This table helps identify which equipment types require **additional overvoltage protection** beyond general requirements in Article 242.
2. **California-Specific**: The "N" marker indicates this table is added by California amendments to the NEC.
3. **Application**: For example, fire pump installations must comply with **Article 695** for overvoltage protection in addition to general rules.

[OK] Source: CEC 2022

---

### cec2022-037

**Original ID:** cec-009 | **Category:** motor_control | **Tier:** california_specific

**Question:** What does CEC Table 430.72(B) specify for motor control circuit overcurrent protection?

**Duration:** 6.3s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## CEC Table 430.72(B) - Motor Control Circuit Overcurrent Protection (CEC 2022)

**Purpose**: Specifies maximum overcurrent protective device ratings (in amperes) for motor control circuits based on conductor size and installation configuration.

---

### **Table Data**
| Conductor Size | Column A (Copper) | Column A (Aluminum) | Column B (Copper) | Column B (Aluminum) | Column C (Copper) | Column C (Aluminum) |
|----------------|-------------------|---------------------|-------------------|---------------------|-------------------|---------------------|
| 18 AWG         | 7A                | —                   | 25A               | —                   | 7A                | —                   |
| 16 AWG         | 10A               | —                   | 40A               | —                   | 10A               | —                   |
| 14 AWG         | (Note 1)          | —                   | 100A              | —                   | 45A               | —                   |
| 12 AWG         | (Note 1)          | (Note 1)            | 120A              | 100A                | 60A               | 45A                 |
| 10 AWG         | (Note 1)          | (Note 1)            | 160A              | 140A                | 90A               | 75A                 |
| >10 AWG        | (Note 1)          | (Note 1)            | (Note 2)          | (Note 2)            | (Note 3)          | (Note 3)            |

---

### **Key Notes**
1. **Column A**:  
   - For conductors ≤12 AWG, values are fixed (e.g., 7A for 18 AWG copper).  
   - For conductors >10 AWG, see **Note 1** (references 310.15).

2. **Column B**:  
   - For conductors ≤10 AWG, values are fixed (e.g., 25A for 18 AWG copper).  
   - For conductors >10 AWG, values are **400% of Table 310.19 (60°C conductors)** (Note 2).

3. **Column C**:  
   - For conductors ≤10 AWG, values are fixed (e.g., 7A for 18 AWG copper).  
   - For conductors >10 AWG, values are **300% of Table 310.16 (60°C conductors)** (Note 3).

---

### **Critical Cross-References**
- **Table 310.19**: Provides base ampacities for 60°C conductors (used for Column B calculations).  
- **Table 310.16**: Provides base ampacities for 60°C conductors (used for Column C calculations).  

---

### **Application Guidance**
- **Column A**: Typically applies to control circuits with direct-current (DC) or low-voltage alternating-current (AC) applications.  
- **Column B/C**: For higher-power control circuits; Column C uses lower percentages (300%) for added safety margins.  
- **Larger Conductors (>10 AWG)**: Requires referencing Tables 310.16/310.19 and applying the specified multipliers (400% or 300%).

---

[OK] Source: CEC 2022

---

### cec2022-038

**Original ID:** cec-010 | **Category:** medium_voltage | **Tier:** california_specific

**Question:** What medium voltage cable tables exist that are California-specific?

**Duration:** 6.2s | **Iterations:** 3

**Tools Called:** search_tables

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Medium Voltage Cable Tables in CEC 2022

The following California Electrical Code (CEC 2022) tables specifically address medium voltage cable applications (typically 2001V and above):

1. **Table 315.10(A)**  
   *Conductor Application and Insulation Rated 2001 Volts and Higher*  
   - Specifies insulation types and applications for medium voltage conductors.

2. **Table 315.60(C)(10)**  
   *Ampacities of an Insulated Three-Conductor Aluminum Cable in Isolated Conduit in Air*  
   - Provides ampacity ratings for aluminum medium voltage cables in air.

3. **Table 315.60(C)(13)**  
   *Ampacities of Three Insulated Copper Conductors Cabled Within an Overall Covering (Three-Conductor Cable) in Underground Electrical Ducts (One Cable per Electrical Duct)*  
   - For underground copper medium voltage cables in ducts.

4. **Table 315.60(C)(5)**  
   *Ampacities of an Insulated Three-Conductor Copper Cable Isolated in Air*  
   - Air-cooled copper medium voltage cable ampacities.

5. **Table 315.60(C)(6)**  
   *Ampacities of an Insulated Three-Conductor Aluminum Cable Isolated in Air*  
   - Air-cooled aluminum medium voltage cable ampacities.

6. **Table 315.60(C)(9)**  
   *Ampacities of an Insulated Three-Conductor Copper Cable in Isolated Conduit in Air*  
   - Conduit-installed copper medium voltage cable ratings.

---

### Key Notes:
- These tables are part of **Article 315** (Cable Assemblies and Raceway Cable Entries) in CEC 2022.
- They align with NEC standards but are incorporated into California's code with no amendments for these specific tables.
- For California-specific amendments, check **Title 24, Part 8** or CALGreen, but medium voltage cable requirements generally follow NEC without state modifications.

[OK] Source: CEC 2022

---

### cec2022-039

**Original ID:** cec-011 | **Category:** conductor_ampacity | **Tier:** delta_table

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75°C?

**Duration:** 4.1s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

**Ampacity**: **230 amperes** at 75°C for copper conductors (CEC Table 310.16).

**Important Considerations**:
1. **Ambient Temperature**: This value assumes 30°C ambient temperature. For different temperatures, apply correction factors from **310.15(B)**.
2. **Bundling**: If more than three current-carrying conductors are bundled, apply adjustment factors from **310.15(C)(1)**.
3. **Overcurrent Protection**: Per **240.4(D)**, 4/0 AWG copper is typically protected up to 250A, but this depends on termination temperature ratings (see 110.14(C)).

[OK] Source: CEC 2022

---

### cec2022-040

**Original ID:** cec-012 | **Category:** grounding | **Tier:** delta_table

**Question:** What size equipment grounding conductor is required for a 200A circuit?

**Duration:** 4.4s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Equipment Grounding Conductor Size (CEC 2022)

For a **200A circuit**, the required equipment grounding conductor (EGC) sizes are:

- **Copper**: **6 AWG**  
- **Aluminum/Copper-Clad Aluminum**: **4 AWG**  

**Source**: CEC 2022 Table 250.122  

**Important Notes**:  
1. California amendments apply (delta symbol in table).  
2. Footnote: If compliance with **250.4(A)(5)** or **250.4(B)(4)** requires larger conductors (e.g., for ground fault protection), size the EGC accordingly.  
3. Refer to **250.120** for installation restrictions (e.g., mechanical protection, secure connections).  

[OK] Source: CEC 2022

---

### cec2022-041

**Original ID:** cec-013 | **Category:** grounding | **Tier:** delta_table

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor?

**Duration:** 5.0s | **Iterations:** 3

**Tools Called:** cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Grounding Electrode Conductor Size (CEC 2022)

**Required GEC size for 3/0 AWG copper service conductor**:  
**4 AWG copper** (per CEC Table 250.66 for service conductors sized 2/0 or 3/0 AWG copper).

**Exceptions for electrode type limits**:
- If using **ground rod, pipe, or plate electrode**, GEC can be reduced to **6 AWG copper** (250.66(A)).
- If using **concrete-encased electrode**, GEC can be reduced to **4 AWG copper** (250.66(B)).

**Key Notes**:
- Base size is 4 AWG copper unless exceptions apply.
- California amendments (delta) may modify NEC requirements, but Table 250.66 directly addresses this scenario.

[OK] Source: CEC 2022 Table 250.66

---

### cec2022-042

**Original ID:** cec-014 | **Category:** ampacity_adjustment | **Tier:** delta_table

**Question:** What is the temperature correction factor for a 75°C rated conductor at 40°C ambient temperature?

**Duration:** 6.7s | **Iterations:** 4

**Tools Called:** cec_lookup_ampacity_adjustment, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

[VERIFIED] Answer is complete. The temperature correction factor of 0.88 from CEC Table 310.15(B)(1)(1) is correct for 75°C conductors at 40°C ambient. The exceptions found during verification (352.60, 356.60, etc.) relate to grounding requirements and do not affect temperature correction calculations. No additional rules apply to this specific question.

---

### cec2022-043

**Original ID:** cec-015 | **Category:** ampacity_adjustment | **Tier:** delta_table

**Question:** What is the ampacity adjustment factor for 7-9 current-carrying conductors in a raceway?

**Duration:** 6.0s | **Iterations:** 3

**Tools Called:** cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Ampacity Adjustment Factor for Bundling (CEC 2022)

The ampacity adjustment factor for **7-9 current-carrying conductors** in a raceway is **0.7 (70%)**, per **CEC 2022 Table 310.15(C)(1)** [California Amendment].

**Key Details:**
- Applies to conductors rated 40°C or higher (typically 60°C, 75°C, or 90°C)
- Adjustment factor reduces allowable ampacity to 70% of table value
- Applies to all conductors in the raceway (including neutrals/spares) as per footnote [*]

[OK] Source: CEC 2022

---

### cec2022-044

**Original ID:** cec-016 | **Category:** working_space | **Tier:** delta_table

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3?

**Duration:** 19.9s | **Iterations:** 7

**Tools Called:** cec_lookup_working_space, cec_search, cec_search

**Reflection:** Yes

**Hint Enforced:** Yes
**Protection Enforced:** No

**Answer:**

## Verification of 110.26(B) Requirements

**CEC 2022 Section 110.26(B)** specifies **dedicated working space** requirements for electrical equipment. Key provisions include:

1. **Dedicated Space**:  
   - The working space must be **clear of unrelated equipment** (e.g., no storage, machinery, or obstructions).  
   - Example: A panel installed in a hallway must not have shelves or furniture blocking access.

2. **Vertical Clearance**:  
   - Requires **6.5 ft (78 in)** of vertical space above the **floor** where work is performed (not the panel height).  
   - Applies even if the panel itself is mounted lower (e.g., a 5 ft tall panel must still have 6.5 ft of vertical clearance above the floor).

3. **Horizontal Clearance**:  
   - The working space must extend **at least 30 in (762 mm) wide** and **6.5 ft deep** (per Table 110.26(A)(1)).

---

### Integration with Previous Findings:
- **Working depth**: 4 ft (1.2 m) for 480V under Condition 3 (Table 110.26(A)(1)).  
- **Location restrictions**:  
  - **240.24(D)**: No panelboards in **closets**.  
  - **240.24(E)**: No panelboards in **bathrooms of dwelling units**.  
- **110.26(B)**: Ensures the working space is **unobstructed** and **vertically clear** (6.5 ft above floor).

---

### Inspector Note:
- A panel installed in a **bathroom** violates **240.24(E)**, even if working space depth is correct.  
- A panel installed in a **closet** violates **240.24(D)**.  
- A panel installed in a **hallway** with shelves blocking access violates **110.26(B)**.  

[OK] Source: CEC 2022 (verified via code text and tool results)

---

### cec2022-045

**Original ID:** cec-017 | **Category:** enclosure | **Tier:** delta_table

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Enclosure Types for Outdoor Use with Rain, Sleet, and Ice (CEC 2022)

**Suitable Enclosure Types:**  
For outdoor use requiring protection against **rain, sleet, and ice**, the following enclosure types are suitable per **Table 110.28**:

- **Type 3**  
- **Type 3R**  
- **Type 3S**  
- **Type 3X**  
- **Type 3RX**  
- **Type 3SX**  
- **Type 4**  
- **Type 4X**  
- **Type 6**  
- **Type 6P**  

**Key Notes:**  
1. **Mechanism Operability in Ice:**  
   - If the enclosure must remain **operable when ice-covered**, only **Type 3S** or **Type 3SX** enclosures satisfy this requirement (see the "Sleet*" footnote).  

2. **Corrosion Resistance:**  
   - For environments with **corrosive agents**, select **Type 3X**, **3RX**, **3SX**, **4X**, **3SX**, **4X**, or **6P** (marked with "X" in the "Corrosive agents" row).  

3. **Terminology:**  
   - These enclosures are classified as **raintight** (Types 3, 3S, 3SX, 3X, 4, 4X, 6, 6P) or **rainproof** (Types 3R, 3RX).  

**Inspector Note:**  
Always verify the specific environmental conditions (e.g., corrosive agents, hosedown requirements) to ensure the selected enclosure type fully complies with Table 110.28.  

[OK] Source: CEC 2022

---

### cec2022-046

**Original ID:** cec-018 | **Category:** lighting_load | **Tier:** delta_table

**Question:** What is the general lighting load in VA per square foot for office buildings?

**Duration:** 5.5s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## General Lighting Load for Office Buildings (CEC 2022)

**Answer:**  
The general lighting load for **office buildings** is **1.3 VA per square foot** (VA/ft²) according to **CEC Table 220.12**.

**Citations:**  
- **Table 220.12** (CEC 2022) - "General Lighting Loads by Non-Dwelling Occupancy"  
- **Footnote [d]**: Banks are classified as office-type occupancies.  

**Inspector Note:**  
The 125% multiplier for continuous loads (per **210.20(A)**) is already included in Table 220.12 values for load calculations.  

[OK] Source: CEC 2022

---

### cec2022-047

**Original ID:** cec-019 | **Category:** flexible_cord | **Tier:** delta_table

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset)?

**Duration:** 9.8s | **Iterations:** 4

**Tools Called:** cec_lookup_table, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Ampacity of 12 AWG Flexible Cord (Thermoset, Column B)

**Answer:**  
The ampacity for a 12 AWG flexible cord with thermoset insulation (Column B, two-conductor applications) is **25 amperes** at 30°C ambient temperature, per **CEC 2022 Table 400.5(A)(1)**.

**Citations:**  
- **Table 400.5(A)(1)**: Lists ampacities for flexible cords, with Column B specifying two-conductor configurations.  
- **Section 400.5(A)**: References this table and defines Column B as applying to two-conductor cords.  

**Inspector Note:**  
This value assumes standard ambient conditions (30°C). Adjustments may be required for higher temperatures or bundled installations (see 400.5(A) for correction factors).  

[OK] Source: CEC 2022

---

### cec2022-048

**Original ID:** cec-020 | **Category:** fixture_wire | **Tier:** delta_table

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire?

**Duration:** 9.6s | **Iterations:** 5

**Tools Called:** cec_lookup_fixture_wire, cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Maximum Operating Temperature for Type SF-2 Fixture Wire (CEC 2022)

The maximum operating temperature for **Type SF-2** silicone insulated fixture wire is **200°C (392°F)**, as confirmed by two sources in the CEC 2022:

1. **CEC 2022 Table 402.3** [California Amendment] directly specifies 200°C for Type SF-2 fixture wire.
2. **CEC 2022 Section 620.11(A)(1)** reinforces this requirement for elevator hoistway door interlock wiring, stating Type SF conductors must be suitable for temperatures of **not less than 200°C**.

This high-temperature rating makes Type SF-2 suitable for demanding applications like elevator systems and other high-heat environments.

[OK] Source: CEC 2022

---

### cec2022-049

**Original ID:** cec-021 | **Category:** adjusted_ampacity | **Tier:** calculation

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40°C ambient temperature.

**Duration:** 13.9s | **Iterations:** 6

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, python_calculator

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**1. Base Ampacity**  
8 AWG THWN copper at 75°C: **50A** (Table 310.16)

**2. Temperature Correction**  
40°C ambient → 0.88 correction factor (Table 310.15(B)(1)(1))

**3. Bundling Adjustment**  
7 conductors in raceway → 0.70 adjustment (Table 310.15(C)(1))

**4. Final Calculation**  
```
50A × 0.88 × 0.70 = 30.8A
```

**Answer:**  
Adjusted ampacity = **30.8A** (rounded to 31A for practical application)

[OK] Source: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)

---

### cec2022-050

**Original ID:** cec-022 | **Category:** service_sizing | **Tier:** calculation

**Question:** Size the conductors, EGC, and GEC for a 200A residential service using copper conductors.

**Duration:** 10.8s | **Iterations:** 5

**Tools Called:** cec_lookup_conductor_size, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Service Sizing (CEC 2022)

**Service conductor**: 2/0 AWG copper (Table 310.12(A) for 200A dwelling service)  
**EGC**: 6 AWG copper (Table 250.122 for 200A OCP)  
**GEC**: 6 AWG copper (per California amendment delta in Table 250.66 for equivalent service conductor size)

[OK] Source: CEC 2022

---

### cec2022-051

**Original ID:** cec-023 | **Category:** commercial_load | **Tier:** calculation

**Question:** Calculate the general lighting load for a 5,000 square foot office building.

**Duration:** 5.3s | **Iterations:** 3

**Tools Called:** cec_lookup_table

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## General Lighting Load Calculation for Office Building (CEC 2022)

**Calculation:**
- **Building area**: 5,000 sq ft  
- **Unit load for office occupancy**: 1.3 VA/ft² (from CEC Table 220.12)  
- **Total lighting load**:  
  $$
  5,000 \, \text{ft}^2 \times 1.3 \, \text{VA/ft}^2 = 6,500 \, \text{VA}
  $$

**Code Notes:**
- The 125% multiplier for continuous loads (per 210.20(A)) is **already included** in the Table 220.12 values.
- This is the **minimum general lighting load** required for branch circuit and feeder calculations.

[OK] Source: CEC 2022 Table 220.12

---

### cec2022-052

**Original ID:** cec-024 | **Category:** motor_circuit | **Tier:** calculation

**Question:** What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure?

**Duration:** 6.5s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## Maximum Overcurrent Protection for 16 AWG Motor Control Circuit (CEC 2022)

**Answer:**  
The maximum overcurrent protection for 16 AWG copper motor control circuit conductors **extending beyond the enclosure** is **10 amperes**.

**Source:**  
- **CEC 2022 Table 430.72(B), Column C (Copper Conductors):**  
  For 16 AWG copper conductors extending beyond the enclosure, the maximum overcurrent protective device rating is **10A**.  

**Key Code Requirements:**  
1. **430.72(B)(2):** Conductors extending beyond the motor control equipment enclosure must not exceed the values in **Column C** of Table 430.72(B).  
2. **240.4(D):** While 16 AWG copper is generally limited to 20A (per 240.4(D)(2)), **Table 430.72(B) takes precedence** for motor control circuits, imposing a stricter 10A limit.  

**Inspector Note:**  
- This applies specifically to motor control circuits **not protected by the motor branch-circuit OCPD**. If the control circuit is protected by the motor branch-circuit OCPD (e.g., a 20A breaker), ensure compliance with **Exception No. 1** in 430.72(B).  

[OK] Source: CEC 2022

---

### cec2022-053

**Original ID:** cec-025 | **Category:** dwelling_load | **Tier:** calculation

**Question:** Calculate the general lighting load for a 2,400 square foot dwelling unit.

**Duration:** 10.0s | **Iterations:** 4

**Tools Called:** cec_lookup_table, cec_exception_search

**Reflection:** Yes (improved answer)

**Hint Enforced:** No
**Protection Enforced:** No

**Answer:**

## General Lighting Load for Dwelling Unit (CEC 2022)

**Answer:**  
For a **dwelling unit**, the general lighting load calculation is **not** found in Table 220.12 (which applies to *non-dwelling* occupancies). Instead, California follows the **NEC standard** for dwelling units with a **3 VA per square foot** requirement (per CEC 220.12(B) for dwelling units, though this is not explicitly listed in Table 220.12).

**Calculation:**  
$$
2,400 \, \text{sq ft} \times 3 \, \text{VA/ft²} = 7,200 \, \text{VA}
$$

**Code Basis:**  
- **NEC 220.12(B)** (adopted in CEC 2022): Dwelling units require **3 VA per square foot** for general lighting load calculations.  
- **No California amendments** override this for general lighting in dwellings.

**Inspector Note:**  
Always verify if the dwelling has special features (e.g., large kitchens, workshops) that might require additional load calculations per 220.55 or 220.56. This calculation assumes standard residential use.

[OK] Source: CEC 2022 (NEC 220.12(B))

---

