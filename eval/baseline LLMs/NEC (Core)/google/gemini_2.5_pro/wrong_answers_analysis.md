# Gemini 2.5 Pro Wrong Answer Analysis

**Judge:** Claude Code (Claude Opus 4.5)
**Method:** LLM-as-Judge
**Overall Score:** 93.93% (263/280)

---

## Executive Summary

**Questions with Errors:** 11 of 28 (39.3%)

**Key Error Pattern:** Gemini 2.5 Pro demonstrates exceptional performance on baseline and core NEC knowledge questions, achieving near-perfect scores on 17 of 28 questions. However, the model struggles with complex multi-step calculations, particularly when NEC-specific table lookups are required (e.g., Table 220.55 for range demand, Table C.8 for conduit fill). The model shows strong conceptual understanding but occasionally makes computational errors or relies on incorrect table values.

**Most Critical Error:** Conduit fill calculation (inspection-007) - Model answered 18 conductors when the correct answer is 28-29, a 37% error that could lead to code violations if followed in practice.

**Strengths:**
- Excellent understanding of GFCI/AFCI requirements (2023 NEC updates)
- Strong grounding and bonding knowledge (detached garage subpanel configuration)
- Comprehensive coverage of working clearance requirements
- Clear explanations with NEC references
- Very thorough answers that go beyond minimum requirements

---

## Detailed Error Analysis (11 of 28)

### 1. baseline-001: Table Lookup (Score: 7/10)

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Model's Answer:** 25 amperes (from Table 310.16, 75°C column), then explains the 20A overcurrent protection limit per 240.4(D).

**Correct Answer:** 20 amperes

**What the Model Did Wrong:** The model answered with the technical ampacity (25A) rather than the practical overcurrent protection limit (20A) that the expected answer was seeking. However, the model did explain both values correctly.

**Root Cause:** Answer format interpretation - the model provided technically correct information (25A is the ampacity) but didn't match the expected simplified answer format. This is a minor issue as the model demonstrated full understanding by explaining the 240.4(D) small conductor rule.

---

### 2. core-002: Multiwire Branch Circuit (Score: 9/10)

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Model's Answer:** Requires 2-pole breaker or handle tie for simultaneous disconnect (210.4(B)). Neutral must be pigtailed per 300.13(B). Recommends 2-pole AFCI/GFCI for kitchen MWBCs.

**Correct Answer:** Requires either handle tie or common trip breaker. Common trip is required if circuit has both line-to-line and line-to-neutral loads. Neutral must be continuous and pigtailed. Circuit breaker: 20A maximum for 12 AWG copper.

**What the Model Did Wrong:** Doesn't explicitly distinguish when common trip (vs handle tie) is mandatory for line-to-line loads.

**Root Cause:** The model correctly explained the simultaneous disconnect requirement but missed the nuance that common trip (not just handle tie) is required when the MWBC serves both 240V line-to-line loads AND 120V line-to-neutral loads simultaneously. This is a subtle but important distinction in 210.4(B).

---

### 3. core-005: Panel in Closet with Clearance Issues (Score: 8/10)

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Model's Answer:** Violations: (1) 24" depth vs required 36", (2) water heater within working space. Mentions closet prohibition with qualification ("if the space is primarily used for storing clothes").

**Correct Answer:** No. Violations: (1) Minimum 36" depth required per 110.26(A)(1), not 24". (2) Panels prohibited in clothes closets per 240.24(D). (3) Working space width must be 30" or equipment width. (4) No storage allowed in working space per 110.26(B).

**What the Model Did Wrong:** Didn't explicitly cite 110.26(B) as a separate violation for equipment/storage in working space. Also qualified the closet prohibition rather than stating it directly.

**Root Cause:** The model correctly identified the key violations but was appropriately cautious about the closet prohibition (since "closet with water heater" could be a utility closet, not a clothes closet). The 110.26(B) storage prohibition should have been called out as a distinct violation.

---

### 4. inspection-001: Service Load Calculation (Score: 7/10) ⚠️ CRITICAL

