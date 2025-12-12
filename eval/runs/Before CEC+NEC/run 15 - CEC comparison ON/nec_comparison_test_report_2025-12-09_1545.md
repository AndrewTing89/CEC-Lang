# NEC Comparison Toggle Test Report

**Date:** 2025-12-09_1545
**Model:** qwen/qwen3-32b

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 4 |
| PASS (compare_with_nec only when ON) | 4/4 |
| Total Time (OFF mode) | 37.9s |
| Total Time (ON mode) | 50.9s |
| Average Additional Time | +3.2s |

---

## Test Results

### cec-001 - CA policy

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

#### Mode: NEC Comparison OFF

- **Duration:** 13.1s
- **Iterations:** 4
- **Tools:** cec_search, cec_exception_search
- **compare_with_nec called:** No

<details>
<summary>Answer (OFF mode)</summary>

## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022)

### **Panelboard Space Requirements**
Per **CEC 2022 Section 408.2(A)**, single-family residential panelboards must provide **reserved circuit breaker spaces** for the following appliances:

1. **Heat pump water heaters**  
2. **Heat pump space heaters**  
3. **Electric cooktops**  
4. **Electric clothes dryers**  

This requirement is mandated by the **California Energy Code (CEC) Section 150.0(n), (t), (u), and (v)** to ensure future-ready electrical infrastructure for electrification and energy efficiency.

---

### **Exceptions Analysis**
After checking exceptions to **Section 408.2(A)** using `cec_exception_search`, no exceptions directly modify the reserved space requirements for the listed appliances. The returned exceptions pertain to unrelated topics like wire-bending space (408.55), enclosure types (408.38), overcurrent protection (408.36), and heating leads (424.97), which do not affect the appliance-specific reserved space rule in 408.2(A).

---

### **Final Answer**
- **Required reserved spaces**: Heat pump water heaters, heat pump space heaters, electric cooktops, and electric clothes dryers.  
- **No exceptions apply** to this specific requirement.  

✓ Source: CEC 2022

</details>

#### Mode: NEC Comparison ON

- **Duration:** 11.0s
- **Iterations:** 4
- **Tools:** cec_search, cec_exception_search, compare_with_nec
- **compare_with_nec called:** Yes

<details>
<summary>Answer (ON mode)</summary>

## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022)

### **California Requirements**
Per **CEC 2022 Section 408.2(A)**, single-family residential buildings must have panelboards with **reserved circuit breaker spaces** for the following appliances:
- Heat pump water heaters  
- Heat pump space heaters  
- Electric cooktops  
- Electric clothes dryers  

This requirement is mandated by the **California Energy Code Section 150.0(n), (t), (u), and (v)** to ensure future-ready electrical infrastructure for electrification and energy efficiency.

---

### **NEC 2023 Comparison**
The **NEC 2023** does **not include appliance-specific reserved circuit breaker spaces** in its general panelboard requirements. Relevant NEC sections (e.g., 408.30, 424.19) focus on:
- Minimum panelboard ratings based on load calculations  
- Disconnecting means for fixed equipment  
- General wiring methods  

**Key Difference**:  
California’s CEC explicitly mandates reserved spaces for specific appliances to support electrification goals (e.g., heat pumps, electric cooking). The NEC leaves such provisions to local jurisdictions or energy codes, making California’s requirements a **state-specific amendment**.

---

### **Citations**
- **CEC 2022**: Section 408.2(A), California Energy Code Section 150.0  
- **NEC 2023**: Sections 408.30, 424.19 (no appliance-specific reserved spaces)  

✓ Source: CEC 2022 / NEC 2023

</details>

#### Analysis

- **Time Difference:** -2.1s
- **Tools Added:** compare_with_nec
- **Verification (compare_with_nec only when ON):** PASS

---

### cec-011 - Table lookup

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?

#### Mode: NEC Comparison OFF

- **Duration:** 7.7s
- **Iterations:** 4
- **Tools:** cec_lookup_conductor_ampacity, cec_exception_search
- **compare_with_nec called:** No

<details>
<summary>Answer (OFF mode)</summary>

## Final Answer: Ampacity of 4/0 AWG Copper Conductor (CEC 2022)

**Ampacity**: **230 amperes** at 75°C  
Per CEC 2022 Table 310.16 (general use, 3 or fewer conductors, 30°C ambient).

**Exceptions Found**:
- **Section 440.6** applies specifically to **hermetic refrigerant motor-compressors** and **multimotor equipment**. These exceptions modify conductor sizing rules for specialized equipment but **do not affect general ampacity values** in Table 310.16.

