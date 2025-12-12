# Judge Report - core-run29_evaluation_results_2025-12-10

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | CEC Lang Agent (qwen/qwen3-32b) |
| **Source File** | core-run29_evaluation_results_2025-12-10.md |
| **Judge** | Claude Code (Opus) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-10 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 27 |
| **Total Score** | 241 / 270 |
| **Percentage** | 89.3% |
| **Avg Accuracy** | 4.48 / 5 |
| **Avg Completeness** | 4.44 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 14 |
| High (8-9/10) | 10 |
| Medium (5-7/10) | 2 |
| Low (0-4/10) | 1 |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| baseline-002 | What size copper conductor for 60A at 75C? | 5/5 | 5/5 | 10/10 |
| baseline-003 | GFCI in residential kitchen | 4/5 | 4/5 | 8/10 |
| baseline-004 | AFCI for bedroom circuits | 5/5 | 5/5 | 10/10 |
| baseline-005 | Aluminum conductors for 200A service | 5/5 | 5/5 | 10/10 |
| baseline-006 | Working clearance for 120/240V panel | 5/5 | 5/5 | 10/10 |
| baseline-007 | Small appliance circuits for kitchen | 5/5 | 5/5 | 10/10 |
| baseline-008 | Surge protection for 200A service | 5/5 | 5/5 | 10/10 |
| core-001 | Service conductors for 200A upgrade | 5/5 | 5/5 | 10/10 |
| core-002 | Multiwire branch circuit requirements | 5/5 | 4/5 | 9/10 |
| core-003 | GFCI locations in residential dwelling | 5/5 | 4/5 | 9/10 |
| core-004 | Surge protection requirement and location | 5/5 | 5/5 | 10/10 |
| core-005 | Panel in closet with 24" clearance | 4/5 | 4/5 | 8/10 |
| core-006 | Two conductors on single breaker terminal | 5/5 | 5/5 | 10/10 |
| core-007 | Detached garage subpanel grounding | 5/5 | 5/5 | 10/10 |
| core-008 | Main bonding vs system bonding jumper | 5/5 | 5/5 | 10/10 |
| core-009 | Small appliance circuits serving dining room | 5/5 | 5/5 | 10/10 |
| core-010 | Adjusted ampacity for 12 AWG THHN | 5/5 | 5/5 | 10/10 |
| core-011 | Why AFCI required for bedrooms | 5/5 | 5/5 | 10/10 |
| core-012 | Torque specifications importance | 5/5 | 4/5 | 9/10 |
| inspection-001 | Service load calculation | 4/5 | 4/5 | 8/10 |
| inspection-002 | Panel in garage violations | 3/5 | 4/5 | 7/10 |
| inspection-005 | Kitchen circuit protection types | 3/5 | 4/5 | 7/10 |
| inspection-006 | Subpanel grounding violations | 5/5 | 5/5 | 10/10 |
| inspection-007 | Conduit fill calculation | 5/5 | 5/5 | 10/10 |
| inspection-008 | Voltage drop calculation | 5/5 | 5/5 | 10/10 |
| inspection-009 | Adjusted ampacity for 12 AWG TW | 5/5 | 5/5 | 10/10 |
| inspection-010 | GEC for parallel service conductors | 2/5 | 1/5 | 3/10 |

---

## Detailed Results

### baseline-002
**Question:** What size copper conductor is required for a 60A circuit at 75°C?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 6 AWG copper with 65A ampacity at 75°C from Table 310.16. Accurately notes 8 AWG is insufficient.
**Completeness Notes:** Provides relevant code references (310.16, 240.4(D)), explains why 6 AWG is required, and notes exceptions don't apply.

---

### baseline-003
**Question:** Where is GFCI protection required in a residential kitchen?
**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies countertop surfaces and within 6 feet of sink. However, does NOT mention dishwasher GFCI requirement which is expected.
**Completeness Notes:** Good coverage of countertop and sink distance requirements, but missing dishwasher-specific requirement.

---

### baseline-004
**Question:** Is AFCI protection required for bedroom circuits in new residential construction?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states yes, AFCI required per 210.12(A) for 120V, 15/20A circuits in bedrooms.
**Completeness Notes:** Covers compliance options and exceptions thoroughly.

---

### baseline-005
**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states yes, 4/0 AWG aluminum per Table 310.12(A).
**Completeness Notes:** Provides conditions for use, alternative copper sizing, and code reference.

---

### baseline-006
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 36 inches (3 feet) per Table 110.26(A)(1).
**Completeness Notes:** Explains voltage range and conditions, includes inspector note about Condition 3.

---

### baseline-007
**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states minimum of two 20A small appliance circuits.
**Completeness Notes:** Cites 210.52(B)(1) and 210.11(C)(1), explains limitations.

---

### baseline-008
**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states yes, per 230.67(A) for all services supplying dwelling units.
**Completeness Notes:** Covers SPD type, location requirements, and installation details.

---

### core-001
**Question:** Service conductors for 200A upgrade
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states 2/0 AWG copper OR 4/0 AWG aluminum per Table 310.12(A).
**Completeness Notes:** Addresses both materials, provides code references, notes conditions.

