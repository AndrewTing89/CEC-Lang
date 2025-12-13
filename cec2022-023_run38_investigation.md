# Investigation: cec2022-023 Still Partially Wrong in Run 38

## Question
New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI.

## Expected Answer
All circuits require AFCI per 210.12(A). Countertop, dishwasher, disposal need combo AFCI/GFCI. Refrigerator needs AFCI.

## Agent's Answer (Run 38)
- **Countertop**: Combination AFCI/GFCI ✓ (CORRECT - Fixed from Run 37)
- **Dishwasher**: GFCI only (AFCI "Not required") ✗
- **Disposal**: GFCI only (AFCI "Not required") ✗
- **Refrigerator**: Standard Breaker (AFCI "Not required") ✗

## Root Cause: SEARCH_FAILURE (Agent never searched for AFCI)

### Evidence

#### 1. Tool Calls Made
The agent made **ONLY ONE** tool call across all 3 iterations:
```
Iteration 1: cec_search(query="210.8 kitchen receptacles GFCI", limit=5)
Iteration 2: No tools called
Iteration 3: No tools called
```

**The agent NEVER searched for AFCI requirements.**

#### 2. What CEC 2022 Actually Says

**Section 210.12(A)** explicitly states:
> "All 120-volt, single-phase, 15- and 20-ampere branch circuits supplying outlets or devices installed in dwelling unit **kitchens**, family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, or similar rooms or areas shall be protected by any of the means described in 210.12(A)(1) through (6)"

**The ONLY exception** is:
> "Exception: AFCI protection shall not be required for an individual branch circuit supplying a **fire alarm system** installed in accordance with 760.41(B) or 760.121(B)."

**There are NO exceptions for:**
- Refrigerators
- Dishwashers
- Garbage disposals
- Any dedicated appliance circuits in kitchens

#### 3. Agent Hallucinated Non-Existent Exceptions

From the agent's answer:
- Dishwasher: "AFCI: **Not required** (not listed in 210.12(A) exceptions for AFCI exemptions)"
- Disposal: "AFCI: **Not required** (not listed in 210.12(A) exceptions for AFCI exemptions)"
- Refrigerator: "AFCI: **Not required** (CEC 210.12(A) exceptions include circuits for refrigerators, freezers, etc.)"

**These exceptions DO NOT EXIST in CEC 2022.**

The agent fabricated these conclusions based on ZERO search evidence about AFCI.

#### 4. Why Countertop Got Fixed But Others Didn't

The countertop got the correct answer (combo AFCI/GFCI) likely because:
1. The search for GFCI returned 210.8(A)(6) which explicitly mentions "kitchen countertop"
2. The agent may have recognized "countertop" as a high-visibility area and applied AFCI based on general knowledge
3. The DOMAIN KNOWLEDGE hint about searching for "all three together" may have partially influenced reasoning for countertop only

But for dedicated appliance circuits, the agent:
1. Found GFCI requirements via 422.5(A)(7) for dishwasher
2. Assumed (incorrectly) that dedicated circuits are exempt from AFCI
3. Never verified this assumption by searching 210.12

### Why Domain Knowledge Failed

The current DOMAIN KNOWLEDGE section says:
```
### Circuit Protection
When a question mentions GFCI, AFCI, or CAFCI - search for ALL THREE together.
```

**This is too weak because:**
1. It's just a guideline, not enforced
2. The agent can ignore it (and did)
3. The enforcement layer (line 664 in agent.py) is DISABLED: "Specialized tool enforcement removed"

## Category Assignment

**ROOT CAUSE**: **SEARCH_FAILURE** (Combined with ENFORCEMENT_GAP)
- Agent never searched for AFCI requirements
- No enforcement mechanism caught this omission
- Hallucinated exceptions based on incorrect assumptions

**NOT** interpretation failure - the agent never saw the correct text.

## Proposed Fix

### Option 1: MANDATORY MULTI-TOPIC SEARCH (Recommended)

When question contains circuit protection keywords, **enforce** multiple searches:

```python
# In agent.py _check_required_tools()

def _detect_circuit_protection_topics(self, question: str) -> list:
    """
    Detect if question asks about circuit protection.
    Return list of required search topics.
    """
    q_lower = question.lower()
    protection_keywords = ['gfci', 'afci', 'cafci', 'circuit protection',
                          'breaker', 'protection required']

    if any(kw in q_lower for kw in protection_keywords):
        # Kitchen/dwelling unit context requires both GFCI and AFCI
        if any(loc in q_lower for loc in ['kitchen', 'dwelling', 'residential', 'bedroom', 'living room']):
            return ['gfci', 'afci']  # Must search both

    return []

def _check_required_tools(self, question, all_tool_calls, ...):
    # ... existing search check ...

    # NEW: Circuit protection enforcement
    required_topics = self._detect_circuit_protection_topics(question)
    if required_topics:
        search_queries = []
        for tc in all_tool_calls:
            if tc.get("name") == "cec_search":
                query = tc.get("args", {}).get("query", "").lower()
                search_queries.append(query)

        for topic in required_topics:
            topic_searched = any(topic in q for q in search_queries)
            if not topic_searched:
                return (False, f"protection_topic:{topic}")

    return (True, None)
```

Then add enforcement message:
```python
elif missing_type.startswith("protection_topic:"):
    topic = missing_type.split(":")[1].upper()
    messages.append(HumanMessage(
        content=f"ENFORCEMENT: Questions about circuit protection in dwelling units require checking {topic} requirements. "
               f"You searched for some protection types but not {topic}. "
               f"Search for Section 210.12 (AFCI) or 210.8 (GFCI) to find {topic} requirements. "
               f"DO NOT answer from memory about protection requirements."
    ))
```

### Option 2: STRENGTHEN DOMAIN KNOWLEDGE (Less Reliable)

Make the instruction more explicit and emphatic:

```
### Circuit Protection (MANDATORY SEARCH)
**CRITICAL**: Questions about GFCI, AFCI, or circuit breaker protection in dwelling units require SEARCHING FOR BOTH:
1. Section 210.8 (GFCI requirements)
2. Section 210.12 (AFCI requirements)

DO NOT assume dedicated circuits are exempt from AFCI. Kitchens require AFCI for ALL circuits per 210.12(A).

Search pattern:
- First search: "210.8 GFCI [location]"
- Second search: "210.12 AFCI dwelling unit [location]"
```

### Option 3: HYBRID (Most Robust)

Combine both:
1. Strengthen domain knowledge with explicit section numbers
2. Add enforcement to catch when it's ignored

## Why This Generalizes

This fix addresses a broader pattern:
- **Multi-topic questions** where agent searches for one topic but not others
- **Common misconceptions** (e.g., "dedicated circuits don't need AFCI")
- **Questions requiring coordination** between multiple code sections

Similar questions that would benefit:
- "What protection is required for bathroom receptacles?" (needs GFCI + AFCI)
- "Size conductors and protection for workshop circuits?" (needs ampacity + OCP + AFCI/GFCI)
- "Requirements for outdoor kitchen receptacles?" (needs GFCI + AFCI + weatherproof)

## Implementation Priority

**HIGH** - This is a systematic failure mode where:
1. Agent confidently states non-existent exceptions
2. Gives partially correct answers (dangerous for inspection work)
3. No verification catches the omission

The enforcement approach (Option 1) is recommended because it provides deterministic protection against this failure mode, while prompt-only fixes (Option 2) are easily ignored by the LLM.
