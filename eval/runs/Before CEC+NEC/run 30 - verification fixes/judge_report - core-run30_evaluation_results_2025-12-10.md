# Judge Report - core-run30_evaluation_results_2025-12-10

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | CEC Lang Agent (qwen/qwen3-32b) |
| **Source File** | core-run30_evaluation_results_2025-12-10.md |
| **Judge** | Claude Code (Opus) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-10T20:05:00 |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 27 |
| **Total Score** | 253 / 270 |
| **Percentage** | 93.7% |
| **Avg Accuracy** | 4.67 / 5 |
| **Avg Completeness** | 4.70 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 20 |
| High (8-9/10) | 2 |
| Medium (5-7/10) | 5 |
| Low (0-4/10) | 0 |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| baseline-002 | What size copper conductor is required for a 60A circuit at 75°C? | 5/5 | 5/5 | 10/10 |
| baseline-003 | Where is GFCI protection required in a residential kitchen? | 4/5 | 4/5 | 8/10 |
| baseline-004 | Is AFCI protection required for bedroom circuits in new residential construction? | 5/5 | 5/5 | 10/10 |
| baseline-005 | Can aluminum conductors be used for a 200A service? If yes, what size? | 5/5 | 5/5 | 10/10 |
| baseline-006 | What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel? | 5/5 | 5/5 | 10/10 |
| baseline-007 | How many 20-ampere small appliance branch circuits are required for a kitchen? | 5/5 | 5/5 | 10/10 |
| baseline-008 | Is surge protection required for a new 200A residential service according to 2023 NEC? | 5/5 | 5/5 | 10/10 |
| core-001 | Service upgrade sizing - service conductors for 200A | 5/5 | 5/5 | 10/10 |
| core-002 | Multiwire branch circuit breaker and neutral requirements | 3/5 | 4/5 | 7/10 |
| core-003 | Where is GFCI protection required in residential dwelling per 2023 NEC? | 5/5 | 4/5 | 9/10 |
| core-004 | Is surge protection required for new 200A residential service? | 5/5 | 5/5 | 10/10 |
| core-005 | Panel in closet with 24" clearance - NEC compliance | 4/5 | 3/5 | 7/10 |
| core-006 | Two 12 AWG conductors on single breaker terminal - code violation? | 5/5 | 5/5 | 10/10 |
| core-007 | Detached garage subpanel grounding and bonding configuration | 5/5 | 5/5 | 10/10 |
| core-008 | Main bonding jumper vs system bonding jumper | 5/5 | 5/5 | 10/10 |
| core-009 | Small appliance branch circuits - kitchen and dining room | 5/5 | 5/5 | 10/10 |
| core-010 | Adjusted ampacity calculation (50°C, 6 conductors) | 5/5 | 5/5 | 10/10 |
| core-011 | Why does NEC require AFCI for bedrooms and living areas? | 5/5 | 5/5 | 10/10 |
| core-012 | Why are torque specifications important? | 5/5 | 5/5 | 10/10 |
| inspection-001 | Service load calculation for 200A residential panel | 2/5 | 3/5 | 5/10 |
| inspection-002 | Panel inspection - working space violations | 5/5 | 5/5 | 10/10 |
| inspection-005 | Kitchen circuit protection requirements (GFCI/AFCI) | 3/5 | 4/5 | 7/10 |
| inspection-006 | Subpanel grounding violations in detached garage | 5/5 | 5/5 | 10/10 |
| inspection-007 | Maximum 10 AWG THHN conductors in 1¼" RMC | 5/5 | 5/5 | 10/10 |
| inspection-008 | Voltage drop calculation | 5/5 | 5/5 | 10/10 |
| inspection-009 | Adjusted ampacity calculation (TW in attic at 43°C) | 5/5 | 5/5 | 10/10 |
| inspection-010 | GEC sizing for parallel service conductors | 5/5 | 5/5 | 10/10 |

---

## Detailed Results

### baseline-002
**Question:** What size copper conductor is required for a 60A circuit at 75°C?

**Agent Answer:** 6 AWG copper with 65A ampacity at 75°C per CEC Table 310.16. Notes that 8 AWG is insufficient (50A) and includes overcurrent protection per 240.4(D).

**Expected Answer:** 6 AWG copper

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct conductor size with proper table reference.
**Completeness Notes:** Provides additional helpful context about 8 AWG being insufficient and 240.4(D) requirements.

---

### baseline-003
**Question:** Where is GFCI protection required in a residential kitchen?

**Agent Answer:** GFCI required for countertop receptacles per Section 210.8(A)(6), receptacles within 6 ft of sink per 210.8(A)(7). Mentions 15- and 20-ampere circuits.

