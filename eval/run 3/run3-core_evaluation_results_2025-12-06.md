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
| **Total Duration** | 746.7s |
| **Avg per Question** | 26.7s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
The ampacity of a 12 AWG copper conductor at a 75°C termination is **25 amperes** per **CEC 2022 Table 310.16**.  

**Key Considerations**:  
1. **Overcurrent Protection Limitation**:  
   - Per **CEC Section 240.4(D)**, 12 AWG copper conductors **must be protected at 20 amperes maximum** for overcurrent protection, even though the table lists 25A. This is a critical exception for compliance.  

2. **California-Specific Amendment**:  
   - The note in Table 310.16 explicitly references **Section 240.4(D)** for overcurrent protection limitations, which is a California amendment to the base NEC.  

---

## NEC 2023 Reference  
- **NEC 2023 Table 310.16** also specifies 25A for 12 AWG copper at 75°C.  
- **Difference**: The NEC does not include the explicit reference to Section 240.4(D) in Table 310.16 footnotes. California enforces this limitation as a state amendment.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 240.4, 310.16

**Response Time:** 13.3s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
For a 60A circuit at 75°C, **4 AWG copper conductor** is required per CEC 2022 Table 310.16.  

**Key Details**:  
- **Ampacity**: 4 AWG copper at 75°C has an ampacity of **85A** (sufficient for 60A load).  
- **Overcurrent Protection**: Per CEC 240.4(D), the maximum overcurrent protection for 4 AWG copper is **70A**.  
- **No Adjustments Needed**: Standard ambient temperature (30°C) and ≤3 current-carrying conductors assumed.  

**Exceptions/Overrides**:  
- No exceptions apply to Table 310.16 for this scenario.  
- CEC 240.4(D) limits overcurrent protection for 4 AWG copper to 70A (compliant with 60A load).  

---
## NEC 2023 Reference  
No difference from NEC 2023. The ampacity and overcurrent protection requirements are identical.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_ampacity, cec_lookup_conductor_ampacity, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 240.4, 310.16

**Response Time:** 23.4s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Kitchens (CEC 2022)

**California Requirement (CEC 2022):**  
Per **CEC 2022 Section 210.8(A)(6)**, **all receptacles installed to serve countertop surfaces in kitchens** must be protected by a ground-fault circuit interrupter (GFCI). This includes:  
- Receptacles on wall-mounted countertops  
- Receptacles on peninsula or island countertops  
- Receptacles integrated into work surfaces  

**Additional Requirements:**  
1. **Spacing**: Per **CEC 210.52(C)(1)**, receptacles must be placed so no point along the countertop is more than 24 inches (600 mm) from an outlet.  
2. **Minimum Outlets**: At least one receptacle must be provided for the first 9 ft² (0.84 m²) of countertop, with additional outlets for every 18 ft² (1.7 m²) or fraction thereof.  
3. **Installation Height**: Receptacles must be installed not more than 20 inches (500 mm) above the countertop or work surface (CEC 210.52(C)(3)(1)).  

**Exceptions:**  
- Receptacles behind fixed appliances (e.g., ranges, sinks) are exempt from spacing requirements (CEC 210.52(C)(1) Exception).  
- Receptacles in floor-mounted cabinets or more than 1.7 m (5.5 ft) above the floor are not counted toward required outlets (CEC 210.52).  

---

## NEC 2023 Reference  
No difference from NEC 2023. The requirement for GFCI protection of countertop receptacles in kitchens is identical in both codes (NEC 210.8(A)(6)).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.8

**Response Time:** 19.4s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection for Bedroom Circuits in New Residential Construction

**California Requirement (CEC 2022):**  
Per **CEC 2022 Section 210.12(A)**, all 120-volt, 15- and 20-ampere branch circuits supplying outlets in dwelling unit bedrooms **must have arc-fault circuit-interrupter (AFCI) protection**. This includes any bedroom in new residential construction.  

**Exceptions Checked:**  
- No exceptions apply to standard bedroom circuits.  
- The only exception (for fire alarm systems) is irrelevant here.  

**NEC 2023 Reference:**  
No difference from NEC 2023. The requirement for AFCI protection in bedrooms is identical in both codes.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 210.12

**Response Time:** 16.2s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** PASS

**Agent Answer:**
## Can Aluminum Conductors Be Used for a 200A Service? (CEC 2022)

**CEC Requirement:**  
Yes, aluminum conductors are permitted for a 200A service per **CEC 2022 Section 230.42(B)**. The minimum size for aluminum service conductors is **250 kcmil** (75°C rated), which has an ampacity of **205A** (per CEC Table 310.16). This meets the 200A requirement without adjustments for temperature or bundling.

**NEC 2023 Reference:**  
No difference from NEC 2023. Section 230.42(B) in NEC also permits 250 kcmil aluminum for 200A services.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