**Key Limiting Rules**:
1. **Overcurrent Protection**: Per Section 240.4(D), 4/0 copper conductors **must be protected at 250A maximum** (not exceeding their 230A ampacity).
2. **Temperature Correction**: If ambient temperature exceeds 30°C, apply correction factors from Table 310.15(B).
3. **Bundling Adjustment**: For more than 3 conductors, apply derating per Table 310.15(C)(1).

✓ Source: CEC 2022

</details>

#### Mode: NEC Comparison ON

- **Duration:** 9.5s
- **Iterations:** 4
- **Tools:** cec_lookup_conductor_ampacity, compare_with_nec, cec_exception_search
- **compare_with_nec called:** Yes

<details>
<summary>Answer (ON mode)</summary>

## Ampacity of 4/0 AWG Copper at 75°C (CEC 2022) – Final Answer

**Base Rule:**  
- **Ampacity:** 230 amperes (CEC Table 310.16, 75°C column for copper)  

**Exceptions Checked:**  
1. **Section 440.6 (HVAC Equipment):**  
   - Applies to hermetic refrigerant motor-compressors and multimotor equipment.  
   - Allows using "branch-circuit selection current" instead of rated-load current for conductor sizing.  
   - **Not applicable** to general conductor ampacity unless specifically for HVAC equipment.  

2. **Section 110.40 (Termination Temperature Limits):**  
   - Permits using 90°C ampacity (Table 311.60) for conductors if terminations are rated for 90°C.  
   - **Does not override** the 75°C value in Table 310.16 unless termination conditions apply.  

**Final Answer:**  
The ampacity of 4/0 AWG copper conductor at 75°C is **230 amperes** under CEC 2022. Exceptions (440.6, 110.40) apply only to specific equipment/termination scenarios and do not affect this general case.  

✓ Source: CEC 2022 Table 310.16 / Exceptions 440.6, 110.40

</details>

#### Analysis

- **Time Difference:** +1.8s
- **Tools Added:** compare_with_nec
- **Verification (compare_with_nec only when ON):** PASS

---

### cec-018 - Table lookup

**Question:** What is the general lighting load in VA per square foot for office buildings according to California code?

#### Mode: NEC Comparison OFF

- **Duration:** 8.5s
- **Iterations:** 4
- **Tools:** cec_search, cec_exception_search
- **compare_with_nec called:** No

<details>
<summary>Answer (OFF mode)</summary>

## General Lighting Load for Office Buildings (CEC 2022)

The general lighting load for **office buildings** in California is **1.3 volt-amperes per square foot (VA/ft²)** per CEC 2022 Table 220.12.

### Exceptions and Notes:
1. **Energy Code Compliance Exception** (Section 220.12(B)):
   - If the building complies with a local energy code, the lighting load may use energy code values **if**:
     - A power monitoring system is installed.
     - The system has alarm thresholds for load exceedance.
     - Demand factors from Table 220.42 are **not applied**.
     - The 125% continuous load multiplier is applied.

2. **Footnote Context**:
   - The 1.3 VA/ft² value assumes 100% power factor and minimum load conditions (Section 220.12 informational note).

✓ Source: CEC 2022 Section 220.12 (Table 220.12)

</details>

#### Mode: NEC Comparison ON

- **Duration:** 19.3s
- **Iterations:** 7
- **Tools:** cec_search, cec_lookup_table, cec_exception_search, compare_with_nec
- **compare_with_nec called:** Yes

<details>
<summary>Answer (ON mode)</summary>

## General Lighting Load for Office Buildings: CEC 2022 vs NEC 2023

### **California Electrical Code (CEC 2022)**
- **Base Value**: **1.3 VA/ft²** (Table 220.12)  
- **Key Features**:  
  - **125% continuous load multiplier already included** in the table value (per 210.20(A)).  
  - **Exception 220.12(B)**: Permits substitution with local energy code values **if**:  
    1. Power monitoring system installed.  
    2. Alarms for load exceedances.  
    3. Demand factors from 220.42 **not applied**.  
  - **Informational Note**: Values assume 100% power factor; actual installations may need higher capacity.  

### **National Electrical Code (NEC 2023)**
- **Base Value**: **3.5 VA/ft²** (Table 220.42(A))  
- **Key Features**:  
  - **125% continuous load multiplier must be applied separately**, resulting in **4.38 VA/ft²**.  
  - No exception for energy code substitution.  
  - Demand factors from Table 220.42 apply to general lighting loads.  

---

### **Side-by-Side Comparison**
| **Parameter**               | **CEC 2022**                          | **NEC 2023**                          |
|-----------------------------|----------------------------------------|----------------------------------------|
| **Base Table Value**        | 1.3 VA/ft² (with 125% included)        | 3.5 VA/ft²                             |
| **Effective Value**         | 1.3 VA/ft² (pre-applied 125%)           | 4.38 VA/ft² (post-calculation)         |
| **Energy Code Flexibility** | Permitted via 220.12(B) with monitoring | Not specified                          |
| **Demand Factors**          | Excluded per 220.12(B)                 | Included per 220.42                    |

