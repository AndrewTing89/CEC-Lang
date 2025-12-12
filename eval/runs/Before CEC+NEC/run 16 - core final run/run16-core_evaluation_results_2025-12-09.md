# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-09
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 28 |
| **Successful** | 28 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 396.5s |
| **Avg per Question** | 14.2s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Ampacity of 12 AWG Copper Conductor (CEC 2022)  

**Ampacity**: **25 amperes** at 75°C termination  
Per CEC 2022 Table 310.16 (California amendment retains NEC 2023 values).  

---

### **Exceptions Found** (Relevance to General Use):  
1. **Section 440.6** (Relevance: 0.50):  
   - Applies to **hermetic refrigerant motor-compressors** and **multimotor equipment**.  
   - Uses nameplate current for conductor sizing.  
   - **Not applicable** to general 12 AWG copper conductors unless specifically used in refrigeration/motor-compressor circuits.  

2. **Section 311.12** (Relevance: 0.33):  
   - Minimum conductor sizes for **transformer windings** and **similar specialized applications**.  
   - **Not applicable** to standard branch circuits.  

---

### **Key Limitations**  
- **Overcurrent Protection**:  
  Per CEC 240.4(D), 12 AWG copper is **limited to 20A protection** despite 25A ampacity.  
  (California amendment: [CEC 240.4(D)] retains NEC 2023 limits).  

- **Adjustments Required If**:  
  - More than 3 conductors (apply bundling correction from 310.15(C)(1)).  
  - Ambient ≠ 30°C (apply temperature correction from 310.15(B)).  

---

✓ **Source**: CEC 2022 Table 310.16, 240.4(D), 440.6, 311.12  
✓ **Note**: Exceptions apply only to specialized equipment (e.g., refrigeration systems). For general use, 25A ampacity with 20A OCP limit remains valid.

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 310.16, 310.15, 440.6, 240.4, 311.12

**Response Time:** 11.3s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size:** **6 AWG copper**  
- **Ampacity:** 65A (Table 310.16, 75°C column)  
- **Overcurrent Protection:** 60A or 65A breaker (per CEC 240.4)  

**Key Notes:**  
1. **6 AWG** is the smallest conductor with ampacity ≥ 60A at 75°C.  
2. **8 AWG (50A)** is insufficient for a 60A circuit.  
3. **Overcurrent Protection Rules:**  
   - **240.4(D)** does not apply to 6 AWG (only covers 18–10 AWG).  
   - Per **240.4**, overcurrent protection must not exceed the conductor's ampacity (65A).  
   - A **60A or 65A breaker** is acceptable.  
4. **Exceptions Verified:**  
   - Exceptions in **440.6** apply only to refrigerant motor-compressors (not relevant here).  
   - No other exceptions apply to standard installations.  

**CEC vs NEC:** Same result under NEC 2023 Table 310.16. No California amendments affect this calculation.  

✓ Source: CEC 2022 Table 310.16, Section 240.4

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_exception_search, cec_find_limiting_rules, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 440.6, 240.4, 310.16

**Response Time:** 16.7s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection in Residential Kitchens (CEC 2022)

In residential kitchens, **GFCI protection is required for all 125-volt, 15- or 20-ampere receptacles installed to serve countertop surfaces** per **CEC 2022 Section 210.8(A)(6)**. 

### Key Requirements:
1. **Scope**: Applies to dwelling units (residential) kitchens.
2. **Protection Method**: GFCI protection must be provided via a GFCI circuit breaker or GFCI receptacle.
3. **No Applicable Exceptions**:
   - The exception in **210.8(A)** regarding ceiling luminaires/fans does not apply to countertop receptacles, as they are general-purpose convenience outlets.
   - No other exceptions in the code relieve this requirement for kitchen countertop receptacles.

### Additional Context:
- **Distance Rule**: Receptacles must be within 6 feet of the countertop edge (per 210.52(C)(2)(b)), but GFCI protection applies regardless of location on the countertop.
- **California-Specific**: No amendments to NEC requirements for kitchens in CEC 2022.

### Example:
A kitchen with a 10-foot countertop requiring two 20A receptacles (per 210.52(C)(2)(a)) must have both receptacles GFCI-protected.

✓ Source: CEC 2022 Section 210.8(A)(6) with exception analysis.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.8, 210.52

**Response Time:** 10.9s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection for Bedroom Circuits (CEC 2022)

**Answer:**  
Yes, **AFCI protection is required** for bedroom circuits in new residential construction under CEC 2022.  

### Key Details:
- **Primary Rule:** CEC 2022 **Section 210.12(A)** mandates AFCI protection for all 120V, 15A, and 20A branch circuits in dwelling units, including bedrooms.  
- **Exceptions Checked:**  
  - No exceptions in CEC 2022 exempt standard bedroom circuits from AFCI requirements.  
  - Cross-referenced rules (e.g., 406.4, 210.70) address receptacle replacements or lighting outlets but do not override AFCI obligations for new construction.  

### Compliance Methods:
Use one of these AFCI protection methods as outlined in **210.12(A)(1)–(6):**
1. **Combination-type AFCI** at the service panel.  
2. **Branch/feeder-type AFCI** paired with an outlet branch-circuit AFCI.  
3. **Supplemental arc protection circuit breaker** with outlet AFCI (under specific conditions).  

**No exceptions apply** to standard bedroom circuits in new residential construction.  

