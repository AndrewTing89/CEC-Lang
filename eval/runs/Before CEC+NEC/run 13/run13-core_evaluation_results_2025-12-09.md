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
| **Total Duration** | 366.6s |
| **Avg per Question** | 13.1s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## 12 AWG Copper Conductor Ampacity (CEC 2022) - Final Answer

**Ampacity**: 25 amperes (CEC Table 310.16, 75°C column)  
**Overcurrent Protection Limit**: 20 amperes (CEC 240.4(D))  

✓ **No applicable exceptions** found for general 12 AWG copper conductor use.  
✓ Exceptions 440.6 and 311.12 relate to specialized equipment (HVAC, conductor materials) not applicable to this general ampacity question.

---

### Final Notes:
- The 25A ampacity from Table 310.16 applies to general wiring.
- Section 240.4(D) **limits overcurrent protection to 20A** for 12 AWG copper regardless of ampacity.
- Exceptions found pertain to specific equipment types (HVAC, multimotor) not mentioned in the original question.

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 240.4, 440.6, 310.16, 311.12

**Response Time:** 11.7s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Final Answer: Corrected Conductor Sizing for 60A Circuit (CEC 2022)

**Minimum required size**: **4 AWG copper**  
- **Ampacity**: 85A (CEC Table 310.16 @ 75°C)  
- **Overcurrent Protection**: 60A (per 240.4(D) limit of 70A for 4 AWG)  

**Why 6 AWG is invalid**:  
- 65A ampacity (Table 310.16) but **240.4(D)** restricts OCPD to **50A max** for 6 AWG copper.  
- 60A OCPD would violate this rule.  

**Exceptions Checked**:  
- Only exception found (440.6) applies to **hermetic refrigerant motor-compressors** – not relevant to general 60A circuits.  

**Final Solution**:  
- Use **4 AWG copper** with **60A OCPD** to comply with both ampacity and 240.4(D) limits.  

✓ Source: CEC 2022 Tables 310.16, 240.4(D)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 240.4, 440.6, 310.16

**Response Time:** 18.9s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection in Residential Kitchens (CEC 2022)  

**GFCI protection is required for all 125–250V receptacles in residential kitchens that serve countertop surfaces**, as specified in **CEC 2022 Section 210.8(A)(6)**.  

### Key Details:  
1. **Primary Rule**:  
   - **CEC 210.8(A)(6)** mandates GFCI protection for kitchen countertop receptacles.  
   - Applies to single-phase branch circuits rated ≤150 volts to ground.  

2. **Exceptions**:  
   - **Exception 1**:  
     *Listed locking support and mounting receptacles* used with ceiling luminaires or fans **are exempt** if:  
     - They are not general-purpose convenience outlets.  
     - If the receptacle is integral to the ceiling device (e.g., a fan with a built-in outlet), **GFCI protection is still required**.  
   - **Exception 2**:  
     *Switched receptacles* supplied by a general-purpose 15- or 20-ampere branch circuit (per 210.70(A)(1), Exception No. 1) are permitted but **must still comply with GFCI requirements** if located in kitchen countertop areas.  

3. **Additional Context**:  
   - **CEC 210.52(B)(3)** reinforces that countertop receptacles must be on small-appliance branch circuits and comply with GFCI rules.  
   - No other exceptions apply to standard kitchen countertop receptacles.  

### Final Answer:  
GFCI protection is **required** for all kitchen countertop receptacles unless the specific exception for listed ceiling-mounted devices applies. Always verify the receptacle type and application to determine exemption eligibility.  

✓ Source: CEC 2022 Sections 210.8(A)(6), 210.52(B)(3)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 210.8, 210.52, 210.70

**Response Time:** 10.8s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection for Bedroom Circuits (CEC 2022)  

**Final Answer:**  
Yes, **AFCI protection is required** for all 120V, single-phase, 15- and 20-ampere branch circuits in bedrooms of new residential construction in California.  

**Key Details:**  
- **Primary Rule:** CEC 2022 **Section 210.12(A)** explicitly requires AFCI protection for dwelling unit bedrooms.  
- **No Applicable Exceptions:**  
  - The exceptions in **Section 406.4(D)(4)** relate to *replacements* of receptacles, not new construction.  
  - Other exceptions (e.g., grounding, GFCI) do not override AFCI requirements for bedrooms.  

**Compliance Methods:**  
Use one of the following:  
1. Combination-type AFCI circuit breaker.  
2. Outlet branch-circuit-type AFCI receptacle at the first outlet.  
3. Branch/feeder-type AFCI at the panel + outlet AFCI at the first outlet.  

**Source:** CEC 2022 Section 210.12(A)  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 406.4, 210.12

**Response Time:** 8.6s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** PASS

**Agent Answer:**
## Aluminum Conductors for 200A Service (CEC 2022)  

**Yes**, aluminum conductors are permitted for a 200A service. The required size is:  

✓ **4/0 AWG aluminum** (75°C rating)  
- Based on **CEC Table 310.12(A)** for single-phase dwelling services  
- Provides 200A ampacity at 75°C  
- Meets **Section 230.42(A)** requirements for service conductor ampacity  

---