**Question:** Residential panel inspection: 200A main breaker with 12kW electric range, 5.5kW dryer, two 20A small appliance circuits, one 20A laundry circuit, 3000 sq ft living space, 4-ton central AC. Calculate the service load per NEC Article 220.

**Model's Answer:** Used Optional Method 220.82. Calculated: General lighting 9000 VA, small appliance 3000 VA, laundry 1500 VA, range 12,000 VA (full nameplate), dryer 5500 VA. Applied demand factors, added AC load. Final: 95.87A.

**Correct Answer:** General lighting: 3000 sq ft × 3 VA = 9000 VA. Small appliance: 3000 VA. Laundry: 1500 VA. Subtotal: 13,500 VA. Apply demand factor per Table 220.42: first 3000 VA at 100% = 3000 VA, remaining 10,500 VA at 35% = 3675 VA. Subtotal with demand: 6675 VA. Range: 8000 VA (per Table 220.55 for one range). Dryer: 5500 VA. AC: 4600 VA. Total: 24,775 VA ÷ 240V = 103.2A.

**What the Model Did Wrong:**
1. Used full 12kW range nameplate rating instead of 8kW from Table 220.55
2. Calculated 95.87A instead of expected 103.2A (7.4A error)
3. Missed mandatory Table 220.55 range demand factor

**Root Cause:** The model applied the Optional Method correctly but failed to apply Table 220.55 for range demand. NEC 220.55 provides specific demand factors for household cooking appliances - for one range rated 12kW or less, the demand load is 8kW, not the full nameplate rating. This is a mandatory table lookup that the model missed, resulting in underestimating the service load. This error is concerning because it could lead to undersizing service equipment in practice.

---

### 5. inspection-002: Panel Clearance Violations (Score: 7/10)

**Question:** Electrical panel inspection in residential garage: Panel has 30" width clearance, 28" depth clearance, water heater 16" to left side, panel at 5 feet height. Identify ALL NEC violations.

**Model's Answer:** Violations: (1) 28" depth vs required 36" per 110.26(A)(1), (2) water heater within 30" working space per 110.26(B), (3) panel mounted too high - assumes 42" panel height would place top breakers at 8'6" exceeding 6'7" maximum.

**Correct Answer:** Violations: (1) Depth clearance is 28" but 110.26(A)(1) requires minimum 36". (2) Water heater at 16" is within the 30" width working space - equipment not related to electrical installation is prohibited in working space per 110.26(B).

