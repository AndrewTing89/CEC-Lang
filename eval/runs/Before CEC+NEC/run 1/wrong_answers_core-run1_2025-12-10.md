# Imperfect Answers - Core Evaluation Run 1

**Date:** 2025-12-10
**Total Imperfect:** 6/28

## core-005 (Score: 0/10)

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Expected:** No, this violates multiple requirements: (1) Minimum 36 inches depth required per 110.26(A)(1), not 24 inches. (2) Panels are prohibited in clothes closets per 240.24(D). (3) Working space width must be 30 inches or equipment width, whichever is greater. (4) No storage allowed in working space per 110.26(B).

**Actual:** ## Working Space Requirements for Electrical Panels (CEC 2022 / NEC 2023)

### **Front Clearance**
- **Service Equipment (Main Panel)**:  
  - **Minimum**: 36 inches (914 mm) per **CEC 110.26(A)(1)(b)**.  
  - **Provided**: 24 inches → **Fails requirement**.  
- **Panelboard (Subpanel)**:  
  - **Minimum**: 30 inches (762 mm) per **CEC 110.26(A)(1)(a)**.  
  - **Provided**: 24 inches → **Fails requirement**.  

---

### **Side Clearance**
- **Service Equipment**:  
  - **Minimum**: 30 inches (762 mm) of clear space on all sides per **CEC 110.26(A)(2)**.  
  - **Provided**: 18 inches to water heater → **Fails requirement**.  
- **Panelboard**:  
  - No specific side clearance, but must be **clear of obstructions** (per **CEC 110.26(A)(3)**).  
  - **Provided**: 18 inches to water heater → **Fails safe clearance**.  

---

### **Key Code References**
1. **CEC 110.26(A)(1)**:  
   - Specifies minimum working space depth:  
     - **36 inches** for service equipment.  
     - **30 inches** for panelboards.  
2. **CEC 110.26(A)(2)**:  
   - Requires **30 inches of clear space** on all sides of service equipment.  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 110.26.  
- Follows NEC 2023 requirements directly.  

---

### **Conclusion**
- **Front clearance**: 24 inches < required 36 inches (service equipment) or 30 inches (panelboard).  
- **Side clearance**: 18 inches < required 30 inches for service equipment.  
- **Result**: **Does not meet CEC/NEC requirements**.  

**[OK] Source**: CEC 2022 Sections 110.26(A)(1) and 110.26(A)(2)

**Reasoning:** Judge error: Invalid control character at: line 6 column 325 (char 385)

---

## inspection-005 (Score: 5/10)

**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.

**Expected:** Per 2023 NEC: (1) Countertop receptacles (2 circuits): GFCI required per 210.8(A)(6), AFCI required per 210.12(A). Use combination AFCI/GFCI breakers. (2) Dishwasher: GFCI required per 210.8(D), AFCI required per 210.12(A). Use combination AFCI/GFCI breaker. (3) Disposal: GFCI not specifically required for disposal, but AFCI required per 210.12(A). AFCI breaker or combination AFCI/GFCI recommended. (4) Refrigerator: AFCI required per 210.12(A). Standard AFCI breaker (GFCI not required for refrigerator circuit).

**Actual:** ## Circuit Protection Requirements for Kitchen Installations (NEC 2023)

### **1. Countertop Receptacles (20A Circuits)**
- **Required Protection**: **GFCI**  
- **NEC Reference**: **210.8(A)(5)**  
  > "All 125-volt, single-phase, 15- and 20-ampere receptacles installed in kitchens shall have ground-fault circuit-interrupter (GFCI) protection for personnel."  
- **Rationale**: Countertop receptacles are required to have GFCI protection due to proximity to water sources and potential shock hazards.

---

### **2. Dishwasher (Dedicated 15A Circuit)**
- **Required Protection**: **Standard Breaker**  
- **NEC Reference**: **210.8(B)(2)**  
  > "GFCI protection shall not be required for receptacles supplying fixed electric space-heating appliances, central air-conditioning equipment, or fixed electric heating, air-conditioning, and refrigeration equipment."  
- **Rationale**: Dishwashers are classified as fixed appliances and are exempt from GFCI requirements.

---

### **3. Garbage Disposal (Dedicated 15A Circuit)**
- **Required Protection**: **Standard Breaker**  
- **NEC Reference**: **210.8(B)(2)**  
  > "GFCI protection shall not be required for receptacles supplying fixed electric heating, air-conditioning, and refrigeration equipment."  
- **Rationale**: Garbage disposals are fixed appliances and do not require GFCI protection.

