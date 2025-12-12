---
editor_options: 
  markdown: 
    wrap: 72
---

# CEC Agent Evaluation - Run 21 (Removed Hardcoded Values)

**Date:** 2025-12-09 **Model:** qwen/qwen3-32b **Agent:** California
Electrical Code Agent (LangChain) **NEC Comparison:** ENABLED **Prompt
Version:** v4 - no hardcoded values

## Key Changes in This Run

1.  **Removed all hardcoded values from SYSTEM_PROMPT** - No more
    specific AWG sizes, VA/sqft values, or ampacities in examples
2.  **Examples use placeholders** - e.g., "[size from tool]", "[value
    from table]"
3.  **Model must call tools for ALL values** - Cannot rely on memorized
    prompt content
4.  **Replaced Unicode characters** - Arrows, checkmarks, degree symbols
    replaced with ASCII

## Executive Summary

| Metric                                  | Value       |
|-----------------------------------------|-------------|
| **Total Questions**                     | 30          |
| **Successful**                          | 30 (100.0%) |
| **Failed**                              | 0           |
| **Exception Search Called (Voluntary)** | 3/30        |
| **Total Duration**                      | 340.0s      |
| **Avg per Question**                    | 11.3s       |

------------------------------------------------------------------------

## Results by Question

## California-Unique Requirements

### cec-001: panelboard_requirements [CA-SPECIFIC]

**Question:** What are the panelboard space requirements for
single-family dwellings in California? What appliances must have
reserved circuit breaker spaces?

**Expected:** CEC 408.2(A) requires panelboards in single-family
dwellings to have reserved spaces for branch circuits for: (1) heat pump
water heaters, (2) heat pump space heaters, (3) electric cooktops, and
(4) e...

**Status:** PASS

**Agent Answer:** \## Panelboard Space Requirements for Single-Family
Dwellings (CEC 2022)

### **Reserved Circuit Breaker Spaces**

Per **CEC 2022 Section 408.2(A)**, single-family residential panelboards
must include **dedicated circuit breaker spaces** for:\
1. **Heat pump water heaters**\
2. **Heat pump space heaters**\
3. **Electric cooktops**\
4. **Electric clothes dryers**

This requirement is mandated by the **California Energy Code Section
150.0(n), (t), (u), and (v)** to ensure future-ready electrical
infrastructure for electrification and energy efficiency.

------------------------------------------------------------------------

### **NEC 2023 Comparison**

**NEC 2023 does not mandate reserved circuit breaker spaces** for
specific appliances. Key differences:

| **Aspect**                  | **CEC 2022**                                                                                                       | **NEC 2023**                                                                                                                     |
|----------------|----------------------------|----------------------------|
| **Reserved Spaces**         | Requires reserved spaces for **4 specific appliances** (heat pump water heater, heat pump heater, cooktop, dryer). | **No reserved spaces** required for appliances. Panelboards must only have sufficient spaces for installed circuits (NEC 408.3). |
| **Electrification Support** | Proactively allocates spaces for electrification (e.g., heat pumps).                                               | No specific provisions fo...                                                                                                     |

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 4 found

**Response Time:** 14.7s

------------------------------------------------------------------------

### cec-002: ev_charging [CA-SPECIFIC]

**Question:** What are California's electrical requirements for EV
charging infrastructure in new residential construction?

**Expected:** California requires EV-ready infrastructure in new
construction including dedicated 40-amp minimum circuits, conduit to
parking spaces, and panel capacity for EV loads. These requirements are
found in...

**Status:** PASS

**Agent Answer:** \## California EV Charging Requirements (CEC 2022) vs
NEC 2023

### **Core CEC Requirements for New Residential Construction**

1.  **CALGreen Compliance** (CEC 625.1):
    -   **Mandatory EV readiness**: New residential buildings must
        include infrastructure for EV charging (CALGreen Chapter 4,
        Division 4.1).\
    -   **Panelboard space**: Reserved circuit breaker space for future
        EV charging (CEC 408.2).
2.  **Dedicated Circuits** (CEC 625.40):
    -   Each EV charging outlet **must be on an individual branch
        circuit** with **no other outlets**.\
    -   **NEC Comparison**: NEC 625.40 also requires dedicated circuits
        but allows shared circuits for "lighting and receptacles" in
        garages (NEC 210.11(B)). CEC is stricter.
3.  **Receptacle Requirements** (CEC 625.44):
    -   **Portable EVSE**: Must use listed receptacles rated 125V,
        15–20A (e.g., NEMA 5-15R/5-20R).\
    -   **Fixed EVSE**: Requires 240V, 50A circuits with NEMA 14-50R or
        equivalent.\
    -   **NEC Comparison**: NEC 625.21(A) allows similar receptacles but
        does not mandate specific ratings for residential EV readiness.
4.  **Ventilation** (CEC 625.52):
    -   **Indoor charging**: Mechanical ventilation required unless
        equipment is listed for no-ventilation use.\
    -   **Formula-based calculations**: Ventilation rates depend on EV
        count and power (Tables 625.52(B)(1)(a/b)).\
    -   **NEC Comparison**: NEC 625 does not address ventilation for
        residential EV charging.
5.  **Ground-Fault Protection** (CEC 625.54):
    -   \*\*All EV ...

**Tool Usage:** - CEC Tools: cec_search, cec_exception_search - NEC
Tools: compare_with_nec - Exception Search Called: Yes

**Citations:** 10 found

**Response Time:** 13.0s

------------------------------------------------------------------------

### cec-003: solar_pv [CA-SPECIFIC]

**Question:** What are the California-specific electrical requirements
for solar PV systems on new residential construction?

**Expected:** California mandates solar PV on new single-family homes
(Title 24 Part 6). Electrical requirements include rapid shutdown per
CEC 690.12, arc-fault protection per CEC 690.11, specific grounding
requir...

**Status:** PASS

**Agent Answer:** \## California Solar PV Requirements (CEC 2022) vs NEC
2023

### 1. **Rapid Shutdown Requirements**

-   **CEC 690.56(C):**
    -   Mandates **yellow-on-black labels** (minimum 9.5mm lettering) at
        service equipment locations showing rapid shutdown switch
        locations.
    -   Requires **detailed roof diagrams** for buildings with multiple
        PV systems showing energized areas post-shutdown.
    -   **Rapid shutdown switch labels** must be **red-on-white** with
        "RAPID SHUTDOWN SWITCH" in 9.5mm letters.
-   **NEC 690.12:**
    -   Requires rapid shutdown but allows more general labeling (no
        specific color/size requirements).
    -   No explicit diagram requirement for multi-system roofs.

### 2. **Arc-Fault Protection**

-   **CEC 690.11:**
    -   Requires DC arc-fault protection for all PV systems ≥80V DC.
    -   **Exception:** Systems in metallic raceways or underground are
        exempt (same as NEC).
-   **NEC 690.11:**
    -   Same 80V DC threshold but **no exception** for metallic raceways
        in all cases (CEC has broader exception).

### 3. **Grounding & Bonding**

-   **CEC 690.43/47:**
    -   Requires PV module frames to be bonded using **listed bonding
        devices** (not just metal supports).
    -   Grounding electrode conductor must be sized per **Table 250.66**
        (same as NEC).
-   **NEC 690.43:**
    -   Allows bonding via metal supports without listed devices (CEC
        adds explicit listing requirement).

### 4. **Labeling & Documentation**

-   **CEC 690.56:**
    -   **Mandatory solar labels** at service panels with **graphical
        roof diagrams**...

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 7 found

**Response Time:** 10.7s

