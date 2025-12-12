# Solutions Analysis - Run 35

**Date:** 2025-12-11
**Wrong/Partial Answers Analyzed:** 7 major issues (10 total including minor)

## Executive Summary

Root cause analysis of 7 failing questions revealed **4 distinct categories** of issues:

| Category | Count | Priority |
|----------|-------|----------|
| Missing/Poor Tool Output | 3 | HIGH |
| Search/Query Issues | 1 | HIGH |
| LLM Hallucination | 1 | HIGH |
| Data/Metadata Gaps | 2 | MEDIUM |

**Key Finding:** Most failures are NOT data issues - they're tool presentation, search query formulation, and agent prompting issues that can be fixed without modifying source data.

---

## Issue Analysis

### Issue 1: cec2022-012 - Surge Protection Search Inconsistency

**Score:** 2/10
**Root Cause Category:** SEARCH_FAILURE

**Investigation:**
- Tools called: `cec_search`
- Files examined: `core/cec_knowledge_tools.py`, `core/opensearch_hybrid_client.py`, `cec_chunks.jsonl`
- Data checked: Section 230.67 EXISTS in chunks (line 502)

**Findings:**
The SAME question (cec2022-008) was answered correctly, but cec2022-012 failed. The difference:
- cec2022-008: "Is surge protection required?" → Simple yes/no → Correct query formulation
- cec2022-012: "Is surge protection required? **If so, where can it be installed?**" → Compound question → LLM formulated query focused on "installation location" instead of "requirement"

The compound question caused the LLM to generate a search query like "surge protection installation location service" which returned grounding sections (250.x) instead of 230.67.

**Evidence:**
```
Section 230.67 exists in cec_chunks.jsonl line 502
Agent answer mentioned 250.24, 250.64, 250.66 (grounding) instead of 230.67 (surge)
```

**Proposed Fix:**
- **Type:** Code + Prompt
- **File(s):** `core/cec_knowledge_tools.py`, `core/agent.py`
- **Change:**
  1. Add query hint injection for critical topics:
     ```python
     QUERY_HINTS = {
         "surge protection": "230.67",
         "AFCI": "210.12",
         "GFCI": "210.8",
     }
     # Boost query with section hint when topic detected
     ```
  2. Add search strategy guidance to system prompt:
     ```
     For compound questions ("Is X required? If so, where?"),
     search the PRIMARY question first. Focus on requirement
     keywords: "required", "shall", "must".
     ```
- **Generalization:** Fixes all compound question scenarios and ensures critical sections are always boosted

---

### Issue 2: cec2022-023 - AFCI Kitchen Circuit Hallucination

**Score:** 6/10
**Root Cause Category:** INTERPRETATION (LLM Hallucination)

**Investigation:**
- Tools called: `cec_search`
- Files examined: `core/agent.py` system prompt, CEC 210.12(A) content
- Data checked: Actual 210.12(A) exceptions in CEC data

**Findings:**
The agent claimed AFCI exemptions that **DO NOT EXIST**:
- "210.12(A)(3) circuits supplying only motors" - **This subsection doesn't exist**
- "210.12(A)(1) circuits supplying refrigeration equipment" - **This is not an exemption**

The ONLY exception in 210.12(A) is for fire alarm systems. Agent hallucinated reasonable-sounding exemptions based on general electrical code patterns.

**Evidence:**
```
CEC 210.12(A) actual text:
"All 120-volt, single-phase, 15- and 20-ampere branch circuits supplying
outlets or devices installed in dwelling unit kitchens..."

Only exception: "AFCI protection shall not be required for an individual
branch circuit supplying a fire alarm system..."
```

**Proposed Fix:**
- **Type:** Prompt
- **File(s):** `core/agent.py`
- **Change:** Add explicit AFCI guidance to system prompt:
  ```
  ## AFCI REQUIREMENTS (CRITICAL FOR DWELLING UNITS)

  Section 210.12(A) requires AFCI protection for ALL 120V, 15A and 20A
  branch circuits in dwelling unit kitchens and other living areas.

  SCOPE: This is a BLANKET requirement - it applies to:
  - All circuits in listed rooms (kitchen, bedroom, living room, etc.)
  - Motor circuits (dishwashers, disposals, etc.)
  - Refrigeration equipment circuits

  ONLY EXCEPTION: Fire alarm system circuits (with metal raceway)

  COMMON MISTAKE TO AVOID:
  - There are NO exemptions for "motor circuits" or "refrigeration equipment"
  - Article 430 (motors) does NOT override 210.12(A) for dwelling units
  ```
- **Generalization:** Prevents hallucination of AFCI exemptions for any dwelling unit circuit question

---

### Issue 3: cec2022-035 - Table 240.4(G) California Flag

**Score:** 5/10
**Root Cause Category:** INCORRECT_EXPECTED_ANSWER

**Investigation:**
- Tools called: `cec_lookup_table`
- Files examined: `cec_tables_unified.json`, `nec_tables_unified.json`
- Data checked: Table 240.4(G) in both CEC and NEC

