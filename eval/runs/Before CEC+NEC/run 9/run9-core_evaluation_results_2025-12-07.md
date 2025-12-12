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
| **Total Duration** | 374.7s |
| **Avg per Question** | 13.4s |

---

## Results by Question


## Baseline

### baseline-001: table_lookup

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected:** 20 amperes

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## 12 AWG Copper Conductor Ampacity (CEC 2022)  

**Ampacity**: **25 amperes** at 75°C termination  
**Source**: CEC 2022 Table 310.16 (California amendment applies)  

### Key Notes:  
1. **Overcurrent Protection**:  
   - Per **CEC 240.4(D)**, 12 AWG copper conductors **must be protected at 20A maximum**, even though the ampacity is 25A. This aligns with NEC 240.4(D).  

2. **Exceptions Checked**:  
   - **Section 310.12** (dwelling services/feeders) does not apply here, as the question does not involve single-phase dwelling services or feeders.  
   - **Section 330.112** (insulation types) is unrelated to ampacity calculations for this scenario.  
   - No other exceptions override the base value in Table 310.16 for this conductor size/temperature.  

3. **California Amendment**:  
   - The California amendment to Table 310.16 does not alter the 25A value for 12 AWG copper at 75°C.  

---
## NEC 2023 Reference  
No difference from NEC 2023 Table 310.16. NEC 240.4(D) also limits 12 AWG copper to 20A overcurrent protection.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 240.4, 310.16, 330.112, 310.12

**Response Time:** 11.9s

---

### baseline-002: table_lookup

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Expected:** 6 AWG copper

**CEC Ref:**  | **NEC Ref:** Table 310.16

**Status:** PASS

**Agent Answer:**
## Conductor Size for 60A Circuit (CEC 2022)

**Required conductor size:** **6 AWG copper**  
- **Ampacity:** 65A (CEC Table 310.16, 75°C column)  
- **Minimum requirement met:** 65A ≥ 60A  

**Overcurrent Protection (CEC 240.4(D)):**  
- **Maximum overcurrent protection:** 70A for 6 AWG copper (65A ampacity)  
- **Permitted:** 60A breaker (load) with 70A overcurrent device (protects conductor)  

**Table Verification:**  
From CEC Table 310.16:  
- **6 AWG copper** at 75°C = **65A**  
- **8 AWG copper** at 75°C = **50A** (insufficient for 60A)  

**Code Compliance:**  
- Section 310.15(B) applies for ambient temperature corrections (not needed here).  
- Section 310.15(C)(1) applies for bundling adjustments (not needed here).  
- **Section 240.4(D):** Permits 70A overcurrent protection for 6 AWG copper (65A ampacity).  

---
## NEC 2023 Reference  
No difference from NEC 2023 (NEC Table 310.16 and 240.4(D) also specify 65A for 6 AWG copper at 75°C with 70A protection).  

✓ Sources: CEC 2022 Table 310.16 & 240.4(D) (primary), NEC 2023 (comparison)  

**Exception Check:**  
No exceptions in CEC 2022 modify Table 310.16 or 240.4(D) for this application.

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_exception_search, cec_lookup_table, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 240.4, 310.15, 310.16

**Response Time:** 16.1s

---

### baseline-003: knowledge_simple

**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection in Residential Kitchens (CEC 2022)  

Ground-fault circuit-interrupter (GFCI) protection is **required for all 125-volt through 250-volt receptacles in kitchens** that serve countertop surfaces, as specified in **CEC 2022 Section 210.8(A)(6)**.  

### Key Requirements:  
1. **Countertop Receptacles**  
   - All receptacles installed to serve countertop surfaces must have GFCI protection.  
   - Applies to receptacles within **6 feet (1.8 meters)** of the countertop edge.  

2. **Small-Appliance Branch Circuits**  
   - The two or more 20-ampere small-appliance branch circuits required in kitchens (per **210.52(B)(1)**) must supply countertop receptacles, which are explicitly included in the GFCI protection mandate.  

---

### Exceptions Checked:  
- **210.52(A)(Exception 1/2):** Allow additional receptacles for specific appliances or clocks but do **not exempt** GFCI protection for countertop circuits.  
- **210.52(C):** Specifies spacing and placement for countertop receptacles but **does not override** the GFCI requirement in 210.8(A)(6).  
- **210.50 & 210.21:** Address receptacle installation height and ratings but **do not provide exceptions** for GFCI protection.  

---

## NEC 2023 Reference  
No difference from NEC 2023. Both codes require GFCI protection for kitchen countertop receptacles under similar provisions (NEC 210.8(A)(6)).  

✓ **Sources**: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 210.8, 210.21, 210.50, 210.52

**Response Time:** 8.9s

---

### baseline-004: knowledge_simple

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Expected:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## AFCI Protection for Bedroom Circuits (CEC 2022)

**Yes**, AFCI protection is required for bedroom circuits in new residential construction in California. 

Per **CEC 2022 Section 210.12(A)**, all 120-volt, 15- and 20-ampere branch circuits in dwelling units (including bedrooms) must have AFCI protection. The exceptions searched (210.70, 210.11, 210.22, 210.52) do not provide any exemptions for bedroom circuits regarding AFCI requirements. 

**Key Findings**:
- No exceptions in CEC 2022 exempt bedrooms from AFCI protection.
- The primary rule in 210.12(A) applies directly to bedrooms as listed locations.
- Exceptions relate to lighting, receptacle placement, and branch circuits but do not override AFCI mandates.

---
## NEC 2023 Reference
No difference from NEC 2023. NEC 2023 also requires AFCI protection for bedrooms per 210.12(A).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 210.70, 210.11, 210.22, 210.52, 210.12

**Response Time:** 9.0s

