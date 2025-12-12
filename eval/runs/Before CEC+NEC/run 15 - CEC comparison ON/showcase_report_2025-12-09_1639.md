# CEC vs NEC Comparison Showcase

**Date:** 2025-12-09_1639

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 3 |
| Questions with NEC Comparison | 2/3 |

## Questions Tested

These questions demonstrate meaningful CEC vs NEC differences:

### showcase-01 - CA policy

**Question:** What are the panelboard space requirements for single-family dwellings in California?

**Expected CEC:** Reserved spaces required for heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers (Section 408.2(A))

**Expected NEC Difference:** NEC has NO reserved space requirements for specific appliances

**Why Good for Showcase:** California-unique electrification mandate - NEC has no equivalent

**Status:** NEEDS REVIEW

---

### showcase-02 - GFCI

**Question:** What are the kitchen GFCI requirements in California?

**Expected CEC:** GFCI required for countertop surfaces and within 6 feet of sink (Section 210.8(A))

**Expected NEC Difference:** NEC requires GFCI for ALL kitchen receptacles including refrigerators (more restrictive)

**Why Good for Showcase:** Shows California is MORE PERMISSIVE - bidirectional difference

**Status:** PASS

<details>
<summary>Full Answer</summary>

## Kitchen GFCI Requirements in California vs. NEC 2023  

### **California Electrical Code (CEC 2022)**  
- **CEC 210.8(A)(6)**: **All countertop receptacles** in kitchens must have **GFCI protection**.  
- **No exceptions** apply to countertop circuits in residential kitchens.  
- **Additional Requirements**:  
  - Receptacles within **1.8 m (6 ft)** of sinks require GFCI (CEC 210.8(A)(7)).  
  - Laundry areas must also have GFCI (CEC 210.8(A)(11)).  
- **Exceptions**:  
  - **Locking receptacles** for ceiling luminaires/fans are exempt if not used for general-purpose convenience.  

---

### **National Electrical Code (NEC 2023)**  
- **NEC 210.8(A)(6)**: Requires GFCI for countertop receptacles in kitchens.  
- **Exceptions**:  
  - **Listed locking receptacles** used with ceiling fixtures (e.g., fans) are exempt.  
  - Industrial labs may exclude GFCI if power interruption creates greater hazards (NEC 210.8(A) Exception).  
- **Flexibility**:  
  - Allows GFCI protection via **circuit breakers or receptacles**.  
  - Permits exceptions for specialized equipment (e.g., fire alarm systems).  

---

### **Key Differences**  
| **Aspect**                | **CEC 2022**                          | **NEC 2023**                          |  
|---------------------------|----------------------------------------|---------------------------------------|  
| **Countertop GFCI**       | **Mandatory with no exceptions**       | Mandatory but allows exceptions for locking receptacles |  
| **Sink Proximity**        | 1.8 m (6 ft) from sink edge             | Same 1.8 m (6 ft) requirement         |  
| **Exceptions**           | None for residential countertop circuits| Exceptions for industrial and specialized fixtures |  
| **Appliance-Specific Rules**| No special exceptions                   | Allows exceptions for vending machines, etc. (NEC 422.5) |  

---

### **Code Citations**  
- **CEC**: 210.8(A)(6), 210.8(A)(7), 210.8(A)(11)  
- **NEC**: 210.8(A)(6), 422.5(B)  

---

**Comparison Tool Output**:  
```json  
{  
  "cec_section": "210.8(A)(6)",  
  "nec_section": "210.8(A)(6)",  
  "difference": "CEC mandates GFCI for all kitchen countertop receptacles with no exceptions, while NEC allows exceptions for listed locking receptacles used with ceiling fixtures and industrial equipment."  
}  
```  

✓ **Source**: CEC 2022, NEC 2023, compare_with_nec tool results.

</details>

---

### showcase-03 - EV infrastructure

**Question:** What are the EV charging infrastructure requirements for new residential construction in California?

**Expected CEC:** EV-ready infrastructure mandated: dedicated circuits, conduit, panel capacity (Title 24/CALGreen)

**Expected NEC Difference:** NEC Article 625 only provides installation rules - no mandate

**Why Good for Showcase:** California as regulatory leader with proactive requirements

**Status:** PASS

<details>
<summary>Full Answer</summary>

## EV Charging Infrastructure Requirements for New Residential Construction (CEC 2022 vs. NEC 2023)

---

### **California Electrical Code (CEC 2022) Requirements**
1. **Dedicated Branch Circuit**  
   - **CEC 625.40**: Each EV charging outlet must have a **dedicated branch circuit** with **no other outlets**.  
   - **Minimum Rating**: **40 amperes** (mandatory for residential use).  

2. **CALGreen Mandate**  
   - **Title 24 Part 6, Section 110.6.1.1**: New residential buildings must include **at least one 40A, 240V circuit** in each garage for EV charging.  
   - **Panelboard Space**: Reserved circuit breaker space for EV charging (CEC 408.2).  

3. **Receptacle and Wiring**  
   - **CEC 625.44**: Receptacles must be rated **250 volts, 50 amperes** (e.g., NEMA 14-50).  
   - **Weatherproof Enclosures**: Required for outdoor EVSE (CEC 625.56).  

4. **No Exceptions for Residential Garages**  
   - **CEC 625.1.1**: Compliance with CALGreen Chapter 4 and 5 is mandatory, with **no exceptions** for single-family dwellings.  

---

### **National Electrical Code (NEC 2023) Comparison**
- **NEC 625.14**: Requires a dedicated branch circuit but allows **30A or 40A** depending on the EVSE.  
- **Flexibility**: Permits 30A circuits for Level 1 (120V) charging.  
- **No Garage Mandate**: No requirement for a dedicated circuit in every residential garage.  
- **Load Calculations**: NEC 220.57 allows EVSE load to be calculated at **7200 VA** or nameplate rating, whichever is larger.  

---

### **Key Differences**
| **Aspect**                | **CEC 2022**                          | **NEC 2023**                          |  
|---------------------------|--------------------------------------|---------------------------------------|  
| **Minimum Circuit Rating** | **40A** (mandatory for residential)  | **30A or 40A** (depends on EVSE)      |  
| **Garage Circuit Mandate** | **1 circuit per garage** (CALGreen) | **No mandate** for residential garages  |  
| **Panelboard Space**       | **Reserved space** for EV circuits   | **No requirement** for reserved spaces|  
| **Exceptions**            | **None** for residential garages     | **Exceptions** for industrial/commercial use |  

---

### **Code Citations**
- **CEC**: 625.1.1, 625.40, 625.44, 625.56, Title 24 Part 6, Section 110.6.1.1  
- **NEC**: 625.14, 220.57, 625.44  

---

**Comparison Tool Output**:  
```json  
{  
  "cec_section": "625.1.1",  
  "nec_section": "625.14",  
  "difference": "CEC mandates 40A minimum for all residential EV circuits and requires one circuit per garage (CALGreen), while NEC allows 30A circuits and lacks a garage-specific mandate."  
}  
```  

✓ **Source**: CEC 2022, NEC 2023, compare_with_nec tool results.

</details>

---

