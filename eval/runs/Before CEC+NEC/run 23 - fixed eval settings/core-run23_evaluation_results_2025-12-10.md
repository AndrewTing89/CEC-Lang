# Core (NEC) Evaluation Results - Run 23

**Date:** 2025-12-10
**Changes:** Fixed eval settings (force_nec_comparison=False)

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 27 |
| Successful | 27 |
| Failed | 0 |
| Success Rate | 100.0% |
| Total Duration | 310.8s |
| Avg Duration | 11.5s |
| Exception Search Used | 0/27 |
| NEC Comparison Used | 0/27 |
| NEC Comparison Forced | No (FIX from Run 22) |

## Results by Question

### baseline-002

**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Duration:** 3.9s | **NEC Comparison:** No

**Tools Called:** cec_lookup_conductor_size

**Answer:**

## Copper Conductor Size for 60A Circuit (CEC 2022)

**Minimum required size**: **6 AWG copper**  
- **Ampacity**: 65A (75°C column, Table 310.16)  
- **Verification**: 65A ≥ 60A required  

**Why not 8 AWG?**  
- 8 AWG copper at 75°C = 50A (insufficient for 60A)  

**Citations**:  
- CEC Table 310.16 (ampacity)  
- CEC 240.4(D) (no conflict - 6 AWG protected at ≤65A)  

[OK] Source: CEC 2022

---

### baseline-003

**Question:** Where is GFCI protection required in a residential kitchen?

**Duration:** 7.3s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## GFCI Protection in Residential Kitchens (CEC 2022)

**Requirement**:  
All **125-volt through 250-volt receptacles** in residential kitchens **serving countertop surfaces** must have **GFCI protection** per **CEC 210.8(A)(6)**.

**Key Details**:  
- Applies to **15- and 20-ampere receptacles** (standard for kitchen countertop circuits).  
- Protection required **within 6 feet of the sink** (implied by general kitchen requirements, though not explicitly stated in 210.8(A)(6)).  
- **No exceptions** for standard countertop receptacles in kitchens.  

**Citations**:  
- **CEC 210.8(A)(6)**: "Kitchens - where the receptacles are installed to serve the countertop surfaces."  
- **CEC 210.8(A)**: General dwelling unit requirements (includes kitchens).  

**Additional Context**:  
- GFCI protection is **mandatory** for personnel safety in areas with water exposure risk (e.g., kitchens, bathrooms).  
- **Exceptions** exist for specific appliances (e.g., hardwired ovens) but **not for standard countertop receptacles**.  

[OK] Source: CEC 2022

---

### baseline-004

**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Duration:** 7.4s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## AFCI Protection for Bedroom Circuits in New Residential Construction (CEC 2022)

**Requirement**:  
Yes, **AFCI protection is required** for all **15- and 20-ampere bedroom circuits** in new residential construction per **CEC 210.12(A)**.

**Key Code Provisions**:  
- **CEC 210.12(A)** mandates AFCI protection for **dwelling unit bedrooms** (among other rooms).  
- Applies to **120-volt, single-phase circuits** supplying outlets in bedrooms.  
- **No exceptions** for new construction (unlike renovations or specific appliance circuits).  

**Protection Methods**:  
1. **Combination-type AFCI** at the panel (most common).  
2. **Branch/feeder-type AFCI** + outlet AFCI at first outlet (less common).  
3. **Supplemental arc protection** + outlet AFCI (with wiring constraints).  

**Citations**:  
- **CEC 210.12(A)**: Explicitly includes bedrooms in required locations.  
- **CEC 210.12(A)(1)**: Lists bedrooms as protected areas.  

**Comparison with NEC**:  
- California adopts **NEC 2023 Section 210.12(A)** without amendment.  
- No additional exceptions in CEC for bedrooms in new construction.  

**Exceptions**:  
- None for **new residential construction**.  
- Renovations may have limited exceptions (see CEC 210.12(D)).  

[OK] Source: CEC 2022

---

### baseline-005

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Duration:** 7.7s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Aluminum Conductors for 200A Service (CEC 2022)

**Answer**:  
Yes, aluminum conductors **can** be used for a 200A service.  

**Minimum Required Size**:  
**2/0 AWG aluminum** (per **CEC Table 310.12(A)** for single-phase dwelling services).  

**Key Details**:  
- **Ampacity**: 205A at 75°C (Table 310.12(A) aluminum column).  
- **Verification**: 205A ≥ 200A service rating.  
- **Termination Compatibility**: Ensure terminals are rated for aluminum (e.g., AA-8000 series).  

**Grounding Electrode Conductor (GEC) Size**:  
- **Minimum**: **4 AWG copper** or **2 AWG aluminum** (per **CEC Table 250.66**, based on 2/0 service conductor).  

**Citations**:  
- **CEC Table 310.12(A)**: Aluminum service conductor sizing for single-phase dwellings.  
- **CEC Table 250.66**: GEC sizing based on service conductor size.  

**Exceptions/Notes**:  
- No exceptions for aluminum in dwelling services (CEC adopts NEC 310.12(A) without amendment).  
- **240.4(D)** does not limit aluminum conductors for services (applies to branch circuits).  

[OK] Source: CEC 2022

---

### baseline-006

**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Duration:** 4.4s | **NEC Comparison:** No

**Tools Called:** cec_lookup_working_space

**Answer:**

## Minimum Working Clearance Depth for Residential Panel (CEC 2022)

**Answer**:  
The **minimum working clearance depth** required in front of a **120/240V residential electrical panel** is **3 feet (900 mm)** when:  
- **Voltage to ground**: 120V (typical for residential panels).  
- **Condition 1**: Exposed live parts on one side of the working space and **no live or grounded parts** on the other side (e.g., panel mounted against a non-conductive wall).  

**Code Reference**:  
- **CEC Table 110.26(A)(1)**: Specifies working space depths based on voltage and conditions.  

**Key Notes**:  
- If the panel is mounted against a **concrete, brick, or tile wall** (considered grounded), **Condition 2** applies, but the depth remains **3 feet** for 120V systems.  
- For higher voltages (e.g., 240V to ground in three-phase systems), greater depths apply (see Table 110.26(A)(1)).  

**Example Application**:  
A standard 120/240V residential service panel with live parts on the front side and a non-conductive wall behind it requires **3 feet of clear working space** in front.  