**Expected Answer:** All receptacles serving kitchen countertop surfaces shall have GFCI protection. Additionally, dishwashers require GFCI protection.

**Score:** 8/10 (Accuracy: 4/5, Completeness: 4/5)
**Accuracy Notes:** Correct on countertops but doesn't explicitly mention dishwasher GFCI requirement.
**Completeness Notes:** Missing explicit dishwasher GFCI mention which is required per current code.

---

### baseline-004
**Question:** Is AFCI protection required for bedroom circuits in new residential construction?

**Agent Answer:** Yes, per CEC 2022 Section 210.12(A) for all 120V, single-phase, 15- and 20-ampere branch circuits. Lists acceptable protection methods and notes exceptions don't apply to new construction.

**Expected Answer:** Yes, AFCI protection is required for all 120-volt, 15- and 20-ampere branch circuits supplying outlets in bedrooms.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct answer with proper code reference.
**Completeness Notes:** Comprehensive answer with additional helpful details about protection methods.

---

### baseline-005
**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Agent Answer:** Yes, 4/0 AWG aluminum at 75°C per CEC Table 310.12(A). Notes table is specific to dwelling units.

**Expected Answer:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct size and proper table reference.
**Completeness Notes:** Provides additional context about table applicability.

---

### baseline-006
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Agent Answer:** 3 feet (900 mm) per CEC Table 110.26(A)(1) for Condition 1.

**Expected Answer:** 36 inches (3 feet)

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct depth with proper table reference.
**Completeness Notes:** Includes metric conversion and condition explanation.

---

### baseline-007
**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen?

**Agent Answer:** Minimum of 2 20-ampere circuits per NEC 210.11(C)(1) and CEC 220.52(A).

**Expected Answer:** Minimum of two 20-ampere small appliance branch circuits

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct number with proper code references.
**Completeness Notes:** Complete answer with California-specific notes.

---

### baseline-008
**Question:** Is surge protection required for a new 200A residential service according to 2023 NEC?

**Agent Answer:** Yes, per NEC 2023 Section 230.67(A). Lists applicability, installation location, and informational notes.

**Expected Answer:** Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD).

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct with proper code section.
**Completeness Notes:** Provides additional helpful details about installation requirements.

---

### core-001
**Question:** A homeowner wants to upgrade from 100A to 200A service. What size service conductors are required, and can they use aluminum?

**Agent Answer:** 2/0 AWG copper or 4/0 AWG aluminum per Table 310.12(A). Notes California EV requirements for new construction.

**Expected Answer:** 2/0 AWG copper OR 4/0 AWG aluminum. Yes, aluminum is permitted per Table 310.12.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct sizes for both conductor types.
**Completeness Notes:** Includes additional relevant context about California requirements.

---

### core-002
**Question:** Multiwire branch circuit requirements for circuit breaker and neutral termination.

**Agent Answer:** Requires 2-pole circuit breaker for simultaneous disconnection per 210.4(B). States single-pole breakers with handle ties are NOT permitted. Neutral sized per 210.4(D).

**Expected Answer:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B).

**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** INCORRECT statement that handle ties are not permitted. NEC 210.4(B) explicitly allows handle ties OR common trip breakers for MWBCs.
**Completeness Notes:** Otherwise comprehensive but the handle tie error is significant.

---

### core-003
**Question:** Where is GFCI protection now required in a residential dwelling according to 2023 NEC?

**Agent Answer:** Lists: bathrooms, garages, outdoors, crawl spaces, kitchens, areas with sinks (6ft), bathtubs/showers, laundry areas, damp/wet locations, boathouses.

**Expected Answer:** Bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens, laundry areas, utility rooms with sinks, boathouses, bathtubs/shower stalls, within 6 feet of sinks.

**Score:** 9/10 (Accuracy: 5/5, Completeness: 4/5)
**Accuracy Notes:** All listed locations are correct.
**Completeness Notes:** Missing explicit mention of "unfinished basements" as a specific category.

---

### core-004
**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Agent Answer:** Yes per 230.67(A). Type 1 or Type 2 SPDs. Can be integral to service equipment, immediately adjacent, or next level downstream per exception.

**Expected Answer:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to service equipment or immediately adjacent. Exception allows first downstream panelboard.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All installation options correctly identified.
**Completeness Notes:** Complete coverage of requirements and exceptions.

---

### core-005
**Question:** Panel in closet with 24 inches clearance in front, water heater 18 inches to side. Does this meet NEC requirements?

**Agent Answer:** Does not meet requirements. Identifies depth violation (36" required vs 24" actual). Discusses Condition 1 vs 2 considerations.

**Expected Answer:** No - violates: (1) 36" depth required; (2) panels prohibited in clothes closets per 240.24(D); (3) 30" width required; (4) no storage in working space per 110.26(B).

