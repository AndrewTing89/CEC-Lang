# Core (NEC) Evaluation Results - Run 32 (Reflection Feature)

**Date:** 2025-12-11
**Changes:** Added reflection/self-verification after initial answer

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 238.5s |
| Avg Duration | 8.8s |
| Reflection Used | 27/27 |
| Reflection Improved | 6/27 |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 6.8s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_size

**Reflection:** Yes

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum conductor size**: **6 AWG copper**  
- **Ampacity**: 65A (meets 60A requirement)  
- **Table reference**: CEC 2022 Table 310.16  

**Key Considerations**:  
1. **Overcurrent Protection**:  
   - Per **240.4(D)**, 6 AWG copper is protected by a maximum 65A overcurrent device.  
   - 65A OCP is acceptable for this 60A circuit.  

2. **Temperature and Bundling Adjustments**:  
   - The 65A ampacity assumes standard ambient temperature (30°C/86°F) and ≤3 current-carrying conductors.  
   - If ambient temperature >30°C or >3 conductors in a raceway, apply correction factors from:  
     - **310.15(B)(1)** (temperature)  
     - **310.15(C)(1)** (bundling)  

3. **California-Specific Requirements**:  
   - No additional CALGreen or Title 24 mandates apply for general 60A circuits.  

**Inspector Note**: Verify installation conditions (temperature, bundling) to ensure derated ampacity still meets 60A.  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 10.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## GFCI Protection Requirements in Residential Kitchens (CEC 2022)

**GFCI protection is required for the following locations in residential kitchens:**

