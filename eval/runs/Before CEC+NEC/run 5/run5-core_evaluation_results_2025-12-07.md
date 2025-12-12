# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-07
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 28 |
| **Successful** | 28 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 383.8s |
| **Avg per Question** | 13.7s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer: Ampacity of 12 AWG Copper at 75°C (CEC 2022)

**Base Ampacity:**  
12 AWG copper at 75°C = **25 amperes** per CEC 2022 Table 310.16.  

**Critical Exceptions/Overrides:**  
- **Overcurrent Protection Limitation:**  
  Section 240.4(D) restricts overcurrent protection for 12 AWG copper to **20A**, even though the ampacity is 25A. This applies to branch circuits with small conductors.  

**California-Specific Notes:**  
- The [CEC] amendment in Table 310.16 explicitly references Section 240.4(D) for overcurrent protection limitations.  

---
## NEC 2023 Reference  
No difference from NEC 2023. Same ampacity (25A) and overcurrent protection limit (20A) apply per NEC 310.16 and 240.4(D).  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.16, 240.4

**Response Time:** 12.2s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
The minimum copper conductor size required for a 60A circuit at 75°C is **6 AWG**.  

- **Ampacity**: 65A (per **CEC 2022 Table 310.16**)  
- **Verification**: 6 AWG copper provides 65A ampacity at 75°C, meeting the 60A requirement.  
- **Exception Analysis**:  
  - **Section 210.19** (branch circuit requirements) does not override Table 310.16 for this scenario. The exception allowing 100% rated equipment terminations does not apply here.  
  - **Section 310.12** (dwelling service conductors) is inapplicable, as this is a branch circuit, not a service/feeder.  
- **Conclusion**: No exceptions modify the Table 310.16 requirement for this 60A circuit.  

---

## NEC 2023 Reference  
No difference from NEC 2023. The same 6 AWG copper conductor size is required for a 60A circuit at 75°C.  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.16, 310.12, 210.19

**Response Time:** 15.1s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Kitchens (CEc 2022)  

**California Requirement (CEc 2022):**  
Per **ceC 2022 Section 210.8(A)(6)**, **all 125-volt through 250-volt receptacles installed in kitchens to serve countertop surfaces** must have **ground-fault circuit-interrupter (GFCI) protection for personnel**. This includes:  

- **Countertop receptacles** (per 210.52(C)):  
  - At least one receptacle per **0.84 m² (9 ft²)** of countertop or work surface.  
  - Additional receptacles for every **1.7 m² (18 ft²)** of countertop.  
  - Receptacles must be located **within 600 mm (24 in.)** of the outer end of peninsular countertops.  

**Key Details:**  
- GFCI protection applies to **all countertop receptacles**, regardless of their location (wall-mounted, under-counter, or in countertops).  
- **No exceptions** were found in the cec_exception_search results that would exempt kitchen countertop receptacles from GFCI requirements.  

**NEC 2023 Reference:**  
No difference from NEC 2023. The National Electrical Code also requires GFCI protection for kitchen countertop receptacles per **NEC 2023 Section 210.8(A)(6)**.  

✓ **Sources: cec 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.8, 210.52

**Response Time:** 10.8s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
**Yes**, AFCI protection is **required for bedroom circuits** in new residential construction per **CEC 2022 Section 210.12(A)**. This requirement applies to all 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets in bedrooms, along with other specified rooms like kitchens, living rooms, and laundry areas.

**Key Details:**
- **Required Protection Methods**: 
  - Combination-type AFCI at the circuit origin (most common method).
  - Alternative methods include branch/feeder-type AFCI combined with outlet-type AFCI (less common).
- **Exceptions**: 
  - Not required for fire alarm systems installed per 760.41(B) or 760.121(B).
  - Minor extensions (≤6 ft) without additional outlets

**Exception Analysis**:
- Searched for exceptions to **Section 210.12** using `cec_exception_search`. The returned exceptions (210.70, 210.11, 210.22, 210.60) relate to lighting outlets, branch circuit requirements, load calculations, and guest room receptacles—**none modify or exempt AFCI requirements for bedroom circuits**.
- No exceptions apply to override the AFCI mandate for bedrooms in Section 210.12(A).

**Code Citation**: CEC 2022 Section 210.12(A) explicitly includes bedrooms in the list of required AFCI-protected locations.

---
## NEC 2023 Reference
No difference from NEC 2023. The national code also requires AFCI protection for bedroom circuits under NEC 2023 Section 210.12(A). California's CEC 2022 aligns with this requirement without additional amendments.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 210.70, 210.12, 760.121, 210.11, 760.41, 210.60, 210.22

**Response Time:** 9.9s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** PASS

**Agent Answer:**
## Final Answer (CEC 2022)

**Can aluminum conductors be used for a 200A service?**  
Yes, per CEC 2022 Section 310.3(B) and Table 310.12(A).

**Required conductor size:**  
**4/0 AWG aluminum** at 75°C (per CEC Table 310.12(A) for single-phase dwelling services).

**Key Requirements:**
1. Minimum size for service conductors: 6 AWG aluminum (CEC 230.31(B)), but 4/0 AWG is required for 200A (Table 310.12(A)).
2. Temperature rating: 75°C (standard for service conductors).
3. No temperature correction/bundling adjustments needed if the installation meets Table 310.12(A) conditions.

