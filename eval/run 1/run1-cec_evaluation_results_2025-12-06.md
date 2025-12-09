# CEC Agent Evaluation - LangChain + Groq

**Date:** 2025-12-06
**Model:** qwen/qwen3-32b
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 5 |
| **Successful** | 5 (100.0%) |
| **Failed** | 0 |
| **Total Duration** | 69.1s |
| **Avg per Question** | 13.8s |

---

## Results by Question


## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?

**Expected:** CEC 408.2 requires panelboards in single-family dwellings to have reserved spaces for branch circuits for: (1) heat pump water heaters, (2) heat pump space heaters, (3) electric cooktops, (4) electric clothes dryers, and (5) electric vehicle charging equipment. This is a California-specific requirem...

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only requirement

**Status:** PASS

**Agent Answer:**
## Panelboard Space Requirements for Single-Family Dwellings (CEC 2022) – Final Answer

---

### **1. Reserved Circuit Breaker Spaces for Appliances**
**California Requirement (CEC 2022 Section 408.2(A)):**
- **Mandatory Reserved Spaces**: Panelboards in single-family dwellings must include pre-wired circuit breaker spaces for:
  - Heat pump water heaters
  - Heat pump space heaters
  - Electric cooktops
  - Electric clothes dryers  
  *This is a California Energy Code mandate (Section 150.0(n), (t), (u), (v)).*

**Exceptions Checked**:
- No exceptions to **Section 408.2(A)** were found that would modify or remove this appliance-specific requirement.
- Exceptions in related sections (e.g., 408.36, 408.38) address overcurrent protection and enclosures, not reserved spaces for appliances.

---

### **2. General Panelboard Requirements**
- **Minimum Rating**: Panelboards must have a rating ≥ calculated feeder capacity (Section 408.30).
- **Enclosure Type**: Must be "dead-front" (no live parts exposed on the front) unless accessible only to qualified personnel (Section 408.38).
- **Wire-Bending Space**: Sized per Table 312.6(A)/(B), with exceptions for smaller panelboards (≤225A, ≤42 devices) (Section 408.55).

---

## NEC 2023 Reference
- **Reserved Spaces**: **Not required** by NEC 2023. The appliance-specific reserved spaces are a **California amendment**.
- **General Requirements**: NEC 2023 Sections 408.30, 408.38, and 408.55 align with CEC requirements for panelboard ratings, enclosures, and wire-bending spaces.

✓ **Sources: CEC 2022 (California), NEC 2023 (reference)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 7 found
- 408.30, 408.38, 408.36, 408.55, 408.2, 312.6, 150.0

**Response Time:** 25.6s

---

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new construction including dedicated 40-amp minimum circuits, conduit to parking spaces, and panel capacity for EV loads. CEC 408.2 requires panelboard spaces for EV charging equipment. Title 24 also mandates EV charging readiness.

**CEC Ref:** CEC 408.2, Title 24 | **NEC Ref:** NEC 625 (general installation only)

**Status:** PASS

**Agent Answer:**
## California Electrical Requirements for EV Charging in New Residential Construction (CEC 2022)  

### **Key CEC 2022 Requirements**  
1. **Dedicated Branch Circuit**  
   - **625.40**: Each EV charging outlet must be supplied by an **individual branch circuit** with **no other outlets** on the same circuit.  
   - **Exception 625.42**: Adjustable ratings are permitted for fixed-in-place equipment if adjustments are restricted to qualified personnel (e.g., locked enclosures, password-protected software).  

2. **Connection Methods**  
   - **625.44**:  
     - **Portable Equipment**: Must use listed receptacles rated 15–50A, 125–250V (e.g., NEMA 14-50).  
     - **Fastened-in-Place Equipment**: Requires listed receptacles up to 50A, 250V.  
     - **Fixed Equipment**: Must be **permanently wired**.  
   - **Exception 625.47**: Multiple feeders/branch circuits are permitted if equipment is identified for the application.  

