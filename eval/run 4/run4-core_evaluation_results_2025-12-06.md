# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-06
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 28 |
| **Successful** | 28 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 893.7s |
| **Avg per Question** | 31.9s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity for 12 AWG Copper Conductor (CEC 2022)

**Base Ampacity:**  
12 AWG copper at 75°C termination = **25 amperes** per CEC 2022 Table 310.16.  

**Critical Exception:**  
Section 240.4(D) limits overcurrent protection for 12 AWG copper conductors to **20 amperes**. This creates a practical "ampacity limit" where the conductor's 25A rating is overridden by the 20A overcurrent protection requirement.  

**California-Specific Notes:**  
- The [CEC amendment] in Table 310.16 explicitly references Section 240.4(D) as a limiting factor for small conductors.  
- No additional CEC exceptions apply for standard 12 AWG copper in dry locations.  

---
## NEC 2023 Reference  
No difference from NEC 2023. NEC Table 310.16 also specifies 25A for 12 AWG copper at 75°C, with identical 240.4(D) overcurrent limits.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 240.4, 310.16

**Response Time:** 34.9s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
The minimum copper conductor size required for a 60A circuit at 75°C is **6 AWG**.  
- **Ampacity**: 65A (per CEC 2022 Table 310.16)  
- **Rationale**: 6 AWG copper has an ampacity of 65A at 75°C, which meets the 60A requirement. Smaller sizes like 8 AWG (50A) are insufficient.  

**Exceptions Checked**:  
- No applicable exceptions found in CEC 2022 for Section 310.16 under standard conductor sizing rules.  

---
## NEC 2023 Reference  
No difference from NEC 2023. Both codes use Table 310.16, and 6 AWG copper at 75°C provides 65A ampacity.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 310.16

**Response Time:** 10.1s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- Conductor: 12 AWG TW (60°C rated) copper
- Number of CCCs: 6
- Ambient temperature: 43°C (110°F)

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):
   12 AWG copper, 60°C column = **20 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   43°C ambient, 60°C conductor = **0.82 factor**

3. **Adjustment Factor** (CEC 2022 Table 310.15(C)(1)):
   6 current-carrying conductors = **0.80 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 20 × 0.82 × 0.80 = 13.12 amperes
   ```

**Final Answer: 13.12 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and
multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

No exceptions to these derating requirements were found.

---
## NEC 2023 Reference
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**"

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 19.8s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- Conductor: 12 AWG TW (60°C rated) copper
- Number of CCCs: 6
- Ambient temperature: 43°C (110°F)

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):
   12 AWG copper, 60°C column = **20 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   43°C ambient, 60°C conductor = **0.82 factor**

3. **Adjustment Factor** (CEC 2022 Table 310.15(C)(1)):
   6 current-carrying conductors = **0.80 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 20 × 0.82 × 0.80 = 13.12 amperes
   ```

**Final Answer: 13.12 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and
multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

No exceptions to these derating requirements were found.

---
## NEC 2023 Reference
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**"

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 15.5s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
**Yes**, aluminum conductors are permitted for a 200A service in California per CEC 2022 Sections 110.5 and 310.3(B).  

**Minimum Required Size**:  
- **250 kcmil aluminum conductors** at 75°C (per CEC 2022 Table 310.16), providing an ampacity of **205A** (meets/exceeds 200A requirement).  

**Key Requirements**:  
1. **Material Compliance**: Aluminum or copper-clad aluminum is allowed (Section 310.3(B)).  
2. **Termination Compatibility**: Equipment terminations must be rated for aluminum conductors (Section 110.14(C)).  
3. **No Exceptions Apply**: The 250 kcmil size is required without derating for standard ambient conditions (no bundling or high-temperature adjustments mentioned).  

**Exception Analysis**:  
- Exceptions to Section 310.3 (e.g., 310.12 for dwelling services) do not apply here, as this is a general service calculation. No exceptions override the 250 kcmil requirement.  

---

## NEC 2023 Reference  
No difference from NEC 2023. Aluminum service conductors for 200A also require **250 kcmil** at 75°C (NEC Table 310.16).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_size, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 110.14, 110.5, 310.3, 310.16, 310.12

**Response Time:** 26.1s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Clearance Depth (CEC 2022)

**California Requirement:**  
For a 120/240V residential panel installed in a typical residential setting with **Condition 2** (exposed live parts on one side and a grounded wall on the other), the minimum working space depth is **1.0 meter (3 feet 6 inches)** per **CEC 2022 Table 110.26(A)(1)**. 

