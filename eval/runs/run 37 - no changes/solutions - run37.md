# Solutions Analysis - Run 37

**Date:** 2025-12-12
**Wrong/Partial Answers Analyzed:** 5 (3 investigated in depth)
**Overall Score:** 96.0% (509/530)

## Executive Summary

Three issues required deep investigation:

| Issue | Score | Root Cause | Fix Priority |
|-------|-------|------------|--------------|
| cec2022-023 | 5/10 | **SEARCH_FAILURE + INTERPRETATION** - Agent never searched for AFCI, hallucinated outdated rule | **HIGH** |
| cec2022-038 | 8/10 | **MISSING_TOOL** - No enumeration tool for California-specific tables | Medium |
| cec2022-045 | 8/10 | **TOOL_LOGIC** - Table 110.28 uses `sections` structure not handled by tool | Medium |

Two issues (cec2022-001, cec2022-021) scored 9/10 and are **not agent errors** - the agent was technically correct or used valid alternative methodology.

---

## Issue Analysis

### Issue 1: cec2022-023 - AFCI Kitchen Circuits (CRITICAL)

**Score:** 5/10
**Root Cause Category:** SEARCH_FAILURE + INTERPRETATION

**Investigation:**
- Tools called: `cec_search` (but only searched for GFCI, never AFCI)
- Files examined: `core/agent.py`, `core/tools.py`, `data/CEC_2022/cec_content/chapter2_structured_fixedheaders.md`
- Data checked: CEC 2022 Section 210.12(A) text

**Findings:**

1. **The Agent Never Searched for AFCI**
   - Tool called: `cec_search("kitchen countertop receptacles GFCI requirement")`
   - The question explicitly asked about "GFCI, **AFCI**, or combination" but agent only searched GFCI
   - The anti-hallucination enforcement only checks IF tools were called, not WHETHER the right topics were searched

2. **The Agent Hallucinated a False Rule**
   - Agent stated: *"210.12 applies only to bedroom circuits"*
   - This is **completely wrong** - it's an outdated rule from pre-2014 NEC
   - CEC 2022 Section 210.12(A) explicitly lists kitchens FIRST

3. **The Data Is Correct**
   From `chapter2_structured_fixedheaders.md` line 518:
   ```
   (A) Dwelling Units. All 120-volt, single-phase, 15- and 20-ampere branch
   circuits supplying outlets or devices installed in dwelling unit KITCHENS,
   family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms,
   sunrooms, recreation rooms, closets, hallways, laundry areas, or similar
   rooms or areas shall be protected by [AFCI]
   ```
   **Kitchens are listed even BEFORE bedrooms!**

4. **Reflection Also Failed** - The reflection step didn't catch the error because it also didn't search for AFCI.

**Evidence:**
```python
# From evaluation results - only one search performed
"tools_called": ["cec_search"]

# Agent's wrong conclusion:
"None of these circuits require AFCI protection (210.12 applies only to bedroom circuits)."
```

**Proposed Fix:**

**Fix 1: Enhanced Question Decomposition Enforcement (core/agent.py)**
```python
# Add to _verify_required_tools() method around line 1119
def _check_protection_type_coverage(self, question: str, tool_calls: list) -> tuple:
    """Verify all protection types mentioned in question were searched."""
    q_lower = question.lower()
    protection_types = []

    if "gfci" in q_lower or "ground-fault" in q_lower:
        protection_types.append("gfci")
    if "afci" in q_lower or "arc-fault" in q_lower:
        protection_types.append("afci")
    if "ocpd" in q_lower or "overcurrent" in q_lower:
        protection_types.append("overcurrent")

    if not protection_types:
        return (True, None)

    # Check if searches covered all mentioned protection types
    search_queries = []
    for tc in tool_calls:
        if "search" in tc.get("tool", "").lower():
            query = str(tc.get("args", {})).lower()
            search_queries.append(query)

    for ptype in protection_types:
        if not any(ptype in q for q in search_queries):
            return (False, f"Missing search for protection type: {ptype}")

    return (True, None)
```

**Fix 2: Add AFCI Guidance to System Prompt (core/agent.py)**
Add to the system prompt knowledge section:
```markdown
**CRITICAL - AFCI Scope (Common Misconception):**
- ✗ WRONG: "AFCI only applies to bedroom circuits" (outdated - pre-2014 NEC)
- ✓ CORRECT: CEC 2022 Section 210.12(A) requires AFCI for ALL dwelling 120V, 15/20A circuits:
  - Kitchens, family rooms, dining rooms, living rooms, bedrooms, hallways, laundry, closets, etc.
- When a question asks about circuit protection (GFCI/AFCI/both), ALWAYS search for BOTH protection types.
```