### **Key Exceptions and Limitations**  
1. **Overload Protection (Section 230.90)**  
   - Overcurrent devices must not exceed the conductor's ampacity (200A for 4/0 AWG aluminum).  
   - Exception: For motor-starting currents, ratings complying with 430.52/62/63 are permitted.  

2. **Minimum Size Requirements (Section 310.3)**  
   - Minimum aluminum size for services is 6 AWG (Section 230.31(B)), but **4/0 AWG is required for 200A**.  

3. **Temperature and Insulation**  
   - Termination temperature limits per **110.14(C)** must be observed (e.g., 75°C for 4/0 AWG THWN).  
   - Insulation must comply with **Section 230.41** (e.g., THWN, XHHW).  

4. **Service Conductor Sizing Rule (Section 310.12)**  
   - For dwelling services rated 100–400A, conductors can be sized at **83% of the service rating** (200A × 0.83 = 166A).  
   - **4/0 AWG aluminum** (200A at 75°C) satisfies this requirement without adjustments.  

---

### **Final Answer**  
✓ **4/0 AWG aluminum** is required for a 200A service.  
✓ **Source**: CEC 2022 Table 310.12(A), Sections 230.42, 230.90, 310.3, and 310.12.

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_size, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 310.12, 310.3, 110.14, 230.41, 430.52, 230.90, 230.42, 230.31

**Response Time:** 11.5s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Clearance Depth (CEC 2022)  

The minimum working clearance depth required in front of a 120/240V residential electrical panel is **900 mm (3 feet)** per **CEC Table 110.26(A)(1)** for **Condition 1** (exposed live parts on one side and grounded parts on the other).  

### Exceptions Checked:  
1. **CEC 110.26(E)** specifies dedicated equipment space requirements but does **not reduce** the minimum working clearance depth. It emphasizes:  
   - A **6-foot (1.8 m) vertical zone** above the panel must be dedicated to electrical equipment.  
   - Suspended ceilings with removable panels are permitted within this zone.  
   - Foreign systems (e.g., plumbing) must be protected to avoid damage.  

2. Other exceptions (352.60, 356.60, 440.14) relate to grounding and disconnecting means and **do not affect** working space requirements for residential panels.  

### Final Answer:  
**3 feet (900 mm)** is the minimum depth required in front of the panel. Additional vertical clearance (6 feet above the panel) is mandated by **110.26(E)** but does not override the horizontal working space.  

✓ Source: CEC 2022 Table 110.26(A)(1) and Section 110.26(E)

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 110.26, 440.14, 356.60, 352.60

**Response Time:** 7.8s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** PASS

**Agent Answer:**
## Small Appliance Branch Circuits in Kitchens (CEC 2022)  

**Answer:**  
A minimum of **2** 20-ampere small-appliance branch circuits are required for a kitchen.  

**Code Basis:**  
- **CEC 2022 Section 210.52(B)(1):**  
  *"Receptacles installed in a kitchen to serve countertop surfaces shall be supplied by not fewer than two small-appliance branch circuits..."*  
- **CEC 2022 Section 210.11(C)(1):**  
  *"Two or more 20-ampere small-appliance branch circuits shall be provided for all receptacle outlets specified by 210.52(B)."*  

**Exceptions Checked:**  
1. **Exception No. 1 (210.52(B)(1)):** Permits switched receptacles from general-purpose circuits but does not reduce the 2-circuit requirement.  
2. **Exception No. 2 (210.52(B)(1)):** Allows specific appliances on individual circuits but does not override the 2-circuit minimum.  

**Key Requirements:**  
- **Minimum 2 circuits** must supply all kitchen countertop and wall receptacles.  
- Circuits **cannot serve more than one kitchen**.  
- Additional circuits are permitted but not required.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.11

**Response Time:** 7.7s

---

### baseline-008: knowledge_simple

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Expected:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is required for a new 200A residential service per **CEC 2022 Section 230.67(A)**. This section explicitly mandates that all services supplying **dwelling units** must include a **surge-protective device (SPD)**.

### Key Details:
- **SPD Location:**  
  - Must be an integral part of the service equipment or located immediately adjacent (Section 230.67(B)).  
  - **Exception:** SPD may be installed at the next level of distribution equipment downstream toward the load if not in the service equipment (Exception to 230.67(B)).  

- **SPD Type:**  
  - Must be **Type 1 or Type 2 SPD** (Section 230.67(C)).  

- **Replacement Requirements:**  
  - If service equipment is replaced, SPD requirements still apply (Section 230.67(D)).  

### Cross-Reference Check:
- No exceptions in CEC 2022 override the SPD requirement for dwelling units.  
- Section 230.94 permits surge arresters on the supply side of the service disconnect but does not negate the SPD requirement.  

✓ Source: CEC 2022 Section 230.67, Exception to 230.67(B)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 230.94, 230.67

**Response Time:** 11.2s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** PASS

**Agent Answer:**
## Final Answer: 200A Service Conductor Sizing (CEC 2022)

### **1. Required Conductor Sizes**
- **Copper**: **2/0 AWG** (Table 310.12(A))  
- **Aluminum**: **4/0 AWG** (Table 310.12(A))  

### **2. Aluminum Use Requirements**
✅ **Permitted**, but with these conditions:
1. **Terminations**: Must be marked **AL/CU** (CEC 110.14(C)(1)(b)).  
2. **Anti-oxidant compound**: Required at all aluminum-to-terminal connections.  
3. **Torque compliance**: Terminals must be tightened to manufacturer specifications (110.14(D)).  