✓ Source: CEC 2022 Sections 210.12(A), 406.4, 210.70

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 210.12, 406.4, 210.70

**Response Time:** 9.4s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** PASS

**Agent Answer:**
## Aluminum Conductors for 200A Service (CEC 2022)  

**Yes**, aluminum conductors are permitted for a 200A service. The required size is:  

**4/0 AWG aluminum**  
- Per **CEC Table 310.12(A)** (Single-Phase Dwelling Services and Feeders)  
- Ampacity: 200A at 75°C (meets 83% of 200A = 166A minimum requirement)  

---

### Code Verification and Exceptions:  
1. **Minimum Size Compliance**  
   - **CEC 310.3(A)**: Minimum aluminum conductor size is 12 AWG. **4/0 AWG** exceeds this requirement.  

2. **Ampacity Requirement**  
   - **CEC 310.12(A)**: Service conductors must have an ampacity of **at least 83% of the service rating** (200A × 0.83 = 166A).  
   - **4/0 AWG aluminum** has an ampacity of **200A** (Table 310.12(A)), satisfying this requirement.  

3. **Overcurrent Protection**  
   - **CEC 230.90**: Overcurrent protection (200A breaker) must not exceed the conductor ampacity. **200A ≤ 200A** is compliant.  

4. **No Conflicting Exceptions**  
   - Exceptions in **310.12** and **310.3** do not restrict aluminum use for this application.  
   - **Parallel Conductors**: Not required here (single 4/0 AWG suffices).  

---

### Key Requirements:  
- **Termination**: Equipment must be rated for aluminum conductors (e.g., CO/ALR markings).  
- **Overcurrent Protection**: 200A breaker per Table 310.12(A).  
- **No Adjustments**: Temperature or bundling corrections not needed if installation conditions align with table assumptions.  

✓ **Source**: CEC 2022 Table 310.12(A), Sections 310.3, 230.90

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 230.90, 310.12, 310.3

**Response Time:** 13.8s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Clearance Depth (CEC 2022)  

For a **120/240V residential electrical panel** (120V to ground, Condition 1), the **minimum working clearance depth** required is:  

**900 mm (3 feet)**  
Per **CEC 2022 Table 110.26(A)(1)**.  

---

### Exception Analysis:  
After reviewing exceptions via `cec_exception_search(110.26(A)(1))`:  
1. **Section 110.26(E)** discusses *dedicated electrical space* (vertical clearance above equipment) but does not override the **depth requirement** for Condition 1.  
2. **Section 110.26(A)(1)(a)** confirms the depth values in Table 110.26(A)(1) apply unless specific conditions (e.g., dead-front assemblies, low-voltage systems) are met.  
   - Your scenario (standard residential panel) does **not** qualify for these exceptions.  
3. **Exception No. 2** in 110.26(A)(3) permits reduced height in existing dwellings but **does not affect depth requirements**.  

---

### Final Answer:  
The **minimum depth of working clearance** in front of the panel remains **900 mm (3 feet)** as per Table 110.26(A)(1). No applicable exceptions reduce this requirement for standard residential installations.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 8.8s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** PASS

**Agent Answer:**
## Small Appliance Branch Circuits in Kitchens (CEC 2022)  

**Minimum Requirement:**  
A kitchen requires **not fewer than two** 20-ampere small-appliance branch circuits.  

**Code Basis:**  
- **CEC 2022 Section 210.52(B)(1):**  
  Mandates two or more 20A circuits to serve all kitchen receptacles (countertops, wall outlets, and refrigerator).  
- **CEC 210.11(C)(1):**  
  Reinforces the requirement for two or more small-appliance circuits in kitchens.  

**Exceptions:**  
1. **Exception No. 1 (210.52(B)(1)):**  
   Allows switched receptacles supplied from a general-purpose 15- or 20-ampere branch circuit (e.g., for lighting).  
2. **Exception No. 2 (210.52(B)(1)):**  
   Permits a specific appliance (e.g., a microwave) to be supplied by an individual branch circuit rated ≥15A.  

**Key Details:**  
- Circuits must serve **only one kitchen** (no shared circuits between kitchens).  
- Exceptions allow **additional circuits** but do not reduce the minimum requirement.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.11

**Response Time:** 9.1s

---

### baseline-008: knowledge_simple

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Expected:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is required for a new 200A residential service under the CEC 2022, but there is an exception regarding installation location.  

**Citations:**  
1. **CEC 2022 Section 230.67(A):** Mandates surge-protective devices (SPDs) for services supplying dwelling units.  
2. **Exception to 230.67(B):** Permits the SPD to be located at the next level of distribution equipment downstream (not necessarily in the service equipment).  

**Key Details:**  
- **Requirement:** SPDs must be installed for all residential services.  
- **Location Flexibility:** The SPD can be placed in downstream distribution equipment (e.g., a panelboard) instead of the service equipment itself, provided it is "immediately adjacent" or at the next distribution level.  
- **Type:** Must be a Type 1 or Type 2 SPD (Section 230.67(C)).  

**No Exemption for Residential Services:**  
The CEC does not exempt residential services from SPD requirements. The exception only modifies the installation location, not the mandate itself.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 230.67

**Response Time:** 9.4s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** PASS

**Agent Answer:**
## Final Answer: Service Conductor Sizing for 200A Residential Upgrade (CEC 2022)