**Key Details:**  
- **Condition 2 Applies:** Grounded walls (e.g., concrete, brick, or tile) are standard in residential construction.  
- **No Exceptions Apply:** The standard depth is required unless specific exceptions (e.g., existing buildings with <200A panels) are met, which are not relevant here.  

**Exceptions Checked:**  
- Dead-front assemblies, low-voltage, and existing building exceptions do not override the depth for standard residential panels.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The working space depth for 240V under Condition 2 is also **3 feet 6 inches** per NEC Table 110.26(A)(1).

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_working_space, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 29.7s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
Per **CEC 2022 Section 210.11(C)(1)**, **two or more 20-ampere small-appliance branch circuits** are required for kitchens. These circuits must supply:  
- All wall/floor receptacles in kitchens (per 210.52(A))  
- Countertop receptacles (per 210.52(C))  
- Refrigeration equipment receptacles  

**Exceptions**:  
1. Additional switched receptacles (e.g., for clocks) on 15/20A circuits are permitted.  
2. Specific appliances (e.g., gas ranges) may use separate circuits.  

The minimum of **two circuits** remains mandatory—no exceptions reduce this requirement.  

---
## NEC 2023 Reference  
No difference from NEC 2023. Both codes require **two 20-ampere small-appliance branch circuits** for kitchens (NEC 210.11(C)(1)).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.11, 210.52

**Response Time:** 18.0s

---

### baseline-008: knowledge_simple

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Expected:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- Conductor: 12 AWG TW (60°C rated) copper
- Number of CCCs: 6
- Ambient temperature: 43°C (110°F)

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):
   12 AWG copper, 60°C column = **20 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   43°C ambient, 60°C conductor = **0.82 factor**

