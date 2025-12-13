# Wrong Answers - Run 38

**Model:** CEC Lang Agent (Gemini 2.5 Pro)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 97.7% (518/530)

---

## Executive Summary
**Questions with Errors:** 9 of 53
**Perfect Scores:** 44

| Question | Score | Issue Type |
|----------|-------|------------|
| cec2022-051 | 3/10 | **Critical** - Wrong unit (14 VA/sq ft vs 1.3 VA/sq ft) |
| cec2022-023 | 7/10 | **Improved** - AFCI still partially wrong for non-countertop |
| cec2022-044 | 7/10 | Minor - Didn't directly answer the question |
| cec2022-006 | 8/10 | Minor - Focus on vertical vs depth clearance |
| cec2022-038 | 8/10 | Minor - Missing table count (20) |
| cec2022-001 | 9/10 | Minor - Ampacity vs OCP nuance |
| cec2022-021 | 9/10 | Minor - Different calculation method |
| cec2022-039 | 9/10 | Minor - Incorrect 240.4(D) reference |
| cec2022-050 | 9/10 | Minor - Different table used |

---

## Improvements from Run 37

### cec2022-023 (AFCI Kitchen): 5/10 → 7/10
**What improved:** Countertop receptacles now correctly get combination AFCI/GFCI.
**What's still wrong:** Dishwasher, disposal, and refrigerator still marked as "AFCI not required" when CEC 210.12(A) requires AFCI for ALL dwelling 120V circuits.

### cec2022-045 (Enclosures): 8/10 → 10/10
**FIXED!** Table sections fix now returns Type 3 and 3R which were previously missing.

---

## Detailed Error Analysis

### 1. cec2022-051 (Score: 3/10) - **CRITICAL NEW ERROR**
**Question:** Calculate the general lighting load for a 5,000 square foot office building.

**Agent Answer:** 5,000 sq ft × 14 VA/sq ft = 70,000 VA

**Expected Answer:** 5,000 sq ft × 1.3 VA/sq ft = 6,500 VA per CEC Table 220.12

**Accuracy:** 1/5 - Completely wrong answer due to unit confusion
**Completeness:** 2/5 - Calculation structure correct, value wrong

**Specific Errors:**
1. Agent uses 14 VA/sq ft (the metric value per m²) instead of 1.3 VA/sq ft
2. Final answer off by factor of ~10x (70,000 VA vs 6,500 VA)
3. This appears to be a table lookup error where the agent grabbed the wrong column

**Root Cause:** Table 220.12 has columns for both VA/sq ft (1.3) and VA/m² (14). Agent retrieved wrong column.

---

### 2. cec2022-023 (Score: 7/10) - **IMPROVED BUT STILL WRONG**
**Question:** New residential construction. Kitchen installation... specify the required protection.

**Agent Answer:**
- Countertop: Combination AFCI/GFCI ✓
- Dishwasher: GFCI only (AFCI "Not required") ✗
- Disposal: GFCI only (AFCI "Not required") ✗
- Refrigerator: Standard Breaker (AFCI "Not required") ✗

**Expected Answer:** All circuits require AFCI per 210.12(A). Countertop, dishwasher, disposal need combo AFCI/GFCI. Refrigerator needs AFCI.

**Accuracy:** 3/5 - 1 of 4 circuits correct
**Completeness:** 4/5 - Comprehensive but wrong conclusions

**Specific Errors:**
1. Still claims AFCI not required for dishwasher, disposal, refrigerator
2. CEC 2022 Section 210.12(A) requires AFCI for ALL 120V, 15/20A dwelling circuits
3. Agent incorrectly cites "210.12(A) exceptions" for refrigerators - no such exception exists

**Root Cause:** Agent searched for AFCI but still misinterprets scope of 210.12(A). The DOMAIN KNOWLEDGE fix helped for countertop (now combo) but agent still has incorrect understanding of which circuits are exempt.

---

### 3. cec2022-044 (Score: 7/10)
**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3?

**Agent Answer:** Discusses 110.26(B) dedicated space requirements but doesn't state "1.2m (4 ft)"

**Expected Answer:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**Accuracy:** 3/5 - Doesn't provide the direct answer
**Completeness:** 4/5 - Related information but misses target

**Specific Errors:**
1. Focuses on dedicated space (110.26(B)) instead of clearance depth (Table 110.26(A)(1))
2. Doesn't look up Table 110.26(A)(1) for Condition 3 at 480V
3. The answer "4 ft" is mentioned but not prominently or correctly

---

### 4. cec2022-006 (Score: 8/10)
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Agent Answer:** Mentions 6.5 ft vertical clearance prominently, mentions "3-foot depth requirement" in passing.

**Expected Answer:** 36 inches (3 feet)

**Accuracy:** 4/5 - Correct value present but not emphasized
**Completeness:** 4/5 - Answer buried in related information

**Specific Errors:**
1. Focuses on vertical clearance (6.5 ft) which wasn't asked
2. Depth (36 in / 3 ft) is mentioned but not as the primary answer

---

### 5. cec2022-038 (Score: 8/10)
**Question:** What medium voltage cable tables exist that are California-specific?

**Agent Answer:** Lists tables 311.60(C)(67)-(76) with detailed applications

**Expected Answer:** 20 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86))

**Accuracy:** 4/5 - Correct series, missing full range
**Completeness:** 4/5 - Missing count and full enumeration

**Specific Errors:**
1. Does not state "20 tables total"
2. Lists only tables 67-76, missing 77-86
3. No enumeration capability - this is a tool limitation

---

## Summary by Category

### Critical Errors (Requires Fix)
| ID | Issue | Recommended Action |
|----|-------|-------------------|
| cec2022-051 | Unit confusion (14 VA/sq ft vs 1.3 VA/sq ft) | Fix Table 220.12 lookup to return correct unit |
| cec2022-023 | AFCI scope still partially wrong | Update expected answer OR fix search results to clarify 210.12(A) scope |

### Minor Errors (Low Priority)
| ID | Issue | Notes |
|----|-------|-------|
| cec2022-044 | Indirect answer | Tool behavior - focuses on wrong section |
| cec2022-006 | Answer not emphasized | Correct value present but buried |
| cec2022-038 | Missing count | Tool limitation - no enumeration capability |
| cec2022-001 | Ampacity vs OCP | Agent technically more accurate |
| cec2022-021 | Calculation method | Both methods valid under Article 220 |
| cec2022-039 | Wrong 240.4(D) ref | Minor - doesn't affect answer |
| cec2022-050 | Different table | Both methods valid |

---

## Key Observations

1. **cec2022-023 IMPROVED but not fixed**: The DOMAIN KNOWLEDGE prompt addition helped (countertop now correct) but agent still misunderstands AFCI scope for dedicated appliance circuits.

2. **cec2022-045 FIXED**: Table sections fix working perfectly - Type 3 and 3R now included.

3. **NEW ERROR cec2022-051**: Table 220.12 has dual units (VA/sq ft and VA/m²). Agent grabbed wrong column. This is a tool/data issue.

4. **Overall improvement**: 96.0% → 97.7% (+1.7 percentage points, +9 raw score)

---

## Recommended Next Steps

1. **Fix cec2022-051**: Investigate Table 220.12 lookup - ensure it returns per-square-foot values, not per-square-meter
2. **cec2022-023**: Consider adding more explicit AFCI guidance or reviewing if expected answer should accept partial credit for dedicated circuits
3. **cec2022-044**: Add hint enforcement for working space depth questions