---

### Supporting Details:
1. **Base Rule**:  
   - CEC 230.42(B) explicitly allows aluminum for service conductors.  
   - Minimum size for aluminum is 250 kcmil (75°C column, Table 310.16).  

2. **Ampacity Calculation**:  
   - 250 kcmil aluminum at 75°C = **205A** (Table 310.16).  
   - No temperature or bundling adjustments needed for standard service installations.  

3. **Exceptions**:  
   - No exceptions override the minimum size or ampacity requirements for this application.  

4. **Terminal Compatibility**:  
   - Ensure terminals are rated for aluminum (per CEC 110.14(C)).  

--- 

**Final Answer**:  
Use **250 kcmil aluminum conductors** for a 200A service. This meets CEC 2022 and NEC 2023 requirements.

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_ampacity, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.14, 230.42, 310.16

**Response Time:** 29.4s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Clearance Depth (CEC 2022)

**Requirement:**  
For a 120/240V residential panel installed under **Condition 2** (exposed live parts on one side and grounded parts on the other, e.g., against a concrete/brick wall), the minimum working clearance depth is **900 mm (3 feet)** per **CEC 2022 Table 110.26(A)(1)**.

**Key Details:**  
- **Voltage Range:** 0–150V (covers 120/240V residential systems).  
- **Condition 2:** Applies when the panel is installed against a grounded surface (e.g., masonry wall).  
- **No Applicable Exceptions:** The standard 900 mm (3 ft) depth is required unless specific exceptions (e.g., low-voltage systems or existing buildings with height reductions) apply, which are not relevant here.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The same 900 mm (3 ft) depth applies under NEC Table 110.26(A)(1) for Condition 2.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 15.5s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** PASS

**Agent Answer:**
## California Requirement (CEC 2022)  
Per **CEC 2022 Section 210.11(C)(1)**, *two or more 20-ampere small-appliance branch circuits* are required to serve all receptacle outlets in kitchens, including countertop and wall outlets.  

**Exceptions Checked**:  
- Exceptions in **210.52(B)** allow additional circuits for specific appliances (e.g., refrigeration) but do not reduce the minimum two-circuit requirement.  
- No California-specific amendments override this rule.  

---

## NEC 2023 Reference  
No difference from NEC 2023. Both codes require **at least two 20-ampere small-appliance branch circuits** for kitchens.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.11, 210.52

**Response Time:** 16.7s

---

### baseline-008: knowledge_simple

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Expected:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## NEC 2023 Requirement for Surge Protection in Residential Services

**Surge protection is required** for a new 200A residential service under NEC 2023.  

### Key Requirements:
1. **Mandatory SPD Installation**  
   Per **NEC 2023 Section 230.67(A)**, services supplying *dwelling units* must include a surge-protective device (SPD). This applies directly to residential services.  

2. **SPD Location and Type**  
   - **Location**: The SPD must be installed *in or adjacent to distribution equipment* on the load side of the service disconnecting means (NEC 225.42(B)).  
   - **Type**: Must be a **Type 1 or Type 2 SPD** with a minimum **10kA nominal discharge current rating** (NEC 225.42(C)).  

3. **No Applicable Exceptions**  
   The exception search for 230.67 found no exemptions for residential services. Exceptions listed (e.g., meters, fire alarm circuits) do not apply to standard dwelling units.  

---

## Final Answer
Yes, surge protection is required for a new 200A residential service under NEC 2023. A Type 1 or Type 2 surge-protective device (SPD) with a minimum 10kA rating must be installed in or adjacent to the service equipment, per **NEC 230.67(A) and 225.42(C)**. No exceptions apply for standard dwelling units.  

✓ **Sources: NEC 2023 Sections 230.67, 225.42**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 2 found
- 230.67, 225.42

**Response Time:** 13.3s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** PASS

**Agent Answer:**
## Service Conductor Sizing for 200A Upgrade (CEC 2022 with NEC Comparison)

---

### **1. Load Calculation (CEC 220.82/220.55)**  
**Appliances**:  
- **Electric Range (12 kW)**:  
  - First 3 kW = 8 kW (demand factor)  
  - Remaining 9 kW × 40% = 3.6 kW  
  - **Total Range Load = 11.6 kW**  

- **Electric Dryer (5.5 kW)**:  
  - Single dryer = 5 kW (per Table 220.54)  

- **Water Heater (4.5 kW)**:  
  - 4.5 kW × 75% (4+ appliances ≥ 500W) = **3.375 kW**  

- **General Lighting (3,000 sq ft × 3 VA/ft²)**: **9 kW**  
- **Small Appliance Circuits (2 × 1,500 VA)**: **3 kW**  
- **Central AC (4 tons ≈ 4.5 kW)**: Non-coincident with heating (no heating listed), so **4.5 kW**  

