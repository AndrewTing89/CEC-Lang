# Judge Report - core-run22_evaluation_results_2025-12-10

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | CEC Agent (qwen/qwen3-32b) |
| **Source File** | core-run22_evaluation_results_2025-12-10.md |
| **Judge** | Claude Code (Opus) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-10 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 28 |
| **Total Score** | 209 / 280 |
| **Percentage** | 74.6% |
| **Avg Accuracy** | 3.7 / 5 |
| **Avg Completeness** | 3.8 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 14 |
| High (8-9/10) | 5 |
| Medium (5-7/10) | 4 |
| Low (0-4/10) | 5 |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| baseline-001 | 12 AWG ampacity at 75C | 5/5 | 5/5 | 10/10 |
| baseline-002 | Conductor size for 60A | 5/5 | 5/5 | 10/10 |
| baseline-003 | GFCI in kitchen | 4/5 | 5/5 | 9/10 |
| baseline-004 | AFCI for bedrooms | 5/5 | 5/5 | 10/10 |
| baseline-005 | Aluminum for 200A service | 5/5 | 5/5 | 10/10 |
| baseline-006 | Working clearance depth | 2/5 | 3/5 | 5/10 |
| baseline-007 | Small appliance circuits | 5/5 | 5/5 | 10/10 |
| baseline-008 | Surge protection required | 5/5 | 5/5 | 10/10 |
| core-001 | 200A service upgrade | 4/5 | 4/5 | 8/10 |
| core-002 | Multiwire branch circuit | 5/5 | 4/5 | 9/10 |
| core-003 | GFCI locations list | 4/5 | 5/5 | 9/10 |
| core-004 | Surge protection location | 2/5 | 3/5 | 5/10 |
| core-005 | Panel in closet violations | 2/5 | 3/5 | 5/10 |
| core-006 | Two conductors on terminal | 5/5 | 5/5 | 10/10 |
| core-007 | Detached garage bonding | 1/5 | 1/5 | 2/10 |
| core-008 | MBJ vs SBJ | 5/5 | 5/5 | 10/10 |
| core-009 | Small appliance + dining | 5/5 | 5/5 | 10/10 |
| core-010 | Adjusted ampacity 50C | 3/5 | 4/5 | 7/10 |
| core-011 | Why AFCI required | 5/5 | 5/5 | 10/10 |
| core-012 | Torque specifications | 4/5 | 5/5 | 9/10 |
| inspection-001 | 200A load calculation | 0/5 | 0/5 | 0/10 |
| inspection-002 | Garage panel violations | 2/5 | 3/5 | 5/10 |
| inspection-005 | Kitchen circuit protection | 2/5 | 2/5 | 4/10 |
| inspection-006 | Subpanel bonding violations | 0/5 | 0/5 | 0/10 |
| inspection-007 | Conduit fill calculation | 5/5 | 5/5 | 10/10 |
| inspection-008 | Voltage drop calculation | 2/5 | 2/5 | 4/10 |
| inspection-009 | Adjusted ampacity 43C | 5/5 | 5/5 | 10/10 |
| inspection-010 | GEC sizing for data center | 5/5 | 4/5 | 9/10 |

---

## Detailed Results

### baseline-001
**Question:** What is the ampacity of a 12 AWG copper conductor with 75C rated insulation (such as THWN) according to NEC Table 310.16?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Model correctly states 25 amperes for 12 AWG at 75C per Table 310.16. Note: Expected answer says 20A which is incorrect for 75C column.
**Completeness Notes:** Includes table reference, CEC comparison, and notes about no amendments.

---

### baseline-002
**Question:** What size copper conductor is required for a 60A circuit at 75C?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 6 AWG copper (65A at 75C).
**Completeness Notes:** Complete with table reference and CEC/NEC comparison.

---

### baseline-003
**Question:** Where is GFCI protection required in a residential kitchen?
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies countertop receptacles per 210.8(A)(6). Does not specifically mention dishwasher GFCI requirement.
**Completeness Notes:** Good coverage with code references.

---

### baseline-004
**Question:** Is AFCI protection required for bedroom circuits in new residential construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states yes, required per 210.12(A) for 15-20A circuits.
**Completeness Notes:** Complete with protection methods and code references.

---

### baseline-005
**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 4/0 AWG aluminum per Table 310.12(A).
**Completeness Notes:** Includes termination compatibility notes (110.14(C)), corrosion protection.

---

### baseline-006
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?
**Score:** 5/10 (Accuracy: 2/5, Completeness: 3/5)
**Accuracy Notes:** WRONG - states 30 inches. Correct answer is 36 inches (3 feet) per Table 110.26(A)(1) for 0-150V/151-600V Condition 1.
**Completeness Notes:** Has code reference but wrong value.

---

### baseline-007
**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states minimum of 2 circuits per 210.11(C)(1).
**Completeness Notes:** Includes scope (kitchen, pantry, breakfast room, dining room).

---

### baseline-008
**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states yes, required per 230.67, Type 1 or Type 2.
**Completeness Notes:** Includes installation locations and code references.

---

### core-001
**Question:** 200A service upgrade - conductor sizing
**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** States 4/0 AWG copper or 250 kcmil aluminum. Expected: 2/0 copper OR 4/0 aluminum per Table 310.12. Oversized but acceptable.
**Completeness Notes:** Good detail but minimum sizes differ from expected.

---

