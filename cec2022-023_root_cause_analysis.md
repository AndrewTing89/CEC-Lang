# Root Cause Analysis: cec2022-023 - AFCI Misconception

## Executive Summary

**Question ID**: cec2022-023
**Question**: Kitchen circuits protection requirements (countertop, dishwasher, disposal, refrigerator)
**Wrong Answer**: Agent stated "210.12 applies only to bedroom circuits" and said AFCI is NOT required
**Correct Answer**: CEC 2022 Section 210.12(A) requires AFCI for ALL dwelling unit 120V circuits including kitchens
**Root Cause**: **SEARCH_FAILURE + INTERPRETATION ERROR**

---

## What the Agent Got Wrong

The agent concluded in its "Inspector Notes":
> **GFCI vs. AFCI**: None of these circuits require **AFCI** protection (210.12 applies only to bedroom circuits).

This statement is **completely false**. CEC 2022 Section 210.12(A) explicitly requires AFCI for kitchens.

---

## Evidence Analysis

### 1. What the Code Actually Says

**CEC 2022 Section 210.12(A) - Dwelling Units**:
```
All 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets
or devices installed in dwelling unit kitchens, family rooms, dining rooms,
living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms,
closets, hallways, laundry areas, or similar rooms or areas shall be protected
by any of the means described in 210.12(A)(1) through (6)
```

**Key Finding**: The word **"kitchens"** appears FIRST in the list, even before bedrooms. AFCI applies to:
- Kitchens ✓
- Family rooms ✓
- Dining rooms ✓
- Living rooms ✓
- Parlors ✓
- Libraries ✓
- Dens ✓
- **Bedrooms** ✓ (not ONLY bedrooms!)
- Sunrooms ✓
- Recreation rooms ✓
- Closets ✓
- Hallways ✓
- Laundry areas ✓

### 2. What the Agent Actually Searched For

**Tools Called** (from trace):
```
1. cec_search: "kitchen countertop receptacles GFCI requirement"
```

**Critical Finding**: The agent ONLY searched for GFCI requirements. It never searched for:
- "AFCI requirements"
- "210.12"
- "arc-fault protection"
- "kitchen circuit protection"

### 3. What the Search Returned

