# Wrong Answers - run19-cec_evaluation_results_2025-12-09

**Model:** qwen/qwen3-32b (CEC Agent with NEC Comparison)
**Prompt Version:** v2 - table routing, completeness, comparison reasoning
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 92.7% (278/300)

---

## Executive Summary
**Questions with Errors:** 8 of 30
**Perfect Scores:** 22

### Comparison with Run 18
| Metric | Run 18 | Run 19 | Change |
|--------|--------|--------|--------|
| Score | 91.7% | 92.7% | +1.0% |
| Perfect | 22 | 22 | Same |

---

## Critical Errors (3 questions)

### 1. cec-026 (Score: 5/10)
**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Accuracy:** 2/5 - WRONG CONCLUSION
**Completeness:** 3/5 - Good comparison details, wrong conclusion

**Expected Answer:**
> CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles.

**Agent's Conclusion:**
> "Equally Restrictive: Both CEC 2022 and NEC 2023 have identical requirements for kitchen countertop GFCI protection."

**Analysis:**
- **Improvement from Run 18:** No longer says "CEC is MORE RESTRICTIVE" (the opposite error)
- **Still Wrong:** Says "Equally Restrictive" when CEC is actually MORE PERMISSIVE
- The agent correctly identified that CEC references "countertop surfaces" and "sink proximity (1.8m/6ft)"
- Failed to recognize that NEC's "all kitchen receptacles" is a BROADER scope = MORE RESTRICTIVE

**Root Cause:** The structured comparison reasoning helped avoid the inverted error but didn't provide enough guidance to determine that "all X" > "only countertop X" in terms of restrictiveness.

---

### 2. cec-007 (Score: 6/10)
**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Accuracy:** 3/5 - Didn't describe table content
**Completeness:** 3/5 - Covered exceptions, missed table purpose

**Expected Answer:**
> CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**Agent's Focus:**
- Motor circuit overcurrent protection exceptions (230.90(A))
- Service conductor overload protection
- Fire pump conductor requirements
- DID NOT describe what Table 240.4(G) contains

**Improvement from Run 18:**
- ✅ Now uses `cec_lookup_table` (was using `cec_search`)
- ❌ Still focuses on exceptions instead of table content

**Root Cause:** The tool routing fix worked but the agent interprets "What does Table X specify?" as "What exceptions affect Table X?" rather than "Describe the table's content."

---

### 3. cec-008 (Score: 5/10)
**Question:** What does CEC Table 242.3 specify for California installations?

**Accuracy:** 2/5 - Did not describe Table 242.3
**Completeness:** 3/5 - Related content but not the table itself

**Expected Answer:**
> CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**Agent's Focus:**
- Cablebus overcurrent protection exceptions
- Cross-references to 240.100/240.101
- Never described what Table 242.3 contains for surge protection

**Improvement from Run 18:**
- ✅ Now uses `cec_lookup_table` (+1 point vs run 18)
- ❌ Still doesn't describe actual surge protection requirements in table

**Root Cause:** Same as cec-007 - agent finds related content but doesn't describe the table's primary purpose (surge protection requirements).

---

## Minor Omissions (5 questions)

### 4. cec-002 (Score: 8/10)
**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Accuracy:** 4/5 - Correct concepts, missing specifics
**Completeness:** 4/5 - Good coverage

**Missing Details:**
- "40-amp minimum circuits" - not specifically stated
- "Conduit to parking spaces" - mentioned but buried in CALGreen reference

---

### 5. cec-013 (Score: 8/10)
**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Accuracy:** 4/5 - Correct for copper, missing aluminum
**Completeness:** 4/5 - Incomplete

**Expected Answer:**
> 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66

**Agent Response:**
> "Required GEC Size: 4 AWG copper"

**Missing:**
- 2 AWG aluminum option from Table 250.66
- Completeness check prompt didn't trigger aluminum inclusion here

---

### 6. cec-017 (Score: 8/10)
**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Accuracy:** 4/5 - Most types listed
**Completeness:** 4/5 - Missing some types

**Expected Answer:**
> Type 3, 3R, 3S, 4, 4X, 6, or 6P

**Agent Response:**
> Types 3S, 3SX, 4, 4X, 6, 6P

**Differences:**
- ❌ Missing: Type 3, Type 3R
- ✅ Added specialized variants (3SX)

---

### 7. cec-022 (Score: 9/10)
**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Accuracy:** 4/5 - Different table reference
**Completeness:** 5/5 - All components sized

**Expected vs Agent:**
| Component | Expected | Agent |
|-----------|----------|-------|
| Service conductor | 3/0 AWG (Table 310.16) | 2/0 AWG (Table 310.12(A)) |
| EGC | 6 AWG | 6 AWG ✅ |
| GEC | 4 AWG | 4 AWG ✅ |

**Analysis:** Both answers are technically valid. Table 310.16 is ampacity-based, Table 310.12(A) is for dwelling service entrance minimums.

---

### 8. cec-030 (Score: 8/10)
**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Accuracy:** 4/5 - Technical details correct
**Completeness:** 4/5 - Mandate distinction not prominent

**Expected Key Point:**
> California MANDATES solar PV on new single-family homes through Title 24 Part 6. The key difference is California requires solar installation; NEC only covers how to install it safely.

**Agent Response:**
- Covers rapid shutdown, wiring methods, grounding
- Title 24 mandate mentioned but not as the PRIMARY distinction
- Technical comparison thorough but fundamental "mandate vs rules" less clear

---

## Error Pattern Summary

| Pattern | Questions | Run 18 | Run 19 | Status |
|---------|-----------|--------|--------|--------|
| Wrong Comparison Conclusion | cec-026 | 4/10 | 5/10 | +1 (no longer inverted) |
| Table Content Miss | cec-007, cec-008 | 10/20 | 11/20 | +1 (uses right tool) |
| Missing Aluminum | cec-013 | 8/10 | 8/10 | No change |
| Missing Enclosure Types | cec-017 | 8/10 | 8/10 | No change |
| Key Distinction Emphasis | cec-028, cec-030 | 17/20 | 17/20 | No change |

---

## Score Breakdown

| Score | Count | Percentage |
|-------|-------|------------|
| 10/10 | 22 | 73.3% |
| 9/10 | 2 | 6.7% |
| 8/10 | 4 | 13.3% |
| 6/10 | 1 | 3.3% |
| 5/10 | 1 | 3.3% |
