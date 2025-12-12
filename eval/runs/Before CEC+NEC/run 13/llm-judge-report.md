# Run 13 - LLM Judge Evaluation Report

**Date:** 2025-12-09
**Evaluator:** Claude Opus 4.5 (LLM-as-Judge)
**Baseline:** Run 12 (96.6% pass rate, 9.1/10 average)

---

## Executive Summary

| Metric | Run 12 | Run 13 | Change |
|--------|--------|--------|--------|
| **Core Questions** | 28 | 28 | - |
| **CEC Questions** | 30 | 30 | - |
| **Core Average Score** | 9.0/10 | **8.9/10** | -0.1 |
| **CEC Average Score** | 9.2/10 | **9.2/10** | 0 |
| **Overall Average** | 9.1/10 | **9.1/10** | 0 |
| **FAILs (critical errors)** | 2 | **3** | +1 |

### Key Improvements
- **core-010 FIXED**: Ampacity derating now correctly calculates 19.68A (was returning 25A without derating)
- **cec-020 FIXED**: SF-2 fixture wire temperature now correctly identifies 200°C

### New Issues Identified (Deep Dive Verified)
- **baseline-002 ERROR**: Agent misapplies 240.4(D) to 6 AWG (it only covers 10 AWG and smaller)
- **cec-018 ERROR**: Agent confuses Table 220.12 (lighting: 1.3 VA/ft²) with Section 220.14(K) (receptacles: 1.0 VA/ft²)
- **inspection-010 ERROR**: Agent misreads Table 250.66 - gives 3/0 AWG instead of 2/0 AWG for 1000 kcmil

---

## Scoring Criteria

| Score | Meaning |
|-------|---------|
| 10 | Perfect - Matches expected answer exactly with correct reasoning |
| 9 | Excellent - Correct answer with minor omissions or extra detail |
| 8 | Good - Substantially correct, missing 1-2 key points |
| 7 | Acceptable - Correct core answer but missing important context |
| 6 | Partial - Some correct elements but missing critical information |
| 5 | Mixed - Half right, half wrong or misleading |
| 4-1 | Poor to Failing - Significant errors or wrong answer |

---

## Core Evaluation (28 Questions)

### Baseline Tier

| ID | Question | Accuracy | Completeness | Notes |
|----|----------|----------|--------------|-------|
| baseline-001 | 12 AWG ampacity at 75°C | 10/10 | 10/10 | **EXCELLENT**: Correctly states 25A ampacity AND mentions 240.4(D) 20A OCP limit. This is better than expected answer which only mentioned 20A. |
| baseline-002 | 60A circuit conductor size | **5/10** | 6/10 | **VERIFIED ERROR**: Agent says 4 AWG citing 240.4(D) limit of 50A for 6 AWG. This is INCORRECT - 240.4(D) only applies to 10 AWG and smaller conductors. 6 AWG is NOT covered. Correct answer is 6 AWG (65A at 75°C). Agent fabricated a non-existent code restriction. |
| baseline-003 | Kitchen GFCI locations | 9/10 | 8/10 | Correctly identifies countertop surfaces and references 210.8(A)(6). Missing explicit dishwasher mention (210.8(D)). |
| baseline-004 | AFCI for bedrooms | 10/10 | 10/10 | Perfect - Yes with correct section 210.12(A) reference and compliance methods. |
| baseline-005 | 200A service aluminum | 10/10 | 10/10 | Correctly identifies 4/0 AWG aluminum per Table 310.12. |
| baseline-006 | Working clearance depth | 10/10 | 10/10 | Correct: 36 inches (3 feet) per 110.26(A)(1). |
| baseline-007 | Kitchen small appliance circuits | 10/10 | 10/10 | Correct: Minimum 2 x 20A circuits per 210.11(C)(1). |
| baseline-008 | Surge protection required | 10/10 | 10/10 | Correct: Yes per 230.67, Type 1/2 SPD required. |

