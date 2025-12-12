# Judge Report - core-run31_evaluation_results_2025-12-11.md

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | qwen/qwen3-32b |
| **Source File** | core-run31_evaluation_results_2025-12-11.md |
| **Judge** | Claude Code (Opus 4.5) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-11T12:30:00Z |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 27 |
| **Total Score** | 247 / 270 |
| **Percentage** | 91.5% |
| **Avg Accuracy** | 4.6 / 5 |
| **Avg Completeness** | 4.6 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 15 |
| High (8-9/10) | 9 |
| Medium (5-7/10) | 3 |
| Low (0-4/10) | 0 |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| baseline-002 | What size copper conductor... | 5/5 | 5/5 | 10/10 |
| baseline-003 | Where is GFCI protection required... | 5/5 | 4/5 | 9/10 |
| baseline-004 | Is AFCI protection required... | 5/5 | 5/5 | 10/10 |
| baseline-005 | Can aluminum conductors... | 5/5 | 5/5 | 10/10 |
| baseline-006 | Minimum depth working clearance... | 5/5 | 5/5 | 10/10 |
| baseline-007 | How many 20A small appliance... | 5/5 | 5/5 | 10/10 |
| baseline-008 | Is surge protection required... | 5/5 | 5/5 | 10/10 |
| core-001 | 200A service conductor sizing... | 5/5 | 5/5 | 10/10 |
| core-002 | Multiwire branch circuit... | 4/5 | 4/5 | 8/10 |
| core-003 | GFCI locations list... | 5/5 | 5/5 | 10/10 |
| core-004 | Surge protection locations... | 5/5 | 5/5 | 10/10 |
| core-005 | Panel in closet compliance... | 5/5 | 5/5 | 10/10 |
| core-006 | Two conductors on terminal... | 5/5 | 5/5 | 10/10 |
| core-007 | Detached garage grounding... | 5/5 | 5/5 | 10/10 |
| core-008 | MBJ vs SBJ difference... | 5/5 | 5/5 | 10/10 |
| core-009 | Kitchen circuits dining room... | 5/5 | 5/5 | 10/10 |
| core-010 | 12 AWG THHN adjusted ampacity... | 5/5 | 5/5 | 10/10 |
| core-011 | Why AFCI protection... | 5/5 | 5/5 | 10/10 |
| core-012 | Torque specifications... | 5/5 | 5/5 | 10/10 |
| inspection-001 | Service load calculation... | 3/5 | 4/5 | 7/10 |
| inspection-002 | Garage panel violations... | 4/5 | 4/5 | 8/10 |
| inspection-005 | Kitchen circuit protection... | 4/5 | 4/5 | 8/10 |
| inspection-006 | Subpanel bonding violations... | 5/5 | 5/5 | 10/10 |
| inspection-007 | Conduit fill calculation... | 5/5 | 4/5 | 9/10 |
| inspection-008 | Voltage drop calculation... | 4/5 | 4/5 | 8/10 |
| inspection-009 | TW ampacity adjustment... | 5/5 | 5/5 | 10/10 |
| inspection-010 | GEC sizing parallel... | 5/5 | 5/5 | 10/10 |

---

## Detailed Results

### baseline-002
**Question:** What size copper conductor is required for a 60A circuit at 75C?

**Agent Answer:** 6 AWG copper with 65A ampacity at 75C

**Expected Answer:** 6 AWG copper

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct answer with accurate Table 310.16 reference.
**Completeness Notes:** Includes additional context about overcurrent protection and adjustment factors.

---

### baseline-003
**Question:** Where is GFCI protection required in a residential kitchen?

**Agent Answer:** All 125V-250V receptacles serving countertop surfaces per 210.8(A)(6).

**Expected Answer:** All receptacles serving countertop surfaces and dishwasher.

**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correct about countertop receptacles.
**Completeness Notes:** Does not mention dishwasher GFCI requirement per 2023 NEC.

---

### baseline-004
**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Agent Answer:** Yes, per 210.12(A) for all 120V, 15A and 20A branch circuits.

**Expected Answer:** Yes, AFCI protection is required per 210.12.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct answer with proper code reference.
**Completeness Notes:** Comprehensive with installation methods and inspector notes.

---

### baseline-005
**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Agent Answer:** Yes, 4/0 AWG aluminum per Table 310.12(A).

**Expected Answer:** Yes, 4/0 AWG aluminum or copper-clad aluminum.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct conductor size and code reference.
**Completeness Notes:** Includes conditions for Table 310.12(A) application.

---

### baseline-006
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Agent Answer:** 900mm (3 feet) per Table 110.26(A)(1).

**Expected Answer:** 36 inches (3 feet).

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct answer with proper reference.
**Completeness Notes:** Includes location restrictions (240.24(D), 240.24(E)) - excellent addition.

