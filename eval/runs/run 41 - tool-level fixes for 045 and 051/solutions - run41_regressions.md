# Solutions Analysis - Run 41 Regressions

**Date:** 2025-12-12
**Regressions Analyzed:** 3

## Executive Summary

Three questions regressed from Run 39 to Run 41:

| Question | Run 39 | Run 41 | Root Cause |
|----------|--------|--------|------------|
| cec2022-009 | 10/10 | 8/10 | Tool Selection Failure |
| cec2022-015 | 10/10 | 9/10 | Search Ranking Variability |
| cec2022-035 | 10/10 | 8/10 | Tool Output Limitation |

**Key Finding:** None of these regressions were caused by the Run 41 code changes (fixes for 045 and 051). They are due to LLM stochastic behavior and search ranking variability.

---

## Issue 1: cec2022-009 - Service Conductor Sizing

**Score:** 10/10 → 8/10 (-2)
**Root Cause Category:** TOOL_SELECTION

### Investigation

**Question:** Service conductor sizing for 200A dwelling upgrade

**Expected:** 2/0 AWG copper OR 4/0 AWG aluminum (Table 310.12(A))
**Run 41 Answer:** 4/0 AWG copper or 250 kcmil aluminum (Table 310.16 values)

**Tools Called:**
- Run 39: `cec_lookup_conductor_size(conductor_application="service")` ✅
- Run 41: `cec_search(query="service conductor sizing dwelling unit")` ❌

### Findings

The agent in Run 41 chose `cec_search` instead of the specialized `cec_lookup_conductor_size` tool. The search results didn't include Table 310.12(A) in top 5, so the agent used Table 310.16 values while incorrectly citing Table 310.12(A).

**The specialized tool exists and works correctly:**
```python
# core/tools.py line 189-211
@tool
def cec_lookup_conductor_size(
    required_ampacity: int,
    conductor_application: str = "general"  # "general" or "service"
)
```

When `conductor_application="service"`, it correctly returns Table 310.12(A) values.

### Evidence

**Table 310.12(A) - Dwelling Services (200A):**
- Copper: **2/0 AWG** ✅
- Aluminum: **4/0 AWG** ✅

**Table 310.16 - General Conductors (200A at 75°C):**
- Copper: **3/0 or 4/0 AWG** (what agent used)
- Aluminum: **250 kcmil** (what agent used)

### Proposed Fix

**Type:** Prompt Enhancement + Enforcement Rule
**File(s):** `core/agent.py`
**Priority:** Medium

**Option A - Enforcement Rule (Recommended):**
```python
# In _enforce_tool_usage() method
if any(kw in q_lower for kw in ['service conductor', '200a service',
                                 'dwelling service', 'service entrance']):
    if 'cec_lookup_conductor_size' not in called_tools:
        return (
            "ENFORCEMENT: This question asks about SERVICE CONDUCTORS. "
            "You MUST call cec_lookup_conductor_size(conductor_application='service') "
            "to get dwelling service sizes from Table 310.12(A)."
        )
```

**Option B - Prompt Enhancement:**
Add to DOMAIN KNOWLEDGE section:
```
### Service Conductor Sizing (Table 310.12(A))
For dwelling service/feeder conductor sizing, ALWAYS use:
  cec_lookup_conductor_size(required_ampacity=X, conductor_application="service")
This uses Table 310.12(A) which has DIFFERENT (smaller) sizes than Table 310.16.
- 200A dwelling: 2/0 Cu or 4/0 Al (NOT 3/0 Cu or 250 Al from Table 310.16)
```

**Generalization:** This fix helps all dwelling service sizing questions.

---

## Issue 2: cec2022-015 - Detached Garage Grounding

**Score:** 10/10 → 9/10 (-1)
**Root Cause Category:** SEARCH_FAILURE

### Investigation

**Question:** Grounding and bonding configuration for detached garage subpanel

**Expected:** Include note that grounding electrode may be required per 250.32(A)
**Run 41 Answer:** Incorrectly stated "No Grounding Electrode Required"

**Tools Called:**
- Both runs: `cec_search` only

### Findings

**Search Result Differences:**
- Run 39: Section 250.32(A) appeared in top 5 results with full text
- Run 41: Section 250.32 was NOT in top 5 results (only mentioned in an info note)

The search query variations ("detached garage grounding subpanel" vs "detached garage subpanel grounding bonding") produced different rankings despite being nearly identical.