---

### baseline-005: table_lookup

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Expected:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**CEC Ref:**  | **NEC Ref:** Table 310.12

**Status:** PASS

**Agent Answer:**
## Aluminum Conductors for 200A Service (CEC 2022) **Final Answer**

**Yes**, aluminum conductors are permitted for a 200A service in California. The required size is:

✓ **4/0 AWG aluminum**  
- Based on **CEC Table 310.12(A)** for single-phase dwelling services  
- 75°C temperature rating assumed (standard for service conductors)  
- Minimum size requirement from **CEC 310.3(B)** (aluminum allowed with 12 AWG minimum for general conductors)

**Exception Analysis:**  
- **CEC 310.3(A)** confirms 12 AWG is the minimum aluminum size for general conductors, but **Table 310.12(A)** specifically governs service conductors and permits 4/0 AWG for 200A services.  
- **CEC 310.12(A)** explicitly allows aluminum for dwelling services when sized per the table.  
- No exceptions in the returned results prohibit aluminum use for 200A services.

---
## NEC 2023 Reference  
No difference from NEC 2023 – aluminum service conductors are permitted at 4/0 AWG for 200A (NEC Table 310.12(A)).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_lookup_conductor_size, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.3, 310.12

**Response Time:** 10.5s

---

### baseline-006: knowledge_simple

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Working Clearance Depth (CEC 2022)

The minimum working clearance depth required in front of a 120/240V residential electrical panel is **900 mm (3 feet)** per **CEC 2022 Table 110.26(A)(1)**. This applies to:

- **Voltage range**: 0–150 volts to ground  
- **Condition 1**: Exposed live parts on one side of the working space with no live/grounded parts on the other side, or both sides effectively insulated  

---

### Exceptions Verified:
1. **Low-voltage exception** (110.26(A)(1)(b)):  
   - **Does not apply** (120/240V exceeds 30V).  
2. **Existing dwelling height exception** (110.26(A)(3) Exception 2):  
   - **Applies to height**, not depth.  
3. **Dedicated space rules** (110.26(E)):  
   - No impact on minimum depth requirement.  

---

### NEC 2023 Reference  
No difference from NEC 2023 Table 110.26(A)(1).  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 7.9s

---

### baseline-007: knowledge_simple

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Expected:** Minimum of two 20-ampere small appliance branch circuits

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1)

**Status:** PASS

**Agent Answer:**
## Minimum Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Answer:**  
A kitchen must have **at least two 20-ampere small appliance branch circuits** to serve countertop and small appliance loads.  

**Code Basis:**  
- **CEC 210.52(B)(1):** Mandates "not fewer than two small-appliance branch circuits" for kitchens.  
- **CEC 210.11(C)(1):** Requires "two or more 20-ampere small-appliance branch circuits" for dwelling units.  

**Exceptions Checked:**  
1. **Exception No. 1 (210.52(B)(1)):** Allows additional switched receptacles on general-purpose circuits but does not reduce the two-circuit minimum.  
2. **Exception No. 2 (210.52(B)(1)):** Permits specific appliances (e.g., refrigerators) on individual circuits but does not affect the two-circuit requirement.  
3. **Cross-reference to 210.11(C)(1):** Confirms the two-circuit minimum applies to all dwelling units.  

**No Valid Exceptions Reduce the Minimum Requirement.**  

---
## NEC 2023 Reference  
No difference from NEC 2023. Both codes require **at least two 20A small appliance branch circuits** for kitchens.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)  

**Verification:**  
- CEC 210.52(B)(1) explicitly states the **minimum of two circuits**.  
- NEC 210.52(B)(1) mirrors this requirement.  
- No California-specific amendments alter this requirement.

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.11

**Response Time:** 10.4s

---

### baseline-008: knowledge_simple

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Expected:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is **required** for a new 200A residential service under the **California Electrical Code (CEC) 2022**, aligning with NEC 2023.  

**Key CEC Section:**  
- **CEC 230.67(A)** mandates that *all services supplying dwelling units* must include a **surge-protective device (SPD)**.  

**Exceptions Checked:**  
- No exceptions in CEC 2022 remove this requirement for residential services.  
- **Exception 230.67(B)** allows SPD placement downstream (not in service equipment), but does not exempt installation.  

**Placement Requirements:**  
- The SPD must be installed **in or adjacent to the service equipment** (CEC 230.67(B)).  
- If not in service equipment, it must be at the next level of distribution downstream (Exception to 230.67(B)).  

**Conclusion:**  
Surge protection is **mandatory** for residential services in California, with no applicable exemptions for standard 200A dwelling unit installations.  

---  
## NEC 2023 Reference  
No difference from NEC 2023.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 1 found
- 230.67

**Response Time:** 22.2s

---


## Core

### core-001: multi_article

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted for service conductors per Table 310.12.

**CEC Ref:**  | **NEC Ref:** Table 310.12, 310.12

**Status:** PASS

**Agent Answer:**
## Service Conductor Sizing (CEC 2022)

✓ **Copper service conductors**: 2/0 AWG (Table 310.12(A) for 200A dwelling service)  
✓ **Aluminum service conductors**: 4/0 AWG (same table, aluminum column)  

**Key Requirements:**  
1. **Permissibility of Aluminum**:  
   - Aluminum is allowed per **CEC 310.3(B)** for service conductors.  
   - Minimum size for aluminum is **4/0 AWG** to meet 200A rating (Table 310.12(A)).  

2. **Material-Specific Provisions**:  
   - **CEC 110.5** confirms aluminum/copper-clad aluminum is permitted, with size adjustments required.  
   - **CEC 310.3(A)** establishes 12 AWG as minimum aluminum size for general conductors, but **Table 310.12(A)** overrides this for service conductors.  