The `cec_search` for "kitchen countertop receptacles GFCI requirement" returned:
- Result 1: 210.52(A) - Receptacle spacing requirements ❌ (not relevant)
- Result 2: 210.52(D) - Bathroom receptacles ❌ (not relevant)
- Result 3: 210.8 - GFCI requirements ✓ (relevant for GFCI, but doesn't mention AFCI)
- Result 4: 406.5 - Receptacle mounting ❌ (not relevant)
- Result 5: 210.52(C) - Countertop receptacles ❌ (not relevant)

**Critical Finding**: Section 210.12 (AFCI requirements) was NOT returned in the search results because the agent searched for "GFCI" not "AFCI" or "arc-fault".

### 4. What the Data Contains

I verified that the CEC data DOES contain the correct 210.12(A) text with kitchens listed:

**File**: `C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\data\CEC_2022\cec_content\chapter2_structured_fixedheaders.md`

**Line 518**:
```markdown
##### (A) Dwelling Units. All 120-volt, single-phase, 15- and 20-ampere branch
circuits supplying outlets or devices installed in dwelling unit kitchens, family
rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms,
recreation rooms, closets, hallways, laundry areas, or similar rooms or areas
shall be protected by any of the means described in 210.12(A)(1) through (6): ∆
```

**Data Quality**: ✓ Correct content is indexed and available

---

## Root Cause Classification

### PRIMARY CAUSE: **SEARCH_FAILURE**

The agent failed to search for AFCI requirements at all. It only searched for GFCI requirements.

**Why This Happened**:
1. The question explicitly asked about "standard breaker, GFCI, **AFCI**, or combination AFCI/GFCI"
2. The agent decomposed the question but focused only on GFCI (the more familiar requirement)
3. The agent did not follow its own DECOMPOSE protocol to search for each protection type separately

**Expected Behavior** (per system prompt STEP 1: DECOMPOSE):
```
Sub-questions:
1. Kitchen countertop receptacles - what protection? (GFCI? AFCI? Both?)
2. Dishwasher circuit - what protection?
3. Garbage disposal - what protection?
4. Refrigerator - what protection?

Search plan:
- cec_search("kitchen GFCI requirements")
- cec_search("kitchen AFCI requirements")  ← MISSED THIS
- cec_search("210.12 AFCI dwelling units")  ← MISSED THIS
```

### SECONDARY CAUSE: **INTERPRETATION ERROR (Hallucination)**

Even though the agent didn't search for AFCI, it confidently stated a FALSE rule:
> "210.12 applies only to bedroom circuits"

**This is a hallucination**. The agent invented this restriction from:
- **Memory of old NEC code**: Prior to NEC 2014, AFCI WAS only required for bedrooms
- **Outdated knowledge**: The model was trained on data that may include old code versions
- **Confabulation**: When lacking search results, the LLM filled in with plausible-sounding but incorrect information

**Anti-Hallucination Layer Failed**: The agent's first-iteration tool enforcement should have prevented this, but the agent DID call a tool (cec_search for GFCI), so the enforcement was satisfied even though it searched for the wrong thing.

---

## Why the Anti-Hallucination System Failed

### Current Enforcement (from `core/agent.py` lines 1119-1132):

```python
# LAYER 2: ANTI-HALLUCINATION CHECK
# If first iteration and no tools called, force tool usage
if iteration == 1 and not has_tool_calls and not all_tool_calls:
    if self.verbose:
        print("  [!] ANTI-HALLUCINATION: No tool calls in first response. Forcing search.")
    messages.append(HumanMessage(
        content="ERROR: You MUST call CEC search tools before answering. "
               "You cannot answer from memory. Call cec_search NOW to retrieve verified code data."
    ))
    continue  # Force another iteration
```

**Gap Identified**: This enforcement checks IF tools were called, but not WHETHER THE RIGHT TOOLS were called or whether SUFFICIENT searches were performed.

In this case:
- ✓ Agent called a tool (cec_search)
- ✗ Agent searched for the wrong thing (GFCI instead of AFCI)
- ✗ Agent invented a rule from memory ("only bedrooms")

---

## Why the Reflection Phase Missed This

The reflection phase (lines 1236-1382) verified the answer and returned:
```
[VERIFIED] Answer is complete.
```

**Reflection Failed Because**:
1. The reflection prompt asks "Did you check for exceptions?" but doesn't ask "Did you search for ALL protection types mentioned in the question?"
2. The reflection didn't catch that AFCI was mentioned in the question but never searched for
3. The LLM in reflection mode also hallucinated the "bedrooms only" rule

---

## Proposed Fixes

### Fix 1: **Enhanced Question Decomposition Enforcement** (HIGH PRIORITY)

**Location**: `core/agent.py` - Add new enforcement in `_verify_required_tools()`

**Current Code** (line 609-691):
```python
def _verify_required_tools(self, question: str, all_tool_calls: List,
                           force_nec_comparison: bool = False,
                           tool_output_hints: list = None) -> tuple:
    """Check if required tools were called"""
    tools_called = {tc.get("name", "") for tc in all_tool_calls}

    # Check for at least one search
    has_search = any(t in tools_called for t in search_tools)
    if not has_search:
        return (False, "search")
```

**Proposed Enhancement**:
```python
def _verify_required_tools(self, question: str, all_tool_calls: List,
                           force_nec_comparison: bool = False,
                           tool_output_hints: list = None) -> tuple:
    """Check if required tools were called"""
    tools_called = {tc.get("name", "") for tc in all_tool_calls}

    # Check for at least one search
    has_search = any(t in tools_called for t in search_tools)
    if not has_search:
        return (False, "search")

    # NEW: Check if question mentions specific protection types
    q_lower = question.lower()
    protection_types = []
    if "gfci" in q_lower:
        protection_types.append("gfci")
    if "afci" in q_lower:
        protection_types.append("afci")
    if "arc-fault" in q_lower or "arc fault" in q_lower:
        protection_types.append("afci")

    # Verify that searches covered all mentioned protection types
    if protection_types:
        search_queries = []
        for tc in all_tool_calls:
            if tc.get("name") == "cec_search":
                query = tc.get("args", {}).get("query", "").lower()
                search_queries.append(query)

        for ptype in protection_types:
            # Check if this protection type was searched
            searched = any(ptype in q for q in search_queries)
            if not searched:
                return (False, f"protection_type:{ptype}")

    # ... rest of existing checks ...
```

**Enforcement Message** (line 1200-1204):
```python
elif missing_type.startswith("protection_type:"):
    ptype = missing_type.split(":", 1)[1].upper()
    messages.append(HumanMessage(
        content=f"INCOMPLETE: The question asks about {ptype} protection, but you haven't "
               f"searched for {ptype} requirements yet. Call cec_search('{ptype} requirements') "
               f"or cec_search('210.8' for GFCI / '210.12' for AFCI) NOW to verify this requirement."
    ))
```

### Fix 2: **Add AFCI Guidance to System Prompt** (MEDIUM PRIORITY)

**Location**: `core/agent.py` line 98-449 (SYSTEM_PROMPT)

**Add After Line 446** (in Examples section):
```markdown
### Example 6: Multi-Protection Questions (GFCI + AFCI)

**Question:** "Kitchen circuits - what protection is required: GFCI, AFCI, or both?"

**Reasoning:**
DECOMPOSE protection types mentioned:
→ [1] GFCI requirements (210.8)
→ [2] AFCI requirements (210.12)

SEARCH PLAN - must search for EACH protection type:
→ [1] cec_search("kitchen GFCI requirements 210.8")
→ [2] cec_search("kitchen AFCI requirements 210.12")

CRITICAL: When question mentions multiple protection types (GFCI, AFCI, etc.),
you MUST search for EACH type separately. DO NOT assume only one applies.

**Common Misconception to Avoid:**
- ✗ WRONG: "AFCI only applies to bedrooms" (outdated - pre-2014 NEC)
- ✓ CORRECT: CEC 2022 Section 210.12(A) requires AFCI for ALL dwelling unit 120V circuits:
  kitchens, bedrooms, living rooms, dining rooms, family rooms, laundry, hallways, etc.

**Answer:**
## Kitchen Circuit Protection (CEC 2022)

**GFCI Required**: Yes - CEC 210.8(A)(6) for countertop receptacles
**AFCI Required**: Yes - CEC 210.12(A) for all 120V circuits in dwelling units

Kitchen circuits require **BOTH** GFCI and AFCI protection (combination AFCI/GFCI breaker).

[OK] Source: CEC 2022
```

### Fix 3: **Enhanced Reflection Prompt** (LOW PRIORITY)

**Location**: `core/agent.py` line 457-474 (REFLECTION_PROMPT)

**Current Code**:
```python
REFLECTION_PROMPT = """## SELF-VERIFICATION CHECK

Review your answer for completeness:

1. **All Parts Answered**: Did you address every part of the question?

2. **Code Citations**: Did you cite specific code sections for each claim?

3. **Exceptions & Cross-References**: Did you check for exceptions...
```

**Proposed Enhancement**:
```python
REFLECTION_PROMPT = """## SELF-VERIFICATION CHECK

Review your answer for completeness:

1. **All Parts Answered**: Did you address every part of the question?

2. **All Protection Types Searched**: If the question mentions GFCI, AFCI, or other
   protection types, did you search for EACH type separately? List the protection
   types mentioned and verify you searched for each.

3. **Code Citations**: Did you cite specific code sections for each claim?

4. **No Memory-Based Rules**: Did you verify EVERY requirement with a tool search,
   or did you state any rules from memory? If you stated "X only applies to Y",
   did you verify this with cec_search to ensure it's current CEC 2022?

5. **Exceptions & Cross-References**: Did you check for exceptions...
```

### Fix 4: **Add AFCI Hint to GFCI Tool Description** (LOW PRIORITY)

**Location**: `core/tools.py` line 48-76 (cec_search tool)

**Current Description** (line 48):
```python
@tool
def cec_search(query: str, article_filter: Optional[str] = None, limit: int = 5) -> str:
    """[PRIMARY] Search CEC 2022 California Electrical Code - USE THIS FIRST.

    This is the DEFAULT search tool for ALL electrical code questions.
    ...
```

**Proposed Enhancement**:
```python
@tool
def cec_search(query: str, article_filter: Optional[str] = None, limit: int = 5) -> str:
    """[PRIMARY] Search CEC 2022 California Electrical Code - USE THIS FIRST.

    This is the DEFAULT search tool for ALL electrical code questions.
    ...

    IMPORTANT FOR PROTECTION REQUIREMENTS:
    - If question asks about circuit protection types (GFCI, AFCI, etc.), search for EACH type
    - GFCI: Section 210.8 (ground-fault protection)
    - AFCI: Section 210.12 (arc-fault protection) - applies to ALL dwelling unit 120V circuits,
      NOT just bedrooms (common misconception from old NEC code)
    - Kitchen circuits typically require BOTH GFCI (210.8) AND AFCI (210.12)

    Returns:
        Relevant CEC sections with citations, table data, and cross-references
    """
```

---

## Testing the Fix

### Test Case 1: Original Question
**Question**: Kitchen circuits protection requirements
**Expected Behavior After Fix**:
1. Agent searches: "kitchen GFCI requirements"
2. Enforcement detects AFCI mentioned in question but not searched
3. Agent forced to search: "kitchen AFCI requirements" or "210.12"
4. Agent finds 210.12(A) listing kitchens
5. Agent correctly answers: "BOTH GFCI and AFCI required"

### Test Case 2: Bedroom Circuits
**Question**: Bedroom circuits protection requirements
**Expected**: Agent correctly identifies AFCI (210.12) applies

### Test Case 3: Garage Circuits
**Question**: Garage receptacle protection requirements
**Expected**: Agent identifies GFCI (210.8) but not AFCI (garages not in 210.12(A) list)

---

## Recommended Action Plan

1. **Implement Fix 1** (Enhanced Question Decomposition) - Prevents search failures
2. **Implement Fix 2** (System Prompt Enhancement) - Educates model about common misconception
3. **Test on cec2022-023** - Verify fix resolves this specific case
4. **Run full evaluation suite** - Ensure no regressions
5. **Consider Fix 3 & 4** - Additional safeguards if issues persist

---

## Conclusion

**Root Cause**: SEARCH_FAILURE (agent didn't search for AFCI) + INTERPRETATION ERROR (hallucinated "bedrooms only" rule)

**Primary Fix**: Enhanced enforcement in `_verify_required_tools()` to detect when question mentions protection types that weren't searched

**Impact**: HIGH - This affects all questions about circuit protection requirements (GFCI, AFCI, OCPD, etc.)

**Estimated Fix Complexity**: MEDIUM - Requires pattern matching on question text and search query verification