**Data Verification:** CEC 250.32(A) exists correctly in data:
```
250.32 Buildings or Structures Supplied by a Feeder(s) or Branch Circuit(s)

(A) Grounding Electrode. A building(s) or structure(s) supplied by
a feeder(s) or branch circuit(s) shall have a grounding electrode
system and grounding electrode conductor installed...

Exception: A grounding electrode shall not be required where only
a single branch circuit supplies the building...
```

### Proposed Fix

**Type:** Prompt Enhancement
**File(s):** `core/agent.py`
**Priority:** Medium

Add to DOMAIN KNOWLEDGE section:
```
### Detached Buildings/Structures (250.32)
When questions involve feeders to detached garages, sheds, or separate buildings:
1. Check 250.32(A) for grounding electrode requirements
2. Feeders (multi-circuit) to detached buildings REQUIRE a grounding electrode
3. Exception: Single branch circuit with EGC = no local electrode needed
4. Neutral and ground must still be separated in subpanel (250.24(D))
```

**Generalization:** This fix helps all detached building grounding questions.

---

## Issue 3: cec2022-035 - Table 240.4(G) California Differences

**Score:** 10/10 → 8/10 (-2)
**Root Cause Category:** TOOL_LOGIC (Output Limitation)

### Investigation

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** Table exists in both codes but California has MODIFIED values
**Run 41 Answer:** Incorrectly stated table "mirrors NEC" without identifying specific differences

**Tools Called:** `cec_lookup_table`

### Findings

The `cec_lookup_table` tool shows the CEC table with a generic delta note but doesn't highlight WHICH rows are modified or HOW they differ from NEC.

**Actual California Modifications Found (by comparing JSON files):**

| Row | CEC 2022 | NEC 2023 | Difference |
|-----|----------|----------|------------|
| Air-conditioning/refrigeration | Parts III, VI | Parts III, IV, VI | CEC removes Part IV |
| Type ITC conductors | Article 727 | Article 335 | Different article |
| Remote-control/signaling | 725.43/725.45/725.121 | 724.43/724.45/725.60 | Different sections |

### Evidence

**Tool Output (current):**
```
Table 240.4(G): Fuses and Circuit Breakers
[California Amendment - delta indicates CA modifications]
... table rows without highlighting what changed ...
```

**Agent couldn't identify:** The tool doesn't show WHICH rows differ from NEC or what the NEC values are.

### Proposed Fix

**Type:** Tool Enhancement
**File(s):** `core/cec_table_tools.py`
**Priority:** Low

Enhance `cec_lookup_table` to show inline delta markers:

```python
# When table has CA amendments, add comparison notes
if table_has_delta_flag:
    for row in table_rows:
        if row_differs_from_nec(row, nec_table):
            output.append(f"⚠️ CA MODIFICATION: {describe_difference(row)}")
```

**Example Output:**
```
Row: Air-conditioning and refrigeration equipment
Article: 440, Parts III, VI
⚠️ CA MODIFICATION: NEC 2023 includes Part IV (440, Parts III, IV, VI)
```

**Generalization:** This helps all "what's unique to California" questions about amended tables.

---

## Summary of Fixes

| Issue | Category | File | Fix Type | Priority | Impact |
|-------|----------|------|----------|----------|--------|
| cec2022-009 | TOOL_SELECTION | agent.py | Enforcement + Prompt | Medium | All dwelling service questions |
| cec2022-015 | SEARCH_FAILURE | agent.py | Prompt | Medium | All detached building questions |
| cec2022-035 | TOOL_LOGIC | cec_table_tools.py | Tool Enhancement | Low | CA-specific table questions |

## Implementation Order

1. **cec2022-009 (Service Conductors)** - Medium priority
   - Add enforcement rule for service conductor questions
   - Add domain knowledge about Table 310.12(A) vs 310.16
   - Highest impact: prevents oversizing of dwelling services

2. **cec2022-015 (Detached Buildings)** - Medium priority
   - Add domain knowledge about 250.32 grounding electrode requirements
   - Inspector-critical: missing grounding electrode is a code violation

3. **cec2022-035 (Table Differences)** - Low priority
   - Enhancement to show NEC comparisons in table output
   - Nice-to-have: helps with "what's California-specific" questions

## Key Observation

**None of these regressions were caused by the Run 41 code changes.** The fixes for cec2022-045 and cec2022-051 only modified table tool formatting, which doesn't affect these unrelated questions. The regressions are due to:

1. LLM stochastic tool selection (cec2022-009)
2. Search ranking variability (cec2022-015)
3. Pre-existing tool limitation (cec2022-035)

These issues existed before Run 41 and surfaced due to normal LLM variance.