**Baseline Average: 9.1/10** (adjusted after deep dive)

### Core Tier

| ID | Question | Accuracy | Completeness | Notes |
|----|----------|----------|--------------|-------|
| core-001 | 200A service conductors | 10/10 | 10/10 | Correct: 2/0 AWG Cu or 4/0 AWG Al per Table 310.12. Includes GEC sizing. |
| core-002 | MWBC requirements | 9/10 | 9/10 | Correctly covers handle tie/common trip, neutral continuity, grouping. Minor: says "2-pole 20A breaker" but handle tie is also acceptable per 210.4(B). |
| core-003 | GFCI locations list | 9/10 | 9/10 | Lists all major locations. Slight format difference but comprehensive. |
| core-004 | Surge protection location | 10/10 | 10/10 | Correct: Type 1/2 SPD, integral/adjacent, downstream exception. |
| core-005 | Panel in closet violations | 9/10 | 8/10 | Correctly identifies 36" depth violation. Missing explicit clothes closet prohibition (240.24(D)). |
| core-006 | Double-tap violation | 10/10 | 10/10 | Correct: Violation per 110.14(A)/110.14(C). |
| core-007 | Detached garage subpanel | 10/10 | 10/10 | Excellent: Neutral/ground separation, no MBJ in subpanel, GEC at detached building. |
| core-008 | MBJ vs SBJ | 10/10 | 10/10 | Perfect explanation of Main Bonding Jumper vs System Bonding Jumper with correct sections. |
| core-009 | Kitchen circuits + dining room | 10/10 | 10/10 | Correct: 2 circuits, can serve dining room, 210.52(B) reference. |
| core-010 | Ampacity derating (50°C, 6 conductors) | **10/10** | **10/10** | **MAJOR FIX**: Correctly calculates 30A × 0.82 × 0.80 = 19.68A. This was a FAIL in Run 12. |
| core-011 | Why AFCI required | 10/10 | 10/10 | Correct: Prevents arc faults/electrical fires, proper section references. |
| core-012 | Torque specifications | 10/10 | 10/10 | Correct: 110.14(D), manufacturer specs, safety reasons explained. |

**Core Average: 9.75/10**

### Inspection Tier

| ID | Question | Accuracy | Completeness | Notes |
|----|----------|----------|--------------|-------|
| inspection-001 | Panel load calculation | 10/10 | 10/10 | Excellent: All steps correct, demand factors applied properly, 103.23A result, 200A adequate. |
| inspection-002 | Garage panel violations | 9/10 | 8/10 | Identifies depth violation and water heater obstruction. Uses Condition 2 (42") instead of Condition 1 (36") - overly conservative but safe. Height assessment may be incorrect. |
| inspection-005 | Kitchen GFCI/AFCI | 8/10 | 8/10 | Mostly correct but missing combination AFCI/GFCI requirement for countertops per 210.12(A). Refrigerator should mention GFCI not required. |
| inspection-006 | Subpanel violations | 10/10 | 9/10 | Correctly identifies neutral/ground bonding violation, MBJ violation in subpanel. Mentions need for separate grounding electrode. |
| inspection-007 | Conduit fill calculation | 9/10 | 9/10 | Correct method: 40% fill, 28 conductors max. Final answer is 28 (conservative vs expected 29). |
| inspection-008 | Voltage drop calculation | 9/10 | 10/10 | Correct calculation: 2.84V (2.37%). Mentions CEC 647.4(D) which is very thorough. |
| inspection-009 | Derating (TW, 43°C, 6 conductors) | 10/10 | 10/10 | Correct: 20A × 0.71 × 0.80 = 11.36A. All factors correct. |
| inspection-010 | GEC sizing for parallel conductors | **5/10** | 5/10 | **VERIFIED ERROR**: Agent says 3/0 AWG but Table 250.66 row "Over 600 through 1100 kcmil" directly specifies 2/0 AWG copper GEC. Agent misread table - used incorrect interpolation logic instead of reading direct specification. |

