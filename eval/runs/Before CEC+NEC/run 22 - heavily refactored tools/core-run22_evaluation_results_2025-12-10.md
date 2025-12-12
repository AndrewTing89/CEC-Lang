# Core Evaluation Results - Run 22 (Patched)

Generated: 2025-12-10 02:22:02

## Summary
- Total Questions: 28
- Successful: 28
- Failed: 0
- Total Duration: 500.3s

---

### baseline-001

**Question:** What is the ampacity of a 12 AWG copper conductor with 75°C rated insulation (such as THWN) according to NEC Table 310.16?

**Duration:** 9.7s | **NEC Comparison:** Yes

**Tools Called:** nec_base_ampacity, compare_with_nec

**Answer:**

## 12 AWG Copper Conductor Ampacity (75°C) - NEC vs CEC Comparison

**NEC 2023 Value:**  
25 amperes (Table 310.16) for 12 AWG copper with 75°C insulation (e.g., THWN).

**CEC 2022 Value:**  
Also **25 amperes** (Table 310.16) for identical conditions.

**Key Findings:**
- ✅ **No California amendments** to Table 310.16 for 12 AWG copper at 75°C
- Both codes use **identical ampacity values** for this conductor
- CEC maintains NEC Table 310.16 without modification for this specific size/insulation combination
- California-specific amendments typically appear in other sections (e.g., 625 for EV, 408.2 for panelboards)

**Code References:**
- NEC/CEC Table 310.16 (both show 25A for 12 AWG copper 75°C column)
- No exceptions or amendments found in CEC 2022 for this conductor size

[OK] Source: NEC 2023 and CEC 2022 comparison


---

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 10.3s | **NEC Comparison:** No

**Tools Called:** cec_lookup_conductor_size, compare_with_nec

**Answer:**

## Copper Conductor Size for 60A Circuit at 75°C (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirement**
- **Minimum size**: **6 AWG copper**
- **Ampacity**: 65A (from CEC Table 310.16)
- **Reference**: CEC 2022 Section 310.16

### **NEC 2023 Comparison**
- **Minimum size**: **6 AWG copper**
- **Ampacity**: 65A (from NEC Table 310.16)
- **Reference**: NEC 2023 Section 310.16

### **Key Findings**
- Both codes specify **6 AWG copper** as the minimum size for a 60A circuit at 75°C.
- Ampacity values match exactly in both codes (65A for 6 AWG at 75°C).
- No California amendments affect this specific conductor sizing requirement.

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 9.8s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirement**
- **Required Location**: **All receptacles serving countertop surfaces in kitchens**
- **Section**: CEC 2022 **Section 210.8(A)(6)**
- **Scope**: Applies to 125–250V receptacles installed to serve countertop surfaces
- **Exceptions**: None specified for kitchen countertop GFCI protection
- **Additional Context**: 
  - Part of broader GFCI requirements in dwelling units (Section 210.8)
  - Aligns with NEC but maintains California-specific enforcement

### **NEC 2023 Comparison**
- **Requirement**: Identical to CEC – **Section 210.8(A)(6)**
- **Language**: "Kitchens – where the receptacles are installed to serve the countertop surfaces"
- **No Material Differences**: Both codes require GFCI protection for:
  - Countertop receptacles
  - Sinks (within 6 ft of bowl)
  - Laundry areas
  - Bathrooms, garages, etc.

### **Key Differences**
| Feature                | CEC 2022               | NEC 2023               |
|------------------------|------------------------|------------------------|
| **Kitchen Countertops** | Required (210.8(A)(6)) | Required (210.8(A)(6)) |
| **Exceptions**           | None for countertops    | None for countertops    |
| **Additional Protections** | Same as NEC         | Base NEC requirements  |

### **California-Specific Notes**
- CEC incorporates NEC 2023 requirements with **no amendments** to kitchen GFCI rules
- Enforcement follows same scope as NEC but with **Title 24** integration for residential compliance

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 13.2s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## AFCI Protection for Bedroom Circuits (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirement**
- **Required**: **Yes** for all bedroom circuits in new residential construction  
- **Section**: CEC 2022 **Section 210.12(A)**  
- **Scope**: Applies to **all 120V, 15–20A branch circuits** supplying outlets in bedrooms  
- **Exceptions**: None specified for bedroom AFCI requirements  
- **Protection Methods**:  
  - Combination-type AFCI at the circuit origin (most common)  
  - Alternative methods (e.g., outlet branch-circuit-type AFCI) per 210.12(A)(2)–(6)  

### **NEC 2023 Comparison**
- **Requirement**: Identical to CEC – **Section 210.12(A)**  
- **Language**: "All 120-volt, single-phase, 15- and 20-ampere branch circuits that supply outlets or devices installed in dwelling unit bedrooms shall be protected by a listed combination-type arc-fault circuit interrupter..."  
- **No Material Differences**: Both codes require AFCI protection for:  
  - Bedrooms  
  - Living rooms, kitchens, and other listed areas  

### **Key Differences**
| Feature                | CEC 2022               | NEC 2023               |  
|------------------------|------------------------|------------------------|  
| **Bedroom AFCI**       | Required (210.12(A))   | Required (210.12(A))   |  
| **Exceptions**           | None for bedrooms      | None for bedrooms      |  
| **Protection Methods**   | Same (combination-type preferred) | Same (combination-type preferred) |  

### **California-Specific Notes**
- CEC incorporates NEC 2023 requirements with **no amendments** to bedroom AFCI rules  
- Enforcement follows same scope as NEC but with **Title 24** integration for residential compliance  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 34.7s | **NEC Comparison:** No

**Tools Called:** cec_lookup_conductor_size, compare_with_nec

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirement**
- **Minimum size**: **4/0 AWG aluminum**  
- **Ampacity**: 200A (from **Table 310.12(A)** for single-phase dwelling services)  
- **Reference**: CEC 2022 **Section 310.12(A)**  
- **Limiting Rules**:  
  - **240.4(D)**: Overcurrent protection for aluminum conductors must not exceed 70% of ampacity (200A OCPD is allowed for 200A ampacity).  
  - **110.14(C)**: Termination temperature limitations (ensure equipment is rated for aluminum).  

### **NEC 2023 Comparison**
- **Minimum size**: **4/0 AWG aluminum**  
- **Ampacity**: 200A (from **NEC Table 310.12(A)** for single-phase services)  
- **Reference**: NEC 2023 **Section 310.12(A)**  
- **Key Differences**:  
  - **No material differences** in sizing between CEC and NEC for this application.  
  - Both codes use **Table 310.12(A)** for single-phase dwelling services.  

### **California-Specific Notes**
- CEC incorporates NEC 2023 requirements with **no amendments** to aluminum conductor sizing for services.  
- **Title 24** compliance ensures alignment with NEC but adds no additional restrictions for this scenario.  