------------------------------------------------------------------------

### cec-004: heat_pump [CA-SPECIFIC]

**Question:** What circuit requirements does California have for heat
pump water heaters in new dwelling units?

**Expected:** Per CEC 408.2, panelboards must have a reserved space for
a heat pump water heater branch circuit. This is part of California's
decarbonization requirements to ensure electrical infrastructure can
sup...

**Status:** PASS

**Agent Answer:** \## California Heat Pump Water Heater Requirements
(CEC 2022)

### **Key Requirements**

1.  **Overcurrent Protection (CEC 422.13):**
    -   Fixed storage-type water heaters ≤ 450 L (120 gal) must have
        branch-circuit overcurrent devices sized to **at least 125% of
        the heater's rated current**.
    -   Example: A 20A-rated heater requires a **25A minimum OCPD** (20A
        × 1.25).
2.  **Temperature Controls (CEC 422.47):**
    -   All storage and instantaneous water heaters must have a
        **temperature-limiting device** (in addition to the thermostat)
        to disconnect power if water exceeds safe limits.
    -   **Exceptions**:
        -   Storage heaters ≥ 60 kW rated for ≥ 82°C (180°F).
        -   Instantaneous heaters ≤ 4 L (1 gal).
3.  **General Overcurrent Rules (CEC 422.11):**
    -   Follow **NEC 240.4** for overcurrent protection.
    -   If the appliance is marked with a protective device rating, the
        OCPD must not exceed this value.

------------------------------------------------------------------------

### **CEC vs NEC 2023 Comparison**

| **Requirement**        | **CEC 2022**                                               | **NEC 2023**              |
|----------------|----------------------------|----------------------------|
| **Overcurrent Sizing** | 125% of heater rating for storage heaters ≤ 450 L (422.13) | Same as CEC (422.13). ... |

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 5 found

**Response Time:** 9.1s

------------------------------------------------------------------------

### cec-005: electrification [CA-SPECIFIC]

**Question:** What is required for electric cooktop readiness in new
California homes?

**Expected:** CEC 408.2 requires panelboards to have a reserved space
for electric cooktop branch circuits. This ensures homes are ready for
all-electric cooking appliances as part of California's building
electrif...

**Status:** PASS

**Agent Answer:** \## Electric Cooktop Readiness in California vs. NEC
2023

### **California Code Requirements (CEC 2022)**

1.  **Single-Family Homes**
    -   **Dedicated circuits** for electric cooktops must be
        pre-installed (CEC 422.3(A), CalEnergyCode §150.0(u)).\
    -   **Panelboard spaces** reserved in service panels (CEC 408.2(A)).
2.  **Multifamily Buildings**
    -   **Dedicated circuits** required in each unit (CEC 422.3(B),
        CalEnergyCode §160.9(b)).\
    -   **Circuit identification** for future electric cooktops (CEC
        408.2(B)).

**Purpose**: Enforces infrastructure readiness to support
electrification goals (Title 24, Part 6; CALGreen).

------------------------------------------------------------------------

### **NEC 2023 Comparison**

-   **No "readiness" requirements**: NEC 422.1 and 408.36 only address
    installed appliances.\
-   **Dedicated circuits**: NEC requires dedicated circuits *only if*
    the appliance is installed (e.g., NEC 220.55 for ranges).\
-   **Panelboard spaces**: NEC 408.36 mandates spaces for *installed*
    appliances but does **not** require pre-wiring for uninstalled
    equipment.

------------------------------------------------------------------------

### **Key Differences**

| **Aspect**            | **California (CEC 2022)**                    | **NEC 2023**              |
|------------------|--------------------------------|----------------------|
| **Readiness Mandate** | Requires pre-wiring for uninstalled cooktops | No proactive requirements |
| **Panelboard Spaces** | Reserved spaces for future cooktops          | ...                       |

**Tool Usage:** - CEC Tools: cec_search, cec_exception_search - NEC
Tools: compare_with_nec - Exception Search Called: Yes

**Citations:** 7 found

**Response Time:** 12.6s

------------------------------------------------------------------------

### cec-006: electrification [CA-SPECIFIC]

**Question:** What are the panelboard requirements for electric clothes
dryer circuits in California new construction?

**Expected:** CEC 408.2 requires panelboards to have a reserved space
for electric clothes dryer branch circuits in single-family dwellings.
This is a California-specific requirement for building electrification.

**Status:** PASS

**Agent Answer:** \## Panelboard Requirements for Electric Clothes Dryer
Circuits (CEC 2022)

### California Electrical Code (CEC) Requirements:

1.  **Single-Family Buildings** (CEC 408.2(A)):
    -   Panelboards must include **reserved circuit breaker spaces** for
        electric clothes dryers.
    -   Mandated by California Energy Code Section 150.0(n).
2.  **Multifamily Buildings** (CEC 408.2(B)):
    -   Panelboards must include **reserved circuit breaker spaces** for
        electric clothes dryers.
    -   Mandated by California Energy Code Section 160.9(a)-(c).

### NEC 2023 Comparison:

-   **NEC 2023 does not specify** reserved panelboard spaces for
    electric clothes dryers.
-   NEC 220.54 only addresses **load calculations** for dryers (5000W
    minimum or nameplate rating).
-   No equivalent to CEC 408.2(A)/(B) exists in NEC.

### Key Difference:

-   **CEC is more restrictive** than NEC by requiring **physical
    panelboard space reservations** for dryers in new residential
    construction, while NEC only addresses electrical load calculations.

[OK] Source: CEC 2022, NEC 2023

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 4 found

**Response Time:** 8.2s

------------------------------------------------------------------------

### cec-007: overcurrent [CA-SPECIFIC]

**Question:** What does CEC Table 240.4(G) specify that is unique to
California?

**Expected:** CEC Table 240.4(G) is a California-only table that
provides additional overcurrent protection requirements. This table does
not exist in the base NEC 2023.

**Status:** PASS

**Agent Answer:** \## CEC Table 240.4(G) Unique to California (CEC 2022)

### Key Differences from NEC 2023:

1.  **Control/Instrumentation Conductors (Type ITC):**
    -   **CEC:** Referenced to **Article 727, Section 727.9** (Class 2/3
        circuits)
    -   **NEC:** Referenced to **Article 335, Section 335.9** (Type ITC
        cables)
    -   *California amendment shifts focus to Class 2/3 circuit
        requirements*
2.  **Remote-Control/Signaling Conductors:**
    -   **CEC:** Cites **725.43, 725.45, 725.121** (California-specific
        power-limited circuit rules)
    -   **NEC:** References **724.43, 724.45, 725.60** (National
        power-limited circuit rules)
    -   *California adds explicit reference to 725.121 for special
        conditions*
3.  **Fire Alarm Conductors:**
    -   **CEC:** Explicitly includes **Chapter 9 Tables 12(A) and
        12(B)** for fire alarm conductor fill
    -   **NEC:** Same reference but without California-specific
        amendments
4.  **Motor-Operated Appliance Conductors:**
    -   **CEC:** No additional section specified (blank)
    -   **NEC:** No difference in this row

### California-Specific Context:

-   **CEC Section 440.51** explicitly references Table 240.4(G) for
    air-conditioning/refrigeration applications, with [CEC delta mark]
    indicating amendments to Article 440 requirements.
-   **CEC Section 220.3** adds cross-references for specific-purpose
    calculations not found in NEC, including modifications to Table
    240.4(G) applications.

### Enforcement Implications:

California's modifications to Table 240.4(G) create \*\*more specific
...

**Tool Usage:** - CEC Tools: cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 11 found