**Required Service Conductor Sizes:**
- **Copper:** 2/0 AWG (CEC Table 310.12(A))
- **Aluminum:** 4/0 AWG (CEC Table 310.12(A))

**Aluminum Permissibility:**
- ✅ **Allowed** per CEC 2022:
  - Section 310.3(B) permits aluminum conductors
  - Section 230.31(B) allows aluminum service conductors ≥6 AWG (4/0 meets this)
  - No temperature/adjustment factors applied (standard dwelling service conditions)

**Key Exceptions Verified:**
1. **Overcurrent Protection (230.90):** 
   - Exception No. 5 allows 310.12(A) ampacity for 120/240V dwelling services
   - Confirms 200A service conductors can use 83% rule (166A minimum) if load calculations justify
   - *Our case uses full 200A rating as required by standard service upgrade*

2. **Material Requirements (310.3):**
   - Confirms aluminum conductors must be AA-8000 series alloy
   - Minimum aluminum size for service conductors is 6 AWG (4/0 complies)

**Final Code Compliance:**
- Conductor sizing follows CEC Table 310.12(A) for single-phase dwelling services
- Aluminum use complies with Sections 310.3(B) and 230.31(B)
- No applicable exceptions override the required conductor sizes

**Note:** Aluminum requires proper termination practices (torque specifications, anti-oxidant compound) per CEC 110.14(C) and 230.31(B).

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 110.14, 310.12, 230.31, 310.3, 230.90

**Response Time:** 11.8s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** PASS

**Agent Answer:**
## California Exceptions for Multiwire Branch Circuit (CEC 2022)

### Key Exceptions Found:
1. **Neutral Continuity** (CEC 210.4(D) + 300.13(B)):
   - Requires **neutral conductor continuity** in multiwire circuits (no device terminations on neutral).
   - Reinforces NEC 200.4(B) grouping requirements for multi-circuit neutrals.

2. **Disconnect Requirements** (CEC 210.4(B)):
   - Mandates **simultaneous disconnection of all ungrounded conductors** (2-pole breaker or handle-tied breakers).
   - No California-specific amendments to this requirement.

3. **No Additional Exceptions**:
   - CEC exceptions for 210.4 do not relax NEC requirements for kitchen MWBCs.
   - No California-specific amendments to neutral termination rules for 12/3 cable in residential applications.

### Final Answer with CEC Compliance:
The requirements for the 12/3 MWBC in the kitchen are the same as NEC 2023 with no California amendments:
- **Breaker**: 2-pole 20A or handle-tied single-pole 20A breakers (CEC 210.4(B))
- **Neutral**: Must use **pigtail splices** at receptacles (CEC 200.4(B) + 300.13(B))
- **No neutral overcurrent protection** (CEC 250.24(D))

✓ Source: CEC 2022 with NEC 2023 comparison

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 4 found
- 210.4, 300.13, 200.4, 250.24

**Response Time:** 12.7s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Dwellings (NEC 2023 with CEC Exceptions)

### **Required Locations for GFCI Protection**  
Per **NEC 2023 Section 210.8(A)** and **CEC 2022 exceptions**, GFCI protection is required for all 120–250V receptacles in these residential locations:

1. **Bathrooms**  
2. **Garages/accessory buildings** (floor at or below grade, non-habitable)  
3. **Outdoors**  
   - *Exception:* Non-readily accessible receptacles for **snow-melting/deicing systems** (per 426.28/427.22).  
4. **Crawl spaces** (at or below grade)  
5. **Basements**  
   - *Exception:* Receptacles for **fire alarm/burglar alarm systems** (per 760.41(B)/760.121(B)).  
6. **Kitchens** (countertop surfaces)  
7. **Sinks** – within **1.8 m (6 ft)** of the bowl’s top inside edge  
8. **Boathouses**  
9. **Bathtubs/shower stalls** – within **1.8 m (6 ft)** of the outside edge  
10. **Laundry areas**  
11. **Indoor damp/wet locations**  

---

### **Key Exceptions (Where GFCI May Be Exempt)**  
1. **Ceiling luminaires/fans**:  
   - Listed **locking support receptacles** for ceiling fans/luminaires (not general-use convenience receptacles).  
2. **Industrial labs**:  
   - Receptacles within **1.8 m (6 ft)** of sinks if power interruption creates greater hazards (Exception No. 3 to 210.8(B)(5)).  
3. **Healthcare facilities**:  
   - Patient bed locations in **Category 1/2 spaces** may comply with 517.21.  
4. **Rooftop receptacles**:  
   - Not required to be readily accessible (Exception to 210.8(B)(3)).  
5. **Special equipment**:  
   - **HVAC systems** (Exception No. 2 to 210.8(B)).  
   - **Vending machines** (per 422.5).  

---

### **Cross-Referenced Rules**  
- **Feeders**: GFCI protection permitted via 215.9 (feeders).  
- **Appliances**: See 422.5 for GFCI requirements for specific appliances.  
- **Boat hoists**: Refer to 555.9.  

---

### **Critical Notes**  
- **Measurement rule**: Distance from receptacles is the shortest path a cord would follow witho...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 10 found
- 210.8, 427.22, 517.21, 426.28, 555.9, 215.9, 760.41, 422.5, 682.15, 760.121

**Response Time:** 14.7s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirements for Residential Services (CEC 2022)

**Requirement:**  
Surge protection **is required** for all new residential services per **CEC 2022 Section 230.67**.  