3. **Installation Considerations**:  
   - Aluminum conductors must comply with **CEC 310.12(A)** derating rules if temperature corrections or bundling apply (not needed here).  
   - No exceptions restrict aluminum use in dwelling services (verified via exception search).  

---
## NEC 2023 Reference  
No difference from NEC 2023 - Table 310.12(A) is identical in both codes for dwelling services.

✓ Sources: CEC 2022 Table 310.12(A), NEC 2023 Table 310.12(A)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_size, cec_lookup_conductor_size, cec_exception_search, cec_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 110.5, 310.3, 310.12

**Response Time:** 16.8s

---

### core-002: multi_article

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Expected:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). Common trip is required if the circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and not switched. Conductors must be grouped per 210.4(D). Circu...

**CEC Ref:**  | **NEC Ref:** 210.4, 210.4(B), 210.4(D)

**Status:** PASS

**Agent Answer:**
## Multiwire Branch Circuit Requirements (CEC 2022) with Exceptions

### Circuit Breaker Requirements:
1. **Two-pole breaker or handle ties** (CEC 210.4(B)):
   - Must **simultaneously disconnect all ungrounded conductors** (hot wires) at the panel.
   - For 12 AWG copper conductors, the breaker must be **20 amperes** (per CEC 240.4(D)(3)).

2. **Handle ties required** for single-pole breakers:
   - Single-pole breakers must be **physically tied together** to ensure both hot legs open simultaneously during overcurrent.

### Neutral Termination Requirements:
1. **Neutral conductor continuity** (CEC 210.4(D)):
   - The neutral conductor **must not be switched or interrupted**.
   - Must terminate directly to the **neutral bus** in the panel without splices or taps (unless sized for full load).

2. **Neutral sizing**:
   - For 12 AWG copper conductors, the neutral must also be **12 AWG** (same size as hots) to carry unbalanced current.

3. **No shared neutrals with other circuits**:
   - The neutral conductor is **dedicated to this MWBC** and cannot serve other circuits (per 210.4(D)).

### Exceptions Considered:
- **Exception 210.4(C)**: Allows line-to-line loads if all ungrounded conductors are opened simultaneously. *Not applicable here* (kitchen receptacles are line-to-neutral loads).
- **Exception 200.4(B)**: Permits ungrouped neutrals in specific cases (e.g., unique raceways). *Not applicable here* (neutral is dedicated and grouped).

---
## NEC 2023 Reference
No difference from NEC 2023. CEC 2022 aligns with NEC 2023 for multiwire branch circuit requirements.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 210.4, 240.4, 200.4

**Response Time:** 16.2s

---

### core-003: nec_2023_updates

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**CEC Ref:**  | **NEC Ref:** 210.8(A)

**Status:** PASS

**Agent Answer:**
## GFCI Protection Requirements in Residential Dwellings (CEC 2022 with Exceptions)

### **Required Locations (CEC 2022 Section 210.8(A))**
GFCI protection is **required** for all 120–250V receptacles in these residential locations:
1. **Bathrooms**  
2. **Garages/accessory buildings** (non-habitable, floor at/above grade)  
3. **Outdoors**  
4. **Crawl spaces** (at/above grade)  
5. **Basements**  
6. **Kitchens** (countertop surfaces)  
7. **Within 6 ft of sinks** (food prep/cooking areas)  
8. **Within 6 ft of bathtubs/showers**  
9. **Laundry areas**  
10. **Indoor damp/wet locations**  

---

### **Exceptions (CEC 2022)**
GFCI **not required** in these specific cases:
1. **Dedicated circuits for snow-melting/deicing systems** (per 426.28/427.22).  
2. **Receptacles for fire alarm/burglar alarm systems** (permanent installations in basements).  
3. **Listed locking support receptacles** for ceiling fans/luminaires (no GFCI if not general-purpose).  
4. **Industrial-grade installations** (qualified personnel, assured grounding program) – **not applicable to typical residences**.  
5. **Healthcare facilities** (see 517.21) – **not typical residential**.  

---

### **Key Notes**
- **Distance measurement**: From receptacle to sink/bathtub edge via shortest path (no piercing barriers).  
- **Ceiling fan/luminaire exceptions**: Only apply to dedicated support receptacles, not general-use outlets.  

---

### **NEC 2023 Comparison**
No significant differences from NEC 2023. California aligns with NEC requirements for residential GFCI, with additional clarifications in exceptions (e.g., alarm systems, ceiling fan receptacles).  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 4 found
- 427.22, 210.8, 426.28, 517.21

**Response Time:** 17.0s

---

### core-004: nec_2023_updates

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**CEC Ref:**  | **NEC Ref:** 230.67

**Status:** PASS

**Agent Answer:**
## Surge Protection Requirement (CEC 2022)  

**Requirement**: Surge protection is **required** for all services supplying dwelling units per **CEC 2022 Section 230.67(A)**.  

**Installation Locations**:  
1. **Integral to service equipment** (main panel)  
2. **Immediately adjacent** to the service equipment  
3. **Exception**: May be installed at **downstream distribution equipment** if:  
   - Located "at each next level distribution equipment toward the load" (CEC 230.67(B) Exception).  

**Type Required**: Type 1 or Type 2 SPD (per CEC 230.67(C)).  

---  
## NEC 2023 Reference  
NEC 2023 **does not explicitly require** surge protection for dwelling units in 230.67. California's CEC 2022 adds this mandate through Section 230.67.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 230.67

**Response Time:** 7.4s

---

### core-005: edge_cases

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 1...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 240.24(D), 110.26(B)

**Status:** PASS

**Agent Answer:**
## Working Space Requirements (CEC 2022)

The installation **does not meet CEC requirements** due to insufficient working space in front of the panel:

1. **Front Clearance Requirement**:  
   For 240V systems (condition 1), **36 inches (3 ft)** of clear working space is required in front of the panel (CEC Table 110.26(A)(1)).  
   → **Actual clearance**: 24 inches (❌ insufficient).

2. **Exceptions Checked**:  
   - **CEC 110.26(E)**: Requires dedicated electrical space (6 ft height zone) but does **not reduce** the 36-inch front clearance requirement.  
   - **CEC 410.16**: Applies to luminaires in closets, not panel clearances.  
   - **CEC 110.70**: Pertains to enclosures for personnel entry, not applicable here.

3. **Side Clearance**:  
   The 18-inch distance to the water heater is **not regulated** by CEC 110.26 for lateral clearance, but the **front clearance remains the critical failure**.

---

## NEC 2023 Reference  
No difference from NEC 2023.  

✓ Sources: CEC 2022 Table 110.26(A)(1) (primary), NEC 2023 Table 110.26(A)(1) (comparison)

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 3 found
- 410.16, 110.26, 110.70

**Response Time:** 8.7s

---

### core-006: edge_cases

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Expected:** Yes, this is a code violation per 110.14(A). Terminals shall accommodate only one conductor unless identified for more than one conductor. Per 110.3(B), equipment must be installed according to manufacturer instructions. If the breaker is not listed for two conductors, this is a violation.

**CEC Ref:**  | **NEC Ref:** 110.14(A), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Multiple Conductors on a Single Breaker Terminal (CEC 2022)

This is a **code violation** under CEC 2022. Here's the analysis:

1. **Primary Rule**:  
   **CEC 408.41** requires each grounded conductor to terminate in an **individual terminal** unless the terminal is explicitly identified for multiple conductors (e.g., parallel conductors). Standard 20A breaker terminals are **not marked** for two conductors.

2. **Exception Check**:  
   The exception in **408.41** permits multiple conductors on a single terminal **only for parallel conductors** (e.g., multiwire branch circuits with a shared neutral). This scenario does **not involve parallel conductors**, so the exception does **not apply**.

3. **Equipment Labeling**:  
   Per **CEC 110.3(B)**, equipment must be used in accordance with its labeling. Since the breaker terminal is **not marked** for two conductors, this installation violates the equipment's approved usage.

4. **NEC 2023 Reference**:  
   NEC 2023 aligns with CEC 2022. **NEC 408.41** and **NEC 110.3(B)** prohibit this practice unless the terminal is listed for multiple conductors.

---

**Corrective Action**:  
- Use a **breaker with a terminal marked for two conductors** (e.g., "2-wire" or "2-conductor" labeled terminals).  
- Alternatively, use a **junction box** to split the two conductors before connecting to separate terminals.  

**Sources**: CEC 2022 Sections 110.3(B), 408.41; NEC 2023 Sections 110.3(B), 408.41.

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 408.41, 110.3

**Response Time:** 11.1s

---

### core-007: grounding_bonding

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Expected:** Grounds and neutrals must be SEPARATED in the subpanel. The 4-wire feeder includes 2 hot, 1 neutral, and 1 equipment grounding conductor. NO main bonding jumper in subpanel (only at service). Neutral bar must be isolated (not bonded to enclosure). Equipment grounding conductor must be bonded to encl...

**CEC Ref:**  | **NEC Ref:** 250.32, 250.24(A)(5), 408.40

**Status:** PASS

**Agent Answer:**
## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)  

### Configuration Requirements:  
1. **Equipment Grounding Conductor (EGC):**  
   - Run with the 4-wire feeder and connected to the **grounding bar** in the garage subpanel.  
   - Size per **Table 250.122** based on the overcurrent protection rating (e.g., 100A feeder → 8 AWG copper).  

2. **Grounding Electrode Conductor (GEC):**  
   - Connect the **grounding bar** in the subpanel to a **local grounding electrode** (e.g., ground rod).  
   - Size per **Table 250.66** based on the largest ungrounded conductor in the feeder (e.g., 3/0 AWG feeder → 4 AWG copper GEC).  

3. **Neutral and Ground Separation:**  
   - **Bond** the neutral and ground bars in the subpanel (per **250.32(B)(1)**).  
   - **Do not connect** the neutral bar to the grounding electrode in the subpanel (per **250.24(A)(5)**).  

4. **Bonding Jumper:**  
   - Install a **supply-side bonding jumper** from the feeder’s source to the subpanel’s grounding system (per **250.30(B)(3)**).  

---

### Exceptions and Key Notes:  
- **Exception 250.32(B)(1) Exception No. 1:**  
  Allows use of a grounded conductor as a ground-fault return path **only if**:  
  - No equipment grounding conductor is present.  
  - No continuous metallic paths exist between buildings.  
  - No ground-fault protection is installed.  
  **Not applicable here** since the feeder includes an EGC.  

- **Exception 250.32(B)(1) Exception No. 2:**  
  Permits connecting the feeder’s grounded conductor to the grounding electrode **only if** system bonding jumpers are installed per **250.30(A)(1)**.  
  **Not applicable** in standard detached garage installations.  

- **250.24(A)(5):**  
  Prohibits connecting the grounded conductor (neutral) to the grounding electrode on the load side of the service disconnect.  
  **Critical** to prevent neutral-to-ground bonds in the subpanel.  

---

### NEC 2023 Reference  
No difference from NEC 2023.  

✓ **Sources:** CEC 2022...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 250.32, 250.66, 250.30, 250.122, 250.24

**Response Time:** 15.4s

---