[OK] Source: CEC 2022 Table 110.26(A)(1)

---

### baseline-007

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Duration:** 9.8s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Minimum Small Appliance Branch Circuits in Kitchens (CEC 2022)

**Answer**:  
**At least two 20-ampere small appliance branch circuits** are required for a kitchen per **CEC 210.52(B)(1)**.  

**Code Requirements**:  
- **CEC 210.52(B)(1)**: Mandates **two or more 20A circuits** to serve all kitchen receptacles, including:  
  - Countertop outlets  
  - Wall and floor receptacles in kitchen areas  
  - Refrigeration equipment  

**Key Details**:  
- **Load Coverage**: Each circuit is calculated at **1,500 VA** (per **CEC Table 220.52**).  
- **No Exceptions for Minimum Number**: California adopts NEC 210.52(B) without amendments.  
- **Additional Circuits Permitted**: More than two circuits may be installed for larger kitchens or islands (see **CEC 210.52(B)(3)**).  

**Citations**:  
- **CEC 210.52(B)(1)**: Minimum two 20A circuits for kitchen small appliance loads.  
- **CEC 210.11(C)(1)**: Requires two or more small-appliance branch circuits for dwelling units.  

**Exceptions**:  
- A receptacle for a specific appliance (e.g., dishwasher) may be on an individual circuit (Exception No. 2 in 210.52(B)(1)).  

[OK] Source: CEC 2022

---

### baseline-008

**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Duration:** 5.5s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## Surge Protection Requirement for Residential Service (NEC 2023)

**Answer**:  
**Yes**, surge protection is **required** for a new **200A residential service** under **NEC 2023 Section 230.67(A)**.  

**Code Requirement**:  
- **NEC 230.67(A)** mandates a **surge-protective device (SPD)** for services supplying:  
  - **Dwelling units** (residential homes)  
  - Dormitory units, hotel/guest rooms, and nursing home patient rooms  

**Key Details**:  
- **SPD Type**: Must be a listed surge-protective device (Type 1 or Type 2) installed at the service entrance.  
- **Application**: Protects against transient overvoltages (lightning, utility switching, etc.).  
- **No Exceptions for Residential Services**: The requirement applies to all dwelling units, including new 200A services.  

**Citations**:  
- **NEC 2023 Section 230.67(A)**: Direct requirement for SPDs in dwelling units.  
- **NEC 230.94**: Permits SPDs on the supply side of the service disconnect (installation guidance).  

**Additional Notes**:  
- **Compliance**: SPD must be installed in accordance with **NEC Article 285** (Surge Protective Devices).  
- **California Adoption**: CEC adopts NEC 230.67(A) without amendments for residential services.  

[OK] Source: NEC 2023

---

### core-001

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Duration:** 17.8s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Service Conductor Sizing for 200A to 300A Upgrade (CEC 2022)

**Answer**:  
**Minimum service conductor size**:  
- **Copper**: **350 kcmil** (310A at 75°C)  
- **Aluminum**: **900 kcmil** (308A at 90°C)  

**Calculation Steps**:  
1. **Load Calculation (CEC 220.82)**:  
   - **General Lighting**: 3,000 sq ft × 3 VA = **9,000 VA**  
   - **Small Appliance Circuits**: 2 × 1,500 VA + 1,500 VA (laundry) = **4,500 VA**  
   - **Range**: 12 kW → **8,000 VA** (per Table 220.55)  
   - **Dryer**: 5.5 kW → **5,000 VA** (per 220.54)  
   - **AC**: 4 tons × 12,000 VA = **48,000 VA**  
   - **Water Heater**: **4,500 VA**  
   - **Total Load**: **79,000 VA**  

2. **Convert to Amperes**:  
   - **79,000 VA ÷ 240V = 329A**  

3. **Demand Factors**:  
   - Apply **35% demand factor** for general lighting/small appliance loads >3,000 VA:  
     - **(9,000 + 4,500 - 3,000) × 0.35 = 3,750 VA**  
     - **Total Load**: 3,000 + 3,750 + 8,000 + 5,000 + 48,000 + 4,500 = **72,250 VA**  
   - **72,250 VA ÷ 240V = 301A**  

4. **Conductor Sizing**:  
   - **Copper**: 350 kcmil (310A at 75°C) from **Table 310.16**  
   - **Aluminum**: 900 kcmil (308A at 90°C) from **Table 310.16**  

**Code References**:  
- **CEC 220.82**: Dwelling unit load calculation method.  
- **CEC 310.16**: Ampacity tables for conductors.  
- **CEC 310.12(A)**: Service conductor minimum sizes (2/0 AWG copper or 4/0 AWG aluminum for 200A, but upsized for calculated load).  

**Key Notes**:  
- **Aluminum Use**: Permitted if ampacity meets load (900 kcmil aluminum at 90°C = 308A).  
- **Service Rating**: **300A** (minimum) to accommodate 301A load.  

**Final Answer**:  
- **Copper**: 350 kcmil (310A)  
- **Aluminum**: 900 kcmil (308A)  
- **Service Rating**: **300A**  

[OK] Source: CEC 2022 Tables 220.55, 220.54, 310.16

---

### core-002

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Duration:** 14.5s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## Multiwire Branch Circuit Requirements (NEC 2023)

**Answer**:  
For a **multiwire branch circuit (MWBC)** using **12/3 cable** in a kitchen, the following NEC requirements apply:

---

### **1. Circuit Breaker Requirements**  
- **Handle-Tied Breakers**:  
  - **Two single-pole breakers** must be **handle-tied** (listed for simultaneous operation) to ensure both ungrounded (hot) conductors are disconnected simultaneously.  
  - **Two-pole breaker** is also acceptable.  
  - **NEC 210.4(B)**: "Multiwire branch circuits shall be provided with a means to disconnect all ungrounded conductors at the point where the branch circuit originates."  

---

### **2. Neutral Conductor Requirements**  
- **Size**:  
  - The **neutral conductor must be at least 12 AWG** (same size as the ungrounded conductors).  
  - **NEC 210.4(A)(2)**: "The neutral conductor shall be sized in accordance with 220.61."  