**Exception Check:**  
No exceptions apply for standard 200A dwelling service conductors. The exceptions in 310.12(A) relate to installation conditions (e.g., wet locations, parallel conductors) and do not affect conductor sizing for a standard 200A service.

---
## NEC 2023 Reference  
No difference from NEC 2023. Same requirements apply per NEC Table 310.12(A).

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_size, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 230.31, 310.3, 310.12

**Response Time:** 10.4s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Clearance Depth (CEC 2022)  

**Requirement:**  
For a 120/240V residential panel under **Condition 2** (exposed live parts on one side and grounded parts on the other, e.g., concrete wall), the minimum working space depth is **914 mm (30 inches)** per **CEC 2022 Table 110.26(A)(1)**.  

**Exceptions Checked:**  
- **Exception No. 2** allows reduced height (not depth) for existing dwelling units with ≤ 200A service equipment.  
- No exceptions override the 30-inch depth requirement for Condition 2.  

**NEC 2023 Reference:**  
No difference from NEC 2023. The same 914 mm (30 in.) depth applies for Condition 2 working space under NEC 2023 Table 110.26(A)(1).  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 10.3s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
Per CEC 2022 Section 210.11(C)(1), **two or more 20-ampere small-appliance branch circuits** are required for all receptacle outlets in kitchens, pantries, breakfast rooms, and dining rooms. This alignss with NEC 2023 Section 210.11(C)(1), which mandates the same requirement.

**Key Exceptions Considered:**
1. **Exception No. 2 in 210.52(B)(1):** Permits a receptacle for a specific appliance (e.g., refrigerator) to be supplied by an individual branch circuit rated ≥15A. This does not reduce the requirement for two small-appliance circuits.
2. **Section 220.52 Exception:** Allows exclusion of a circuit for a specific appliance on an individual branch circuit, but the two-circuit minimum remains.

The CEC maintains the two-circuit requirement without modification from NEC, ensuring adequate capacity for countertop appliances and general kitchen use.

---
## NEC 2023 Reference
No difference from NEC 2023. Both codes require two 20-ampere small-appliance branch circuits for kitchens.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 220.52, 210.11, 210.52

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
Yes, surge protection is required for a new 200A residential service per **CEC 2022 Section 230.67(A)**, aligning with NEC 2023. However, California allows flexibility in SPD installation location via an exception.

---

### Key Details from CEC 2022:
- **Section 230.67(A):**  
  All services supplying dwelling units **must** have a surge-protective device (SPD).

- **Exception to Location Requirement (Section 230.67(B)):**  
  The SPD **does not need to be in the service equipment** if installed at the **next level of distribution equipment downstream** toward the load. This allows installation in a distribution panel rather than the main service panel.

- **Type Requirement (Section 230.67(C)):**  
  SPDs must be **Type 1 or Type 2** devices.

---

### Additional CEC Exceptions:
- **Section 230.94:**  
  Permits SPDs (Type 1) to be installed on the **supply side of the service disconnecting means** under specific conditions (e.g., metering, fire alarm circuits).

---

### Summary:
- **Requirement:** SPDs are mandatory for residential services (CEC 2022 §230.67).  
- **Flexibility:** SPDs can be installed downstream of the service equipment (Exception to §230.67(B)).  
- **No Direct Exceptions:** No exemptions for residential services based on service size (200A) or location type.

This aligns with NEC 2023 but emphasizes California's specific wording and exceptions.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 230.67, 230.94

**Response Time:** 10.3s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** PASS

**Agent Answer:**
## Final Answer: California Electrical Code (CEC 2022) Requirements

**Service Conductor Sizing for 200A Dwelling Service:**

**Required Conductor Size:**  
**4/0 AWG aluminum** (per CEC 2022 Table 310.12(A))  

**Key Code Requirements:**  
1. **Table 310.12(A) Application:**  
   - For a 200A service, conductors must have an ampacity of at least **166A** (200A × 83%).  
   - 4/0 AWG aluminum at 75°C terminals provides **180A ampacity** (Table 310.12(A)), meeting the requirement.  

2. **Aluminum Conductor Allowability:**  
   - **Permitted** under CEC 310.3(B) for service conductors.  
   - Requires **75°C-rated terminations** (110.14(C)) and compliance with 310.106(B) for aluminum installation (e.g., listed connectors, proper torque).  

3. **No Derating Required:**  
   - Table 310.12(A) assumes standard conditions (30°C ambient, no bundling).  
   - If elevated temperatures or multiple conductors apply, use **310.15(B)(1)** (temperature correction) and **310.15(C)(1)** (bundling adjustment).  

**Exceptions Checked:**  
- No exceptions override Table 310.12(A) for standard dwelling services.  

---

## NEC 2023 Reference  
No difference from NEC 2023. Same conductor sizing applies per Table 310.12(A).  

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 310.106, 110.14, 310.15, 310.3, 310.12

**Response Time:** 18.2s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** PASS

**Agent Answer:**
## Adjusted Answer with CEC Exceptions Considered