### **3. Grounding Electrode Conductor (GEC)**
- **Copper service**: **4 AWG Cu** (Table 250.66).  
- **Aluminum service**: **2 AWG Cu** (Table 250.66).  

---

### **Key Code References**
- **Table 310.12(A)**: Dwelling service conductor sizing.  
- **110.14(C)**: Aluminum termination requirements.  
- **250.66**: GEC sizing based on service conductor size.  

---

### **Exceptions Verified**
- No exceptions in **310.12(A)** allow smaller conductors for aluminum.  
- **110.14(C)** exceptions confirm aluminum use with proper termination.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_conductor_size, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 310.12, 110.14, 250.66

**Response Time:** 19.2s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** PASS

**Agent Answer:**
## NEC Requirements for Multiwire Branch Circuit (210.4) with Exceptions

**Circuit Breaker Requirements:**
1. **Simultaneous Disconnection (210.4(B)):**  
   A **2-pole 20A circuit breaker** is required to disconnect both ungrounded (hot) conductors simultaneously.  
   - *Exception:* Handle ties or interlocking devices may be used if approved by the AHJ, but 2-pole breakers are standard for MWBCs.  
   - *Footnote:* See 240.15(B) for single-pole breaker use with handle ties.

2. **Ampacity Compliance (240.4(D)):**  
   12 AWG copper conductors require a **20A overcurrent device** (not exceeding 25A for 12 AWG in specific cases, but 20A is standard for kitchen circuits).

---

**Neutral Termination Requirements:**
1. **Continuity (200.4(B)):**  
   The neutral conductor must remain unbroken and uninterrupted.  
   - *Exception 1:* Unique cables (e.g., 12/3 NM-B) inherently group conductors, so no additional marking is required.  
   - *Exception 2:* Conductors passing through boxes without splices/terminations don’t need grouping.

2. **Sizing (250.122):**  
   The neutral must be **12 AWG** to handle potential unbalanced harmonic currents from kitchen receptacles.

3. **Grouping (210.4(D)):**  
   All conductors (hots and neutral) must be grouped in the same cable (12/3 NM-B) to prevent magnetic field imbalances.

---

**Key Exceptions/Notes:**
- **Line-to-Neutral Loads Only (210.4(C)):**  
  MWBCs must supply only line-to-neutral loads (e.g., standard receptacles).  
  - *Exception 1:* Permits line-to-line loads if all hots are disconnected simultaneously (not applicable here).  
  - *Exception 2:* Permits line-to-line loads with simultaneous disconnection (not applicable here).

- **Kitchen-Specific (210.5(D)):**  
  Kitchens require **at least two 20A small-appliance branch circuits**, but this question focuses on MWBC wiring rules.

---

**Summary of Compliance:**
- ✅ 2-pole 20A breaker for simultaneous disconnection  
- ✅ 12 AWG neutral with continuous termin...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 6 found
- 210.4, 240.15, 250.122, 240.4, 210.5, 200.4

**Response Time:** 13.2s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Dwellings (NEC 2023 with CEC Exceptions)

### **Required Locations (NEC 210.8(A))**
1. **Bathrooms**  
2. **Garages/accessory buildings** (floor at or below grade)  
3. **Outdoors**  
4. **Crawl spaces** (at or below grade)  
5. **Kitchens** (countertop surfaces)  
6. **Within 6 ft of sinks** (food prep/cooking areas)  
7. **Boathouses**  
8. **Within 6 ft of bathtubs/showers**  
9. **Laundry areas**  
10. **Indoor damp/wet locations**  

---

### **Exceptions (CEc_exception_search Results)**
1. **Fire alarm/burglar alarm systems**:  
   - Receptacles for permanently installed systems (e.g., 760.41(B)) are exempt (CEc 210.8(A)(5) exception).  

2. **Snow-melting/deicing systems**:  
   - Non-readily accessible receptacles on dedicated circuits (426.28/427.22) are exempt (ce 210.8(A)(3) exception).  

3. **Ceiling luminaires/fans**:  
   - Listed locking receptacles for ceiling fans/luminaires are exempt if not for general use (ce 210.8(A) exception).  

4. **Industrial labs/hospitals**:  
   - Receptacles where power interruption creates greater hazards (e.g., patient beds in healthcare facilities) may bypass GFCI (ce 210.8(B)(5) exceptions).  

5. **Rooftop receptacles**:  
   - Need not be readily accessible (ce 210.8(F) exception).  

---

### **Key Notes**
- **Cross-references**:  
  - Appliances: See 422.5 for GFCI requirements.  
  - Boathouses: See 555.9.  
  - Industrial exceptions: See 590.6(B)(2).  

✓ Source: NEC 2023 Section 210.8(A), CEC 2022 exceptions.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 7 found
- 426.28, 427.22, 422.5, 590.6, 760.41, 555.9, 210.8

**Response Time:** 15.4s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirements for Residential Service (CEC 2022)  

**Requirement:**  
Surge protection **is required** for all new residential services per **CEC 2022 Section 230.67**.  

**Installation Locations:**  
1. **Integral to service equipment** (e.g., main panel)  
2. **Adjacent to service equipment**  
3. **Downstream at next distribution level** (exception allows SPD installation at downstream panels if not integrated into service equipment)  