---

### core-002
**Question:** Multiwire branch circuit requirements
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies 2-pole breaker for simultaneous disconnect per 210.4(B), neutral termination.
**Completeness Notes:** Missing explicit mention of handle tie option and conductor grouping requirement 210.4(D).

---

### core-003
**Question:** GFCI locations in residential dwelling
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Lists correct locations: bathrooms, garages, outdoors, crawl spaces, kitchens, laundry, etc.
**Completeness Notes:** Missing explicit mention of unfinished basements as a distinct location.

---

### core-004
**Question:** Surge protection requirement and location
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states yes per 230.67, Type 1 or Type 2 SPD required.
**Completeness Notes:** Covers location options (integral or adjacent), exception for downstream panelboard.

---

### core-005
**Question:** Panel in closet with 24" clearance
**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies depth violation (24" < 36") and obstruction issue. However, incorrectly states 42" required for 240V when it should be 36" for Condition 1/2. Also doesn't clearly identify this as a "closet" violation per 240.24(D).
**Completeness Notes:** Identifies key violations but misses clothes closet prohibition.

---

### core-006
**Question:** Two conductors on single breaker terminal
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies code violation per 408.41/110.14(A) for unmarked terminals.
**Completeness Notes:** Explains exception requirement and manufacturer marking requirement.

---

### core-007
**Question:** Detached garage subpanel grounding
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states neutral and ground must be separated, no main bonding jumper in subpanel.
**Completeness Notes:** Covers EGC sizing, GEC to local electrode, cites correct code sections.

---

### core-008
**Question:** Main bonding vs system bonding jumper
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly distinguishes MBJ (service equipment) vs SBJ (separately derived systems).
**Completeness Notes:** Includes sizing requirements, when each is required, and exceptions.

---

### core-009
**Question:** Small appliance circuits serving dining room
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly states minimum two circuits, and yes they can serve dining room.
**Completeness Notes:** Cites correct code sections and explains limitations.

---

### core-010
**Question:** Adjusted ampacity for 12 AWG THHN
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates: 30A base × 0.82 (temp) × 0.80 (bundle) = 19.7A.
**Completeness Notes:** Shows all steps, cites tables, notes 240.4(D) limit.

---

### core-011
**Question:** Why AFCI required for bedrooms
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly explains AFCI prevents electrical fires from arc faults that standard breakers can't detect.
**Completeness Notes:** Lists specific causes (damaged cords, loose connections), explains detection mechanism.

---

### core-012
**Question:** Torque specifications importance
**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correctly explains torque prevents loose connections and heat generation.
**Completeness Notes:** Cites 110.14(D) correctly but doesn't mention Table 110.14(D) explicitly.

---

### inspection-001
**Question:** Service load calculation
**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Uses optional method (220.82) correctly but expected answer uses standard method (220.42) with different demand factors. Both methods are valid but results differ. Final conclusion (200A adequate) is correct.
**Completeness Notes:** Shows clear work but uses different calculation method than expected.

---

### inspection-002
**Question:** Panel in garage violations
**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies depth violation (28" < 36") and water heater obstruction. Incorrectly claims 54" width required (should be 30" or equipment width). Incorrectly claims 6.5' headroom violation (5' mounting height doesn't directly indicate headroom violation).
**Completeness Notes:** Identifies main issues but includes incorrect requirements.

---

### inspection-005
**Question:** Kitchen circuit protection types
**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies most circuits need AFCI+GFCI. However, states refrigerator only needs AFCI which is INCORRECT per NEC 2023 210.8(A)(5) - ALL kitchen receptacles including refrigerator now require GFCI.
**Completeness Notes:** Covers all circuits but has error on refrigerator requirement.

---

### inspection-006
**Question:** Subpanel grounding violations
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies bonded neutral/ground as violation and neutral-to-enclosure bond as violation.
**Completeness Notes:** Provides correct configuration, explains why bonding is wrong in subpanels.

---

### inspection-007
**Question:** Conduit fill calculation
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates 28 conductors maximum (0.6104 ÷ 0.0211 = 28.91 → 28).
**Completeness Notes:** Shows all steps with correct table references.

---

### inspection-008
**Question:** Voltage drop calculation
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates 2.84V drop, 2.37%, which meets 3% recommendation.
**Completeness Notes:** Shows formula and calculation, confirms compliance.

---

### inspection-009
**Question:** Adjusted ampacity for 12 AWG TW
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly calculates: 20A base × 0.71 (temp) × 0.80 (bundle) = 11.36A.
**Completeness Notes:** Shows all steps with correct factors for 60°C conductor.

---

### inspection-010
**Question:** GEC for parallel service conductors
**Score:** 3/10 (Accuracy: 2/5, Completeness: 1/5)
**Accuracy Notes:** Response is essentially empty - no answer provided. The expected answer is 2/0 AWG copper GEC per Table 250.66 for 1000 kcmil equivalent service conductors.
**Completeness Notes:** Failed to provide any answer. Tool was called multiple times but no conclusion reached.

---