- **Dedicated Neutral**:  
  - The neutral must **not be shared** with other circuits.  
  - **NEC 210.4(B)**: "The neutral conductor shall not be connected to any other circuit."  
- **No Switching**:  
  - The neutral conductor **must not be switched**.  
  - **NEC 210.4(B)**: "The neutral conductor shall not be connected to a switch."  

---

### **3. Grounding Conductor**  
- **Size**:  
  - The **equipment grounding conductor (EGC)** must be **12 AWG** (same as the ungrounded conductors).  
  - **NEC 250.12(B)**: "The equipment grounding conductor shall be sized in accordance with Table 250.12."  

---

### **4. Additional Requirements**  
- **Load Balancing**:  
  - The MWBC must supply **balanced loads** on both ungrounded conductors to minimize neutral current.  
  - **NEC 210.4(A)(1)**: "The neutral conductor shall be sized to carry the maximum unbalanced current."  
- **Kitchen Application**:  
  - MWBCs are **permitted** for kitchen receptacles, but **two or more 20A circuits** are required (per **NEC 210.52(B)(1)**).  

---

### **Summary**  
- **Breaker**: Two 20A single-pole breakers with a **handle tie** or a two-pole 20A breaker.  
- **Neutral**: 12 AWG, **dedicated and unswitched**.  
- **Grounding**: 12 AWG EGC connected to the panel and all receptacles.  

**Citations**:  
- **NEC 210.4(B)**: Handle-tied breakers for MWBCs.  
- **NEC 210.4(A)(2)**: Neutral conductor sizing.  
- **NEC 250.12(B)**: Grounding conductor sizing.  

[OK] Source: NEC 2023

---

### core-003

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Duration:** 10.1s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

**Answer**:  
GFCI protection is **required** for all receptacles in the following locations per **NEC 210.8(A)(1)–(A)(11)** for residential dwellings:

---

### **1. Bathrooms**  
- **All receptacles** in bathrooms.  
- **Citation**: **NEC 210.8(A)(2)**.

---

### **2. Garages and Accessory Buildings**  
- **All receptacles** in garages and accessory buildings with floors at or below grade level.  
- **Citation**: **NEC 210.8(A)(3)**.

---

### **3. Outdoor Locations**  
- **All outdoor receptacles** (e.g., patios, decks, exterior walls).  
- **Citation**: **NEC 210.8(A)(4)**.

---

### **4. Crawl Spaces**  
- **All receptacles** in crawl spaces at or below grade level.  
- **Citation**: **NEC 210.8(A)(5)**.

---

### **5. Kitchens**  
- **All receptacles** in kitchens, including those within **6 feet of a sink**.  
- **Citation**: **NEC 210.8(A)(5)**.

---

### **6. Sinks and Wet Areas**  
- **Receptacles within 6 feet** of the top inside edge of a sink bowl.  
- **Citation**: **NEC 210.8(A)(7)**.

---

### **7. Boathouses**  
- **All receptacles** in boathouses.  
- **Citation**: **NEC 210.8(A)(8)**.

---

### **8. Bathtubs and Shower Stalls**  
- **Receptacles within 6 feet** of the outside edge of a bathtub or shower stall.  
- **Citation**: **NEC 210.8(A)(9)**.

---

### **9. Laundry Areas**  
- **All receptacles** in laundry rooms.  
- **Citation**: **NEC 210.8(A)(10)**.

---

### **10. Damp/Wet Locations**  
- **All receptacles** in indoor damp or wet locations (e.g., near pools, spas).  
- **Citation**: **NEC 210.8(A)(11)**.

---

### **Key Exceptions**  
- **HVAC equipment**: Exempt until September 1, 2026 (**NEC 210.8(A) Exception No. 2**).  
- **Dedicated circuits for heating/cooling**: May be exempt if not readily accessible (**NEC 210.8(A) Exception No. 1**).  

---

**Citations**:  
- **NEC 210.8(A)(1)–(A)(11)**: Full list of required locations.  
- **NEC 210.8(B)**: Additional requirements for non-dwelling units (not applicable here).  

[OK] Source: NEC 2023

---

### core-004

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Duration:** 9.2s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Surge Protection Requirements for 200A Residential Service (CEC 2022)

**Answer**:  
**Surge protection is required** for a new **200A residential service** per **CEC 230.67**, as services supplying dwelling units must include a **surge-protective device (SPD)**.

---

### **Installation Locations**  
Per **CEC 230.67(B)**, the SPD must be installed:  
1. **Integral to the service equipment** (main panel).  
2. **Immediately adjacent to the service equipment**.  

**Exception**:  
- The SPD may be installed at the **next level of distribution equipment downstream** (e.g., a subpanel) if it is part of the service equipment.  

---

### **Additional Requirements**  
- **SPD Type**: Must be **Type 1 or Type 2** (per **CEC 230.67(C)**).  
- **Supply-Side Installation**: Per **CEC 230.94**, SPDs may be installed on the **supply side of the service disconnect** if permitted by 230.82.  

---

### **Code Citations**  
- **CEC 230.67**: Surge protection for dwelling unit services.  
- **CEC 230.94**: Permits SPDs on the supply side of the service disconnect.  

[OK] Source: CEC 2022

---

### core-005

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Duration:** 9.3s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## Working Space Compliance for Electrical Panel in a Closet (NEC 2023)

**Answer**:  
The installation **does not meet NEC requirements** due to **insufficient front clearance** for the electrical panel.  

---

### **1. Front Clearance Requirements**  
- **Required**: **30 inches** (762 mm) of clear working space in front of the panel for a residential service (120/240V, 120V to ground).  
- **Provided**: **24 inches**.  
- **Citation**: **NEC 110.26(A)(1)** and **Table 110.26(A)(1)** (Condition 1 for 120V-to-ground panels).  

**Issue**: The 24-inch clearance is **6 inches short** of the required 30 inches.  

---

### **2. Side Clearance (Water Heater)**  
- **Distance**: 18 inches to the side of the panel.  
- **NEC Requirement**: No specific minimum side clearance is mandated, but the working space must be **clear of obstructions** (NEC 110.26(A)(2)).  
- **Assessment**:  
  - 18 inches may be **within the required working space** if the water heater is considered an obstruction.  
  - **Remedy**: Relocate or shield the water heater to ensure the working space is unobstructed.  

