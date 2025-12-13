# Investigation Report: cec2022-035 Regression from Run 39 (10/10) to Run 41 (8/10)

## Question Details
- **ID**: cec2022-035 (original_id: cec-007)
- **Question**: "What does CEC Table 240.4(G) specify that is unique to California?"
- **Category**: overcurrent
- **Tier**: california_specific

## Summary of Regression
- **Run 39**: Agent received 10/10 (PASS)
- **Run 41**: Agent received 8/10 (judge score unavailable due to API error, but previously scored 8/10 in Run 12)
- **Issue**: Agent doesn't clearly state the specific California-modified values in Table 240.4(G)

## Tool Calls Comparison

### Run 39
- **Tools called**: `cec_lookup_table("240.4(G)")` only
- **Agent answer**: Correctly identified table as cross-reference guide with California amendments. Called out fire alarm exceptions (760.43, 645.3(B)(5), 250.162(A)(3)) and electric welder exceptions (630.12(A)). Stated "Always verify cross-referenced sections for local amendments."

### Run 41
- **Tools called**: `cec_lookup_table("240.4(G)")` only
- **Agent answer**: Says "CEC Table 240.4(G) itself is not uniquely modified in California (it mirrors NEC Table 240.4(G))." Then discusses fire alarm and HVAC implications via California amendments but doesn't clearly state what's modified IN THE TABLE.

## Root Cause Analysis

### 1. Expected Answer Evolution
The expected answer for this question **changed significantly** between earlier runs and the standardized evaluation set:

**OLD expected answer** (used in Runs 2-20):
> "CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023."

**NEW expected answer** (standardized, used in Run 35+):
> "CEC Table 240.4(G) provides overcurrent protection requirements for small conductors. Note: Table 240.4(G) exists in BOTH CEC 2022 and NEC 2023, but California has modified values. The table specifies maximum overcurrent protection for conductors including fixture wires and flexible cords."

**Impact**: The old expected answer was FACTUALLY INCORRECT. It claimed the table doesn't exist in NEC 2023, which is false. The new expected answer correctly identifies that the table exists in both codes but California has modified it.

### 2. Actual California Modifications in Table 240.4(G)

I compared `C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\data\CEC_2022\cec_tables_unified.json` with `C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\data\NEC_2023\nec_tables_unified.json`:

**Difference #1: Air-conditioning and refrigeration equipment**
- NEC 2023: Article "440, Parts III, IV, VI"
- CEC 2022: Article "440, Parts III, VI"
- **California removes Part IV reference**

**Difference #2: Control and instrumentation circuit conductors (Type ITC)**
- NEC 2023: Article "335", Section "335.9"
- CEC 2022: Article "727", Section "727.9"
- **California changes article from 335 to 727**