---

### **4. Refrigerator (Dedicated 20A Circuit)**
- **Required Protection**: **Standard Breaker**  
- **NEC References**:  
  - **210.8(B)(2)**: Exempts fixed refrigeration equipment from GFCI.  
  - **210.12(A)**: Exempts fixed refrigeration equipment from AFCI.  
- **Rationale**:  
  - **GFCI**: Not required for fixed refrigeration equipment.  
  - **AFCI**: Not required for fixed refrigeration equipment (exempt under 210.12(A)).  

---

### **Summary Table**
| **Circuit**               | **Protection Type** | **NEC Section**       |
|---------------------------|---------------------|------------------------|
| Countertop receptacles    | GFCI                | 210.8(A)(5)           |
| Dishwasher                | Standard            | 210.8(B)(2)           |
| Garbage disposal          | Standard            | 210.8(B)(2)           |
| Refrigerator              | Standard            | 210.8(B)(2), 210.12(A)|

---

### **Key Notes**
- **GFCI vs. AFCI**:  
  - **GFCI** protects against ground faults (shock hazards).  
  - **AFCI** protects against arc faults (fire hazards).  
- **Fixed Appliances**: Dishwashers, garbage disposals, and refrigerators are exempt from GFCI and AFCI requirements when installed as fixed equipment.  
- **Code Compliance**: All circuits meet NEC 2023 requirements for residential kitchens.  

**[OK] Source**: NEC 2023 Sections 210.8 and 210.12

**Reasoning:** The ACTUAL ANSWER incorrectly states that dishwashers, disposals, and refrigerators are exempt from AFCI protection. While it correctly identifies GFCI requirements (or lack thereof), it misses the crucial AFCI requirements for almost all circuits in a dwelling unit, as per NEC 210.12(A). The reference to 210.8(A)(5) for GFCI protection of countertop receptacles is also slightly off; 210.8(A)(6) is the correct section. Completeness is moderate as it addresses each appliance, but the lack of AFCI info is a major omission.

---

## inspection-009 (Score: 6/10)

**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.

**Expected:** Step 1: Base ampacity of 12 AWG TW copper at 60°C = 20 amperes (Table 310.16). Step 2: Temperature correction for 43°C ambient with 60°C conductor from Table 310.15(B)(1)(1): Correction factor = 0.71 (for 41-45°C range in 60°C column). Step 3: Bundling adjustment for 6 conductors from Table 310.15(C)(1): Adjustment factor = 0.80 (for 4-6 conductors). Step 4: Calculate adjusted ampacity: 20A × 0.71 × 0.80 = 11.36 amperes. Conclusion: The adjusted ampacity is 11.36 amperes (approximately 11.4A), which represents a 43% reduction from the base 20A rating.

**Actual:** ## Adjusted Ampacity for 12 AWG TW Conductors (CEC 2022)

### **Step 1: Base Ampacity**
- **Conductor Type**: 12 AWG TW (60°C rated)  
- **Base Ampacity**: **20A** (CEC Table 310.16, 60°C column)  

---

### **Step 2: Temperature Correction Factor**
- **Ambient Temperature**: 110°F (43°C)  
- **Correction Factor**:  
  - **CEC Table 310.15(B)(1)(1)** → **0.58** (for 60°C conductors at 43°C)  

---

### **Step 3: Bundling Adjustment Factor**
- **Number of Conductors**: 6 current-carrying conductors in the same raceway  
- **Adjustment Factor**:  
  - **CEC Table 310.15(B)(2)(a)** → **0.50** (for 6 conductors)  

---

### **Step 4: Final Adjusted Ampacity**
$$
\text{Adjusted Ampacity} = \text{Base Ampacity} \times \text{Temperature Correction} \times \text{Bundling Adjustment}
$$
$$
= 20 \, \text{A} \times 0.58 \times 0.50 = 5.8 \, \text{A}
$$

---

### **Summary**
| **Factor**               | **Value** |
|--------------------------|-----------|
| Base Ampacity (60°C)     | 20A       |
| Temperature Correction   | 0.58      |
| Bundling Adjustment      | 0.50      |
| **Final Adjusted Ampacity** | **5.8A**  |

---

### **CEC Compliance**
- **CEC 310.15(B)(1)(1)**: Temperature correction for ambient temperatures above 30°C.  
- **CEC 310.15(B)(2)(a)**: Bundling adjustment for more than 3 current-carrying conductors.  

---

### **Final Answer**
The adjusted ampacity is **5.8A**, significantly reduced due to high ambient temperature and bundling.  

