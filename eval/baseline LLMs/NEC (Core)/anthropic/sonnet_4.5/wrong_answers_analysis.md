# Claude Sonnet 4.5 Wrong Answer Analysis

**Judge:** Claude Code (Claude Opus 4.5)
**Method:** LLM-as-Judge
**Date:** December 9, 2025
**Overall Score:** 96.92% (252/260)

---

## Executive Summary

**Questions with Errors:** 2 of 26 evaluated questions (scores below 10/10)

**Overall Performance:** Excellent. Claude Sonnet 4.5 achieved 96.92% accuracy on this NEC evaluation, demonstrating strong electrical code knowledge and reasoning.

**Key Error Pattern:** Service conductor sizing using wrong NEC table. The model consistently used Table 310.15(B)(16) for service conductor ampacity instead of the correct Table 310.12, leading to undersized aluminum conductor recommendations (3/0 AWG instead of 4/0 AWG for 200A service).

**Most Critical Error:** Questions baseline-005 and core-001 both involved specifying aluminum service conductor size as 3/0 AWG instead of 4/0 AWG. This could result in dangerous undersized service installations in the field.

**Strengths:**
- Excellent performance on complex calculations (load calculations, derating, voltage drop, conduit fill)
- Strong understanding of GFCI/AFCI requirements and 2023 NEC updates
- Comprehensive grasp of grounding and bonding concepts
- Accurate knowledge of clearance requirements and code violations
- Detailed, well-explained answers with proper code references

---

## Detailed Error Analysis (2 of 26)

### 1. baseline-005: Aluminum Service Conductor Sizing (Score: 6/10)

**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Model's Answer:** "Yes, aluminum conductors can be used for a 200A service. For a 200-ampere service using aluminum or copper-clad aluminum conductors at 75C termination, you would need: **3/0 AWG** (also written as 000 AWG) aluminum or copper-clad aluminum. According to NEC Table 310.15(B)(16), the ampacity ratings at 75C are: 2/0 AWG aluminum: 180 amperes, 3/0 AWG aluminum: 200 amperes, 4/0 AWG aluminum: 230 amperes..."

**Correct Answer:** Yes, **4/0 AWG** aluminum or copper-clad aluminum per Table 310.12.

**What the Model Did Wrong:**
1. Specified 3/0 AWG aluminum instead of 4/0 AWG
2. Referenced Table 310.15(B)(16) instead of Table 310.12 for service conductors

**Root Cause:** The model used the wrong NEC table. Service conductors (Article 230) should be sized using Table 310.12, which provides simplified ampacity ratings specifically for service conductors. Table 310.15(B)(16) is for general branch circuit and feeder conductors. While 3/0 AWG aluminum has a 200A ampacity in Table 310.15(B)(16), Table 310.12 requires 4/0 AWG for 200A service.

**Safety Impact:** High. This could result in undersized service conductors being installed, creating a fire hazard.

**Scores:** Accuracy: 2/5 (significant error), Completeness: 4/5 (good explanation but wrong answer)

---

### 2. core-001: 200A Service Upgrade with Aluminum (Score: 6/10)

**Question:** A homeowner wants to upgrade from 100A to 200A service. The house has 3,000 sq ft of living space, electric range (12kW), electric dryer (5.5kW), central AC (4 tons), and electric water heater (4.5kW). What size service conductors are required, and can they use aluminum?

**Model's Answer:** "...For aluminum service conductors at 75C, you would need **3/0 AWG aluminum** (or copper-clad aluminum). According to Table 310.15(B)(16): 2/0 AWG aluminum: 180A, 3/0 AWG aluminum: 200A, 4/0 AWG aluminum: 230A. Since the service is 200 amperes, 3/0 AWG aluminum meets the requirement..."

**Correct Answer:** 2/0 AWG copper OR **4/0 AWG aluminum**. Yes, aluminum is permitted for service conductors per Table 310.12.

**What the Model Did Wrong:**
1. Specified 3/0 AWG aluminum instead of 4/0 AWG aluminum
2. Used Table 310.15(B)(16) instead of Table 310.12
3. Otherwise performed excellent load calculation work (correctly determined 200A service requirement)

**Root Cause:** Same systematic error as baseline-005. The model consistently applies the wrong table for service conductor sizing. This is a knowledge gap specifically about when to use Table 310.12 vs Table 310.15(B)(16).

**Safety Impact:** High. Despite excellent load calculation work, the final conductor sizing recommendation is dangerous.

**Scores:** Accuracy: 2/5 (critical sizing error despite good load calc), Completeness: 4/5 (thorough explanation)

---