**SPD Type Requirements:**  
- Must be **Type 1 or Type 2 SPD** (Section 230.67(C))  
- Type 1: Installed at service entrance for protection against external surges  
- Type 2: Installed at distribution panels for secondary protection  

**Key Exception:**  
If not integrated into service equipment, SPD may be installed at downstream panels **but must still protect the entire dwelling** (Exception to 230.67(B)).  

**No Conflicting Exceptions Found:**  
- Other exceptions (e.g., 230.40, 230.2) do not override 230.67 for residential applications.  
- Section 230.94 confirms SPDs may be installed on the supply side of service disconnects (permitted by exception).  

✓ Source: CEC 2022 Section 230.67 and exceptions.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 230.40, 230.94, 230.67, 230.2

**Response Time:** 7.6s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** PASS

**Agent Answer:**
## Working Space Requirements (CEC 2022)

The installation **does not meet CEC requirements** for working space around electrical equipment:

1. **Required front clearance**: 36 inches (3 ft) minimum per CEC Table 110.26(A)(1) for 240V equipment (Condition 1).
2. **Actual front clearance**: 24 inches (insufficient by 12 inches).
3. **Side clearance**: 18 inches to water heater is acceptable as long as it doesn't reduce the required 30-inch wide work space (not specified in question).

### Key Violation:
- **CEC 110.26(A)(1)** mandates a minimum **36-inch depth** of working space in front of the panel for 240V systems under Condition 1 (exposed live parts on one side, grounded parts on the other).

### Exceptions Checked:
- **CEC 110.26(A)(1)(b)** (low voltage exception) does not apply (30V max).
- **CEC 110.26(A)(1)(c)** (existing buildings) requires special conditions not mentioned.
- **CEC 425.8** (industrial exceptions) requires special permission and qualified personnel not indicated.

### Corrective Action:
Increase front clearance to **at least 36 inches** to comply with CEC requirements.

✓ Source: CEC 2022 Table 110.26(A)(1)

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 110.26, 425.8

**Response Time:** 8.5s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Multiple Conductors on a Terminal (CEC 2022)

**Answer:**  
Yes, this is a **code violation** under **CEC 2022 Section 110.14(C)**.  

### Key Requirements:
1. **Single Conductor per Terminal (110.14(C)(1))**  
   Conductors must be connected to terminals in a manner that prevents damage. A terminal is **not permitted to have more than one conductor** unless:  
   - The terminal is **listed and marked** for multiple conductors (Exception 1 to 110.14(C)(1)).  

2. **Breaker Terminal Rating**  
   The breaker in question is **not marked** for two conductors, violating the requirement that multiple conductors require a terminal specifically listed for this use.  

3. **Overcurrent Protection Compliance**  
   While 12 AWG copper conductors are permitted on a 20A breaker (per **CEC 240.4(D)(3)**), this does not override the termination rule in 110.14(C).  

### Exceptions Checked:
- **408.41**: Applies to grounded conductor terminations in panelboards. Not applicable here (ungrounded conductors on a breaker).  
- **355.60, 300.15, 215.2, 230.90**: None address multiple conductors on a breaker terminal.  

### Corrective Action:
- Replace the breaker with one **listed for two conductors** (e.g., marked "2 Wires") or  
- Use a **single conductor** per terminal as required.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 408.41, 110.14, 215.2, 230.90, 300.15, 240.4, 355.60

**Response Time:** 11.0s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** PASS

**Agent Answer:**
## Grounding and Bonding for Detached Garage Subpanel (CEC 2022) – Final Answer

For a **detached garage subpanel** with a **4-wire feeder**, the grounding and bonding configuration must adhere to the following **California-specific requirements**:

---

### **1. Neutral and Ground Separation**
- **Neutral bus**: Connected **only** to the **grounded (neutral) conductor** from the feeder.
- **Grounding bus**: Connected to:
  - The **equipment grounding conductor (EGC)** from the house panel.
  - The **grounding electrode conductor (GEC)** from the garage's grounding electrode (e.g., ground rod).
- **No bonding** between neutral and ground is allowed in the subpanel.  
  *(CEC 250.32(B)(1) – Enforces separation in subpanels)*

---

### **2. Equipment Grounding Conductor (EGC)**
- The **4-wire feeder must include an EGC** sized per **Table 250.122** based on the feeder's overcurrent protection rating.
- The EGC connects to the **grounding bus** in the subpanel.  
  *(CEC 250.142(B) – Prohibits using grounded conductor for grounding on load side)*

---

### **3. Grounding Electrode Conductor (GEC)**
- A **separate grounding electrode** (e.g., ground rod) is required at the detached garage.
- The GEC connects the grounding electrode to the **grounding bus** in the subpanel.
- The GEC must be sized per **Table 250.66** based on the largest ungrounded conductor in the feeder.  
  *(CEC 250.32(B)(2) – Mandates grounding electrode for separate buildings)*

---

### **4. Exceptions and Overrides**
- **Exception 250.142(A)(2)**: Permits connecting the grounded conductor to equipment on the supply side of the main disconnect in separate buildings.  
  *Does not apply here* because the subpanel is on the **load side** of the main service disconnect.