### core-002
**Question:** Multiwire branch circuit requirements
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies common trip/handle tie per 210.4(B), 240.15(B)(1).
**Completeness Notes:** Missing explicit mention of grouping per 210.4(D).

---

### core-003
**Question:** Where is GFCI protection required - list all locations
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Lists 11 locations including "indoor damp/wet locations" rather than specifically "unfinished basements".
**Completeness Notes:** Comprehensive list with code references.

---

### core-004
**Question:** Surge protection required and installation location
**Score:** 5/10 (Accuracy: 2/5, Completeness: 3/5)
**Accuracy Notes:** MAJOR ERROR - States NEC 2023 does NOT require surge protection. This is WRONG - NEC 2023 Section 230.67 DOES require SPD for dwelling units.
**Completeness Notes:** Partial information but fundamental error on NEC requirement.

---

### core-005
**Question:** Panel in closet with 24" clearance violations
**Score:** 5/10 (Accuracy: 2/5, Completeness: 3/5)
**Accuracy Notes:** Wrong depth requirement (says 30", correct is 36"). Misses clothes closet prohibition (240.24(D)).
**Completeness Notes:** Identifies some violations but misses key ones.

---

### core-006
**Question:** Two conductors on unmarked terminal
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies violation per 110.14(A).
**Completeness Notes:** Clear explanation and remedy.

---

### core-007
**Question:** Detached garage subpanel bonding configuration
**Score:** 2/10 (Accuracy: 1/5, Completeness: 1/5)
**Accuracy Notes:** WRONG TOPIC - Answered about GEC sizing instead of bonding configuration. Expected: grounds/neutrals separated, no MBJ in subpanel, neutral isolated.
**Completeness Notes:** Does not address the question asked.

---

### core-008
**Question:** Main bonding jumper vs system bonding jumper
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies MBJ at service (250.28), SBJ at separately derived systems (250.30).
**Completeness Notes:** Complete with sizing references.

---

### core-009
**Question:** Small appliance circuits serving dining room
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 2 circuits, can serve dining room per 210.52(B)(1).
**Completeness Notes:** Includes prohibited loads.

---

### core-010
**Question:** Adjusted ampacity at 50C with 6 conductors
**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** Wrong base ampacity - states 35A, should be 30A for 12 AWG THHN at 90C. Correct factors (0.82, 0.80). Result 23.1A should be ~19.68A.
**Completeness Notes:** Method correct but wrong starting value.

---

### core-011
**Question:** Why AFCI protection required
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies arc fault prevention, fire hazard, damaged wiring.
**Completeness Notes:** Good explanation with code reference.

---

### core-012
**Question:** Torque specifications importance
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies fire hazard prevention, 110.3(B).
**Completeness Notes:** Missing specific mention of 110.14(D) as expected.

---

### inspection-001
**Question:** 200A service load calculation
**Score:** 0/10 (Accuracy: 0/5, Completeness: 0/5)
**Accuracy Notes:** WRONG TOPIC - Answered about torque specifications instead of load calculation. Expected: detailed Article 220 calculation.
**Completeness Notes:** Does not address the question at all.

---

### inspection-002
**Question:** Garage panel violations
**Score:** 5/10 (Accuracy: 2/5, Completeness: 3/5)
**Accuracy Notes:** Wrong depth requirement (28" < 30" stated, should be 36"). Misinterprets panel height (5 feet is mounting height, not working space violation).
**Completeness Notes:** Identifies water heater obstruction correctly.

---

### inspection-005
**Question:** Kitchen circuit protection types
**Score:** 4/10 (Accuracy: 2/5, Completeness: 2/5)
**Accuracy Notes:** MAJOR ERRORS - Says dishwasher exempt from GFCI (WRONG per 2023 NEC 210.8(D)). Misses AFCI requirements for all kitchen circuits per 210.12(A).
**Completeness Notes:** Incomplete and inaccurate protection requirements.

---

### inspection-006
**Question:** Subpanel bonding violations
**Score:** 0/10 (Accuracy: 0/5, Completeness: 0/5)
**Accuracy Notes:** WRONG TOPIC - Answered about service load calculation instead of subpanel bonding. Expected: identify bonding violations, correct configuration.
**Completeness Notes:** Does not address the question at all.

---

### inspection-007
**Question:** Conduit fill calculation for 10 AWG THHN in 1.25" RMC
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** CORRECT! Uses nec_conduit_fill_calculator. Gets 0.6104 sq in fill, 0.0211 sq in conductor, 28 conductors.
**Completeness Notes:** Complete calculation with Chapter 9 table references.

---

### inspection-008
**Question:** Voltage drop calculation
**Score:** 4/10 (Accuracy: 2/5, Completeness: 2/5)
**Accuracy Notes:** Wrong result - states 4.36V (3.63%). Correct: VD = (2 x 50 x 1.29 x 22)/1000 = 2.84V (2.37%).
**Completeness Notes:** Formula understood but calculation error.

---

### inspection-009
**Question:** Adjusted ampacity with temp and bundling factors
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** CORRECT! Base 20A, temp factor 0.71, bundling factor 0.80, result 11.36A.
**Completeness Notes:** All steps shown clearly.

---

### inspection-010
**Question:** GEC sizing for 1000 kcmil service
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correctly states 2/0 AWG copper GEC per Table 250.66.
**Completeness Notes:** Missing note about 6 AWG exception for rod electrodes.

---