---

### **3. Key Code Violations**  
- **Front Clearance**: Fails **NEC 110.26(A)(1)** (minimum 30 inches for 120V-to-ground panels).  
- **Side Clearance**: Violates **NEC 110.26(A)(2)** if the water heater impedes access or egress.  

---

### **Conclusion**  
- **Front clearance fails**: 24 inches < 30 inches required.  
- **Side clearance is marginal**: 18 inches may obstruct working space.  

**Remedy**:  
1. Increase front clearance to **at least 30 inches**.  
2. Ensure the water heater is **relocated or shielded** to avoid obstructing the working space.  

[OK] Source: NEC 2023

---

### core-006

**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?

**Duration:** 7.7s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Code Violation for Multiple Conductors on a Single Breaker Terminal (CEC 2022)

**Answer**:  
Yes, this is a **code violation** under **CEC 408.41**.  

---

### **Key Violation**  
- **CEC 408.41** states:  
  > *"Each grounded conductor shall terminate within the panelboard in an individual terminal that is not also used for another conductor."*  
  - **Exception**: Only allowed if the terminal is **specifically identified** for multiple conductors (e.g., marked "2-wire" or "multi-wire").  

- **Your Case**:  
  - The breaker terminal is **not marked** for two conductors.  
  - Two 12 AWG conductors are landed on a single terminal.  

---

### **Risks**  
- **Overheating**: Multiple conductors on a single terminal can cause **poor contact** and **excessive heat**.  
- **Arc Faults**: Loose connections increase the risk of **arc faults** and potential fire hazards.  

---

### **Corrective Actions**  
1. **Use a Terminal Marked for Multiple Conductors**:  
   - Replace the breaker with one **listed for two conductors** (e.g., "2-wire" terminals).  
2. **Pigtail Connection**:  
   - Connect both 12 AWG conductors to a **pigtail** (12 AWG) via a wire nut, then connect the pigtail to the breaker terminal.  

---

### **Code Citations**  
- **CEC 408.41**: Grounded conductor terminations in panelboards.  
- **CEC 110.14(A)**: Terminal connections for circuit breakers (aligns with NEC 110.14(A)).  

[OK] Source: CEC 2022

---

### core-007

**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?

**Duration:** 21.6s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Grounding and Bonding Configuration for Detached Garage Subpanel (CEC 2022)

**Answer**:  
For a **detached garage subpanel** fed by a **4-wire feeder**, the grounding and bonding must comply with **CEC 250.24(D)** and **250.142(A)**. Here's the correct configuration:

---

### **1. Neutral and Ground Separation**  
- **Neutral Bus**: Connect the **neutral conductor** from the feeder to the **neutral bus** in the subpanel.  
- **Grounding Bus**: Connect the **equipment grounding conductor (EGC)** from the feeder to the **grounding bus** in the subpanel.  
- **No Bonding**: **Do not bond** the neutral and grounding buses in the subpanel (CEC 250.142(A)).  

---

### **2. Grounding Electrode Conductor (GEC)**  
- **Not Required**: A **separate grounding electrode conductor (GEC)** is **not connected** in the subpanel.  
- **Main Service Only**: The GEC is connected **only at the main service panel** (CEC 250.24(D)).  

---

### **3. Equipment Grounding**  
- **Bond Subpanel Enclosure**: Connect the **grounding bus** to the subpanel’s metal enclosure (CEC 250.142(B)).  
- **Feeder EGC Size**: Size the EGC based on the **feeder’s overcurrent protection** (e.g., 100A breaker → 8 AWG copper, per Table 250.122).  

---

### **4. Grounding Electrode at Subpanel**  
- **Not Required**: A **separate grounding electrode** (e.g., ground rod) is **not required** at the subpanel unless it is a **separately derived system** (CEC 250.32(B)).  

---

### **5. Key Code Citations**  
- **CEC 250.24(D)**: Grounding of feeder circuits in separate buildings.  
- **CEC 250.142(A)**: Neutral and grounding conductor separation in subpanels.  
- **CEC 250.66**: Sizing of equipment grounding conductors.  

---

### **Summary**  
- **Neutral**: Connected to neutral bus.  
- **Ground**: Connected to grounding bus (no bonding to neutral).  
- **GEC**: Not connected in subpanel.  
- **Enclosure**: Bonded to grounding bus.  

[OK] Source: CEC 2022

---

### core-008

**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?

**Duration:** 10.0s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Difference Between Main Bonding Jumper and System Bonding Jumper (CEC 2022)

### **1. Definitions**  
- **Main Bonding Jumper**:  
  - Connects the **grounded conductor (neutral)** to the **equipment grounding conductor** at the **main service panel** (service equipment).  
  - **Code Reference**: CEC 250.28 and 100.  

- **System Bonding Jumper**:  
  - Connects the **grounded conductor** of a **separately derived system** (e.g., transformer, generator, PV system) to the **equipment grounding conductor** at the **point of connection**.  
  - **Code Reference**: CEC 250.30 and 100.  

---

### **2. Key Differences**  
| **Feature**               | **Main Bonding Jumper**                          | **System Bonding Jumper**                      |
|---------------------------|--------------------------------------------------|------------------------------------------------|
| **Location**              | **Main service panel** (service equipment)       | **Separately derived systems** (e.g., transformers, generators, PV systems) |
| **Purpose**               | Bonds **neutral (grounded conductor)** to **equipment grounding conductor** at the service. | Bonds **grounded conductor** of the derived system to **equipment grounding conductor**. |
| **Code Reference**        | **CEC 250.24(B)**                                | **CEC 250.30(A)**                              |
| **Required in Subpanels** | **No** (neutral and ground must be separated in subpanels). | **Yes** (if the subpanel is fed by a separately derived system). |

---

### **3. When Each is Required**  
#### **Main Bonding Jumper**  
- **Required in**: **Main service panel** (service equipment).  
- **Function**: Ensures the **neutral (grounded conductor)** is bonded to the **equipment grounding conductor** at the service point.  
- **Code**: **CEC 250.24(B)**.  
- **Example**: In a main service panel, the main bonding jumper connects the neutral bus to the equipment grounding conductor (ground bar).  

