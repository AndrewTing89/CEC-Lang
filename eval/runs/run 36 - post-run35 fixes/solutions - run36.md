# Solutions Analysis - Run 36

**Date:** 2025-12-11
**Wrong/Partial Answers Analyzed:** 3 major issues (7 total including minor)

## Executive Summary

Root cause analysis of 3 main failing questions (scoring 7-8/10) revealed a **surprising finding:**

| Category | Count | Priority |
|----------|-------|----------|
| **Incorrect Expected Answer** | 2 | HIGH |
| **Wrong Hint in Evaluation** | 1 | HIGH |
| **Missing Tool Capability** | 1 | MEDIUM |

**Key Finding:** The remaining issues are NOT agent bugs - they are **evaluation framework errors**. The agent's answers were often MORE accurate than the expected answers.

---

## Issue Analysis

### Issue 1: cec2022-035 - Table 240.4(G) "California-Only" Claim

**Score:** 7/10
**Root Cause Category:** INCORRECT_EXPECTED_ANSWER

**Investigation:**
- Tools called: `cec_lookup_table`, `cec_search`
- Files examined: `cec_tables_unified.json`, `nec_tables_unified.json`
- Data checked: Table 240.4(G) in both CEC and NEC

**Findings:**
The expected answer claims Table 240.4(G) "does not exist in the base NEC 2023" - **THIS IS FACTUALLY INCORRECT**.

**Evidence:**
```json
// CEC Table 240.4(G) - Line 3269 of cec_tables_unified.json
{
  "caption": "Specific Conductor Applications",
  "california_amendment": true,
  "amendment_type": "delta"  // DELTA = modified, not new
}

// NEC Table 240.4(G) - Line 3305 of nec_tables_unified.json
{
  "caption": "Specific Conductor Applications"
  // SAME TABLE EXISTS IN NEC
}
```

**Actual California Modifications (only 2 of 10 rows differ):**
1. Air-conditioning conductors: CEC references "440, Parts III, VI" vs NEC "440, Parts III, IV, VI"
2. Type ITC conductors: CEC references Article 727 vs NEC Article 335

**The Agent Was More Accurate:**
The agent correctly discussed "California amendments denoted by delta symbol" and "modifications from the base NEC" - which is factually correct. The expected answer's claim that the table "doesn't exist in NEC" is false.

**Proposed Fix:**
- **Type:** Evaluation Data
- **File(s):** `eval/standardized_llm-as-judge/CEC2022_eval_questions.json`
- **Change:** Update expected answer:
  ```
  CEC Table 240.4(G) exists in both CEC 2022 and NEC 2023, but the California
  version contains delta amendments. Specific modifications include:
  1) Air-conditioning conductor references omit NEC Part IV
  2) Type ITC conductors reference Article 727 instead of NEC Article 335
  The delta (Δ) symbol indicates modifications from the base NEC.
  ```
- **Generalization:** Clarifies the distinction between "California-only" (N marker) vs "California-modified" (delta marker)

---

### Issue 2: cec2022-038 - Medium Voltage Table Count Error

**Score:** 8/10
**Root Cause Category:** INCORRECT_EXPECTED_ANSWER + MISSING_TOOL

**Investigation:**
- Tools called: `cec_search`
- Files examined: `cec_tables_unified.json`
- Data checked: All Tables 311.60(C)(67) through 311.60(C)(86)

**Findings:**
1. **Expected answer is mathematically wrong:** Claims "18 tables" but the range 67-86 contains **20 tables** (86 - 67 + 1 = 20)
2. **All 20 tables exist** in `cec_tables_unified.json` with `california_amendment: true` metadata
3. **Search only returned 8 table references** due to limit=10 constraint
4. **No enumeration tool exists** to list all tables matching a pattern

**Evidence:**
```bash
# Count of MV tables in JSON
$ grep -c "Table 311.60(C)(" cec_tables_unified.json
20  # NOT 18 as expected answer claims

# All have California metadata
$ grep -B2 "Table 311.60(C)(67)" cec_tables_unified.json
"california_amendment": true,
"amendment_type": "delta",
```

**Why Agent Only Listed 6:**
The hybrid search query "medium voltage cable tables" with limit=10 returned chunks referencing only some tables. The agent listed what it found in the search results, not the complete set.

**Proposed Fix:**
- **Type:** Evaluation Data + New Tool
- **File(s):**
  1. `eval/standardized_llm-as-judge/CEC2022_eval_questions.json` - Fix count to 20
  2. `core/cec_table_tools.py` - Add table enumeration tool