- **Title 24 Part 6 (California mandate)**: Requires grounding electrodes for all detached structures with electrical service.  
  *Applies here* – The garage must have its own grounding electrode.

---

### **Summary Configuration**...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.66, 250.122, 250.142, 250.32

**Response Time:** 11.8s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** PASS

**Agent Answer:**
## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)  

### **Definitions**  
1. **Main Bonding Jumper**  
   - Connects the **grounded conductor (neutral)** to the **equipment grounding conductor** at the **service** (CEC 100, 250.28).  
   - **Required at every service** (e.g., utility service entrance).  

2. **System Bonding Jumper**  
   - Connects the **grounded conductor** to the **equipment grounding conductor** at the **source of a separately derived system** (e.g., transformers, generators) (CEC 250.28, 250.30).  
   - **Required at every separately derived system**.  

---

### **Key Differences**  
| Feature                  | Main Bonding Jumper                     | System Bonding Jumper                     |  
|--------------------------|------------------------------------------|--------------------------------------------|  
| **Location**             | At the **service** (utility connection) | At the **source of a separately derived system** |  
| **Application**          | Services (e.g., residential, commercial) | Separately derived systems (e.g., transformers, generators) |  
| **Sizing**               | Per **Table 250.102(C)(1)** based on largest ungrounded service conductor | Per **Table 250.102(C)(1)** based on largest ungrounded conductor in the derived system |  

---

### **When Required**  
1. **Main Bonding Jumper**  
   - **Mandatory at every service** (CEC 250.28(B)).  
   - Example: A residential service with 200A service entrance conductors requires a main bonding jumper sized per Table 250.102(C)(1).  

2. **System Bonding Jumper**  
   - **Mandatory at the source of every separately derived system** (CEC 250.30(A)(1)).  
   - Example: A 480V to 208V transformer requires a system bonding jumper at its secondary side.  

---

### **Sizing Rules**  
Both jumpers are sized using **Table 250.102(C)(1)**:  
- **Main bonding jumper**: Based on the largest ungrounded service conductor.  
- **System bonding jumper**: Based on the la...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 250.36, 250.28, 250.30, 250.102, 250.8

**Response Time:** 12.3s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** PASS

**Agent Answer:**
## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)  

**Answer:**  

1. **Minimum Required Circuits:**  
   A **minimum of two 20-ampere small-appliance branch circuits** are required for the kitchen (and similar areas like pantries, breakfast rooms, or dining rooms).  
   - **Citation:** CEC 2022 **Section 210.52(B)(1)**  
   - **Rationale:** These circuits must serve all wall, countertop, and floor receptacles in the kitchen, as well as receptacles for refrigeration equipment.  

2. **Dining Room Receptacles:**  
   **Yes**, these two 20-ampere small-appliance branch circuits **can also serve dining room receptacles**.  
   - **Citation:** CEC 2022 **Section 210.52(B)(1)** explicitly permits the circuits to supply receptacles in the kitchen *and other rooms* (e.g., dining rooms) specified in the code.  
   - **Limitation:** No small-appliance branch circuit shall serve more than **one kitchen** (per CEC 2022 Section 210.52(B)(1)).  

**Key Exceptions:**  
- **Exception No. 1 (210.52(B)(1)):** Allows switched receptacles from a general-purpose 15- or 20-ampere branch circuit for specific uses (e.g., lighting).  
- **Exception No. 2 (210.52(B)(1)):** Permits a receptacle for a specific appliance to be on an individual branch circuit (e.g., a dedicated circuit for a microwave).  
- **Exception in 210.52(B)(3):** Clarifies that small-appliance circuits may serve dining room receptacles but not exceed one kitchen per circuit.  

**Cross-References:**  
- **220.52:** Load calculations for small-appliance circuits (1,500 VA per circuit).  
- **210.11(C)(1):** Requires two or more small-appliance circuits for dwelling units.  

**Final Verification:**  
- No limiting rules override this application.  
- Exceptions do not restrict dining room receptacles from being served by small-appliance circuits.  

**Source:** CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 210.52, 220.52, 210.11

**Response Time:** 10.6s

---

### core-010: load_calculations

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Expected:** Base ampacity: 30A at 90°C (Table 310.16). Temperature correction factor: 0.82 for 50°C (Table 310.15(B)(1)). Bundling adjustment: 0.80 for 6 conductors (Table 310.15(C)(1)). Adjusted ampacity = 30A × 0.82 × 0.80 = 19.68A, approximately 20A.

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Final Adjusted Ampacity (CEC 2022)

After verifying exceptions and cross-references:

1. **Base Calculation**:  
   $ 30A \times 0.82 \times 0.80 = 19.68A $  

2. **Exception Review**:  
   - **Section 310.15(B)**: Confirms temperature correction method is valid.  
   - **Section 310.15(C)(1)**: Bundling adjustment applies as written (no exception for THHN).  
   - No exceptions override the calculation for this scenario.  

**Final Answer**: **19.68 amperes**  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 310.15

**Response Time:** 12.2s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## California Electrical Code (CEC 2022) Requirement for AFCI Protection in Bedrooms and Living Areas

### **Why AFCI is Required**  
Under **CEC 210.12**, arc-fault circuit interrupter (AFCI) protection is mandated for **15A and 20A branch circuits** in dwelling units supplying outlets in:  
- Bedrooms  
- Living rooms  
- Hallways  
- Closets  
- Laundry areas  
- Similar spaces  