**1. Circuit Breaker Requirements (CEC 2022 Section 210.4):**  
- **Simultaneous Disconnection (210.4(B)):**  
  All ungrounded conductors must be disconnected simultaneously using:  
  - A **2-pole circuit breaker** or  
  - **Single-pole breakers with an approved handle tie**.  
  *Exception: None applicable for kitchen receptacles.*  

- **Breaker Rating:**  
  For 12 AWG copper (12/3 cable), overcurrent protection must not exceed **20A** (per CEC 240.4(D)).  

**2. Neutral Termination Requirements (CEC 2022 Section 200.4(B)):**  
- **Grouping:**  
  The grounded (neutral) conductor must be **grouped with its associated ungrounded conductors** in the panel.  
  *Exception 2 to 200.4(B):* If the 12/3 cable enters the panel via a raceway or cable that clearly identifies the grouping, marking is not required.  

- **Load Restrictions (210.4(C)):**  
  The circuit must supply **only line-to-neutral loads** (e.g., receptacles).  
  *Exception 2:* Line-to-line loads are allowed if all ungrounded conductors are disconnected simultaneously (satisfied by the 2-pole breaker).  

**3. Additional CEC Requirements:**  
- **Kitchen-Specific Rules:**  
  - GFCI protection is required for kitchen receptacles (CEC 210.8(A)(6)), but this is separate from MWBC requirements.  
  - Harmonic currents on neutrals are a concern for nonlinear loads (Informational Note 1 in 210.4).  

**4. Code Citations:**  
- CEC 210.4(B) for simultaneous disconnection.  
- CEC 200.4(B) for neutral grouping.  
- CEC 240.4(D) for 12 AWG conductor overcurrent limits.  

---
## NEC 2023 Reference  
No significant differences from CEC 2022. NEC 210.4 and 200.4(B) have identical requirements for multiwire branch circuits and neutral grouping.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 4 found
- 200.4, 210.8, 240.4, 210.4

**Response Time:** 13.1s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Dwellings (CEC 2022)  
**Per CEC 2022 Section 210.8, GFCI protection is required for all 120–250V receptacles in the following locations in dwelling units:**  

1. **Bathrooms**  
2. **Garages and accessory buildings** with floors at or below grade level (non-habitable, storage/work areas).  
3. **Outdoors** (all exterior receptacles).  
4. **Crawl spaces** at or below grade level.  
5. **Basements** (unfinished areas).  
6. **Kitchens** (countertop surfaces and areas with sinks).  
7. **Sinks** where receptacles are within **6 ft (1.8 m)** of the bowl’s top inside edge.  
8. **Boathouses**.  
9. **Bathtubs or shower stalls** where receptacles are within **6 ft (1.8 m)** of the outside edge.  
10. **Laundry areas**.  
11. **Indoor damp/wet locations** (e.g., near pools, hot tubs).  

---

### **Exceptions (CEC 2022 Section 210.8)**  
1. **Non-readily accessible receptacles** on dedicated circuits for:  
   - Electric snow-melting/deicing systems (per 426.28/427.22).  
   - Pipeline or vessel heating equipment.  
2. **Fire alarm/burglar alarm systems** in basements (no GFCI required).  
3. **Ceiling luminaires/fans** with listed locking support receptacles (no GFCI required if not general-purpose).  
4. **Industrial labs** or healthcare facilities** (specific exceptions apply for equipment safety).  

---

### **NEC 2023 Comparison**  
The CEC 2022 aligns with NEC 2023 for GFCI requirements in residential locations. California does not add additional exceptions beyond the NEC in this section.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 427.22, 210.8, 426.28

**Response Time:** 21.0s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirement for 200A Residential Service (CEC 2022)

**California Requirement:**
Per **CEC 2022 Section 230.67**:
1. **Mandatory Requirement**: Surge-protective devices (SPDs) are **required** for all services supplying dwelling units.
2. **Installation Locations**:
   - **Primary Location**: Must be an **integral part of the service equipment** (main panel).
   - **Alternative Location**: May be installed **immediately adjacent** to the service equipment.
   - **Exception**: SPDs may be located at the **next level distribution equipment downstream** (e.g., a subpanel in a detached garage) instead of the service equipment itself.
3. **SPD Type**: Must be **Type 1** (for overhead services) or **Type 2** (for underground services).
4. **Replacement Rule**: If service equipment is replaced, SPD installation requirements apply.

**Key Exceptions**:
- **Section 230.67(B) Exception**: Permits SPD installation at downstream distribution equipment instead of the service equipment.
- **Section 230.94**: Allows SPDs to be connected on the supply side of the service disconnecting means (as permitted by 230.82).

**Example Compliance**:
- A 200A residential service panel must include a listed Type 1 or Type 2 SPD either:
  - Directly in the main service panel, or
  - In a subpanel downstream (e.g., a detached garage panel).

---

## NEC 2023 Reference
**No equivalent requirement** exists in NEC 2023. Surge protection is **not mandated** by the national code for residential services, making this a **California-specific amendment** [CEC].

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 230.67, 230.82, 230.94

**Response Time:** 10.2s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** PASS

**Agent Answer:**
## California Electrical Code (CEC 2022) Exceptions Analysis

