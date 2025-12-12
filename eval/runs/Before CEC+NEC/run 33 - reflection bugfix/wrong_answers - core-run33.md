# Wrong Answers - core-run33_evaluation_results_2025-12-11.md

**Model:** CEC Lang Agent (Qwen3-32B via Groq)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 94.8% (256/270)

**Note:** Scores updated after clarifying CEC 2022 vs NEC 2023 differences for kitchen GFCI requirements.

---

## Executive Summary

**Questions with Errors:** 3 of 27
**Perfect Scores:** 24

| Category | Count |
|----------|-------|
| Perfect (10/10) | 24 |
| Minor issues (8-9/10) | 3 |
| Moderate issues (7/10) | 0 |
| Major issues (0-6/10) | 0 |

### Improvement Over Previous Run
- **Run 31:** 91.5% (247/270) - Pre-reflection baseline
- **Run 32:** 81.1% (219/270) - Reflection bug caused answers to be lost
- **Run 33:** 94.8% (256/270) - Bug fixed, +13.7% improvement, **BEST SCORE**

---

## Questions Correctly Answered (Previously Marked as Errors)

### baseline-003 and inspection-005 - CEC 2022 vs NEC 2023 Clarification

These were initially marked as errors because the expected answers were based on NEC 2023 requirements. After review:

- **baseline-003:** Agent correctly states kitchen GFCI is required for "countertop surfaces" per CEC 2022 210.8(A)(6). The dishwasher explicit requirement is an NEC 2023 expansion not yet in CEC 2022.

- **inspection-005:** Agent correctly states refrigerator needs "AFCI Only" (not GFCI) citing the CEC 2022 210.8(A)(6) exception for dedicated appliance circuits. NEC 2023 removed this exception, but CEC 2022 (our target code) still has it.

**Verdict:** Both answers are CORRECT for CEC 2022. Expected answers file has been updated with CEC 2022 vs NEC 2023 sections.

---

## Detailed Error Analysis

### 1. inspection-002 (Score: 8/10)

**Question:** Electrical panel inspection in residential garage: Panel has 30 inches width clearance, 28 inches depth clearance in front, and a water heater located 16 inches to the left side. Panel is surface-mounted on wall at 5 feet height. Identify ALL NEC violations.

**Accuracy:** 4/5 - One incorrect violation identified
**Completeness:** 4/5 - Two correct violations, one incorrect

**Issue Type:** LLM Reasoning Error (not retrieval)

**Specific Errors:**
- **INCORRECT CLAIM:** Agent states "Insufficient Panel Height - 5 ft" is a violation per 110.26(A)(2)
- **Analysis:** The 110.26(A)(2) requirement is for working space HEIGHT (6.5 ft clearance above floor), not panel mounting height
- Mounting a panel at 5 ft height does NOT violate code - the vertical working space clearance (floor to 6.5 ft minimum) is what matters
- The tool output did NOT include 110.26(A)(2) text, so the LLM incorrectly inferred a violation

**Correctly Identified Violations:**
1. Depth clearance 28" < 36" required - CORRECT
2. Water heater obstruction in working space - CORRECT

**Incorrectly Identified Violation:**
3. "Insufficient Panel Height" - INCORRECT interpretation

---

### 2. core-005 (Score: 9/10)

**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?

**Accuracy:** 5/5 - Correctly identifies main violations
**Completeness:** 4/5 - Missing explicit storage prohibition reference

**Issue Type:** LLM Underutilization of Retrieved Data

**Specific Errors:**
- Agent correctly identifies the 36" depth violation and clothes closet prohibition
- Tool output explicitly mentioned "110.26(B): Dedicated space above and below equipment"
- **OMISSION:** Agent did not explicitly cite 110.26(B) in the answer despite it being in the tool hints
- Expected answer includes: "No storage allowed in working space per 110.26(B)"

---

### 3. inspection-010 (Score: 9/10)

**Question:** A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase. Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required.

**Accuracy:** 5/5 - Correct GEC size (2/0 AWG copper)
**Completeness:** 4/5 - Missing ground rod exception

**Issue Type:** Retrieval Gap (exception not in knowledge base)

**Specific Errors:**
- Agent correctly identifies 2/0 AWG copper per Table 250.66
- Table footnotes [1], [2], [3] were provided but 250.66(A) exception was not
- **OMISSION:** Did not mention the 250.66(A) exception that allows 6 AWG maximum if the GEC connects solely to a ground rod electrode
- This exception lives in section text, not table footnotes - retrieval gap

---

## Problem Pattern Analysis

| Issue Type | Count | Questions |
|------------|-------|-----------|
| LLM reasoning error | 1 | inspection-002 |
| LLM underutilization | 1 | core-005 |
| Retrieval/knowledge gap | 1 | inspection-010 |

### Remaining Issues

1. **LLM Misinterpretation of 110.26(A)(2):** Agent confused panel mounting height with working space height requirement. This is a reasoning error, not a retrieval issue.

2. **Underutilization of Retrieved Hints:** The 110.26(B) reference was in the tool output but the agent didn't incorporate it into the answer.

3. **Missing Exception in Knowledge Base:** The 250.66(A) ground rod exception isn't in the table footnotes. Consider adding section-level exceptions to table lookups.

---

## Recommendations for Improvement

1. **Clarify 110.26(A)(2)** - Could add explicit guidance to tool output: "110.26(A)(2) refers to WORKING SPACE height (6.5 ft above floor), NOT panel mounting height"

2. **Strengthen reflection prompts** - Reflection could specifically check "Did I use all hints from tool outputs?"

3. **Add section exceptions to table lookups** - For Table 250.66, include 250.66(A) exception about ground rod sizing

---

## Reflection Feature Performance

**Reflection Used:** 27/27 questions (100%)
**Reflection Improved:** 3/27 questions (11.1%)

The reflection bugfix successfully prevented the "[VERIFIED]" message from replacing actual answers. Questions that benefited from reflection improvements:
- baseline-005: Exception search added
- core-001: Additional searches for verification
- core-010: Exception searches for adjustment factors

**Conclusion:** The reflection feature is working as intended after the bugfix. Only 3 questions have minor issues (all 9/10 or 8/10), demonstrating strong overall performance.