#### **System Bonding Jumper**  
- **Required in**: **Separately derived systems** (e.g., transformers, generators, photovoltaic systems).  
- **Function**: Bonds the **grounded conductor** of the derived system to the **equipment grounding conductor** at the point of connection.  
- **Code**: **CEC 250.30(A)**.  
- **Example**: In a transformer-derived system, the system bonding jumper connects the transformer’s secondary neutral to the equipment grounding conductor.  

---

### **4. Sizing Requirements**  
- **Main Bonding Jumper**:  
  - Sized per **Table 250.66** based on the **largest service conductor**.  
- **System Bonding Jumper**:  
  - Sized per **Table 250.122** based on the **largest ungrounded conductor** of the derived system.  

---

### **5. Code Citations**  
- **Main Bonding Jumper**:  
  - **CEC 250.24(B)** (installation in service equipment).  
  - **Table 250.66** (sizing).  

- **System Bonding Jumper**:  
  - **CEC 250.30(A)** (installation in derived systems).  
  - **Table 250.122** (sizing).  

---

### **6. Summary of Requirements**  
| **Scenario**                          | **Main Bonding Jumper** | **System Bonding Jumper** |
|---------------------------------------|-------------------------|---------------------------|
| Main service panel                    | ✅ Required             | ❌ Not required           |
| Subpanel fed by main service          | ❌ Not required         | ❌ Not required           |
| Subpanel fed by derived system        | ❌ Not required         | ✅ Required               |
| Transformer secondary (derived system)| ❌ Not required         | ✅ Required               |

[OK] Source: CEC 2022

---

### core-009

**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Duration:** 8.2s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Small Appliance Branch Circuits in Kitchens (CEC 2022)

### **1. Required Number of Circuits**  
- **Minimum Requirement**: **Two 20-ampere small appliance branch circuits** are required for **kitchen countertops and small appliance receptacles**.  
- **Code Reference**: **CEC 210.52(B)(1)** and **210.11(C)(1)**.  

---

### **2. Can These Circuits Serve Dining Room Receptacles?**  
- **Yes**, but with **limitations**:  
  - **Permitted**: Small appliance branch circuits can supply **dining room receptacles** if they are **within 6 feet of the kitchen countertop** (CEC 210.52(B)(1) Exception 1).  
  - **Prohibited**: Dining room receptacles **more than 6 feet from the kitchen** must be on **separate circuits** (e.g., general-purpose branch circuits).  

---

### **3. Key Code Citations**  
- **CEC 210.52(B)(1)**:  
  > *"In the kitchen, pantry, breakfast room, dining room, or similar area of a dwelling unit, the two or more 20-ampere small-appliance branch circuits required by 210.11(C)(1) shall serve all wall and floor receptacle outlets covered by 210.52(A), all countertop outlets covered by 210.52(C), and receptacle outlets for refrigeration equipment."*  
- **CEC 210.52(B)(1) Exception 1**:  
  > *"Receptacles installed solely for the electrical supply to and support of an electric clock in any of the rooms specified in 210.52(B)(1) shall be permitted."*  

---

### **4. Additional Requirements**  
- **Dedicated Circuits**: Small appliance circuits must be **dedicated to the kitchen** and **not shared** with other areas (e.g., laundry, garage).  
- **No Overloading**: Circuits must not supply **fixed appliances** (e.g., ovens, dishwashers) unless specifically permitted (CEC 210.52(B)(1) Exception 2).  

---

### **5. Summary**  
- **Kitchen**: **2 x 20A circuits** required for countertops and small appliances.  
- **Dining Room**: Receptacles **within 6 feet of the kitchen** can be served by small appliance circuits.  
- **Dining Room (Beyond 6 Feet)**: Requires **separate circuits** (not small appliance branch circuits).  

[OK] Source: CEC 2022

---

### core-010

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Duration:** 20.1s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Adjusted Ampacity for 12 AWG THHN Conductors (CEC 2022)

### **1. Base Ampacity**  
- **12 AWG THHN at 90°C**: **30A** (CEC Table 310.16).  

---

### **2. Temperature Correction Factor**  
- **Ambient Temperature**: 50°C  
- **Correction Factor** (Table 310.15(B)(2) for 90°C insulation): **0.71**  

---

### **3. Bundling Adjustment Factor**  
- **Number of Conductors**: 6  
- **Adjustment Factor** (Table 310.15(C)(1) for 4–6 conductors): **0.80**  

---

### **4. Adjusted Ampacity Calculation**  
$$
\text{Adjusted Ampacity} = \text{Base Ampacity} \times \text{Temp Factor} \times \text{Bundling Factor}
$$
$$
= 30 \, \text{A} \times 0.71 \times 0.80 = 17.04 \, \text{A}
$$

---

### **5. Final Result**  
- **Adjusted Ampacity**: **17A** (rounded down per CEC 240.4(B)).  

---

### **6. Code Citations**  
- **Base Ampacity**: CEC Table 310.16  
- **Temperature Correction**: CEC Table 310.15(B)(2)  
- **Bundling Adjustment**: CEC Table 310.15(C)(1)  

[OK] Source: CEC 2022

---

### core-011

**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Duration:** 16.4s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## AFCI Protection Requirements for Bedrooms and Living Areas (NEC 2023)

### **1. Why AFCI Protection is Required**  
- **NEC 210.12(A)** mandates **arc-fault circuit interrupter (AFCI) protection** for **15- and 20-ampere branch circuits** supplying outlets in **bedrooms** of dwelling units.  
- **NEC 210.12(B)** extends this requirement to **living rooms, family rooms, and similar areas** (e.g., dens, recreation rooms).  

---

### **2. Electrical Hazard Prevented**  
AFCI protection prevents **electrical fires caused by arc faults** in the wiring system.  
- **Arc faults** occur when damaged or worn insulation, loose connections, or other wiring issues create high-resistance arcs.  
- These arcs can **generate intense heat (up to 10,000°F)**, igniting nearby combustible materials (e.g., wood, paper, fabric).  

---

### **3. Key Code Citations**  
- **NEC 210.12(A)**:  
  > *"In dwelling units, all 15- and 20-ampere branch circuits supplying outlets in bedrooms shall be protected by a listed arc-fault circuit interrupter, installed to provide protection of the branch circuit."*  