### core-008: grounding_bonding

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Expected:** Main Bonding Jumper (MBJ): Located at SERVICE EQUIPMENT, connects grounded conductor (neutral) to equipment grounding conductor. Required at service disconnect per 250.28. System Bonding Jumper (SBJ): Located at SEPARATELY DERIVED SYSTEMS (transformers, generators), same function as MBJ but for SDS....

**CEC Ref:**  | **NEC Ref:** Article 100, 250.28, 250.30

**Status:** PASS

**Agent Answer:**
## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022) with Exceptions

---

### **Definitions**
1. **Main Bonding Jumper**  
   - **Location**: At the **service equipment**.  
   - **Purpose**: Bonds the **grounded conductor (neutral)** to the **equipment grounding conductor (EGC)** or supply-side bonding jumper.  
   - **Citation**: CEC 2022 Section 100 (Bonding Jumper, Main).  

2. **System Bonding Jumper**  
   - **Location**: At a **separately derived system** (e.g., transformer, generator).  
   - **Purpose**: Bonds the **grounded conductor** to the **supply-side bonding jumper** or EGC.  
   - **Citation**: CEC 2022 Section 100 (Bonding Jumper, System).  

---

### **Key Differences**
| Feature                  | **Main Bonding Jumper**                          | **System Bonding Jumper**                          |
|--------------------------|---------------------------------------------------|----------------------------------------------------|
| **Location**             | Service equipment (service entrance).           | Separately derived system (e.g., transformer).     |
| **Required By**          | **CEC 250.28** (Service Grounding).             | **CEC 250.30(A)(1)** (Separately Derived Systems). |
| **Material**             | Copper, aluminum, or corrosion-resistant material. | Same as main bonding jumper.                       |
| **Sizing**               | Per Table 250.102(C)(1).                        | Per Table 250.102(C)(1).                          |

---

### **Exceptions and Special Cases**
#### **Main Bonding Jumper (CEC 250.28)**
1. **Material/Construction**:  
   - May be a **screw** with a **green finish** (visible when installed).  
   - **Exception 250.28(B)**.  

2. **Multiple Enclosures**:  
   - For services with **multiple enclosures**, the main bonding jumper for each enclosure is sized based on the **largest ungrounded service conductor** serving that enclosure.  
   - **Exception 250.28(D)(2)**.  

3. **Impedance Grounded S...

**Tool Usage:**
- CEC Tools: cec_search, cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 5 found
- 250.102, 250.36, 250.28, 250.30, 250.24

**Response Time:** 12.1s

---

### core-009: load_calculations

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Expected:** Minimum of TWO 20-ampere circuits required per 210.11(C)(1). Yes, these circuits can and should serve dining room, pantry, and breakfast room receptacles. They cannot serve lighting outlets or receptacles outside these areas.

**CEC Ref:**  | **NEC Ref:** 210.11(C)(1), 210.52(B)

**Status:** PASS

**Agent Answer:**
## Small Appliance Branch Circuit Requirements (CEC 2022)

1. **Minimum Required Circuits**:  
   **Two or more 20-ampere small-appliance branch circuits** are required for all receptacle outlets in kitchens, including countertop surfaces, wall/floor receptacles, and refrigeration equipment (CEC 210.11(C)(1), 210.52(B)(1)).

2. **Dining Room Receptacles**:  
   These circuits **can serve dining room receptacles** as permitted by CEC 210.52(B)(3). The small-appliance branch circuits may supply receptacles in the kitchen and **other rooms** listed in 210.52(B)(1) (e.g., dining rooms, family rooms).  
   **Limitation**: No small-appliance branch circuit shall serve more than **one kitchen**.

---
## NEC 2023 Reference  
No difference from NEC 2023. The requirement for two 20A small-appliance circuits in kitchens and their permitted use in dining rooms is identical in NEC 2023 (NEC 210.52(B)).

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.52, 210.11

**Response Time:** 8.6s

---

### core-010: load_calculations

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Expected:** Base ampacity: 30A at 90°C (Table 310.16). Temperature correction factor: 0.82 for 50°C (Table 310.15(B)(1)). Bundling adjustment: 0.80 for 6 conductors (Table 310.15(C)(1)). Adjusted ampacity = 30A × 0.82 × 0.80 = 19.68A, approximately 20A.

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1)

**Status:** PASS

**Agent Answer:**
## Final Answer with Exceptions Considered

After reviewing exceptions in CEC 2022 Section 310.15, the adjusted ampacity calculation remains valid with the following considerations:

1. **Termination Temperature Limitation**  
   Per Exception 2 in 310.15, the corrected ampacity (15A) must not exceed the termination temperature rating. Since THHN is rated 75°C and typical breaker terminations are also 75°C, this requirement is satisfied.

2. **Bundling and Temperature Corrections Applied Correctly**  
   - Bundling adjustment (6 conductors): 0.80 (Table 310.15(C)(1))  
   - Temperature correction (50°C ambient): 0.75 (Table 310.15(B)(1))  
   - Both factors applied sequentially as required by 310.15(C)(1) and (B)(1)

3. **No California-Specific Exceptions Apply**  
   The [CEC] amendments in Table 310.16 do not override the standard derating procedure for this scenario.

**Final Adjusted Ampacity**: **15.0 amperes**  

---
## NEC 2023 Reference  
No difference from NEC 2023 (same tables and factors apply).  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 310.16

**Response Time:** 16.4s

---

### core-011: why_questions

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Expected:** AFCI protection prevents electrical fires caused by arc faults. It detects arcing conditions that standard breakers cannot, including series arcing (broken/damaged wires), parallel arcing (line-to-line or line-to-ground), loose connections, damaged insulation, and deteriorated wire. Required per 210...

**CEC Ref:**  | **NEC Ref:** 210.12

**Status:** PASS

**Agent Answer:**
## Why CEC Requires AFCI Protection in Bedrooms and Living Areas (CEC 2022)

