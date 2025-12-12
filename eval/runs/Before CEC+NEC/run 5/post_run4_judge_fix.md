# Post-Run 4 Analysis and Fixes

## Run 4 Results Summary

| Evaluation | Accurate | Partial | Inaccurate | Success Rate |
|------------|----------|---------|------------|--------------|
| **CEC (30 Q)** | 20 (66.7%) | 10 (33.3%) | 0 (0.0%) | 100% |
| **Core (28 Q)** | 17 (60.7%) | 9 (32.1%) | 2 (7.1%) | 92.9% |

## Issues Identified in Run 4

### Issue A: LLM Hallucination / Answer Swapping (CRITICAL)

**Affected Questions:** baseline-003, baseline-004

**The Problem:**
- baseline-003 asks: "Where is GFCI protection required in a residential kitchen?"
- baseline-004 asks: "Is AFCI protection required for bedroom circuits?"
- **BOTH returned:** Derating calculation answer about "12 AWG TW (60C rated) copper" with "6 current-carrying conductors" at "43C ambient"

**Evidence:**
- The tool calls were CORRECT (cec_search, cec_exception_search)
- Tool outputs were CORRECT (returned GFCI/AFCI/kitchen/bedroom data)
- The LLM IGNORED the tool outputs and hallucinated a derating calculation

**Root Cause:**
The two-step prompting approach injected planning reasoning into the execution step:
```python
f"Your reasoning was:\n{planning_reasoning}\n\nMake the appropriate tool calls now..."
```
If the planning step hallucinated wrong context (e.g., thinking about derating from a previous question), it poisoned the execution step.

---

### Issue B: Wrong Table for Service Conductors (HIGH)

**Affected Question:** baseline-005

**The Problem:**
- Question: "Can aluminum conductors be used for a 200A service? If yes, what size?"
- Expected: **4/0 AWG aluminum** (per Table 310.12(A))
- Agent said: **250 kcmil aluminum** (per Table 310.16)

**Root Cause:**
The `cec_lookup_conductor_size_for_ampacity()` function hardcoded Table 310.16:
```python
table_310_16 = tools.tables_data["tables"].get("Table 310.16")
```

But for SERVICE conductors:
- **Table 310.12(A)** applies: "Single-Phase Dwelling Services and Feeders"
- For 200A aluminum: **4/0 AWG** (not 250 kcmil)

---

## Fixes Applied for Run 5

### Fix A: Simplified to 1-Prompt System

**Problem:** Two-step prompting (planning -> execution) caused context contamination/hallucination.

**Solution:** Removed two-step prompting. Now uses single-step approach where the LLM:
1. Receives the question
2. Makes tool calls directly
3. Sees tool outputs
4. Generates answer based on actual tool results

**Changes Made:**
- Removed planning call (lines ~1291-1305 in agent.py)
- Removed reasoning injection (`f"Your reasoning was:\n{planning_reasoning}..."`)
- Simplified to single `_invoke_llm_with_retry(messages)` call with tools

**Trade-off:**
- Lost: Explicit "thinking" trace in output
- Gained: No hallucination from injected planning context

---

### Fix B: Added `conductor_application` Parameter for Table Selection

**Problem:** Reverse lookup always used Table 310.16, even for service conductors.

**Solution:** Added `conductor_application` parameter to select correct table:

```python
def cec_lookup_conductor_size_for_ampacity(
    required_ampacity: int,
    temperature_rating: str = "75C",
    conductor_type: str = "copper",
    conductor_application: str = "general"  # NEW PARAMETER
) -> str:
```

**Values:**
- `"general"` (default): Uses Table 310.16 for branch circuits, feeders, general wiring
- `"service"`: Uses Table 310.12(A) for single-phase dwelling services and feeders

**Files Modified:**
- `core/cec_table_tools.py` - Added conductor_application parameter
- `core/nec_table_tools.py` - Added conductor_application parameter
- `core/tools.py` - Updated wrapper functions
- `core/agent.py` - Updated system prompt with TABLE SELECTION guidance

---

### Fix C: Updated Examples to Avoid Contamination

**Problem:** Tool examples used 200A/4/0 AWG which matched baseline-005 evaluation question.

**Solution:** Changed all examples to use 150A/2/0 AWG instead:
- Before: `cec_lookup_conductor_size(200, "75C", "aluminum", "service")` -> "4/0 AWG"
- After: `cec_lookup_conductor_size(150, "75C", "aluminum", "service")` -> "2/0 AWG"

---

## System Prompt Updates

Added new section "TABLE SELECTION FOR CONDUCTOR SIZING (CRITICAL)" with:
- Keywords to detect service conductor questions
- Instructions to use `conductor_application="service"` parameter
- Example showing difference between tables for same ampacity

---

## Expected Improvements for Run 5

1. **baseline-003, baseline-004**: Should now return correct GFCI/AFCI answers (no hallucination from planning step)
2. **baseline-005**: Should return 4/0 AWG aluminum (using Table 310.12(A) with "service" application)
3. **Overall**: Expect reduction in Inaccurate from 2 to 0

---

## Run 5 Configuration

- Date: 2025-12-07
- Model: Same as Run 4
- Changes: 1-prompt system, conductor_application parameter, updated examples
- Evaluation Sets: Core (28 questions), CEC (30 questions)