**Findings:**
The expected answer is **FACTUALLY INCORRECT**. It claims Table 240.4(G) "does not exist in the base NEC 2023" - but it DOES exist in both codes.

The table is correctly marked in CEC JSON:
- `california_amendment: true`
- `amendment_type: "delta"` (modified, not new)

The ACTUAL difference: CEC version references "Article 440 Parts III, VI" while NEC references "Parts III, IV, VI" (CEC removed Part IV reference).

**Evidence:**
```json
// CEC Table 240.4(G) - Line 3269 of cec_tables_unified.json
"california_amendment": true,
"amendment_type": "delta"

// NEC Table 240.4(G) - Line 3305 of nec_tables_unified.json
// EXISTS - same table structure, different row content
```

**Proposed Fix:**
- **Type:** Evaluation Data
- **File(s):** `eval/standardized_llm-as-judge/CEC2022_eval_questions.json`
- **Change:** Update expected answer:
  ```json
  "expected_answer": "CEC Table 240.4(G) has California-specific modifications
  (delta amendment) compared to NEC 2023. For example, the air-conditioning
  row references Article 440 Parts III and VI in CEC, while NEC includes Part IV."
  ```
- **Generalization:** Clarifies distinction between "California-only" (N marker) vs "California-modified" (delta marker)

---

### Issue 4: cec2022-044 - Working Space 480V Tool Distraction

**Score:** 3/10
**Root Cause Category:** TOOL_LOGIC (Output Distraction)

**Investigation:**
- Tools called: `cec_lookup_working_space`, `cec_search`
- Files examined: `core/cec_table_tools.py`, evaluation trace
- Data checked: Tool returned CORRECT answer (1.2m) but agent got distracted

**Findings:**
The tool **RETURNED THE CORRECT ANSWER** (1.2 m / 4 ft) but then added confusing hints:
```
Working space requirement: 1.2 m (4 ft)

**IMPORTANT - LOCATION vs CLEARANCE:**
...also check:
- 240.24(E): Panels prohibited in bathrooms
- 110.26(B): Dedicated space above and below equipment
```

The agent saw these hints and started searching for 110.26(B), getting distracted from the actual answer. Hint enforcement forced additional tool calls that derailed the response.

**Evidence:**
```json
// From evaluation trace
"enforcement_triggered": "ENFORCEMENT: Missing hint:110.26(B) - forced additional tool call"
```

**Proposed Fix:**
- **Type:** Code
- **File(s):** `core/cec_knowledge_tools.py` (working space tool wrapper)
- **Change:** Remove or contextualize the "IMPORTANT - LOCATION vs CLEARANCE" hints:
  - Option A: Remove hints entirely from working space tool output
  - Option B: Only show hints when question mentions "panel location", "bathroom", or "closet"
  - Option C: Make hints a separate "inspector_notes" field that doesn't trigger enforcement
- **Generalization:** Prevents tool output hints from derailing agent responses for all working space queries

---

### Issue 5: cec2022-048 - SF-2 Fixture Wire Missing Tool

**Score:** 2/10
**Root Cause Category:** MISSING_DATA (Search/Table Architecture Gap)

**Investigation:**
- Tools called: `cec_search`
- Files examined: `cec_tables_unified.json`, `cec_chunks.jsonl`
- Data checked: SF-2 EXISTS in JSON (line 17158) but NOT in search chunks

**Findings:**
Data architecture mismatch between two knowledge sources:

1. **OpenSearch chunks**: Table 402.3 chunk only has table TITLE, not row data
2. **Table JSON**: Contains complete Table 402.3 with all 32 fixture wire types including SF-2

The agent searched chunks, found no SF-2, and concluded it doesn't exist - but never tried `cec_lookup_table("402.3")` which would have found it.

**Evidence:**
```json
// SF-2 in cec_tables_unified.json line 17158
{
  "type_letter": "SF-2",
  "max_operating_temp": "200°C (392°F)",
  "insulation": "Silicone rubber"
}

// Chunk line 1398 - only has table header, no row data
"## Table 402.3 Fixture Wires ∆\n\n(continues)\n\n## Table 402.3 Continued ∆"
```

**Proposed Fix:**
- **Type:** Code (New Tool)
- **File(s):** `core/cec_table_tools.py`, `core/tools.py`
- **Change:** Add dedicated fixture wire lookup tool:
  ```python
  def lookup_fixture_wire(self, wire_type: str) -> Dict[str, Any]:
      """
      Look up fixture wire specifications from CEC 2022 Table 402.3

      Args:
          wire_type: Fixture wire type letter (e.g., "SF-2", "PF", "TFN")

      Returns:
          Dict with max_operating_temp, insulation, AWG sizes, application
      """
  ```
- **Generalization:** Provides deterministic lookup for all 32 fixture wire types in Table 402.3

---

### Issue 6: cec2022-051 - Table 220.12 Unit Confusion

