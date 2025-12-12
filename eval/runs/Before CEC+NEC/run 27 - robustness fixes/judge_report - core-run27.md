# Judge Report - core-run27

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | CEC Lang Agent (qwen/qwen3-32b) |
| **Source File** | core-run27_evaluation_results_2025-12-10.md |
| **Judge** | Claude Code (Opus 4.5) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-10 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 27 |
| **Total Score** | 245 / 270 |
| **Percentage** | 90.7% |
| **Avg Accuracy** | 4.63 / 5 |
| **Avg Completeness** | 4.81 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 21 |
| High (8-9/10) | 2 |
| Medium (5-7/10) | 2 |
| Low (0-4/10) | 2 |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| baseline-002 | Conductor size for 60A circuit | 5/5 | 5/5 | 10/10 |
| baseline-003 | GFCI in residential kitchen | 4/5 | 5/5 | 9/10 |
| baseline-004 | AFCI for bedroom circuits | 5/5 | 5/5 | 10/10 |
| baseline-005 | Aluminum for 200A service | 5/5 | 5/5 | 10/10 |
| baseline-006 | Working clearance depth | 5/5 | 5/5 | 10/10 |
| baseline-007 | Small appliance circuits | 5/5 | 5/5 | 10/10 |
| baseline-008 | Surge protection per NEC 2023 | 5/5 | 5/5 | 10/10 |
| core-001 | 200A service conductors | 5/5 | 5/5 | 10/10 |
| core-002 | MWBC breaker/neutral requirements | 5/5 | 5/5 | 10/10 |
| core-003 | GFCI locations in dwelling | 5/5 | 5/5 | 10/10 |
| core-004 | Surge protection installation | 5/5 | 5/5 | 10/10 |
| core-005 | Panel in closet violations | 1/5 | 2/5 | 3/10 |
| core-006 | Two conductors on terminal | 5/5 | 5/5 | 10/10 |
| core-007 | Garage subpanel grounding | 4/5 | 5/5 | 9/10 |
| core-008 | MBJ vs SBJ difference | 5/5 | 5/5 | 10/10 |
| core-009 | Small appliance + dining room | 5/5 | 5/5 | 10/10 |
| core-010 | Ampacity adjustment 50°C | 5/5 | 5/5 | 10/10 |
| core-011 | Why AFCI required | 5/5 | 5/5 | 10/10 |
| core-012 | Torque specifications | 5/5 | 5/5 | 10/10 |
| inspection-001 | Load calculation 200A panel | 3/5 | 4/5 | 7/10 |
| inspection-002 | Panel inspection violations | 5/5 | 5/5 | 10/10 |
| inspection-005 | Kitchen circuit protection | 3/5 | 4/5 | 7/10 |
| inspection-006 | Subpanel bonding violations | 5/5 | 5/5 | 10/10 |
| inspection-007 | Conduit fill calculation | 5/5 | 5/5 | 10/10 |
| inspection-008 | Voltage drop calculation | 5/5 | 5/5 | 10/10 |
| inspection-009 | Ampacity TW at 43°C | 5/5 | 5/5 | 10/10 |
| inspection-010 | GEC sizing for data center | 5/5 | 5/5 | 10/10 |

---

## Detailed Results

### baseline-002
**Question:** What size copper conductor is required for a 60A circuit at 75°C?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 6 AWG copper with 65A ampacity at 75°C from Table 310.16. Matches expected answer exactly.
**Completeness Notes:** Excellent detail including why 8 AWG is insufficient, OCP limits per 240.4(D), and inspector notes about derating.

---

### baseline-003
**Question:** Where is GFCI protection required in a residential kitchen?
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies countertop receptacles per 210.8(A)(6). Minor omission: didn't explicitly mention dishwasher requirement.
**Completeness Notes:** Very thorough on countertops including islands and peninsulas, GFCI device types.

---

### baseline-004
**Question:** Is AFCI protection required for bedroom circuits in new residential construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states AFCI required per Section 210.12(A) for 120V, 15/20A circuits.
**Completeness Notes:** Excellent coverage of six protection methods and exceptions.

---

### baseline-005
**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 4/0 AWG aluminum per Table 310.12(A).
**Completeness Notes:** Includes application scope, insulation requirements, and inspector notes.

---

### baseline-006
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 900mm (3 feet) per Table 110.26(A)(1).
**Completeness Notes:** Includes conditions and when clearance increases to 1,050mm.

---

### baseline-007
**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states minimum two 20A circuits per 210.11(C)(1).
**Completeness Notes:** Includes code citations and serving restrictions.

---

### baseline-008
**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states yes per Section 230.67(A)(1).
**Completeness Notes:** Includes SPD type requirements and citation.

---

### core-001
**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 2/0 AWG copper or 4/0 AWG aluminum per Table 310.12(A).
**Completeness Notes:** Provides both material options with termination and inspector notes.

---

### core-002
**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly covers simultaneous disconnection (210.4(B)), phasing requirements, and neutral termination.
**Completeness Notes:** Very thorough with code references 210.4(B), 210.4(D), and 200.4(B).

---