1. **Countertop Receptacles**  
   - All receptacles installed to serve countertop surfaces **must have GFCI protection**.  
   - **Source**: CEC 2022 [Section 210.8(A)(6)](https://example.com/cec210.8)  

2. **Receptacles Near Sinks**  
   - Any receptacle within **1.8 meters (6 feet)** of the **top inside edge of the sink bowl** must be GFCI-protected.  
   - **Source**: CEC 2022 [Section 210.8(A)(7)](https://example.com/cec210.8)  

---

**Key Details:**  
- **Scope**: Applies to 125–250V receptacles in dwelling units (residential kitchens).  
- **Exceptions**:  
  - Receptacles for **hardwired appliances** (e.g., built-in ovens) may not require GFCI if the appliance is listed as inherently safe.  
  - **Ceiling-mounted lighting/fans** are exempt, but **general-use receptacles** in these devices still require GFCI.  

**Inspector Note**: Verify that all countertop and sink-near receptacles are GFCI-protected using either a GFCI circuit breaker or GFCI receptacles. Test functionality per [CEC 210.8](https://example.com/cec210.8) requirements.  

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 6.6s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022)

**Yes**, arc-fault circuit interrupter (AFCI) protection is **required** for all 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets or devices in **bedrooms** of new residential construction. This requirement is explicitly stated in **CEC 2022 Section 210.12(A)**.

### Key Details:
- **Applies to**: Dwelling units (residential homes).
- **Protected areas**: Bedrooms, along with kitchens, family rooms, dining rooms, living rooms, and other similar spaces.
- **Permitted methods**: 
  - Combination-type AFCI at the service panel.
  - Branch/feeder-type AFCI combined with outlet branch-circuit-type AFCI.
  - Supplemental arc protection circuit breaker with outlet AFCI (under specific conditions).
- **Exceptions**: 
  - Not required for fire alarm circuits (not applicable to bedrooms).
  - Limited exceptions for circuit extensions <6 ft (not relevant to new construction).

**Source**: CEC 2022 Section 210.12(A)  
[OK] Source: CEC 2022

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 7.5s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_exception_search

**Reflection:** Yes (improved answer)

**Answer:**

[VERIFIED] Answer is complete.

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 8.2s | **Iterations:** 4

**Tools Called:** cec_lookup_working_space, cec_exception_search

**Reflection:** Yes (improved answer)

**Answer:**

[VERIFIED] Answer is complete.

The minimum working clearance depth of **900 mm (3 ft)** for a 120/240V residential panel under **Condition 2** (exposed live parts on one side and grounded parts on the other) is correctly cited from **CEC Table 110.26(A)(1)**. 

### Exception Review:
- **110.26(E)** addresses *dedicated vertical space* (height from floor to 6 ft above equipment) and does not conflict with the 3 ft depth requirement.
- **440.14** and **425.8** exceptions apply to HVAC/refrigeration equipment and industrial heating systems, which are outside the scope of a standard residential panel.
- No exceptions reduce or eliminate the 3 ft depth requirement for residential applications.

### Additional Compliance Notes:
- **240.24(D)** and **240.24(E)** govern panel *location* (closets/bathrooms), but the 3 ft depth requirement remains unchanged.
- The answer includes the critical distinction between *clearance depth* (this question) and *location restrictions* (separate rule). 

All code references are accurate, and no applicable exceptions were found for this specific residential scenario.

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 5.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Number of 20-Ampere Small Appliance Branch Circuits for a Kitchen (CEC 2022)

**Answer:**  
A minimum of **two** 20-ampere small-appliance branch circuits are required for a kitchen in a dwelling unit.  

**Code Requirements:**  
1. **CEC 2022 Section 210.11(C)(1):**  
   *"In addition to the number of branch circuits required by other parts of this section, two or more 20-ampere small-appliance branch circuits shall be provided for all receptacle outlets specified by 210.52(B)."*  

2. **CEC 2022 Section 210.52(B)(1):**  
   *"In the kitchen [...] the two or more small-appliance branch circuits required by 210.11(C)(1) shall serve [...] all countertop outlets [...] and receptacle outlets for refrigeration equipment."*  

**Inspector Note:**  
- The code permits **additional** small-appliance branch circuits beyond the minimum two (see Exception No. 1 in 210.52(B)(1)).  
- Each small-appliance branch circuit **must serve only the kitchen** (no other areas).  

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 5.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Surge Protection Requirement for Residential Service (CEC 2022)

**Answer:**  
Yes, surge protection is required for a new 200A residential service per **CEC 2022 Section 230.67**:

- **230.67(A)**: All services supplying dwelling units **must include a surge-protective device (SPD)**.
- **230.67(B)**: The SPD must be:
  - An integral part of the service equipment, or
  - Located immediately adjacent to the service equipment.
  - *Exception*: Permitted at the next level of distribution downstream toward the load.
- **230.67(C)**: The SPD must be **Type 1 or Type 2**.

This requirement applies to all new residential services in California under CEC 2022. While the 2023 NEC may have similar provisions, this answer is based on the authoritative CEC 2022 text.

[OK] Source: CEC 2022

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 12.7s | **Iterations:** 4

**Tools Called:** cec_lookup_conductor_size, cec_lookup_conductor_size

**Reflection:** Yes

**Answer:**

## Service Conductor Sizing (CEC 2022)

**Required Service Conductor Size:**
- **Copper:** 2/0 AWG (Table 310.12(A) for 200A)
- **Aluminum:** 4/0 AWG (Table 310.12(A) for 200A)

**Key Requirements:**
1. **Table 310.12(A)** applies to single-phase dwelling service conductors (✓ 120/240V system, ✓ supplying entire dwelling load)
2. **Aluminum is permitted** for service conductors when:
   - Terminations are rated for **75°C** (per Table 310.12(A) footnotes)
   - Proper torque specifications are followed per **110.14(D)**
3. **No adjustments needed** since:
   - No temperature correction factors (standard ambient conditions assumed)
   - No bundling adjustments (typically 3 or 4 conductors for service entrance)

**Inspector Note:** Verify equipment terminations are rated for 75°C if using aluminum. Check California amendments in **Title 24 Part 6** for any additional requirements.

[OK] Source: CEC 2022

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 8.5s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Multiwire Branch Circuit Requirements (CEC 2022)

### Circuit Breaker Requirements
1. **Simultaneous Disconnect** (Section 210.4(B)):  
   - All ungrounded (hot) conductors must be disconnected simultaneously using a **2-pole circuit breaker** or **handle-tied single-pole breakers**.  
   - This prevents overloading the neutral conductor if one hot leg remains energized.  

2. **AFCI Protection** (Section 210.12(A)):  
   - A **combination-type AFCI breaker** or **system-combination AFCI** is required for kitchen circuits.  
   - Alternative: An outlet-type AFCI at the first receptacle (if permitted by local code).  

3. **Breaker Rating**:  
   - Must match the conductor size (12 AWG copper = **20A maximum** per 240.4(D)).  

---

### Neutral Termination Requirements
1. **Dedicated Neutral** (Section 210.4(D)):  
   - The neutral conductor must **not be shared** with other circuits.  
   - Must terminate at the **neutral bus bar in the panelboard**, not at a junction box or subpanel.  

2. **Neutral Sizing**:  
   - For 120V line-to-neutral loads (kitchen receptacles), the neutral must be the **same size as the ungrounded conductors** (12 AWG copper).  

3. **No Overcurrent Protection on Neutral**:  
   - The neutral conductor must **not be intentionally interrupted** by a switch or breaker (per 210.4(D)).  

---

### Key Code Citations
- **Simultaneous Disconnect**: CEC 2022 Section 210.4(B)  
- **AFCI Protection**: CEC 2022 Section 210.12(A)  
- **Conductor Sizing**: CEC 2022 Table 310.16 (12 AWG copper = 30A at 75°C, but limited to 20A by 240.4(D))  

[OK] Source: CEC 2022

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 9.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## GFCI Protection Locations in Residential Dwellings (CEC 2022)

According to **CEC 2022 Section 210.8**, GFCI protection is required for all 125–250V receptacles in the following locations within dwelling units:

---

### **Required Locations (210.8(A)(1)–(11))**
1. **Bathrooms**  
2. **Garages and accessory buildings** (floor at or below grade, non-habitable)  
3. **Outdoors**  
   - *Exception:* Receptacles for dedicated snow-melting/deicing systems (per 426.28/427.22).  
4. **Crawl spaces** (at or below grade)  
5. **Basements**  
   - *Exception:* Receptacles for fire alarm systems (not required).  
6. **Kitchens** (countertop surfaces)  
7. **Within 1.8 m (6 ft)** of sink bowl edges  
8. **Boathouses**  
9. **Within 1.8 m (6 ft)** of bathtub/shower stall edges  
10. **Laundry areas**  
11. **Indoor damp/wet locations**  

---

### **Additional Requirements**
- **Crawl space lighting outlets** (210.8(C)): All lighting outlets in crawl spaces require GFCI protection.  
- **Rooftops** (210.8(D)(3)): Receptacles on rooftops must be GFCI-protected unless non-accessible.  
- **Specific appliances** (422.5): Vending machines, dishwashers, sump pumps, etc., require GFCI protection unless exceptions apply.  
- **Fountains** (680.58): Receptacles within 6.0 m (20 ft) of fountains must be GFCI-protected.  

---

### **Exceptions**
- **Locking receptacles** for ceiling fans/luminaires: Exempt if not used for general-purpose convenience.  
- **Industrial labs** (210.8(B)(5)): Receptacles for equipment where power interruption creates greater hazards may be exempt.  
- **Dedicated circuits** for heating systems (e.g., snow-melting) may be exempt per 426.28/427.22.  

---

[OK] Source: CEC 2022, Sections 210.8, 422.5, 680.58

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 10.3s | **Iterations:** 4

**Tools Called:** cec_search, cec_search

**Reflection:** Yes (improved answer)

**Answer:**

## Surge Protection for Residential Service (CEC 2022) - Revised

**Answer:**  
Surge protection **is required** by the California Electrical Code (CEC 2022) for a new 200A residential service.  

### Code Requirements:
1. **Mandatory Requirement**:  
   - **Section 230.67(A)**: All services supplying dwelling units **must** include a surge-protective device (SPD).  
   - **Section 230.67(C)**: The SPD must be **Type 1 or Type 2** (see Section 100 definitions).  

2. **Installation Location**:  
   - **Section 230.67(B)**: The SPD must be:  
     - An integral part of the **main service equipment**, or  
     - Installed **immediately adjacent** to the service equipment.  
   - **Exception**: SPDs may be installed at **downstream distribution equipment** (e.g., subpanels) if they provide equivalent protection.  

3. **Grounding Requirements**:  
   - SPDs must be connected to the **equipment grounding conductor** per **Table 250.122**.  
     - For a 200A service:  
       - **Copper**: 6 AWG (Table 250.122, 200A column).  
       - **Aluminum**: 4 AWG.  

### Inspector Note:  
- Verify the SPD is listed for the application (UL 1449-compliant).  
- Ensure grounding conductor size matches Table 250.122 and is properly bonded to the service equipment.  

[OK] Source: CEC 2022  

[VERIFIED] Answer is complete.

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 18.0s | **Iterations:** 4

**Tools Called:** cec_search, cec_search

**Reflection:** Yes

**Answer:**

## Panel in Closet Clearance Compliance (CEC 2022)

**1. Panel Location in Closet**  
- **Violation**: Section 240.24(D) explicitly prohibits overcurrent devices (panels) from being located in clothes closets due to fire hazard risks from ignitable materials.  
- **Exception**: No exceptions apply for standard residential closets.  

**2. Working Space Clearance**  
- **Front Clearance**: 24 inches meets **Table 110.26(A)(1)** requirements for working space depth (minimum 20 inches for panels ≤6 ft tall).  
- **Side Clearance**: The 18-inch distance to the water heater is not regulated by NEC/CEC for panels, but local codes may address water heater proximity to electrical equipment.  

**3. Key Code Citations**  
- **240.24(D)**: Prohibits panels in clothes closets.  
- **Table 110.26(A)(1)**: Requires minimum 20–30 inches front clearance (depending on panel height).  

**Conclusion**:  
- The panel **fails** due to being in a clothes closet (240.24(D) violation).  
- Front clearance (24 inches) is **compliant** if panel height ≤6 ft.  

[OK] Source: CEC 2022

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 5.5s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Code Violation for Multiple Conductors on a Single Breaker Terminal (CEC 2022)

**Yes, this is a code violation** under **CEC 2022 Section 110.14(A)** and **110.3(B)**. Here's the breakdown:

1. **Section 110.14(A) - Terminals for Multiple Conductors**  
   - *"Terminals for more than one conductor and terminals used to connect aluminum shall be so identified."*  
   - The breaker terminal in question is **not marked/identified** for two conductors. Only terminals explicitly listed/identified for multiple conductor connections are permitted.

2. **Section 110.3(B) - Equipment Installation**  
   - *"Equipment shall be installed in accordance with any instructions included in the listing or labeling."*  
   - If the breaker manufacturer does not specify approval for two conductors on a single terminal (common for most standard breakers), this installation violates the equipment's listing.

**Inspector Note:**  
- **14 AWG through 1 AWG conductors** are often limited to single terminations unless the terminal is specifically marked (e.g., "2-wire" or "2-conductor").  
- This violation increases risk of poor connections, overheating, or equipment damage.  

[OK] Source: CEC 2022 Sections 110.14(A), 110.3(B)

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 9.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Grounding and Bonding for Detached Garage Subpanel (CEC 2022)

### Configuration Requirements:
1. **Grounding Electrode Conductor (GEC):**
   - A **separate grounding electrode conductor** must connect the subpanel's grounding bus to a **local grounding electrode** (e.g., ground rod) at the garage.  
   - Size the GEC per **Table 250.66** based on the **largest ungrounded (hot) conductor** in the feeder.  
     Example: For a 100A feeder with 3/0 AWG copper conductors, use a **4 AWG copper** GEC (Table 250.66).

2. **Equipment Grounding Conductor (EGC):**
   - The **4th wire** in the feeder (EGC) must connect the subpanel's grounding bus to the **main panel's grounding system**.  
   - Size the EGC per **Table 250.122** based on the overcurrent protection at the main panel.  
     Example: For a 100A breaker, use a **8 AWG copper** EGC.

3. **No Neutral-to-Ground Bond:**
   - The **neutral bus** in the subpanel **must remain isolated** from the enclosure (no bonding). This prevents parallel neutral paths and ensures fault current returns via the EGC.

4. **Bonding Jumper (if required):**
   - If the subpanel has a separately derived system (e.g., transformer), a **supply-side bonding jumper** is required per **250.30(B)(3)** to bond the source to the first disconnect.

---

### Key Code References:
- **250.30(B):** Grounding and bonding for separately derived systems (applies to subpanels in detached structures).  
- **250.24(A)(5):** Prohibits re-grounding the neutral on the load side of the service disconnect (critical for subpanels).  
- **250.58:** Requires all grounding electrodes in the structure to be bonded together.  
- **250.66:** Sizes the grounding electrode conductor based on feeder conductor size.  

---

### Inspector Note:
- Verify the **GEC connects to a local electrode** (e.g., ground rod) at the garage.  
- Confirm the **EGC is sized correctly** and runs with the feeder.  
- Ensure **neutral and ground bars are isolated** in the subpanel.  

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 6.3s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper (CEC 2022)

### Definitions
- **Main Bonding Jumper** (CEC 2022 Section 100):  
  Connects the **grounded circuit conductor** (neutral) to the **equipment grounding conductor** at the **service**.  
  - Required for **services** (e.g., utility-fed electrical systems).  

- **System Bonding Jumper** (CEC 2022 Section 100):  
  Connects the **grounded circuit conductor** to the **supply-side bonding jumper** or **equipment grounding conductor** at a **separately derived system** (e.g., transformers, generators).  
  - Required for **separately derived systems** (systems not directly connected to the utility service).  

---

### When Each is Required
1. **Main Bonding Jumper** (CEC 2022 250.28):  
   - **Required at services** (e.g., utility meter location).  
   - If the service has **multiple enclosures** (per 230.71(B)), each enclosure must have a main bonding jumper sized based on the **largest ungrounded service conductor** serving that enclosure.  

2. **System Bonding Jumper** (CEC 2022 250.28):  
   - **Required at separately derived systems** (e.g., transformer secondary, solar PV systems).  
   - If the system has **multiple enclosures**, each enclosure must have a system bonding jumper sized based on the **largest ungrounded feeder conductor** serving that enclosure.  

---

### Sizing Requirements
Both jumpers are sized per **Table 250.102(C)(1)** based on the **largest ungrounded conductor** in the system:  

| Largest Ungrounded Conductor | Main/System Bonding Jumper Size (Copper) |  
|-----------------------------|------------------------------------------|  
| 2 AWG or smaller            | 8 AWG                                    |  
| 1 AWG or 1/0 AWG            | 6 AWG                                    |  
| 2/0 AWG or 3/0 AWG          | 4 AWG                                    |  
| 4/0 AWG through 350 kcmil   | 2 AWG                                    |  
| 600 kcmil                   | 1/0 AWG                                  |  

**Example**:  
- For a service with **4/0 AWG copper service conductors**, the main bonding jumper must be **4 AWG copper** (per Table 250.102(C)(1)).  

---

### Key Differences
| Feature                     | Main Bonding Jumper                     | System Bonding Jumper                     |  
|-----------------------------|------------------------------------------|-------------------------------------------|  
| **Location**                | Service (utility connection point)       | Separately derived system (e.g., transformer secondary) |  
| **Application**             | Services (e.g., residential, commercial) | Separately derived systems (e.g., generators, transformers) |  
| **Sizing Basis**            | Largest service conductor                | Largest feeder conductor to the system    |  

---

### Inspector Notes
- **Main bonding jumpers** are part of the **service equipment** and must comply with 250.28(D).  
- **System bonding jumpers** are part of **separately derived systems** and must comply with 250.28(D) and 250.102(C).  
- Both must be made of **copper, aluminum, or corrosion-resistant material** (250.28(A)).  

[OK] Source: CEC 2022 Sections 100, 250.28, 250.102(C)(1)

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 7.7s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Small Appliance Branch Circuits in Kitchens and Dining Rooms (CEC 2022)

### **1. Required Number of 20-Amp Small Appliance Branch Circuits for a Kitchen**
- **Minimum Requirement**: **Two 20-amp small appliance branch circuits** are required for the kitchen area in a dwelling unit.  
- **Code Basis**: CEC 2022 **Section 210.11(C)(1)** mandates at least two 20-amp circuits for small appliances in kitchens, pantries, and dining rooms. However, the **kitchen** (distinct from pantry/dining room) is explicitly required to have **two dedicated circuits** to handle high-load appliances like microwaves and toasters.  

---

### **2. Can These Circuits Serve Dining Room Receptacles?**
- **Answer**: **No**, the two required kitchen small appliance branch circuits **cannot** serve dining room receptacles.  
- **Code Basis**:  
  - **Section 210.11(C)(1)** specifies that the two small appliance circuits must serve **kitchen** and **pantry** receptacles.  
  - **Section 220.52(A)** confirms that small appliance loads are calculated separately and do not include dining room receptacles.  
  - **Section 210.52(B)** (not explicitly referenced but implied) requires dining room receptacles to be on separate circuits if they are not part of the kitchen/pantry.  

---

### **Key Code Citations**
- **210.11(C)(1)**: Requires two 20-amp small appliance branch circuits for kitchens and pantries.  
- **220.52(A)**: Specifies 1500 VA per small appliance circuit, excluding dining rooms.  
- **220.42**: Excludes kitchens and dining rooms from demand factor calculations, reinforcing separate circuit requirements.  

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 5.8s | **Iterations:** 3

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG THHN copper at 90°C = **30A** (Table 310.16)

**Step 2: Temperature Correction**  
Ambient 50°C → 0.82 correction factor (Table 310.15(B)(1)(1))  
30A × 0.82 = **24.6A**

**Step 3: Bundling Adjustment**  
6 conductors → 0.8 adjustment factor (Table 310.15(C)(1))  
24.6A × 0.8 = **19.68A**

**Final Adjusted Ampacity**  
**19.68A** (round down to **19A** for practical application)

**Citations**  
- Base ampacity: Table 310.16  
- Temperature correction: Table 310.15(B)(1)(1)  
- Bundling adjustment: Table 310.15(C)(1)  

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 11.3s | **Iterations:** 4

**Tools Called:** cec_search, cec_exception_search

**Reflection:** Yes (improved answer)

**Answer:**

[VERIFIED] Answer is complete.  

The answer addresses the requirement (CEC 2022 Section 210.12), explains the hazard (arc faults causing fires), and includes relevant exceptions (e.g., Section 210.12(D) for circuit modifications). All cross-references and exceptions were reviewed, and no critical gaps were identified.

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 5.9s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Torque Specifications for Conductor Terminations (CEC 2022)

Torque specifications are critical for ensuring **secure, low-resistance electrical connections** in panels and equipment. Improper torque can lead to:
- **Under-torqued connections**: Loose terminations causing arcing, overheating, and potential fire hazards.
- **Over-torqued connections**: Damaged conductors or terminals, leading to mechanical failure or compromised conductivity.

### Code Requirements
The requirements are found in **CEC 2022 Section 110.14(D)** and **Section 430.9(C)**:

1. **Section 110.14(D) - Terminal Connection Torque**  
   - **Torque values** must be as indicated on the equipment or in the manufacturer’s installation instructions.  
   - **Approved methods** (e.g., torque tools, shear bolts, or breakaway devices) must be used to achieve the specified torque.  
   - **Informational Notes**:  
     - Contact the equipment manufacturer if torque values are not marked.  
     - Refer to UL 486A-486B or NFPA 70B for torque guidance.  

2. **Section 430.9(C)**  
   - Control circuit devices with screw-type terminals using **14 AWG or smaller copper conductors** must be torqued to **at least 0.8 N·m (7 lb-in.)** unless otherwise specified.  

### Key Takeaways
- Always follow **manufacturer-marked torque values** on equipment.  
- Use **calibrated torque tools** to ensure compliance.  
- Document torque application as part of installation practices to prevent future issues.  

[OK] Source: CEC 2022

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 15.2s | **Iterations:** 4

**Tools Called:** cec_search, cec_lookup_table

**Reflection:** Yes (improved answer)

**Answer:**

[VERIFIED] Answer is complete.

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 9.3s | **Iterations:** 3

**Tools Called:** cec_lookup_working_space

**Reflection:** Yes

**Answer:**

## Electrical Panel Inspection Violations (CEC 2022)

### 1. **Insufficient Working Space Depth**
- **Violation**: The required working space depth for a 120V panel (condition 1) is **35.43 inches (900 mm)** per **CEC Table 110.26(A)(1)**. The provided depth of **28 inches** is insufficient.
- **Citation**: CEC 2022 Table 110.26(A)(1), 110.26(A)(1)(b).

### 2. **Obstruction in Working Space**
- **Violation**: The water heater located **16 inches** from the panel intrudes into the required working space. **No obstructions** are permitted within the working space.
- **Citation**: CEC 2022 110.26(A)(1)(c) ("No pipes, ducts, or other obstructions shall be located in the working space").

### 3. **Incorrect Panel Mounting Height**
- **Violation**: The panel is mounted at **5 feet (60 inches)** from the floor. The minimum required height is **6.5 feet (78 inches)** from the floor to the **bottom of the panel**.
- **Citation**: CEC 2022 110.26(A)(2).

---

### Additional Notes:
- **Width Clearance**: The 30-inch width clearance aligns with **Table 110.26(A)(1)** for 120V panels (minimum 30 inches). No violation if the panel width does not exceed this.
- **Location Restrictions**: Verify if the panel is in a prohibited location (e.g., clothes closet per **240.24(D)**). The question does not specify this, so no violation is assumed here.

[OK] Source: CEC 2022

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 9.8s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Circuit Protection Requirements for New Residential Kitchen (2023 NEC)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required**: **Combination AFCI/GFCI**
- **NEC References**:
  - **GFCI**: 210.8(A)(6) requires GFCI protection for all 125V–250V receptacles serving countertop surfaces.
  - **AFCI**: 210.12(A) mandates AFCI protection for all branch circuits in dwelling units, including kitchens.

### 2. **Dishwasher (Dedicated 15A Circuit)**
- **Protection Required**: **Combination AFCI/GFCI**
- **NEC References**:
  - **GFCI**: 210.8(D) and 422.5(B) require GFCI protection for appliances like dishwashers if connected via a receptacle.
  - **AFCI**: 210.12(A) applies to all branch circuits, including dedicated appliance circuits.

### 3. **Garbage Disposal (Dedicated 15A Circuit)**
- **Protection Required**: **Combination AFCI/GFCI**
- **NEC References**:
  - **GFCI**: 210.8(A)(6) applies if the disposal is connected via a countertop receptacle. If hardwired, GFCI may not apply (see 422.5(B)).
  - **AFCI**: 210.12(A) requires AFCI for all branch circuits.

### 4. **Refrigerator (Dedicated 20A Circuit)**
- **Protection Required**: **Standard AFCI**
- **NEC References**:
  - **GFCI**: **Not required** (Exception to 210.8(A)(6) excludes refrigerators from countertop GFCI requirements).
  - **AFCI**: 210.12(A) applies to all branch circuits, including dedicated refrigerator circuits.

---

### Inspector Notes:
- **Countertop Circuits**: Must use **combination AFCI/GFCI breakers** or **GFCI receptacles with upstream AFCI protection**.
- **Appliance Circuits**: Dishwasher and disposal circuits require **combination protection** unless hardwired (GFCI may not apply).
- **Refrigerator Circuit**: **Standard AFCI** is sufficient; GFCI is not required per 210.8(A)(6) exception.

[OK] Source: 2023 NEC (210.8, 210.12, 422.5)

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 7.0s | **Iterations:** 3

**Tools Called:** cec_search

**Reflection:** Yes

**Answer:**

## Subpanel Grounding Violations in Detached Garage (CEC 2022)

### Identified Violations:
1. **Bonded Neutral and Ground Bars**  
   - **Violation**: Neutral and ground bars are bonded together in the subpanel.  
   - **Code**: CEC 2022 **250.32(B)(1)** requires **separate** neutral and ground bars in detached structures. Bonding creates a parallel neutral path, risking shock hazards.  
   - **Correct**: Neutral and ground bars must be **electrically isolated** in subpanels (unlike main panels).

2. **Neutral Bar Bonded to Metal Enclosure**  
   - **Violation**: Neutral bar connected to the metal enclosure.  
   - **Code**: CEC 2022 **250.142(B)** prohibits bonding neutral to enclosures in subpanels. This creates unintended grounding paths.  
   - **Correct**: Neutral bar should only connect to the **feeder neutral conductor** (no enclosure connection).

3. **Missing Grounding Electrode Conductor**  
   - **Violation**: No mention of a grounding electrode (e.g., ground rod) at the detached garage.  
   - **Code**: CEC 2022 **250.32(B)(1)** and **250.50** require a **local grounding electrode** (e.g., ground rod) for detached structures.  
   - **Correct**: Install a grounding electrode (e.g., 8 ft ground rod) at the garage and connect it to the subpanel’s **ground bar** via a grounding electrode conductor (sized per **Table 250.66**).

---

### Correct Configuration for Detached Subpanel:
1. **Feeder Conductors**:  
   - **2 hots**, **1 neutral**, **1 equipment grounding conductor (EGC)** (4-wire feeder) – ✅ Compliant with **250.32(B)(1)**.

2. **Subpanel Internal Connections**:  
   - **Neutral Bar**:  
     - Connected only to the **feeder neutral conductor**.  
     - **No bonding** to ground bar or metal enclosure.  
   - **Ground Bar**:  
     - Connected to:  
       - **Feeder EGC** (from main panel).  
       - **Local grounding electrode conductor** (e.g., ground rod at garage).  
     - **No bonding** to neutral bar.  
   - **Metal Enclosure**:  
     - Bonded **only to the ground bar** (via a bonding jumper).  

3. **Grounding Electrode Conductor Size**:  
   - For #2 AWG aluminum feeder conductors, use **4 AWG copper** or **2 AWG aluminum** for the grounding electrode conductor (per **Table 250.66**).  

---

### Inspector Notes Reconciliation:
| Inspector Note | Status | Correct Action |
|----------------|--------|----------------|
| Neutral bar and ground bar bonded | ❌ Violation | **Separate** neutral and ground bars; remove bonding jumper. |
| Ground bar bonded to metal enclosure | ✅ Compliant | Maintain this connection. |
| Neutral bar bonded to metal enclosure | ❌ Violation | **Disconnect** neutral bar from enclosure. |
| Feeder ground connected to ground bar | ✅ Compliant | Maintain this connection. |
| Feeder neutral connected to neutral bar | ✅ Compliant | Maintain this connection. |

---

### Code Citations:
- **250.32(B)(1)**: Requires separate grounding electrode conductor for detached structures.  
- **250.50**: Mandates grounding electrode (e.g., ground rod) at detached buildings.  
- **250.66**: Sizes grounding electrode conductor based on largest ungrounded feeder conductor.  
- **250.142(B)**: Prohibits bonding neutral to enclosures in subpanels.  

[OK] Source: CEC 2022

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 5.4s | **Iterations:** 3

**Tools Called:** cec_lookup_conduit_fill

**Reflection:** Yes

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC (CEC 2022)

**Calculation:**
1. **Conduit Fill Limit:**  
   - RMC 1¼" total area = 1.526 in² (Chapter 9 Table 4)  
   - 40% fill limit = 0.61 in² (for 3 or more conductors)  

2. **Conductor Area:**  
   - 10 AWG THHN = 0.0211 in² per conductor (Chapter 9 Table 5)  

3. **Maximum Conductors:**  
   $$
   \frac{0.61\ \text{in²}}{0.0211\ \text{in²/conductor}} = 28.91 \rightarrow \lfloor 28 \rfloor
   $$

**Final Answer:**  
**28 conductors** (maximum at 40% fill)  

**Verification:**  
- 28 × 0.0211 = 0.5908 in² (96.9% of 0.61 in² fill limit)  
- 3 conductors = 0.0633 in² (4.1% fill)  

**Citations:**  
- Conduit area: CEC 2022 Chapter 9 Table 4  
- Conductor area: CEC 2022 Chapter 9 Table 5  
- Fill calculation method: CEC 2022 300.15(B)(2)(a)  

[OK] Source: CEC 2022

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 14.3s | **Iterations:** 6

**Tools Called:** python_calculator, python_calculator, cec_search

**Reflection:** Yes

**Answer:**

## Voltage Drop Calculation (CEC 2022)

1. **Voltage drop calculation**:
   $$
   VD = 2 \times I \times R \times \frac{L}{1000} = 2 \times 22A \times 1.29\ \Omega \times \frac{50}{1000} = 2.808\ V
   $$

2. **Percentage voltage drop**:
   $$
   \text{Percentage} = \left(\frac{2.808V}{120V}\right) \times 100 = 2.34\%
   $$

3. **Code compliance verification**:
   - **NEC/CEC recommendation**: 3% maximum for branch circuits (per CEC 210.19(A)FPN)
   - **Result**: 2.34% ≤ 3% → **Meets requirements**

**Key Code References**:
- CEC 210.19(A)FPN: "Voltage drop on branch circuits... shall not exceed 3%... for reasonable efficiency of operation"
- CEC 647.4(D): Stricter 1.5% limit applies only to specific fixed equipment circuits (not applicable here)

[OK] Source: CEC 2022

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 7.1s | **Iterations:** 5

**Tools Called:** cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment

**Reflection:** Yes

**Answer:**

## Adjusted Ampacity Calculation (CEC 2022)

**Step 1: Base Ampacity**  
12 AWG copper (60°C rated) = **20A** (Table 310.16)

**Step 2: Temperature Correction**  
Ambient = 43°C → Correction factor = **0.71** (Table 310.15(B)(1)(1))  
20A × 0.71 = **14.2A**

**Step 3: Bundling Adjustment**  
6 conductors → Adjustment factor = **0.8** (Table 310.15(C)(1))  
14.2A × 0.8 = **11.36A**

**Final Adjusted Ampacity**  
**11.36 amperes** after applying both corrections.

**Limiting Rule Check**  
- 240.4(D) allows 20A OCPD for 12 AWG copper (base rule)  
- Adjusted ampacity (11.36A) < 20A → OCPD remains valid  

[OK] Source: CEC 2022

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 8.6s | **Iterations:** 4

**Tools Called:** cec_lookup_grounding_conductor, cec_exception_search

**Reflection:** Yes (improved answer)

**Answer:**

[VERIFIED] Answer is complete.

---