**Difference #3: Remote-control, signaling, and power-limited circuit conductors**
- NEC 2023: Section "724.43, 724.45, 725.60, and Chapter 9, Tables 11(A) and 11(B)"
- CEC 2022: Section "725.43, 725.45, 725.121, and Chapter 9, Tables 11(A) and 11(B)"
- **California uses different section references (725.43/725.45/725.121 vs NEC's 724.43/724.45/725.60)**
- Note: NEC appears to have a typo with "724.43" instead of "725.43"

**Metadata differences**:
- CEC table includes `"california_amendment": true` and `"amendment_type": "delta"`
- CEC description explicitly states: "California amendment (delta) indicates modifications from the base NEC"

### 3. Tool Output Analysis

Both Run 39 and Run 41 called `cec_lookup_table("240.4(G)")` and received **identical tool output**:

```
CEC 2022 Table 240.4(G) - Specific Conductor Applications
Section: Article 240
Description: Cross-reference table for overcurrent protection requirements of specific conductor types...
California amendment (delta) indicates modifications from the base NEC.

[Full table listing conductors and their article/section references]
```

**The problem**: The tool output does NOT show a side-by-side comparison with NEC values. It only shows the CEC table with a note that "California amendment (delta) indicates modifications from the base NEC" but doesn't specify WHICH rows/values are modified.

### 4. Agent Behavior Difference

**Run 39** (10/10):
- Correctly identified the table as a cross-reference guide with California amendments
- Searched for and found specific exceptions (fire alarm systems, electric welders)
- Explicitly stated: "Always verify cross-referenced sections for local amendments"
- The reflection phase called additional exception_search tools for 760.43 and 630.12

**Run 41** (8/10):
- Incorrectly stated "CEC Table 240.4(G) itself is not uniquely modified in California (it mirrors NEC Table 240.4(G))"
- Focused on cross-referenced sections (760.43, 440) having California amendments
- Did NOT mention the actual table row differences (Article 440 Parts, Article 727 vs 335, Section differences)
- Reflection verified the answer as complete without additional tool calls

### 5. Why the Regression?

The Run 41 agent **missed the key insight** that the table rows themselves contain different values from NEC. Specifically:

1. The agent said "mirrors NEC" when it should have identified the 3 specific row differences
2. The tool output doesn't explicitly highlight which rows differ from NEC
3. The agent would need to call BOTH `cec_lookup_table("240.4(G")` AND `lookup_table("240.4(G")` (NEC version) to see the differences side-by-side
4. OR the tool output needs to be augmented with delta markers on modified rows

## Proposed Fixes (DO NOT IMPLEMENT)

### Option 1: Enhance Tool Output (Recommended)
Modify `cec_lookup_table` to include delta markers on rows that differ from NEC:

```python
# In core/cec_table_tools.py
def cec_lookup_table(table_id: str) -> str:
    cec_table = get_cec_table(table_id)
    nec_table = get_nec_table(table_id)  # Also fetch NEC version

    # Compare rows and add delta markers
    if nec_table:
        for row_idx, cec_row in enumerate(cec_table['rows']):
            if row_idx < len(nec_table['rows']):
                nec_row = nec_table['rows'][row_idx]
                if cec_row != nec_row:
                    # Add delta marker to output
                    row_output += " ⚠️ CALIFORNIA MODIFICATION (differs from NEC 2023)"

    return formatted_output
```

### Option 2: Update Expected Answer
The current expected answer is vague: "California has modified values." It should be more specific:

```
Expected Answer (Option 2):
"CEC Table 240.4(G) provides overcurrent protection cross-references for specific conductor applications.
This table exists in both CEC 2022 and NEC 2023, but California has modified THREE entries:
1. Air-conditioning/refrigeration: CEC omits Part IV (only Parts III, VI vs NEC's III, IV, VI)
2. Type ITC conductors: CEC references Article 727 (vs NEC's Article 335)
3. Remote-control/signaling conductors: CEC uses sections 725.43/725.45/725.121 (vs NEC's 724.43/724.45/725.60)"
```

### Option 3: Add Comparison Tool
Create a new tool `cec_compare_with_nec(table_id)` that shows side-by-side differences:

```python
def cec_compare_with_nec(table_id: str) -> str:
    """Compare CEC and NEC versions of a table, highlighting California modifications"""
    return """
    COMPARISON: CEC vs NEC Table 240.4(G)

    Row 1: Air-conditioning/refrigeration
      - NEC: 440, Parts III, IV, VI
      - CEC: 440, Parts III, VI  ← CALIFORNIA REMOVES PART IV

    Row 3: Type ITC conductors
      - NEC: Article 335, Section 335.9
      - CEC: Article 727, Section 727.9  ← CALIFORNIA CHANGES ARTICLE

    [etc.]
    """
```

### Option 4: Agent Prompt Enhancement
Add guidance to the agent system prompt for California-specific table questions:

```
When answering questions about "what is unique to California" for tables:
1. Look up the table in CEC
2. If the table has california_amendment=true, also look up the NEC version
3. Compare row-by-row to identify specific differences
4. State the specific modified values, not just "California has amendments"
```

## Conclusion

**Root cause**: The agent cannot easily identify which specific rows/values in Table 240.4(G) differ from NEC because:
1. The tool output doesn't highlight row-level differences
2. The agent would need to call both CEC and NEC lookup tools and manually compare
3. LLM variance caused Run 41 to say "mirrors NEC" vs Run 39 correctly identifying amendments

**Best fix**: Option 1 (Enhance Tool Output) - Add delta markers to table tool output showing which rows differ from NEC, with specific value comparisons inline. This makes California modifications immediately visible without requiring the agent to call multiple tools or do manual comparison.

**Second-best fix**: Option 3 (Comparison Tool) - Create dedicated `cec_compare_with_nec` tool for side-by-side comparison, but this requires the agent to know to call it for California-specific questions.

**Files to modify** (for Option 1):
- `C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\core\cec_table_tools.py` - Enhance `cec_lookup_table()` function
- `C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\data\NEC_2023\nec_tables_unified.json` - Already available for comparison
- `C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\data\CEC_2022\cec_tables_unified.json` - Already has `california_amendment: true` flag