3. **Backfeeding Prevention**  
   - **625.46**: Systems with power export functions must prevent backfeeding to the premises wiring when utility power is lost.  

4. **Weatherproof Enclosures**  
   - **625.56**: Receptacles in wet locations require **weatherproof enclosures** (e.g., extra-duty outlet box hoods).  

5. **GFCI Protection**  
   - **625.56(D)**: **GFCI protection** is required for all EV charging receptacles.  
   - **Exception 647.7**: Technical power systems in restricted areas (e.g., data centers) may exempt GFCI, but this does not apply to residential installations.  

---

### **Exceptions and Overrides**  
- **625.42**: Adjustable ratings for fixed equipment with restricted access (e.g., locked enclosures).  
- **625.46**: Backfeeding prevention for systems with power export.  
- **625.47**: Multiple circuits permitted for identified equipment.  
- **250.86**: Grounding exceptions for short metal enclosures (not applicable to EV receptacles).  

---

### **NEC 2023 Comparison**  
- **Similar Requirements**: NEC 625.40 and 62...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 625.46, 625.47, 250.86, 625.44, 625.42, 647.7, 625.40, 625.56

**Response Time:** 12.8s

---

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes (Title 24 Part 6). Electrical requirements include rapid shutdown per CEC 690.12, arc-fault protection per CEC 690.11, specific grounding requirements per 690.41-47, and multiple disconnecting means requirements.

**CEC Ref:** CEC 690, Title 24 Part 6 | **NEC Ref:** NEC 690 (installation rules only, no mandate)

**Status:** PASS

**Agent Answer:**
## California-Specific Solar PV Requirements (CEC 2022)

### Key CEC 2022 Requirements for Residential Solar PV Systems:
1. **Voltage Limits**  
   - DC circuits in **one- and two-family dwellings** are limited to **600 volts maximum** (CEC 690.7).  
   - Circuits in buildings (non-residential) may go up to **1,000 volts**.  
   - Use temperature correction factors (Table 690.7(A)) for crystalline silicon modules to calculate maximum voltage based on lowest expected ambient temperature.

2. **Arc-Fault Protection**  
   - Required for all PV systems with **≥80V DC** operating between conductors (CEC 690.11).  
   - **Exception**: Systems not installed on/in buildings (e.g., ground-mounted arrays in enclosures) may skip arc-fault protection if installed in metallic raceways, metal-clad cables, or enclosed trays (CEC 690.11 Exception).

3. **Conductor Sizing**  
   - Conductors must carry **≥125% of the calculated maximum current** (CEC 690.8(B)(1)).  
   - For source circuits: Maximum current = sum of parallel module short-circuit currents × 125% (CEC 690.8(A)(1)(a)(1)).  
   - Adjustments for temperature and bundling apply unless using listed assemblies rated for continuous 100% operation (CEC 690.8(B) Exception).

4. **Overcurrent Protection**  
   - Overcurrent devices must be **rated ≥125% of calculated maximum current** (CEC 690.9(B)(1)).  
   - Single overcurrent devices may protect parallel source circuits if all devices are in the same polarity (CEC 690.9(C)).  
   - **Exception**: Conductors ≤3m (10 ft) in length, installed in metal raceways, or underground may use single-end protection (CEC 690.9(A)(4)).

5. **System Grounding and Rapid Shutdown**  
   - PV systems must comply with CEC 690.4(D) for grounding and 690.41 for rapid shutdown (not detailed here but critical for compliance).

---

## NEC 2023 Comparison
- **Voltage Limits**: NEC 690.7 allows **1,000V DC** in all buildings (no 600V residential limit in NEC).  
- **Arc-Fault Protection**: NEC 690.1...

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 6 found
- 690.4, 690.7, 690.11, 690.9, 690.8, 690.41

**Response Time:** 10.6s

---

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for a heat pump water heater branch circuit. This is part of California's decarbonization requirements to ensure electrical infrastructure can support heat pump water heaters as replacements for gas water heaters.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Final Answer: Circuit Requirements for Heat Pump Water Heaters in California (CEC 2022)