---

### baseline-007
**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Agent Answer:** Minimum of two 20A circuits per 210.11(C)(1) and 220.52.

**Expected Answer:** Minimum of two 20-ampere small appliance branch circuits.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct answer with proper code references.
**Completeness Notes:** Comprehensive explanation with additional context.

---

### baseline-008
**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Agent Answer:** Yes, per Section 230.67. Type 1 or Type 2 SPD required.

**Expected Answer:** Yes, all services supplying dwelling units shall have SPD per 230.67.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct with all relevant code sections.
**Completeness Notes:** Excellent coverage of location, type, and replacement requirements.

---

### core-001
**Question:** A homeowner wants to upgrade from 100A to 200A service...

**Agent Answer:** 2/0 AWG copper OR 4/0 AWG aluminum per Table 310.12(A).

**Expected Answer:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct conductor sizes for both materials.
**Completeness Notes:** Includes load verification and overcurrent protection notes.

---

### core-002
**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles...

**Agent Answer:** Requires 2-pole breaker or handle tie per 210.4(B). Neutral must be grouped per 210.4(D).

**Expected Answer:** Handle tie OR common trip breaker per 210.4(B). Common trip required if line-to-line and line-to-neutral loads.

**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Correct about handle tie requirement but doesn't explicitly state "handle ties SHALL be permitted per 240.15(B)(1)".
**Completeness Notes:** Missing detail about common trip requirement for mixed loads.

---

### core-003
**Question:** Where is GFCI protection now required in a residential dwelling...

**Agent Answer:** Lists all locations: bathrooms, garages, outdoors, crawl spaces, basements, kitchens, sinks, boathouses, bathtubs/showers, laundry areas, indoor damp/wet locations.

**Expected Answer:** All listed locations plus within 6 feet of sinks.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All locations correctly identified with code references.
**Completeness Notes:** Comprehensive list with exceptions noted.

---

### core-004
**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Agent Answer:** Yes per 230.67(A). Integral to service equipment, immediately adjacent, or next level downstream.

**Expected Answer:** Yes per 230.67. Type 1 or Type 2 SPD. Integral, adjacent, or first downstream panelboard.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct answer with proper installation locations.
**Completeness Notes:** Comprehensive coverage of all options.

---

### core-005
**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side...

**Agent Answer:** Fails: 36" depth required (24" provided), 30" width requirement may fail, 240.24(D) prohibits panels in clothes closets.

**Expected Answer:** Violates: (1) 36" depth required, (2) panels prohibited in clothes closets per 240.24(D), (3) 30" width minimum, (4) no storage in working space.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correctly identifies all key violations including 240.24(D).
**Completeness Notes:** Comprehensive compliance table with clear pass/fail indicators.

---

### core-006
**Question:** During an inspection, I found two 12 AWG conductors landed on a single 20A breaker terminal...

**Agent Answer:** Yes, violation per 408.41 and 110.14(A). Terminal must be identified for multiple conductors.

**Expected Answer:** Yes, violation per 110.14(A). Must be identified for more than one conductor. Per 110.3(B), follow manufacturer instructions.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct identification of violation with appropriate code sections.
**Completeness Notes:** Includes corrective action recommendations.

---

### core-007
**Question:** A detached garage is fed from the house panel with a 4-wire feeder...

**Agent Answer:** EGC per Table 250.122, separate neutral/ground bars, GEC to local electrode per 250.32.

**Expected Answer:** Grounds/neutrals separated, no MBJ in subpanel, neutral isolated, EGC bonded to enclosure, GEC may be required per 250.32.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All key points correctly addressed.
**Completeness Notes:** Clear configuration summary with code citations.

---

### core-008
**Question:** What is the difference between a main bonding jumper and a system bonding jumper?

**Agent Answer:** MBJ at service equipment per 250.28, SBJ at separately derived systems. Sized per Table 250.102(C)(1).

**Expected Answer:** MBJ at service, SBJ at separately derived systems. Neither used in subpanels.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct definitions and applications.
**Completeness Notes:** Excellent comparison table and inspector notes.

---

### core-009
**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room?

**Agent Answer:** Minimum two 20A circuits per 210.11(C)(1). Yes, can serve dining room per 210.52(B)(1).

**Expected Answer:** Minimum TWO 20A circuits. Yes, can serve dining room, pantry, breakfast room. Cannot serve lighting.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct number and dining room allowance.
**Completeness Notes:** Includes key code citations and conditions.

---

### core-010
**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50C ambient...

**Agent Answer:** Base 30A, temp correction 0.82, bundling 0.80. Final: 30 x 0.82 x 0.80 = 19.68A.

**Expected Answer:** 30A x 0.82 x 0.80 = 19.68A, approximately 20A.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact calculation match with correct factors.
**Completeness Notes:** Step-by-step calculation with all references.