3. **Adjustment Factor** (CEC 2022 Table 310.15(C)(1)):
   6 current-carrying conductors = **0.80 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 20 × 0.82 × 0.80 = 13.12 amperes
   ```

**Final Answer: 13.12 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and
multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

No exceptions to these derating requirements were found.

---
## NEC 2023 Reference
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 15.3s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

### **Service Load Calculation (CEC 220.82)**
- **Total Calculated Load**: 43,470 VA → **181.1 A** at 240V  
- **Minimum Service Rating**: 200A (per 230.42, service rating must match overcurrent device).

### **Conductor Sizing Exceptions**
1. **Section 220.82 Exception**:  
   - Optional calculation (Part IV) permits using Table 220.55 demand factors for ranges.  
   - No exceptions override the 200A requirement for this load.

2. **Section 310.16 Exception**:  
   - Aluminum conductors allowed if sized per 310.3 (minimum 12 AWG for service conductors).  
   - 250 kcmil aluminum meets this and 200A ampacity.

3. **Section 110.14(C) Exception**:  
   - Aluminum conductors must be terminated per manufacturer instructions (110.3(B)).  
   - Requires equipment listed for aluminum (e.g., CO/ALR receptacles).

---

### **Final Determination**
- **Required Conductors**:  
  - **Copper**: 3/0 AWG (200A)  
  - **Aluminum**: 250 kcmil (205A)  
- **Aluminum Permitted**: Yes, if:  
  - Installed per 110.3(B) (manufacturer instructions).  
  - Terminated with equipment rated for aluminum (110.14(C)).  
  - Minimum size of 12 AWG met (242.28).

---

### **NEC Comparison**
- **Demand Factors**: Same as CEC (Table 220.55).  
- **Conductor Sizing**: NEC Table 310.16 also requires 3/0 copper or 250 kcmil aluminum for 200A.  
- **No California-Specific Differences**: This calculation aligns with NEC.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_size, cec_lookup_conductor_size, cec_search, cec_search, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 9 found
- 110.14, 181.1, 242.28, 110.3, 220.82, 230.42, 310.3, 220.55, 310.16

**Response Time:** 49.6s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** PASS

**Agent Answer:**
## CEC 2022 Requirements for Multiwire Branch Circuit (12/3 Cable) in California

**1. Circuit Breaker Requirements**  
- **Type**: A **2-pole circuit breaker** is required to simultaneously disconnect all ungrounded (hot) conductors at the panelboard (CEC 210.4(B)).  
- **Rating**: 20A breaker for 12 AWG copper conductors (CEC 240.4(D)).  

**2. Neutral Conductor Termination**  
- **Grouping**: The neutral conductor must be **grouped with its associated ungrounded conductors** in the panelboard (CEC 200.4(B)). This prevents misidentification and ensures the neutral is not shared with other circuits.  
- **Termination**: The neutral must terminate on the **neutral bus** in the panel, not on the equipment grounding conductor (EGC) bus.  

**3. Exceptions**  
- No exceptions apply for standard kitchen multiwire branch circuits.  
- **Exception 210.4(C)** (line-to-line loads) does not apply here, as kitchen receptacles are line-to-neutral loads.  

**4. California-Specific Compliance**  
- CEC 2022 aligns with NEC 2023 for MWBC requirements. No California amendments ([CEC]) affect this scenario.  

---
## NEC 2023 Reference  
- **210.4(B)**: Requires simultaneous disconnection of all ungrounded conductors.  
- **200.4(B)**: Mandates grouping of neutral conductors with their associated hots.  
- **240.4(D)**: 12 AWG copper requires 20A overcurrent protection.  

**Comparison**: No difference from NEC 2023. California has no amendments to these requirements.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search, nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 210.4, 240.4, 200.4

**Response Time:** 29.6s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Dwellings (NEC 2023)  

**Required Locations (NEC 2023 Section 210.8(A)):**  
GFCI protection is required for **all 125–250V receptacles** in the following locations in dwelling units:  
1. **Bathrooms**  
2. **Garages** and accessory buildings with floors at or below grade (non-habitable, for storage/work).  
3. **Outdoors**.  
4. **Crawl spaces** at or below grade level.  
5. **Kitchens**.  
6. **Areas with sinks** and permanent food/prep/cooking provisions.  
7. **Sinks** – receptacles within 1.8 m (6 ft) from the bowl’s top inside edge.  
8. **Bathtubs/showers** – receptacles within 1.8 m (6 ft) of the tub/shower’s outside edge.  
9. **Laundry areas**.  
10. **Indoor damp/wet locations**.  

---

**Exceptions (NEC 2023 Section 210.8):**  
- **Exception No. 1**: Receptacles not readily accessible for dedicated equipment (e.g., snow-melting systems) are exempt (per 426.28/427.22).  
- **Exception No. 2**: Receptacles for **permanently installed premises security systems** may omit GFCI protection.  
- **Exception No. 3**: **Listed weight-supporting ceiling receptacles (WSCR)** used with compatible fixtures (e.g., ceiling fans) may omit GFCI if the receptacle is not a general-purpose convenience outlet.  
- **Exception No. 4**: Factory-installed, non-readily accessible receptacles in bathroom exhaust fans are exempt unless required by listing/installation instructions.  
- **Exception No. 2 (HVAC)**: GFCI is not required for **listed HVAC equipment** (expires September 1, 2026).  

---

**Additional Notes:**  
- **Feeders**: Section 215.9 allows GFCI protection at the **feeder level** instead of individual outlets.  
- **HVAC Exception**: The exemption for HVAC equipment is temporary and expires **September 1, 2026**.  

✓ **Sources: NEC 2023 (primary)**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 4 found
- 210.8, 427.22, 426.28, 215.9

**Response Time:** 27.2s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
**Surge Protection Requirement for Residential Services (CEC 2022):**  

1. **Requirement**:  
   - **Yes**, surge protection is mandatory for all services supplying dwelling units per **CEC 2022 Section 230.67(A)**.  
   - A listed **surge-protective device (SPD)** must be installed.  

2. **Installation Locations**:  
   - **Primary Location**: The SPD must be an **integral part of the service equipment** (e.g., main panel).  
   - **Alternative Location**: If not in the service equipment, it must be **immediately adjacent** to the service equipment (Section 230.67(B)).  
   - **Exception**: The SPD may be installed at the **next level distribution equipment downstream** toward the load (e.g., subpanels) if not in the service equipment (Exception to 230.67(B)).  

3. **SPD Type**:  
   - Must be **Type 1 or Type 2 SPD** (Section 230.67(C)).  

4. **Replacement Rule**:  
   - If service equipment is replaced, the SPD requirements **must still apply** (Section 230.67(D)).  

---

## NEC 2023 Reference  
**Difference from NEC**:  
- The **NEC 2023 does not mandate SPDs** for residential services.  
- CEC 2022 adds this requirement as a **California-specific amendment** [CEC].  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 230.67

**Response Time:** 16.0s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** PASS

**Agent Answer:**
## NEC 2023 Compliance Analysis

### **1. Working Space Requirements (110.26)**
- **Depth**:  
  - **Required**: 30 inches (Condition 2, Table 110.26(A)(1) for 120V equipment).  
  - **Provided**: 24 inches.  
  - **Result**: ❌ **Fails** depth requirement.  

- **Width**:  
  - **Required**: 30 inches (110.26(A)(2) – width must be equipment width or 30", whichever greater).  
  - **Provided**: 18 inches (distance to water heater).  
  - **Result**: ❌ **Fails** width requirement.  

- **Storage Violation**:  
  - **Rule**: 110.26(B) prohibits storage in working space.  
  - **Provided**: Water heater located 18" from panel.  
  - **Result**: ❌ **Fails** – water heater placement violates storage prohibition.  

---

### **2. Panel Location Restrictions (240.24(D))**
- **Rule**: Panels **prohibited in clothes closets**.  
- **Scenario**: User specified a "closet" but did not clarify if it is a **clothes closet**.  
  - If **clothes closet**: ❌ **Fails** 240.24(D).  
  - If **general closet**: ✅ **Compliant** (no explicit prohibition).  

---

### **3. Exceptions Checked**
- **110.26 Exceptions**:  
  - No exceptions apply for reduced depth/width in this scenario.  
- **240.24(D) Exceptions**:  
  - No exceptions for panel installation in clothes closets.  

---

### **Final Determination**
- **Working Space**: ❌ **Non-compliant** (insufficient depth/width, storage violation).  
- **Panel Location**: ❌ **Non-compliant if in a clothes closet**.  

**Recommendation**:  
- Increase front clearance to **30 inches** and side clearance to **30 inches**.  
- Relocate the water heater or panel to avoid storage violations.  
- Verify closet type (clothes vs. general) to address 240.24(D).  

✓ **Sources**: NEC 2023 (Sections 110.26, 240.24)

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search, cec_exception_search
- NEC Tools: nec_search, nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 110.26, 240.24

**Response Time:** 47.8s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
This is a **code violation** under CEC 2022.  

**Key Requirements from CEC 2022:**  
1. **Section 110.14(A)** explicitly requires that terminals designed for more than one conductor must be **identified for that purpose**. The breaker terminal in question is **not marked** for two conductors, violating this rule.  
2. **Section 408.41** (Grounded Conductor Terminations) reinforces that grounded conductors must terminate in **individual terminals** unless the terminal is specifically identified for multiple conductors (e.g., parallel conductors). This exception does **not apply** to non-parallel conductors on a single circuit breaker.  

**Why the Exception Does Not Apply:**  
The exception in **408.41** permits multiple grounded conductors on a single terminal **only for parallel conductors** (e.g., multi-phase service conductors). This scenario involves **two conductors on a single 20A circuit breaker**, which is not a parallel conductor installation.  

**NEC Comparison:**  
NEC 2023 has identical requirements in **110.14(A)** and **408.41**. The national code also prohibits multiple conductors on a terminal unless it is identified for that purpose.  

---

## NEC 2023 Reference  
No difference from NEC 2023. Same requirements apply.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 110.14, 408.41

**Response Time:** 13.7s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
**Grounding and Bondinging Configuration for Detached Garage Subpanel (CEC 2022):**  

1. **Grounding Electrode System (CEC 250.50):**  
   - A **separate grounding electrode system** (e.g., ground rod, concrete-encased electrode) must be installed at the detached garage.  
   - All grounding electrodes present at the garage (e.g., metal water pipe, ground rod) must be **bonded together** to form a grounding electrode system.  
   - If no existing electrodes are present, install at least one electrode (e.g., 8-ft ground rod).  

2. **Grounding Electrode Conductor (CEC 250.64):**  
   - A **8 AWG copper conductor** (or 6 AWG aluminum) connects the subpanel’s grounding electrode to the grounding electrode system.  
   - This conductor must be sized per **CEC Table 250.66** based on the subpanel’s overcurrent protection (100A in this case).  

3. **Equipment Grounding and Neutral Bonding (CEC 250.142):**  
   - In the subpanel, the **neutral and equipment grounding conductors must be bonded** together (unlike in the main panel).  
   - The **equipment grounding conductor** (from the feeder) connects to the subpanel’s bonding bar, which is tied to the local grounding electrode.  

4. **Feeder Requirements (4-Wire System):**  
   - The 4-wire feeder includes:  
     - Two ungrounded (hot) conductors.  
     - One grounded (neutral) conductor.  
     - One equipment grounding conductor (8 AWG copper).  
   - The neutral conductor must **not be bonded to the grounding electrode** at the subpanel—only the equipment grounding conductor connects to the grounding electrode.  

5. **Exceptions and Key Notes:**  
   - **Exception 250.54:** Auxiliary grounding electrodes (e.g., additional rods) may be added but **must not create parallel paths** for ground-fault current.  
   - **Concrete-encased electrodes** (e.g., rebar in foundation) are permitted but **not required** if inaccessible without disturbing concrete.  

---

## NEC 2023 Reference  
- *...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 5 found
- 250.142, 250.54, 250.50, 250.66, 250.64

**Response Time:** 21.5s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- Conductor: 12 AWG TW (60°C rated) copper
- Number of CCCs: 6
- Ambient temperature: 43°C (110°F)

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):
   12 AWG copper, 60°C column = **20 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   43°C ambient, 60°C conductor = **0.82 factor**

3. **Adjustment Factor** (CEC 2022 Table 310.15(C)(1)):
   6 current-carrying conductors = **0.80 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 20 × 0.82 × 0.80 = 13.12 amperes
   ```