**Installation Locations:**  
1. **Integral to service equipment** (main panel)  
2. **Immediately adjacent** to the service equipment  
3. **Downstream distribution equipment** (per Exception in 230.67(B)):  
   - If installed at the next level of distribution (e.g., subpanel), it must be "immediately adjacent" to the service equipment in terms of electrical continuity  

**SPD Type:**  
- Must be **Type 1 or Type 2** surge-protective device (SPD)  

**Key Exceptions:**  
- Section 230.94 allows Type 1 SPDs to be installed on the **supply side** of the service disconnecting means (e.g., at the meter base) if properly coordinated  

**Cross-Reference Verified:**  
- Exception in **230.67(B)** explicitly permits downstream installation at next-level distribution equipment  
- No conflicting rules found in limiting rules or additional exceptions  

✓ Source: CEC 2022 Section 230.67, 230.94

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 230.67, 230.94

**Response Time:** 10.1s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** PASS

**Agent Answer:**
## Working Space Requirements (CEC 2022)

The installation **does not meet CEC requirements** for the following reasons:

1. **Front Clearance Violation**  
   - **Required**: 30 inches (762 mm) minimum depth for 120V systems (CEC Table 110.26(A)(1), Condition 1).  
   - **Provided**: Only 24 inches.  
   - **No applicable exception** applies to reduce this requirement for a closet installation.  

2. **Side Clearance Violation**  
   - **Requirement**: Working space must be **clear of obstructions** (CEC 110.26(A)(2)).  
   - **Provided**: Water heater is only 18 inches from the panel, intruding into the required working space.  
   - **Exceptions**:  
     - Exception 110.26(E) (dedicated space) does not apply here, as a closet is not a "dedicated electrical space" unless specifically designed for electrical equipment.  
     - No other exceptions permit obstructions within working space.  

3. **Closet Installation Limitations**  
   - CEC 110.26(E) requires electrical equipment to be in **dedicated spaces** with no foreign systems (e.g., water heaters) in the dedicated zone. A closet does not satisfy this unless explicitly designed for electrical use.  

### Corrective Actions:  
- Increase front clearance to **at least 30 inches**.  
- Relocate the water heater or install a barrier to ensure **no obstructions** within the working space.  
- If the panel must remain in a closet, redesign the space as a **dedicated electrical room** per CEC 110.26(E).  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 11.3s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Code Violation Check (CEC 2022) - Final Answer

**Answer:**  
Yes, this is a **code violation** under **CEC 2022 Section 408.41**.  

### Key Requirements:
1. **Section 408.41** requires each grounded conductor to terminate in an **individual terminal** within the panelboard.  
2. The **exception** allows multiple conductors on a single terminal **only if the terminal is explicitly marked** for this purpose (e.g., "2-wire" or "parallel conductor" marking).  

### Your Situation:
- The breaker terminal is **not marked** for two conductors.  
- Two 12 AWG conductors are landed on a single terminal without proper marking.  

### Required Correction:
- **Option 1:** Use a **breaker with a terminal marked** for two conductors (per the exception in 408.41).  
- **Option 2:** Terminate each conductor in a **separate terminal** on individual breakers.  

### Supporting CEC Sections:
- **CEC 2022 Section 408.41** (Grounded Conductor Terminations)  
- **CEC 2022 Section 110.3(B)** (Mechanical Execution of Electrical Connections - terminals must be used as designed).  

**Exceptions Checked:**  
- The exception in **408.41** explicitly requires terminal marking for multiple conductors.  
- Other exceptions (e.g., 404.2) relate to switch loops or fused switches and do **not apply** to breaker terminations.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 408.41, 110.3, 404.2

**Response Time:** 12.6s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** PASS

**Agent Answer:**
## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

### Configuration Requirements

1. **No Grounding Electrode at Subpanel**  
   - **CEC 250.32(B)(1)** explicitly prohibits a grounding electrode (e.g., ground rod) at the detached garage subpanel. Grounding is provided via the **feeder's equipment grounding conductor (EGC)**.

2. **Neutral and Ground Separation**  
   - In the subpanel, **neutral and ground bars must be isolated** (not bonded). This ensures the neutral returns current and the EGC handles fault currents.

3. **Feeder EGC Sizing**  
   - The EGC in the feeder must be sized per **CEC Table 250.122** based on the feeder's overcurrent protection rating. Example: For a 60A feeder, use **10 AWG copper**.

4. **Bonding at Main Panel Only**  
   - The **main service panel** bonds neutral and ground. The subpanel relies on the feeder's EGC for grounding continuity.

5. **Grounding Electrode at Main Panel**  
   - The main panel must have a **grounding electrode conductor (GEC)** connected to a grounding electrode (e.g., ground rods) per **CEC 250.50**.

---

### Exceptions and Key Notes

- **Exception 250.32(B)(1) Exception No. 1** allows the grounded conductor to serve as a ground-fault return path **only if**:
  - No equipment grounding conductor is present (not applicable here, as the feeder includes an EGC).
  - No continuous metallic paths exist between buildings.
  - Ground-fault protection is not installed.

- **CEC 250.24(B)** reinforces that subpanels must **not bond neutral and ground**—this is reserved for the main panel.

---

### Final Answer

For a detached garage subpanel fed by a 4-wire feeder:
- **Do not install a grounding electrode (e.g., ground rod)** at the subpanel.
- **Separate neutral and ground bars** in the subpanel.
- Size the **feeder's EGC** per **Table 250.122**.
- Ensure the **main panel** has a GEC connected to a grounding electrode.

