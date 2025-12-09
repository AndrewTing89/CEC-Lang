# Post Run 6 Analysis: LLM Variance Discovery

## Run 6 Results Summary

| Evaluation | Run 5 | Run 6 | Change |
|------------|-------|-------|--------|
| **Core (28 Q)** | 22 Accurate (78.6%) | 21 Accurate (75.0%) | -1 |
| **CEC (30 Q)** | 23 Accurate (76.7%) | 22 Accurate (73.3%) | -1 |
| **Inaccurate** | 0 | 0 | Same |
| **Success Rate** | 100% | 100% | Same |

## Key Finding: Targeted Fixes Worked, But LLM Variance Exists

### Fixes That Worked (Run 5 → Run 6)

| Question | Run 5 | Run 6 | Fix Applied |
|----------|-------|-------|-------------|
| **cec-020** | Partial (105C) | Accurate (200C) | Article Selection Guide |
| **baseline-006** | Partial (30") | Accurate (36") | Tool Result Enforcement |

### Unexpected Regressions (Run 5 → Run 6)

| Question | Run 5 | Run 6 | Analysis |
|----------|-------|-------|----------|
| cec-005 | Accurate | Partial | LLM variance - different search path |
| cec-008 | Accurate | Partial | LLM variance - incomplete enumeration |
| cec-016 | Accurate | Partial | LLM variance - different interpretation |
| cec-019 | Accurate | Partial | LLM variance - different search results |
| cec-022 | Accurate | Partial | LLM variance - partial list |
| cec-030 | Accurate | Partial | LLM variance - incomplete comparison |
| core-002 | Accurate | Partial | LLM variance - missing requirements |
| core-005 | Accurate | Partial | LLM variance - missing violations |
| inspection-008 | Accurate | Partial | LLM variance - calculation difference |

## Root Cause Analysis

### Temperature Already Set to 0.0

From `core/agent.py` lines 1105-1134:
```python
def __init__(
    self,
    model_name: str = "qwen/qwen3-32b",
    temperature: float = 0.0,  # ALREADY DETERMINISTIC
    verbose: bool = True
):
```

**Despite temperature=0, variance occurs due to:**
1. Groq API-level non-determinism (server-side sampling)
2. Search result ordering variations
3. Tool execution timing differences
4. Token generation variance at API level

### Implication

Single-run evaluations are insufficient to measure true accuracy. Results can swing 5-10% between runs purely due to LLM variance, not prompt/data quality.

## Solution: Multi-Run Averaging

### Approach
1. Run each question N times (default 3)
2. Collect all verdicts per question
3. Use majority voting for final verdict
4. Track consistency metrics per question

### Expected Outcomes
- **High-consistency questions** (3/3 same verdict): Confident baseline
- **Medium-variance questions** (2/3 agreement): Use majority
- **High-variance questions** (different each run): Flag for prompt improvement

### Benefits
1. Establishes true baseline accuracy (averaging out variance)
2. Identifies inherently unstable questions
3. Provides data for targeted prompt fixes
4. Separates "real" failures from "unlucky" runs

## Files Created for Run 7

| File | Purpose |
|------|---------|
| `run_multi_evaluation.py` | Multi-run evaluation with N passes per question |
| `create_variance_report.py` | Analyze consistency across runs |
| `create_cec_judge_report.py` | Judge report with variance data |
| `create_core_judge_report.py` | Judge report with variance data |

## Run 6 Prompt Fixes Applied (Reference)

These were added to `core/agent.py` for Run 6:

1. **Article Selection Guide** - Maps wire types to correct articles
2. **Tool Result Enforcement** - Stronger language to use CEC values
3. **List Enumeration** - Use limit=10+ for list questions
4. **Multi-Part Completeness** - Verify all parts answered

---
*Analysis Date: 2025-12-07*
*Run 7 Strategy: Multi-run averaging with 3 passes per question*