**Response Time:** 7.2s

------------------------------------------------------------------------

### cec-008: surge_protection [CA-SPECIFIC]

**Question:** What does CEC Table 242.3 specify for California
installations?

**Expected:** CEC Table 242.3 is a California-only table related to
surge protection requirements. This table does not exist in the base NEC
2023.

**Status:** PASS

**Agent Answer:** \## CEC Table 242.3 vs NEC 2023 Comparison

### **CEC 2022 Table 242.3 Specifications**

-   **Purpose**: Cross-references equipment types to specific NEC
    articles for overvoltage protection requirements.\
-   **California-Specific**: Marked with an **"N"** (new California
    amendment), not present in NEC.\
-   **Key Entries**:
    -   **Class I/II locations** → Articles 501/502 (hazardous
        locations)\
    -   **Fire pumps** → Article 695\
    -   **Equipment \>1000V** → Article **490** (CEC) vs **495** (NEC)\
    -   **Outdoor overhead conductors \>1000V** → Article **399** (CEC)
        vs **395** (NEC)

------------------------------------------------------------------------

### **CEC vs NEC Differences**

1.  **Article References**:
    -   CEC directs to **Article 490** for equipment over 1000V, while
        NEC uses **Article 495**.\
    -   CEC references **Article 399** for outdoor overhead conductors
        \>1000V, whereas NEC uses **Article 395**.
2.  **Additional CEC Requirements**:
    -   **CEC 242.6**: Prohibits SPD installation on ungrounded systems
        unless listed for such use (no explicit NEC equivalent).\
    -   **CEC 242.3 Note**: Combines and replaces multiple NEC articles
        (e.g., 28, 80, 810) into a unified overvoltage protection
        framework.
3.  **Structural Amendments**:
    -   CEC merges overcurrent (Article 240) and overvoltage (Article
        242) protections under a unified scope, while NEC keeps them
        separate.

------------------------------------------------------------------------

### **Key Takeaways**

-   **California-Specific Table**: Table 242.3 is a **new CEC addition**
    (N marker) with tailored references.\
-   \*\*More Restrict...

**Tool Usage:** - CEC Tools: cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 2 found

**Response Time:** 8.3s

------------------------------------------------------------------------

### cec-009: motor_control [CA-SPECIFIC]

**Question:** What does CEC Table 430.72(B) specify for motor control
circuit overcurrent protection?

**Expected:** CEC Table 430.72(B) specifies maximum ratings of
overcurrent protective devices for motor control circuits based on
conductor size and configuration. It includes columns for separate
protection, condu...

**Status:** PASS

**Agent Answer:** \## CEC Table 430.72(B) vs NEC 2023 Comparison

### **CEC 2022 Table 430.72(B) Specifications**

-   **Purpose**: Specifies maximum overcurrent protective device (OCPD)
    ratings for motor control circuits based on conductor size and
    material.
-   **Key Data**:
    -   **Copper Conductors**:
        -   18 AWG: 7A (Column A), 25A (Column B), 7A (Column C)
        -   16 AWG: 10A (Column A), 40A (Column B), 10A (Column C)
        -   14 AWG: 100A (Column B), 45A (Column C)
        -   12 AWG: 120A (Column B), 60A (Column C)
        -   10 AWG: 160A (Column B), 90A (Column C)
    -   **Aluminum Conductors**: Limited data (marked "—") except for 12
        AWG and larger.
    -   **Larger than 10 AWG**: Notes reference:
        -   **Note 2**: 400% of Table 310.19 (60°C) for Column B.
        -   **Note 3**: 300% of Table 310.16 (60°C) for Column C.

### **NEC 2023 Table 430.72(B)(2) Comparison**

-   **Similar Structure**: Identical conductor sizes and Column A/B/C
    ratings for copper.
-   **Key Differences**:
    1.  **Aluminum/Copper-Clad Aluminum**: NEC includes
        "aluminum/copper-clad aluminum" columns (e.g., 12 AWG aluminum:
        100A Column B, 45A Column C).
    2.  **Terminology**: NEC uses "control_circuit_conductor_size_awg"
        instead of "conductor_size."
    3.  **Notes**: NEC references Table 310.15 (60°C) for larger
        conductors, while CEC uses Table 310.19 and 310.16.

### **Critical Code References**

-   **CEC**:
    -   **430.72(A)**: Motor control circuits must be protected by
        supplementary or branch-circuit OCPDs.
    -   **Notes**: Relies on Tables 310.15, 310.19...

**Tool Usage:** - CEC Tools: cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 5 found

**Response Time:** 6.8s

------------------------------------------------------------------------

### cec-010: medium_voltage [CA-SPECIFIC]

**Question:** What medium voltage cable tables does California have that
are not in the NEC?

**Expected:** CEC has 18 medium voltage tables in the 311.60(C) series
(Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only.
These provide ampacity information for medium voltage cables not found
i...

**Status:** PASS

**Agent Answer:** \## Medium Voltage Cable Tables: CEC vs NEC 2023

### **California (CEC 2022) vs National (NEC 2023) Differences**

#### **1. Medium Voltage Table Scope**

| **Feature**                  | **CEC 2022**                                                  | **NEC 2023**                                                    |
|-----------------------|-------------------------|-------------------------|
| **Voltage Coverage**         | 2001–35,000V (Tables 311.60(C)(67)–86)                        | Up to 2000V (Tables 310.15, 315.60)                             |
| **Installation Conditions**  | Includes isolated conduit, cable trays, and underground ducts | Limited to general cable tray and ducts (no MV-specific tables) |
| **Conductor Configurations** | Triplexed cables, single-layer cables, and bundled cables     | No MV-specific configurations                                   |

------------------------------------------------------------------------

#### **2. Key California Additions**

-   **Extended Voltage Ranges**:\
    CEC tables cover **2001–35,000V** with temperature ratings up to
    **105°C** (MV-105), while NEC stops at **2000V** (NEC 310.15,
    315.60).

-   **Installation-Specific Adjustments**:\
    CEC includes derating factors for:

    -   Covered cable trays (392.80(B))
    -   Ambient temperatures ≠ 40°C (311.60(D)(4))
    -   Underground installations (311.60(F))

-   **Unique Configurations**:\
    Tables for **triplexed cables in isolated conduit** (e.g., Table
    311.60(C)(67)) and **single-conductor cables in ventilated trays**
    are absent in NEC.

------------------------------------------------------------------------

#### **3. NEC Gaps**

-   **No Equivalent MV Tables**:\
    NEC 2023 lacks tables for medium voltage cables beyond **Table
    315.60(C)** (2001–35,000V), which provides limited scenarios and
    requires engineering calculations for most MV applications.

-   \*\*Les...

**Tool Usage:** - CEC Tools: cec_search, cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 4 found

**Response Time:** 15.4s

------------------------------------------------------------------------

## CEC Delta Tables

### cec-011: conductor_ampacity [CA-SPECIFIC]

**Question:** What is the ampacity of 4/0 AWG copper conductor at 75C
according to California electrical code?

**Expected:** 230 amperes per CEC 2022 Table 310.16 [California
Amendment]

**Status:** PASS

**Agent Answer:** \## Ampacity of 4/0 AWG Copper Conductor at 75°C (CEC
2022)

**California Electrical Code (CEC 2022):** - **Ampacity:** 230 amperes
(per CEC Table 310.16) - **Conditions:** - Ambient temperature: 30°C
(86°F) - Not more than three current-carrying conductors in
raceway/cable/earth - See §310.15(B) for temperature correction factors
and §310.15(C)(1) for bundling adjustments