**What the Model Did Wrong:** Added a speculative height violation based on assumed panel dimensions (42" tall) not provided in the question. A panel bottom at 5 feet with typical 30-40" height would have top breakers at 90-100", which could still be under the 79" maximum depending on actual panel size.

**Root Cause:** The model made an assumption about panel dimensions not given in the question to create a third violation. The expected answer correctly focused on the two clear violations: insufficient depth and obstruction in working space. The model should have identified the actual violations without speculation.

---

### 6. inspection-005: Kitchen Circuit Protection (Score: 9/10)

**Question:** New residential construction, 2023 NEC. Kitchen has countertop receptacles, dishwasher, garbage disposal, and refrigerator on separate circuits. Specify required protection.

**Model's Answer:** All circuits require combination AFCI/GFCI. Countertops: 210.12(B)(1) + 210.8(A)(6). Dishwasher: 210.12(B)(1) + 210.8(D)(7). Disposal: 210.12(B)(1) + 210.8(A)(6) (receptacle in kitchen). Refrigerator: 210.12(B)(1) + 210.8(A)(6).

**Correct Answer:** Countertops: Combo AFCI/GFCI. Dishwasher: Combo AFCI/GFCI per 210.8(D) + 210.12(A). Disposal: GFCI not specifically required, but AFCI required per 210.12(A). Refrigerator: Standard AFCI (GFCI not required).

**What the Model Did Wrong:** For garbage disposal, model says GFCI required via 210.8(A)(6) receptacle rule, but expected answer says GFCI not specifically required for disposal.

**Root Cause:** This is a reasonable interpretation difference. If the disposal is plug-in (on a receptacle), the model's answer is correct per 210.8(A)(6) (all receptacles in kitchen). If hardwired, the expected answer is more accurate. The expected answer is more nuanced, recognizing that 210.8(D) doesn't specifically list garbage disposals unlike dishwashers.

---

### 7. inspection-007: Conduit Fill Calculation (Score: 5/10) ⚠️ CRITICAL

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors. Determine the maximum number of conductors.

**Model's Answer:** 18 conductors (per Table C.8). Shows calculation: 0.607 in² ÷ 0.0211 in² = 28.77, but then defaults to Table C.8 value of 18 without explaining the discrepancy.

**Correct Answer:** Per Table 1: Maximum 40% fill. From Table 4: 1¼" RMC has 0.610 in² at 40% fill. From Table 5: 10 AWG THHN = 0.0211 in². Calculation: 0.610 ÷ 0.0211 = 28.91 conductors. Per Note 7: round up when decimal is 0.8 or larger. Maximum is 29 conductors (conservatively 28).

**What the Model Did Wrong:**
1. Final answer of 18 vs correct 28-29 conductors (37% error)
2. Calculation shown (0.607/0.0211 = 28.77) contradicts stated answer (18)
3. Relied on Table C.8 without verifying against manual calculation

**Root Cause:** The model appears to have used an incorrect Table C.8 value (or possibly confused conduit types - 1" RMC vs 1¼" RMC). The manual calculation the model partially showed (28.77) is very close to the correct answer (28.91), but the model then defaulted to the Table C.8 value of 18 without recognizing the massive discrepancy. This is a critical error - installing only 18 conductors when 28-29 are permitted wastes conduit space and increases project costs. Conversely, if the model's answer were used to overfill, it could lead to code violations.

---

### 8. inspection-008: Voltage Drop Calculation (Score: 8/10)

**Question:** A 120V circuit supplies 22A continuous load using 12 AWG copper (1.29 Ω/1000 ft). One-way distance is 50 feet. Calculate voltage drop.

**Model's Answer:** Discusses both 22A and 27.5A (125% for continuous). States "we will use 22A for the calculation." Shows VD = 22A × 0.129Ω but calculates 2.56-2.58V (2.13-2.15%).

**Correct Answer:** VD = (2 × L × R × I) / 1000 = (2 × 50 × 1.29 × 22) / 1000 = 2.84V. Percentage: (2.84V / 120V) × 100 = 2.37%. Yes, meets NEC 3% recommendation.

**What the Model Did Wrong:**
1. Calculated 2.56-2.58V vs expected 2.84V (about 10% low)
2. Calculation inconsistency - stated will use 22A but appears to calculate with ~20A
3. Final percentage: 2.13-2.15% vs expected 2.37%

**Root Cause:** The model correctly calculated R_total = 100ft/1000 × 1.29 = 0.129Ω. Using 22A, the result should be 22A × 0.129Ω = 2.838V ≈ 2.84V. However, the model appears to have used approximately 20A in the final calculation instead of the stated 22A, resulting in ~2.58V. The confusion arose from discussing multiple current values (22A actual, 27.5A for protection sizing) and then using the wrong value in the final calculation.

---

### 9. inspection-009: Ampacity Derating Calculation (Score: 9/10)

**Question:** A conduit in an attic contains six 12 AWG TW (60°C) copper conductors. Attic temperature reaches 110°F (43°C). Calculate adjusted ampacity.

**Model's Answer:** Initial statement says "12.8 amperes" but step-by-step calculation shows: Base 20A (60°C) × 0.71 (temp correction) × 0.80 (bundling) = 11.36A. Recalculates to confirm 11.36A. Discusses 10A breaker requirement.

**Correct Answer:** Base ampacity: 20A at 60°C. Temperature correction: 0.71 for 43°C (41-45°C range in 60°C column). Bundling adjustment: 0.80 for 6 conductors. Adjusted ampacity = 20A × 0.71 × 0.80 = 11.36 amperes.

**What the Model Did Wrong:** Initial statement claims "12.8 amperes" which contradicts the subsequent calculation showing 11.36A.

**Root Cause:** The model has an internal inconsistency where it states one answer (12.8A) initially, then shows a complete, correct calculation arriving at 11.36A. The calculation is correct and matches the expected answer exactly. The initial 12.8A appears to be an error in the summary statement that was corrected in the detailed work. Minor issue as the calculation methodology and final answer (11.36A) are correct.

---

### 10. Multiple Minor Deductions (Score: 8-9/10 each)

Several questions received minor deductions for completeness or minor interpretation differences:

- **baseline-001**: Gave ampacity (25A) vs overcurrent limit (20A), though both are technically correct
- **core-002**: Didn't explicitly distinguish when common trip vs handle tie is mandatory
- **core-005**: Didn't cite 110.26(B) as separate violation; qualified closet prohibition
- **inspection-005**: Minor interpretation difference on disposal GFCI requirement (plug-in vs hardwired)
- **inspection-009**: Initial statement error (12.8A) corrected in calculation

These are minor issues that don't significantly impact the overall quality of the responses.

---

## Error Pattern Summary

| Error Type | Count | Severity | Examples |
|------------|-------|----------|----------|
| **NEC Table Lookup Errors** | 2 | High | Table 220.55 (range demand), Table C.8 (conduit fill) |
| **Calculation Inconsistencies** | 2 | Medium | Voltage drop (wrong current), derating (initial vs calculated) |
| **Interpretation/Format** | 4 | Low | Answer format, disposal GFCI, closet qualification, 110.26(B) |
| **Speculative Violations** | 1 | Low | Panel height assumption |
| **Nuance/Detail Missing** | 2 | Low | Common trip distinction, separate violation citation |

### Key Patterns:

1. **Strong Baseline Performance**: 8 of 8 baseline questions scored 7-10/10 (avg 9.6/10)
2. **Excellent Core Knowledge**: 12 of 12 core questions scored 8-10/10 (avg 9.6/10)
3. **Weakness in Complex Calculations**: 4 of 8 inspection questions had significant errors in calculations requiring multiple NEC table lookups
4. **Outstanding Explanations**: Model consistently provides thorough, well-referenced answers with NEC citations
5. **Table Lookup Reliability**: When calculations require specific NEC table values (220.55, C.8), the model sometimes uses incorrect values

### Recommendations for Improvement:

1. **Verify NEC Table Lookups**: Implement additional verification for critical table values, especially Table 220.55 (cooking appliances), Chapter 9 Tables (conduit fill)
2. **Calculation Consistency**: Ensure stated values match calculated values throughout the answer
3. **Avoid Speculation**: Don't add violations based on assumptions not given in the problem
4. **Cross-Check Calculations**: When manual calculation contradicts table lookup (e.g., 28.77 vs 18), flag for verification

---

## Overall Assessment

Gemini 2.5 Pro demonstrates **excellent NEC knowledge** with a 93.93% overall score. The model excels at:

- GFCI/AFCI requirements (2023 NEC updates) - perfect accuracy
- Grounding and bonding concepts - perfect accuracy
- Working clearance requirements - strong performance
- Explaining "why" questions with conceptual understanding
- Providing comprehensive answers with proper NEC references

The model's weaknesses are primarily in:

- Complex multi-step load calculations requiring Table 220.55
- Conduit fill calculations using Chapter 9 Tables
- Maintaining consistency between stated and calculated values
- Avoiding speculative assumptions not in the problem

Despite these calculation errors, the model would be highly valuable for:

- Educational purposes (explains concepts thoroughly)
- Code interpretation questions (strong understanding of requirements)
- Preliminary design work (with calculation verification)

For critical applications (inspection, final design), calculations should be independently verified, particularly for service load calculations and conduit fill.
