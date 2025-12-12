# NEC/CEC LLM-as-Judge Evaluation Rubric

**Version:** 1.0
**Created:** 2025-12-09
**Standard Judge:** Claude Opus 4.5

---

## Overview

This rubric provides standardized criteria for evaluating LLM responses to National Electrical Code (NEC) and California Electrical Code (CEC) questions. Each response is scored on two dimensions: **Accuracy** and **Completeness**.

**Total Score:** Accuracy (0-5) + Completeness (0-5) = Total (0-10)

---

## Accuracy Scoring (0-5 points)

Measures how **correct** the answer is compared to the expected answer and code requirements.

| Score | Label | Criteria |
|-------|-------|----------|
| **5** | Fully Accurate | Answer matches expected answer exactly. Correct code references. No factual errors. |
| **4** | Mostly Accurate | Correct answer with minor omissions or slight imprecision. Core facts correct. |
| **3** | Partially Accurate | Mostly correct but contains minor errors. Main concept understood but details wrong. |
| **2** | Significant Errors | Partially correct but has significant errors that could mislead. |
| **1** | Mostly Wrong | Few correct elements. Fundamental misunderstanding of the code requirement. |
| **0** | Completely Wrong | Entirely incorrect, dangerous misinformation, or no relevant answer provided. |

### Accuracy Examples

**Score 5 - Fully Accurate:**
- Q: "What is the ampacity of 12 AWG copper at 75°C?"
- Expected: "20 amperes"
- Response: "20 amperes per NEC Table 310.16"

**Score 4 - Mostly Accurate:**
- Q: "What size conductor for 200A service?"
- Expected: "4/0 AWG aluminum or 2/0 AWG copper per Table 310.12"
- Response: "4/0 AWG aluminum" (correct but missing copper option)

**Score 3 - Partially Accurate:**
- Q: "Calculate adjusted ampacity: 30A × 0.82 × 0.80"
- Expected: "19.68A"
- Response: "17.04A" (used wrong temperature factor 0.71 instead of 0.82)

**Score 2 - Significant Errors:**
- Q: "Working clearance for 240V panel?"
- Expected: "36 inches per 110.26(A)(1)"
- Response: "24 inches" (wrong value, could cause safety issues)

**Score 1 - Mostly Wrong:**
- Q: "Is GFCI required in kitchens?"
- Expected: "Yes, for countertop receptacles per 210.8(A)(6)"
- Response: "Only if within 6 feet of a sink" (misunderstands kitchen requirement)

**Score 0 - Completely Wrong:**
- Q: "Maximum conductors in 1¼" RMC?"
- Expected: "28-29 conductors"
- Response: "144 conductors" (used wrong units, dangerous overestimate)

---

## Completeness Scoring (0-5 points)

Measures how **thorough** the answer is in covering all relevant aspects.

| Score | Label | Criteria |
|-------|-------|----------|
| **5** | Fully Complete | All key points covered. Includes relevant exceptions, notes, and context. |
| **4** | Nearly Complete | Covers main points with minor details missing. Adequate for practical use. |
| **3** | Reasonably Complete | Covers primary requirements but missing important secondary details. |
| **2** | Partially Complete | Answers the question but missing significant relevant information. |
| **1** | Very Incomplete | Minimal information provided. Missing most key points. |
| **0** | No Relevant Info | Does not address the question or provides no useful information. |

### Completeness Examples

**Score 5 - Fully Complete:**
- Q: "AFCI requirements for bedrooms?"
- Response includes: Yes required (210.12(A)), applicable rooms, protection methods (combination AFCI, outlet branch-circuit), exceptions if any

**Score 4 - Nearly Complete:**
- Q: "GFCI locations in dwelling?"
- Response lists: bathrooms, kitchens, garages, outdoors, basements (but misses laundry areas)

**Score 3 - Reasonably Complete:**
- Q: "Service conductor sizing?"
- Response gives: correct size but doesn't mention temperature rating assumptions or Table reference

**Score 2 - Partially Complete:**
- Q: "Multiwire branch circuit requirements?"
- Response mentions: handle tie requirement (but omits neutral continuity, grouping requirements)

---

## Special Scoring Considerations

### Calculation Questions

For questions requiring calculations (derating, voltage drop, conduit fill, load calculations):

1. **Check each step:**
   - Correct base values from tables
   - Correct factors/multipliers
   - Correct arithmetic
   - Correct final answer

2. **Partial credit:**
   - Correct methodology but wrong value: Score 3-4
   - Wrong methodology: Score 1-2
   - Order-of-magnitude error: Score 0-1

### Table Lookup Questions

1. **Verify:**
   - Correct table referenced
   - Correct row/column used
   - Correct value extracted

2. **Common errors to check:**
   - Wrong temperature column (60°C vs 75°C vs 90°C)
   - Wrong conductor material (copper vs aluminum)
   - Metric vs imperial units

### Code Interpretation Questions

1. **Check for:**
   - Correct code section cited
   - Accurate interpretation of requirement
   - Relevant exceptions mentioned
   - Proper context provided

---

## Output Format

Each evaluation should produce:

```json
{
  "id": "question-id",
  "question": "Question text...",
  "accuracy": 0-5,
  "completeness": 0-5,
  "total": 0-10,
  "accuracy_notes": "Explanation of accuracy score",
  "completeness_notes": "Explanation of completeness score",
  "errors": ["List of specific errors found"]
}
```

---

## Summary Statistics

After evaluating all questions, calculate:

```json
{
  "total_questions": N,
  "total_accuracy": sum of accuracy scores,
  "total_completeness": sum of completeness scores,
  "total_score": sum of total scores,
  "max_possible": N × 10,
  "avg_accuracy": total_accuracy / N,
  "avg_completeness": total_completeness / N,
  "avg_total": total_score / N,
  "percentage": (total_score / max_possible) × 100
}
```

---

## Judge Prompt Template

Use this prompt when asking an LLM to judge a response:

```
You are an expert NEC (National Electrical Code) evaluator. Judge this LLM response for ACCURACY and COMPLETENESS.

QUESTION: {question}

EXPECTED ANSWER: {expected_answer}
NEC/CEC REFERENCE: {reference}

MODEL'S RESPONSE:
{model_response}

Evaluate on two criteria:

1. ACCURACY (0-5 points):
   - 5: Fully accurate, matches expected answer
   - 4: Correct with minor omissions
   - 3: Mostly correct with minor errors
   - 2: Partially correct with significant errors
   - 1: Mostly wrong with few correct elements
   - 0: Completely wrong or dangerous misinformation

2. COMPLETENESS (0-5 points):
   - 5: Fully complete, all key points covered
   - 4: Nearly complete, minor details missing
   - 3: Reasonably complete, covers main points
   - 2: Partially complete, missing important details
   - 1: Very incomplete, missing most key points
   - 0: No relevant information provided

Respond in this exact JSON format only:
{"accuracy": <0-5>, "completeness": <0-5>, "accuracy_notes": "<brief explanation>", "completeness_notes": "<brief explanation>", "errors": ["<error1>", "<error2>"] or []}
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-09 | Initial rubric based on baseline LLM evaluations |