**Source**: CEC 2022 Sections 250.32, 250.24, 250.122.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.122, 250.32, 250.50, 250.24

**Response Time:** 12.3s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** PASS

**Agent Answer:**
## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)  

### **Definitions**  
1. **Main Bonding Jumper** (CEC 100):  
   - Connects the **grounded circuit conductor (neutral)** to the **equipment grounding conductor** at the **service** (e.g., main panel).  
   - Ensures electrical continuity between grounding and neutral at the service point.  

2. **System Bonding Jumper** (CEC 100):  
   - Connects the **grounded circuit conductor** to the **supply-side bonding jumper** or **equipment grounding conductor** at a **separately derived system** (e.g., transformers, generators).  
   - Bonds the derived system’s grounded conductor to the equipment grounding network.  

---

### **Key Differences**  
| Feature                  | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |  
|--------------------------|--------------------------------------------------|--------------------------------------------------|  
| **Location**             | At the **service** (main electrical panel)       | At **separately derived systems** (transformers, generators) |  
| **Purpose**              | Bonds neutral to equipment grounding at the service | Bonds neutral to equipment grounding at derived systems |  
| **Applicable Systems**   | **Service entrances**                            | **Separately derived systems** (NEC/CEC Article 250) |  

---

### **When Required**  
1. **Main Bonding Jumper** (CEC 250.28):  
   - **Mandatory at every service** (main panel).  
   - Required to ensure the grounded (neutral) conductor and equipment grounding conductor are bonded at the service point.  

2. **System Bonding Jumper** (CEC 250.28):  
   - **Mandatory at separately derived systems** (e.g., transformer secondary, solar PV systems).  
   - Required to bond the derived system’s grounded conductor to the equipment grounding system.  

---

### **Sizing Requirements**  
Both jumpers must be sized per **Table 250.102(C)(1)** based ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 250.30, 250.102, 250.28

**Response Time:** 12.7s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** PASS

**Agent Answer:**
## Small Appliance Branch Circuits for Kitchen and Dining Room (CEC 2022)  

### **Required Number of Circuits**  
- **Minimum Requirement**: **2** 20-ampere small-appliance branch circuits are required for the kitchen (CEC 210.52(B)(1)).  
- **Purpose**: These circuits serve all kitchen receptacles (wall, countertop, and refrigeration equipment).  

### **Serving Dining Room Receptacles**  
- **Permitted**: Yes, the kitchen small-appliance branch circuits **can also serve dining room receptacles**.  
- **Code Basis**: CEC 210.52(B)(1) explicitly allows these circuits to supply receptacles in "other rooms specified in 210.52(B)(1)", which includes dining rooms.  

### **Exceptions and Limitations**  
- **No Other Outlets**: The small-appliance circuits **must not serve any other outlets** (e.g., laundry, bathroom) unless exceptions apply (e.g., Exception No. 1 for switched receptacles).  
- **Single Kitchen Limit**: A single small-appliance circuit **cannot serve more than one kitchen** (CEC 210.52(B)(1)).  

### **Key Code References**  
1. **CEC 210.52(B)(1)**: Requires two 20A circuits for kitchen receptacles and permits them to serve dining room outlets.  
2. **CEC 210.11(C)(1)**: Mandates at least two small-appliance branch circuits for dwelling units.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.11

**Response Time:** 9.5s

---

### core-010: load_calculations

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Expected:** Base ampacity: 30A at 90°C (Table 310.16). Temperature correction factor: 0.82 for 50°C (Table 310.15(B)(1)). Bundling adjustment: 0.80 for 6 conductors (Table 310.15(C)(1)). Adjusted ampacity = 30A × 0.82 × 0.80 = 19.68A, approximately 20A.

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Final Answer: Adjusted Ampacity for 12 AWG THHN Conductors (CEC 2022)

**Final Derated Ampacity**: **19.68 amperes**  
**Overcurrent Protection Required**: **20A** (per CEC 240.4(D)(5))

---

### **Step-by-Step Calculation**:
1. **Base Ampacity**:  
   - 12 AWG THHN copper = **30A** (CEC Table 310.16, 90°C column).

2. **Temperature Correction**:  
   - Ambient temperature = 50°C  
   - Correction factor = **0.82** (CEC Table 310.15(B)(1)(1)).

3. **Bundling Adjustment**:  
   - 6 current-carrying conductors in a raceway  
   - Adjustment factor = **0.80** (CEC Table 310.15(C)(1)).

4. **Derated Ampacity**:  
   $$
   30A \times 0.82 \times 0.80 = 19.68A
   $$

---

### **Overcurrent Protection (OCPD)**:
- **CEC 240.4(D)(5)** explicitly limits overcurrent protection for **12 AWG copper** to **20A**, regardless of derating.  
- Even though the derated ampacity is slightly below 20A, the OCPD must not exceed the standard 20A rating (no exceptions apply for this scenario).

---

### **Code References**:
- **CEC Table 310.16**: Base ampacity (THHN, 90°C).  
- **CEC Table 310.15(B)(1)(1)**: Temperature correction (50°C ambient).  
- **CEC Table 310.15(C)(1)**: Bundling adjustment (6 conductors).  
- **CEC 240.4(D)(5)**: Overcurrent protection for 12 AWG copper.  

---

