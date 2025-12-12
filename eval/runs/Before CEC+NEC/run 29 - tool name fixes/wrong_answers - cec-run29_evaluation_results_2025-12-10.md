# Wrong Answers - cec-run29_evaluation_results_2025-12-10

**Model:** CEC Lang Agent (qwen/qwen3-32b)
**Judge:** Claude Code (Opus)
**Overall Score:** 87.6% (254/290)

---

## Executive Summary
**Questions with Errors:** 12 of 29
**Perfect Scores:** 17

---

## Detailed Error Analysis

### 1. cec-020 (Score: 5/10) - CRITICAL ERROR
**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire according to California code?
**Accuracy:** 2/5 - Incorrect temperature value
**Completeness:** 3/5 - Found correct table but wrong value
**Specific Errors:**
- INCORRECT: States maximum operating temperature is **105°C**
- CORRECT ANSWER: **200°C (392°F)** per CEC 2022 Table 402.3
- This is a significant error - off by nearly 100°C
- The agent identified the correct table (402.3) but retrieved wrong value

---

### 2. cec-019 (Score: 7/10)
**Question:** What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?
**Accuracy:** 3/5 - Incorrect ampacity value
**Completeness:** 4/5 - Good explanation but wrong value
**Specific Errors:**
- INCORRECT: States ampacity is **20 amperes**
- CORRECT ANSWER: **25 amperes** per CEC 2022 Table 400.5(A)(1)
- Agent correctly identified the table but provided wrong value
- Note: Agent correctly distinguished flexible cord tables from fixed wiring tables

---

### 3. cec-026 (Score: 7/10)
**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?
**Accuracy:** 3/5 - Comparison correct but conclusion framing unclear
**Completeness:** 4/5 - Good details but confusing conclusion
**Specific Errors:**
- States "NEC 2023 is more restrictive" which is technically correct, but expected answer frames it as "CEC 2022 is MORE PERMISSIVE"
- The key distinction: CEC limits GFCI to countertops and within 6 feet of sink; NEC requires GFCI for ALL kitchen receptacles including refrigerators and built-in microwaves
- Response correctly identifies this but the conclusion could be clearer

---

### 4. cec-022 (Score: 8/10)
**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.
**Accuracy:** 4/5 - Some sizing may be incorrect
**Completeness:** 4/5 - All components addressed
**Specific Errors:**
- Service conductors: States **2/0 AWG** (per Table 310.12(A)) vs expected **3/0 AWG** (per Table 310.16)
- Table 310.12(A) is specifically for dwelling services and may allow smaller conductors
- GEC: States **6 AWG** but expected is **4 AWG** (based on 3/0 service conductors per Table 250.66)
- EGC: States **6 AWG** which matches expected answer
- NOTE: The 2/0 AWG from Table 310.12(A) may be acceptable for dwelling services specifically

---

### 5. cec-007 (Score: 8/10)
**Question:** What does CEC Table 240.4(G) specify that is unique to California?
**Accuracy:** 4/5 - Unclear if table is California-specific
**Completeness:** 4/5 - Provides context but doesn't definitively answer
**Specific Errors:**
- Response states table is "identical to NEC Table 240.4(G)"
- Expected answer states "CEC Table 240.4(G) is a California-only table"
- This is a direct contradiction - needs verification
- Response acknowledges California may have amendments elsewhere but doesn't confirm table uniqueness

---

### 6. cec-002 (Score: 9/10)
**Question:** EV charging infrastructure requirements
**Accuracy:** 5/5 - Covers key requirements
**Completeness:** 4/5 - Minor omission
**Specific Errors:**
- MISSING: Specific mention of **40-amp minimum** circuit requirement
- Expected answer mentions "dedicated 40-amp minimum circuits"

---

### 7. cec-017 (Score: 9/10)
**Question:** Enclosure types for outdoor use with rain/sleet/ice
**Accuracy:** 5/5 - Lists suitable types
**Completeness:** 4/5 - Missing some types
**Specific Errors:**
- Lists: Type 3S, 3SX, 3X, 4, 4X, 6, 6P
- MISSING: **Type 3** and **Type 3R** which are also suitable per expected answer
- Expected answer includes: "Type 3, 3R, 3S, 4, 4X, 6, or 6P"

---

### 8. cec-029 (Score: 9/10)
**Question:** AFCI requirements comparison CEC vs NEC
**Accuracy:** 5/5 - Correct comparison
**Completeness:** 4/5 - Could be clearer
**Specific Errors:**
- Response provides detailed differences
- Expected answer notes requirements are "largely similar"
- Could more clearly emphasize the similarity rather than focusing on minor differences

---

### 9. cec-030 (Score: 9/10)
**Question:** Solar PV requirements comparison CEC vs NEC
**Accuracy:** 5/5 - Correct key distinction
**Completeness:** 4/5 - Could emphasize mandate more
**Specific Errors:**
- Correctly identifies California mandates PV installation
- Could more strongly emphasize "California requires solar installation; NEC only covers how to install it safely"

---

## Problem Areas Summary

1. **Table Value Lookup Errors (cec-020, cec-019):** Two questions had incorrect values retrieved from tables despite identifying the correct tables. This suggests the table lookup tools may be returning wrong data or the agent is misinterpreting results.

2. **Table Source Selection (cec-022):** Question of which table to use (310.12(A) for dwellings vs 310.16 general) affects conductor sizing. Both may be valid but lead to different answers.

3. **California-Specific vs NEC Content (cec-007):** Unclear whether certain tables are California-specific amendments or match NEC exactly. Better documentation needed.

4. **Minor Completeness Issues:** Several answers missing specific details (40-amp EV circuits, Type 3/3R enclosures, etc.)

---

## Recommendations

1. **Verify Table Lookup Tool Accuracy:** Check that cec_lookup_* tools are returning correct values for:
   - Table 400.5(A)(1) - flexible cord ampacities
   - Table 402.3 - fixture wire temperature ratings

2. **Clarify Table Selection Logic:** When multiple tables could apply (e.g., 310.12(A) vs 310.16), the agent should explain which applies and why.

3. **Improve California Amendment Identification:** Better distinguish which tables/sections are California-specific vs identical to NEC.