---

### **California-Specific Amendments [CEC]**
- **Lower Base Load**: Reflects Title 24 energy efficiency standards.  
- **Embedded 125% Factor**: Simplifies calculations by pre-including continuous load requirements.  
- **Energy Code Path**: Allows reduced loads if monitoring systems are implemented (Exception 220.12(B)).  

✓ **Source**: CEC 2022 Sections 220.12, 220.42; NEC 2023 Sections 220.42, 220.12

</details>

#### Analysis

- **Time Difference:** +10.8s
- **Tools Added:** cec_lookup_table, compare_with_nec
- **Verification (compare_with_nec only when ON):** PASS

---

### cec-021 - Calculation

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.

#### Mode: NEC Comparison OFF

- **Duration:** 8.6s
- **Iterations:** 4
- **Tools:** cec_lookup_conductor_ampacity, cec_exception_search
- **compare_with_nec called:** No

<details>
<summary>Answer (OFF mode)</summary>

## Adjusted Ampacity Calculation (CEC 2022) with Exceptions

1. **Base Ampacity**:  
   8 AWG THWN copper = **50A** @ 75°C (CEC Table 310.16)

2. **Temperature Correction (40°C ambient)**:  
   Factor = **0.88** (CEC Table 310.15(B)(1))

3. **Bundling Adjustment (7 conductors)**:  
   Factor = **0.70** (CEC Table 310.15(C)(1))

4. **Final Calculation**:  
   ```
   50A × 0.88 × 0.70 = 30.8A
   ```

5. **Exception Check**:  
   - **Section 310.15** confirms temperature correction and bundling adjustments are permitted **if the corrected ampacity does not exceed the termination temperature rating** (110.14(C)).  
   - THWN conductors are rated for 75°C, but terminations (e.g., breakers) are often limited to 60°C or 75°C. If terminations are 60°C, further derating is required.  
   - **No exceptions apply** to this specific calculation (HVAC/440.6 and motor control/427.45 exceptions are irrelevant here).

6. **Limiting Rule Check**:  
   - Section 240.4(D) allows 8 AWG copper up to **40A** OCP (no conflict with 30.8A adjusted ampacity).

**Final Answer**: **30.8 amperes**  
✓ Source: CEC 2022  
✓ Exceptions reviewed: 310.15 (temperature/termination limits), 440.6 (HVAC), 427.45 (motor control)  
✓ Calculated using:  
  - Table 310.16 (base ampacity)  
  - Table 310.15(B)(1) (temperature correction)  
  - Table 310.15(C)(1) (bundling adjustment)  
  - Section 240.4(D) (overcurrent protection)

</details>

#### Mode: NEC Comparison ON

- **Duration:** 11.1s
- **Iterations:** 5
- **Tools:** cec_derated_ampacity, compare_with_nec, cec_exception_search
- **compare_with_nec called:** Yes

<details>
<summary>Answer (ON mode)</summary>

## Final Adjusted Ampacity with Exception Check (CEC 2022)

### **Base Calculation**
- **Base Ampacity**: 50A (Table 310.16, 8 AWG THWN @ 75°C)
- **Temp Correction**: 0.88 (Table 310.15(B)(1), 40°C ambient)
- **Bundling Factor**: 0.70 (Table 310.15(C)(1), 7 conductors)
- **Final Calculation**:  
  `50A × 0.88 × 0.70 = 30.8A`

### **Exception Review**
1. **Section 440.6 (HVAC equipment)**:  
   - Applies only to **hermetic refrigerant motor-compressors** or **multimotor equipment**.  
   - **Not applicable** here (general wiring, not HVAC-specific).

2. **Section 427.45 (Conductor in ferromagnetic envelope)**:  
   - Permits exceeding Table 310.16 ampacity for conductors **inside a ferromagnetic envelope**.  
   - **Not applicable** here (standard THWN in raceway, no special insulation/environment).

### **Conclusion**
No applicable exceptions modify the calculation.  

**Final Answer**:  
Adjusted ampacity is **30.8A** under CEC 2022.

</details>

#### Analysis

- **Time Difference:** +2.5s
- **Tools Added:** compare_with_nec, cec_derated_ampacity
- **Verification (compare_with_nec only when ON):** PASS

---

## Conclusion

The NEC comparison toggle is working as expected.

- When OFF: Agent uses only CEC tools
- When ON: Agent additionally calls `compare_with_nec` to show differences from NEC 2023
- Average overhead: +3.2s per question