### **Exception Check**:
- No exceptions to **240.4(D)(5)** apply for 12 AWG copper in this configuration.  
- Cross-referenced exceptions (e.g., 368.17, 230.90) pertain to busways, services, or equipment not relevant here.  

---

**✓ Source**: CEC 2022 Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1), and Section 240.4(D)(5).

**Tool Usage:**
- CEC Tools: cec_derated_ampacity, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 310.16, 310.15, 368.17, 240.4, 230.90

**Response Time:** 14.1s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## Why CEC Requires AFCI Protection in Bedrooms and Living Areas (CEC 2022)

### **Requirement**
The California Electrical Code (CEC) mandates **Arc-Fault Circuit Interrupter (AFCI)** protection for all 120-volt, single-phase, 15- and 20-ampere branch circuits in dwelling units supplying outlets in:
- Bedrooms
- Living rooms
- Hallways
- Closets
- Bathrooms (in some configurations)
- Similar areas (CEC 210.12(A))

### **Electrical Hazard Prevented**
AFCI protection prevents **electrical fires caused by arc faults**, which can occur due to damaged wiring, loose connections, or deteriorated insulation. Arc faults generate high heat, potentially igniting surrounding materials.

---

### **Exceptions to AFCI Requirements**
1. **Fire Alarm Systems**  
   - AFCI protection is **not required** for branch circuits supplying fire alarm systems installed in accordance with **760.41(B)** or **760.121(B)**, provided the circuit is installed in **metal raceway, metal auxiliary gutter, steel-armored cable, Type MC, or Type AC cable** meeting 250.118 requirements.

2. **Short Circuit Extensions**  
   - AFCI protection is **not required** for branch circuit extensions **≤ 1.8 m (6 ft)** that do not add outlets or devices (excluding splicing devices). This applies to modifications in areas covered by 210.12(A), (B), or (C).

3. **Replacement Receptacles**  
   - Replacements in AFCI-protected areas may use **listed outlet branch-circuit-type AFCI receptacles** or be protected by a **combination-type AFCI circuit breaker** (CEC 406.4(D)(4)).

---

### **Key Code References**
- **Primary Rule**: CEC 210.12(A)  
- **Exceptions**: CEC 210.12(A) Exception, 406.4(D)(4)  
- **Fire Alarm Exception**: CEC 210.12(A) Exception referencing 760.41(B)/760.121(B)  

---

### **Summary**
AFCI protection is required in bedrooms and living areas to mitigate fire risks from arc faults. Exceptions apply for fire alarm systems (with specific wiring methods) and short circuit extensions. Always verify l...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 5 found
- 250.118, 210.12, 760.41, 406.4, 760.121

**Response Time:** 14.3s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Torque Specifications for Conductor Terminations (CEC 2022)  

Torque specifications ensure **secure, low-resistance connections** in electrical panels, preventing overheating, arcing, and equipment failure. The requirements are outlined in **CEC 2022 Section 110.14(D)**, with no exceptions modifying this rule for torque applications.  

### Key Requirements from **110.14(D)**:  
1. **Manufacturer Specifications**:  
   - Torque values must be specified by the equipment manufacturer or installation instructions.  
   - Use **approved methods** (e.g., torque tools, shear bolts) to achieve the indicated torque.  

2. **Control Circuit Devices**:  
   - For **14 AWG or smaller copper conductors**, screw-type terminals must be torqued to a **minimum of 0.8 N·m (7 lb-in.)** unless otherwise identified (per **Section 430.9(C)**).  

3. **Informational Guidance**:  
   - If torque values are not marked, contact the manufacturer (per *Informational Note 2*).  
   - Refer to **UL 486A-486B** or **NFPA 70B** for additional torque guidance.  

### Exceptions Check:  
- **No exceptions** to **110.14(D)** directly modify torque requirements.  
- Cross-referenced sections (e.g., 300.15, 250.148) address unrelated topics (boxes, grounding).  

### Consequences of Non-Compliance:  
- **Loose connections**: Overheating, arcing, fire hazards.  
- **Over-tightening**: Damaged terminals or conductors.  

✓ Source: CEC 2022 Sections 110.14(D), 430.9(C)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.148, 430.9, 110.14, 300.15

**Response Time:** 9.8s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Final Service Load Calculation with Exceptions Checked (CEC 2022)

### **Exceptions Review**
1. **CEC 220.55 (Range Demand Factor):**  
   - **Exception 210.21(B)(4)** confirms the range receptacle rating can use the demand factor from Table 220.55.  
   - **No conflicting exceptions** override the 8 kW + 50% remaining kW calculation.  

2. **CEC 220.54 (Dryer Demand Factor):**  
   - No exceptions apply to the 5 kW + 50% calculation for dryers.  

3. **Other Exceptions:**  
   - **220.53** (appliances) and **220.56** (commercial equipment) do not apply to this residential load calculation.  

### **Final Calculation Summary**
- **Total Service Load:** 26,525 VA  
- **Current:** 26,525 VA ÷ 240 V ≈ **110.5 A**  

### **Conclusion**
- **200A Panel Adequacy:**  
  - The calculated load (**110.5 A**) is **well below** the 200A panel rating.  
  - **✓ Panel is adequately sized** per CEC 2022 Article 220, with no exceptions overriding the demand factors.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 220.55, 220.56, 220.54, 210.21, 220.53, 110.5

**Response Time:** 13.0s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## Electrical Panel Inspection Violations (CEC 2022)  