**Relevant Exceptions Checked:**
1. **Exception No. 2 (110.26(A))**: Allows reduced height (not depth/width) for existing dwelling units with ≤200A panels
2. **Exception No. 3 (110.26(A))**: Permits meters in sockets (not applicable here)
3. **Low-voltage exception (110.26(A)(1)(b))**: Only applies to ≤30V systems (not applicable)
4. **Existing building exception (110.26(A)(1)(c))**: Requires written procedures for equipment on both sides of an aisle (not applicable in a closet)

**Key Findings:**
- No exceptions in CEC 2022 reduce required **front depth** or **side width** for panels in closets
- Exception No. 2 only modifies **height** requirements for existing installations
- Storage in working space (water heater) is explicitly prohibited by 110.26(B)

---

## Final Determination (CEC 2022)

**This installation does NOT meet California Electrical Code requirements** due to:

1. **Front Clearance Depth**  
   - Required: 36 inches (Condition 2 for 240V systems)  
   - Installed: 24 inches (insufficient)

2. **Side Clearance Width**  
   - Required: 30 inches (minimum width per 110.26(A)(2))  
   - Installed: 18 inches (insufficient)

3. **Storage Prohibition**  
   - Water heater placement violates 110.26(B) (no storage in working space)

**NEC 2023 Comparison:**  
Same requirements apply per NEC 2023. No California amendments affect these working space dimensions.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 12.4s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Code Violation Analysis (CEC 2022)

**California Requirement:**
This is a **code violation** under CEC 2022 Section 408.41. The key requirements are:

1. **408.41 Grounded Conductor Terminations**  
   - *Each conductor must terminate in an individual terminal not shared with another conductor.*  
   - **Exception**: Only permitted for *parallel conductors* if the terminal is explicitly marked for multiple conductors.

2. **Terminal Marking Requirement**  
   - The breaker terminal in question is **not marked** for two conductors. The exception (for parallel conductors) does not apply here, as the scenario involves a standard 20A circuit, not parallel conductors.

3. **Relevant Exceptions**  
   - No applicable exceptions exist for this configuration. The exception in 408.41 only permits multiple conductors on terminals **specifically identified** for this purpose.

---

## NEC 2023 Reference  
NEC 2023 Article 408.41 contains identical language to CEC 2022. The national code also prohibits multiple conductors on a terminal unless explicitly marked. **No difference from NEC 2023.**

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 408.41

**Response Time:** 7.1s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
In a detached garage with a 4-wire feeder from the house panel, the grounding and bonding configuration must comply with **CEC 2022 Sections 250.32 and 250.64**, with the following key requirements:  

1. **Grounding Electrode Requirement**  
   - **CEC 250.32(A)** mandates a local grounding electrode (e.g., ground rod) at the detached garage. This is **non-negotiable** for feeders (unlike single branch circuits, which have exceptions).  

2. **Equipment Grounding Conductor (EGC)**  
   - The feeder must include an EGC sized per **Table 250.122** (based on the overcurrent device rating). This conductor connects to the subpanel’s grounding bar and the local grounding electrode.  

3. **Neutral-Ground Separation**  
   - In the subpanel, **neutral and ground bars must be isolated** (not bonded). The neutral conductor from the feeder connects only to the neutral bar. This prevents the neutral from acting as a grounding path, as required by **250.32(B)(1)**.  

4. **Grounding Electrode Conductor (GEC)**  
   - A separate GEC connects the subpanel’s grounding bar to the local electrode. Its size is determined by **Table 250.66** based on the largest ungrounded (hot) conductor in the feeder.  

5. **No Neutral-to-Ground Bond**  
   - The grounded (neutral) conductor from the feeder **must not** connect to the grounding electrode or subpanel’s grounding system. This avoids parallel paths for fault currents.  

---

### Exceptions Checked  
- **250.142** allows using the grounded conductor for grounding in specific cases (e.g., single branch circuits), but **does not apply here** because the garage is fed by a feeder.  
- **250.134** exceptions for DC circuits or separately run EGCs are irrelevant in this AC feeder scenario.  

---

## NEC 2023 Reference  
The NEC has **identical requirements** for detached structures supplied by feeders. Key differences in CEC:  
- **[CEC]** explicitly requires a grounding electrode for all detached structures...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 250.64, 250.66, 250.134, 250.142, 250.122, 250.32

**Response Time:** 11.4s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** PASS

**Agent Answer:**
## Main Bonding Jumper vs System Bonding Jumper (CEC 2022 with Exceptions)

### **Definitions and Requirements**
1. **Main Bonding Jumper**  
   - **Definition**: Connects the grounded conductor (neutral) to the equipment grounding conductor at the **service** (CEC 2022 Section 100).  
   - **Required**: At every service per **CEC 250.24(D)**.  
   - **Exceptions**:  
     - **250.28(D)**: Sizing based on Table 250.102(C)(1). For services with multiple enclosures (per 230.71(B)), each enclosure’s main bonding jumper must match the largest ungrounded service conductor.  
     - **250.24(D) Exception 1**: Impedance-grounded systems follow 250.36.  