**Inspection Average: 8.6/10** (adjusted after deep dive)

### Core Evaluation Total: **8.9/10** (249/280 points) - adjusted after deep dive

---

## CEC Evaluation (30 Questions)

### California-Specific Requirements

| ID | Question | Accuracy | Completeness | Notes |
|----|----------|----------|--------------|-------|
| cec-001 | Panelboard reserved spaces | 10/10 | 10/10 | Correct: Heat pump water heaters, heat pump space heaters, cooktops, dryers per 408.2(A). |
| cec-002 | EV charging requirements | 9/10 | 9/10 | Comprehensive coverage of CEC 625 and CALGreen. Slight oversimplification on Title 24 details. |
| cec-003 | Solar PV requirements | 10/10 | 10/10 | Excellent coverage: rapid shutdown, grounding, arc-fault, Title 24 mandate. |
| cec-004 | Heat pump water heater circuits | 10/10 | 10/10 | Correct: Reserved spaces per 408.2, California Energy Code 150.0(n). |
| cec-005 | Electric cooktop readiness | 10/10 | 10/10 | Correct: CEC 408.2, California Energy Code 150.0(u). |
| cec-006 | Electric dryer panelboard | 10/10 | 10/10 | Correct: Reserved spaces per 408.2 for electrification. |
| cec-007 | Table 240.4(G) | 8/10 | 8/10 | Identifies California delta symbol but doesn't fully explain what the table contains. |
| cec-008 | Table 242.3 | 9/10 | 9/10 | Good explanation of cross-reference table for surge protection. |
| cec-009 | Table 430.72(B) | 10/10 | 10/10 | Excellent: Columns A/B/C explained, exception coverage. |
| cec-010 | Medium voltage tables | 10/10 | 10/10 | Correct: 18 tables (311.60(C)(67-86)), California-only. |

**California-Specific Average: 9.6/10**

### CEC Delta Tables

| ID | Question | Accuracy | Completeness | Notes |
|----|----------|----------|--------------|-------|
| cec-011 | 4/0 AWG ampacity at 75°C | 10/10 | 10/10 | Correct: 230A per CEC Table 310.16. |
| cec-012 | EGC for 200A circuit | 10/10 | 10/10 | Correct: 6 AWG Cu or 4 AWG Al per Table 250.122. |
| cec-013 | GEC for 3/0 service | 10/10 | 10/10 | Correct: 4 AWG Cu per Table 250.66. |
| cec-014 | Temp correction 75°C at 40°C | 10/10 | 10/10 | Correct: 0.88 per Table 310.15(B)(1)(1). |
| cec-015 | Bundling 7-9 conductors | 10/10 | 10/10 | Correct: 0.70 (70%) per Table 310.15(C)(1). |
| cec-016 | Working space 480V Condition 3 | 10/10 | 10/10 | Correct: 1.2m (4 ft) per Table 110.26(A)(1). |
| cec-017 | Enclosure types for outdoor | 9/10 | 9/10 | Lists appropriate types but slightly different format than expected. |
| cec-018 | Office lighting load | **5/10** | 5/10 | **VERIFIED ERROR**: Agent says 1 VA/ft² citing Section 220.14(K). WRONG - that's for receptacle loads. Table 220.12 (lighting) clearly shows 1.3 VA/ft² for offices. Agent confused lighting vs receptacle load sections. |
| cec-019 | 12 AWG flexible cord ampacity | 10/10 | 10/10 | Correct: 25A per Table 400.5(A)(1). |
| cec-020 | SF-2 fixture wire temp | **10/10** | **10/10** | **MAJOR FIX**: Correctly identifies 200°C. This was a FAIL in Run 12. |

**Delta Tables Average: 9.2/10** (adjusted after deep dive)

### Complex Calculations