### **Requirement**
CEC 2022 **Section 210.12** mandates **Arc-Fault Circuit Interrupter (AFCI)** protection for all 120-volt, single-phase, 15- and 20-ampere branch circuits in:
- **Dwelling units**: Bedrooms, living rooms, hallways, closets, kitchens, and similar areas.
- **Dormitory units**: Bedrooms, living rooms, and similar spaces.
- **Guest rooms/hotel suites**: Guest rooms in hotels/motels.

This aligns with NEC 210.12 but includes California-specific enforcement through Title 24.

---

### **Electrical Hazard Prevented**
AFCI protection prevents **electrical fires caused by arc faults**, which occur due to:
- Damaged or degraded wiring
- Loose connections
- Overloaded circuits
- Improper use of extension cords

Standard circuit breakers do not detect arcs unless they cause overcurrent. AFCIs identify abnormal arcing patterns and interrupt the circuit to mitigate fire risk.

---

### **Key Exceptions in CEC 2022**
1. **Fire alarm systems** (Section 210.12, Exception):  
   - AFCI protection not required for circuits supplying fire alarm systems installed per **760.41(B)** or **760.121(B)**.  
   - Wiring must use metal raceway, MC cable, or equivalent per **250.118**.

2. **Arc welding equipment** (Exception to 210.12(D)):  
   - Exempt until January 1, 2025.

3. **Branch circuit modifications** (Section 210.12(D)):  
   - AFCI not required for extensions ≤ 1.8 m (6 ft) without additional outlets/devices.

4. **Supplemental protection systems**:  
   - Combination-type AFCIs (UL 1699) or outlet branch-circuit AFCIs (UL 1699A) permitted under specific installation conditions.

---

### **Cross-References and Notes**
- **UL Standards**:  
  - Combination-type AFCIs: UL 1699  
  - Outlet branch-circuit AFCIs: UL Subject 1699A  
- **Fire alarm power requirements**: See **760.41(B)** and **760.121(B)**.
- **Conduit/enclosure requirements**: Metal raceways or concrete-encased conduits per...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 4 found
- 210.12, 760.121, 760.41, 250.118

**Response Time:** 27.4s

---

### core-012: why_questions

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Expected:** Torque specifications prevent: (1) loose connections causing high resistance and heat generation (fire hazard), (2) poor contact leading to arcing, (3) overtightening causing crushed conductors or damaged terminals. Requirements found in 110.14(D) - must follow manufacturer specifications or Table 1...

**CEC Ref:**  | **NEC Ref:** 110.14(D), 110.3(B)

**Status:** PASS

**Agent Answer:**
## Torque Specifications for Conductor Terminations (CEC 2022)

Torque specifications are critical for conductor terminations because **improperly torqued connections can lead to overheating, arcing, and fire hazards**. Proper torque ensures:
- Low-resistance electrical connections
- Mechanical stability
- Compliance with safety standards

### CEC Requirements
While **CEC 2022 does not explicitly amend NEC 110.14(C)(D)**, it **inherits this requirement**. Key provisions include:
- **110.14(C)(D)**: Tightening torque values must follow **manufacturer's installation instructions**. Approved methods (e.g., torque tools, shear bolts) must be used to achieve specified torque values.
- **Informational Notes**:
  - Contact manufacturers if torque values are unspecified.
  - Refer to UL 486A-486B or NFPA 70B for guidance.

### Exceptions and Special Cases
1. **Equipment Markings**: If equipment is listed for higher temperature-rated conductors, those may be used (110.14(C)(1)(a/b)).
2. **Separate Connectors**: Pressure connectors must not exceed their listed temperature rating (110.14(C)(2)).

---
## NEC 2023 Reference
NEC 2023 retains **110.14(C)(D)** with added emphasis on torque specifications for **listed devices**. California follows this requirement without modification.

✓ Sources: CEC 2022 (inherited from NEC), NEC 2023

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.14

**Response Time:** 8.5s

---


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Service Load Calculation (CEC 2022) with Exceptions Verified

### Step 1: General Lighting Load  
- **3,000 sq ft × 3 VA/sq ft** = **9,000 VA**  
  *(CEC Table 220.12)*  
  **Exception Check**: 220.12(B) allows energy code adjustments with monitoring systems. **Not applicable** here (residential dwelling, no monitoring system mentioned).

### Step 2: Small Appliance Circuits  
- **2 circuits × 1,500 VA** = **3,000 VA**  
  *(210.52(B)(1))*  
  **Exception Check**: 220.52(A) permits excluding specific circuits. **Not applicable** (standard 2-circuit calculation used).

### Step 3: Laundry Circuit  
- **1 circuit × 1,500 VA** = **1,500 VA**  
  *(210.52(C)(1))*  
  **Exception Check**: 220.52(B) permits exclusion for specialized circuits. **Not applicable** (standard laundry circuit included).

### Step 4: Range Load (Demand Factor)  
- **12 kW range → 8,000 VA**  
  *(CEC Table 220.55, Column C for single range)*  
  **Exception Check**: No exceptions override standard range demand factors for single ranges.

### Step 5: Dryer Load  
- **5.5 kW dryer → 5,500 VA**  
  *(220.54: Use nameplate value if >5,000 VA)*  
  **Exception Check**: No exceptions apply to nameplate value usage.

### Step 6: Air Conditioner (Continuous Load)  
- **4,600 W × 1.25** = **5,750 VA**  
  *(220.18: Continuous loads require 125%)*  
  **Exception Check**: 220.40 allows demand factors but requires summing all loads. **Applied per standard method**.

---