**Score:** 7/10 (Accuracy: 4/5, Completeness: 3/5)
**Accuracy Notes:** Correctly identifies depth violation but misses clothes closet prohibition (240.24(D)) and storage prohibition (110.26(B)).
**Completeness Notes:** Missing several important violations that should be cited.

---

### core-006
**Question:** Two 12 AWG conductors on single 20A breaker terminal not marked for two conductors. Code violation?

**Agent Answer:** Yes, violation per 408.41 and 110.14(A). Discusses exception for parallel conductors (not applicable for 12 AWG).

**Expected Answer:** Yes, violation per 110.14(A). Terminals accommodate only one conductor unless identified for more.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct identification of violation with proper code references.
**Completeness Notes:** Provides additional context about parallel conductor exception.

---

### core-007
**Question:** Detached garage with 4-wire feeder - grounding and bonding configuration in subpanel.

**Agent Answer:** Local grounding electrode required per 250.32(A). EGC from 4-wire feeder to grounding bus. Neutral and ground separation. Neutral isolated from enclosure. Includes diagram.

**Expected Answer:** Grounds and neutrals SEPARATED in subpanel. NO main bonding jumper. Neutral bar isolated. EGC bonded to enclosure. Grounding electrode may be required per 250.32.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All key points correctly covered.
**Completeness Notes:** Excellent comprehensive answer with helpful diagram.

---

### core-008
**Question:** Difference between main bonding jumper and system bonding jumper. When is each required?

**Agent Answer:** MBJ at service connects grounded conductor to EGC per 250.28. SBJ at separately derived systems per 250.168. Sizing per Table 250.102(C)(1). Includes comparison table.

**Expected Answer:** MBJ at service equipment per 250.28. SBJ at separately derived systems per 250.30. Neither used in subpanels.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Accurate definitions and applications.
**Completeness Notes:** Excellent comprehensive response with sizing requirements.

---

### core-009
**Question:** How many 20-ampere small appliance branch circuits for kitchen? Can they serve dining room?

**Agent Answer:** Two 20A circuits per 210.52(B)(1). Yes, can serve dining room, pantry, breakfast room. Cannot serve more than one kitchen.

**Expected Answer:** Minimum TWO 20A circuits per 210.11(C)(1). Yes, can serve dining room, pantry, breakfast room. Cannot serve lighting or receptacles outside these areas.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct on all counts.
**Completeness Notes:** Covers all key requirements.

---

### core-010
**Question:** Six 12 AWG THHN conductors in conduit at 50°C. Adjusted ampacity?

**Agent Answer:** Base 30A at 90°C. Temp correction 0.82 for 50°C. Bundling 0.80 for 6 conductors. 30 × 0.82 × 0.80 = 19.68A → 19A (rounded down per 310.15(B)(2)(a)).

**Expected Answer:** Base 30A at 90°C. Temp correction 0.82. Bundling 0.80. 30 × 0.82 × 0.80 = 19.68A, approximately 20A.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Perfect calculation with all correct factors. Agent's rounding to 19A is actually more correct per 310.15(B)(2)(a) which requires rounding down.
**Completeness Notes:** Shows all steps clearly with table references.

---

### core-011
**Question:** Why does NEC require AFCI for bedrooms and living areas? What hazard does it prevent?

**Agent Answer:** AFCIs detect and interrupt arc faults which cause fires. Lists causes: damaged wiring, loose connections, overloaded circuits, rodent damage.

**Expected Answer:** AFCI prevents electrical fires from arc faults. Detects series/parallel arcing, loose connections, damaged insulation.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct explanation of hazard prevention.
**Completeness Notes:** Comprehensive coverage of arc fault causes.

---

### core-012
**Question:** Why are torque specifications important for conductor terminations?

**Agent Answer:** Ensures secure low-resistance connections. Loose = heat/fire hazard, over-torqued = damage. Requirements in 110.14(D), UL 486A-486B, 430.9(C).

**Expected Answer:** Prevents loose connections (fire hazard), poor contact (arcing), overtightening (damage). Requirements in 110.14(D), Table 110.14(D), 110.3(B).

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct explanation of importance.
**Completeness Notes:** Comprehensive with additional code references.

---

### inspection-001
**Question:** Service load calculation for 200A panel with specific loads.

**Agent Answer:** General load 13,500 VA. Range 8000 VA, dryer 5500 VA, AC 4600 VA. Total before demand 21,600 VA. Applies 100%/40% demand factor. Final: 14,640 VA ÷ 240V = 61A. 200A adequate.

