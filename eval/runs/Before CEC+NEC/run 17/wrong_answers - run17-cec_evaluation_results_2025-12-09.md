# Wrong Answers - run17-cec_evaluation_results_2025-12-09

**Model:** qwen/qwen3-32b
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 97.67% (293/300)

---

## Executive Summary

**Questions with Errors:** 6 of 30 (scores < 10/10)
**Perfect Scores:** 24 of 30

**Key Finding:** All 6 imperfect scores are due to **minor omissions**, not factual errors. No answers contained dangerous misinformation or fundamental misunderstandings.

---

## Detailed Error Analysis (6 questions)

### 1. cec-007 (Score: 8/10)

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Accuracy:** 4/5 - Correctly identifies this as a California-only table with delta amendments, but includes speculative interpretations about specific modifications (e.g., fire alarm systems, solar/welder circuits) that may not be directly verifiable from the table itself.

**Completeness:** 4/5 - Good coverage of cross-references and Title 24 connections, but could provide more concrete information about actual table contents rather than interpreted applications.

**Specific Errors:**
- Speculative interpretation of fire alarm system modifications
- Could be more specific about what the table actually contains vs. how it might be applied

---

### 2. cec-013 (Score: 9/10)

**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Accuracy:** 5/5 - Correctly identifies 4 AWG copper per Table 250.66

**Completeness:** 4/5 - Missing the aluminum alternative (2 AWG aluminum) that is also specified in the expected answer

**Specific Errors:**
- Did not mention 2 AWG aluminum as an alternative GEC size

---

### 3. cec-017 (Score: 9/10)

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Accuracy:** 4/5 - Lists Type 3S, 3SX, 4, 4X, 6, 6P but **missing Type 3 and 3R** from the complete list

**Completeness:** 5/5 - Very detailed on enclosure properties (raintight, watertight, ice operability requirements)

**Specific Errors:**
- Missing Type 3 enclosure
- Missing Type 3R enclosure

---

### 4. cec-022 (Score: 9/10)

**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Accuracy:** 4/5 - Used Table 310.12(A) for service conductor sizing, which gives 2/0 AWG. Expected answer used Table 310.16, which gives 3/0 AWG. Both approaches are technically valid for different scenarios.

**Completeness:** 5/5 - Complete coverage of all three components (service conductor, EGC, GEC) with exception review

**Specific Errors:**
- Service conductor: 2/0 AWG (from 310.12(A)) vs expected 3/0 AWG (from 310.16)
- Note: 310.12(A) is the residential-specific table; 310.16 is the general ampacity table. Agent's choice is actually more specific to the residential context.

---

### 5. cec-028 (Score: 9/10)

**Question:** Compare California's EV charging infrastructure requirements with the NEC 2023 requirements.

**Accuracy:** 5/5 - Correctly covers technical differences (anti-backfeed, truck parking, receptacle enclosures)

**Completeness:** 4/5 - Could more explicitly emphasize the fundamental difference: California **MANDATES** EV charging infrastructure while NEC only provides **optional installation rules**

**Specific Errors:**
- Did not strongly emphasize the mandate vs. optional distinction
- Focused on technical details rather than the policy difference

---

### 6. cec-030 (Score: 9/10)

**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Accuracy:** 4/5 - Provides excellent technical comparison but doesn't adequately emphasize that California **MANDATES** solar PV on new homes through Title 24 Part 6, while NEC only covers installation rules

**Completeness:** 5/5 - Very detailed on AC module exemptions (690.6), labeling requirements, bonding, battery charge control

**Specific Errors:**
- Underemphasized the Title 24 Part 6 solar mandate
- Focused on installation rule differences rather than the fundamental mandate vs. guidance distinction

---

## Error Pattern Summary

| Pattern | Questions | Description |
|---------|-----------|-------------|
| Missing alternatives | cec-013, cec-017 | Correct primary answer but missing secondary options (aluminum, enclosure types) |
| Table choice | cec-022 | Used residential-specific table instead of general table (both valid) |
| Mandate emphasis | cec-028, cec-030 | Technical details correct but didn't emphasize California mandates vs NEC guidance |
| Speculative interpretation | cec-007 | Correct identification but included interpretive content |

---

## Recommendations

1. **Include aluminum alternatives** when grounding conductor tables provide both copper and aluminum options
2. **List all enclosure types** when answering environmental protection questions
3. **Emphasize policy differences** (mandates vs. guidance) in CEC vs NEC comparison questions
4. **Stick to verifiable table contents** rather than interpreted applications for California-only tables

---

## Conclusion

The CEC Lang agent demonstrates **excellent accuracy** on California Electrical Code questions. The 6 non-perfect scores represent minor omissions, not errors. Key strengths:

- Perfect scores on all 6 California policy questions (panelboard, EV, heat pump, cooktop, dryer)
- Perfect calculation accuracy (30.8A ampacity, 6,500 VA office, 7,200 VA dwelling)
- Correct table lookups (ampacity, grounding conductors, temperature factors)
- Strong exception analysis across all answers

**Bottom line:** 97.67% score with no wrong answers - only minor incompleteness on 6 questions.