**Total Calculated Load**:  
9 kW (lighting) + 3 kW (small appliances) + 11.6 kW (range) + 5 kW (dryer) + 3.375 kW (water heater) + 4.5 kW (AC) = **36.475 kW**  

**Service Load in Amperes**:  
36,475 VA ÷ 240 V = **152 A**  

---

### **2. Conductor Sizing (CEC 310.12)**  
Per CEC 310.12(A), service conductors must have **minimum 83% of service rating**:  
200 A × 83% = **166 A required**  

#### **Copper Conductors**  
- **2/0 AWG** at 75°C = **175 A** (CEC Table 310.16)  
- **Adequate** (175 A ≥ 166 A)  

#### **Aluminum Conductors**  
- **4/0 AWG** at 75°C = **180 A** (CEC Table 310.16)  
- **Adequate** (180 A ≥ 166 A)  

---

### **3. Aluminum Use (CEC 110.14(C))**  
- **Permitted** under CEC 110.14(C) for service conductors if rated for 75°C (4/0 AWG aluminum meets this).  
- **Terminal Compatibility**: Ensure all terminations are rated for aluminum (e.g., listed for use with aluminum conductors).  

---

### **4. California Amendments vs. NEC**  
- **Conductor Sizing**:  
  - CEC 310.12 matches NEC 310.12 for 83% rule.  
  - California allows aluminum conductors with proper terminations (same as NEC).  
- **Demand Factors**:  
  - CEC 220.55/220.54 demand factors align with NEC 220.55/220.54.  

---

### **Final Answer**  
- **Required Service Conductors**:  
  - **2/0 AWG copper** or **4...

**Tool Usage:**
- CEC Tools: cec_exception_search, cec_exception_search, cec_search, cec_lookup_conductor_ampacity, cec_lookup_conductor_ampacity
- NEC Tools: nec_search, nec_search, compare_with_nec
- CEC Primary: Yes

**Citations:** 6 found
- 310.12, 220.82, 220.54, 220.55, 110.14, 310.16

**Response Time:** 73.4s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** PASS

**Agent Answer:**
## CEC 2022 Requirements for Multiwire Branch Circuit in Kitchen

**1. Circuit Breaker Requirements (CEC 210.4(B)):**
- **Breaker Type**: Must use a **2-pole circuit breaker with a common trip mechanism** (e.g., handle tie or interlocked breakers). This ensures both ungrounded (hot) conductors are disconnected simultaneously during an overload or short circuit.
- **Breaker Size**: For 12 AWG copper conductors, the overcurrent protection must not exceed **20A** (per CEC Table 310.16 and 240.4(D)).

**2. Neutral Conductor Requirements (CEC 200.4(A) & 210.4(D)):**
- **Sizing**: The neutral conductor must be **12 AWG copper**, same size as the ungrounded conductors, to carry the maximum unbalanced load between the two hot conductors.
- **Termination**: The neutral must terminate on a **separate grounded (neutral) busbar** in the panel, not shared with other circuits unless permitted by 210.4(B) (which limits shared neutrals to two circuits maximum).

**3. Key CEC Sections Cited:**
- **210.4(B)**: Requires multiwire branch circuits to have a means to disconnect all ungrounded conductors at the panelboard.
- **240.4(D)**: Limits overcurrent protection for 12 AWG copper to 20A.
- **200.4(A)**: Prohibits sharing neutral conductors between multiple branch circuits unless specifically permitted.

**4. Exceptions Checked:**
- No exceptions apply to the common trip requirement for multiwire circuits. Informational Note in 210.4(B) emphasizes proper neutral sizing.

---
## NEC 2023 Reference
No difference from NEC 2023. California adopts NEC 210.4(B) and 240.4(D) without amendments for multiwire branch circuits.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_lookup_conductor_ampacity
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 240.4, 210.4, 310.16, 200.4

**Response Time:** 50.8s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

**Locations Requiring GFCI Protection (NEC 210.8(A)):**  
1. **Bathrooms**  
2. **Garages** and accessory buildings with floors at or below grade (storage/work areas)  
3. **Outdoors**  
4. **Crawl spaces** at or below grade level  
5. **Kitchens**  
6. **Areas with sinks** for food preparation/cooking  
7. **Sinks** – receptacles within 1.8 m (6 ft) of the bowl’s top inside edge  
8. **Boathouses**  
9. **Bathtubs/shower stalls** – receptacles within 1.8 m (6 ft) of the outside edge  
10. **Laundry areas**  
11. **Indoor damp/wet locations** (e.g., utility sinks, laundry rooms)  

---