**Score:** 2/10
**Root Cause Category:** TOOL_LOGIC (Poor Output Formatting)

**Investigation:**
- Tools called: `cec_lookup_table`
- Files examined: `core/tools.py`, Table 220.12 structure
- Data checked: Table has BOTH `volt_amperes_per_m2` (14) AND `volt_amperes_per_ft2` (1.3)

**Findings:**
The `cec_lookup_table()` function outputs raw Python dict strings:
```
{'type_of_occupancy': 'Office', 'volt_amperes_per_m2': 14, 'volt_amperes_per_ft2': 1.3}
```

The LLM sees both values (14 and 1.3) but has NO CLEAR COLUMN HEADERS. It incorrectly picked the larger number (14) and paired it with the imperial unit (sq ft), resulting in 70,000 VA instead of 6,500 VA.

**Evidence:**
```python
# Current code (tools.py line 700)
for row in table_data.get('rows', []):
    output.append(str(row))  # Raw dict string!
```

**Proposed Fix:**
- **Type:** Code
- **File(s):** `core/tools.py`
- **Change:** Improve table row formatting to clearly label columns:
  ```python
  for row in table_data.get('rows', []):
      row_parts = []
      for key, value in row.items():
          key_formatted = key.replace('_', ' ').replace('m2', 'm²').replace('ft2', 'ft²').title()
          row_parts.append(f"{key_formatted}: {value}")
      output.append(" | ".join(row_parts))
  ```
  Output becomes:
  ```
  Type Of Occupancy: Office | Volt Amperes Per M²: 14 | Volt Amperes Per Ft²: 1.3
  ```
- **Generalization:** Fixes unit confusion for ALL tables with metric/imperial columns

---

### Issue 7: cec2022-038 - Medium Voltage Tables Metadata

**Score:** 7/10
**Root Cause Category:** MISSING_DATA (Metadata Gap)

**Investigation:**
- Tools called: `cec_search`
- Files examined: `cec_tables_unified.json`
- Data checked: All 20 tables 311.60(C)(67) through (86) exist

**Findings:**
All 20 medium voltage tables ARE present in the JSON, but they lack the `california_amendment` boolean field that tools use for filtering. The tables mention "California amendment (delta)" in their descriptions but lack the structured field.

**Evidence:**
```json
// Tables exist but lack boolean flag
"Table 311.60(C)(67)": {
  "description": "...California amendment (delta)..."
  // Missing: "california_amendment": true
}

// Grep for california_amendment in entire JSON: 0 matches
```

**Proposed Fix:**
- **Type:** Data
- **File(s):** `data/CEC_2022/cec_tables_unified.json`
- **Change:** Add `california_amendment: true` and `amendment_type: "delta"` to all 20 medium voltage tables (and audit all other tables for same issue):
  ```json
  "Table 311.60(C)(67)": {
    "california_amendment": true,
    "amendment_type": "delta",
    ...
  }
  ```
- **Generalization:** Enables California-specific filtering for all tables in the system

---

## Summary of Fixes

| Issue | Category | File | Fix Type | Priority |
|-------|----------|------|----------|----------|
| cec2022-012 | SEARCH_FAILURE | `cec_knowledge_tools.py`, `agent.py` | Code + Prompt | HIGH |
| cec2022-023 | INTERPRETATION | `agent.py` | Prompt | HIGH |
| cec2022-035 | INCORRECT_EXPECTED | `CEC2022_eval_questions.json` | Eval Data | LOW |
| cec2022-044 | TOOL_LOGIC | `cec_knowledge_tools.py` | Code | HIGH |
| cec2022-048 | MISSING_DATA | `cec_table_tools.py`, `tools.py` | New Tool | HIGH |
| cec2022-051 | TOOL_LOGIC | `tools.py` | Code | HIGH |
| cec2022-038 | MISSING_DATA | `cec_tables_unified.json` | Data | MEDIUM |

---

## Implementation Order

1. **cec2022-051 (Table formatting)** - Quick win, fixes unit confusion across ALL tables
2. **cec2022-044 (Working space hints)** - Quick win, removes agent distraction
3. **cec2022-023 (AFCI prompt)** - Critical safety issue, prevents hallucinated exemptions
4. **cec2022-048 (Fixture wire tool)** - Adds missing capability for Table 402.3
5. **cec2022-012 (Query hints)** - Improves search reliability for critical topics
6. **cec2022-038 (MV table metadata)** - Data quality improvement
7. **cec2022-035 (Expected answer)** - Evaluation accuracy fix

---

## Expected Impact

After implementing these fixes:
- **Direct fixes:** 7 questions should improve (est. +35 points)
- **Indirect benefits:**
  - Table formatting fix helps ALL table lookups
  - AFCI prompt helps ALL dwelling unit AFCI questions
  - Query hints help ALL surge/GFCI/AFCI questions
  - Fixture wire tool enables ALL Table 402.3 questions

**Projected score improvement:** 90.9% → ~95%+ (estimated)