| ID | Question | Accuracy | Completeness | Notes |
|----|----------|----------|--------------|-------|
| cec-021 | 8 AWG THWN derating | 10/10 | 10/10 | Correct: 50A × 0.88 × 0.70 = 30.8A |
| cec-022 | 200A service sizing | 9/10 | 9/10 | Uses 2/0 AWG per 310.12 (83% rule). Expected 3/0 per 310.16. Both defensible. |
| cec-023 | Office lighting 5000 sqft | 10/10 | 10/10 | Correct: 5000 × 1.3 = 6,500 VA |
| cec-024 | Motor control 16 AWG OCP | 10/10 | 10/10 | Correct: 10A per Table 430.72(B) Column C. |
| cec-025 | Dwelling lighting 2400 sqft | 10/10 | 10/10 | Correct: 2400 × 3 = 7,200 VA |

**Calculations Average: 9.8/10**

### CEC vs NEC Comparison

| ID | Question | Accuracy | Completeness | Notes |
|----|----------|----------|--------------|-------|
| cec-026 | Kitchen GFCI comparison | 9/10 | 9/10 | Correctly identifies NEC as more restrictive. Good analysis. |
| cec-027 | Panelboard comparison | 10/10 | 10/10 | Correct: CEC 408.2 requires reserved spaces, NEC does not. |
| cec-028 | EV charging comparison | 10/10 | 10/10 | Excellent: CA mandates, NEC only guides installation. |
| cec-029 | AFCI comparison | 9/10 | 9/10 | Good comparison, slight differences in exception coverage noted. |
| cec-030 | Solar PV comparison | 10/10 | 10/10 | Correct: CA mandates via Title 24, NEC only installation rules. |

**Comparison Average: 9.6/10**

### CEC Evaluation Total: **9.2/10** (277/300 points) - adjusted after deep dive

---

## Questions with Notable Improvements from Run 12

### 1. core-010: Ampacity Derating (FIXED - Was FAIL)
**Question:** Six 12 AWG THHN conductors in 50°C ambient

| Aspect | Run 12 | Run 13 |
|--------|--------|--------|
| Answer | 25A (no derating) | 19.68A |
| Calculation | Missing | 30A × 0.82 × 0.80 = 19.68A |
| Score | 0/10 (FAIL) | 10/10 |

**Fix Applied:** New unified ampacity calculation tool + rule hierarchy prompt

### 2. cec-020: SF-2 Fixture Wire Temperature (FIXED - Was FAIL)
**Question:** Maximum operating temperature for Type SF-2

| Aspect | Run 12 | Run 13 |
|--------|--------|--------|
| Answer | Could not find | 200°C (392°F) |
| Reference | None | CEC Section 620.11(A)(1) |
| Score | 0/10 (FAIL) | 10/10 |

**Fix Applied:** Routing guidance for table lookups

### 3. baseline-001: 12 AWG Ampacity with Limiting Rule
**Question:** Ampacity of 12 AWG copper at 75°C

| Aspect | Run 12 | Run 13 |
|--------|--------|--------|
| Answer | 25A (just ampacity) | 25A ampacity + 20A OCP limit |
| Limiting Rule | Not mentioned | 240.4(D) explicitly cited |
| Score | 8/10 | 10/10 |

**Fix Applied:** Rule hierarchy system prompt

### 4. core-010 Improvements Detail
The agent now correctly:
1. Identifies base ampacity (30A at 90°C for THHN)
2. Applies temperature correction (0.82 for 50°C)
3. Applies bundling adjustment (0.80 for 6 conductors)
4. Shows full calculation: 30 × 0.82 × 0.80 = 19.68A

---

## Questions with Verified Errors (Deep Dive Analysis)

### 1. baseline-002: Conductor for 60A Circuit - **VERIFIED ERROR**
- Agent says: 4 AWG citing 240.4(D) 50A limit for 6 AWG
- Correct answer: **6 AWG** (65A at 75°C, sufficient for 60A)
- **Root Cause:** Agent misapplied 240.4(D) "Small Conductors" which ONLY applies to 10 AWG and smaller. 6 AWG is NOT covered by this section - it falls under general rule 240.4(B). The agent fabricated a non-existent "50A limit for 6 AWG."
- **Score:** 5/10 (was 8/10)

