# Wrong Answers - run20-cec_evaluation_results_2025-12-09

**Model:** qwen/qwen3-32b
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 95.0% (285/300)

---

## Executive Summary
**Questions with Errors:** 8 of 30
**Perfect Scores:** 22

**This run validates removing mandatory exception search:**
- +7 points improvement over run 19
- 37% faster execution (11.6s vs 18.6s avg)
- Key improvements on cec-007 (+4) and cec-008 (+5)

---

## Detailed Error Analysis (8 questions)

### 1. cec-013 (Score: 8/10)
**Question:** What size GEC is required for a 3/0 AWG copper service conductor?
**Accuracy:** 4/5 - Copper size correct
**Completeness:** 4/5 - Missing aluminum option
**Specific Errors:**
- Agent: "4 AWG copper"
- Expected: "4 AWG copper OR 2 AWG aluminum"
- Missing the aluminum alternative

---

### 2. cec-017 (Score: 9/10)
**Question:** Enclosure types for outdoor rain/sleet/ice
**Accuracy:** 5/5 - All listed types are correct
**Completeness:** 4/5 - Slightly different list
**Specific Errors:**
- Agent lists: 3, 3S, 3SX, 3X, 4, 4X, 6, 6P
- Expected lists: 3, 3R, 3S, 4, 4X, 6, 6P
- Missing 3R, includes 3SX and 3X instead
- All agent's types ARE valid for the conditions

---

### 3. cec-022 (Score: 8/10)
**Question:** 200A residential service sizing
**Accuracy:** 4/5 - Uses different table
**Completeness:** 4/5 - EGC and GEC correct
**Specific Errors:**
- Agent: 2/0 AWG copper (CEC Table 310.12(A) for dwelling services)
- Expected: 3/0 AWG copper (CEC Table 310.16 general)
- **Note:** Agent's answer may actually be MORE correct for dwelling-specific applications

---

### 4. cec-026 (Score: 7/10) - **Key remaining issue**
**Question:** Compare kitchen GFCI requirements CEC vs NEC
**Accuracy:** 3/5 - Restrictiveness direction disputed
**Completeness:** 4/5 - Good coverage of details
**Specific Errors:**
- **Expected:** CEC is MORE PERMISSIVE (limits GFCI to countertops + within 6ft of sink)
- **Agent:** Claims CEC is MORE RESTRICTIVE due to Title 24 CALGreen requiring GFCI for ALL 125V kitchen receptacles
- **Analysis:** Both perspectives have merit:
  - Base CEC 210.8: May be more permissive
  - CEC + CALGreen together: May be more restrictive
- This is a nuanced interpretation difference

---

### 5. cec-029 (Score: 9/10)
**Question:** Compare AFCI requirements CEC vs NEC
**Accuracy:** 5/5 - Correctly states similar requirements
**Completeness:** 4/5 - Minor detail missing
**Specific Errors:**
- Could explicitly list all room types: kitchens, family rooms, dining rooms, living rooms, bedrooms, sunrooms, closets, hallways, laundry areas
- Good coverage otherwise

---

### 6. cec-030 (Score: 9/10)
**Question:** Compare solar PV requirements
**Accuracy:** 4/5 - Different focus than expected
**Completeness:** 5/5 - Good technical detail
**Specific Errors:**
- Expected emphasizes: California MANDATES solar on new homes (Title 24 Part 6)
- Agent focuses on: Technical differences in Article 690 (AC module treatment)
- Both are correct but different emphasis

---

## Root Cause Analysis

### Why Run 20 Improved Over Run 19

**1. No forced exception search pollution**
- Run 19: Every question forced to call cec_exception_search, returning low-relevance results (0.24-0.50 similarity)
- Run 20: Agent only calls exception search when contextually relevant (1/30)
- Result: Cleaner answer synthesis without noise

**2. Better tool selection**
- cec_lookup_table now properly recognized in search_tools list
- Agent uses it 10/30 times vs 7/30 in run 19
- Table-specific questions (cec-007, cec-008) now answered correctly

**3. Faster execution**
- 37% reduction in response time
- No wasted time on irrelevant searches

### Remaining Issue: cec-026 Interpretation

The GFCI comparison question highlights a nuanced issue:
- **Expected answer** compares base CEC 210.8 vs NEC 210.8
- **Agent's answer** considers CEC + CALGreen as a whole

Both interpretations are valid. Consider:
1. Updating expected answer to acknowledge both perspectives
2. OR adding prompt guidance about comparing base code vs code+amendments

---

## Improvement Summary

| Question | Run 19 | Run 20 | Change | Reason |
|----------|--------|--------|--------|--------|
| cec-001 | 8/10 | 10/10 | +2 | Better content retrieval |
| cec-004 | 6/10 | 10/10 | +4 | OpenSearch working |
| cec-005 | 6/10 | 10/10 | +4 | OpenSearch working |
| cec-006 | 7/10 | 10/10 | +3 | OpenSearch working |
| cec-007 | 6/10 | 10/10 | +4 | **No forced exception search** |
| cec-008 | 5/10 | 10/10 | +5 | **No forced exception search** |
| cec-020 | 6/10 | 10/10 | +4 | Better table lookup |

**Total improvement: +7 points (278 → 285)**