### Exceptions to GFCI Requirements:  
- **Exception 1**: Receptacles for electric snow-melting/deicing equipment (not readily accessible).  
- **Exception 2**: Receptacles for permanently installed premises security systems.  
- **Exception 3**: Weight-supporting ceiling receptacles (WSCR) for ceiling fans/luminaires (if not general-purpose).  
- **Exception 4**: Factory-installed, non-accessible receptacles in bathroom exhaust fans.  
- **Exception 5**: HVAC equipment (expires September 1, 2026).  

---

### NEC 2023 vs. CEC 2022  
- **No material differences** for residential GFCI requirements between NEC 2023 and CEC 2022. California adopts NEC 210.8(A) with no amendments.  

✓ **Sources: NEC 2023 (primary), CEC 2022 (comparison)**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search, nec_search
- CEC Primary: No

**Citations:** 1 found
- 210.8

**Response Time:** 11.7s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirement for Residential Service (CEC 2022)

**California Requirement:**  
Per **CEC 2022 Section 230.67**, surge protection is **required** for all services supplying dwelling units. Key requirements include:  

1. **SPD Type**: Must be a **Type 1 or Type 2 surge-protective device (SPD)**.  
2. **Installation Location**:  
   - The SPD must be an **integral part of the service equipment** or **immediately adjacent** to it.  
   - **Exception**: If the SPD is installed at the **next level distribution equipment downstream** toward the load, it complies with the requirement.  

**Example**: For a 200A residential service, the SPD could be mounted directly on the service panel or placed in a subpanel downstream (e.g., a dedicated circuit panel for sensitive equipment).  

---

## NEC 2023 Reference  
The **NEC 2023 does not explicitly require SPDs** for residential services. CEC 2022 adds this requirement as a California-specific amendment to enhance protection against voltage surges in dwelling units.  

**Key Difference**:  
- **CEC**: Mandates SPDs for all residential services (Section 230.67).  
- **NEC**: No general requirement for SPDs in residential services (covered only in optional or specialized applications).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 1 found
- 230.67

**Response Time:** 14.6s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** PASS

**Agent Answer:**
## CEC 2022 Compliance Analysis

### **Working Space Requirements (CEC 110.26)**
1. **Front Clearance (Depth)**  
   - **Required**: 36 inches (1.0 m) for 240V Condition 2 (exposed live parts on one side, grounded parts on the other).  
   - **Provided**: 24 inches.  
   - **Conclusion**: **Non-compliant**. The 24-inch clearance is insufficient (Table 110.26(A)(1)).  

2. **Side Clearance (Width)**  
   - **Required**: 30 inches (width of equipment or 30 in., whichever is greater).  
   - **Provided**: 18 inches to the side of the water heater.  
   - **Conclusion**: **Non-compliant** unless the panel width is < 30 inches (unclear from question).  

3. **Height Requirement**  
   - **Required**: 6.5 ft (78 in.) from floor to ceiling.  
   - **Provided**: Not specified, but assume standard closet height (≥6.5 ft).  
   - **Conclusion**: **Compliant** if height ≥ 6.5 ft.  

---

### **Exceptions Checked**
- **Existing Buildings (110.26(A)(1)(c))**: Not applicable (voltage > 30V).  
- **Low-Voltage Exception (110.26(A)(1)(b))**: Not applicable (240V > 30V).  

---

### **Final Determination**
- **Front Clearance**: **Fails** CEC 110.26(A)(1) (24" < 36" for Condition 2).  
- **Side Clearance**: **Fails** if panel width ≥ 30 inches.  
- **Overall Compliance**: **Non-compliant** due to insufficient front clearance.  

**CEC Reference**:  
- **110.26(A)(1)**: Minimum depth of 36 inches required for Condition 2.  

**Recommendation**: Increase front clearance to at least 36 inches and ensure side clearance meets 30 inches.  

---

## NEC 2023 Reference  
- **110.26(A)(1)**: Minimum depth of 30 inches for Condition 2 (NEC).  
- **Difference from CEC**: CEC requires stricter 36-inch depth for 240V installations.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search, cec_lookup_working_space
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 29.7s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** PASS

**Agent Answer:**
## CEC 2022 Compliance Analysis

**1. Overcurrent Protection (CEC 2022 Section 240.4(D))**  
- **12 AWG copper conductors** are permitted to be protected by a **20A overcurrent device** (✓ Compliant).  
- This matches the 20A breaker in the scenario.  

**2. Multiple Conductors on a Single Terminal (CEC 2022 Section 110.14(A))**  
- **Critical violation**: The breaker terminal is **not marked for two conductors**.  
- Per 110.14(A), terminals for more than one conductor **must be identified** for such use.  
- **No exception** in CEC allows bypassing this requirement for standard breaker terminals.  

**3. NEC Comparison**  
- NEC 2023 has **identical requirements** (Section 110.14(A) and 240.4(D)).  
- No California-specific amendments apply here.  

---

## Final Determination  
**This is a code violation under CEC 2022.**  