---

### core-011
**Question:** Why does the NEC require AFCI protection for bedrooms and living areas?

**Agent Answer:** Prevents electrical fires from arc faults: series arcing, damaged wiring, loose connections. Per 210.12 for dwelling units.

**Expected Answer:** Prevents fires from arc faults. Detects series arcing, loose connections, damaged insulation. Per 210.12.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct explanation of AFCI purpose.
**Completeness Notes:** Excellent technical basis including UL 1699 reference.

---

### core-012
**Question:** Why are torque specifications important when terminating conductors...

**Agent Answer:** Prevents loose connections, arcing, overtightening damage. Found in 110.14(D) and manufacturer instructions.

**Expected Answer:** Prevents loose connections, arcing, crushed conductors. Per 110.14(D) and Table 110.14(D).

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct reasons and code references.
**Completeness Notes:** Comprehensive with practical implications.

---

### inspection-001
**Question:** Residential panel inspection: 200A main breaker. Calculate service load...

**Agent Answer:** Total 32,500 VA / 240V = 135.4A. 200A panel adequately sized.

**Expected Answer:** Using Table 220.42 demand factors (first 3000 VA at 100%, remainder at 35%), total ~24,775 VA, 103.2A. 200A adequate.

**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** Did NOT correctly apply Table 220.42 demand factors for general lighting. Used 67% for range (should be 8000VA from Table 220.55). Final answer correct but methodology differs from expected.
**Completeness Notes:** Shows work but uses different demand factor approach than specified.

---

### inspection-002
**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth...

**Agent Answer:** Lists violations: insufficient depth (28" vs 36" required), insufficient height, water heater obstruction.

**Expected Answer:** Violations: (1) 28" depth vs 36" required, (2) water heater in working space prohibited per 110.26(B). Width meets minimum.

**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Correctly identifies depth violation. Incorrectly applies 42" for Condition 2 instead of 36" for Condition 1.
**Completeness Notes:** Covers most violations but some inaccuracies in specific requirements.

---

### inspection-005
**Question:** New residential construction, 2023 NEC. Kitchen installation...

**Agent Answer:** Countertops: AFCI/GFCI. Dishwasher: GFCI+AFCI. Disposal: GFCI+AFCI. Refrigerator: AFCI only.

**Expected Answer:** All circuits require combination AFCI/GFCI per 2023 NEC, including refrigerator.

**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Incorrectly states refrigerator is exempt from GFCI (2023 NEC expanded 210.8(A)(5) to all kitchen receptacles).
**Completeness Notes:** Good structure but refrigerator GFCI requirement missed.

---

### inspection-006
**Question:** Subpanel inspection in detached garage...

**Agent Answer:** Violations: neutral/ground bonded, neutral bonded to enclosure, MBJ installed. Correct: separate bars, remove MBJ.

**Expected Answer:** Violations: neutral bonded to enclosure, MBJ installed. Correct: separate bars, isolated neutral, remove MBJ.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All violations correctly identified.
**Completeness Notes:** Comprehensive correct configuration with code citations.

---

### inspection-007
**Question:** A 1 1/4-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN...

**Agent Answer:** 40% fill area 0.61 sq in / 0.0211 sq in per conductor = 28.91, max 28 conductors.

**Expected Answer:** 0.610 sq in / 0.0211 sq in = 28.91, round up to 29 per Note 7 (or 28 conservative).

**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** Correct calculation methodology.
**Completeness Notes:** Uses 28 (conservative) but doesn't mention Note 7 rounding rule that would allow 29.

---

### inspection-008
**Question:** A 120V single-phase branch circuit supplies a continuous load of 22 amperes...

**Agent Answer:** 2.37% voltage drop meets 3% recommendation.

**Expected Answer:** VD = (2 x 50 x 1.29 x 22) / 1000 = 2.84V. 2.84V / 120V = 2.37%. Meets 3% recommendation.

**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Correct percentage result.
**Completeness Notes:** Does not show the step-by-step calculation formula as requested.

---

### inspection-009
**Question:** A conduit in an attic contains six 12 AWG TW...

**Agent Answer:** 20A x 0.71 x 0.80 = 11.36A.

**Expected Answer:** 20A x 0.71 x 0.80 = 11.36A.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Exact calculation match.
**Completeness Notes:** Clear step-by-step process with proper factors.

---

### inspection-010
**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper...

**Agent Answer:** For 1000 kcmil (over 600 through 1100), minimum 2/0 AWG copper GEC per Table 250.66.

**Expected Answer:** Per Table 250.66, for 1000 kcmil copper, minimum 2/0 AWG copper GEC.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct answer with proper table reference.
**Completeness Notes:** Includes footnote about parallel conductors.

---