### **Key Considerations**
1. **Termination Compatibility**: Ensure all equipment (panel, meter base) is rated for aluminum conductors (e.g., **110.14(C)**).  
2. **Corrosion Protection**: Use **aluminum with corrosion-resistant coating** (e.g., AA-8000 series) per CEC 2022 **Section 310.104**.  
3. **Grounding Conductor**: Size equipment grounding conductor per **Table 250.122** (e.g., 6 AWG aluminum for 200A service).  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 15.3s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Working Clearance Depth for Residential Panels (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirement**
- **Minimum depth**: **30 inches (762 mm)**  
- **Condition**: **Condition 1** (exposed live parts on one side, no live/grounded parts on the other)  
- **Reference**: CEC 2022 **Table 110.26(A)(1)**  
- **Key Notes**:  
  - Applies to **120/240V residential panels**.  
  - If live parts exist on both sides (Condition 3), depth increases to **36 inches (914 mm)**.  
  - **Title 24** compliance ensures no additional restrictions for standard residential installations.  

---

### **NEC 2023 Comparison**
- **Minimum depth**: **30 inches (762 mm)**  
- **Condition**: **Condition 1** (same as CEC)  
- **Reference**: NEC 2023 **Table 110.26(A)(1)**  
- **Key Notes**:  
  - Identical requirements for **Condition 1** working space.  
  - No material differences in depth for residential panels.  

---

### **Key Differences**
| Feature                | CEC 2022               | NEC 2023               |  
|------------------------|------------------------|------------------------|  
| **120/240V, Condition 1** | 30 inches (762 mm)     | 30 inches (762 mm)     |  
| **Condition 3 (both sides live)** | 36 inches (914 mm) | 36 inches (914 mm)     |  
| **Additional Rules**   | Same as NEC            | Base NEC requirements  |  

---

### **California-Specific Notes**
- CEC 2022 **fully alignss with NEC 2023** for residential working space requirements.  
- **Title 24** (CALGreen) does not impose stricter rules for standard residential panels.  
- **Exceptions**: Existing buildings or low-voltage systems may have relaxed requirements, but these do not apply to new construction.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 11.8s | **NEC Comparison:** No

**Tools Called:** cec_search, nec_search, compare_with_nec

**Answer:**

## Small Appliance Branch Circuits in Kitchens (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirement**
- **Minimum required**: **2 circuits**  
- **Section**: CEC 2022 **Section 210.11(C)(1)** and **210.52(B)(3)**  
- **Scope**: Applies to **kitchen, pantry, breakfast room, dining room**  
- **Key Notes**:  
  - Each circuit must be **20-ampere, 120-volt**.  
  - **No exceptions** for reducing the number of circuits.  
  - Circuits must serve **all wall, floor, and countertop receptacles** in these areas.  
  - **Title 24** compliance ensures alignment with NEC but adds no additional requirements.  

---

### **NEC 2023 Comparison**
- **Minimum required**: **2 circuits**  
- **Section**: NEC 2023 **Section 210.11(C)(1)** and **210.52(B)(3)**  
- **Scope**: Same as CEC (kitchen, pantry, breakfast room, dining room)  
- **Key Notes**:  
  - Identical requirements to CEC for minimum circuits.  
  - No small-appliance branch circuit may serve **more than one kitchen**.  

---

### **Key Differences**
| Feature                | CEC 2022               | NEC 2023               |  
|------------------------|------------------------|------------------------|  
| **Minimum circuits**   | 2 (kitchen/pantry)     | 2 (kitchen/pantry)     |  
| **Voltage/Amperage**   | 120V, 20A              | 120V, 20A              |  
| **Additional Rules**   | Same as NEC            | Base NEC requirements  |  

---

### **California-Specific Notes**
- CEC 2022 **fully aligns with NEC 2023** for small appliance circuits.  
- **Title 24** does not impose stricter requirements for this application.  
- **Exceptions**: None—minimum of 2 circuits is mandatory.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 16.0s | **NEC Comparison:** No

**Tools Called:** cec_search, nec_search, compare_with_nec

**Answer:**

## Surge Protection for Residential Services (CEC 2022 vs NEC 2023)

### **CEC 2022 Requirement**
- **Required**: **Yes** for services supplying dwelling units.  
- **Section**: **230.67(A)**  
  - *"All services supplying dwelling units shall be provided with a surge-protective device (SPD)."*  
- **SPD Type**: **Type 1 or Type 2** (Section 230.67(C)).  
- **Location**: Must be **integral to service equipment** or **immediately adjacent** (Section 230.67(B)).  
- **Exceptions**: None for standard residential services.  

---

### **NEC 2023 Requirement**
- **Required**: **Yes** for services supplying dwelling units.  
- **Section**: **230.67(A)** (identical to CEC):  
  - *"All services supplying dwelling units shall be provided with a surge-protective device (SPD)."*  
- **SPD Type**: **Type 1 or Type 2** (NEC 230.67(C)).  
- **Location**: Must be installed **in or adjacent to distribution equipment** on the **load side of the service disconnect** (NEC 215.18(B)).  
- **Additional Notes**:  
  - **Informational Note**: SPDs are most effective when installed **closest to the branch circuit**.  
  - **Surge sources**: Lightning, utility grid, or utilization equipment.  

---

### **Key Differences**
| Feature                | CEC 2022               | NEC 2023               |  
|------------------------|------------------------|------------------------|  
| **SPD Requirement**   | Required for services  | Required for services  |  
| **Applicable Section** | 230.67                 | 230.67                 |  
| **SPD Type**           | Type 1 or Type 2       | Type 1 or Type 2       |  
| **Installation Location**| Integral to service equipment or adjacent | Load side of service disconnect |  
| **Exceptions**         | None                   | None                   |  

---

### **California-Specific Notes**
- CEC 2022 **fully adopts NEC 2023** requirements for surge protection.  
- **Title 24** does not add stricter rules for residential services.  
- **UL 1449** compliance required for SPDs (both codes).  

---

### **Conclusion**
- **Both CEC 2022 and NEC 2023 require surge protection** for residential services (200A or any size).  
- **SPD must be Type 1 or 2** and installed per code-specified locations.  
- **No exceptions** for standard residential services in either code.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 24.3s | **NEC Comparison:** No

**Tools Called:** cec_lookup_conductor_size, compare_with_nec

**Answer:**

## Service Conductor Sizing for 200A Residential Upgrade (CEC 2022 vs NEC 2023)

---

### **1. Conductor Sizing Requirements**
#### **California Electrical Code (CEC 2022)**
- **Copper**: **4/0 AWG** (200A at 75°C)  
- **Aluminum**: **250 kcmil** (200A at 75°C)  
- **Reference**: CEC **Table 310.16** (general conductors) and **240.4(D)** (overcurrent protection limits)  
- **Key Rule**: Conductors must have an ampacity **equal to or greater than** the overcurrent device rating (200A).  

#### **National Electrical Code (NEC 2023)**
- **Copper**: **4/0 AWG** (200A at 75°C)  
- **Aluminum**: **250 kcmil** (200A at 75°C)  
- **Reference**: NEC **Table 310.16** and **240.4(D)**  
- **Key Rule**: Same as CEC—conductors must meet or exceed the overcurrent device rating.  

---

### **2. Aluminum Use Permissibility**
#### **CEC 2022**
- **Permitted** if:  
  - Conductors are **250 kcmil aluminum** (200A at 75°C).  
  - Terminals are rated for **aluminum** (marked "AL" or "AL/CU").  
  - **Anti-oxidant compound** is applied at connections.  
- **Code Reference**: CEC **110.14(C)**  

#### **NEC 2023**
- **Permitted** under identical conditions:  
  - Same conductor size and terminal requirements.  
  - **Code Reference**: NEC **110.14(C)**  

---

### **3. Code Comparison Summary**
| **Feature**                | **CEC 2022**                          | **NEC 2023**                          |  
|-----------------------------|---------------------------------------|---------------------------------------|  
| **Minimum Conductor Size**   | 4/0 Cu or 250 kcmil Al                | 4/0 Cu or 250 kcmil Al                |  
| **Overcurrent Protection**   | 240.4(D) applies (200A limit)         | 240.4(D) applies (200A limit)         |  
| **Aluminum Permissibility**  | Yes (with proper terminals)           | Yes (with proper terminals)           |  
| **Key Tables**               | Table 310.16 (ampacity)               | Table 310.16 (ampacity)               |  

---

### **4. California-Specific Notes**
- **Title 24** does not impose stricter conductor sizing rules.  
- **CALGreen** mandates energy efficiency but does not affect conductor sizing.  
- **Exception**: If service is in a seismic zone, additional support requirements apply (CEC 314.29).  

---

### **Final Answer**
- **Service Conductors**: **4/0 AWG copper** or **250 kcmil aluminum** (200A at 75°C).  
- **Aluminum Use**: Permitted **if** terminals are rated for aluminum and proper connections are made.  
- **Code Alignment**: CEC 2022 and NEC 2023 requirements are **identical** for this application.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 20.3s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Multiwire Branch Circuit Requirements (CEC 2022 vs NEC 2023)

---

### **1. Circuit Breaker Requirements**
#### **CEC 2022**
- **Common Trip Device**: Required for multiwire branch circuits (210.4(B)).  
  - *"Each multiwire branch circuit shall be provided with a means that will simultaneously disconnect all ungrounded conductors."*  
- **Permitted Methods**:  
  - **2-pole breaker** with a common trip mechanism.  
  - **Single-pole breakers with identified handle ties** (240.15(B)(1)) for line-to-neutral loads (e.g., kitchen receptacles).  
- **Purpose**: Prevents overloading the neutral conductor if one hot leg is energized while the other is not.  

#### **NEC 2023**
- **Same as CEC**: NEC **210.4(B)** and **240.15(B)(1)** mirror CEC requirements.  
- **Key Note**: Handle ties are explicitly permitted for single-phase line-to-neutral loads.  

---

### **2. Neutral Termination Requirements**
#### **CEC 2022**
- **Sizing**: Neutral conductor must be **same size as ungrounded conductors** (12 AWG in this case).  
  - *"The neutral conductor shall be sized to carry the maximum unbalanced load."* (220.61)  
- **Harmonic Currents**: No special sizing required for kitchen receptacles (non-linear loads not typical).  

#### **NEC 2023**
- **Same as CEC**: NEC **220.61** aligns with CEC 220.61.  
- **Key Note**: Neutral must not be shared with other circuits unless explicitly permitted (not applicable here).  

---

### **3. Code Comparison Summary**
| **Feature**                | **CEC 2022**                          | **NEC 2023**                          |  
|-----------------------------|----------------------------------------|----------------------------------------|  
| **Breaker Type**            | 2-pole or handle-tied single-pole      | 2-pole or handle-tied single-pole      |  
| **Neutral Sizing**          | 12 AWG (same as hots)                  | 12 AWG (same as hots)                  |  
| **Harmonic Currents**       | Not addressed (standard sizing)        | Not addressed (standard sizing)        |  
| **Key Sections**            | 210.4(B), 240.15(B)(1), 220.61         | 210.4(B), 240.15(B)(1), 220.61         |  

---

### **4. California-Specific Notes**
- **Title 24**: No amendments to multiwire branch circuit requirements.  
- **CALGreen**: No impact on circuit breaker or neutral sizing.  

---

### **Final Answer**
- **Circuit Breaker**: Must use **2-pole breaker** or **handle-tied single-pole breakers** to disconnect all ungrounded conductors simultaneously.  
- **Neutral Termination**: **12 AWG** (same size as hots) to handle unbalanced loads.  
- **Code Alignment**: CEC 2022 and NEC 2023 requirements are **identical** for this application.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 23.1s | **NEC Comparison:** No

**Tools Called:** cec_search, nec_search, compare_with_nec

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (NEC 2023 vs CEC 2022)

---

### **NEC 2023 Requirements (210.8)**  
GFCI protection is **required** for all 125–250V receptacles in the following **11 locations**:  
1. **Bathrooms**  
2. **Garages** (and accessory buildings at or below grade)  
3. **Outdoors**  
4. **Crawl spaces** (at or below grade)  
5. **Kitchens** (countertop surfaces)  
6. **Areas with sinks** (food prep/cooking)  
7. **Sinks** (within 6 ft of bowl edge)  
8. **Boathouses**  
9. **Bathtubs/showers** (within 6 ft of edge)  
10. **Laundry areas**  
11. **Indoor damp/wet locations**  

**Additional NEC 2023 Coverage**:  
- **Rooftops** (210.8(B)(5))  
- **Aquariums/bait wells** (210.8(B)(13))  
- **Industrial exceptions** for equipment where GFCI could create hazards (210.8(B)(3)).  

**Exceptions**:  
- Dedicated circuits for snow-melting/deicing (426.28/427.22).  
- HVAC equipment (exception expires 2026).  
- Specific industrial/healthcare exceptions.  

---

### **CEC 2022 Requirements**  
CEC **fully adopts NEC 2023** requirements for GFCI protection. **No additional amendments** are made in CEC 2022 for residential GFCI locations.  

**Key CEC Additions**:  
- **Fountains**: Receptacles within 20 ft of fountain edges (680.58).  
- **Portable generators**: 15-kW or smaller generators must have integral GFCI (445.20).  
- **Nonmetallic extensions**: Must include Class A GFCI protection (382.6).  

---

### **Key Differences**  
| **Location**               | **NEC 2023** | **CEC 2022** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **Rooftops**              | Required     | Not explicitly listed | Covered under "outdoors" in CEC. |  
| **Aquariums**             | Required     | Not explicitly listed | Covered under "indoor damp/wet locations." |  
| **HVAC equipment**        | Exception (2026) | No exception | CEC aligns with NEC until 2026. |  
| **Portable generators**   | Not specified | Required (445.20) | CEC adds GFCI for portable generators. |  

---

### **California-Specific Notes**  
- **Title 24**: No stricter requirements than NEC 2023.  
- **CALGreen**: No impact on GFCI locations.  

---

### **Conclusion**  
- **NEC 2023 and CEC 2022 are identical** in core GFCI requirements for residential dwellings.  
- **CEC adds specific rules** for fountains, portable generators, and nonmetallic extensions.  
- **All 11 locations** in NEC 210.8 apply in California, with **additional CEC coverage** for niche applications.  

[OK] Source: NEC 2023 and CEC 2022 comparison


---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 14.9s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Surge Protection Requirements: CEC 2022 vs NEC 2023

---

### **1. CEC 2022 Mandates Surge Protection**
- **Requirement**: **Mandatory** for all services supplying **dwelling units** (Section 230.67).  
- **SPD Type**: Must be **Type 1 or Type 2**.  
- **Installation Locations**:  
  - **Integral to service equipment** (main panel).  
  - **Adjacent to service equipment**.  
  - **Downstream distribution equipment** (e.g., subpanels) **if not integrated** (Exception to 230.67(B)).  
- **Code Reference**: CEC **230.67**, **242.1**.  

---

### **2. NEC 2023: No Mandatory Requirement**
- **Requirement**: **Not required** for residential services.  
- **Permitted Installation**: SPDs may be installed **at the service entrance** or **branch circuits** for optional protection.  
- **Code Reference**: NEC **230.66**, **250.94**.  

---

### **3. Key Differences**
| **Feature**                | **CEC 2022**                          | **NEC 2023**                          |  
|-----------------------------|----------------------------------------|----------------------------------------|  
| **Mandatory Requirement**   | **Yes** for dwelling units            | **No** requirement                     |  
| **SPD Type**                | Type 1 or Type 2                      | No type restriction (optional)         |  
| **Installation Locations**  | Service equipment, adjacent, or downstream | Service entrance or branch circuits |  
| **Exceptions**              | Permits downstream installation       | No exceptions (optional only)          |  

---

### **4. California-Specific Notes**
- **Title 24**: Enforces CEC 230.67 as law—surge protection is **required** for all residential services.  
- **CALGreen**: No additional mandates.  
- **Exceptions**: SPDs may be installed in subpanels if not integrated into the main service equipment.  

---

### **5. Final Answer**
- **Requirement**: **Mandatory under CEC 2022** for residential services; **not required under NEC 2023**.  
- **Installation**: Must be **Type 1 or 2 SPD** at the service equipment, adjacent location, or downstream distribution equipment.  
- **Code Difference**: CEC is **more restrictive** than NEC by mandating SPDs for dwelling units.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 16.4s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Working Space Clearance for 120V Panel: CEC 2022 vs NEC 2023

---

### **1. Code Requirements for 120V Panels**
#### **Front Clearance (Depth)**  
- **CEC 2022**:  
  - **30 inches** required (Table 110.26(A)(1), Condition 1 for 0–150V).  
- **NEC 2023**:  
  - **30 inches** required (Table 110.26(A)(1), Condition 1 for 0–150V).  

#### **Side Clearance**  
- **CEC 2022**:  
  - **No minimum distance** specified (110.26(A)(1)).  
- **NEC 2023**:  
  - **No minimum distance** specified (110.26(A)(1)).  

---

### **2. Your Setup Evaluation**
| **Measurement**       | **Requirement** | **Your Setup** | **Compliance** |  
|------------------------|-----------------|----------------|----------------|  
| **Front clearance**    | 30 inches       | 24 inches      | ❌ Fails         |  
| **Side clearance**     | No minimum      | 18 inches      | ✅ Acceptable    |  

---

### **3. Code Comparison Summary**
| **Feature**            | **CEC 2022** | **NEC 2023** | **Notes** |  
|-------------------------|--------------|--------------|-----------|  
| **Front clearance**     | 30 inches    | 30 inches    | Identical |  
| **Side clearance**      | No minimum   | No minimum   | No obstruction = acceptable |  
| **California amendments** | None         | N/A          | CEC aligns fully with NEC |  

---

### **4. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on working space.  

---

### **5. Final Answer**
- **Front Clearance**: **Does not meet** CEC/NEC requirements (24 inches < 30 inches).  
- **Side Clearance**: **Acceptable** (18 inches to the side is permitted if not obstructinging working space).  
- **Remedy**: Increase front clearance to **at least 30 inches**.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 14.6s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Dual Conductor on Breaker Terminal: CEC 2022 vs NEC 2023

---

### **1. Code Requirements**
#### **Terminal Markings (110.14(A))**
- **CEC 2022**:  
  - Terminals **not marked for multiple conductors** must have **only one conductor**.  
  - If two conductors are used, the terminal must be **marked "2"** (Section 110.14(A)).  
- **NEC 2023**:  
  - Identical requirement: Terminals **not marked for multiple conductors** must have **only one conductor** (Section 110.14(A)).  

#### **Overcurrent Protection (240.4(D))**
- **12 AWG copper conductors** must be protected at **20A maximum** (both CEC and NEC).  

---

### **2. Your Setup Evaluation**
| **Factor**               | **Requirement**                     | **Your Setup**                     | **Compliance** |  
|--------------------------|--------------------------------------|------------------------------------|----------------|  
| **Conductor size**       | 12 AWG protected at 20A                | 12 AWG on 20A breaker              | ✅ Acceptable    |  
| **Terminal marking**     | Must be marked "2" for dual conductors | Terminal **not marked** for two    | ❌ Violation     |  

---

### **3. Code Comparison Summary**
| **Feature**              | **CEC 2022** | **NEC 2023** | **Notes** |  
|--------------------------|--------------|--------------|-----------|  
| **Dual conductor allowed** | ❌ No        | ❌ No        | Only permitted if terminal is marked "2". |  
| **Overcurrent limit**     | 20A for 12 AWG | 20A for 12 AWG | Identical. |  
| **California amendments**  | None         | N/A          | CEC aligns fully with NEC. |  

---

### **4. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on breaker/terminal requirements.  

---

### **5. Final Answer**
- **Violation**: **Yes**. The terminal is **not marked for two conductors**, violating **CEC 2022 110.14(A)** and **NEC 2023 110.14(A)**.  
- **Remedy**:  
  - Use a **breaker terminal marked "2"** for dual conductors.  
  - Alternatively, use a **single conductor** per terminal.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 19.2s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Grounding Electrode Conductor Sizing for Detached Garage: CEC 2022 vs NEC 2023

---

### **1. Code Requirements for Grounding Electrode Conductor**
#### **CEC 2022**  
- **Section 250.66**:  
  - Grounding electrode conductor size must be **not less than Table 250.66** values.  
  - **No exceptions** for concrete-encased electrodes (unlike NEC 250.35(B)).  
  - Example: For a 200A service, use **2/0 AWG copper** (Table 250.66).  

#### **NEC 2023**  
- **Section 250.66**:  
  - Same base sizing as CEC (Table 250.66).  
  - **Exception**: For concrete-encased electrodes, conductor size may be **4 AWG copper** (Section 250.35(B)).  

---

### **2. Key Differences**  
| **Feature**                | **CEC 2022**                          | **NEC 2023**                          |  
|----------------------------|----------------------------------------|----------------------------------------|  
| **Concrete-encased electrode exception** | **No exception** (must follow Table 250.66) | **4 AWG copper allowed** (Section 250.35(B)) |  
| **Grounding electrode conductor continuity** | Must be **continuous** (250.64(C)) | Must be **continuous** (250.64(C)) |  
| **California amendments**   | No additional exceptions                | N/A                                    |  

---

### **3. California-Specific Notes**  
- **Title 24**: Enforces strict adherence to Table 250.66—no 4 AWG exception for concrete-encased electrodes.  
- **CALGreen**: No impact on grounding electrode conductor sizing.  

---

### **4. Final Answer**  
- **Grounding Electrode Conductor Size**:  
  - **CEC 2022**: Must follow **Table 250.66** (e.g., 2/0 AWG for 200A service).  
  - **NEC 2023**: May use **4 AWG copper** for concrete-encased electrodes (exception in 250.35(B)).  
- **Compliance**: California (CEC) is **more restrictive** than NEC by disallowing the 4 AWG exception.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 19.2s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Main Bonding Jumper vs. System Bonding Jumper: CEC 2022 vs NEC 2023

---

### **1. Definitions**
#### **Main Bonding Jumper (MBJ)**  
- **CEC 2022 250.28**:  
  - Connects the **grounded (neutral) conductor** to the **equipment grounding conductor** in **service equipment** (main panel).  
  - Ensures equipotential bonding at the service disconnect.  

- **NEC 2023 250.28**:  
  - Identical definition and purpose.  

#### **System Bonding Jumper (SBJ)**  
- **CEC 2022 250.30**:  
  - Connects the **grounded conductor** to the **equipment grounding conductor** in **separately derived systems** (e.g., transformers, generators).  
  - Required to bond the system to the equipment grounding system.  

- **NEC 2023 250.30**:  
  - Identical definition and purpose.  

---

### **2. Key Differences**
| **Feature**               | **Main Bonding Jumper (MBJ)**                     | **System Bonding Jumper (SBJ)**                     |  
|----------------------------|---------------------------------------------------|-----------------------------------------------------|  
| **Location**              | **Service equipment** (main panel)                | **Separately derived systems** (e.g., transformers) |  
| **Purpose**               | Bonds grounded conductor to equipment grounding at the service | Bonds grounded conductor to equipment grounding in separately derived systems |  
| **Required When**         | In **service disconnects**                        | In **separately derived systems**                   |  
| **Sizing Reference**      | **Table 250.102(C)(1)** (based on service conductor size) | **Table 250.102(C)(1)** (based on largest ungrounded conductor in the derived system) |  

---

### **3. Code Comparison Summary**
| **Feature**               | **CEC 2022** | **NEC 2023** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **MBJ in service equipment** | Required     | Required     | Identical. |  
| **SBJ in separately derived systems** | Required     | Required     | Identical. |  
| **Sizing method**         | Table 250.102(C)(1) | Table 250.102(C)(1) | Identical. |  
| **California amendments**  | None         | N/A          | CEC aligns fully with NEC. |  

---

### **4. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on bonding jumper requirements.  

---

### **5. Final Answer**
- **Main Bonding Jumper (MBJ)**:  
  - Required in **service equipment** to bond the grounded conductor to the equipment grounding conductor.  
  - Size per **Table 250.102(C)(1)** (based on service conductor size).  

- **System Bonding Jumper (SBJ)**:  
  - Required in **separately derived systems** (e.g., transformers, generators) to bond the grounded conductor to the equipment grounding conductor.  
  - Size per **Table 250.102(C)(1)** (based on largest ungrounded conductor in the derived system).  

- **Code Alignment**: CEC 2022 and NEC 2023 requirements are **identical** for both jumpers.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 17.5s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Small Appliance Branch Circuits in Kitchens: CEC 2022 vs NEC 2023

---

### **1. Code Requirements**
#### **Minimum Number of Circuits**
- **CEC 2022 210.52(B)(1)**:  
  - **Two 20-amp small appliance branch circuits** are required to serve **kitchen countertop, dining room, pantry, and breakfast room receptacles**.  
  - These circuits must supply **all receptacles** in these areas (including countertop and refrigeration equipment).  

- **NEC 2023 210.52(B)(1)**:  
  - Identical requirement: **Two 20-amp circuits** for kitchen countertop and dining area receptacles.  

#### **Dining Room Receptacles**
- **CEC 2022 210.52(B)(1)**:  
  - The two circuits **can serve dining room receptacles** if they are **within the same area** (e.g., adjacent dining room).  
  - **Prohibited**: Circuits cannot serve other areas (e.g., garage, outdoor receptacles).  

- **NEC 2023 210.52(B)(3)**:  
  - Same allowance: Dining room receptacles are permitted on the two kitchen circuits if they are **part of the same space**.  

---

### **2. Code Comparison Summary**
| **Feature**               | **CEC 2022** | **NEC 2023** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **Minimum circuits required** | 2 (20-amp)   | 2 (20-amp)   | Identical. |  
| **Dining room receptacles allowed** | ✅ Yes (same area) | ✅ Yes (same area) | Identical. |  
| **Prohibited loads**       | No garage/outdoor loads | No garage/outdoor loads | Identical. |  
| **California amendments**  | None         | N/A          | CEC aligns fully with NEC. |  

---

### **3. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on small appliance circuit requirements.  

---

### **4. Final Answer**
- **Number of Circuits**: **Two 20-amp small appliance branch circuits** are required for the kitchen countertop and dining area (CEC 2022 210.52(B)(1) / NEC 2023 210.52(B)(1)).  
- **Dining Room Receptacles**:  
  - **Allowed** if they are **within the same area** (e.g., adjacent dining room).  
  - **Prohibited** from serving other areas (e.g., garage, outdoor receptacles).  
- **Code Alignment**: CEC 2022 and NEC 2023 requirements are **identical**.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 19.4s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Adjusted Ampacity for 12 AWG THHN Conductors: CEC 2022 vs NEC 2023

---

### **1. Base Ampacity**  
- **CEC 2022 Table 310.16**:  
  - 12 AWG THHN (90°C column) = **35A**.  
- **NEC 2023 Table 310.16**:  
  - Identical: **35A**.  

---

### **2. Temperature Correction Factor**  
- **Ambient Temperature**: 50°C.  
- **CEC 2022 Table 310.15(B)(1)**:  
  - For 90°C insulation at 50°C ambient = **0.82**.  
- **NEC 2023 Table 310.15(B)(1)(1)**:  
  - Identical: **0.82**.  

---

### **3. Bundling Adjustment Factor**  
- **Number of Conductors**: 6 current-carrying conductors.  
- **CEC 2022 Table 310.15(C)(1)**:  
  - For 4–6 conductors = **0.80**.  
- **NEC 2023 Table 310.15(C)(1)**:  
  - Identical: **0.80**.  

---

### **4. Adjusted Ampacity Calculation**  
$$
35A \times 0.82 \times 0.80 = 23.1A
$$

---

### **5. Termination Limitations**  
- **CEC 2022 110.14(C)**:  
  - If conductors are terminated at **60°C**, ampacity is limited to **20A** (Table 310.16, 60°C column).  
  - If terminated at **75°C**, ampacity is limited to **30A** (Table 310.16, 75°C column).  
  - **Final Allowable Ampacity**: **23.1A** (if terminations are 75°C).  

- **NEC 2023 110.14(C)**:  
  - Identical limitations: **20A** (60°C) or **30A** (75°C).  

---

### **6. Code Comparison Summary**  
| **Feature**               | **CEC 2022** | **NEC 2023** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **Base ampacity (THHN)**   | 35A          | 35A          | Identical. |  
| **Temperature correction** | 0.82         | 0.82         | Identical. |  
| **Bundling adjustment**    | 0.80         | 0.80         | Identical. |  
| **Final adjusted ampacity** | 23.1A        | 23.1A        | Identical. |  
| **Termination limits**     | 20A/30A      | 20A/30A      | Identical. |  

---

### **7. Final Answer**  
- **Adjusted Ampacity**: **23.1A** (calculated value).  
- **Final Allowable Ampacity**:  
  - **20A** if terminated at **60°C**.  
  - **23.1A** if terminated at **75°C**.  
- **Code Alignment**: CEC 2022 and NEC 2023 calculations are **identical**.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 14.5s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## AFCI Protection in Bedrooms and Living Areas: CEC 2022 vs NEC 2023

---

### **1. Code Requirements**
#### **CEC 2022 210.12(A)(1)**  
- **AFCI Protection Required**:  
  - All **15- and 20-ampere branch circuits** in **bedrooms, living rooms, family rooms, dining rooms, and similar areas** of dwelling units.  
  - **Exclusions**: Circuits for appliances, lighting, or smoke alarms.  

#### **NEC 2023 210.12(A)(1)**  
- **Identical Requirement**:  
  - Same locations and exclusions as CEC 2022.  

---

### **2. Electrical Hazard Prevented**
- **Arc Faults**:  
  - Arcs occur due to **damaged insulation**, **loose connections**, or **cord damage**.  
  - **Risk**: Arcs can ignite surrounding materials (e.g., wood, fabric), causing **electrical fires**.  
  - **AFCI Function**: Detects high-energy arc faults and interrupts the circuit before a fire starts.  

---

### **3. Code Comparison Summary**
| **Feature**               | **CEC 2022** | **NEC 2023** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **AFCI required in bedrooms/living areas** | ✅ Yes         | ✅ Yes         | Identical. |  
| **Excluded circuits**       | Appliances, lighting, smoke alarms | Same exclusions | Identical. |  
| **California amendments**   | None         | N/A          | CEC aligns fully with NEC. |  

---

### **4. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on AFCI requirements.  

---

### **5. Final Answer**
- **Requirement**: AFCI protection is required for **15- and 20-ampere circuits** in **bedrooms, living rooms, and similar areas** to prevent **electrical fires caused by arc faults**.  
- **Hazard Prevented**: Arc faults from damaged wiring or cords, which can ignite surrounding materials.  
- **Code Alignment**: CEC 2022 and NEC 2023 requirements are **identical**.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 15.3s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Torque Specifications for Conductor Terminations: CEC 2022 vs NEC 2023

---

### **1. Importance of Torque Specifications**
- **Safety**: Ensures secure, low-resistance connections to prevent arcing, overheating, and fire hazards.  
- **Equipment Longevity**: Prevents damage to terminals from over-tightening or loose connections.  
- **Code Compliance**: Mandated by CEC and NEC to ensure consistent, safe installations.  

---

### **2. Code Requirements**
#### **CEC 2022 110.3(B)**  
- **Torque Values**:  
  - All threaded fasteners for conductor terminations must be tightened to the **manufacturer’s specified torque**.  
  - Equipment must be **labeled with torque values**.  
  - **Torque-rated tools** must be used for installation.  

#### **NEC 2023 110.3(B)**  
- **Identical Requirement**:  
  - Same emphasis on **manufacturer-specified torque** and **torque-rated tools**.  

#### **Additional CEC Reference: 110.14(C)(D)**  
- **Terminal Connection Torque**:  
  - Tightening torque must match values indicated on equipment or in manufacturer instructions.  
  - **Approved methods** include torque tools, shear bolts, or breakaway devices with visual indicators.  

#### **NEC 2023 110.14(C)(2)**  
- **Identical Language**:  
  - Requires coordination of conductor temperature ratings with termination provisions.  

---

### **3. Code Comparison Summary**
| **Feature**               | **CEC 2022** | **NEC 2023** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **Torque specifications** | ✅ 110.3(B)  | ✅ 110.3(B)  | Identical. |  
| **Labeling requirement**  | ✅ Yes       | ✅ Yes       | Identical. |  
| **Torque tool requirement** | ✅ Yes      | ✅ Yes       | Identical. |  
| **California amendments** | None         | N/A          | CEC aligns fully with NEC. |  

---

### **4. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on torque specifications.  

---

### **5. Final Answer**
- **Why Torque Specs Matter**:  
  - Prevents loose connections (arcing, overheating) and terminal damage.  
  - Ensures compliance with safety standards and equipment longevity.  
- **Code References**:  
  - **CEC 2022**: 110.3(B) (torque values), 110.14(C)(D) (termination methods).  
  - **NEC 2023**: Identical sections and requirements.  
- **Code Alignment**: CEC 2022 and NEC 2023 are **fully aligned** on torque specifications.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 18.9s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Torque Specifications for Conductor Terminations: CEC 2022 vs NEC 2023

---

### **1. Code Requirements**
#### **CEC 2022 110.3(B)**  
- **Torque Values**:  
  - All threaded fasteners for conductor terminations must be tightened to the **manufacturer’s specified torque**.  
  - Equipment must be **labeled with torque values**.  
  - **Torque-rated tools** must be used for installation.  

#### **NEC 2023 110.3(B)**  
- **Identical Requirement**:  
  - Same emphasis on **manufacturer-specified torque** and **torque-rated tools**.  

---

### **2. Importance of Torque Specifications**
- **Safety**: Ensures secure, low-resistance connections to prevent arcing, overheating, and fire hazards.  
- **Equipment Longevity**: Prevents damage to terminals from over-tightening or loose connections.  
- **Code Compliance**: Mandated by CEC and NEC to ensure consistent, safe installations.  

---

### **3. Code Comparison Summary**
| **Feature**               | **CEC 2022** | **NEC 2023** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **Torque specifications** | ✅ 110.3(B)  | ✅ 110.3(B)  | Identical. |  
| **Labeling requirement**  | ✅ Yes       | ✅ Yes       | Identical. |  
| **Torque tool requirement** | ✅ Yes      | ✅ Yes       | Identical. |  
| **California amendments** | None         | N/A          | CEC aligns fully with NEC. |  

---

### **4. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on torque specifications.  

---

### **5. Final Answer**
- **Why Torque Specs Matter**:  
  - Prevents loose connections (arcing, overheating) and terminal damage.  
  - Ensures compliance with safety standards and equipment longevity.  
- **Code References**:  
  - **CEC 2022**: 110.3(B) (torque values).  
  - **NEC 2023**: Identical sections and requirements.  
- **Code Alignment**: CEC 2022 and NEC 2023 are **fully aligned** on torque specifications.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 16.4s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Residential Panel Working Space Violations: CEC 2022 vs NEC 2023

---

### **1. Code Requirements**
#### **CEC 2022 110.26(A)(1) & (A)(2)**  
- **Working Space Clearances**:  
  - **Depth**: Minimum **30 inches** in front of equipment rated over 120V.  
  - **Width**: Minimum **30 inches** or the width of the equipment, whichever is greater.  
  - **Height**: Minimum **6.5 feet (78 inches)** from the floor to the top of the equipment.  
  - **Clearance**: No obstructions within the working space.  

#### **NEC 2023 110.26(A)(1) & (A)(2)**  
- **Identical Requirements**:  
  - Same depth, width, height, and obstruction rules as CEC 2022.  

---

### **2. Violations Identified**
#### **Violation 1: Insufficient Depth**  
- **Given**: 28 inches depth.  
- **Required**: 30 inches (per 110.26(A)(1)).  
- **Impact**: Risk of inadequate space for safe maintenance.  

#### **Violation 2: Obstruction in Working Space**  
- **Given**: Water heater located 16 inches from the panel.  
- **Required**: No obstructions within the working space (110.26(A)(2)).  
- **Impact**: Obstructs access and creates fire hazard.  

#### **Violation 3: Panel Height Below Minimum**  
- **Given**: Panel mounted at 5 feet (60 inches).  
- **Required**: Minimum 6.5 feet (78 inches) height (110.26(A)(1)).  
- **Impact**: Inadequate clearance for safe operation.  

---

### **3. Code Comparison Summary**
| **Feature**               | **CEC 2022** | **NEC 2023** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **Minimum depth**         | ✅ 30 inches | ✅ 30 inches | Identical. |  
| **Minimum width**         | ✅ 30 inches | ✅ 30 inches | Identical. |  
| **Minimum height**        | ✅ 6.5 feet  | ✅ 6.5 feet  | Identical. |  
| **Obstruction rule**      | ✅ Clear     | ✅ Clear     | Identical. |  
| **California amendments** | None         | N/A          | CEC aligns fully with NEC. |  

---

### **4. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on working space requirements.  

---

### **5. Final Answer**
- **Violations**:  
  1. **Depth**: 28 inches < 30 inches (110.26(A)(1)).  
  2. **Obstruction**: Water heater within working space (110.26(A)(2)).  
  3. **Height**: 5 feet < 6.5 feet (110.26(A)(1)).  
- **Code Alignment**: CEC 2022 and NEC 2023 requirements are **identical**.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 19.5s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Circuit Protection Requirements: CEC 2022 vs NEC 2023

---

### **1. Code Requirements**
#### **(1) Countertop Receptacles (20A Circuits)**  
- **Protection Required**: **GFCI**  
- **NEC 2023 210.8(A)(6)**: All 125V, single-phase, 15- and 20A receptacles in kitchens must have **GFCI protection**.  
- **CEC 2022 210.8(A)(6)**: Identical requirement.  

#### **(2) Dishwasher (15A Dedicated Circuit)**  
- **Protection Required**: **Standard Breaker**  
- **NEC 2023 210.8(A)(6) Exception 2**: Listed appliances (e.g., dishwashers) supplied by a **dedicated branch circuit** are **exempt from GFCI**.  
- **CEC 2022 210.8(A)(6) Exception 2**: Identical exemption.  

#### **(3) Garbage Disposal (15A Dedicated Circuit)**  
- **Protection Required**: **Standard Breaker**  
- **NEC 2023 210.8(A)(6) Exception 2**: Listed appliances on dedicated circuits are **exempt from GFCI**.  
- **CEC 2022 210.8(A)(6) Exception 2**: Identical exemption.  

#### **(4) Refrigerator (20A Dedicated Circuit)**  
- **Protection Required**: **Standard Breaker**  
- **NEC 2023 210.12(A) Exception 2**: AFCI is **not required** for circuits supplying fixed electric refrigeration equipment.  
- **CEC 2022 210.12(A) Exception 2**: Identical exemption.  

---

### **2. Code Comparison Summary**
| **Circuit**               | **NEC 2023** | **CEC 2022** | **Notes** |  
|---------------------------|--------------|--------------|-----------|  
| **Countertop receptacles** | ✅ GFCI      | ✅ GFCI      | Identical. |  
| **Dishwasher**            | ❌ GFCI      | ❌ GFCI      | Exempt. |  
| **Garbage disposal**      | ❌ GFCI      | ❌ GFCI      | Exempt. |  
| **Refrigerator**          | ❌ AFCI      | ❌ AFCI      | Exempt. |  

---

### **3. California-Specific Notes**
- **Title 24**: No additional requirements beyond NEC 2023.  
- **CALGreen**: No impact on circuit protection requirements.  

---

### **4. Final Answer**
- **Countertop receptacles**: **GFCI** (NEC 210.8(A)(6)).  
- **Dishwasher**: **Standard breaker** (NEC 210.8(A)(6) Exception 2).  
- **Garbage disposal**: **Standard breaker** (NEC 210.8(A)(6) Exception 2).  
- **Refrigerator**: **Standard breaker** (NEC 210.12(A) Exception 2).  
- **Code Alignment**: CEC 2022 and NEC 2023 requirements are **identical**.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 25.9s | **NEC Comparison:** No

**Tools Called:** cec_search, compare_with_nec

**Answer:**

## Service Load Calculation for Residential Panel: CEC 2022 vs NEC 2023

---

### **1. Load Calculation Summary**
| **Load Type**               | **Calculation**                                                                 | **VA**       |
|-----------------------------|---------------------------------------------------------------------------------|--------------|
| **General Lighting**        | 3,000 sq ft × 3 VA/ft² (NEC 220.11)                                            | **9,000**    |
| **Small Appliance Circuits**| 2 circuits × 1,500 VA (NEC 220.52) + 75% demand factor                          | **3,375**    |
| **Laundry Circuit**         | 1,500 VA (NEC 220.52)                                                           | **1,500**    |
| **Electric Range**          | 12 kW → 8,000 VA (NEC Table 220.55)                                            | **8,000**    |
| **Dryer**                   | 5,500 VA actual → 5,000 VA minimum (NEC 220.54)                                 | **5,000**    |
| **Air Conditioning**        | 4,600 VA × 125% (NEC 220.18)                                                   | **5,750**    |
| **Total Calculated Load**   | 9,000 + 3,375 + 1,500 + 8,000 + 5,000 + 5,750                                  | **32,625 VA**|

---

### **2. Code Comparison: CEC 2022 vs NEC 2023**
| **Requirement**             | **CEC 2022** | **NEC 2023** | **Notes** |
|-----------------------------|--------------|--------------|-----------|
| **Small Appliance Load**    | ✅ 1,500 VA/circuit | ✅ 1,500 VA/circuit | Identical. |
| **Laundry Circuit Load**    | ✅ 1,500 VA    | ✅ 1,500 VA    | Identical. |
| **Dryer Minimum Load**      | ✅ 5,000 VA    | ✅ 5,000 VA    | Identical. |
| **Range Demand Factor**     | ✅ 8,000 VA    | ✅ 8,000 VA    | Identical. |
| **AC 125% Rule**            | ✅ Applied     | ✅ Applied     | Identical. |
| **California Amendments**     | None           | N/A            | CEC aligns fully with NEC. |

---

### **3. Final Determination**
- **Total Calculated Load**: **32,625 VA** → **135.94 A** (32,625 ÷ 240V).  
- **Panel Rating**: 200A.  
- **Conclusion**: The 200A panel is **adequately sized** (135.94A < 200A).  

---

### **4. Key Code Citations**
- **General Lighting**: NEC 220.11 (3 VA/sq ft).  
- **Small Appliance/Laundry**: NEC 220.52 (75% demand factor).  
- **Dryer**: NEC 220.54 (5,000 VA minimum).  
- **Range**: NEC Table 220.55 (8,000 VA for 12 kW).  
- **Air Conditioning**: NEC 220.18 (125% for largest motor).  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 25.6s | **NEC Comparison:** Yes

**Tools Called:** nec_conduit_fill_calculator, compare_with_nec

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼" RMC Conduit (CEC vs NEC)

### **NEC 2023 Calculation**  
- **Conduit Area (RMC 1¼")**: 1.526 sq in (Chapter 9 Table 4)  
- **40% Fill Limit**: 0.6104 sq in  
- **Conductor Area (10 AWG THHN)**: 0.0211 sq in (Chapter 9 Table 5)  
- **Maximum Conductors**:  
  $$
  \frac{0.6104}{0.0211} \approx 28.9 \rightarrow \textbf{28 conductors}
  $$

---

### **CEC 2022 Comparison**  
- **Same Methodology**: CEC uses **Chapter 9 Table 1** for conduit fill calculations (referenced in CEC Sections 350.22, 326.116, etc.).  
- **No California Amendments**: CEC 2022 does **not amend** conduit fill rules for this scenario.  
- **Result**: **28 conductors** (identical to NEC).  

---

### **Key Differences?**  
- **None Found**:  
  - Both codes use **identical Chapter 9 Tables** for conduit fill calculations.  
  - California has **no amendments** to Table 1, Chapter 9 for this application.  
  - The CEC semantic search confirmed alignment with NEC 2023 (e.g., CEC Sections 350.22 and 326.116 mirror NEC 350.22 and 326.116).  

---

### **Conclusion**  
- **NEC 2023 and CEC 2022 are identical** for this calculation.  
- **Maximum Conductors**: **28** (10 AWG THHN in 1¼" RMC).  
- **California-Specific Notes**:  
  - No exceptions or amendments apply here.  
  - CEC maintains NEC Chapter 9 conduit fill rules without modification.  

[OK] Source: NEC 2023 and CEC 2022 Chapter 9 Tables


---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 26.8s | **NEC Comparison:** No

**Tools Called:** cec_lookup_conductor_resistance, cec_search, compare_with_nec

**Answer:**

## Voltage Drop Compliance: CEC 2022 vs NEC 2023

---

### **1. Code Requirements Comparison**
| **Parameter**               | **CEC 2022** | **NEC 2023** | **Key Differences** |
|-----------------------------|--------------|--------------|---------------------|
| **Voltage Drop Limit**     | ✅ 3% max (210.19(A)(1) Info Note 4) | ✅ 3% max (210.19(A)(1) Info Note 4) | **Identical**. Both codes specify 3% maximum for branch circuits. |
| **Lenient Guideline**       | ❌ Not specified | ⚠� 8% max (Info Note 1) | **NEC allows 8%** as a non-mandatory guideline for planning. |
| **Calculation Method**     | ✅ Same formula | ✅ Same formula | Identical calculation approach. |

---

### **2. Final Answer**
- **Voltage Drop**: **4.36 V (3.63%)** → **Exceeds 3% limit**.  
- **Compliance**: **Non-compliant** with both CEC 2022 and NEC 2023.  
- **Corrective Actions**:  
  1. **Upgrade to 10 AWG** (resistance = 1.20 Ω/1000 ft):  
     $$
     VD = \frac{2 \times 50 \times 1.20 \times 22}{1000} = 2.64 \, \text{V} \, (2.2\%)
     $$
  2. **Reduce distance to 40 ft** with 12 AWG:  
     $$
     VD = \frac{2 \times 40 \times 1.98 \times 22}{1000} = 3.49 \, \text{V} \, (2.91\%)
     $$

---

### **3. Code Citations**
- **CEiling limit**: CEC 210.19(A)(1) and NEC 210.19(A)(1) Informational Note No. 4.  
- **Lenient guideline**: NEC 210.19(A)(1) Informational Note No. 1 (8%).  

[OK] Source: CEC 2022 and NEC 2023 comparison.


---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 14.5s | **NEC Comparison:** Yes

**Tools Called:** cec_base_ampacity, compare_with_nec

**Answer:**

## Adjusted Ampacity Calculation for 12 AWG TW Conductors (CEC vs NEC)

---

### **Final Calculation Summary**  
- **Base Ampacity (CEC/NEC Table 310.16)**:  
  **20 amperes** for 12 AWG TW (60°C rated) copper.  

- **Temperature Correction Factor (43°C ambient)**:  
  **0.71** (CEC/NEC Table 310.15(B)(1)).  

- **Bundling Adjustment Factor (6 conductors)**:  
  **0.80** (CEC/NEC Table 310.15(C)(1)).  

- **Final Adjusted Ampacity**:  
  $$
  20 \, \text{A} \times 0.71 \times 0.80 = \textbf{11.36 amperes} \rightarrow \textbf{11 amperes (rounded)}
  $$

---

### **CEC vs NEC Comparison**  
1. **Base Ampacity**:  
   - **Identical**: Both codes specify **20A** for 12 AWG TW copper (60°C column).  

2. **Temperature Correction**:  
   - **Identical**: Both use **0.71** for 43°C ambient (Table 310.15(B)(1)).  

3. **Bundling Adjustment**:  
   - **Identical**: Both apply **0.80** for 6 conductors (Table 310.15(C)(1)).  

4. **California-Specific Notes**:  
   - **No amendments** to Tables 310.15(B)(1) or 310.15(C)(1) in CEC 2022.  
   - CEC maintains NEC adjustment rules **without modification**.  

---

### **Key Code References**  
- **Base Ampacity**: CEC/NEC Table 310.16  
- **Temperature Correction**: CEC/NEC Table 310.15(B)(1)  
- **Bundling Adjustment**: CEC/NEC Table 310.15(C)(1)  

---

### **Final Answer**  
- **Adjusted Ampacity**: **11 amperes** (after applying temperature and bundling factors).  
- **Code Compliance**: Both CEC 2022 and NEC 2023 yield **identical results** for this calculation.  

[OK] Source: CEC 2022 and NEC 2023 comparison


---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 13.3s | **NEC Comparison:** No

**Tools Called:** cec_lookup_grounding_conductor, nec_lookup_grounding_conductor, compare_with_nec

**Answer:**

## Minimum GEC Size for 1000 kcmil Copper Conductors: CEC 2022 vs NEC 2023

---

### **1. Code Requirements Comparison**
| **Parameter**               | **CEC 2022** | **NEC 2023** | **Notes** |
|-----------------------------|--------------|--------------|-----------|
| **GEC Size (1000 kcmil Cu)** | ✅ 2/0 AWG (Table 250.66) | ✅ 2/0 AWG (Table 250.66) | **Identical**. |
| **Parallel Conductors Rule** | ✅ Use total area (4 × 250 kcmil = 1000 kcmil) | ✅ Same rule | No change. |
| **Material Requirement**   | ✅ Copper only | ✅ Copper only | No change. |

---

### **2. Step-by-Step Calculation**
1. **Total Service Conductor Size**:  
   - 4 × 250 kcmil = **1000 kcmil per phase** (NEC 250.66(A)).  

2. **GEC Size from Table 250.66**:  
   - For **1000 kcmil copper**, GEC = **2/0 AWG** (NEC Table 250.66).  

---

### **3. Code Compliance**
- **CEC 2022**:  
  - 2/0 AWG copper GEC meets Table 250.66 requirements.  
- **NEC 2023**:  
  - Same calculation → **Compliant**.  

---

### **4. Key Observations**
- **No Changes in 2023**: The GEC sizing for 1000 kcmil copper remains **2/0 AWG** in both codes.  
- **Parallel Conductors**: NEC 250.66(A) explicitly requires using the **total area** of parallel conductors for GEC sizing.  

---

### **5. Code Citations**
- **GEC Sizing**: NEC/CEC Table 250.66.  
- **Parallel Conductors Rule**: NEC 250.66(A).  

[OK] Source: NEC 2023 and CEC 2022 comparison.


---
