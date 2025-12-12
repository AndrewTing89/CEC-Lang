# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-09
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 8 |
| **Successful** | 8 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 113.0s |
| **Avg per Question** | 14.1s |

---

## Results by Question


## Inspection

### inspection-001: panel_load_calculation

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table...

**CEC Ref:**  | **NEC Ref:** 220.40, 220.42, Table 220.42, Table 220.55

**Status:** PASS

**Agent Answer:**
## Service Load Calculation with Exceptions (CEC 2022)

### **Step 1: General Lighting Load**
- **3,000 sq ft × 3 VA/sq ft (Table 220.12)** = **9,000 VA**
- **Demand Factor (Table 220.42):**
  - First 3,000 VA @ 100% = **3,000 VA**
  - Remaining 6,000 VA @ 35% = **2,100 VA**
  - **Total General Lighting Load** = **5,100 VA**

### **Step 2: Small Appliance & Laundry Circuits**
- **2 × 1,500 VA (220.14(K))** = **3,000 VA**
- **1 × 1,500 VA (220.14(Q))** = **1,500 VA**
- **Total** = **4,500 VA**
- **Demand Factor (Table 220.42):**
  - First 3,000 VA @ 100% = **3,000 VA**
  - Remaining 1,500 VA @ 35% = **525 VA**
  - **Total Small Appliance Load** = **3,525 VA**

### **Step 3: Major Appliances**
1. **Electric Range (12 kW)**
   - **Demand Factor (Table 220.55, Column C)** = **8,000 VA**
2. **Dryer (5.5 kW)**
   - **Demand Factor (220.54)** = **5,500 VA**
3. **AC (4600 W)**
   - **Continuous Load (210.20(A))** = **4600 × 1.25 = 5,750 VA**

### **Step 4: Total Service Load**
- **General Load** = **5,100 VA**
- **Small Appliance Load** = **3,525 VA**
- **Range** = **8,000 VA**
- **Dryer** = **5,500 VA**
- **AC** = **5,750 VA**
- **Total** = **27,875 VA**

### **Step 5: Convert to Amperes**
- **27,875 VA ÷ 240 V** = **116.1 A**

### **Exceptions Applied**
- **Range Demand Factor (220.55):** 12 kW range reduced to 8,000 VA per Table 220.55.
- **Dryer Demand Factor (220.54):** 5.5 kW dryer used at nameplate rating (5,500 VA).
- **General Lighting Demand Factor (220.40):** 35% applied to load exceeding 3,000 VA.

### **Conclusion**
- **200A Panel Capacity** > **116.1A Calculated Load**
- **✓ Panel is adequately sized** per NEC 220.83 (dwelling service calculation method).

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 9 found
- 220.83, 220.55, 220.42, 220.12, 210.20, 220.40, 220.54, 116.1, 220.14

**Response Time:** 19.8s

---

### inspection-002: clearance_violations

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Expected:** Violations: (1) Depth clearance is 28 inches but 110.26(A)(1) requires minimum 36 inches for 120/240V equipment - VIOLATION. (2) Water heater at 16 inches is within the 30-inch width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B) - VIOLA...

**CEC Ref:**  | **NEC Ref:** 110.26(A)(1), 110.26(B), 110.26(A)(3)

**Status:** PASS

**Agent Answer:**
## Electrical Panel Inspection Violations (CEC 2022)  

### 1. **Insufficient Depth Clearance**  
- **Violation**: 28 inches depth < required **30 inches** for 240V panels (Condition 1).  
- **Citation**: CEC 2022 Table 110.26(A)(1)  
- **Fix**: Increase depth clearance to **30 inches** in front of the panel.  
- **Exceptions Checked**:  
  - **110.26(E)** (dedicated space) does not override depth requirements.  
  - **110.26(A)(1)(c)** (existing buildings) applies only to **height**, not depth.  

---

### 2. **Obstruction in Working Space**  
- **Violation**: Water heater located **16 inches** from panel < required **30 inches** clear.  
- **Citation**: CEC 2022 110.26(A)(2)  
- **Fix**: Relocate water heater **≥30 inches** from panel or install a permanent barrier.  
- **Exceptions Checked**:  
  - **110.26(E)** (dedicated space) prohibits foreign equipment (e.g., water heater) in working zone.  

---