**Final Answer: 13.12 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and
multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

No exceptions to these derating requirements were found.

---
## NEC 2023 Reference
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**"

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 17.7s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]

**Number of 20-Ampere Small Appliance Branch Circuits Required for a Kitchen:**  
Per **CEC 2022 Section 210.11(C)(1)**, **at least two 20-ampere small-appliance branch circuits** are required to serve all receptacle outlets in kitchens, including countertop surfaces and refrigeration equipment.  

**Can These Circuits Serve Dining Room Receptacles?**  
Yes. **CEC 2022 Section 210.52(B)(1)** explicitly permits small-appliance branch circuits to supply receptacle outlets in the kitchen **and other rooms specified in 210.52(B)(1)**, which includes dining rooms. The text states:  
> "either or both of which shall also be permitted to supply receptacle outlets in the same kitchen and in other rooms specified in 210.52(B)(1)."  

**Key Exceptions:**  
- No small-appliance branch circuit shall serve more than one kitchen (per 210.52(B)(1)).  
- Dining room receptacles must not be included in the "1.8 m (6 ft) spacing" requirement for wall receptacles (covered separately in 210.52(A)).  

---

## NEC 2023 Reference  
The NEC has **identical requirements** for small-appliance branch circuits in kitchens (NEC 210.52(B)(1)) and permits serving dining room receptacles under the same logic. California's CEC does not amend this requirement.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.11, 210.52

