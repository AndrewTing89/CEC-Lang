# Claude Code Judge Instructions

When you receive this directory and are asked to evaluate model responses, follow these instructions.

**IMPORTANT:**
- **Use your own LLM reasoning capabilities** to evaluate responses
- **NO regex or pattern matching** - actually read and understand each answer
- **NO external API calls** - you ARE the judge

---

## Quick Start

1. Read the model responses file (**.md preferred**, .json as fallback)
2. Read the expected answers file (`core_evaluation_questions.json`)
3. For each response, score Accuracy (0-5) and Completeness (0-5)
4. Output `judge_report - [filename].md` and `wrong_answers - [filename].md`

---

## Step-by-Step Workflow

### Step 1: Load the Files

Read these two files:
- **Expected answers:** In this folder:
  - `core_evaluation_simple-text.txt` - NEC 2023 questions (28 questions)
  - `cec_evaluation_simple-text.txt` - CEC 2022 questions (10 questions)
- **Model responses:** The file to evaluate (user will specify)
  - **Prefer .md format** if both .md and .json exist (smaller, easier to parse)
  - Fall back to .json only if .md is not available

**IMPORTANT:** The expected answers are a REFERENCE, not an answer key for regex matching. You must:
1. Understand what the expected answer means
2. Read the model's response and understand what it's saying
3. Use your reasoning to judge if the model's answer is correct/complete
4. A response can be correct even if worded differently than expected

### Step 2: Evaluate Each Response

For each Q&A pair in the responses file:

1. Find the matching expected answer by ID
2. Compare the model's response to the expected answer
3. Score using the rubric in `RUBRIC.md`:

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

4. Note specific errors found
5. Total = Accuracy + Completeness (0-10)

### Step 3: Create Output Files

Create two files in the same directory as the responses:

#### File 1: `judge_report - [source_filename].md`

```markdown
# Judge Report - [source_filename]

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | [model name from responses file] |
| **Source File** | [source_filename] |
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
| baseline-001 | What is the ampacity... | 5/5 | 5/5 | 10/10 |
| core-001 | A homeowner wants... | 4/5 | 5/5 | 9/10 |
...

---

## Detailed Results

### baseline-001
**Question:** [full question]
**Score:** 10/10 (Accuracy: 5/5, Completeness: 5/5)
**Accuracy Notes:** [explanation]
**Completeness Notes:** [explanation]

---
[repeat for each question]
```

#### File 2: `wrong_answers - [source_filename].md`

```markdown
# Wrong Answers - [source_filename]

**Model:** [model name]
**Judge:** Claude Code (Opus)
**Overall Score:** Z% (X/Y)

---

## Executive Summary
**Questions with Errors:** N of M
**Perfect Scores:** P

---

## Detailed Error Analysis (N questions)

### 1. [question-id] (Score: X/10)
**Question:** [question text]
**Accuracy:** X/5 - [explanation]
**Completeness:** X/5 - [explanation]
**Specific Errors:**
- [error 1]
- [error 2]

---
[repeat for each imperfect score]
```

---

## Special Considerations

### Calculation Questions
Verify:
- Correct base values from tables
- Correct factors/multipliers used
- Correct arithmetic
- Final answer accuracy

### Table Lookup Questions
Check:
- Correct table referenced
- Correct row/column used
- Correct temperature column (60°C vs 75°C vs 90°C)
- Correct conductor material (copper vs aluminum)

### Code Interpretation Questions
Look for:
- Correct code section cited
- Accurate interpretation
- Relevant exceptions mentioned

---

## Example Evaluation

**Question:** "What is the ampacity of 12 AWG copper conductor at 75°C termination?"

**Expected Answer:** "20 amperes per NEC Table 310.16"

**Model Response:** "The ampacity of 12 AWG copper at 75°C is 20 amperes according to Table 310.16 of the NEC."

**Evaluation:**
```json
{
  "accuracy": 5,
  "completeness": 5,
  "total": 10,
  "accuracy_notes": "Correctly states 20 amperes, correctly cites Table 310.16",
  "completeness_notes": "Includes table reference and temperature rating context",
  "errors": []
}
```

---

## Input File Formats

### Expected Answers (simple-text.txt)

Located in this folder:
- `core_evaluation_simple-text.txt` (NEC - 28 questions)
- `cec_evaluation_simple-text.txt` (CEC - 10 questions)

**These are REFERENCES for your reasoning, not regex patterns to match against.**

Format:
```
baseline-001	What is the ampacity of 12 AWG copper conductor at 75°C termination?

EXPECTED ANSWER: 20 amperes

--------------------------------------------------------------------------------

baseline-002	What size copper conductor is required for a 60A circuit at 75°C?

EXPECTED ANSWER: 6 AWG copper

--------------------------------------------------------------------------------
```

### Model Responses - PREFERRED: Markdown (.md)

**Always try .md first** - same filename, smaller and easier to parse.

Example `core_evaluation_results.md`:
```markdown
## baseline-001
**Question:** What is the ampacity of 12 AWG copper at 75°C?
**Answer:** The ampacity is 20 amperes per Table 310.16...

---

## core-001
**Question:** A homeowner wants to upgrade...
**Answer:** For a 200A service...
```

### Model Responses - Fallback: JSON

Only use .json if .md is not available:
```json
{
  "model": "GPT-4o",
  "qa_pairs": [
    {
      "id": "baseline-001",
      "question": "What is the ampacity...",
      "answer": "The ampacity is 20 amperes..."
    }
  ]
}
```

---

## Remember

1. **NO regex grading** - use LLM reasoning to understand and evaluate each answer
2. **Read .md files first** - they're smaller and won't hit context limits
3. **Use yourself as the judge** - no API calls needed
4. **Be consistent** - apply the same standards to all responses
5. **Be thorough** - check calculations step by step
6. **Note errors specifically** - don't just say "wrong", explain what's wrong
7. **Output both files** - judge_report AND wrong_answers