**Reasoning**:  
- While the 20A breaker matches the 12 AWG conductor's overcurrent protection requirements (✓),  
- The termination of **two conductors on a terminal not marked for multiple conductors** violates **CEC 110.14(A)**.  

**Corrective Action**:  
- Replace the breaker with one explicitly marked for two 12 AWG conductors, or  
- Use a single conductor per terminal with an approved connector for parallel conductors.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 240.4, 110.14

**Response Time:** 32.9s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** PASS

**Agent Answer:**
## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

### **California Requirement (CEC 2022)**
1. **Grounding Electrode System**  
   - A **separate grounding electrode** (e.g., ground rod, concrete-encased electrode) **must be installed at the detached garage** per **CEC 2022 Section 250.32(A)**.  
   - The grounding electrode conductor must connect the subpanel’s grounding bus to this electrode.  
   - **Exception**: Not required if the garage is supplied by a **single branch circuit** (not applicable here due to 4-wire feeder).

2. **Equipment Grounding Conductor (EGC)**  
   - An **equipment grounding conductor** (4th wire in the feeder) must run with the feeder conductors to the subpanel.  
   - The EGC size is determined by **CEC 250.122**, based on the overcurrent protection rating of the feeder.  

3. **Bonding and Neutral Isolation**  
   - The **neutral and ground bars must be isolated** in the subpanel.  
   - The **neutral bar** connects only to the **main panel’s grounding system** (no connection at the subpanel).  
   - The **grounding electrode conductor** connects the subpanel’s grounding bus to the local grounding electrode.  

4. **Grounding Electrode Conductor Size**  
   - Sizing follows **CEC Table 250.66**, based on the largest ungrounded conductor in the feeder.  

---

## NEC 2023 Reference  
No difference from NEC 2023. The configuration alignss with NEC 250.32 and 250.122.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 250.122, 250.32, 250.66

**Response Time:** 17.8s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** PASS

**Agent Answer:**
## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

---

### **Main Bonding Jumper**  
**Definition**:  
Per CEC 2022 Section 250.28, the **main bonding jumper** connects the grounded conductor (neutral) to the equipment grounding conductor at the **service equipment**. It ensures electrical continuity between the neutral and equipment grounding system at the service.  

**When Required**:  
- **At every service** (250.24(B)).  
- Must be sized per Table 250.102(C)(1) based on the largest ungrounded service conductor.  
- Required for services with multiple enclosures (250.28(D)(2)).  

**Key Requirements**:  
- Material: Copper, aluminum, or corrosion-resistant material (250.28(A)).  
- Size: Minimum size per Table 250.102(C)(1).  

---

### **System Bonding Jumper**  
**Definition**:  
Per CEC 2022 Section 250.30, the **system bonding jumper** connects the grounded conductor to the equipment grounding conductor at the **source of a separately derived system** (e.g., transformers, generators).  

**When Required**:  
- **For all grounded separately derived systems** (250.30(A)(1)).  
- Installed at the **source** or **first disconnecting means** of the derived system.  
- Required for systems with multiple enclosures (250.30(A)(1)(3)).  

**Key Requirements**:  
- Must be unspliced (250.30(A)(1)).  
- Size: Per Table 250.102(c)(1), based on the largest ungrounded conductor of the derived system.  
- Exceptions:  
  - For small transformers (≤1000 VA), minimum size is 14 AWG copper or 12 AWG aluminum (250.30(A)(1)(3)).  
  - Parallel paths allowed under specific conditions (250.30(A)(1) Exception No. 2).  

---

### **Key Differences**  
| Feature                  | Main Bonding Jumper                     | System Bonding Jumper                          |
|--------------------------|----------------------------------------|------------------------------------------------|
| **Location**              | Service equipment                      | Separately deri...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 4 found
- 250.28, 250.102, 250.30, 250.24

**Response Time:** 16.4s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
**1. Required Small-Appliance Branch Circuits for Kitchens**  
Per **CEC 2022 Section 210.11(C)(1)**, **two or more 20-ampere small-appliance branch circuits** are required to serve all receptacle outlets in kitchens, including wall, floor, countertop, and refrigeration equipment outlets.  

**2. Serving Dining Room Receptacles**  
Yes, these circuits **can supply dining room receptacles** under **CEC 210.52(B)(1)**. The code explicitly permits small-appliance branch circuits to serve "other rooms specified in 210.52(B)(1)" (e.g., dining rooms, family rooms). However:  
- **No small-appliance branch circuit shall serve more than one kitchen** (Exception to 210.52(B)(1)).  
- Dining room receptacles must comply with spacing rules (1.8 m/6 ft maximum from any wall point, per 210.52(A)(1)).  

**3. Exceptions**  
- A receptacle for a specific appliance (e.g., electric clock, gas range lighting) may be added to a small-appliance circuit (Exception No. 2 to 210.52(B)(1)).  
- Additional small-appliance circuits are permitted but not required.  

