# Standardized LLM-as-Judge Evaluation Framework

A reusable framework for evaluating LLM responses to NEC/CEC electrical code questions using consistent, standardized criteria.

---

## How to Use

Give this folder to Claude Code and ask it to evaluate model responses:

```
"Evaluate the model responses in [path/to/responses.json] using the judge framework"
```

Claude Code will follow `CLAUDE_CODE_INSTRUCTIONS.md` and output:
- `judge_report - [filename].md` - Summary stats, all scores, which ones were wrong
- `wrong_answers - [filename].md` - Deep dive into incorrect answers

**No API keys needed** - Claude Code uses its own Opus capabilities as the judge.

---

## Files

| File | Description |
|------|-------------|
| `CLAUDE_CODE_INSTRUCTIONS.md` | Step-by-step instructions for Claude Code |
| `RUBRIC.md` | Detailed scoring criteria with examples |
| `templates/` | Input/output format templates |

---

## Scoring Rubric

Each response is scored on two dimensions:

### Accuracy (0-5)
| Score | Meaning |
|-------|---------|
| 5 | Fully accurate, matches expected answer |
| 4 | Correct with minor omissions |
| 3 | Mostly correct with minor errors |
| 2 | Partially correct with significant errors |
| 1 | Mostly wrong |
| 0 | Completely wrong or dangerous |

### Completeness (0-5)
| Score | Meaning |
|-------|---------|
| 5 | Fully complete, all key points covered |
| 4 | Nearly complete, minor details missing |
| 3 | Reasonably complete, covers main points |
| 2 | Partially complete, missing important details |
| 1 | Very incomplete |
| 0 | No relevant information |

**Total Score:** Accuracy + Completeness = 0-10 per question

---

## Input File Formats

### Expected Answers

```json
{
  "questions": [
    {
      "id": "baseline-001",
      "question": "What is the ampacity of 12 AWG copper at 75°C?",
      "expected_answer": "20 amperes",
      "nec_reference": "Table 310.16"
    }
  ]
}
```

### Model Responses

**Format A: Q&A Pairs**
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

**Format B: Results Array**
```json
{
  "metadata": {"model": "qwen/qwen3-32b"},
  "results": [
    {
      "id": "baseline-001",
      "question": "What is the ampacity...",
      "answer": "## Ampacity of 12 AWG..."
    }
  ]
}
```

---

## Output Files

### 1. Judge Report
`judge_report - [filename].md`

Main report with summary statistics, all scores, and highlights of incorrect answers.

### 2. Wrong Answers Deep Dive
`wrong_answers - [filename].md`

Detailed analysis of ONLY the incorrect answers - why they were wrong, specific errors made.

---

## Workflow

1. **Collect Responses**: Get model answers to the evaluation questions
2. **Format Responses**: Convert to JSON format (see templates)
3. **Run Evaluation**: Ask Claude Code to evaluate using this framework
4. **Review Results**: Check the generated reports

---

## Best Practices

1. **Be consistent**: Use the same judge (Claude Code/Opus) for all evaluations
2. **Review edge cases**: Manually verify borderline scores (3-4)
3. **Track patterns**: Note systematic errors across models

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-09 | Initial framework |
| 1.1 | 2025-12-09 | Simplified to Claude Code only |