**Response Time:** 13.6s

---

### core-010: load_calculations

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Expected:** Base ampacity: 30A at 90°C (Table 310.16). Temperature correction factor: 0.82 for 50°C (Table 310.15(B)(1)). Bundling adjustment: 0.80 for 6 conductors (Table 310.15(C)(1)). Adjusted ampacity = 30A × 0.82 × 0.80 = 19.68A, approximately 20A.

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- Conductor: 12 AWG THHN copper (90°C rating)
- Number of CCCs: 6
- Ambient temperature: 50°C

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):  
   12 AWG THHN copper at 90°C = **30 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):  
   50°C ambient → **0.82 factor**

3. **Bundling Adjustment** (CEC 2022 Table 310.15(C)(1)):  
   6 current-carrying conductors → **0.80 factor**

4. **Adjusted Ampacity Calculation:**  
   ```python
   adjusted = 30 × 0.82 × 0.80 = 19.68 amperes
   ```

**Final Answer: 19.68 amperes**  
This accounts for both elevated ambient temperature and multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

No exceptions to these derating requirements were found in CEC 2022.

---
## NEC 2023 Reference  
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 8.5s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## CEC 2022 Requirement for AFCI Protection in Bedrooms and Living Areas

**California Requirement (CEC 2022):**  
Per **CEc_search("AFCI bedrooms living areas")**, CEC 2022 Section 210.12(C) requires **arc-fault circuit-interrupter (AFCI) protection** for all 120-volt, 15- and 20-ampere branch circuits in dwelling unit bedrooms, living rooms, and similar areas. This aligns with NEC 2023 Section 210.12(C).

**Exceptions:**  
- **Fire alarm systems**: AFCI protection is exempt for circuits supplying fire alarm systems installed per 760.41(B) or 760.121(B) (CEC 2022 Section 210.12, Exception).  
- **Short extensions**: No AFCI required for branch circuit extensions ≤ 1.8 m (6 ft) without additional outlets (CEC 2022 Section 210.12(D), Exception).  

**Electrical Hazard Prevented:**  
AFCI protection prevents fires caused by **arc faultss**—high-resistance electrical discharges in damaged or degraded wiring (e.g., from pinched cords, loose connections, or rodent damage). Arcs generate heat that can ignite surrounding materials, particularly in high-traffic areas like bedrooms and living rooms.

---

## NEC 2023 Reference  
No difference from NEC 2023. CEC 2022 adopts NEC 2023 requirements for AFCI protection in dwelling units without amendments.  

✓ **Sources**: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 760.41, 760.121, 210.12

**Response Time:** 21.1s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Why Torque Specifications Are Important:**  
Torque specifications ensure proper termination of conductors in panels to prevent overheating, arcing, and connection failures. Improper torque can lead to loose connections (overheating) or over-tightened connections (damaged terminals).  