**Generalization:** This fix helps ALL circuit protection questions by:
1. Forcing the agent to search for each protection type mentioned
2. Preventing hallucination of outdated code rules
3. Ensuring comprehensive answers when multiple protection types are relevant

---

### Issue 2: cec2022-038 - Medium Voltage Tables Count

**Score:** 8/10
**Root Cause Category:** MISSING_TOOL

**Investigation:**
- Tools called: `cec_search` (semantic search only)
- Files examined: `core/cec_table_tools.py`, `data/CEC_2022/cec_tables_unified.json`
- Data checked: All 20 MV tables verified present with `california_amendment: true` flag

**Findings:**

1. **All 20 Tables Exist in Data**
   ```
   Tables verified: 311.60(C)(67) through 311.60(C)(86)
   All have california_amendment: true
   ```

2. **No Enumeration Tool Exists**
   - `cec_search` returns narrative text, not structured counts
   - `search_tables_by_keyword()` finds tables but doesn't filter by California-specific flag
   - No tool can answer "how many California-specific tables exist?"

3. **Agent Gave Correct Info But Not Count**
   - Listed several correct tables (67-70, 75-76, etc.)
   - Never stated "20 tables total" because search results don't provide this

**Evidence:**
```json
// From cec_tables_unified.json - sample table metadata
{
  "Table 311.60(C)(67)": {
    "california_amendment": true,
    "caption": "Ampacities of an Insulated Triplexed...",
    "section": "311.60(C)(67)"
  }
}
```

**Proposed Fix:**

**Add New Tool: `list_california_specific_tables()` (core/cec_table_tools.py)**
```python
def list_california_specific_tables(self, section_filter: Optional[str] = None) -> str:
    """
    Enumerate all California-specific tables (tables with california_amendment flag).

    Args:
        section_filter: Optional section prefix to filter (e.g., "311.60" for MV tables)

    Returns:
        String with count and enumeration of California-specific tables
    """
    ca_tables = []

    for table_id, table_data in self.tables_data["tables"].items():
        if table_data.get("california_amendment", False):
            section = table_id.replace("Table ", "")
            if section_filter is None or section.startswith(section_filter):
                ca_tables.append({
                    "table_id": table_id,
                    "caption": table_data.get("caption", "")[:80],
                    "section": table_data.get("section", "")
                })

    ca_tables.sort(key=lambda x: x["table_id"])

    output = [f"California-specific tables" + (f" in section {section_filter}" if section_filter else "")]
    output.append(f"**Total count: {len(ca_tables)} tables**\n")

    for table in ca_tables:
        output.append(f"- {table['table_id']}: {table['caption']}...")

    return "\n".join(output)
```

**Generalization:** This fix helps ALL "how many" and "what exists" questions about California amendments by providing a structured enumeration capability.

---

### Issue 3: cec2022-045 - Enclosure Types Incomplete

**Score:** 8/10
**Root Cause Category:** TOOL_LOGIC

**Investigation:**
- Tools called: `cec_lookup_table`
- Files examined: `core/cec_table_tools.py`, `core/tools.py`, `data/CEC_2022/cec_tables_unified.json`
- Data checked: Table 110.28 structure

**Findings:**

1. **Table 110.28 Uses `sections` Structure**
   ```json
   {
     "Table 110.28": {
       "sections": [
         {
           "section_name": "For Outdoor Use",
           "rows": [
             {
               "environmental_condition": "Rain, snow, and sleet",
               "type_3": "X",
               "type_3r": "X",
               "type_3s": "X",
               // ... all types marked
             }
           ]
         }
       ]
     }
   }
   ```

2. **Tool Only Extracts Top-Level `rows`**
   From `core/cec_table_tools.py` line 384:
   ```python
   result = {
       ...
       "rows": table.get("rows", []),  # Returns [] for Table 110.28!
       ...
   }
   ```
   Table 110.28 has no top-level `rows` - data is in `sections[0].rows`.

3. **Agent Got Empty Row Data**
   - Tool returned headers, notes, and footnotes
   - But actual row data (which types are suitable) was empty
   - Agent had to guess from footnotes/notes, missed Type 3 and 3R