2. **System Bonding Jumper**  
   - **Definition**: Connects the grounded conductor to the equipment grounding conductor at a **separately derived system** (e.g., transformers, generators) (CEC 2022 Section 100).  
   - **Required**: At every **separately derived system** per **CEC 250.30**.  
   - **Exceptions**:  
     - **250.30(A)(1)**: System bonding jumpers can be installed at the source or first disconnecting means. For systems with multiple enclosures, sizing is based on the largest ungrounded conductor.  
     - **250.30(A) Exception No. 2**: Dual connections at source and first disconnecting means are permitted if no parallel paths exist.  
     - **250.30(A) Exception No. 3**: For small transformers (≤1000 VA), minimum size is 14 AWG copper or 12 AWG aluminum.  

---

### **Key Differences**
| Feature                  | Main Bonding Jumper                     | System Bonding Jumper                     |
|--------------------------|-----------------------------------------|-------------------------------------------|
| **Location**             | Service equipment                       | Separately derived systems                |
| **Code Reference**       | CEC 250.24(D)                           | CEC 250.30                                |
| **Sizing**               | Table 250.102(C)(1)                      ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 230.71, 250.28, 250.24, 250.102, 250.30, 250.36

**Response Time:** 13.1s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]  
**Minimum Requirement:**  
A kitchen requires **at least two 20-ampere small-appliance branch circuits** per CEC 2022 Section 210.11(C)(1). These circuits must serve all receptacles in the kitchen (wall, floor, countertop) and are permitted to also supply receptacles in the dining room, pantry, or breakfast room per Section 210.52(B)(1).  

**Dining Room Receptacles:**  
Yes, the two small-appliance branch circuits serving the kitchen **can also supply dining room receptacles**. However:  
- Each kitchen must have its own dedicated small-appliance circuits (no more than one kitchen per circuit).  
- Additional circuits may be added for load balancing if needed.  

**Key Code Citations:**  
- **210.11(C)(1):** Requires two or more 20A small-appliance circuits for kitchens.  
- **210.52(B)(1):** Permits these circuits to serve dining room receptacles.  
- **Exceptions:** No exceptions override the two-circuit minimum or restrict dining room use.  

**Exception Analysis:**  
- **210.52(B)(1) Exception No. 1:** Allows switched receptacles on general-purpose circuits for clocks.  
- **210.52(B)(1) Exception No. 2:** Permits individual circuits for specific appliances (e.g., refrigerators).  
- These exceptions do not affect the two-circuit minimum or dining room receptacle allowance.  

---
## NEC 2023 Reference  
No difference from NEC 2023. The requirement for two 20A small-appliance circuits in kitchens and their permitted use in dining rooms is identical.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.11, 210.52

**Response Time:** 10.3s

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
- Conductor temperature rating: 90°C

**Calculations:**

1. **Base Ampacity** (CEC 2022 Table 310.16):  
   12 AWG copper at 90°C = **30 amperes**

2. **Temperature Correction** (CEC 2022 Table 310.15(B)(1)):  
   50°C ambient → **0.82 factor**

3. **Bundling Adjustment** (CEC 2022 Table 310.15(C)(1)):  
   6 conductors → **0.80 factor**

4. **Final Calculation:**  
   ```python
   30A × 0.82 × 0.80 = 19.68 amperes
   ```

**Final Answer:**  
The adjusted ampacity is **19.68 amperes** after applying both temperature correction and bundling adjustments per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

**Exception Analysis:**  
- No exceptions apply to the temperature correction (310.15(B)(1)) for THHN conductors in this scenario.  
- No exceptions apply to the bundling adjustment (310.15(C)(1)) since the raceway length and conductor count fall within standard requirements.  

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

**Response Time:** 14.8s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]
The California Electrical Code (CEC) requires Arc-Fault Circuit Interrupter (AFCI) protection for 15- and 20-ampere branch circuits in bedrooms, living rooms, and similar areas **to prevent electrical fires caused by dangerous arcing faults**. This requirement is adopted directly from NEC 2023 Section 210.12, with no additional amendments in the CEC.

### Key CEC Requirements:
- **Section 210.12(A)** mandates AFCI protection for all 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets devices in:
  - Bedrooms
  - Living rooms
  - Hallways
  - Closets
  - Bathrooms
  - Similar habitable spaces

### Exceptions in CEC 2022:
After checking `cec_exception_search("210.12", "bedrooms and living areas")`, **no exceptions** were found that modify the AFCI requirement for these areas. The exceptions returned relate to lighting outlets (Section 210.70) and receptacle spacing (Section 210.52), which are separate from AFCI protections.

### Electrical Hazard Prevented:
AFCIs detect and interrupt **series arcs** (e.g., from damaged wiring) and **parallel arcs** (e.g., from loose connections), which can reach temperatures exceeding 10,000°F and ignite surrounding materials. Standard circuit breakers do not detect these arcs, making AFCIs critical for fire prevention in areas with embedded wiring.

---
## NEC 2023 Reference
The NEC requirement is identical to the CEC. No differences exist between CEC 2022 and NEC 2023 for this requirement.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 210.12, 210.70, 210.52

**Response Time:** 11.7s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Torque Specifications for Conductor Terminations (CEC 2022)  

