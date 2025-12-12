# Solutions Analysis for Run $ARGUMENTS

Analyze wrong/partial answers from Run $ARGUMENTS and investigate root causes thoroughly.

## Input Files
- Wrong answers file: `eval/runs/run $ARGUMENTS*/wrong_answers - run$ARGUMENTS.md`
- Judge report: `eval/runs/run $ARGUMENTS*/judge_report - run$ARGUMENTS.md`
- Evaluation results: `eval/runs/run $ARGUMENTS*/run$ARGUMENTS_evaluation_results_*.json`

## Output File
Create: `eval/runs/run $ARGUMENTS*/solutions - run$ARGUMENTS.md`

## Instructions

1. **Read the wrong_answers file** to get the list of questions that scored below 10/10

2. **For each wrong/partial answer, launch a parallel subagent** (use Task tool with subagent_type="general-purpose") to investigate:

   Each subagent should:

   a. **Understand the failure**
      - Read the question, expected answer, and agent's answer
      - Identify what specifically went wrong

   b. **Trace the tool chain**
      - Check which tools were called (from evaluation results JSON)
      - Read the relevant tool code:
        - `core/cec_knowledge_tools.py` - for search issues
        - `core/cec_table_tools.py` - for table lookup issues
        - `core/nec_knowledge_tools.py` / `core/nec_table_tools.py` - if NEC tools used
        - `core/agent.py` - for agent logic/prompt issues
        - `core/tools.py` - for tool definitions

   c. **Check the data sources**
      - For table issues: Read `data/CEC_2022/cec_tables_unified.json` or `data/NEC_2023/nec_tables_unified.json`
      - Verify if the expected data exists in the JSON
      - Check for typos, missing entries, wrong values

   d. **Test the hypothesis**
      - If search issue: Use Grep to search for the expected content in data files
      - If table issue: Read the specific table from JSON to confirm
      - If prompt issue: Read the system prompt in agent.py

   e. **Determine root cause** (one of):
      - MISSING_DATA: Data not in JSON tables
      - WRONG_DATA: Data exists but has incorrect values
      - SEARCH_FAILURE: Search didn't return relevant results
      - TOOL_LOGIC: Tool code has a bug or limitation
      - PROMPT_ISSUE: System prompt needs clarification
      - UNIT_ERROR: Wrong units used in calculation/lookup
      - INTERPRETATION: Agent misinterpreted code requirements

   f. **Propose general fix** (NOT hardcoded answers):
      - For MISSING_DATA: Specify what to add to which JSON file
      - For WRONG_DATA: Specify correction needed
      - For SEARCH_FAILURE: Suggest search index or query improvements
      - For TOOL_LOGIC: Describe code change needed
      - For PROMPT_ISSUE: Propose prompt addition/modification
      - For UNIT_ERROR: Suggest validation or conversion logic
      - For INTERPRETATION: Propose clarifying guidance

3. **Wait for all subagents to complete** using AgentOutputTool

4. **Compile the solutions report** with this format:

```markdown
# Solutions Analysis - Run $ARGUMENTS

**Date:** [today's date]
**Wrong/Partial Answers Analyzed:** [count]

## Executive Summary
[Brief overview of main issues found and fix categories]

## Issue Analysis

### Issue 1: [Question ID] - [Brief Description]

**Score:** X/10
**Root Cause Category:** [MISSING_DATA | WRONG_DATA | SEARCH_FAILURE | TOOL_LOGIC | PROMPT_ISSUE | UNIT_ERROR | INTERPRETATION]

**Investigation:**
- Tools called: [list]
- Files examined: [list]
- Data checked: [what was verified]

**Findings:**
[Detailed explanation of what went wrong and why]

**Evidence:**
[Code snippets, JSON excerpts, or search results that confirm the issue]

**Proposed Fix:**
- **Type:** [Data | Code | Prompt]
- **File(s):** [which files to modify]
- **Change:** [specific change needed - general rule, not hardcoded answer]
- **Generalization:** [how this fix helps similar questions]

---

[Repeat for each issue]

## Summary of Fixes

| Issue | Category | File | Fix Type | Priority |
|-------|----------|------|----------|----------|
| ... | ... | ... | ... | High/Medium/Low |

## Implementation Order
1. [First fix - why first]
2. [Second fix]
...
```

5. **Do NOT implement any fixes** - only document findings and proposals

## Important Notes
- Be thorough - dig into the actual code and data
- Propose GENERAL solutions that will help with similar questions
- Never suggest hardcoding specific answers
- Prioritize fixes by impact (how many questions affected)
- Include code snippets and JSON excerpts as evidence