1. **Depth Clearance Violation**  
   - **Requirement**: Minimum depth of **30 inches** per **Table 110.26(A)(1)** (Condition 1 for residential panels).  
   - **Issue**: Panel has **28 inches** of depth clearance.  
   - **Citation**: CEC 2022 **110.26(A)(1)**.  
   - **Exception Check**: No applicable exception for reduced depth in residential garages. Exception No. 2 (existing dwellings ≤ 200A) **does not apply** to panels in **garages** (not main service locations).  

2. **Obstruction in Working Space**  
   - **Requirement**: Working space must be **clear of obstructions** (CEC 2022 **110.26(A)(3)**).  
   - **Issue**: Water heater located **16 inches** from the panel.  
   - **Citation**: CEC 2022 **110.26(A)(3)**.  

3. **Vertical Clearance Violation**  
   - **Requirement**: Working space must extend from floor to **6.5 ft (78 in.)** height (CEC 2022 **110.26(A)(2)**).  
   - **Issue**: Panel mounted at **5 ft (60 in.)**, leaving **60 in.** vertical clearance.  
   - **Exception Check**: Exception No. 2 (existing dwellings ≤ 200A) **does not apply** to **garage panels**.  

4. **Additional Violation**  
   - **Requirement**: Panel must allow **unobstructed access to all parts** (CEC 2022 **110.34(A)**).  
   - **Issue**: Mounting height may restrict access to upper panel components.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 110.34, 110.26

**Response Time:** 18.5s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## Corrected Circuit Protection Requirements for New Residential Kitchen (NEC 2023 with CEC Exceptions Considered)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **Combination AFCI/GFCI Breaker**
- **NEC References**:
  - **210.8(A)(5)**: GFCI required for all kitchen countertop receptacles.
  - **210.12(A)**: AFCI required for all dwelling unit branch circuits.
- **CEC Exceptions**: No applicable exceptions found for countertop circuits.

### 2. **Dishwasher (Dedicated 15A Circuit)**
- **Protection Required**: **GFCI Breaker**
- **NEC References**:
  - **210.8(A)(5)**: GFCI required for all kitchen receptacles.
  - **210.12(A)**: AFCI required for all dwelling unit branch circuits.
- **CEC Exceptions**: No exception applies to dishwashers (not listed in 210.8 exceptions).

### 3. **Garbage Disposal (Dedicated 15A Circuit)**
- **Protection Required**: **GFCI Breaker**
- **NEC References**:
  - **210.8(A)(5)**: GFCI required for all kitchen receptacles.
  - **210.12(A)**: AFCI required for all dwelling unit branch circuits.
- **CEC Exceptions**: No exception applies to garbage disposals.

### 4. **Refrigerator (Dedicated 20A Circuit)**
- **Protection Required**: **AFCI Breaker Only**
- **NEC References**:
  - **210.12(A)**: AFCI required for all dwelling unit branch circuits.
  - **210.8(A) Exception No. 2**: Permits specific appliances (e.g., refrigerator) on individual circuits without GFCI if not readily accessible.
- **CEC Exceptions**: Confirmed no additional restrictions in CEC 2022 exceptions.

---

### Final Notes:
- **GFCI is mandatory** for all kitchen receptacles **except** where explicitly exempted (e.g., refrigerator).
- **AFCI is mandatory** for all circuits in dwelling units.
- **Refrigerator** is the only appliance here exempt from GFCI due to **NEC 210.8(A) Exception No. 2** (fixed appliance on dedicated circuit).

✓ Source: NEC 2023 & CEC 2022

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 210.8, 210.12

**Response Time:** 17.6s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## Subpanel Bonding Violations in Detached Garage (CEC 2022) – Final Answer

### **Identified Violations**
1. **Neutral and Ground Bars Bonded Together**  
   - **Violation**: CEC 250.24(D) requires **neutral and ground to be separated** in subpanels.  
   - **Exceptions Checked**:  
     - **250.25** applies to supply-side systems (not load-side subpanels).  
     - **250.142** exceptions permit grounded conductor use only on the **supply side**.  
   - **Conclusion**: No applicable exceptions. Bonding neutral and ground bars violates code.

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: CEC 250.142(A) prohibits **neutral-to-enclosure bonding** in subpanels.  
   - **Exceptions Checked**:  
     - **250.142(A)(2)** allows neutral-to-enclosure bonding **only on the supply side** (main panel).  
   - **Conclusion**: No exceptions apply. Bonding neutral bar to enclosure violates code.

3. **Missing Grounding Electrode Conductor**  
   - **Violation**: CEC 250.32(B) mandates a **local grounding electrode** for detached structures.  
   - **Exceptions Checked**:  
     - **250.54** permits auxiliary electrodes but **does not exempt** the primary grounding electrode requirement.  
   - **Conclusion**: No exceptions apply. A grounding electrode conductor is required.

---

### **Correct Configuration**
1. **Feeder Connections**  
   - **Feeder Neutral**: Connect to **neutral bar** (no bonding to enclosure or ground bar).  
   - **Feeder Ground**: Connect to **ground bar** (bonded to enclosure).  

2. **Bonding**  
   - **Ground Bar**: Bond to metal enclosure using a **listed bonding jumper**.  
   - **Neutral Bar**: **Isolated** from enclosure and ground bar.  