- **NEC 210.12(B)**:  
  > *"In dwelling units, all 15- and 20-ampere branch circuits supplying outlets in other than kitchens, bathrooms, garages, and areas specified in 210.12(A) shall be protected by a listed arc-fault circuit interrupter."*  

---

### **4. Rationale for Specific Areas**  
- **Bedrooms and living areas** are high-risk locations for arc faults due to:  
  - Frequent use of portable appliances and extension cords.  
  - Concealed wiring in walls that may degrade over time.  
  - Increased likelihood of physical damage to cords or outlets.  

---

### **5. How AFCI Differs from GFCI**  
- **AFCI** protects against **fire hazards** (arc faults).  
- **GFCI** protects against **shock hazards** (ground faults).  
- Both are required in different areas (e.g., GFCI for kitchens/bathrooms, AFCI for bedrooms/living rooms).  

---

### **6. Exceptions**  
- AFCI protection is **not required** for:  
  - Circuits supplying **fixed appliances** (e.g., ovens, dishwashers).  
  - Circuits in **kitchens, bathrooms, garages** (covered by other requirements).  

[OK] Source: NEC 2023

---

### core-012

**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?

**Duration:** 8.9s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Torque Specifications for Conductor Termination (CEC 2022)

### **1. Importance of Torque Specifications**  
- **Ensures Secure Connections**: Proper torque prevents loose connections, reducing arcing, overheating, and fire hazards.  
- **Avoids Damage**: Over-tightening can damage terminals or conductors, while under-tightening risks mechanical failure.  
- **Compliance with Code**: Mandated by CEC 110.14(D) to ensure safe, reliable electrical installations.  

---

### **2. Code Requirements**  
- **Primary Reference**: **CEC 110.14(D)**  
  > *"Tightening torque values for terminal connections shall be as indicated on equipment or in installation instructions provided by the manufacturer. An approved means shall be used to achieve the indicated torque value."*  

- **Key Details**:  
  - **Manufacturer Specifications**: Torque values must match equipment markings or installation instructions.  
  - **Approved Tools**: Use torque-measuring devices (e.g., torque screwdrivers/wrenches) or visual indicators (shear bolts, breakaway devices).  
  - **Documentation**: If torque values are not marked, contact the manufacturer or refer to standards like **UL 486A-486B**.  

---

### **3. Supporting Code Sections**  
- **CEC 430.9(C)**: Requires minimum torque of **0.8 N·m (7 lb-in.)** for control circuit devices with screw-type terminals using 14 AWG or smaller copper conductors.  
- **CEC 370.20(B)**: References **110.14(C)** for temperature limitations at terminations (indirectly tied to torque compliance).  

---

### **4. Consequences of Non-Compliance**  
- **Loose Connections**: Arcing, overheating, and potential fire hazards.  
- **Damaged Equipment**: Over-tightening can crack insulation or deform terminals.  
- **Code Violations**: Fails inspection under **110.14(D)** and related sections.  

---

### **5. Best Practices**  
- Always use a **calibrated torque tool**.  
- Verify torque values are **marked on the equipment**.  
- Follow **manufacturer instructions** for termination methods.  

[OK] Source: CEC 2022

---

### inspection-001

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Duration:** 20.1s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Service Load Calculation for Residential Panel (CEC 2022)

### **1. General Lighting Load**  
- **3000 sq ft × 3 VA/sq ft** = **9000 VA** (CEC Table 220.12).  
- **Demand Factor**: First 3000 VA at 100%, remaining 6000 VA at 35%:  
  $$
  3000 + (6000 \times 0.35) = 3000 + 2100 = 5100 \, \text{VA}  
  $$

---

### **2. Small Appliance Circuits**  
- **2 circuits × 1500 VA** = **3000 VA** (CEC 220.52).  

---

### **3. Laundry Circuit**  
- **1 circuit × 1500 VA** = **1500 VA** (CEC 220.52).  

---

### **4. Range Load**  
- **12 kW range** → Apply demand factor from CEC 220.55:  
  - **First 8 kW at 100%** = 8000 VA  
  - **Remaining 4 kW × 40%** = 1600 VA  
  - **Total** = **9600 VA**.  

---

### **5. Dryer Load**  
- **5.5 kW dryer** → Apply demand factor from CEC 220.54:  
  - **5000 VA (first 5000 VA)** + **500 VA (remaining 500 VA × 10%)** = **5500 VA**.  

---

### **6. Central AC Load**  
- **4600 VA** (19.2A × 240V).  
- **Continuous load** → Multiply by **1.25**:  
  - **4600 × 1.25** = **5750 VA** (CEC 210.20(A)).  

---

### **7. Total Load Calculation**  
| Load Type               | VA Before Demand | Demand Factor | Adjusted VA |
|-------------------------|------------------|---------------|-------------|
| General Lighting        | 9000             | 35% (over 3000 VA) | 5100 VA |
| Small Appliance         | 3000             | 100%          | 3000 VA     |
| Laundry                 | 1500             | 100%          | 1500 VA     |
| Range                   | 12,000           | 8000 + 40%    | 9600 VA     |
| Dryer                   | 5500             | 100%          | 5500 VA     |
| Central AC              | 4600             | 1.25          | 5750 VA     |
| **Total**               |                  |               | **29,950 VA** |

---

### **8. Final Service Load**  
- **Total VA** = **29,950 VA**  
- **Service Size** = **29,950 VA ÷ 240V** ≈ **124.8 A**  

---

### **9. Panel Adequacy**  
- **200A main breaker** provides **48,000 VA** (200A × 240V).  
- **124.8 A < 200A** → **Panel is adequately sized**.  

---

### **10. Code Citations**  
- **General Lighting**: CEC Table 220.12  
- **Small Appliance**: CEC 220.52  
- **Range**: CEC 220.55  
- **Dryer**: CEC 220.54  
- **AC Load**: CEC 210.20(A)  

[OK] Source: CEC 2022

---

### inspection-002

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Duration:** 11.9s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## Residential Garage Electrical Panel Violations (NEC 2023)

### **1. Insufficient Working Space Depth**  
- **Violation**: NEC 110.26(A)(1) requires **30 inches of depth** for working space in front of panels rated 120V–277V (Condition 1 or 2).  
  - **Measured**: 28 inches (insufficient).  
  - **Impact**: Risk of restricted access for safe maintenance.  