**California Requirement (CEC 2022):**

1. **Single-Family Buildings (1-2 dwellings):**
   - **Dedicated Circuit Spaces:** Panelboards must include dedicated circuit breaker spaces for heat pump water heaters per **CEC 2022 Section 408.2(A)** and California Energy Code Section 150.0(n).
   - **Branch Circuits:** Designated branch circuits and receptacles must be provided as specified in California Energy Code Section 150.0(n) (per **Section 422.3(A)**).

2. **Multifamily Buildings:**
   - **Dedicated Circuits:** Each dwelling unit must have dedicated circuits and circuit identifications for heat pump water heaters per **CEC 2022 Section 422.3(B)** and California Energy Code Section 160.9(b).

**Exceptions Checked:**
- **Section 422.12** (central heating equipment exceptions) and **Section 422.47** (water heater controls) do not apply to heat pump water heaters in this context.
- **Section 408.36** (panelboard overcurrent protection) does not override the dedicated circuit requirements for heat pump water heaters.

**Key Exception Notes:**
- No exceptions in the CEC override the mandatory readiness provisions for heat pump water heaters.
- **Special permission** under **Section 422.23** could allow non-standard installations, but standard dedicated circuits remain the default requirement.

---
## NEC 2023 Reference
These requirements are **California-specific amendments** [CEC]. The base NEC 2023 does not mandate pre-wiring for heat pump water heaters in dwelling units. California’s Energy Code provisions ensure future compatibility with energy-efficient appliances.

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 8 found
- 422.47, 408.36, 422.12, 408.2, 160.9, 422.3, 150.0, 422.23

**Response Time:** 10.1s

---

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space for electric cooktop branch circuits. This ensures homes are ready for all-electric cooking appliances as part of California's building electrification requirements.

**CEC Ref:** CEC 408.2 | **NEC Ref:** N/A - CEC only

**Status:** PASS

**Agent Answer:**
## Electric Cooktop Readiness Requirements (CEC 2022)  
**Primary Rule:**  
Per **CEC 2022 Section 408.2(A)**, new single-family homes **must have panelboards pre-wired with dedicated circuit breaker spaces** for electric cooktops (along with heat pump water heaters, heat pump space heaters, and dryers). This supports California's Title 24 Energy Code mandates for future-ready electrical infrastructure.

---

### Exceptions Checked (CEC 2022)  
1. **Section 422.23** & **424.10** (Special Permission for Alternative Installations):  
   - Allow non-standard installation methods **only with special permission**.  
   - **Does not override** the pre-wiring requirement in 408.2.  

2. **Section 210.52(C)** (Kitchen Receptacle Outlets):  
   - Exempts areas directly behind ranges/counter-mounted cooking units from receptacle spacing rules.  
   - **Unrelated** to panelboard pre-wiring for cooktops.  

**Conclusion:** No exceptions invalidate the core requirement in 408.2. The rule applies universally unless special permission is granted for alternative installations (which is rare and requires approval).

---

### NEC 2023 Reference  
This is a **California-specific amendment** [CEC]. The base NEC 2023 (Article 408) does not require pre-wiring for future electric appliances. California’s rule directly supports electrification goals under Title 24 Energy Code.  

**Violation Risk:** Failing to pre-wire for electric cooktops in new single-family homes violates **CEC 408.2(A)** and Title 24.  

✓ **Sources: CEC 2022 (primary), NEC 2023 (comparison)**

**Tool Usage:**
- CEC Tools: cec_search, cec_exception_search
- NEC Tools: None
- CEC Primary: Yes

**Citations:** 4 found
- 210.52, 424.10, 408.2, 422.23

**Response Time:** 10.0s

---


## Analysis

### Key Metrics

- **CEC-Primary Responses**: 5/5
- **Success Rate**: 100.0%
- **Average Response Time**: 13.8s

### Model Information

- **Provider**: Groq
- **Model**: qwen/qwen3-32b
- **Framework**: LangChain + LangGraph

