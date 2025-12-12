# LLM-as-Judge Evaluation Report

**Date:** 2025-12-09 12:36
**Source:** run12-core_evaluation_results_2025-12-09.json
**Model Evaluated:** qwen/qwen3-32b
**Judge Model:** Claude Sonnet 4

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | 28 |
| **Judge PASS** | 0 (0.0%) |
| **Judge FAIL** | 28 |
| **Original Pass Rate** | 100.0% |

### Average Scores (0-10 scale)

| Category | Score |
|----------|-------|
| Technical Accuracy | 0.0/10 |
| Completeness | 0.0/10 |
| Code References | 0.0/10 |
| Reasoning Quality | 0.0/10 |
| **Overall** | **0.0/10** |

---

## Detailed Judgments

### Passed (0)


### Failed (28)

**baseline-001** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**baseline-002** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**baseline-003** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**baseline-004** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**baseline-005** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**baseline-006** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**baseline-007** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**baseline-008** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-001** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-002** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-003** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-004** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-005** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-006** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-007** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-008** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-009** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-010** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-011** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**core-012** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**inspection-001** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**inspection-002** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**inspection-005** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**inspection-006** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**inspection-007** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**inspection-008** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**inspection-009** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0

**inspection-010** - Score: 0/10
- Failed to evaluate
- **Errors:** Evaluation failed
- Accuracy: 0 | Complete: 0 | Refs: 0 | Reasoning: 0


---

## Methodology

The LLM-as-Judge approach evaluates each agent response against:
1. **Expected Answer** - Ground truth from the question bank
2. **Technical Accuracy** - Correctness of code values, calculations
3. **Completeness** - Coverage of all question aspects
4. **Code References** - Proper NEC/CEC section citations
5. **Reasoning Quality** - Clarity and logic of explanation

A **PASS** verdict requires an overall score >= 6/10.