**Why Torque Specifications Matter:**  
1. **Safety Compliance:** Ensures connections meet equipment listing requirements (UL/CSA).  
2. **Prevents Failures:** Proper torque minimizes resistance, heat, and connection degradation.  
3. **Manufacturer Intent:** Equipment is designed for specific torque values to ensure reliability.  

**CEC Requirements:**  
- **Primary Rule:** CEC 2022 **Section 110.14(D)** mandates tightening torque values as indicated on equipment or in manufacturer instructions. Approved methods include torque tools, shear bolts, or breakaway devices.  
- **Specific Case:** CEC **Section 430.9(C)** requires a minimum torque of **0.8 N·m (7 lb-in.)** for control circuit devices with screw-type terminals using 14 AWG or smaller copper conductors (unless otherwise identified).  

**Exceptions Checked:**  
- No exceptions to Section 110.14(D) or 430.9(C) apply to torque specifications.  
- Cross-references (e.g., 110.14(C) temperature limitations) do not override torque requirements.  

**Key Citations:**  
- CEC 2022 **Section 110.14(D)** (Terminal Connection Torque)  
- CEC 2022 **Section 430.9(C)** (Control Circuit Devices)  

---
## NEC 2023 Reference  
NEC 2023 Section 110.14(D) mirrors CEC 2022 requirements. CEC adds the specific 0.8 N·m minimum in 430.9(C) for control circuit devices. No other differences found.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 430.9, 110.14

**Response Time:** 10.2s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Service Load Calculation (CEC 2022 with Exceptions)

### Step 1: General Lighting and Receptacles  
- **3,000 sq ft × 3 VA/sq ft = 9,000 VA (9 kW)**  

### Step 2: Small Appliance Circuits  
- **2 circuits × 1,500 VA = 3,000 VA (3 kW)**  

### Step 3: Laundry Circuit  
- **1 circuit × 1,500 VA = 1,500 VA (1.5 kW)**  

### Step 4: Major Appliances  
- **Range (12 kW):**  
  Per **CEC Table 220.55**:  
  8 kW + 40% of (12 kW - 8 kW) = **9.6 kW**  
- **Dryer (5.5 kW):**  
  Per **CEC 220.54**:  
  5,000 VA + 55% of (5,500 VA - 5,000 VA) = **5,275 VA (5.275 kW)**  

### Step 5: Heating/Cooling  
- **AC Load (4.6 kW):**  
  No heating specified → **100% of AC load**  

### Step 6: Total Load Before Demand Factors  
- **9 kW (lighting) + 3 kW (small appliances) + 1.5 kW (laundry) + 9.6 kW (range) + 5.275 kW (dryer) + 4.6 kW (AC) = 32.975 kW**  

### Step 7: Apply Demand Factors (CEC 220.54)  
- **First 10 kW at 100%:** 10 kW  
- **Remaining 22.975 kW at 40%:** 22.975 × 0.4 = **9.19 kW**  
- **Total Service Load:** 10 + 9.19 = **19.19 kW**  

### Step 8: Convert to Amperes  
- **19,190 VA ÷ 240V = 79.96 A**  

---

## CEC Exceptions Applied  
1. **CEC 220.80 (Optional Calculations):**  
   - Allows simplified optional method (not used here, but available).  
2. **CEC 220.40 (General Load Sum):**  
   - Confirms calculated load must include all branch circuits after demand factors.  
3. **CEC 220.44 (Receptacle Loads):**  
   - No impact on this calculation (applies to non-dwelling units).  

---

## Final Determination  
- **200A Panel Capacity:** 200A  
- **Calculated Load:** ~80A  
- **Conclusion:** The 200A panel is **adequately sized** with significant headroom.  

---

## CEC vs NEC Comparison  
- **No material differences** from NEC 2023. California uses the same demand factors and tables (220.54, 220.55).  
- **Exceptions checked:** No amendments to service load calculations in CEC 2022.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 5 found
- 220.40, 220.54, 220.55, 220.44, 220.80

**Response Time:** 18.5s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## **California Electrical Code (CEC 2022) Violations Identified**

### **1. Insufficient Depth Clearance (Violation of CEC 110.26(A)(1))**
- **Measured:** 28 inches  
- **Required:** 30 inches (Table 110.26(A)(1), *Condition 2* for residential panels with grounded parts on one side).  
- **Exception Check:**  
  - **Exception No. 2** (CEC 110.26(A)(1)(c)) allows reduced clearance in existing dwellings for panels ≤ 200A.  
  - **However, this exception does NOT waive the 30-inch depth requirement**—it only permits reduced *height* clearance.  
  - **Result:** Depth violation remains unaddressed by exceptions.

---

### **2. Obstruction in Working Space (Violation of CEC 110.26(B))**
- **Issue:** Water heater located 16 inches from the panel (within the required 30-inch depth).  
- **Violation:** Storage or obstructions are strictly prohibited in working space (CEC 110.26(B)).  
- **Exception Check:** No exceptions apply—obstructions are explicitly forbidden regardless of panel size or location.

---

### **3. Insufficient Vertical Height Clearance (Violation of CEC 110.26(A)(3))**
- **Measured:** 5 feet (60 inches)  
- **Required:** 6.5 feet (78 inches) vertically from floor to top of working space.  
- **Exception Check:**  
  - **Exception No. 2** (CEC 110.26(A)(1)(c)) permits reduced *height* clearance in existing dwellings for panels ≤ 200A.  
  - **However, this exception does NOT apply to the vertical height requirement**—only to depth and width in specific scenarios.  
  - **Result:** Vertical height violation remains unaddressed by exceptions.

