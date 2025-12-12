# LLM-as-Judge Evaluation

You are the judge. Use your reasoning capabilities to evaluate model responses against expected answers.

**CRITICAL: DO NOT write Python scripts that call external APIs (Anthropic, OpenAI, etc.) for judging.**
**YOU are Claude Code - use YOUR OWN built-in LLM capabilities to read and evaluate the answers directly.**
**Simply read the files and apply the scoring rubric yourself. No API calls needed.**

## Arguments
- `$ARGUMENTS` = run folder name or number (e.g., "run 27" or "27" or "run 27 - robustness fixes")

## Step 1: Determine Which Run to Judge

If `$ARGUMENTS` is empty or not provided:
1. List the folders in `eval/runs/` to show the user available runs
2. Ask the user: "Which run would you like me to judge? (enter number or full folder name)"
3. Wait for their response before proceeding

## Step 2: Locate the Run Folder

Find the run folder in `eval/runs/`. If just a number is provided, find the matching folder.
List the contents and identify the results file:
- `run{N}_evaluation_results_*.md` (unified eval results)
- OR legacy format: `core-run{N}_evaluation_results_*.md` and `cec-run{N}_evaluation_results_*.md`

Prefer `.md` files over `.json` (smaller, easier to parse).

## Step 3: Load Expected Answers

Read the expected answers from:
- **Unified (new format):** `eval/standardized_llm-as-judge/CEC2022_eval_simple-text.txt`
- **Legacy Core:** `eval/standardized_llm-as-judge/core_evaluation_simple-text.txt`
- **Legacy CEC:** `eval/standardized_llm-as-judge/cec_evaluation_simple-text.txt`

Use the unified file for runs with `run{N}_` prefix. Use legacy files for runs with `core-run{N}_` or `cec-run{N}_` prefix.

These are REFERENCES for your reasoning, not regex patterns to match.

## Step 4: Evaluate Each Response

For each Q&A pair in the results file:

### Scoring Rubric

**Accuracy (0-5):**
| Score | Meaning |
|-------|---------|
| 5 | Fully accurate, matches expected answer |
| 4 | Correct with minor omissions |
| 3 | Mostly correct with minor errors |
| 2 | Partially correct with significant errors |
| 1 | Mostly wrong |
| 0 | Completely wrong or dangerous |

**Completeness (0-5):**
| Score | Meaning |
|-------|---------|
| 5 | All key points covered |
| 4 | Nearly complete, minor details missing |
| 3 | Reasonably complete |
| 2 | Partially complete |
| 1 | Very incomplete |
| 0 | No relevant information |

**Total = Accuracy + Completeness (0-10)**

### Special Considerations

**Calculation Questions:** Verify correct base values, factors/multipliers, arithmetic, final answer.

**Table Lookup Questions:** Check correct table, row/column, temperature column (60/75/90C), conductor material.

**Code Interpretation Questions:** Check correct section cited, accurate interpretation, relevant exceptions.

## Step 5: Create Output Files

Create TWO files in the run folder:

### File 1: `judge_report - run{N}.md`

```markdown
# Judge Report - run{N}

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | [model name from responses] |
| **Source File** | {source_filename} |
| **Judge** | Claude Code (Opus) |
| **Method** | LLM-as-Judge |
| **Timestamp** | [current timestamp] |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | N |
| **Total Score** | X / Y |
| **Percentage** | Z% |
| **Avg Accuracy** | A / 5 |
| **Avg Completeness** | B / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | X |
| High (8-9/10) | X |
| Medium (5-7/10) | X |
| Low (0-4/10) | X |

---

## All Evaluations
| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| cec2022-001 | What is the ampacity... | 5/5 | 5/5 | 10/10 |
...

---

## Detailed Results

### {question-id}
**Question:** [full question]

**Agent Answer:** [the actual answer the agent gave - truncate to ~500 chars if very long, ending with "..."]

**Expected Answer:** [the expected answer from simple-text.txt]

**Score:** X/10 (Accuracy: X/5, Completeness: X/5)
**Accuracy Notes:** [explanation]
**Completeness Notes:** [explanation]

---
[repeat for each question]
```

### File 2: `wrong_answers - run{N}.md`

```markdown
# Wrong Answers - run{N}

**Model:** [model name]
**Judge:** Claude Code (Opus)
**Overall Score:** Z% (X/Y)

---

## Executive Summary
**Questions with Errors:** N of M
**Perfect Scores:** P

---

## Detailed Error Analysis

### 1. {question-id} (Score: X/10)
**Question:** [question text]

**Agent Answer:** [what the agent actually said - truncate to ~500 chars if very long, ending with "..."]

**Expected Answer:** [what the correct answer should be from simple-text.txt]

**Accuracy:** X/5 - [explanation]
**Completeness:** X/5 - [explanation]
**Specific Errors:**
- [error 1]
- [error 2]

---
[repeat for each imperfect score, sorted by lowest score first]
```

## Step 6: Handle Legacy Runs

If the run folder has separate core and CEC results (legacy format):
1. Judge the core results first, create both output files with `core-run{N}` suffix
2. Then judge the CEC results, create both output files with `cec-run{N}` suffix

## Step 7: Summary

After judging, report:
- Overall scores for each eval
- Number of perfect scores vs errors
- Top 3 problem areas identified

## Important Reminders

- Use LLM reasoning - NO regex matching
- A response can be correct even if worded differently than expected
- Be consistent - apply the same standards to all responses
- Be specific about errors - don't just say "wrong", explain what's wrong
- Check calculations step by step