### 3. **Incorrect Panel Height**  
- **Violation**: Panel mounted at **5 ft (60 in)** height < required **6.5 ft (78 in)**.  
- **Citation**: CEC 2022 110.26(A)(3)  
- **Fix**: Raise panel to **≥6.5 ft** from floor to bottom of panel.  
- **Exceptions Checked**:  
  - **110.26(A)(3) Exception No. 2** (existing dwellings) applies only if panel height is **≥2.0 m (6.5 ft)**. Current height fails this.  

---

### 4. **Width Clearance**  
- **Compliant**: 30 inches width meets minimum requirement (Table 110.26(A)(1)).  

---

### Summary of Violations  
- **Depth clearance** (28 in)  
- **Obstruction** (water heater at 16 in)  
- **Panel height** (5 ft)  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_lookup_working_space, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 110.26

**Response Time:** 13.4s

---

### inspection-005: gfci_afci_compliance

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically requi...

**CEC Ref:**  | **NEC Ref:** 210.8(A), 210.8(D), 210.12(A)

**Status:** PASS

**Agent Answer:**
## Circuit Protection Requirements (NEC 2023 with Exceptions Verified)

### 1. **Countertop Receptacles (Two 20A Circuits)**
- **Protection Required:** **Combination AFCI/GFCI Breaker**
- **NEC References:**
  - **210.8(A)(6):** GFCI protection required for all countertop receptacles.
  - **210.12(A):** AFCI protection required for all branch circuits in dwelling units (including kitchens).
  - **No exceptions apply** to countertop circuits (verified via `cec_exception_search` for 210.8(A)(6)).

---

### 2. **Dishwasher (15A Dedicated Circuit)**
- **Protection Required:** **GFCI Breaker**
- **NEC References:**
  - **210.8(A)(7):** GFCI protection required for receptacles supplying appliances like dishwashers.
  - **210.12(A) Exception No. 2:** AFCI exemption for dedicated appliance circuits (e.g., dishwasher). Only GFCI is required.

---

### 3. **Garbage Disposal (15A Dedicated Circuit)**
- **Protection Required:** **GFCI Breaker**
- **NEC References:**
  - **210.8(A)(7):** GFCI protection required for receptacles supplying appliances like garbage disposals.
  - **210.12(A) Exception No. 2:** AFCI exemption for dedicated appliance circuits. Only GFCI is required.

---

### 4. **Refrigerator (20A Dedicated Circuit)**
- **Protection Required:** **Standard Breaker**
- **NEC References:**
  - **210.12(A) Exception No. 2:** AFCI exemption for dedicated circuits supplying specific appliances (e.g., refrigerators).
  - **210.8(A):** No GFCI requirement for refrigerators (not in wet locations or countertops). Only standard overcurrent protection is needed.

---

### Summary Table
| Circuit Type               | Protection Type         | NEC Sections                          |
|----------------------------|-------------------------|---------------------------------------|
| Countertop receptacles     | AFCI + GFCI             | 210.8(A)(6), 210.12(A)                |
| Dishwasher                 | GFCI                    | 210.8(A)(7), 210.12(A) Exception No. 2|
| Garbage di...

**Tool Usage:**
- CEC Tools: cec_exception_search
- NEC Tools: nec_search
- CEC Primary: Yes

**Citations:** 2 found
- 210.12, 210.8

**Response Time:** 20.5s

---

### inspection-006: subpanel_violations

**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.

**Expected:** VIOLATIONS: (1) Neutral bar bonded to enclosure - VIOLATION per 250.24(A)(5) and 408.40. In subpanels, neutral must be isolated from enclosure. (2) Main bonding jumper installed - VIOLATION. MBJ only permitted at service equipment per 250.28, not in subpanels. CORRECT configuration: Remove bond betw...

**CEC Ref:**  | **NEC Ref:** 250.24(A)(5), 250.28, 408.40, 250.32(B)

**Status:** PASS

**Agent Answer:**
## Corrected Subpanel Grounding Analysis (CEC 2022)

**Re-evaluation with Exceptions Considered:**

After reviewing exceptions for **CEC 250.24(D)**, no exceptions apply to the subpanel in a detached garage scenario. The violations identified remain valid:

---

### **Critical Violations Confirmed:**

1. **Neutral-Ground Bonding (Violation of CEC 250.24(D))**  
   - **No exceptions apply** for subpanels in detached garages.  
   - **Correct action:** Neutral and ground bars must be **completely isolated** (no bonding).