### Total Load Calculation  
1. **General Lighting + Small Appliance + Laundry**  
   = 9,000 + 3,000 + 1,500 = **13,500 VA**  
   Apply demand factor:  
   - First 3,000 VA @ 100% = **3,000 VA**  
   - Remaining 10,500 VA @ 35% = **3,675 VA**  
   **Total = 6,675 VA**  
   *(220.53 Demand Factor)*  

2. **Appliance Loads**  
   = 8,000 (range) + 5,500 (dryer) + 5,750 (AC) = **19,250 VA**  

3. **Total Service Load**  
   = 6,675 + 19,250 = **25,925 VA**  

---

### Final Service Size  
- **25,925 VA ÷ 240V** = **108 A**  
  *(220.85 St...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 9 found
- 220.40, 220.52, 220.55, 220.12, 210.52, 220.85, 220.18, 220.53, 220.54

**Response Time:** 16.2s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## Electrical Panel Inspection Violations (Final Answer with Exceptions Checked)

**Confirmed Violations (No Applicable Exceptions Found):**

1. **Depth Clearance (110.26(A)(1))**  
   - **Measured:** 28 inches  
   - **Required:** 36 inches (3 ft) for 240V equipment (Condition 1)  
   - **Exception Check:** 110.26(E) allows structural overhangs but not foreign systems like water heaters.  
   - **Status:** **Violation remains** – Water heater is a foreign system without protection.  

2. **Obstruction in Working Space (110.26(B)(2))**  
   - **Issue:** Water heater located 16 inches from panel.  
   - **Exception Check:** 110.26(E) permits foreign systems *with protection* (e.g., leak barriers). No such protection is mentioned.  
   - **Status:** **Violation remains** – Storage/proximity of foreign systems violates rule.  

3. **Panel Height (110.26(A)(2))**  
   - **Measured:** 5 ft (60 in)  
   - **Required:** Minimum 6.5 ft (78 in) for service equipment.  
   - **Exception Check:** 110.26(A)(2) Exception No. 2 allows **existing** dwelling units ≤ 200A to have reduced height.  
     - **Not applicable here** if this is a new installation.  
   - **Status:** **Violation remains** – Height is insufficient.  

4. **Width Clearance (110.26(A)(1))**  
   - **Measured:** 30 inches ✅ *Compliant*  
   - **No exceptions needed** – Meets minimum width requirement.  

---

## NEC 2023 Reference  
No difference from NEC 2023. California adopts NEC 110.26 requirements without amendment.  

**✓ Sources:** CEC 2022 (primary), NEC 2023 (comparison)  

**Final Note:** All violations persist due to lack of applicable exceptions. Corrective actions required:  
- Increase depth clearance to 36 inches.  
- Relocate water heater ≥ 36 inches from panel or install protective barriers.  
- Raise panel to minimum 6.5 ft height.

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 13.6s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## Circuit Protection Requirements (NEC 2023 with CEC Exceptions Considered)

### 1. **Countertop Receptacles (2 x 20A circuits)**
- **Protection Required**: **Combination AFCI/GFCI breaker**
- **NEC References**: 
  - **210.8(A)(6)**: Kitchens require GFCI protection for all countertop receptacles.
  - **210.12(A)**: All dwelling unit branch circuits require AFCI protection.
- **CEC Exceptions**: No exceptions apply to protection requirements; 210.52(C) only addresses receptacle placement, not protection type.

### 2. **Dishwasher (15A dedicated circuit)**
- **Protection Required**: **Combination AFCI/GFCI breaker**
- **NEC References**: 
  - **210.8(A)(6)**: Applies to all kitchen receptacles, including appliances like dishwashers.
  - **210.12(A)**: Mandatory AFCI for all dwelling unit circuits.
- **CEC Exceptions**: No exceptions apply; 210.52(B)(1) allows dedicated circuits but does not exempt from GFCI/AFCI.

### 3. **Garbage Disposal (15A dedicated circuit)**
- **Protection Required**: **Combination AFCI/GFCI breaker**
- **NEC References**: 
  - **210.8(A)(6)**: Covers all kitchen receptacles, including garbage disposals.
  - **210.12(A)**: Requires AFCI for all dwelling unit circuits.
- **CEC Exceptions**: 210.52(B)(2) Exception No. 2 permits dedicated circuits but does not override GFCI/AFCI requirements.

### 4. **Refrigerator (20A dedicated circuit)**
- **Protection Required**: **Combination AFCI/GFCI breaker**
- **NEC References**: 
  - **210.8(A)(6)**: Refrigerators in kitchens require GFCI protection.
  - **210.12(A)**: All dwelling unit circuits must have AFCI protection.
- **CEC Exceptions**: No exceptions apply; 210.52(B)(1) includes refrigeration equipment in small-appliance circuits but does not exempt from protection.

---

## Key Notes:
- **Combination AFCI/GFCI breakers** are required for all circuits in dwelling units where both protections apply (kitchen circuits).
- **Exceptions in CEC 2022** (e.g., 210.52(C), 210.52(B)) pertain to **recepta...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 3 found
- 210.12, 210.8, 210.52

**Response Time:** 15.4s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## Subpanel Grounding and Bonding Violations (CEC 2022) – Final Answer

### **Confirmed Violations (No Exceptions Apply)**
1. **Neutral and Ground Bars Bonded**  
   - **Rule**: CEC 250.24(A)(5) explicitly prohibits connecting grounded (neutral) and grounding (equipment) conductors on the load side of the service disconnect.  
   - **Exceptions Checked**: No exceptions in CEC 250.24(A)(5) or related sections (e.g., 250.54, 250.25) permit neutral-ground bonding in subpanels.  

2. **Neutral Bar Bonded to Enclosure**  
   - **Rule**: CEC 250.4(B)(2) requires equipment grounding (not neutral) to connect to the enclosure. Bonding the neutral bar to the enclosure creates a parallel ground path.  
   - **Exceptions Checked**: Exceptions in 250.97 and 250.86 relate to raceway bonding, not subpanel neutral-enclosure connections.  

3. **Main Bonding Jumper Installed in Subpanel**  
   - **Rule**: CEC 250.24(B) restricts the main bonding jumper to the **main service panel**.  
   - **Exceptions Checked**: No exceptions in 250.24(B) or 250.25 permit a main bonding jumper in subpanels.  

---

### **Correct Configuration (Per CEC 2022)**
1. **Neutral Bar**  
   - Connect **only the feeder neutral conductor**.  
   - **No bonding** to ground bar or enclosure.  

2. **Ground Bar**  
   - Connect:  
     - **Feeder equipment grounding conductor** (from main panel).  
     - **Grounding electrode conductor (GEC)** (e.g., 4 AWG copper for #2 AWG aluminum feeders per Table 250.66).  
   - Bond to the **metal enclosure** per CEC 408.40.  

3. **Enclosure Bonding**  
   - Ground bar must be bonded to the metal enclosure.  
   - Neutral bar must remain **unbonded**.  

---

### **NEC 2023 Reference**  
No difference from NEC 2023. NEC 250.24(A)(5) and 250.4(A)(5) also prohibit neutral-ground bonding in subpanels.  

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 250.97, 250.54, 250.66, 408.40, 250.24, 250.4, 250.86, 250.25

**Response Time:** 11.0s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**
## Final Answer with Exception Check

**Conduit Fill Calculation Confirmed:**  
The calculation using CEC Chapter 9 Tables 4 and 5 (conduit area and conductor area) remains valid. The `cec_exception_search` for **300.15** returned exceptions related to boxes, fittings, and underground installations, but **none apply to conduit fill calculations** for RMC with THHN conductors.  

**Key Findings:**  
- No exceptions override Chapter 9 fill rules for this scenario.  
- The 40% fill limit (Table 4) and conductor area (Table 5) are unchanged.  
- The result of **28 maximum 10 AWG THHN conductors** in 1¼" RMC stands.  

**Final Verification:**  
- **Three conductors** is acceptable (4.1% fill).  
- **28 conductors** is the maximum allowed (40% fill).  

---
## NEC 2023 Reference  
No difference from NEC 2023 (same tables and exceptions).  

✓ Sources: CEC 2022 Chapter 9 Tables 4 and 5, NEC 2023 Chapter 9 Tables 4 and 5

**Tool Usage:**
- CEC Tools: cec_lookup_conduit_fill, cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 300.15

**Response Time:** 17.1s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**
## Voltage Drop Calculation (CEC 2022)

**Voltage drop**: 2.84 volts  
**Percentage**: 2.36%  

**Calculation steps**:
1. **Formula**:  
   $$
   VD = \frac{2 \times I \times L \times R}{1000} = \frac{2 \times 22 \, \text{A} \times 50 \, \text{ft} \times 1.29 \, \Omega}{1000} = 2.84 \, \text{V}
   $$
2. **Percentage**:  
   $$
   \frac{2.84 \, \text{V}}{120 \, \text{V}} \times 100 = 2.36\%
   $$

**Compliance**:  
✓ **Meets general recommendation** (≤3% for branch circuits per **CEC 210.19(A)**).  
⚠️ **Stricter limits apply in specialized systems** (e.g., 1.5% for fixed equipment in **CEC 647.4(D)(1)**).

**Exceptions Checked**:  
- No exceptions to 210.19(A) directly address voltage drop limits.  
- Informational Note 3 in 210.19(A) explicitly references the 3% recommendation.  

---
## NEC 2023 Reference  
No difference from NEC 2023. Voltage drop recommendations remain unchanged.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 647.4, 210.19

**Response Time:** 15.8s

---

### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Final Adjusted Ampacity with Exceptions Considered (CEC 2022)

1. **Base Calculation Confirmed**:  
   20A × 0.71 (temp) × 0.50 (bundling) = **7.1A** as previously calculated

2. **Exception Analysis**:  
   - **310.15 Exception**: Permits applying correction factors **as long as the adjusted ampacity does not exceed the termination temperature rating** (110.14(C)).  
     → Our adjusted ampacity (7.1A) is **well below** the 60°C termination limit (20A), so this exception **does not override** our calculation.  
   - **310.15(C)(1) Exception**: No exceptions apply to the bundling adjustment for 6 conductors in a raceway >24" long (our case).  

3. **Special Conditions Checked**:  
   - No exceptions for TW insulation type  
   - No rooftop temperature adder applies (attic ≠ rooftop)  
   - No engineering supervision waiver for interpolation  

**Final Answer**: **7.1 amperes** after applying all required adjustments and exceptions.

---
## NEC 2023 Reference  
No difference from NEC 2023.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 310.15, 110.14

**Response Time:** 12.8s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Grounding Electrode Conductor Sizing (CEC 2022)

For **1000 kcmil copper service-entrance conductors** (4 × 250 kcmil parallel conductors), **CEC Table 250.66** requires a **350 kcmil copper** grounding electrode conductor (GEC).

**Key Details:**
- **Total equivalent service conductor size**: 1000 kcmil (per phase, 4 parallel conductors)
- **CEC Table 250.66**: 1000 kcmil copper service conductors → **350 kcmil copper GEC**
- **Exceptions Checked**: No exceptions in CEC 250.66 override this requirement for parallel conductors

---
## NEC 2023 Reference
No difference from NEC 2023 Table 250.66.

✓ Sources: CEC 2022 (primary), NEC 2023 (comparison)

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 10.2s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 28/28
- **Success Rate**: 100.0%
- **Average Response Time**: 13.4s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