---

### **4. Panel Height Compliance (No Direct Violation)**
- **Measured:** 5 feet (60 inches)  
- **Requirement:** No specific height limit for panel installation, but working space must extend to 6.5 feet.  
- **Conclusion:** Panel height itself is not a violation, but the working space above it is insufficient.

---

### **5. Entrance Access (Pending Verification)**
- **Requirement:** At least one entrance of **2...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search, nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 32.6s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## Required Protection for Kitchen Circuits (NEC 2023 with Exceptions Checked)

### 1. **Countertop Receptacles (20A circuits)**
- **Protection Required:** **GFCI + AFCI (Combination)**
- **NEC References:**
  - **210.8(A)(6):** GFCI protection required for all countertop receptacles in kitchens.
  - **210.12(A):** AFCI required for all 120V, 15A/20A circuits in dwelling units.
- **Exceptions Checked:** No exceptions apply to GFCI/AFCI requirements for countertop receptacles.

### 2. **Dishwasher (15A dedicated circuit)**
- **Protection Required:** **GFCI + AFCI (Combination)**
- **NEC References:**
  - **210.8(A)(6):** GFCI applies to all kitchen receptacles, including dishwashers.
  - **210.12(A):** AFCI required (no exception for dishwashers).
- **Exceptions Checked:** No exceptions exempt dishwashers from GFCI/AFCI.

### 3. **Garbage Disposal (15A dedicated circuit)**
- **Protection Required:** **GFCI + AFCI (Combination)**
- **NEC References:**
  - **210.8(A)(6):** GFCI required for all kitchen receptacles.
  - **210.12(A):** AFCI required (no exception for disposals).
- **Exceptions Checked:** No exceptions apply.

### 4. **Refrigerator (20A dedicated circuit)**
- **Protection Required:** **Standard Breaker (No GFCI or AFCI)**
- **NEC References:**
  - **210.8(A)(6):** GFCI not required for fixed appliances.
  - **210.12(A) Exception:** AFCI not required for circuits serving only fixed refrigeration equipment.
- **Exceptions Checked:** Confirmed exemption for refrigerators.

---

**Key Exceptions Verified:**
- **210.52(B)(1):** Allows additional receptacles but does not exempt from GFCI/AFCI.
- **210.52(C)(1) Exceptions:** Address receptacle placement, not protection requirements.

**Final Determination:** All requirements stand as initially stated. No exceptions override the GFCI/AFCI mandates for countertop, dishwasher, or disposal circuits. Refrigerator remains exempt from both protections.

✓ **Sources: NEC 2023 (primary), verified exceptions**

**Tool Usage:**
- CEC Tools: None
- NEC Tools: nec_search, nec_exception_search
- CEC Primary: No

**Citations:** 3 found
- 210.8, 210.12, 210.52

**Response Time:** 15.2s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## [Main Answer - CEC 2022]

**Identified Violations and Correct Configuration:**

1. **Violation: Neutral and Ground Bars Bonded Together**  
   - **CEC 2022 Section 250.24(D):** The grounded (neutral) conductor must not be reconnected to ground on the load side of the service disconnect. Bonding neutral and ground bars in a subpanel creates a parallel path for neutral current, risking equipment damage and improper GFCI operation.  
   - **Correct:** Neutral and ground bars must be **separated** in subpanels. The main bonding jumper (connecting neutral/ground) exists **only** in the main service panel.

2. **Violation: Neutral Bar Bonded to Metal Enclosure**  
   - **CEC 2022 Section 250.4(A)(5):** The neutral (grounded) conductor must not be connected to normally non-current-carrying metal parts in subpanels. Bonding the neutral bar to the enclosure creates a ground loop and violates the requirement for an effective ground-fault current path.  
   - **Correct:** Neutral bar must remain **electrically isolated** from the metal enclosure in subpanels. Only the **ground bar** should be bonded to the enclosure.

3. **Violation: Ground Bar Bonded to Metal Enclosure (Improper Method)**  
   - **CEC 2022 Section 250.104:** Equipment grounding must use a **listed bonding jumper** (not a main bonding jumper). While bonding the ground bar to the enclosure is correct, the method must comply with 250.104(A)(1) (e.g., direct metal-to-metal contact with a listed bonding jumper).  
   - **Correct:** Ensure the ground bar is bonded to the enclosure using a **listed bonding jumper** (not a main bonding jumper).

4. **Violation: Feeder Neutral Connected to Neutral Bar (Improper Grounding Path)**  
   - **CEC 2022 Section 250.24(C)(5):** The neutral conductor must not carry ground-fault current. If the neutral bar is bonded to the enclosure (as in this case), the feeder neutral becomes part of the ground-fault path, violating 250.4(A)(5).  
   - **Correct:** Feeder neutral connects ...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.4, 250.24, 250.50, 250.104

**Response Time:** 10.4s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Verified (CEC 2022)