**[OK] Source**: CEC 2022 Tables 310.16, 310.15(B)(1)(1), and 310.15(B)(2)(a)

**Reasoning:** The actual answer is well-formatted and complete, following all the steps and providing necessary details. However, the temperature correction factor and bundling adjustment factors are INCORRECT. This leads to a completely wrong final adjusted ampacity. The code citations are correct, but the values derived from those tables are wrong. The temperature correction factor of 0.58 and bundling adjustment factor of 0.50 are both incorrect based on the 2022 CEC and NEC. Therefore, the accuracy score is low.

---

## inspection-007 (Score: 7/10)

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Expected:** Per Chapter 9 Table 1: Maximum 40% fill for more than two conductors. From Chapter 9 Table 4: Trade size 1¼" RMC has 40% fill area of 0.610 square inches. From Chapter 9 Table 5: 10 AWG THHN conductor area is 0.0211 square inches. Calculation: 0.610 in² ÷ 0.0211 in² per conductor = 28.91 conductors. Per Chapter 9 Note 7: When the decimal is 0.8 or larger, round up to the next whole number. Since 0.91 > 0.8, maximum is 29 conductors. However, conservative practice uses 28 conductors maximum.

**Actual:** ## Maximum Number of 10 AWG THHN Conductors in 1¼-Inch RMC (NEC 2023)

### **Step 1: Conduit Internal Area**
- **Conduit Type**: Rigid Metal Conduit (RMC)  
- **Size**: 1¼ inches (1.25 in.)  
- **Internal Cross-Sectional Area**:  
  - **NEC Table 4 (Chapter 9)**:  
    - RMC 1¼-inch internal area = **1.363 in²**  

---

### **Step 2: Conductor Cross-Sectional Area**
- **Conductor Type**: 10 AWG THHN  
- **Cross-Sectional Area**:  
  - **NEC Table 5 (Chapter 9)**:  
    - 10 AWG THHN = **0.0511 in²** per conductor  

---

### **Step 3: Maximum Fill Calculation**
- **Fill Limit**: 40% for **more than two conductors** (NEC 300.15(B)(2)(a)).  
- **Formula**:  
  $$
  \text{Maximum Conductors} = \frac{\text{Conduit Area} \times 40\%}{\text{Conductor Area}} = \frac{1.363 \times 0.40}{0.0511}
  $$
- **Calculation**:  
  $$
  \frac{0.5452}{0.0511} \approx 10.67
  $$
- **Final Answer**: **10 conductors** (round down to the nearest whole number).  

---

### **Step 4: Verify with NEC Table 1 (Chapter 9)**
- **NEC Table 1**:  
  - For **more than two conductors**, the maximum fill is **40%** of the conduit area.  
  - This aligns with the calculation above.  

---

### **Summary**
| **Parameter**               | **Value**         |
|----------------------------|-------------------|
| Conduit Area (RMC 1¼")       | 1.363 in²         |
| Conductor Area (10 AWG THHN) | 0.0511 in²        |
| 40% Fill Limit              | 0.5452 in²        |
| Maximum Conductors          | **10**            |

---

### **Final Answer**
**10 conductors** of 10 AWG THHN can be installed in a 1¼-inch RMC conduit.  

**[OK] Source**: NEC 2023 Chapter 9 Tables 4 and 5

**Reasoning:** The actual answer incorrectly states the cross-sectional area of both the conduit and the conductor. This dramatically changes the result. However, the methodology shown is correct and it provides a lot of detail on where it got the numbers.

---

## core-003 (Score: 8/10)

**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.

**Expected:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (countertop receptacles and dishwasher), laundry areas, utility rooms with sinks, boathouses, areas with bathtubs or shower stalls, and within 6 feet of sinks.

**Actual:** ## GFCI Protection Requirements in Residential Dwellings (NEC 2023)

### **Required Locations (NEC 210.8(A))**
1. **Bathrooms**  
2. **Garages and accessory buildings** (floor at or below grade level)  
3. **Outdoors**  
4. **Crawl spaces** (at or below grade level)  
5. **Kitchens**  
6. **Areas with sinks** (permanent provisions for food prep, beverage prep, or cooking)  
7. **Sinks** (receptacles within 6 ft of the top inside edge of the bowl)  
8. **Boathouses**  
9. **Bathtubs or shower stalls** (receptacles within 6 ft of the outside edge)  
10. **Laundry areas**  
11. **Indoor damp and wet locations**  

---

### **Key Code Basis**
- **NEC 210.8(A)**: Mandates GFCI protection for all listed locations in dwelling units.  
- **Exceptions**: Specific exceptions apply (e.g., receptacles for HVAC equipment, security systems), but the **11 locations above are standard requirements**.  

---

### **California (CEC 2022) Considerations**
- **No amendments** to NEC 210.8 in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

**[OK] Source**: NEC 2023 Section 210.8(A)

**Reasoning:** The answer is mostly accurate, although the formatting is a little off and could be more concise. The answer includes 'indoor damp and wet locations', which is true, but not as specific as 'unfinished basements' and 'crawl spaces' which are generally considered 'damp and wet locations'. Also, the answer includes 'areas with sinks' and 'sinks' which is a bit redundant, as it is already covered in the expectation. However, overall the answer is good.

---

## inspection-001 (Score: 8/10)

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Expected:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 2 circuits × 1500 VA = 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table 220.55 for one range). Dryer: 5500 VA at 100%. AC: 4600 VA at 100% (largest motor). Total: 6675 + 8000 + 5500 + 4600 = 24,775 VA. Current: 24,775 VA ÷ 240V = 103.2A. Conclusion: 200A service is adequately sized with 48% safety margin.