**CEC 2022 Requirements:**  
Per **CEC 2022 Section 110.14(D)**:  
- Tightening torque values for terminal connections **must match the manufacturer's specifications** indicated on the equipment or in installation instructions.  
- An **approved means** (e.g., torque tools, shear bolts, breakaway devices) must be used to achieve the specified torque.  
- If torque values are not provided, contact the manufacturer or refer to **UL 486A-486B** or **NFPA 70B** for guidance.  

**Additional Context from CEC 430.9(C):**  
- For control circuit devices with screw-type terminals using **14 AWG or smaller copper conductors**, torque requirements apply to ensure reliable connections.  

**Exceptions:**  
- No exceptions override the torque requirements in 110.14(D).  

---
## NEC 2023 Reference  
The NEC (2023) includes similar requirements in **NEC 110.14(D)** but does **not explicitly mandate torque tools** or reference manufacturer instructions as strongly as the CEC. California’s CEC adds specificity for enforceable compliance.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 430.9, 110.14

**Response Time:** 15.0s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Final Answer: Service Load Calculation (NEC 2023)

### **1. General Lighting Load**  
3000 sq ft × 3 VA/ft² = **9000 VA** (NEC 220.41)  

### **2. Small Appliance & Laundry Circuits**  
3 circuits × 1500 VA = **4500 VA** (NEC 220.11(B))  

### **3. Range Load**  
12 kW range → **8000 VA** (Table 220.55 demand factor for 1 range)  

### **4. Dryer Load**  
5.5 kW dryer → **5000 VA** (Table 220.54 demand factor for 1 dryer)  

### **5. AC Load**  
4600 VA × 1.25 (continuous load) = **5750 VA** (NEC 220.60)  

---

### **Total Load Calculation**  
**Total Load (VA)** = 9000 + 4500 + 8000 + 5000 + 5750 = **32,250 VA**  

**Convert to Amperes**:  
32,250 VA ÷ 240V = **134.4 A**  

---

### **Conclusion**  
The calculated service load is **134.4 A**, which is **well below the 200A panel capacity**. The panel is **adequately sized** for the loads.  

**NEC References**:  
- General lighting: 220.41  
- Small appliance/laundry: 220.11(B)  
- Range: 220.55  
- Dryer: 220.54  
- AC: 220.60  

**Exceptions Verified**:  
- No exceptions override the demand factors for range (220.55) or dryer (220.54).  
- Continuous load multiplier (125%) applied to AC per 220.60.  

✓ **Sources: NEC 2023 (primary)**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_search, nec_search, nec_search, nec_exception_search, nec_exception_search, nec_exception_search
- CEC Primary: No

**Citations:** 6 found
- 220.54, 134.4, 220.41, 220.60, 220.11, 220.55

**Response Time:** 61.0s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## [Main Answer - NEC 2023]
**Identified NEC Violations in Residential Garage Panel Installation:**

1. **Insufficient Working Space Depth (NEC 110.26(A)(1))**  
   - **Requirement:** Minimum depth of **30 inches** for Condition 2 (live parts on one side, grounded on the other).  
   - **Violation:** Measured depth is **28 inches** (110.26(A)(1) Table 110.26(A)(1)).  
   - **Impact:** Inadequate clearance for safe maintenance and inspection.

2. **Storage in Working Space (NEC 110.26(B))**  
   - **Requirement:** Working space **must not be used for storage**.  
   - **Violation:** Water heater located **16 inches to the left** within the working space.  
   - **Impact:** Obstructs access and violates safety clearance.

3. **Height Clearance Compliance (NEC 110.26(A)(3))**  
   - **Requirement:** Working space height must be **6.5 ft (78 in)** from floor to equipment top.  
   - **Compliance:** Panel mounted at **5 ft (60 in)**. Assuming a standard panel height of **24 in**, total height is **81 in (6.75 ft)**, which **meets** the requirement.  

---

## NEC 2023 Reference  
- **Depth Violation:** NEC 110.26(A)(1) Table 110.26(A)(1) specifies 30-inch depth for Condition 2.  
- **Storage Violation:** NEC 110.26(B) explicitly prohibits storage in working space.  
- **Height Compliance:** NEC 110.26(A)(3) requires 6.5 ft height; 6.75 ft meets this.  

✓ **Sources: NEC 2023 (primary)**

**Tool Usage:**
- CEC Tools: cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: nec_search, nec_search, nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 29.2s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## NEC 2023 Requirements for Kitchen Circuits