This requirement aligns with the **NEC** but is enforced in California per the CEC. The primary purpose is to **prevent electrical fires caused by arc faults**, which can occur due to damaged wiring, loose connections, or faulty devices.  

---

### **Electrical Hazard Prevented**  
AFCI protection targets **dangerous arcing faults** that standard circuit breakers cannot detect. Arcs can:  
- Generate extreme heat (up to 10,000°F), igniting nearby combustibles (e.g., bedding, curtains, furniture).  
- Occur in hidden locations (e.g., wall cavities, electrical boxes).  

---

### **Key CEC Exceptions**  
1. **Fire alarm systems**: AFCI is not required for circuits supplying fire alarm systems installed per **760.41(B)** or **760.121(B)**, provided wiring is in metal raceways or listed cables (CEC 210.12 Exception).  
2. **Short wiring extensions**: No AFCI required for branch circuit extensions ≤6 ft (1.8 m) without additional outlets (CEC 210.12(D) Exception).  
3. **Replacement receptacles**: Specific rules apply for replacing AFCI-protected outlets (CEC 406.4(D)(4)).  

---

### **Protection Methods**  
Per **CEC 210.12(A)**, AFCI protection can be achieved via:  
- **Combination-type AFCI** (most common).  
- **Branch/feeder-type AFCI** + outlet AFCI at the first outlet.  
- **System combination-type AFCI** (breaker + outlet device).  

---

### **California-Specific Notes**  
- CEC 2022 adopts NEC 2023 requirements without additional amendments for AFCI in dwelling units.  
- Exceptions and installation rules mirror NEC, with no unique California mandates for this section.  

✓ Sour...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 4 found
- 760.41, 406.4, 210.12, 760.121

**Response Time:** 12.7s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Torque Specifications for Conductor Termination (CEC 2022)  

Torque specifications ensure **secure, low-resistance connections** to prevent overheating, arcing, and equipment failure. The primary requirement is found in **CEC 110.14(D)**, with no applicable exceptions modifying this rule for general conductor termination scenarios.  

### Key Requirements:  
1. **Torque Values** (CEC 110.14(D)):  
   - Follow **manufacturer-specified torque values** on equipment or installation instructions.  
   - Use **approved methods** (torque tools, shear bolts, breakaway devices) to achieve the specified torque.  
   - *Informational Note*: Contact the manufacturer if torque values are not indicated.  

2. **Control Circuit Devices** (CEC 430.9(C)):  
   - Screw-type terminals with 14 AWG or smaller copper conductors must be torqued to a **minimum of 0.8 N·m (7 lb-in.)** unless marked otherwise.  

3. **Temperature Coordination** (CEC 110.14(C)):  
   - Conductor ampacity must not exceed the lowest temperature rating of any connected termination (e.g., 60°C or 75°C limitations).  

### Exceptions Review:  
- No exceptions from **cec_exception_search** directly modify 110.14(D) for general conductor termination.  
- Sections like **300.15**, **368.17**, **250.148**, and **215.2** address unrelated topics (boxes, overcurrent protection, grounding, feeders) and do not relax torque requirements.  

### Why Compliance Matters:  
- **Over-torquing** risks damaging terminals or insulation.  
- **Under-torquing** creates loose connections → heat → potential fire hazards.  
- Ensures compliance with **UL 486A-486B** and **NFPA 70B** maintenance standards.  

✓ Source: CEC 2022 Sections 110.14(D), 430.9(C)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 110.14, 250.148, 215.2, 430.9, 300.15, 368.17

**Response Time:** 13.6s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Service Load Calculation (CEC 2022) with Exceptions Considered

### Step 1: General Lighting Load  
**3 VA/sq ft × 3000 sq ft = 9000 VA**  
*(CEC Table 220.12 for general lighting load)*  

**Exception Check**:  
- **Section 220.12(B)** allows energy code values if monitoring systems are installed. Not applicable here (no monitoring system mentioned).  
- **Section 220.42** demand factors apply (residential use).  

---

### Step 2: Small Appliance & Laundry Circuits  
- **Small Appliance**: 2 circuits × 1500 VA = **3000 VA**  
- **Laundry**: 1 circuit × 1500 VA = **1500 VA**  
*(CEC 220.52)*  

---

### Step 3: Range Load  
**12 kW range → 8000 VA**  
*(CEC Table 220.55 demand factor for single range)*  

---

### Step 4: Dryer Load  
**5.5 kW dryer → 5500 VA**  
*(CEC 220.54: Use nameplate rating >5000 VA)*  

---

### Step 5: Central AC  
**4600 VA**  
*(Given: 19.2A × 240V = 4608 VA)*  

---

### Step 6: Apply Demand Factors  
**General Lighting + Small Appliance + Laundry**  
- **Total**: 9000 + 3000 + 1500 = **13,500 VA**  
- **Demand Factor**:  
  - First 3000 VA @ 100% = **3000 VA**  
  - Remaining 10,500 VA @ 35% = **3,675 VA**  
  - **Total Adjusted**: 3000 + 3675 = **6,675 VA**  
*(CEC 220.42)*  

---