- **Change 1:** Update expected answer:
  ```
  CEC has 20 medium voltage tables in the 311.60(C) series
  (Tables 311.60(C)(67) through 311.60(C)(86)) that are California amendments.
  ```
- **Change 2:** Add new tool:
  ```python
  def list_tables_by_pattern(self, pattern: str) -> List[str]:
      """List all table IDs matching a regex pattern.
      Example: list_tables_by_pattern(r"311\.60\(C\)") returns all MV tables."""
  ```
- **Generalization:** Enables complete enumeration of table sets, not just search-based discovery

---

### Issue 3: cec2022-006 - Working Space Depth Confusion

**Score:** 8/10
**Root Cause Category:** WRONG_HINT + HINT_ENFORCEMENT_DISTRACTION

**Investigation:**
- Tools called: `cec_lookup_working_space`, `cec_search` (x2)
- Files examined: `cec_table_tools.py`, evaluation trace
- Data checked: Table 110.26(A)(1) working space data

**Findings:**
The working space tool **returned the CORRECT answer** in iteration 1:
```
Working space requirement for 120V (condition 1): 900 mm (3 ft) per CEC 2022 Table 110.26(A)(1)
```

**However**, the evaluation question has hint `"110.26(B)"` which:
1. **Is the WRONG section** - the question asks about 110.26(A) depth, not 110.26(B) dedicated space
2. **Forced additional searches** that returned irrelevant results (Section 646.18 about modular data centers)
3. **Caused the agent to discuss 110.26(B) instead of reporting the correct 110.26(A) answer**

**Evidence from trace:**
```json
{
  "iteration": 1,
  "tool": "cec_lookup_working_space",
  "output": "900 mm (3 ft)"  // CORRECT!
},
{
  "iteration": 2,
  "enforcement_triggered": "ENFORCEMENT: Missing hint:110.26(B) - forced additional tool call"
  // DISTRACTION BEGINS
}
```

**The Agent Had the Right Answer:**
The tool correctly returned "900 mm (3 ft)" = 36 inches. But hint enforcement forced the agent to chase 110.26(B), which is about dedicated space ABOVE/BELOW equipment (24-30 inches), not working clearance DEPTH in front (36 inches).

**Proposed Fix:**
- **Type:** Evaluation Data
- **File(s):** `eval/standardized_llm-as-judge/CEC2022_eval_questions.json`
- **Change:**
  1. Change hint from `"110.26(B)"` to `"110.26(A)(1)"` (correct section)
  2. Or remove the hint entirely since `cec_lookup_working_space` tool already handles this
- **Generalization:** Ensures hints point to the correct code section for the question being asked

---

## Summary of Fixes

| Issue | Category | File | Fix Type | Priority |
|-------|----------|------|----------|----------|
| cec2022-035 | INCORRECT_EXPECTED_ANSWER | `CEC2022_eval_questions.json` | Eval Data | HIGH |
| cec2022-038 | INCORRECT_EXPECTED_ANSWER | `CEC2022_eval_questions.json` | Eval Data | HIGH |
| cec2022-038 | MISSING_TOOL | `cec_table_tools.py` | New Tool | MEDIUM |
| cec2022-006 | WRONG_HINT | `CEC2022_eval_questions.json` | Eval Data | HIGH |

---

## Implementation Order

1. **Fix cec2022-035 expected answer** - The current expected answer is factually incorrect
2. **Fix cec2022-038 expected answer** - Change "18 tables" to "20 tables" (math error)
3. **Fix cec2022-006 hint** - Change from 110.26(B) to 110.26(A)(1)
4. **Add table enumeration tool** - Nice-to-have for listing tables by pattern

---

## Key Insight

**Run 36 achieved 95.1% accuracy, but 3 of the "errors" are actually evaluation framework problems:**

| Question | Agent Accuracy | Expected Answer Accuracy |
|----------|---------------|-------------------------|
| cec2022-035 | More accurate (noted delta amendments) | Wrong (claims table doesn't exist in NEC) |
| cec2022-038 | Partial (6 of 20 tables) | Wrong count (18 instead of 20) |
| cec2022-006 | Had correct answer initially | Hint points to wrong section |

**If we fix the evaluation framework, the agent's actual accuracy is closer to 97-98%.**

---

## Expected Impact

After fixing the evaluation data:
- **cec2022-035:** Should score 9-10/10 (agent's answer is correct)
- **cec2022-038:** May still need tool improvement for complete enumeration
- **cec2022-006:** Should score 10/10 (agent already gets correct answer from tool)

**Projected score after eval fixes:** 95.1% → ~97%