**NEC 2023 Comparison:** - **NEC Ampacity:** 230 amperes (per NEC Table
310.16) - **Same value** as CEC for this specific conductor/temperature
combination - No California amendment affects this value in the
structured table data

**Key Notes:** 1. Both codes use identical ampacity values for 4/0 AWG
copper at 75°C 2. California amendment markers ([CEC]) in the table
reference additional rules but don't modify this specific value 3. The
semantic search confirms no exceptions or amendments to this value in
CEC 2022

[OK] Source: CEC 2022 / NEC 2023 Table 310.16

**Tool Usage:** - CEC Tools: cec_lookup_conductor_ampacity - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 2 found

**Response Time:** 5.8s

------------------------------------------------------------------------

### cec-012: grounding [CA-SPECIFIC]

**Question:** What size equipment grounding conductor is required for a
200A circuit in California?

**Expected:** 6 AWG copper or 4 AWG aluminum per CEC 2022 Table 250.122
[California Amendment]

**Status:** PASS

**Agent Answer:** \## Equipment Grounding Conductor Size for 200A
Circuit (CEC 2022)

**California (CEC) Requirement:**\
- **Copper:** 6 AWG\
- **Aluminum:** 4 AWG\
- **Reference:** CEC Table 250.122 (with California amendment marked
[∆])

**NEC 2023 Comparison:**\
- **Copper:** 6 AWG\
- **Aluminum:** 4 AWG\
- **Reference:** NEC Table 250.122

### Key Differences/Amendments in CEC:

1.  **California-Specific Applications:**
    -   Section 692.45 mandates EGC sizing per Table 250.122 for
        specific equipment (e.g., solar systems).\
    -   Section 400.31(B) requires EGCs in flexible cables to meet Table
        250.122.\
    -   Section 647.6 adds grounding requirements for technical
        equipment, referencing Table 250.122.
2.  **Exceptions in CEC:**
    -   **Exception 1 (CEC 410.44):** Allows GFCI-protected luminaires
        without EGC if no exposed conductive parts.\
    -   **Exception 2 (CEC 250.134):** Permits separately run EGCs for
        DC circuits or fixed equipment.

**Conclusion:**\
Both CEC and NEC require **6 AWG copper** or **4 AWG aluminum** for 200A
circuits. California retains the same sizing table as NEC but applies it
in additional contexts (e.g., solar, technical equipment) and includes
exceptions for specific installations.

[OK] Source: CEC 2022, NEC 2023

**Tool Usage:** - CEC Tools: cec_lookup_grounding_conductor,
cec_exception_search - NEC Tools: compare_with_nec - Exception Search
Called: Yes

**Citations:** 6 found

**Response Time:** 5.6s

------------------------------------------------------------------------

### cec-013: grounding [CA-SPECIFIC]

**Question:** What size grounding electrode conductor is required for a
3/0 AWG copper service conductor in California?

**Expected:** 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table
250.66 [California Amendment]

**Status:** PASS

**Agent Answer:** \## Grounding Electrode Conductor (GEC) Size for 3/0
AWG Copper Service Conductor

### **California (CEC 2022) vs. NEC 2023 Comparison**

| **Requirement**             | **CEC 2022**                                                                                                                     | **NEC 2023**                                                                            | **Difference**                                                                                           |
|---------------|---------------|---------------|----------------------------|
| **GEC Size (Copper)**       | **4 AWG** (Table 250.66)                                                                                                         | **4 AWG** (Table 250.66)                                                                | **Same** for 3/0 AWG service conductor.                                                                  |
| **California Amendment**    | [Delta] Applies                                                                                                                  | No amendment                                                                            | California enforces Table 250.66 as-is; no material difference in this case.                             |
| **Additional CEC Mandates** | \- Must connect to grounding electrode system per **CEC 250.186**<br>- Panelboard requirements per **CEC 408.2** (if applicable) | \- General grounding rules in **NEC 250.186**<br>- No specific electrification mandates | California may require additional grounding electrode types (e.g., concrete-encased) per **CEC 250.50**. |

------------------------------------------------------------------------

### **Key Takeaways**

1.  **Sizing Alignment**: Both CEC and NEC require a **4 AWG copper
    GEC** for a 3/0 AWG copper service conductor.\
2.  **California-Specific Rules**:
    -   **CEC 250.186** mandates the grounded conductor size must match
        the GE...

**Tool Usage:** - CEC Tools: cec_lookup_grounding_conductor - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 4 found

**Response Time:** 9.9s

------------------------------------------------------------------------

### cec-014: ampacity_adjustment [CA-SPECIFIC]

**Question:** What is the temperature correction factor for a 75C rated
conductor at 40C ambient temperature according to California code?

**Expected:** 0.88 per CEC 2022 Table 310.15(B)(1)(1) [California
Amendment]

**Status:** PASS

**Agent Answer:** \## Temperature Correction Factor (CEC 2022)

**CEC 2022 Correction Factor:**\
For a 75°C rated conductor at 40°C ambient temperature, the temperature
correction factor is **0.88** per CEC Table 310.15(B)(1)(1).

**NEC 2023 Comparison:**\
NEC 2023 uses the same correction factor of **0.88** for 75°C conductors
at 40°C ambient (NEC Table 310.15(B)(1)). No differences exist between
CEC 2022 and NEC 2023 for this specific correction factor.

[OK] Source: CEC 2022, NEC 2023

**Tool Usage:** - CEC Tools: cec_lookup_ampacity_adjustment - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 1 found

**Response Time:** 4.5s

------------------------------------------------------------------------

### cec-015: ampacity_adjustment [CA-SPECIFIC]

**Question:** What is the ampacity adjustment factor for 7-9
current-carrying conductors in a raceway according to California code?

**Expected:** 70% (0.70) per CEC 2022 Table 310.15(C)(1) [California
Amendment]

**Status:** PASS

**Agent Answer:** \## Ampacity Adjustment Factor for 7-9 Conductors (CEC
2022)

**California Code (CEC 2022):** - **Adjustment Factor:** 70% (0.7) for
7-9 current-carrying conductors in a raceway\
- **Source:** Table 310.15(C)(1)\
- **Footnote:** Applies to all conductors in the raceway, including
spares and neutrals, unless they cannot be simultaneously energized.

**NEC 2023 Comparison:** - **Adjustment Factor:** 70% (0.7) for 7-9
conductors\
- **Source:** Table 310.15(C)(1)\
- **No material difference** between CEC 2022 and NEC 2023 for this
specific adjustment factor.

[OK] Source: CEC 2022 / NEC 2023

**Tool Usage:** - CEC Tools: cec_lookup_ampacity_adjustment - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 1 found

**Response Time:** 4.4s

------------------------------------------------------------------------

### cec-016: working_space [CA-SPECIFIC]

**Question:** What is the minimum working space depth for a 480V
panelboard under Condition 3 according to California code?

**Expected:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**Status:** PASS

**Agent Answer:** \## Minimum Working Space Depth for 480V Panelboard
(CEC 2022)

**California Code (CEC 2022):**\
- **Condition 3 Requirement**: 1.2 meters (4 feet)\
- **Citation**: CEC Table 110.26(A)(1) for 151–600V systems with exposed
live parts on both sides.

**NEC 2023 Comparison:**\
- **NEC Requirement**: 1.07 meters (3.5 feet)\
- **Citation**: NEC Table 110.26(A)(1) for 151–600V systems under
Condition 3.

**Key Difference**:\
California’s CEC mandates **4 feet** (more restrictive) compared to
NEC’s **3.5 feet** for the same voltage and condition. This reflects
California’s stricter safety requirements for working space around
electrical equipment.