---

### **2. Obstruction in Working Space**  
- **Violation**: NEC 110.26(A)(2) mandates **clear working space** free of obstructions.  
  - **Issue**: Water heater located **16 inches from the panel** (within required 30-inch depth).  
  - **Impact**: Obstructs access to the panel, increasing fire and shock hazards.  

---

### **3. Inadequate Working Space Height**  
- **Violation**: NEC 110.26(A)(3) requires **minimum height of 2.0 m (6 ft 6 in)** for working space.  
  - **Measured**: Panel mounted at 5 feet height.  
  - **Impact**: Working space height is **13 inches short**, violating clearance requirements.  

---

### **4. Surface-Mounted Panel Clearance**  
- **Violation**: NEC 110.26(A)(1) applies to **surface-mounted panels**.  
  - **Issue**: Depth clearance (28 inches) is **less than required 30 inches**.  
  - **Impact**: Compromises safety during panel access.  

---

### **5. Missing Egress Requirements**  
- **Violation**: NEC 110.26(C)(1) requires **at least one entrance/egress** for working space.  
  - **Issue**: Panel location in a garage may restrict unobstructed egress paths.  
  - **Impact**: Emergency access and safety compromised.  

---

### **Code Citations**  
- **Working Space Depth/Height**: NEC 110.26(A)(1) and (A)(3)  
- **Clearance from Obstructions**: NEC 110.26(A)(2)  
- **Egress Requirements**: NEC 110.26(C)(1)  

---

### **Corrective Actions**  
1. **Increase depth clearance** to 30 inches.  
2. **Relocate the water heater** outside the working space.  
3. **Raise the panel** to ensure 6.5 feet of vertical clearance.  
4. **Ensure unobstructed egress** paths per 110.26(C).  

[OK] Source: NEC 2023

---

### inspection-005

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Duration:** 23.3s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## Required Protection for Kitchen Circuits (2023 NEC)

### **1. Countertop Receptacles (20A Circuits)**  
- **Protection Required**: **GFCI + AFCI (Combination Breaker)**  
- **NEC References**:  
  - **GFCI**: 210.8(A)(6) – All countertop receptacles must have GFCI protection.  
  - **AFCI**: 210.12(A) – All 120V, 15-20A branch circuits in kitchens require AFCI protection.  

---

### **2. Dishwasher (15A Dedicated Circuit)**  
- **Protection Required**: **GFCI + AFCI (Combination Breaker)**  
- **NEC References**:  
  - **GFCI**: 210.8(A)(7) – Receptacles within 6 ft of a sink (e.g., dishwasher) require GFCI.  
  - **AFCI**: 210.12(A) – Applies to all kitchen circuits, including dishwashers.  

---

### **3. Garbage Disposal (15A Dedicated Circuit)**  
- **Protection Required**: **GFCI + AFCI (Combination Breaker)**  
- **NEC References**:  
  - **GFCI**: 210.8(A)(7) – Receptacles within 6 ft of a sink (e.g., disposal) require GFCI.  
  - **AFCI**: 210.12(A) – Covers all kitchen circuits, including disposals.  

---

### **4. Refrigerator (20A Dedicated Circuit)**  
- **Protection Required**: **GFCI + AFCI (Combination Breaker)**  
- **NEC References**:  
  - **GFCI**: 210.8(A)(5) – All kitchen receptacles (including refrigerators) require GFCI.  
  - **AFCI**: 210.12(A) – Applies to all kitchen circuits, including refrigerators.  

---

### **Key Notes**  
- **Combination Breakers**: Use a single breaker that provides both GFCI and AFCI protection (e.g., Siemens QDCAFCI or Eaton BRCAFCI).  
- **Exceptions**: None apply for these circuits under 2023 NEC.  

[OK] Source: NEC 2023

---

### inspection-006

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Duration:** 16.4s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## Corrected Subpanel Grounding/Bonding Violations (NEC 2023)

### **1. Neutral and Ground Bars Bonded Together**  
- **Violation**: **NEC 250.32(B)** – In a subpanel (not the main service), **neutral and ground must be isolated**.  
  - **Issue**: Main bonding jumper (which bonds neutral and ground) is installed in the subpanel.  
  - **Impact**: Creates parallel paths for fault current, increasing shock hazard.  
  - **Correct**: **Remove the main bonding jumper**. Neutral and ground bars must remain **separate**.  

---

### **2. Neutral Bar Bonded to Metal Enclosure**  
- **Violation**: **NEC 250.102** – The **neutral conductor must not be bonded to the enclosure** in a subpanel.  
  - **Issue**: Neutral bar is physically connected to the metal enclosure.  
  - **Impact**: Creates unintended grounding paths, risking equipment damage and shock.  
  - **Correct**: Neutral bar must be **electrically isolated** from the enclosure.  

---

### **3. Ground Bar Bonded to Metal Enclosure**  
- **Violation**: **NEC 250.30(A)** – The **grounding electrode conductor** (not the equipment grounding conductor) must connect to the grounding electrode system.  
  - **Issue**: Ground bar is bonded to the enclosure, but this is **not sufficient** for grounding.  
  - **Impact**: Inadequate grounding for fault current.  
  - **Correct**: The **equipment grounding conductor** (feeder ground wire) must connect to the ground bar, and the ground bar must be **bonded to the grounding electrode system** (e.g., ground rod) via a separate conductor.  

---

### **4. Feeder Neutral Connected to Neutral Bar**  
- **Violation**: **NEC 250.32(B)** – The **neutral conductor** must be connected to the **grounding electrode system** **only at the main service panel**.  
  - **Issue**: Feeder neutral is connected to the neutral bar in the subpanel.  
  - **Impact**: Neutral-to-ground voltage can develop, creating shock risks.  
  - **Correct**: Feeder neutral must terminate **only on the neutral bar** (no bonding to ground).  

---

### **Correct Configuration**  
1. **Neutral Bar**:  
   - Connect **feeder neutral conductor** to the neutral bar.  
   - **No bonding** to ground bar or enclosure.  

2. **Ground Bar**:  
   - Connect **feeder equipment grounding conductor** (ground wire) to the ground bar.  
   - Bond the ground bar to the **grounding electrode system** (e.g., ground rod) via a separate conductor.  

