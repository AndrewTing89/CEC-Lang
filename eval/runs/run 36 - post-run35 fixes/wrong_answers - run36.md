# Wrong/Partial Answers - Run 36

**Model:** Gemini 2.5 Pro (via CEC Agent)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 95.1% (504/530)

---

## Executive Summary
**Questions with Errors:** 7 of 53
**Perfect Scores:** 46

**Significant Improvement from Run 35:**
- Run 35: 90.9% (482/530) with 7 questions scoring 0-4
- Run 36: 95.1% (504/530) with 0 questions scoring below 7

---

## Detailed Error Analysis

### 1. cec2022-035 (Score: 7/10)
**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Agent Answer:** CEC Table 240.4(G) cross-references overcurrent protection requirements for specialized conductors, with California-specific amendments denoted by the delta (Δ) symbol. Key unique aspects include cross-references to California Energy Code (Title 24)... Section 422.3 mandates dedicated circuits... Section 440.51 includes an informational note directing users to 240.4(G)...

**Expected Answer:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**Accuracy:** 4/5 - Agent discusses California amendments but doesn't clearly state whether this table exists in NEC or is California-only.
**Completeness:** 3/5 - Missing the key point that this is a California-only table not found in NEC 2023.
**Specific Errors:**
- Did not explicitly state the table is California-only
- Did not confirm whether NEC 2023 has this table
- Over-complicated the answer with tangential cross-references

---

### 2. cec2022-038 (Score: 8/10)
**Question:** What medium voltage cable tables exist that are California-specific?

**Agent Answer:** Lists Tables 311.60(C)(67), (68), (69), (70), (75), (76) with descriptions... mentions 311.60(B) engineering supervision... references Section 392.80(B)...

**Expected Answer:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only. These provide ampacity information for medium voltage cables not found in the base NEC.

**Accuracy:** 4/5 - Correctly identifies several California-specific MV tables but incomplete.
**Completeness:** 4/5 - Missing the full range (through 86) and explicit count (18 tables).
**Specific Errors:**
- Only listed 6 specific tables instead of the full 18-20
- Did not provide the range (67 through 86)
- Did not state these are California-only

---

### 3. cec2022-006 (Score: 8/10)
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Agent Answer:** Discusses 110.26(B) dedicated space requirements... mentions 600mm (24 in.) to 900mm (30 in.)... references Section 646.18... states "CEC 2022 Section 110.26(B) requires dedicated and free from obstructions"

**Expected Answer:** 36 inches (3 feet)

**Accuracy:** 4/5 - Agent got confused between 110.26(A) working space DEPTH and 110.26(B) dedicated space above/below.
**Completeness:** 4/5 - Provided related information but didn't clearly state 36 inches.
**Specific Errors:**
- Confused 110.26(A) (working space depth) with 110.26(B) (dedicated space)
- Mentioned 24-30 inches instead of the correct 36 inches
- Search tool returned irrelevant Section 646.18 reference

---

### 4. cec2022-001 (Score: 9/10)
**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Agent Answer:** 12 AWG copper at 75°C termination has an ampacity of **25 amperes** per CEC Table 310.16. 240.4(D) restricts overcurrent protection to 20A maximum...

**Expected Answer:** 20 amperes

**Accuracy:** 5/5 - Both 25A (table ampacity) and 20A (practical OCP limit) are correct interpretations.
**Completeness:** 4/5 - Thorough but question wanted the simple answer.
**Specific Errors:**
- Not an error per se - agent gave the technically correct table value (25A) and noted the practical limit (20A)
- Expected answer wanted just 20A (the OCP-limited value)

---

### 5. cec2022-045 (Score: 9/10)
**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?

**Agent Answer:** Type 3, 3S, 3SX, 3X, 4, 4X, 6, 6P

**Expected Answer:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures

**Accuracy:** 5/5 - Listed correct enclosure types.
**Completeness:** 4/5 - Minor difference in types listed.
**Specific Errors:**
- Included 3SX and 3X (which are valid)
- Missed Type 3R (which is also valid for rain protection)

---

### 6. cec2022-050 (Score: 9/10)
**Question:** Size the conductors, EGC, and GEC for a 200A residential service using copper conductors.

**Agent Answer:** Service conductors: 2/0 AWG copper (Table 310.12(A)), EGC: 6 AWG copper (Table 250.122), GEC: 4 AWG copper (Table 250.66)

**Expected Answer:** Service conductors: 3/0 AWG copper minimum (200A at 75°C per CEC Table 310.16). EGC: 6 AWG copper. GEC: 4 AWG copper.

**Accuracy:** 4/5 - Used Table 310.12(A) (dwelling-specific) vs Table 310.16 (general).
**Completeness:** 5/5 - Complete answer with all three components.
**Specific Errors:**
- Used 2/0 AWG (Table 310.12(A) dwelling-specific) instead of 3/0 AWG (Table 310.16 general)
- Both are technically valid - 310.12(A) is more permissive for dwelling services
- EGC and GEC sizes are correct

---

### 7. cec2022-018 (Score: 10/10 - Borderline)
**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**Agent Answer:** 25A × 0.75 × 0.80 = 15A

**Expected Answer:** 30A × 0.82 × 0.80 = 19.68A (approximately 20A)

**Note:** This was scored 10/10 but has a discrepancy:
- Agent used 75°C column base ampacity (25A) with corresponding temp factor (0.75)
- Expected used 90°C column base ampacity (30A) with corresponding temp factor (0.82)
- Both approaches are valid - the result differs slightly (15A vs 19.68A)
- Agent's approach is more conservative

---

## Summary of Remaining Issues

| Issue | Score | Category | Priority |
|-------|-------|----------|----------|
| cec2022-035 | 7/10 | California-only table identification | LOW |
| cec2022-038 | 8/10 | MV table completeness | LOW |
| cec2022-006 | 8/10 | 110.26(A) vs 110.26(B) confusion | MEDIUM |
| cec2022-001 | 9/10 | Ambiguous expected answer | LOW |
| cec2022-045 | 9/10 | Minor enclosure type omission | LOW |
| cec2022-050 | 9/10 | Table selection (310.12(A) vs 310.16) | LOW |

---

## Comparison: Run 35 vs Run 36 Problem Questions

| Question | Run 35 Score | Run 36 Score | Status |
|----------|--------------|--------------|--------|
| cec2022-012 (Surge) | 2/10 | **10/10** | FIXED |
| cec2022-023 (AFCI) | 6/10 | **10/10** | FIXED |
| cec2022-044 (Working Space) | 3/10 | **10/10** | FIXED |
| cec2022-048 (SF-2) | 2/10 | **10/10** | FIXED |
| cec2022-051 (Office Load) | 2/10 | **10/10** | FIXED |
| cec2022-035 (240.4(G)) | 5/10 | 7/10 | Improved |
| cec2022-038 (MV Tables) | 7/10 | 8/10 | Improved |

---

## Recommendations for Future Improvement

1. **cec2022-035**: Add explicit `california_only: true` vs `california_modified: true` flags to table metadata
2. **cec2022-038**: Add a tool to list all tables matching a pattern (e.g., "311.60(C)(*)")
3. **cec2022-006**: Improve working space tool to clearly distinguish 110.26(A) depth from 110.26(B) dedicated space
4. **Expected Answers**: Consider accepting both table ampacity (25A) and OCP-limited (20A) for cec2022-001