**Maximum Conductors:**  
A 1¼" RMC conduit can accommodate **28** 10 AWG THHN conductors under CEC 2022 Chapter 9 fill requirements.

**Exception Analysis:**  
The following exceptions were checked for conduit fill rules:
1. **Section 402.7** – Limits fixture wires to Table 1 fill percentages.
2. **Sections 358.22, 362.22, 354.22** – All reiterate the Table 1 fill limits for specific conduit types.
3. **Section 640.23** – Applies Table 1 fill rules to technical power systems.

**No exceptions override the 40% fill rule** for this scenario. All exceptions align with the base requirement from Chapter 9, Table 1.

---
## NEC 2023 Reference  
No difference from NEC 2023. Conduit fill calculations remain unchanged.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_lookup_conduit_fill, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 402.7, 640.23, 354.22, 362.22, 358.22

**Response Time:** 18.4s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**
## Voltage Drop Calculation (CEC 2022)

**Given:**
- Circuit: 120V single-phase
- Load: 22A continuous
- Conductor: 12 AWG copper (1.29 Ω/1000ft)
- Distance: 50 feet one-way

**Calculations:**

1. **Voltage Drop Formula** (per NEC 210.19(A) and CEC 2022):
   $$
   VD = \frac{2 \times I \times L \times R}{1000}
   $$
   Where:
   - $ I = 22 $ A
   - $ L = 50 $ ft
   - $ R = 1.29 $ Ω/1000ft

2. **Substitute Values:**
   $$
   VD = \frac{2 \times 22 \times 50 \times 1.29}{1000} = \frac{2838}{1000} = 2.838 \text{ volts}
   $$

3. **Percentage Drop:**
   $$
   \text{Percentage} = \left( \frac{2.838}{120} \right) \times 100 = 2.365\%
   $$

**Code Compliance Analysis:**

- **CEC 2022 Section 647.4(D):**  
  - Voltage drop on branch circuits **shall not exceed 1.5%** (2.84V > 1.8V → **Non-compliant**).  
  - Combined feeder/branch drop **shall not exceed 2.5%** (2.36% < 3.0V → **Compliant**).  

- **Informational Note in CEC 210.19(A):**  
  - Recommends **3% maximum** for branch circuits (2.36% ≤ 3.6V → **Compliant**).  

**Conflict Resolution:**  
Section 647.4(D) applies to **specific high-voltage systems** (context from "wiring methods for systems over 600V"). For **standard 120V branch circuits**, the **3% recommendation** in 210.19(A) governs.  

**Final Answer:**
- **Voltage Drop:** 2.84 volts (2.36% of 120V)
- **Compliance:**  
  - ✅ Meets **NEC/CEC 3% recommendation** (2.36% ≤ 3%)  
  - ⚠️ Exceeds **CEC 647.4(D) 1.5% limit** (likely inapplicable for standard 120V circuits)  

**Note:** Verify conductor resistance from **Table 8, Chapter 9** (standard 12 AWG copper = 1.98 Ω/1000ft). Using this value:  
$$
VD = \frac{2 \times 22 \times 50 \times 1.98}{1000} = 4.356V \, (3.63\%) \, \text{→ Exceeds 3% limit}.
$$

---
## NEC 2023 Reference
No difference from NEC 2023. Same voltage drop formula and 3% recommendation apply.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 647.4, 210.19

**Response Time:** 20.9s

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

3. **Adjustment Factor** (CEC 2022 Table 310.15(C)(1)):
   6 current-carrying conductors = **0.80 factor**

4. **Adjusted Ampacity Calculation:**
   ```python
   adjusted = 20 × 0.71 × 0.80 = 11.36 amperes
   ```

**Final Answer: 11.36 amperes**

This adjusted ampacity accounts for both elevated ambient temperature and
multiple conductors per CEC 2022 Sections 310.15(B)(1) and 310.15(C)(1).

No exceptions to these derating requirements were found.

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

**Response Time:** 10.6s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Minimum Grounding Electrode Conductor Size (CEC 2022)

**Given:**
- Four parallel 250 kcmil copper conductors per phase
- Total equivalent service size: 4 × 250 kcmil = **1000 kcmil**

**CEC Table 250.66 Requirements:**
| Service Conductor Size | Minimum GEC Size (Copper) |
|------------------------|--------------------------|
| 601–1100 kcmil          | **250 kcmil**            |

**Exceptions Checked:**
1. **250.66(A)**: Applies only if connected to rod/pipe/plate electrodes and doesn't extend to other electrodes. Not applicable here.
2. **250.66(B)**: Applies for concrete-encased electrodes. Not applicable here.
3. **250.66(C)**: Applies for ground rings. Not applicable here.
4. **250.54**: Permits auxiliary electrodes but doesn't affect conductor size.
5. **250.166**: DC system exceptions not applicable to this AC installation.

**Final Answer:**
The minimum required copper grounding electrode conductor (GEC) size is **250 kcmil** per CEC Table 250.66. No applicable exceptions reduce this requirement for the given scenario.

---
## NEC 2023 Reference
No difference from NEC 2023. Same requirements apply.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 250.54, 250.66, 250.166

**Response Time:** 15.5s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 27/28
- **Success Rate**: 100.0%
- **Average Response Time**: 13.7s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