2. **Neutral-to-Enclosure Bonding (Violation of CEC 250.142(B))**  
   - **No exceptions** permit neutral-to-enclosure connections in subpanels.  
   - **Correct action:** Neutral bar must be **electrically isolated** from the enclosure.

3. **Ground-to-Enclosure Bonding (Violation of CEC 250.104(B))**  
   - **No exceptions** allow direct bonding of ground bars to enclosures in subpanels.  
   - **Correct action:** Ground bar connects only to:  
     - Feeder equipment grounding conductor  
     - Local grounding electrode (if required)  

---

### **Correct Configuration (Reaffirmed):**

| Component          | Correct Connection                          | Code Reference         |
|--------------------|---------------------------------------------|------------------------|
| **Neutral Bar**    | Feeder neutral only                         | CEC 250.24(D)          |
| **Ground Bar**     | Feeder EGC + local GEC (if required)        | CEC 250.32(B)          |
| **Enclosure**      | Bonded to ground bar via EGC                | CEC 250.104(B)         |
| **Bonding Jumper** | **None** (only in main panel)               | CEC 250.24(D)          |

---

### **Key Code References (No Exceptions Apply):**
- **CEC 250.24(D):** Neutral and ground separation in subpanels.  
- **CEC 250.32(B):** Equipment grounding conductor must return to main panel.  
- **CEC 250.142(B):** No neutral-to-ground bonds in subpanels.  

✓ Source: CEC 2022

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 250.32, 250.142, 250.104, 250.24

**Response Time:** 11.2s

---

### inspection-007: conduit_fill

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors....

**CEC Ref:**  | **NEC Ref:** Chapter 9 Table 1, Chapter 9 Table 4, Chapter 9 Table 5, Chapter 9 Note 7

**Status:** PASS

**Agent Answer:**
## Final Verification with Exceptions (CEC 2022)

**Exceptions Checked:**  
1. **Section 402.7** and **366.12** confirm conduit fill limits are governed by **Table 1, Chapter 9** (no override).  
2. **Section 675.12** and **342.22** are unrelated to general conduit fill calculations.  

**Conclusion:**  
No exceptions apply to this scenario. The NEC Chapter 9 calculation (28 conductors) is valid under CEC 2022.  

**Final Answer:**  
**28 conductors maximum** in 1¼" RMC for 10 AWG THHN  
✓ Source: CEC 2022 (adopting NEC 2023 Chapter 9 Tables) with no applicable exceptions

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 342.22, 675.12, 402.7, 366.12

**Response Time:** 12.9s

---

### inspection-008: voltage_drop

**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?

**Expected:** Voltage drop formula: VD = (2 × L × R × I) / 1000. Where: L = 50 feet (one-way distance), R = 1.29 ohms/1000ft for 12 AWG copper (Chapter 9 Table 8), I = 22 amperes, multiply by 2 for round trip. Calculation: VD = (2 × 50 × 1.29 × 22) / 1000 = 2,838 / 1000 = 2.84 volts. Percentage: (2.84V / 120V) × ...

**CEC Ref:**  | **NEC Ref:** 210.19(A)(1) Informational Note No. 4, Chapter 9 Table 8

**Status:** PASS

**Agent Answer:**
## Voltage Drop Calculation (CEC 2022)

**Voltage drop**:  
VD = (2 × I × L × R) / 1000  
= (2 × 22A × 50ft × 1.29Ω/1000ft) / 1000  
= **2.84 volts**  
**Percentage drop**:  
(2.84V / 120V) × 100 = **2.36%**

---

### Code Compliance Analysis

1. **General Branch Circuit Recommendation**  
   - NEC/CEC informational note in **210.19(A)** recommends **≤3%** voltage drop for branch circuits.  
   - **2.36%** meets this recommendation.  

2. **Stricter Fixed Equipment Limit**  
   - **CEC 647.4(D)(1)** limits voltage drop to **1.5%** for fixed equipment with portable cord connections.  
   - **2.36%** exceeds this limit, but this applies only if **portable cords** are used (not specified in the question).  

3. **Exception Check**  
   - No exceptions relax the 1.5% limit in **647.4(D)**.  
   - Cross-references (e.g., informational note) clarify the 1.5% applies specifically to **portable cord scenarios**.  

---

### Final Determination

✓ **Meets NEC/CEC general branch circuit recommendation (≤3%)**.  
⚠️ **Would violate 1.5% limit for fixed equipment with portable cords** (not applicable here).  