**Actual:** ## Service Load Calculation for Residential Panel (CEC 2022)

### **Given Loads**
1. **Electric Range**: 12 kW (40A breaker)  
2. **Dryer**: 5.5 kW (30A breaker)  
3. **Small Appliance Circuits**: 2 × 20A (1800 VA each)  
4. **Laundry Circuit**: 1 × 20A (1800 VA)  
5. **General Lighting**: 3000 sq ft × 3 VA/sq ft = 9000 VA  
6. **Central AC**: 4600 W (19.2A at 240V)  

---

### **Step 1: General Lighting Load**  
- **Per CEC Table 220.12**: 3 VA/sq ft × 3000 sq ft = **9000 VA**  

---

### **Step 2: Small Appliance and Laundry Circuits**  
- **Small Appliance Circuits**: 2 × 1800 VA = **3600 VA**  
- **Laundry Circuit**: 1 × 1800 VA = **1800 VA**  
- **Total**: 3600 + 1800 = **5400 VA**  

---

### **Step 3: Electric Range Demand**  
- **Per CEC 220.55**:  
  - First 8 kW at 100% = **8000 VA**  
  - Remaining 4 kW × 40% = **1600 VA**  
  - **Total**: 8000 + 1600 = **9600 VA**  

---

### **Step 4: Dryer Demand**  
- **Per CEC 220.54**: 5.5 kW × 100% = **5500 VA**  

---

### **Step 5: Central AC Load**  
- **Continuous Load**: 4600 W × 125% = **5750 VA**  

---

### **Step 6: Total Load Calculation**  
1. **Sum All Loads**:  
   - General Lighting: 9000 VA  
   - Small Appliance/Laundry: 5400 VA  
   - Range: 9600 VA  
   - Dryer: 5500 VA  
   - AC: 5750 VA  
   - **Total**: **35,250 VA**  

2. **Apply Standard Method (CEC 220.40)**:  
   - First 10,000 VA at 100% = **10,000 VA**  
   - Remaining 25,250 VA × 40% = **10,100 VA**  
   - **Total Service Load**: 10,000 + 10,100 = **20,100 VA**  

---

### **Step 7: Convert to Amperes**  
- **Service Load in Amperes**:  
  $$
  \frac{20,100 \text{ VA}}{240 \text{ V}} = 83.75 \text{ A}
  $$

---

### **Conclusion**  
- **200A Panel**: The calculated load is **83.75A**, well within the 200A main breaker capacity.  
- **Code Compliance**:  
  - **CEC 220.55**: Range demand factor applied.  
  - **CEC 220.54**: Dryer demand factor applied.  
  - **CEC 220.40**: Standard method for load calculation.  

---

### **California (CEC 2022) Considerations**  
- **No amendments** to NEC 220.55/220.54/220.40 in CEC 2022.  
- Follows NEC 2023 requirements directly.  

---

### **Final Answer**  
- **Service Load**: **83.75A**  
- **200A Panel**: **Adequately sized** (83.75A < 200A).  

**[OK] Source**: CEC 2022 Sections 220.55, 220.54, and 220.40

**Reasoning:** The answer is mostly accurate, but uses CEC instead of NEC (although it does state that CEC 2022 follows NEC 2023 directly). The range demand calculation is also slightly different - although still acceptable. Finally, the AC load is treated as a continuous load, which is a conservative approach, but not strictly required. Overall, a good answer, but not perfect. It's also more verbose than necessary.

---