**Evidence:**
Tool output showed:
```
Headers: Environmental Conditions | Type 3 | Type 3R | Type 3S | ...
[No row data shown]
Notes: Mechanism shall be operable when ice covered.
```

**Proposed Fix:**

**Modify `cec_lookup_table()` in core/tools.py to Handle Sections:**
```python
# After line 731, add logic to handle sections structure
if table_data.get('sections'):
    # Handle tables with sections (like Table 110.28)
    for section in table_data['sections']:
        section_name = section.get('section_name', 'Section')
        output.append(f"\n=== {section_name} ===")
        for row in section.get('rows', []):
            if isinstance(row, dict):
                row_parts = []
                for key, value in row.items():
                    key_formatted = key.replace('_', ' ').title()
                    row_parts.append(f"{key_formatted}: {value}")
                output.append(" | ".join(row_parts))
else:
    # Handle flat tables (existing code)
    for row in table_data.get('rows', []):
        # ... existing code ...
```

**Also update `get_table_data()` in core/cec_table_tools.py line 384:**
```python
result = {
    ...
    "rows": table.get("rows", []),
    "sections": table.get("sections", []),  # ADD THIS LINE
    ...
}
```

**Generalization:** This fix helps ALL tables that use the `sections` structure (not just Table 110.28).

---

## Issues NOT Requiring Fixes

### cec2022-001 (Score: 9/10) - Ampacity vs OCP
- **Agent Answer:** 25A ampacity per Table 310.16, with note about 20A OCP limit per 240.4(D)
- **Expected Answer:** 20 amperes
- **Analysis:** Agent is **technically more accurate**. Table 310.16 shows 25A ampacity; 20A is the OCP limit. The expected answer conflates these.
- **Recommendation:** Update expected answer to accept both 25A (ampacity) and 20A (practical limit with OCP).

### cec2022-021 (Score: 9/10) - Calculation Methodology
- **Agent Answer:** 120.21A calculated, 200A adequate
- **Expected Answer:** 103.2A calculated, 200A adequate
- **Analysis:** Both reach same conclusion. Agent applied 125% continuous load factor to AC (valid under 210.20(A)). Expected answer used different demand factors.
- **Recommendation:** Both methods are acceptable under Article 220. No fix needed.

---

## Summary of Fixes

| Issue | Category | File(s) | Fix Type | Priority |
|-------|----------|---------|----------|----------|
| cec2022-023 | SEARCH_FAILURE + INTERPRETATION | `core/agent.py` | Code + Prompt | **HIGH** |
| cec2022-038 | MISSING_TOOL | `core/cec_table_tools.py`, `core/tools.py` | New Tool | Medium |
| cec2022-045 | TOOL_LOGIC | `core/tools.py`, `core/cec_table_tools.py` | Code Fix | Medium |
| cec2022-001 | N/A (agent correct) | `eval/standardized_llm-as-judge/CEC2022_eval_questions.json` | Expected Answer | Low |
| cec2022-021 | N/A (valid method) | None | None | None |

---

## Implementation Order

1. **cec2022-023 - AFCI Enforcement (HIGH PRIORITY)**
   - Why first: Safety-critical error affecting circuit protection questions
   - Impact: All GFCI/AFCI combination questions
   - Effort: Medium (prompt + enforcement logic)

2. **cec2022-045 - Sections Structure Handling**
   - Why second: Affects multiple tables with sections structure
   - Impact: Table 110.28 and similar multi-section tables
   - Effort: Low (simple code addition)

3. **cec2022-038 - California Tables Enumeration Tool**
   - Why third: Nice-to-have for "how many" questions
   - Impact: Enumeration/count questions about CA amendments
   - Effort: Low (new function)

4. **cec2022-001 - Update Expected Answer**
   - Why last: Not an agent error, just expected answer precision
   - Impact: Evaluation accuracy only
   - Effort: Minimal

---

## Key Takeaways

1. **The AFCI issue is the only REAL error** - Agent hallucinated outdated code knowledge
2. **Data is generally good** - All issues stem from tool logic or agent interpretation, not missing data
3. **Enforcement needs enhancement** - Current anti-hallucination only checks IF tools called, not WHAT was searched
4. **Some expected answers need review** - cec2022-001's expected "20A" conflates ampacity and OCP