### 3. core-002: Multiwire Branch Circuit Requirements (Score: 8/10)

**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?

**Model's Answer:** Provided thorough explanation of simultaneous disconnect requirement, neutral continuity, and conductor grouping per 210.4.

**Correct Answer:** Requires either a handle tie or common trip breaker to simultaneously disconnect all ungrounded conductors per 210.4(B). **Common trip is required if the circuit has both line-to-line and line-to-neutral loads.** Handle tie vs common trip distinction...

**What the Model Did Wrong:**
- Correctly identified the simultaneous disconnect requirement
- Was slightly vague on the distinction between when a handle tie is sufficient vs when common trip is specifically required
- Did not emphasize that common trip is mandatory when both line-to-line AND line-to-neutral loads are present

**Root Cause:** Nuance omission. The model understood the general requirement but didn't fully articulate the specific condition that triggers the common trip vs handle tie distinction.

**Safety Impact:** Low. The practical guidance is mostly correct; this is a fine-point nuance.

**Scores:** Accuracy: 4/5 (slightly vague on nuance), Completeness: 4/5 (main points covered)

---

## Error Pattern Summary

| Error Type | Count | Question IDs | Severity |
|------------|-------|--------------|----------|
| Wrong NEC table for service conductors | 2 | baseline-005, core-001 | **CRITICAL** |
| Incomplete nuance (handle tie vs common trip) | 1 | core-002 | Minor |

---

## Error Type Breakdown

### Critical Error: Service Conductor Table Confusion

**Pattern:** Model consistently uses Table 310.15(B)(16) for service conductor sizing instead of Table 310.12.

**Why This Matters:**
- Table 310.12 is specifically for service entrance conductors (Article 230)
- Table 310.15(B)(16) is for general branch circuits and feeders
- The tables have different ampacity values for the same conductor sizes
- Using the wrong table leads to undersized service conductors

**Correct Application:**
- **Service conductors (Article 230):** Use Table 310.12
- **Feeders and branch circuits (Articles 210, 215):** Use Table 310.15(B)(16) or 310.16

**Affected Questions:** baseline-005, core-001 (both 200A service sizing with aluminum)

**Recommendation:** The model needs specific training or prompting to distinguish between service conductor sizing (Table 310.12) and general conductor sizing (Table 310.15(B)(16)).

---

## Comparison to Expected Performance

### Strengths (Perfect Scores on These Categories):

1. **Simple Table Lookups:** 100% (baseline-001, baseline-002, baseline-006)
2. **AFCI/GFCI Requirements:** 100% (baseline-004, core-003, core-004, inspection-005)
3. **Grounding & Bonding:** 100% (core-007, core-008, inspection-006)
4. **Complex Calculations:** 100% (core-010, inspection-001, inspection-007, inspection-008)
5. **Clearance Requirements:** 100% (baseline-006, core-005, inspection-002)
6. **Code Violations:** 100% (core-005, core-006, inspection-002)
7. **2023 NEC Updates:** 100% (baseline-008, core-004)
8. **Conceptual Understanding:** 100% (core-011, core-012)

### Weaknesses:

1. **Service Conductor Sizing:** 0% (both service sizing questions failed with same error)
2. **Multi-requirement Questions:** Some omissions when multiple code sections apply

---

## Recommendations

### For Model Improvement:

1. **High Priority:** Add specific training on Table 310.12 vs Table 310.15(B)(16) distinction
   - When to use each table
   - Service conductor special rules
   - Article 230 vs Article 210/215 conductor sizing

2. **Low Priority:** Enhanced nuance detection for subtle code distinctions
   - Handle tie vs common trip requirements
   - When exceptions apply vs base rules

### For Users:

1. **Double-check service conductor sizing** - verify aluminum service conductor recommendations against Table 310.12
2. Model is highly reliable for: calculations, GFCI/AFCI requirements, grounding/bonding, clearances, code violations
3. Overall, model demonstrates inspector-grade knowledge with one systematic blind spot

---

## Conclusion

Claude Sonnet 4.5 demonstrates excellent NEC knowledge and reasoning ability, scoring 96.92% overall (252/260 points). The model excels at complex calculations, code violation identification, grounding/bonding concepts, and 2023 NEC updates.

The primary weakness is a systematic error in service conductor sizing, where the model consistently uses Table 310.15(B)(16) instead of Table 310.12, resulting in undersized aluminum conductor recommendations for 200A services (3/0 AWG instead of 4/0 AWG). This is a critical safety issue that should be addressed.

With correction of this single systematic error, the model would achieve near-perfect performance on this evaluation set (98.5%+).