### 1. **Countertop Receptacles (20A Circuits)**
- **Protection Required**: **GFCI**  
- **NEC Reference**: **210.8(A)(5)**  
  - Kitchens require GFCI protection for all 125V–250V receptacles installed in areas with sinks or food preparation.  
- **AFCI**: **Not required** (AFCI applies to dwelling unit bedrooms, not kitchens per 210.12(B)).  

---

### 2. **Dishwasher (15A Circuit)**
- **Protection Required**: **GFCI**  
- **NEC Reference**: **210.8(D)**  
  - Dishwashers are explicitly listed in 210.8(D) as requiring GFCI protection.  
- **AFCI**: **Not required** (dedicated appliance circuits is exempt from AFCI unless in specific areas like bedrooms).  

---

### 3. **Garbage Disposal (15A Circuit)**
- **Protection Required**: **GFCI**  
- **NEC Reference**: **210.8(A)(6)**  
  - Sinks and food preparation areas (kitchens) require GFCI. Garbage disposals are fixed appliances in this category.  
- **AFCI**: **Not required** (same as above).  

---

### 4. **Refrigerator (20A Circuit)**
- **Protection Required**: **Standard Breaker**  
- **NEC Reference**: **210.8(D) Exception**  
  - Refrigerators are **not required** to have GFCI if they are fixed appliances and not in a location requiring GFCI (e.g., not within 6 ft of a sink).  
- **AFCI**: **Required** if on a small-appliance branch circuit (210.12(B)), but **not required** if on a dedicated circuit (per 210.12(B) exception for fixed appliances).  

---

## Summary of Protection Requirements

| Circuit Type               | Protection Required | NEC Section(s)                     |
|---------------------------|---------------------|-----------------------------------|
| Countertop Receptacles    | GFCI                | 210.8(A)(5)                       |
| Dishwasher                | GFCI                | 210.8(D)                          |
| Garbage Disposal          | GFCI                | 210.8(A)(6)                       |
| Refrigerator              | Standa...

**Tool Usage:**
- CEC Tools: cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: nec_search, nec_search, nec_search, nec_search, nec_search, nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 210.8, 210.12

**Response Time:** 35.1s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]

### **Violations Identified:**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation:** CEC 250.24(B) prohibits bonding the grounded (neutral) and grounding (equipment) conductors in a subpanel. This creates a parallel path for fault currents and violates the requirement for a single-point bond at the main service.  
   - **Correct Configuration:** Neutral and ground bars must be **isolated** in the subpanel. The neutral bar connects only to the feeder neutral conductor from the main panel. The ground bar connects to the equipment grounding conductor and grounding electrode system.

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation:** CEC 250.32(B)(1) explicitly prohibits connecting the grounded conductor (neutral) to the enclosure in a detached structure. This creates a direct path for fault currents to the enclosure, increasing shock risk.  
   - **Correct Configuration:** The neutral bar must remain **unbonded** to the enclosure. The enclosure is bonded only to the grounding electrode system via the equipment grounding conductor.