**Conclusion**: The voltage drop of **2.36%** is acceptable for standard branch circuits but would require correction (larger conductors or shorter distance) if supplying equipment with portable cords.  

✓ Source: CEC 2022 Sections 210.19, 647.4(D)

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 2 found
- 210.19, 647.4

**Response Time:** 14.1s

---

### inspection-009: derating_calculation

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C...

**CEC Ref:**  | **NEC Ref:** Table 310.16, Table 310.15(B)(1), Table 310.15(C)(1), 310.15(B), 310.15(C)

**Status:** PASS

**Agent Answer:**
## Final Adjusted Ampacity with Exception Review (CEC 2022)

1. **Base Calculation Confirmed**:  
   12 AWG TW copper @ 60°C = **20A** (Table 310.16)  
   Temperature correction (43°C): **×0.71** (Table 310.15(B)(1))  
   Bundling adjustment (6 conductors): **×0.80** (Table 310.15(C)(1))  
   **Final: 20 × 0.71 × 0.80 = 11.36A**

2. **Exception Analysis**:  
   - **Section 310.15** explicitly permits temperature and bundling adjustments **as long as corrected ampacity does not exceed termination temperature ratings** (110.14(C)).  
   - Conductors are TW (60°C rated), and terminations must also be 60°C rated per 110.14(C). Adjusted ampacity (11.36A) is **well below** the 20A base value, so no conflict.  
   - No exceptions override this calculation for general-purpose conductors in this scenario.  

3. **Limiting Rule Check**:  
   - **240.4(D)** allows 20A OCP for 12 AWG copper (matches base ampacity).  
   - Adjusted ampacity (11.36A) is **less than** OCP limit – no conflict.  

**Final Answer**: **11.36 amperes**  

✓ Source: CEC 2022  
✓ Exceptions Verified: No applicable exceptions override calculation.

**Tool Usage:**
- CEC Tools: cec_lookup_conductor_ampacity, cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 310.15, 240.4, 110.14, 310.16

**Response Time:** 11.8s

---

### inspection-010: grounding_electrode_conductor

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.

**Expected:** Per Table 250.66: For service entrance conductors 1000 kcmil copper (4 × 250 kcmil in parallel), locate the row for 'Over 600 kcmil through 1100 kcmil'. The minimum grounding electrode conductor size is 2/0 AWG copper or 4/0 AWG aluminum. Answer: Minimum 2/0 AWG copper GEC required. Note: If this GE...

**CEC Ref:**  | **NEC Ref:** Table 250.66, 250.66(A)

**Status:** PASS

**Agent Answer:**
## Minimum Size Copper GEC for Parallel Service Conductors (CEC 2022)

For a main service with **four parallel 250 kcmil copper conductors per phase** (total equivalent 1000 kcmil), the minimum size **copper grounding electrode conductor (GEC)** required is:

**2/0 AWG copper**  
(Per CEC 2022 Table 250.66, California amendment applies)

---

### Key Steps:
1. **Total Service Conductor Size**:  
   4 × 250 kcmil = **1000 kcmil equivalent** (per phase).

2. **Table 250.66 Reference**:  
   - For service conductors **over 600 kcmil through 1100 kcmil**, the minimum copper GEC is **2/0 AWG**.

3. **California Amendment**:  
   The table includes a delta symbol (△) indicating a California-specific modification from NEC. Always verify local amendments when applying.

---

### Exceptions Considered:
- **Exception 250.66(A)**: If connected to a rod/pipe electrode, **6 AWG copper** is permitted (but only if the GEC does not extend to other electrode types requiring larger conductors).
- **Exception 250.66(B)**: For concrete-encased electrodes, **4 AWG copper** is permitted under similar conditions.
- **Exception 250.66(C)**: For ground rings, the GEC size matches the ground ring conductor.

**No exceptions apply** unless the installation uses a specific electrode type (rod/pipe, concrete-encased, or ground ring). Since the question does not specify the electrode type, the **standard 2/0 AWG copper** from Table 250.66 remains valid.

---

✓ **Source**: CEC 2022 Table 250.66 with California amendments.

**Tool Usage:**
- CEC Tools: cec_lookup_grounding_conductor, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 1 found
- 250.66

**Response Time:** 9.2s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 8/8
- **Success Rate**: 100.0%
- **Average Response Time**: 14.1s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