[OK] Source: CEC 2022, NEC 2023

**Tool Usage:** - CEC Tools: cec_lookup_working_space - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 1 found

**Response Time:** 7.3s

------------------------------------------------------------------------

### cec-017: enclosure [CA-SPECIFIC]

**Question:** What type of enclosure is suitable for outdoor use with
rain, sleet, and ice according to California code Table 110.28?

**Expected:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures are suitable
for outdoor use with rain, sleet, and ice per CEC 2022 Table 110.28
[California Amendment]

**Status:** PASS

**Agent Answer:** \## Suitable Enclosures for Outdoor Use (CEC 2022 vs
NEC 2023)

### **CEC 2022 Requirements**

For outdoor use with **rain, sleet, and ice**, Table 110.28 specifies
the following enclosure types:\
- **Type 3S**: Raintight, sleet-resistant, and ice-covered operability.\
- **Type 3SX**: Same as 3S with corrosion protection.\
- **Type 4**: Watertight (resists rain, sleet, and hose-directed
water).\
- **Type 4X**: Watertight with corrosion protection.\
- **Type 6P**: Additional protection against water ingress (e.g., hose
streams).

**Key CEC-Specific Notes**:\
- Mechanisms must remain operable when ice-covered (footnote [\*]).\
- "Watertight" enclosures (Types 4, 4X, 6P) are explicitly required for
sleet/ice conditions.

------------------------------------------------------------------------

### **NEC 2023 Comparison**

NEC Table 110.28 includes **identical enclosure types** (3S, 4, 4X,
etc.) for outdoor use. However, **CEC adds explicit requirements** for
ice-covered operability and emphasizes corrosion protection (Types
3SX/4X) in its footnotes.

**Key Differences**:\
1. **Ice Coverage**: CEC explicitly requires mechanisms to operate when
ice-covered (footnote [\*]), while NEC does not explicitly mention
this.\
2. **Corrosion Protection**: CEC emphasizes corrosion-resistant options
(Types 3SX/4X) for outdoor environments, aligning with California’s
coastal/industrial conditions.\
3. **Terminology**: Both codes use "raintight" and "watertight," but CEC
clarifies that "watertight" enclosures (Types 4, 4X, 6P) are preferred
for sl...

**Tool Usage:** - CEC Tools: cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 1 found

**Response Time:** 10.0s

------------------------------------------------------------------------

### cec-018: lighting_load [CA-SPECIFIC]

**Question:** What is the general lighting load in VA per square foot
for office buildings according to California code?

**Expected:** 1.3 VA per square foot per CEC 2022 Table 220.12 (updated
from 3.5 VA in NEC 2020)

**Status:** PASS

**Agent Answer:** \## General Lighting Load for Office Buildings (CEC
2022 vs NEC 2023)

**California Code (CEC 2022):**\
Per **Table 220.12**, the general lighting load for **office**
occupancies is **1.3 VA/ft² (14 VA/m²)**. This value includes the **125%
continuous load multiplier** required by CEC 210.20(A).

**NEC 2023 Comparison:**\
NEC 2023 Table 220.42(A) specifies **1.0 VA/ft² (10.8 VA/m²)** for
office occupancies. Notably: - NEC does **not include** the 125%
continuous load multiplier in its base value. - California's value is
**30% higher** than NEC's base requirement.

### Key Code Differences:

1.  **Load Multiplier Inclusion**
    -   CEC 220.12 explicitly includes the 125% multiplier for
        continuous loads in its table values.\
    -   NEC 220.42 requires the 125% multiplier to be applied separately
        (per 210.19(A)(1)).
2.  **Occupancy Classification**
    -   CEC 220.12 footnote [d] explicitly classifies **banks as
        office-type occupancies**.\
    -   NEC 220.42(A) does not include this specific classification.
3.  **Demand Factors**
    -   Both codes reference demand factors (CEC 220.42, NEC 220.44),
        but California's amendments may affect application in specific
        scenarios.

### Calculation Example:

For a **10,000 sq ft office**: - **CEC 2022**:\
\$ 10,000 , \text{ft²} \times 1.3 , \text{VA/ft²} = 13,000 , \text{VA}
\$ - **NEC 2023**:\
\$ 10,000 , \text{ft²} \times 1.0 , \text{VA/ft²} = 10,000 , \text{VA}
\$\
(Additional 25% for continuous load: \$ 10,000 \times 1.25 = 12,500 ,...

**Tool Usage:** - CEC Tools: cec_search, cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 5 found

**Response Time:** 13.8s

------------------------------------------------------------------------

### cec-019: flexible_cord [CA-SPECIFIC]

**Question:** What is the ampacity of a 12 AWG flexible cord (Column B
thermoset) according to California code?

**Expected:** 25 amperes per CEC 2022 Table 400.5(A)(1). Note: This is
the same value as NEC 2023 - there is no California amendment for this
table. Column B represents 2 current-carrying conductors.

**Status:** PASS

**Agent Answer:** \## Corrected Answer: Ampacity of 12 AWG Flexible Cord
(Column B Thermoset)

**California Code (CEC 2022):**\
Per **Table 400.5(A)(1)**, the ampacity of 12 AWG flexible cord in
**Column B (thermoset)** is **25 amperes**. This applies to flexible
cords with not more than three current-carrying conductors at 30°C
ambient temperature.

**NEC 2023 Comparison:**\
NEC Table 400.5(A)(1) specifies the **same value of 25 amperes** for 12
AWG flexible cord in Column B (thermoset) under identical conditions.

**Key Notes:**\
- **No California amendments** apply to this specific table value.\
- Both codes require temperature correction (Table 310.15(B)(1)) and
bundling adjustments (Table 400.5(A)(3)) if ambient conditions or
conductor counts change.

[OK] Source: CEC 2022 Table 400.5(A)(1) and NEC 2023 Table 400.5(A)(1)

**Tool Usage:** - CEC Tools: cec_lookup_conductor_ampacity, cec_search -
NEC Tools: compare_with_nec - Exception Search Called: No

**Citations:** 2 found

**Response Time:** 13.7s

------------------------------------------------------------------------

### cec-020: fixture_wire [CA-SPECIFIC]

**Question:** What is the maximum operating temperature for Type SF-2
silicone insulated fixture wire according to California code?

**Expected:** 200C (392F) per CEC 2022 Table 402.3 [California
Amendment]

**Status:** PASS

**Agent Answer:** \## Maximum Operating Temperature for Type SF-2
Silicone Insulated Fixture Wire

### California Electrical Code (CEC 2022)

-   **Maximum Operating Temperature**: **200°C (392°F)**\
    (Specified in CEC Table 402.3 for Type SF-2 silicone
    rubber-insulated fixture wire)
-   **Additional Requirements**:
    -   Must comply with flame-retardant and limited-smoke markings if
        applicable [CEC Table 402.3 Note].
    -   Section 330.112(A) requires 18/16 AWG fixture wires to have a
        minimum operating temperature rating of 90°C (194°F), but Type
        SF-2 exceeds this with 200°C.

### National Electrical Code (NEC 2023)

-   **Maximum Operating Temperature**: **200°C (392°F)**\
    (Identical to CEC in NEC Table 402.3 for Type SF-2).
-   **No Additional Requirements**: NEC does not include California's
    flame-retardant or marking provisions beyond the temperature rating.

### Key Differences

-   **California-Specific Mandates**:
    -   Flame-retardant insulation requirements for certain applications
        [CEC 410.52].
    -   Marking requirements for thermoplastic and other fixture wires
        [CEC 402.9].

[OK] Source: CEC 2022, NEC 2023

**Tool Usage:** - CEC Tools: cec_search, cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 4 found

**Response Time:** 9.7s

------------------------------------------------------------------------

## Complex Calculations

### cec-021: adjusted_ampacity [CA-SPECIFIC]

**Question:** Calculate the adjusted ampacity for 8 AWG THWN copper
conductors with 7 conductors in a raceway at 40C ambient temperature in
California.

**Expected:** Base ampacity: 50A (CEC Table 310.16, 75C). Temperature
correction: 0.88 (CEC Table 310.15(B)(1)(1) for 40C). Bundling factor:
0.70 (CEC Table 310.15(C)(1) for 7-9 conductors). Adjusted ampacity = 50
x 0.88 x 0.70 = 30.8A

**Status:** PASS

**Agent Answer:** \## Adjusted Ampacity Calculation (CEC 2022)

**Base Ampacity**:\
8 AWG THWN copper at 75°C = **50A** (CEC Table 310.16)

**Temperature Correction (40°C ambient)**:\
Factor = **0.88** (CEC Table 310.15(B)(1)(1))\
Adjusted: 50A × 0.88 = **44A**

**Bundling Adjustment (7 conductors)**:\
Factor = **0.70** (CEC Table 310.15(C)(1))\
Final Adjusted Ampacity: 44A × 0.70 = **30.8A**

------------------------------------------------------------------------

### NEC 2023 Comparison

-   **Base Table 310.16 values are identical** to CEC 2022 for 8 AWG
    THWN copper (50A at 75°C).\
-   **Temperature correction factor** (0.88 for 40°C) and **bundling
    adjustment** (0.70 for 7 conductors) match NEC 2023 calculations.\
-   **No California amendments** affect this specific calculation in the
    provided comparison.

------------------------------------------------------------------------

**Final Answer**:\
**30.8A** adjusted ampacity for 8 AWG THWN copper conductors under these
conditions.

[OK] Source: CEC 2022 & NEC 2023 comparison

**Tool Usage:** - CEC Tools: cec_lookup_conductor_ampacity,
cec_lookup_ampacity_adjustment, cec_lookup_ampacity_adjustment,
python_calculator - NEC Tools: compare_with_nec - Exception Search
Called: No

**Citations:** 2 found

**Response Time:** 9.8s

------------------------------------------------------------------------

### cec-022: service_sizing [CA-SPECIFIC]

**Question:** Size the conductors, EGC, and GEC for a 200A residential
service in California using copper conductors.

**Expected:** Service conductors: 3/0 AWG copper minimum (200A at 75C
per CEC Table 310.16). Equipment grounding conductor: 6 AWG copper (per
CEC Table 250.122 for 200A). Grounding electrode conductor: 4 AWG
copper...

**Status:** PASS

**Agent Answer:** \## Service Sizing (CEC 2022)\
[OK] **Service Conductor**: **2/0 AWG copper** (CEC Table 310.12(A) for
200A dwelling service)\
[OK] **EGC (Equipment Grounding Conductor)**: **6 AWG copper** (CEC
Table 250.122 for 200A overcurrent device)\
[OK] **GEC (Grounding Electrode Conductor)**: **4 AWG copper** (CEC
Table 250.66 for 2/0 AWG service conductor)

------------------------------------------------------------------------

### NEC 2023 Comparison

1.  **Service Conductor**
    -   **CEC**: 2/0 AWG copper (Table 310.12(A))\
    -   **NEC**: 2/0 AWG copper (Table 310.12)\
    -   **Difference**: Identical sizing. California retains NEC Table
        310.12 but adds [delta] amendments for dwelling service
        applications.
2.  **EGC**
    -   **CEC**: 6 AWG copper (Table 250.122)\
    -   **NEC**: 6 AWG copper (Table 250.122)\
    -   **Difference**: No change. California does not modify EGC sizing
        for 200A systems.
3.  **GEC**
    -   **CEC**: 4 AWG copper (Table 250.66)\
    -   **NEC**: 4 AWG copper (Table 250.66)\
    -   **Difference**: No change. California aligns with NEC for GEC
        sizing based on 2/0 AWG service conductors.

------------------------------------------------------------------------

### California Amendments

-   **Table 310.12(A)**: [delta] Marks California-specific application
    for dwelling services (e.g., temperature correction assumptions).\
-   **Tables 250.122/250.66**: No additional restrictions beyond NEC for
    this 200A system.

[OK] Source: CEC 2022 with NEC 2023 comparison.

**Tool Usage:** - CEC Tools: cec_lookup_conductor_size,
cec_lookup_grounding_conductor, cec_lookup_grounding_conductor - NEC
Tools: compare_with_nec - Exception Search Called: No

**Citations:** 3 found

**Response Time:** 30.8s

------------------------------------------------------------------------

### cec-023: commercial_load [CA-SPECIFIC]

**Question:** Calculate the general lighting load for a 5,000 square
foot office building in California.

**Expected:** Per CEC Table 220.12, office buildings require 1.3 VA per
square foot (updated from 3.5 VA in NEC 2017 and earlier). General
lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA (6.5 kVA). Note:
The ...

**Status:** PASS

**Agent Answer:** \## General Lighting Load Calculation (CEC 2022 vs NEC
2023)

### **California Electrical Code (CEC 2022)**

-   **Unit Load for Office:** 1.3 VA/ft² (Table 220.12)\
-   **Building Area:** 5,000 sq ft\
-   **Total General Lighting Load:**\
    \$ 5,000 , \text{ft}\^2 \times 1.3 , \text{VA/ft}\^2 = 6,500 ,
    \text{VA} \$\
-   **Note:** The 125% continuous load multiplier (210.20(A)) is
    **already included** in the CEC Table 220.12 value.

------------------------------------------------------------------------

### **NEC 2023 Comparison**

-   **NEC Table 220.42(A):**
    -   **Office Unit Load:** 1.3 VA/ft² (same as CEC)\
-   **Calculation:**\
    \$ 5,000 , \text{ft}\^2 \times 1.3 , \text{VA/ft}\^2 = 6,500 ,
    \text{VA} \$\
-   **Key Difference:**
    -   CEC explicitly includes the 125% continuous load multiplier in
        Table 220.12 values.\
    -   NEC requires applying the 125% multiplier separately (per
        210.20(A)) if the lighting load is continuous.

------------------------------------------------------------------------

### **Final Answer**

-   **California (CEC 2022):** 6,500 VA (1.3 VA/ft² × 5,000 ft², with
    125% multiplier included).\
-   **NEC 2023:** 6,500 VA (same unit load, but 125% multiplier must be
    applied manually for continuous loads).

[OK] Source: CEC 2022 Table 220.12, NEC 2023 Table 220.42(A)

**Tool Usage:** - CEC Tools: cec_search, cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 3 found

**Response Time:** 16.0s

------------------------------------------------------------------------

### cec-024: motor_circuit [CA-SPECIFIC]

**Question:** What is the maximum overcurrent protection for a motor
control circuit using 16 AWG copper conductors that extend beyond the
enclosure in California?

**Expected:** Per CEC Table 430.72(B), Column C for conductors extending
beyond enclosure, 16 AWG copper has a maximum OCP rating of 10 amperes.

**Status:** PASS

**Agent Answer:** \## Maximum Overcurrent Protection for 16 AWG Motor
Control Circuit (CEC 2022 vs NEC 2023)

