# Wrong Answers - core-run32_evaluation_results_2025-12-11.md

**Model:** qwen/qwen3-32b
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 81.1% (219/270)

---

## Executive Summary
**Questions with Errors:** 13 of 27
**Perfect Scores:** 14
**Critical Bug Identified:** Reflection replacing answers with "[VERIFIED]" message

---

## CRITICAL BUG - Reflection Answer Replacement

When reflection called additional tools and marked as "improved", the final answer was sometimes just `[VERIFIED] Answer is complete` without the actual content. This is a code bug in the reflection implementation.

**Affected Questions (Lost 21 points):**
- baseline-005: Answer about aluminum conductor size missing
- inspection-001: Load calculation completely missing
- inspection-010: GEC size answer missing
- core-011: Only summary, full explanation missing

---

## Detailed Error Analysis

### 1. baseline-005 (Score: 3/10) - REFLECTION BUG
**Question:** Can aluminum conductors be used for a 200A service? If yes, what size?

**Agent Answer:** `[VERIFIED] Answer is complete.`

**Expected Answer:** Yes, 4/0 AWG aluminum or copper-clad aluminum

**Accuracy:** 1/5 - No answer provided due to bug
**Completeness:** 2/5 - Critical information missing
**Root Cause:** Reflection bug - answer replaced by verification message

---

### 2. inspection-001 (Score: 3/10) - REFLECTION BUG
**Question:** Residential panel inspection: 200A main breaker... Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Agent Answer:** `[VERIFIED] Answer is complete.`

**Expected Answer:** Full load calculation showing:
- General lighting: 9000 VA (3000 sq ft × 3 VA)
- Apply Table 220.42 demand factors: first 3000 VA at 100%, remaining at 35%
- Range: 8000 VA per Table 220.55
- Total: ~103.2A, 200A service adequate

**Accuracy:** 1/5 - No calculation shown
**Completeness:** 2/5 - Question specifically asked to "show your work"
**Root Cause:** Reflection bug - entire calculation replaced by verification message

---

### 3. inspection-010 (Score: 3/10) - REFLECTION BUG
**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase. Determine the minimum size copper GEC required.

**Agent Answer:** `[VERIFIED] Answer is complete.`

**Expected Answer:** 2/0 AWG copper per Table 250.66 (for 1000 kcmil equivalent)

**Accuracy:** 1/5 - No GEC size given
**Completeness:** 2/5 - Table reference and answer missing
**Root Cause:** Reflection bug - answer replaced by verification message

---

### 4. core-009 (Score: 5/10) - WRONG ANSWER
**Question:** How many 20-ampere small appliance branch circuits are required for a kitchen, and can these circuits also serve the dining room receptacles?

**Agent Answer:** "**No**, the two required kitchen small appliance branch circuits **cannot** serve dining room receptacles."

**Expected Answer:** "**Yes**, these circuits can and should serve dining room, pantry, and breakfast room receptacles."

**Accuracy:** 2/5 - Dining room answer is completely backwards
**Completeness:** 3/5 - Got circuit count right (2 minimum)
**Specific Errors:**
- 210.52(B) explicitly permits serving dining room, pantry, breakfast room from kitchen small appliance circuits
- Agent stated the opposite of what the code requires

---

### 5. inspection-002 (Score: 6/10)
**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front...

**Agent Answer:** Required depth is 35.43 inches (900mm), panel mounting height of 5 feet is violation

**Expected Answer:** Required depth is 36 inches per 110.26(A)(1), panel height is NOT a violation (5 feet is acceptable)

**Accuracy:** 3/5 - Wrong depth (35.43" vs 36")
**Completeness:** 3/5 - Incorrectly identified height as violation
**Specific Errors:**
- Working space depth is 36 inches (3 feet), not 35.43 inches
- Panel at 5 feet height is not automatically a violation

---

### 6. core-011 (Score: 6/10) - PARTIAL BUG
**Question:** Why does the NEC require AFCI protection for bedrooms and living areas? What electrical hazard does it prevent?