3. **Grounding Electrode**  
   - Install a **separate grounding electrode conductor** (e.g., #6 copper) from the subpanel’s ground bar to a **local ground rod** (8 ft long, 8 in. below grade).  

4. **Main Bonding Jumper**  
   - **Removed**: Only present in the **main service panel**.  

---
...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 250.142, 250.32, 250.24, 250.54, 250.25, 250.66

**Response Time:** 13.2s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**
## Final Verification with Exceptions (CEC 2022)

**Exception Check for CEC 402.7:**  
- **No applicable exceptions** found for RMC conduit fill calculations.  
- The only exceptions relate to:  
  - **Strut-type channel raceways** (384.22) – Not applicable here  
  - **Elevator installations** (620.33) – Not applicable here  

**Conclusion:**  
The 40% fill rule in **CEC 402.7** applies without exception for rigid metal conduit (RMC). No California amendments or exceptions modify the calculation for 10 AWG THHN conductors in 1¼" RMC.  

**Final Answer:**  
A 1¼-inch RMC conduit can accommodate **28** 10 AWG THHN conductors at 40% fill.  

✓ Source: CEC 2022 Chapter 9 Tables 4 and 5  
✓ No exceptions apply (verified via cec_exception_search)

**Tool Usage:**
- CEC Tools: cec_lookup_conduit_fill, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 384.22, 402.7, 620.33

**Response Time:** 20.9s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**
## Voltage Drop Calculation (CEC 2022)  

**Voltage drop**:  
2.84 volts (2.365% of 120V supply)  

**Calculation steps**:  
1. **Formula**:  
   $$
   VD = \frac{2 \times I \times R \times L}{1000} = \frac{2 \times 22 \times 1.29 \times 50}{1000} = 2.838\ \text{V}
   $$  
2. **Percentage**:  
   $$
   \frac{2.838}{120} \times 100 = 2.365\%
   $$  

**CEC Verification**:  
- **CEC 647.4(D)**:  
  - **Fixed Equipment**: Voltage drop on branch circuits must not exceed **1.5%** (2.365% exceeds this).  
  - **Combined Feeder + Branch**: Must not exceed **2.5%** (this applies only if feeder drop is included).  

**Exceptions Checked**:  
- No exceptions in **CEC 647.4(D)** relax the 1.5% limit for fixed equipment.  
- **Informational Note**: Refers to portable cords (not applicable here).  

**Conclusion**:  
✗ **Fails CEC 647.4(D)** (2.365% > 1.5% for fixed equipment).  
✓ **Meets NEC 210.19 informational note** (≤3% recommended).  

**Recommendation**: Use **10 AWG conductors** (lower resistance) to reduce voltage drop to ≤1.5%.  

✓ Source: CEC 2022, 647.4(D)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 210.19, 647.4

**Response Time:** 25.0s

---

### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Final Adjusted Ampacity with Exception Check (CEC 2022)

### 1. **Base Ampacity (Table 310.16)**  
- **12 AWG TW copper** at 60°C rating: **20A**

### 2. **Temperature Correction (Table 310.15(B)(1))**  
- **Ambient temperature**: 43°C  
- **Correction factor**: **0.71** (for 60°C insulation at 43°C)

### 3. **Bundling Adjustment (Table 310.15(C)(1))**  
- **6 current-carrying conductors**:  
- **Adjustment factor**: **0.8** (for 4–6 conductors)

### 4. **Final Calculation**  
```
Adjusted Ampacity = 20A × 0.71 × 0.8 = **11.36A**
```

### 5. **Exception Review**  
- **No applicable exceptions** found for 310.15 in this scenario.  
- **Key exception notes**:  
  - Type XHHW-2 is exempt from rooftop temperature adjustments (not applicable here).  
  - Adjustment factors do not apply for short raceways (<600mm) or protected underground conductors (not applicable here).  

### 6. **Limiting Rule Check (240.4(D))**  
- **12 AWG copper** is limited to **20A overcurrent protection**.  
- Final ampacity (11.36A) is below this limit, so OCP device remains valid.

### 7. **Code Compliance**  
- Temperature correction and bundling adjustment applied per **310.15(B)(1)** and **310.15(C)(1)**.  
- No exceptions override the calculation for this configuration.

**Final Answer**: **11.36A**  
(Tables: 310.16, 310.15(B)(1), 310.15(C)(1), 240.4(D))  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_derated_ampacity, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 240.4, 310.16, 310.15

**Response Time:** 44.5s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Minimum Size Copper GEC for 1000 kcmil Service Conductors (CEC 2022)

For a service with **1000 kcmil equivalent copper service conductors**, the minimum size **copper grounding electrode conductor (GEC)** required is:

**2/0 AWG copper**  
(Per CEC 2022 Table 250.66, column for copper GEC)

### Key Details:
- **Service conductor equivalent**: 1000 kcmil (4 × 250 kcmil parallel conductors)
- **GEC size range**: Over 600 through 1100 kcmil service conductors
- **California amendment**: Table includes California-specific adjustments [CEC]

### Exception Review:
- **CEC 250.30(A)(5)**: Applies to separately derived systems, which is not relevant here.
- **CEC 250.190(B)**: Confirms GEC sizing per Table 250.66 based on largest ungrounded conductor.
- **No applicable exceptions override Table 250.66 for this scenario**.

✓ Source: CEC 2022 Table 250.66

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 250.190, 250.30, 250.66

**Response Time:** 8.7s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 28/28
- **Success Rate**: 100.0%
- **Average Response Time**: 14.2s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