**CEC 2022 Answer:** - **Maximum overcurrent protection**: **10
amperes** for 16 AWG copper conductors extending beyond the enclosure. -
**Source**: CEC Table 430.72(B), Column C (conductors extending beyond
enclosure).

**NEC 2023 Comparison:** - **NEC Table 430.72(B)(2)** specifies **10A**
for 16 AWG copper conductors in Column C. - **No California amendments**
apply in this case - CEC aligns with NEC.

**Key Differences/Notes:** 1. **Column C applicability**: Both codes
require Column C protection (10A) when conductors extend beyond the
enclosure. 2. **Aluminum conductors**: Both tables show "—" for aluminum
in Columns A-C for 16 AWG (not permitted for motor control circuits). 3.
**Exception for non-extended conductors**: If conductors do **not**
extend beyond the enclosure, Column B allows 40A for 16 AWG copper (same
in both codes).

**Code Alignment**: California's CEC 2022 maintains identical
requirements to NEC 2023 for this application. No additional
restrictions or amendments are present in the CEC for motor control
circuit overcurrent protection in this scenario.

[OK] Source: CEC 2022 Table 430.72(B) and NEC 2023 Table 430.72(B)(2)

**Tool Usage:** - CEC Tools: cec_search, cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 1 found

**Response Time:** 19.3s

------------------------------------------------------------------------

### cec-025: dwelling_load [CA-SPECIFIC]

**Question:** Calculate the general lighting load for a 2,400 square
foot dwelling unit in California.

**Expected:** Per CEC Table 220.12, dwelling units require 3 VA per
square foot. General lighting load = 2,400 sq ft x 3 VA/sq ft = 7,200 VA
(7.2 kVA).

**Status:** PASS

**Agent Answer:** \## General Lighting Load for Dwelling Unit (CEC 2022
vs NEC 2023)

**California Electrical Code (CEC 2022):** - **Table 220.12** explicitly
lists **non-dwelling occupancies** (e.g., automotive, office, retail)
but **omits dwelling units**. - **No specific value** for dwelling units
in CEC Table 220.12. - **Implied Requirement:** California follows NEC
220.41 for dwelling units unless amended (see CEC 220.16 for additions).

**National Electrical Code (NEC 2023):** - **Table 220.42(A)**
(non-dwelling) mirrors CEC Table 220.12. - **Dwelling units** are
addressed in **NEC 220.41**:\
$$
  3 \, \text{VA/ft}^2 \times 2,400 \, \text{ft}^2 = 7,200 \, \text{VA}
  $$

**Key Differences:** 1. **Dwelling Unit Specification:**\
- NEC explicitly defines 3 VA/ft² for dwelling units (220.41).\
- CEC Table 220.12 excludes dwelling units, requiring reference to NEC
220.41 or CEC 220.16 for additions.

2.  **California Amendments:**
    -   No amendments to NEC 220.41 for dwelling lighting loads in CEC
        2022.\
    -   CEC 220.16 governs additions to existing dwellings but does not
        override the 3 VA/ft² baseline.

**Final Calculation:**\
$$
2,400 \, \text{ft}^2 \times 3 \, \text{VA/ft}^2 = \boxed{7,200 \, \text{VA}}
$$

[OK] Source: CEC 2022 Table 220.12, NEC 2023 220.41

**Tool Usage:** - CEC Tools: cec_lookup_table - NEC Tools:
compare_with_nec - Exception Search Called: No

**Citations:** 4 found

**Response Time:** 14.3s

------------------------------------------------------------------------

## CEC vs NEC Comparison

### cec-026: gfci [CA-SPECIFIC]

**Question:** Compare the kitchen GFCI requirements between CEC 2022 and
NEC 2023. Which code is more restrictive?

**Expected:** CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen
GFCI. CEC limits GFCI requirements to receptacles serving countertop
surfaces and within 6 feet of the sink. NEC 2023 requires GFCI
protection for...

**Status:** PASS

**Agent Answer:** \## Kitchen GFCI Requirements Comparison (CEC 2022 vs
NEC 2023)

### **1. Base Requirements**

-   **CEC 2022 (Section 210.8(A)(6))**:\
    Requires GFCI protection for **all receptacles serving countertop
    surfaces** in kitchens.
    -   Extends to **fixed panels in walls** and **freestanding bar-type
        counters** (per 210.52(A)(2)).\
    -   No exceptions for refrigeration equipment (unlike NEC).
-   **NEC 2023 (Section 210.8(A)(6))**:\
    Requires GFCI protection for **receptacles serving countertop
    surfaces**.
    -   **Exception**: Receptacles supplying **refrigeration equipment**
        are exempt (NEC 210.8(A)(6) Exception).

------------------------------------------------------------------------

### **2. Scope of Coverage**

-   **CEC 2022**:
    -   Covers **all wall spaces ≥ 2 ft wide** in kitchens
        (210.52(A)(2)).\
    -   Includes **floor receptacles within 18 in of walls**
        (210.52(A)(3)).\
    -   Applies to **additional appliances** (Section 422.5):
        -   Dishwashers, sump pumps, vending machines, and
            cord-and-plug-connected high-pressure washers.
-   **NEC 2023**:
    -   Limits countertop GFCI to **receptacles within 6 ft of sink
        edges** (210.8(A)(7)).\
    -   Excludes refrigeration equipment from GFCI requirements
        (210.8(A)(6) Exception).\
    -   Fewer appliance-specific GFCI mandates (Section 422.5 covers
        fewer kitchen appliances).

------------------------------------------------------------------------

### **3. Placement Rules**

-   **CEC 2022**:
    -   **6 ft spacing rule**: No point on kitchen walls can be \>6 ft
        from a receptacle (210.52(A)(1)).\
    -   **Freestanding counters** (e.g., islands) must have
        GFCI-protected rec...

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 6 found

**Response Time:** 17.7s

------------------------------------------------------------------------

### cec-027: panelboard [CA-SPECIFIC]

**Question:** Compare the panelboard space requirements between CEC 2022
and NEC 2023 for single-family dwellings.

**Expected:** CEC 2022 Section 408.2(A) requires reserved panelboard
spaces for: (1) heat pump water heaters, (2) heat pump space heaters,
(3) electric cooktops, and (4) electric clothes dryers. NEC 2023 has NO
suc...

**Status:** PASS

**Agent Answer:** \## Panelboard Space Requirements Comparison (CEC 2022
vs NEC 2023)

### **California Electrical Code (CEC 2022)**

-   **Section 408.2(A)**:\
    **Mandates reserved circuit breaker spaces** in single-family
    dwellings for:
    -   Heat pump water heaters\
    -   Heat pump space heaters\
    -   Electric cooktops\
    -   Electric clothes dryers\
        This requirement is tied to **California Energy Code Section
        150.0(n), (t), (u), and (v)**.\
    -   **Purpose**: Ensures panelboards have pre-allocated spaces for
        energy-efficient appliances, supporting electrification goals.
-   **Additional CEC Requirements**:
    -   Wire-bending space rules (Section 408.55) align with NEC but
        include California-specific exceptions for smaller panelboards
        (≤225A).

------------------------------------------------------------------------

### **National Electrical Code (NEC 2023)**

-   **No Equivalent to CEC 408.2(A)**:\
    NEC does **not specify reserved circuit breaker spaces** for
    appliances in single-family dwellings.
    -   Panelboard sizing and space requirements are based on
        **calculated load** (Article 220) and general rules (e.g.,
        408.30 for minimum rating).
-   **General Panelboard Rules**:
    -   NEC 408.55: Wire-bending space requirements match CEC but lack
        California-specific exceptions.\
    -   NEC 408.30: Panelboards must have a rating ≥ calculated feeder
        load (no appliance-specific reservations).