### Step 7: Total Service Load  
**Total Load = 6,675 (adjusted) + 8,000 (range) + 5,500 (dryer) + 4,600 (AC) = 24,775 VA**  
**Convert to Amperes**:  
$$
\frac{24,775 \text{ VA}}{240 \text{ V}} = 103.23 \text{ A}
$$

---

### Step 8: Panel Sizing Check  
- **Calculated Load**: **103.23 A**  
- **Installed Panel**: **200 A**  

**Conclusion**:  
The 200A panel is **adequately sized** (103.23 A ≤ 200 A).  

**Exceptions Verified**:  
- No applicable exceptions override the calculation.  
- Demand factors and load assumptions align with CEC 2022 requirements.  

✓ Source: CEC 2022 Article 220

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 220.54, 220.55, 220.42, 103.23, 220.12, 220.52

**Response Time:** 25.7s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## Electrical Panel Inspection Violations (CEC 2022) – Final Answer

### 1. **Insufficient Working Space Depth**  
- **Measured**: 28 inches  
- **Required**: 3.5 feet (42 inches) for **Condition 2** (exposed live parts on one side and grounded parts on the other).  
- **Citation**: CEC Table 110.26(A)(1)  
- **Exception Check**:  
  - **110.26(E)** allows structural overhangs/roof extensions but **not foreign equipment** (e.g., water heater).  
  - **No applicable exception** permits reduced depth for this scenario.  

### 2. **Obstruction in Working Space**  
- **Issue**: Water heater located **16 inches** from panel (within 42-inch required depth).  
- **Citation**: CEC 110.26(A)(1) requires **clear working space** free of obstructions.  
- **Exception Check**:  
  - **110.26(E)(1)(a)** explicitly prohibits foreign equipment (e.g., water heater) in dedicated electrical space.  
  - **No exception** permits this obstruction.  

### 3. **Mounting Height Violation**  
- **Measured**: 5 feet (60 inches) from floor to panel bottom.  
- **Required**: **6.5 feet (78 inches)** for equipment ≤600V.  
- **Citation**: CEC 110.26(A)(2)  
- **Exception Check**:  
  - **110.26(A)(2) Exception No. 2** allows reduced height **only in existing dwellings** with service equipment ≤200A.  
  - **Not applicable** here (no indication of existing dwelling or 200A limit).  

---

### Summary of Violations  
- **Depth**: 28" < 42" (Condition 2)  
- **Obstruction**: Water heater within working space (violates 110.26(E))  
- **Height**: Panel mounted at 60" < 78"  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 18.6s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## Circuit Protection Requirements (NEC 2023 with CEC Exceptions Verified)

1. **Countertop Receptacles (20A circuits):**  
   - **Protection:** GFCI  
   - **Reference:** NEC 210.8(A)(6) requires GFCI for all 125V, 15- and 20A receptacles in kitchens.  
   - **Exception Check:** No exceptions apply to countertop receptacles under 210.8(A)(6).  

2. **Dishwasher (15A dedicated circuit):**  
   - **Protection:** GFCI  
   - **Reference:** If connected via a receptacle, GFCI applies under 210.8(A)(6).  
   - **Exception Check:** No exceptions apply to kitchen receptacles.  

3. **Garbage Disposal (15A dedicated circuit):**  
   - **Protection:** GFCI  
   - **Reference:** If supplied by a receptacle, GFCI is required (210.8(A)(6)).  
   - **Exception Check:** No exceptions apply to kitchen receptacles.  

4. **Refrigerator (20A dedicated circuit):**  
   - **Protection:** AFCI  
   - **Reference:** NEC 210.12(A) mandates AFCI for all dwelling unit branch circuits.  
   - **Exception Check:** No exceptions apply to refrigerators (GFCI not required).  

**Summary:**  
- **GFCI:** Countertop receptacles, dishwasher, garbage disposal (if on receptacles).  
- **AFCI:** Refrigerator.  

✓ Source: NEC 2023 and CEC 2022 exceptions verified.

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 210.8, 210.12

**Response Time:** 15.9s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## Revised Analysis with Exceptions Considered

After reviewing exceptions to CEC 250.4, **no exceptions apply** to the specific violations identified in the subpanel configuration. The key rules remain unchanged:

### **Critical Exceptions Checked**
1. **CEC 250.54 (Auxiliary Grounding Electrodes)**  
   - Permits connecting auxiliary electrodes to equipment grounding conductors but **does not allow bonding neutrals and grounds** in subpanels.  
   - **Irrelevant to the violations** (neutral/ground bonding and enclosure connections).

2. **CEC 250.25 (Supply-Side Grounding)**  
   - Applies to systems connected on the supply side of the service disconnect (e.g., utility equipment).  
   - **Not applicable** to the detached garage subpanel scenario.

---

### **Final Violations and Corrections**
1. **Neutral and Ground Bars Bonded**  
   - **Violation**: CEC 250.4(A)(3) requires **separate neutrals and grounds** in subpanels.  
   - **Correction**: Install an **insulated neutral bar** with no connection to the ground bar or enclosure.

2. **Neutral Bar Bonded to Enclosure**  
   - **Violation**: CEC 250.104(A) prohibits this in subpanels.  
   - **Correction**: Remove the bond. Neutral bar must only connect to the **feeder neutral conductor**.