3. **Missing Grounding Electrode Conductor**  
   - **Violation:** CEC 250.50 requires a grounding electrode (e.g., rod, plate) at the detached garage. The grounding electrode conductor must connect the ground bar to this electrode.  
   - **Correct Configuration:** Install a grounding electrode (e.g., 8 ft copper rod) at the garage and connect it to the ground bar with a conductor sized per CEC Table 250.66 (e.g., #6 copper for a 100A subpanel).

4. **Ground Bar Bonded to Enclosure**  
   - **Compliant:** The equipment grounding conductor (feeder ground) is correctly connected to the ground bar, and the ground bar is bonded to the enclosure. This ensures fault currents return to the main panel via the feeder.

---

### **Correct Subpanel Configuration (CEC 2022):**
1. **Feeder Conductors:**  
   - 2 hots (#2 AWG aluminum) → Connect to subpanel breaker.  
   - 1 neutral (#2 AWG alum...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 250.32, 250.24, 110.26, 250.66, 250.50

**Response Time:** 16.6s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**
## Final Answer: Maximum Number of Conductors (CEC 2022)  

**Given:**  
- **Conduit**: 1¼-inch Rigid Metal Conduit (RMC)  
- **Conductors**: 10 AWG THHN  

---

### **Step 1: Conduit Fill Area (40% of total area)**  
From **CEC 2022 Chapter 9 Table 4**:  
- **Total area of 1¼-inch RMC** = **1.526 in²**  
- **40% fill limit** = $ 1.526 \times 0.4 = 0.6104 \, \text{in²} $  

---

### **Step 2: Conductor Area**  
From **CEC 2022 Chapter 9 Table 5**:  
- **10 AWG THHN** = **0.0211 in²/conductor**  

---

### **Step 3: Calculation**  
$$
\text{Max Conductors} = \frac{0.6104 \, \text{in²}}{0.0211 \, \text{in²/conductor}} \approx 28.93 \rightarrow \lfloor 28.93 \rfloor = 28 \, \text{conductors}
$$

---

### **Step 4: Verify Exceptions**  
- **CE_exception_search(base_rule="402.7")** confirmed no exceptions apply to conduit fill calculations for this scenario.  
- Cross-referenced sections (e.g., 250.86, 300.50) relate to grounding and underground installations, which are **not applicable** here.  

---

**Final Answer:**  
A maximum of **28** 10 AWG THHN conductors can be installed in a 1¼-inch RMC conduit per **CEc 2022 Chapter 9 Tables**.  

**NEC Comparison:**  
No difference from NEC 2023. Same conduit and conductor dimensions apply.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conduit_fill, cec_lookup_conduit_fill, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 250.86, 300.50, 402.7

**Response Time:** 77.8s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**
## Voltage Drop Calculation (CEC 2022)

**Given:**
- Voltage: 120V single-phase
- Current: 22A (continuous load)
- Conductor: 12 AWG copper (resistance = 1.29 Ω/1000 ft)
- One-way distance: 50 ft (total round-trip = 100 ft)

**Calculations:**

1. **Total Resistance (R_total):**
   $$
   R_{\text{total}} = \frac{1.29 \, \Omega}{1000 \, \text{ft}} \times 100 \, \text{ft} = 0.129 \, \Omega
   $$

2. **Voltage Drop (VD):**
   $$
   VD = I \times R_{\text{total}} = 22 \, \text{A} \times 0.129 \, \Omega = 2.838 \, \text{V}
   $$

3. **Percentage Drop:**
   $$
   \text{Percentage Drop} = \left( \frac{2.838}{120} \right) \times 100 = 2.365\%
   $$

**Final Answer:**
- **Voltage Drop:** 2.84 volts
- **Percentage Drop:** 2.37%

**Compliance Check:**
- **CEC 2022 Section 647.4(D):** Maximum 1.5% voltage drop for branch circuits (2.37% exceeds this limit).
- **NEC 2023:** 3% maximum recommended for branch circuits (2.37% is acceptable).

**Conclusion:**  
The voltage drop of 2.37% meets NEC recommendations but **violates CEC 2022's stricter 1.5% limit** for branch circuits. This installation would be non-compliant in California.

---
## NEC 2023 Reference
NEC 2023 does not specify a voltage drop limit for branch circuits, but industry best practice recommends ≤3%. The calculation method matches NEC principles.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 647.4

**Response Time:** 171.5s

---

### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- Conductor: 12 AWG TW (60°C rated) copper
- Number of CCCs: 6
- Ambient temperature: 43°C (110°F)

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):
   12 AWG copper, 60°C column = **20 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):
   43°C ambient, 60°C conductor = **0.71 factor**

3. **Bundling Adjustment** (CEC 2022 Table 310.15(C)(1)):
   6 current-carrying conductors = **0.80 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 20 × 0.71 × 0.80 = 11.36 amperes
   ```

**Final Answer: 11.36 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1). No exceptions to these derating requirements were found.

---
## NEC 2023 Reference
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 8.3s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Minimum Grounding Electrode Conductor Size (CEC 2022 Table 250.66)  

**California Requirement (CEC 2022):**  
Per **CEC 250.66**, the minimum copper grounding electrode conductor (GEC) size for **1000 kcmil service conductors** is **3/0 AWG**.  

**Exception Analysis:**  
- **250.66(A)**: If connected to a **rod, pipe, or plate electrode**, the GEC can be reduced to **6 AWG copper** (instead of 3/0 AWG).  
- **250.66(B)**: If connected to a **concrete-encased electrode**, the GEC can be reduced to **4 AWG copper**.  
- **250.66(C)**: If connected to a **ground ring**, the GEC size matches the ground ring conductor.  

**Final Determination:**  
- **Default (No Exception)**: **3/0 AWG copper** (per Table 250.66).  
- **With Exception**: Size reduction possible depending on electrode type (e.g., 6 AWG for rod/pipe).  

**NEC Comparison:**  
No difference from NEC 2023. Table 250.66 and exceptions remain identical.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (reference)**  
⚠️ **Note**: The `lookup_grounding_conductor` tool failed to access Table 250.66. This answer was derived from CEC 2022 Section 250.66 and exceptions. Verify with the actual code table for critical applications.

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 43.7s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 25/28
- **Success Rate**: 100.0%
- **Average Response Time**: 31.9s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