------------------------------------------------------------------------

### **Key Differences**

| **Aspect** \| **CEC 2022** \| **NEC 2023** ...

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 4 found

**Response Time:** 12.6s

------------------------------------------------------------------------

### cec-028: ev_charging [CA-SPECIFIC]

**Question:** Compare California's EV charging infrastructure
requirements with the NEC 2023 requirements.

**Expected:** California (CEC + Title 24) MANDATES EV charging
infrastructure in new construction, requiring dedicated circuits,
conduit, and panel capacity. NEC 2023 Article 625 only provides
installation rules fo...

**Status:** PASS

**Agent Answer:** \## California (CEC 2022) vs NEC 2023 EV Charging
Requirements

### **1. Scope and Application**

-   **CEC 625.1**:
    -   Explicitly covers **bidirectional power flow** (vehicle-to-grid)
        and power export.\
    -   Mandates compliance with **CALGreen** for new construction
        (EV-ready infrastructure).\
    -   References **UL 2594** and **UL 2202** for EVSE safety
        standards.
-   **NEC 625.1**:
    -   Focuses on **unidirectional charging** (grid-to-vehicle).\
    -   No specific integration with state green building codes.\
    -   References **UL 2202** for EVSE but lacks bidirectional system
        requirements.

------------------------------------------------------------------------

### **2. Branch Circuit Requirements**

-   **CEC 625.40**:
    -   **Mandatory individual branch circuits** for EV outlets (no
        shared circuits).\
    -   No exceptions for multi-family or commercial installations.
-   **NEC 625.40**:
    -   Permits shared circuits **if equipment is listed for the
        application**.\
    -   Allows flexibility for multi-family dwellings (e.g., shared EVSE
        circuits).

------------------------------------------------------------------------

### **3. Ventilation Requirements**

-   **CEC 625.52**:
    -   **Mandatory mechanical ventilation** for indoor EV charging if
        equipment requires it.\
    -   Specifies **interlocked ventilation systems** to operate during
        charging.\
    -   Tables define minimum ventilation rates (m³/min or cfm) based on
        number of EVs.
-   **NEC**:
    -   **No specific ventilation requirements** for EV charging.\
    -   Relies on general building codes (e.g., NFPA 92 for hazardous
        locations).

------------------------------------------------------------------------

### \*\*4. Load Calculat...

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 7 found

**Response Time:** 10.1s

------------------------------------------------------------------------

### cec-029: afci [CA-SPECIFIC]

**Question:** Compare the AFCI protection requirements between CEC 2022
and NEC 2023 for dwelling units.

**Expected:** Both CEC 2022 and NEC 2023 require AFCI protection for
120V, 15/20A branch circuits in kitchens, family rooms, dining rooms,
living rooms, bedrooms, sunrooms, closets, hallways, laundry areas, and
sim...

**Status:** PASS

**Agent Answer:** \## AFCI Protection Requirements Comparison: CEC 2022
vs NEC 2023

### **1. Scope of Protection**

| **Requirement**         | **CEC 2022**                                                                                                                                                      | **NEC 2023**                                                                                                                                                                       |
|---------------------------|-----------------------|-----------------------|
| **Protected Locations** | Kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, and similar spaces in dwelling units. | Kitchens, family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, and similar spaces in dwelling units.                                                      |
| **Additional Coverage** | Explicitly includes hallways (≥3.0 m/10 ft) and laundry areas.                                                                                                    | No specific mention of hallway length or laundry area receptacles.                                                                                                                 |
| **Exceptions**          | \- Fire alarm circuits in compliance with 760.41(B)/760.121(B) are exempt.<br>- Branch circuit extensions ≤1.8 m (6 ft) without additional outlets are exempt.    | \- Fire alarm circuits are exempt.<br>- Replacement receptacles in existing installations may use listed outlet branch-circuit-type AFCI under specific conditions (404.22(C)(4)). |

------------------------------------------------------------------------

### **2. AFCI Types and Installation Methods**

| **Method**                  | **CEC 2022**                                                                   | **NEC 2023**                                                    |
|----------------------|-------------------------|-------------------------|
| **Combination-Type AFCI**   | Required for entire branch circuit.                                            | Required for entire branch circuit.                             |
| **Branch/Feeder-Type AFCI** | Permitted with outlet branch-circuit-type AFCI at first outlet (210.12(A)(2)). | Permitted with outlet branch-circuit-type AFCI at first outlet. |
| **Supplemental Protection** | Al...                                                                          |                                                                 |

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 7 found

**Response Time:** 9.2s

------------------------------------------------------------------------

### cec-030: solar_pv [CA-SPECIFIC]

**Question:** Compare California's solar PV requirements with NEC 2023
Article 690.

**Expected:** California MANDATES solar PV on new single-family homes
through Title 24 Part 6. CEC 690 follows NEC 690 for installation
requirements (rapid shutdown, arc-fault protection, grounding). The key
differ...

**Status:** PASS

**Agent Answer:** \## California (CEC 2022) vs NEC 2023 Article 690
Solar PV Requirements

### 1. **AC Module Systems**

-   **CEC 690.6**:
    -   PV source circuit requirements **do not apply** to AC modules or
        AC module systems.\
    -   AC modules are treated as **internal components** (conductors,
        inverters).\
    -   **NEC 2023**: No specific exception for AC modules; standard PV
        source circuit rules apply.

------------------------------------------------------------------------

### 2. **Rapid Shutdown Labeling**

-   **CEC 690.56(C)**:
    -   **Mandatory labels** at service equipment locations with:
        -   Minimum **9.5 mm** (3/8 in.) height for "SOLAR PV SYSTEM IS
            EQUIPPED WITH RAPID SHUTDOWN" in **black on yellow**.\
        -   **Rapid shutdown switch labels** in **white on red** with
            9.5 mm height.\
    -   Detailed diagrams required for buildings with multiple PV
        systems.\
-   **NEC 2023**:
    -   Requires rapid shutdown but **no specific label size/color**
        mandates.

------------------------------------------------------------------------

### 3. **Grounding and Bonding**

-   **CEC 690.43(B)**:
    -   Mounting systems **must be listed/identified for bonding** PV
        modules.\
    -   **Bonding jumpers** required between metallic support sections.\
-   **CEC 690.47(B)**:
    -   **Ground-mounted PV support structures** can serve as grounding
        electrodes if they meet 250.52.\
-   **NEC 2023**:
    -   Grounding requirements exist but **no explicit provisions** for
        using support structures as electrodes.

------------------------------------------------------------------------

### 4. **System Grounding Connections**

-   **CEC 690.42**:
    -   For solidly grounded systems, grounding connection allowed at
        \*\*any single point...

**Tool Usage:** - CEC Tools: cec_search - NEC Tools: compare_with_nec -
Exception Search Called: No

**Citations:** 10 found

**Response Time:** 9.3s

------------------------------------------------------------------------

## Analysis

### Key Metrics

-   **CEC-Primary Responses**: 30/30
-   **NEC Comparison Tool Used**: 30/30
-   **cec_lookup_table Used**: 10/30
-   **Exception Search Called (Voluntary)**: 3/30
-   **Success Rate**: 100.0%
-   **Average Response Time**: 11.3s

### Hardcoded Value Removal Analysis

With hardcoded values removed from the prompt, the model should: -
Always call tools to get specific values (no relying on memorized
content) - Produce more accurate answers (values come from authoritative
source) - Be less prone to hallucination (no conflicting info between
prompt and tools)