**Agent Answer:** `[VERIFIED] Answer is complete. The answer addresses the requirement (CEC 2022 Section 210.12), explains the hazard (arc faults causing fires)...`

**Expected Answer:** Full explanation of arc faults - series arcing, parallel arcing, loose connections, deteriorated wire, fire prevention

**Accuracy:** 3/5 - Summary only, not full explanation
**Completeness:** 3/5 - Missing detailed arc fault types
**Root Cause:** Partial reflection bug - summary instead of full answer

---

### 7. inspection-005 (Score: 7/10)
**Question:** New residential construction, 2023 NEC. Kitchen installation... specify required protection for each circuit.

**Agent Answer:** Refrigerator requires "Standard AFCI" only, not GFCI

**Expected Answer:** ALL kitchen receptacles including refrigerator require GFCI per 2023 NEC 210.8(A)(5) expansion

**Accuracy:** 4/5 - Wrong on refrigerator GFCI
**Completeness:** 3/5 - Other circuits correctly identified
**Specific Errors:**
- NEC 2023 expanded 210.8(A)(5) to cover ALL kitchen receptacles
- Refrigerator MUST have GFCI protection in 2023 NEC

---

### 8. core-005 (Score: 7/10)
**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side.

**Agent Answer:** Front clearance meets requirements (said 20-30 inches range)

**Expected Answer:** Minimum 36 inches depth required per 110.26(A)(1), 24 inches is a VIOLATION

**Accuracy:** 4/5 - Closet violation correct, depth wrong
**Completeness:** 3/5 - Missing clear depth violation
**Specific Errors:**
- Working space depth is 36 inches minimum, not 20-30 inches
- 24 inches front clearance is a violation, not compliant

---

### 9. baseline-003 (Score: 8/10)
**Question:** Where is GFCI protection required in a residential kitchen?

**Agent Answer:** Countertop receptacles and within 6 feet of sink

**Expected Answer:** Countertop surfaces AND dishwasher

**Accuracy:** 4/5 - Countertop correct
**Completeness:** 4/5 - Missing dishwasher
**Specific Errors:**
- Does not mention dishwasher GFCI requirement per 2023 NEC

---

### 10. core-002 (Score: 8/10)
**Question:** An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements?

**Agent Answer:** 2-pole breaker or handle-tied per 210.4(B), neutral dedicated per 210.4(D)

**Expected Answer:** Handle tie OR common trip per 210.4(B), common trip required if both L-L and L-N loads, 240.15(B)(1) permits handle ties

**Accuracy:** 4/5 - Overall correct
**Completeness:** 4/5 - Missing key details
**Specific Errors:**
- Does not explicitly reference 240.15(B)(1) which permits handle ties
- Missing distinction that common trip is required when circuit has BOTH line-to-line and line-to-neutral loads

---

## Error Patterns

### Pattern 1: Reflection Bug (21 points lost)
The reflection implementation has a critical bug where answers are replaced by "[VERIFIED]" message when reflection calls tools and marks as "improved". This needs immediate fix.

### Pattern 2: 2023 NEC Kitchen GFCI Expansion
Agent not aware that 2023 NEC 210.8(A)(5) expanded to ALL kitchen receptacles including refrigerator.

### Pattern 3: Small Appliance Circuit Scope
Agent incorrectly believes kitchen small appliance circuits cannot serve dining room (opposite of 210.52(B)).

### Pattern 4: Working Space Depth
Agent using wrong depth values (35.43" or 20-30" instead of 36").

---

## Recommendations

1. **FIX REFLECTION BUG IMMEDIATELY**: When reflection marks "improved", ensure the revised answer is returned, not just the verification message.

2. **Update Knowledge Base**: Add 2023 NEC 210.8(A)(5) kitchen GFCI expansion covering all receptacles.

3. **Correct Small Appliance Understanding**: 210.52(B) allows/requires dining room, pantry, breakfast room to be served by kitchen circuits.

4. **Fix Working Space Tool**: Return 36 inches (not 900mm/35.43") for residential 120/240V panels.