3. **Ground Bar Bonded to Enclosure**  
   - **Violation**: Creates redundant paths if not done via a **single main bonding jumper** (CEC 250.102(B)).  
   - **Correction**: Bond the ground bar to the enclosure using a **listed bonding jumper** (e.g., green screw or wire).

4. **Missing Separate Grounding Electrode**  
   - **Violation**: CEC 250.32(B) requires a **separate grounding electrode** (e.g., ground rod) at detached structures.  
   - **Correction**: Install a **4.5m (15 ft) ground rod** bonded to the subpanel’s ground bar via a 6 AWG copper conductor (CEC 250.66).

---

### **Correct Configuration Summary**
| Component          | Connection                                  | Code Reference         |
|--------------...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 250.104, 250.66, 250.54, 250.102, 250.32, 250.25, 250.4

**Response Time:** 13.5s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**
## Final Answer: Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Code Verification with Exceptions Checked:**  
After reviewing exceptions to CEC 300.15 (conduit fill rules), **no exceptions apply** to this specific calculation for RMC with 10 AWG THHN conductors. The returned exceptions relate to:  
- RTRC permitted uses (Section 355.10)  
- Box/conduit body requirements (Section 300.15)  
- Service-entrance conductor protection (Section 230.50)  
- Outside wiring methods (Section 225.10)  

None of these exceptions modify the 40% fill limit or conduit fill calculations for **rigid metal conduit (RMC)** with THHN conductors.  

**Final Calculation:**  
- **Maximum Conductors:** 28 (based on 40% fill of 1¼" RMC)  
- **Requested Conductors:** 3 (4.1% fill, well within limits)  

✓ **Source:** CEC 2022 Chapter 9 Tables 4 and 5  
✓ **Exceptions Checked:** No applicable exceptions found for this scenario.

**Tool Usage:**
- CEC Tools: cec_lookup_conduit_fill, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 225.10, 355.10, 230.50, 300.15

**Response Time:** 16.7s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**
## Final Answer: Voltage Drop Compliance Check

**Voltage Drop Calculation:**
- **Voltage drop:** 2.84 volts (2.36% of 120V)
- **NEC 210.19(A)(1):** ✅ Meets 3% maximum recommendation
- **CEC 2022 Section 647.4(D):** ⚠️ **Exceeds 1.5% limit for fixed equipment** (2.36% > 1.5%)

**Exception Analysis:**
- No applicable exceptions found for **CEC 647.4(D)** voltage drop requirements
- Exceptions referenced in search results apply to unrelated sections (300.15, 368.17, etc.)

**Code Compliance Summary:**
1. **NEC-compliant:** ✅ 2.36% < 3% (acceptable for general branch circuits)
2. **CEC-compliant:** ❌ 2.36% > 1.5% (fails California's stricter fixed equipment requirement)

**Recommendation:**
- Use **10 AWG copper conductors** (1.02 Ω/1000ft) to reduce voltage drop:
  $$
  VD = 2 \times 22A \times 1.02\Omega \times \left(\frac{50}{1000}\right) = 2.24V \, (1.87\%)
  $$
  This meets both NEC and CEC 647.4(D) requirements.

✓ Source: CEC 2022 Section 647.4(D) and NEC 210.19(A)(1)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 647.4, 368.17, 210.19, 300.15

**Response Time:** 18.1s

---

### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Final Adjusted Ampacity with Exception Check (CEC 2022)

After reviewing exceptions for **CEC 310.16** (temperature correction and bundling adjustment), **no applicable exceptions** modify the calculation for this scenario. Key findings:

1. **Section 440.6** (refrigerant motor-compressors) and **Section 427.45** (ferromagnetic envelope conductors) are unrelated to general ampacity adjustments.
2. **Section 310.15** confirms the methodology (temperature/bundling factors) but does not override the calculation.
3. No exceptions relax the requirement to apply both correction factors.

---

### Final Calculation:
$$
\text{Adjusted Ampacity} = 20A \times 0.71 \times 0.80 = 11.36A
$$

**Answer**:  
**11.36 amperes** after applying temperature correction (0.71) and bundling adjustment (0.80) per CEC 2022 Tables 310.16, 310.15(B)(1)(1), and 310.15(C)(1).  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 440.6, 310.16, 310.15, 427.45

**Response Time:** 10.9s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Sizing (CEC 2022)

For **4 × 250 kcmil copper service conductors** (total 1000 kcmil per phase), the minimum **copper GEC** is:

✓ **3/0 AWG** (per CEC Table 250.66, Column "Copper")

**Calculation:**
- Total service conductor size = 4 × 250 kcmil = **1000 kcmil**
- Table 250.66 shows:
  - 600 kcmil → 1/0 AWG
  - **1100 kcmil → 3/0 AWG**
- Since 1000 kcmil is between 600 and 1100 kcmil, **use the next larger size (3/0 AWG)**

**Exception Review:**
- No exceptions in CEC 2022 modify Table 250.66 for parallel conductors
- 250.66(A)-(C) only apply to specific electrode types (rods, concrete-encased, ground rings), not conductor sizing
- 250.30(A)(6)(b) confirms GEC sizing per Table 250.66 for parallel systems

✓ Source: CEC 2022 Table 250.66

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 250.66, 250.30

**Response Time:** 10.6s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 28/28
- **Success Rate**: 100.0%
- **Average Response Time**: 13.1s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