### core-003
**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC? List all locations.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Lists all 11 required locations per 210.8(A).
**Completeness Notes:** Comprehensive list including exceptions.

---

### core-004
**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states required per 230.67(A), Type 1/2 SPD, at service or adjacent or downstream.
**Completeness Notes:** All installation locations covered with exception.

---

### core-005
**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?
**Score:** 3/10 (Accuracy: 1/5, Completeness: 2/5)
**Accuracy Notes:** WRONG. Model claims installation meets requirements based on 12" requirement for "Condition 2" - this is incorrect. 36" minimum is required for 120/240V equipment per 110.26(A)(1). The model misinterpreted the voltage and table conditions.
**Completeness Notes:** Missed multiple violations: (1) 36" depth required not 24", (2) potential clothes closet prohibition per 240.24(D), (3) water heater in working space violation.

---

### core-006
**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal. The breaker is not marked for two conductors. Is this a code violation?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies violation. Cited 240.15(A) and 240.5(B) instead of expected 110.14(A), but conclusion is correct.
**Completeness Notes:** Very thorough with corrective actions and risk explanation.

---

### core-007
**Question:** A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?
**Score:** 9/10 (Accuracy: 4/5, Completeness: 5/5)
**Accuracy Notes:** Correctly covers separation of neutrals/grounds, no bonding in subpanel. Minor inaccuracy: stated grounding electrode "not required" but 250.32 may require it in some cases.
**Completeness Notes:** Very thorough with code references and inspector notes.

---

### core-008
**Question:** What is the difference between a main bonding jumper and a system bonding jumper? When is each required?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly distinguishes MBJ (at service) from SBJ (at separately derived systems).
**Completeness Notes:** Excellent table format comparing the two.

---

### core-009
**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states minimum two circuits, can serve dining room per 210.52(B)(1).
**Completeness Notes:** Includes code citations and inspector notes.

---

### core-010
**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates 30A × 0.82 × 0.80 = 19.68A.
**Completeness Notes:** Shows all steps with table references.

---

### core-011
**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly explains AFCI prevents electrical fires from arc faults.
**Completeness Notes:** Very thorough with hazard types and protection mechanisms.

---

### core-012
**Question:** Why are torque specifications important when terminating conductors in a panel, and where are the requirements found?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly cites 110.14(D) and importance of proper torque.
**Completeness Notes:** Includes informational notes and approved methods.

---

### inspection-001
**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.
**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** Conclusion correct (200A adequate), but calculation differs from standard method. Model got 114.17A vs expected 103.2A due to different demand factor application. Did not apply Table 220.42 correctly to general/lighting loads.
**Completeness Notes:** Shows work but methodology differs from expected Article 220 standard calculation.

---

### inspection-002
**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side within the working space. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies depth violation (28" vs 36" required), water heater obstruction.
**Completeness Notes:** Very thorough with summary table of violations and required fixes.

---

### inspection-005
**Question:** New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references.
**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** Correctly requires GFCI+AFCI for countertop, dishwasher, disposal. INCORRECT on refrigerator - claims standard breaker only due to exception, but NEC 2023 expanded 210.8(A)(5) to cover ALL kitchen receptacles including dedicated appliance circuits.
**Completeness Notes:** Covers all circuits with references but wrong on refrigerator protection requirements.

---

### inspection-006
**Question:** Subpanel inspection in detached garage: 100A subpanel fed from main house panel with 4-wire feeder (#2 AWG aluminum: 2 hots, 1 neutral, 1 ground). Inspector notes: (1) neutral bar and ground bar are bonded together with main bonding jumper installed, (2) ground bar is bonded to metal enclosure, (3) neutral bar is bonded to metal enclosure, (4) feeder ground wire is connected to ground bar, (5) feeder neutral is connected to neutral bar. Identify all violations and explain correct configuration.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies violations: neutral bonded to enclosure, MBJ installed in subpanel.
**Completeness Notes:** Very detailed with correct configuration and summary of fixes.

---

### inspection-007
**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates 0.610 / 0.0211 = 28.91, rounds to 28 conductors.
**Completeness Notes:** Shows calculation and verification of fill percentage.

---

### inspection-008
**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates VD = 2.84V, 2.37%, meets NEC 3% recommendation.
**Completeness Notes:** Shows formula and all steps clearly.

---

### inspection-009
**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates 20A × 0.71 × 0.80 = 11.36A.
**Completeness Notes:** Shows all steps with table references.

---

### inspection-010
**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 4 × 250 kcmil = 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required for this installation.
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 2/0 AWG copper per Table 250.66.
**Completeness Notes:** Shows calculation and code requirements.

---

## Notes

- **baseline-001 was not included** in the model responses (27 questions evaluated instead of expected 28)
- **core-005 had a critical error** where the model misinterpreted working space requirements
- **inspection-005 incorrectly exempted refrigerator** from GFCI/AFCI requirements under NEC 2023
- Overall strong performance on calculation and code interpretation questions

---

*Report Generated: 2025-12-10*
*Judge: Claude Code (Opus 4.5) - LLM-as-Judge Method*