3. **Main Bonding Jumper**:  
   - **Remove** the main bonding jumper from the subpanel.  

4. **Enclosure Bonding**:  
   - The metal enclosure is grounded via the **equipment grounding conductor** (not neutral).  

---

### **NEC References**  
- **Neutral/Ground Separation**: 250.32(B)  
- **Grounding Electrode Connection**: 250.30(A)  
- **Main Bonding Jumper**: 250.102  

[OK] Source: NEC 2023

---

### inspection-007

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Duration:** 8.6s | **NEC Comparison:** No

**Tools Called:** nec_generic_table_raw, nec_generic_table_raw

**Answer:**

## Maximum Number of 10 AWG THHN Conductors in 1¼-inch RMC (NEC 2023)

### **Step 1: Conduit Cross-Sectional Area**  
From **NEC Table 4 (Chapter 9)** for **1¼-inch RMC**:  
- **Cross-sectional area** = **1.722 in²**.  

### **Step 2: Conductor Cross-Sectional Area**  
From **NEC Table 5 (Chapter 9)** for **10 AWG THHN**:  
- **Cross-sectional area** = **0.0437 in²**.  

### **Step 3: Maximum Fill Calculation**  
For **more than two conductors**, the maximum fill is **40% of the conduit area** (NEC 110.38(B)).  

$$
\text{Maximum Fill Area} = 1.722 \, \text{in²} \times 0.40 = 0.6888 \, \text{in²}
$$

$$
\text{Number of Conductors} = \frac{0.6888 \, \text{in²}}{0.0437 \, \text{in²/conductor}} \approx 15.76
$$

### **Final Result**  
- **Maximum number of 10 AWG THHN conductors**: **15** (rounded down to the nearest whole number).  

---

### **NEC References**  
- **Conduit Area**: NEC Table 4 (Chapter 9)  
- **Conductor Area**: NEC Table 5 (Chapter 9)  
- **Fill Limit**: NEC 110.38(B)  

[OK] Source: NEC 2023

---

### inspection-008

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Duration:** 11.7s | **NEC Comparison:** No

**Tools Called:** nec_search

**Answer:**

## Voltage Drop Calculation for 12 AWG Copper Conductors (NEC 2023)

### **Given**  
- **Voltage**: 120V  
- **Load**: 22A continuous  
- **Conductor**: 12 AWG copper, **1.29 ohms/1000 ft**  
- **Distance**: 50 ft (one-way)  

---

### **Step 1: Calculate Voltage Drop**  
Using the formula:  
$$
VD = \frac{2 \times L \times R \times I}{1000}
$$  
Where:  
- $ L = 50 $ ft  
- $ R = 1.29 $ ohms/1000 ft  
- $ I = 22 $ A  

$$
VD = \frac{2 \times 50 \times 1.29 \times 22}{1000} = \frac{2838}{1000} = 2.84 \, \text{volts}
$$

---

### **Step 2: Calculate Percentage Voltage Drop**  
$$
\text{Percentage} = \left( \frac{VD}{\text{Source Voltage}} \right) \times 100 = \left( \frac{2.84}{120} \right) \times 100 = 2.37\%
$$

---

### **NEC Compliance Check**  
- **Maximum recommended voltage drop for branch circuits**: **3%** (NEC 210.19(A)(1) Informational Note No. 4).  
- **Result**: **2.37%** < 3% → **Compliant**.  

---

### **Final Answer**  
- **Voltage Drop**: **2.84 volts**  
- **Percentage**: **2.37%**  
- **Compliance**: ✅ Meets NEC 3% recommendation.  

[OK] Source: NEC 2023

---

### inspection-009

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Duration:** 12.2s | **NEC Comparison:** No

**Tools Called:** cec_search

**Answer:**

## Adjusted Ampacity for 12 AWG TW Conductors (NEC 2023)  

### **Step 1: Base Ampacity**  
From **NEC Table 310.16** for **12 AWG TW (60°C rated) copper**:  
- **Base ampacity** = **20A** (60°C column).  

---

### **Step 2: Temperature Correction Factor**  
Ambient temperature = **43°C**.  
From **NEC Table 310.15(B)(1)** for **60°C conductors**:  
- **Correction factor** = **0.58** (at 43°C).  

---

### **Step 3: Bundling Adjustment Factor**  
Number of current-carrying conductors = **6**.  
From **NEC Table 310.15(C)(1)**:  
- **Adjustment factor** = **0.50** (for 6 conductors).  

---

### **Step 4: Adjusted Ampacity Calculation**  
$$
\text{Adjusted Ampacity} = \text{Base Ampacity} \times \text{Temperature Factor} \times \text{Bundling Factor}
$$
$$
= 20 \, \text{A} \times 0.58 \times 0.50 = 5.8 \, \text{A}
$$

---

### **Final Result**  
- **Adjusted ampacity**: **5.8A**  
- **NEC Compliance**: The adjusted ampacity is significantly reduced due to high ambient temperature and bundling.  

---

### **NEC References**  
- **Base Ampacity**: NEC Table 310.16  
- **Temperature Correction**: NEC Table 310.15(B)(1)  
- **Bundling Adjustment**: NEC Table 310.15(C)(1)  

[OK] Source: NEC 2023

---

### inspection-010

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Duration:** 6.8s | **NEC Comparison:** No

**Tools Called:** nec_lookup_grounding_conductor

**Answer:**

## Minimum Size Copper GEC for 4 × 250 kcmil Service Conductors (NEC 2023)

### **Step 1: Equivalent Service Conductor Size**  
- **Four parallel 250 kcmil copper conductors per phase**  
- **Total equivalent area** = 4 × 250 kcmil = **1000 kcmil**  

---

### **Step 2: Apply NEC Table 250.66**  
From **NEC Table 250.66** for **copper grounding electrode conductor (GEC)**:  
- **For service conductors ≥ 600 kcmil and ≤ 1100 kcmil**:  
  - **Minimum GEC size** = **2/0 AWG copper**  

---

### **Final Result**  
- **Minimum required GEC size**: **2/0 AWG copper**  

---

### **NEC References**  
- **GEC sizing**: NEC Table 250.66  
- **Parallel conductor equivalent area**: NEC 250.66(A)  

[OK] Source: NEC 2023

---