---

## NEC 2023 Reference  
No difference from NEC 2023. The requirements for small-appliance branch circuits and their use in dining rooms are identical between CEC 2022 and NEC 2023.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: compare_with_nec, compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 210.11, 210.52

**Response Time:** 23.6s

---

### core-010: load_calculations

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Expected:** Base ampacity: 30A at 90°C (Table 310.16). Temperature correction factor: 0.82 for 50°C (Table 310.15(B)(1)). Bundling adjustment: 0.80 for 6 conductors (Table 310.15(C)(1)). Adjusted ampacity = 30A × 0.82 × 0.80 = 19.68A, approximately 20A.

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- 6 current-carrying 12 AWG THHN copper conductors
- Ambient temperature: 50°C
- Conductor temperature rating: 90°C (THHN)

**1. Base Ampacity**  
From CEC 2022 Table 310.16:  
12 AWG copper at 90°C = **30 amperes**

**2. Temperature Correction**  
From CEC 2022 Table 310.15(B)(1):  
50°C ambient → **0.82 correction factor**

**3. Bundling Adjustment**  
From CEC 2022 Table 310.15(C)(1):  
6 conductors → **0.80 adjustment factor**

**4. Calculation**  
$$
\text{Adjusted Ampacity} = 30 \, \text{A} \times 0.82 \times 0.80 = 19.68 \, \text{A}
$$

**Final Answer:**  
The adjusted ampacity is **19.68 amperes** per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

---
## NEC 2023 Reference  
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 20.5s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## NEC 2023 Requirement  
The National Electrical Code (NEC) requires **arc-fault circuit interrupter (AFCI) protection** for bedrooms and living areas to mitigate the risk of **electrical fires caused by arc faults**.  

### Key Code References:  
1. **NEC 210.12(B)**  
   - Mandates AFCI protection for **dwelling unit branch circuits** in:  
     - Bedrooms  
     - Living rooms  
     - Hallways  
     - Closets  
     - Bathrooms  
     - Similar areas  

2. **NEC 100 Definition**  
   - An **arc fault** is defined as an unintended electrical discharge (arc) that generates heat, potentially igniting surrounding materials.  

### Electrical Hazard Prevented  
AFCIs detect **series arcs** (e.g., from damaged wiring, loose connections, or deteriorated cords) and **parallel arcs** (e.g., from short circuits). These arcs can reach temperatures exceeding **3,500°F**, igniting combustible materials like wood, paper, or fabric.  

### Exceptions  
- No exceptions apply to bedrooms/living areas under 210.12(B).  
- Exceptions exist for fire alarm systems (Exception No. 1) and arc welding equipment (Exception No. 2), but these are unrelated to residential sleeping/occupancy areas.  

**NEC 2023 Reference:**  
No difference from NEC 2023.  

✓ **Sources: NEC 2023 (primary)**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 1 found
- 210.12

**Response Time:** 16.2s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Torque Specifications for Conductor Terminations (CEC 2022)

**California Requirement (CEC 2022):**  
Torque specifications are critical to ensure proper conductor termination in panels, as outlined in **CEC 2022 Section 110.14(D)** and **Section 430.9(C)**:  

1. **Section 110.14(D)**:  
   - *Requirement*: "Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer. An approved means shall be used to achieve the indicated torque value."  
   - *Purpose*: Ensures connections are secure enough to prevent loosening over time, reducing risks of overheating, arcing, or equipment failure.  
   - *Approved Methods*: Torque tools, shear bolts, or breakaway devices with visual indicators.  
   - *Informational Notes*:  
     - Contact manufacturers for torque values if not provided.  
     - Refer to UL 486A-486B or NFPA 70B for additional guidance.  

2. **Section 430.9(C)**:  
   - *Requirement*: Control circuit devices with screw-type terminals for 14 AWG or smaller copper conductors must be torqued to a minimum of **0.8 N·m (7 lb-in.)** unless otherwise identified.  

**Why Torque Matters**:  
- Improper torque can lead to poor electrical contact, increasing resistance and heat.  
- Over-tightening may damage terminals or insulation; under-tightening risks loose connections.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The requirements in **NEC 2023 Section 110.14(D)** mirror CEC 2022, emphasizing manufacturer-specified torque values and approved tightening methods.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 2 found
- 110.14, 430.9

**Response Time:** 12.8s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Service Load Calculation (CEC 2022)

**1. General Lighting Load**  
3 VA/sq ft × 3000 sq ft = **9000 VA**  
Demand factor: First 3000 VA @ 100% + Remaining 6000 VA @ 35%  
= 3000 + (6000 × 0.35) = **5100 VA**  