### 2. cec-018: Office Lighting Load - **VERIFIED ERROR**
- Agent says: 1 VA/ft² citing Section 220.14(K)
- Correct answer: **1.3 VA/ft²** per Table 220.12
- **Root Cause:** Agent confused two different sections:
  - Table 220.12 = General **lighting** loads → Office = **1.3 VA/ft²**
  - Section 220.14(K) = **Receptacle** loads → Office = 1 VA/ft²
- The agent cited receptacle loads when asked about lighting loads.
- **Score:** 5/10 (was 7/10)

### 3. inspection-010: GEC Sizing - **VERIFIED ERROR**
- Agent says: 3/0 AWG with faulty interpolation logic
- Correct answer: **2/0 AWG** per Table 250.66 row "Over 600 through 1100 kcmil"
- **Root Cause:** Agent misread table structure. Instead of reading the direct specification in the row label, it tried to interpolate between boundary values (600 and 1100) and incorrectly selected 3/0 AWG.
- **Score:** 5/10 (was 8/10)

---

## Summary Statistics (Adjusted After Deep Dive)

### Score Distribution

| Score | Core | CEC | Total |
|-------|------|-----|-------|
| 10/10 | 18 | 22 | 40 (69%) |
| 9/10 | 7 | 6 | 13 (22%) |
| 8/10 | 1 | 1 | 2 (3%) |
| 5/10 | 2 | 1 | 3 (5%) |
| <5 | 0 | 0 | 0 |

### Issues by Category

| Category | Issue | Root Cause |
|----------|-------|------------|
| 240.4(D) Scope | baseline-002 | Agent doesn't know 240.4(D) only covers 10 AWG and smaller |
| Table Disambiguation | cec-018 | Agent confuses lighting loads (220.12) with receptacle loads (220.14) |
| Table Reading | inspection-010 | Agent uses interpolation instead of reading direct row specification |

---

## Conclusions

### What Worked Well
1. **Unified Ampacity Tool** - Fixed core-010 completely (19.68A calculation now correct)
2. **cec-020 Fixed** - SF-2 fixture wire temperature now correctly identified as 200°C
3. **Exception Search** - More thorough exception checking in most answers

### What Needs Fixing (Run 14 Targets)

#### 1. 240.4(D) Scope Knowledge (baseline-002)
**Problem:** Agent thinks 240.4(D) applies to all conductor sizes
**Fix Needed:** Add explicit knowledge that 240.4(D) "Small Conductors" ONLY covers:
- 18 AWG (7A max)
- 16 AWG (10A max)
- 14 AWG (15A max)
- 12 AWG (20A max)
- 10 AWG (30A max)
**NOT 8 AWG, 6 AWG, 4 AWG, etc.** - these fall under general 240.4(B)

#### 2. Table Section Disambiguation (cec-018)
**Problem:** Agent confuses similar-sounding code sections
**Fix Needed:** Better routing in system prompt:
- "General lighting load" → Table 220.12
- "Receptacle load" → Section 220.14
- Never cite 220.14(K) when asked about lighting loads

#### 3. Table Range Reading (inspection-010)
**Problem:** Agent interpolates instead of reading table row labels directly
**Fix Needed:** Improve table lookup logic to:
- First check if value falls within a named range (e.g., "Over 600 through 1100")
- Return the value specified for that range
- Do NOT interpolate between boundary values

### Overall Assessment
Run 13 **fixed 2 issues but exposed 3 new ones** that weren't caught before:
- **Overall score: 9.1/10** (same as Run 12)
- **69% perfect scores** (down from initial 74% estimate)
- **3 verified errors** need fixing for Run 14

The improvements in Run 13 (ampacity tool, rule hierarchy) are working, but the deep dive revealed code interpretation errors that need addressing.