**Expected Answer:** General load 13,500 VA with Table 220.42 demand (first 3000 at 100% = 3000, remaining 10500 at 35% = 3675). Range 8000 VA, dryer 5500 VA, AC 4600 VA. Total: 24,775 VA ÷ 240V = 103.2A.

**Score:** 5/10 (Accuracy: 2/5, Completeness: 3/5)
**Accuracy Notes:** INCORRECT methodology. The agent applied a 100%/40% demand factor to the total combined load instead of applying Table 220.42 demand factors specifically to the general lighting/receptacle load. The expected approach yields 103.2A while the agent got 61A - a significant difference.
**Completeness Notes:** Shows work but uses wrong approach to demand factors.

---

### inspection-002
**Question:** Panel inspection - 30" width, 28" depth, water heater 16" to side. Identify violations.

**Agent Answer:** Identifies depth violation (28" < 36" required). Water heater obstruction in working space. Potential headroom violation if ceiling < 6.5'.

**Expected Answer:** Depth 28" < 36" required - violation. Water heater at 16" within 30" width - prohibited per 110.26(B) - violation.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All violations correctly identified.
**Completeness Notes:** Thorough analysis including potential headroom issue.

---

### inspection-005
**Question:** Kitchen circuit protection requirements for countertop, dishwasher, disposal, refrigerator.

**Agent Answer:** Countertop: AFCI/GFCI. Dishwasher: AFCI/GFCI. Disposal: AFCI/GFCI. Refrigerator: AFCI only (claims GFCI exception under 210.8(A) Exception No. 2).

**Expected Answer:** All circuits need AFCI/GFCI combo per NEC 2023 210.8(A)(5) which covers ALL kitchen receptacles including refrigerators.

**Score:** 7/10 (Accuracy: 3/5, Completeness: 4/5)
**Accuracy Notes:** INCORRECT on refrigerator. NEC 2023 expanded 210.8(A)(5) to require GFCI for ALL kitchen receptacles - there is no exemption for refrigerators in 2023 NEC.
**Completeness Notes:** Otherwise comprehensive but refrigerator error is significant.

---

### inspection-006
**Question:** Subpanel grounding violations in detached garage.

**Agent Answer:** Identifies violations: neutral/ground bonded, neutral to enclosure, MBJ installed. Provides correct configuration with code references.

**Expected Answer:** Neutral bonded to enclosure - violation. MBJ installed - violation (only at service). Correct: remove bonds, isolate neutral, ground bar to enclosure only.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** All violations correctly identified.
**Completeness Notes:** Excellent detailed explanation with correct configuration.

---

### inspection-007
**Question:** Maximum 10 AWG THHN conductors in 1¼" RMC.

**Agent Answer:** 40% of 1.526 sq in = 0.6104 sq in. 10 AWG THHN = 0.0211 sq in. 0.6104 ÷ 0.0211 = 28.91 → 28 conductors. Verification shows 38.7% fill.

**Expected Answer:** 0.610 ÷ 0.0211 = 28.91 → 29 per Note 7 (0.91 > 0.8). Conservative practice: 28.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct calculation. Agent chose conservative 28 which is acceptable.
**Completeness Notes:** Includes verification step showing fill percentage.

---

### inspection-008
**Question:** Voltage drop calculation for 120V circuit with 22A continuous load, 50 ft one-way.

**Agent Answer:** VD = 2 × 22 × 1.29 × 50/1000 = 2.838V. % = 2.838/120 × 100 = 2.365%. Meets 3% per 210.19(A).

**Expected Answer:** VD = 2.84V. % = 2.37%. Yes, meets 3% recommendation.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Perfect calculation.
**Completeness Notes:** Complete with code reference.

---

### inspection-009
**Question:** Adjusted ampacity for 12 AWG TW in attic at 43°C with 6 conductors.

**Agent Answer:** Base 20A at 60°C. Temp correction 0.71 for 43°C. Bundling 0.80 for 6 conductors. 20 × 0.71 × 0.80 = 11.36A → 11A.

**Expected Answer:** Base 20A. Temp correction 0.71. Bundling 0.80. 20 × 0.71 × 0.80 = 11.36A (43% reduction).

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Perfect calculation with all correct factors.
**Completeness Notes:** All steps shown with table references.

---

### inspection-010
**Question:** GEC sizing for 4 × 250 kcmil copper parallel service conductors.

**Agent Answer:** 4 × 250 = 1000 kcmil. GEC = 2/0 AWG copper per Table 250.66.

**Expected Answer:** For 1000 kcmil (Over 600 through 1100 kcmil row), minimum 2/0 AWG copper or 4/0 aluminum.

**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** Correct GEC size with proper table reference.
**Completeness Notes:** Includes method for calculating parallel conductor equivalent.

---