**2. Small Appliance Circuits**  
2 × 1500 VA = **3000 VA**  
Laundry circuit: **1500 VA**  
Total: 3000 + 1500 = **4500 VA**  

**3. Electric Range**  
12 kW nameplate → **8000 VA** (per CEC Table 220.55 demand factor)  

**4. Electric Dryer**  
5.5 kW nameplate → **5500 VA** (per CEC Table 220.54: use nameplate rating)  

**5. Central AC**  
4600 VA (non-coincident with heating, no heating load specified)  

**Total Service Load Calculation**  
5100 (lighting) + 4500 (appliances) + 8000 (range) + 5500 (dryer) + 4600 (AC) = **27,700 VA**  

**Convert to Amps**  
27,700 VA ÷ 240V = **115.42A**  

---

## Final Determination  
The calculated service load is **115.42A**, well below the 200A panel rating.  

**✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)**  
**No difference from NEC 2023** – CEC 2022 aligns with NEC for demand factors and load calculations in this scenario.

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search, cec_exception_search
- NEC Tools: nec_search, nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 220.54, 220.55

**Response Time:** 33.8s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## NEC Violations in Residential Garage Electrical Panel

### 1. **Working Space Depth Violation**  
**NEC 110.26(A)(1)** requires a minimum working space depth of **30 inches** for panels operating at 100–250 volts (Condition 2: live parts on one side, grounded on the other).  
- **Measured depth**: 28 inches (insufficient).  
- **Violation**: Fails to meet the 30-inch minimum depth requirement.  

---

### 2. **Obstruction in Working Space**  
**NEC 110.26(B)** mandates that working space must be **clear of obstructions** and not used for storage.  
- **Water heater placement**: Located 16 inches to the left of the panel.  
- **Violation**: If the panel width is ≤30 inches, the required working space width is 30 inches (NEC 110.26(A)(2)). A water heater within this zone blocks access and violates the "clear space" rule.  

---

### 3. **Working Space Height Compliance**  
**NEC 110.26(A)(3)** requires working space height to be **2.0 meters (6.5 ft)** or the height of the equipment, whichever is greater.  
- **Panel height**: Surface-mounted at 5 ft (60 inches). Assuming the panel itself is ≤6.5 ft tall, the working space height is **compliant**.  

---

### 4. **Entrance/Access Compliance**  
**NEC 110.26(C)(1)** requires at least one entrance of **24 in width × 6.5 ft height**. No violations reported for this.  

---

## Summary of Violations  
1. **Depth**: 28 in < 30 in (Table 110.26(A)(1)).  
2. **Obstruction**: Water heater intrudes into required working space.  

---

## NEC 2023 Reference  
- **110.26(A)(1)**: Minimum depth for Condition 2 = 30 in.  
- **110.26(B)**: No obstructions in working space.  

✓ **Sources: NEC 2023 (primary)**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 1 found
- 110.26

**Response Time:** 17.0s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## Final Answer

**1. Countertop Receptacles (20A circuits):**  
- **Protection Required:** Combination AFCI/GFCI breaker  
- **NEC References:**  
  - **210.8(B):** GFCI protection required for all countertop receptacles.  
  - **210.12(A):** AFCI protection required for all kitchen branch circuits.  

**2. Dishwasher (15A dedicated circuit):**  
- **Protection Required:** Standard breaker  
- **NEC References:**  
  - **210.8(B)(2):** Fixed appliances (e.g., dishwashers) are exempt from GFCI if not easily accessible.  
  - **210.12(B):** Fixed appliances are exempt from AFCI requirements.  

**3. Garbage Disposal (15A dedicated circuit):**  
- **Protection Required:** Standard breaker  
- **NEC References:**  
  - **210.8(B)(2):** Fixed appliances (e.g., garbage disposals) are exempt from GFCI.  
  - **210.12(B):** Fixed appliances are exempt from AFCI.  

**4. Refrigerator (20A dedicated circuit):**  
- **Protection Required:** Standard breaker  
- **NEC References:**  
  - **210.8(B)(2):** Fixed appliances (e.g., refrigerators) are exempt from GFCI.  
  - **210.12(B):** Fixed appliances are exempt from AFCI.  

---

**Key Notes:**  
- **Fixed appliances** (dishwasher, garbage disposal, refrigerator) are defined as permanently connected and not easily accessible, qualifying for exceptions in **210.8(B)(2)** and **210.12(B)**.  
- **Countertop receptacles** must comply with both GFCI and AFCI requirements due to their general accessibility and higher risk of faults.  

✓ **Sources:** NEC 2023 (references verified via training data).

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_search, nec_search, nec_search, nec_search, nec_search, nec_search, nec_search, nec_search, nec_exception_search, nec_exception_search, nec_exception_search, nec_exception_search
- CEC Primary: No

**Citations:** 2 found
- 210.12, 210.8

**Response Time:** 44.0s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## Corrected Subpanel Configuration for Detached Garage

### **Violations Confirmed**
1. **Bonded Neutral/Ground Bars** (CEC 250.24(B) violation)  
   - **Issue**: Neutral and ground bars are bonded with a main bonding jumper.  
   - **Fix**: Remove the bonding jumper to isolate neutral and ground bars in the subpanel.  

2. **Neutral Bar Bonded to Enclosure** (CEC 250.24(B) violation)  
   - **Issue**: Neutral bar is bonded to the metal enclosure.  
   - **Fix**: Disconnect the neutral bar from the enclosure. Neutrals must only connect at the main panel.  

3. **Missing Local Grounding Electrode** (CEC 250.32(B) violation)  
   - **Issue**: No grounding electrode (e.g., ground rod) installed at the detached garage.  
   - **Fix**: Install an 8 ft copper ground rod and connect it to the subpanel’s ground bar via a **#6 copper** or **#4 aluminum** grounding electrode conductor (GEC).  

---

### **Correct Configuration Steps**
1. **Isolate Neutral and Ground Bars**  
   - Remove the main bonding jumper between neutral and ground bars.  
   - Connect **feeder neutral** to the isolated neutral bar.  
   - Connect **feeder ground** to the ground bar.  

2. **Bond Ground Bar to Enclosure**  
   - Maintain the bond between the ground bar and metal enclosure (already correct).  

3. **Install Local Grounding Electrode**  
   - Drive an 8 ft copper ground rod near the subpanel.  
   - Connect the rod to the ground bar using a **#6 copper** GEC (based on #2 AWG aluminum feeders).  

---

### **Calculations and Code References**
- **GEC Sizing**:  
  - Feeder conductor: #2 AWG aluminum (115A ampacity).  
  - Per CEC Table 250.66, GEC must be **#6 copper** or **#4 aluminum**.  

- **Exceptions Checked**:  
  - No exceptions apply to 250.24(B) or 250.32(B) for this configuration.  

---

## NEC vs. CEC Comparison
- **No material difference** between CEC 2022 and NEC 2023 for subpanel grounding/bonding in detached structures.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (compari...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_lookup_grounding_conductor
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 250.24, 250.32, 250.66

**Response Time:** 59.0s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**


### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**


### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

**Given:**
- 6 current-carrying 12 AWG TW (60°C) copper conductors
- Ambient temperature: 43°C (110°F)

**1. Base Ampacity (CEC Table 310.16):**
12 AWG copper at 60°C = **20 amperes**

**2. Temperature Correction (CEC Table 310.15(B)(1)):**
43°C ambient → **0.71 correction factor**

**3. Bundling Adjustment (CEC Table 310.15(C)(1)):**
6 conductors → **0.70 adjustment factor**

**4. Final Calculation:**
```python
adjusted_ampacity = 20 × 0.71 × 0.70 = 9.94 amperes
```

**5. Overcurrent Protection Check (CEC 240.4(D)):**
- 12 AWG copper is limited to **20A overcurrent protection** (no conflict with 9.94A adjusted ampacity)

**Final Answer:**  
The adjusted ampacity is **9.94 amperes** after applying both temperature correction and bundling adjustment factors.

---
## NEC 2023 Reference  
No difference from NEC 2023. Same ampacity values and adjustment factors apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: compare_with_nec
- CEC Primary: Yes

**Citations:** 3 found
- 240.4, 310.15, 310.16

**Response Time:** 13.1s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Minimum Size Copper Grounding Electrode Conductor (GEC) for 1000 kcmil Service Conductors

**CEC 2022 Requirement:**  
Per CEC Table 250.66, the grounding electrode conductor (GEC) for service conductors totaling **1000 kcmil** (four parallel 250 kcmil conductors) is sized based on the **next higher size** listed in the table. For service conductors up to 600 kcmil, the GEC is **1/0 AWG copper**. Since 1000 kcmil exceeds the table's listed sizes, the GEC remains **1/0 AWG copper** (per the "next higher size" rule in NEC/CEC 250.66).

**Exceptions Considered:**  
- **Exception 250.66(A)**: If connected to rod, pipe, or plate electrodes, the GEC could be reduced to **6 AWG copper** if it does not extend to other electrode types. However, this applies only to specific electrode types and is not the general rule.  
- **Exception 250.66(B)**: For concrete-encased electrodes, the GEC could be **4 AWG copper**, but this is also electrode-specific.  

**Final Answer:**  
The minimum size copper GEC required is **1/0 AWG** for 1000 kcmil service conductors under CEC 2022 Table 250.66.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The same logic applies: for service conductors exceeding the table's listed sizes, the GEC is sized based on the next higher size (NEC 250.66).  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 31.5s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 21/28
- **Success Rate**: 92.9%
- **Average Response Time**: 26.7s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

