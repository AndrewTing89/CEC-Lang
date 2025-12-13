# Wrong Answers - run44

**Model:** qwen/qwen3-32b (via Groq)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 94.2% (499/530)

---

## Executive Summary
**Questions with Errors:** 14 of 53
**Perfect Scores:** 39

**Error Categories:**
- Calculation errors (wrong factors): 1
- AFCI exception misinterpretation: 1
- Working space depth confusion: 1
- Table lookup failures: 2
- Minor differences in code interpretation: 9

---

## Detailed Error Analysis

### 1. cec2022-048 (Score: 5/10)
**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire?

**Agent Answer:** After verifying with CEC 2022 Table 402.3 via cec_search, Type SF-2 silicone insulated fixture wire is not explicitly listed in the referenced table data. The closest matching entries are: Type KF-2: 200°C (392°F), Type PF: 200°C (392°F)...

**Expected Answer:** 200°C (392°F) per CEC 2022 Table 402.3

**Accuracy:** 2/5 - Agent failed to find SF-2 in the table when it is actually present
**Completeness:** 3/5 - Provided alternatives but not the correct answer
**Specific Errors:**
- Failed to locate SF-2 in Table 402.3
- Expressed uncertainty when the answer is definitively 200°C
- Tool/search limitation caused incorrect response

---

### 2. cec2022-027 (Score: 6/10)
**Question:** A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity.

**Agent Answer:** Base: 20A (Table 310.16). Temperature correction: 0.82. Bundling: 0.80. Adjusted: 20A × 0.82 × 0.80 = 13.12A

**Expected Answer:** Base: 20A. Temperature correction: 0.71 (for 41-45°C in 60°C column). Bundling: 0.80. Adjusted: 20A × 0.71 × 0.80 = 11.36A

**Accuracy:** 2/5 - Used wrong temperature correction factor (0.82 vs 0.71)
**Completeness:** 4/5 - Showed methodology correctly but used wrong value
**Specific Errors:**
- Used 0.82 correction factor which is for 75°C conductors at 50°C
- Should have used 0.71 from the 60°C column for 41-45°C ambient range
- Final answer of 13.12A is ~15% higher than correct 11.36A
- This error could result in undersized conductors in high-temperature environments

---

### 3. cec2022-038 (Score: 6/10)
**Question:** What medium voltage cable tables exist that are California-specific?

**Agent Answer:** Lists tables in 315.10(A), 315.60(C) series. Notes they're derived from NEC Article 315 without amendments.

**Expected Answer:** CEC has 20 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only.

**Accuracy:** 3/5 - Referenced wrong article number (315 vs 311) and wrong series
**Completeness:** 3/5 - Failed to identify the specific California-only tables
**Specific Errors:**
- Cited Article 315 instead of Article 311
- Did not identify the 311.60(C)(67) through 311.60(C)(86) series as California-specific
- Incorrectly stated tables are adopted without amendments when they are California-only

---

### 4. cec2022-013 (Score: 7/10)
**Question:** A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet code requirements?

**Agent Answer:** Violation of 240.24(D) for clothes closet. Violation of 110.26(A)(1) - states "30 inches minimum required." Water heater at 18" to side is "acceptable if doesn't block access."

**Expected Answer:** No, violates: (1) 36 inches depth required per 110.26(A)(1). (2) Panels prohibited in clothes closets per 240.24(D). (3) 30 inches width required. (4) No storage/equipment in working space per 110.26(B).

**Accuracy:** 3/5 - Confused width (30") with depth (36")
**Completeness:** 4/5 - Missed 110.26(B) storage prohibition argument
**Specific Errors:**
- Stated 30 inches minimum depth when correct requirement is 36 inches (Table 110.26(A)(1) shows 3 ft for 0-150V Condition 1)
- Incorrectly assessed water heater as compliant when it may violate working space requirements
- Did not cite 110.26(B) regarding prohibition of equipment in dedicated equipment space

---

### 5. cec2022-023 (Score: 7/10)
**Question:** New residential construction kitchen: countertop receptacles, dishwasher, garbage disposal, refrigerator. Specify required protection for each.

**Agent Answer:** Countertops: AFCI/GFCI combo. Dishwasher: GFCI only (AFCI exempt under Exception 1). Disposal: GFCI only (AFCI exempt). Refrigerator: Standard breaker (both exempt).

**Expected Answer:** Countertops: AFCI/GFCI combo. Dishwasher: AFCI/GFCI combo per 422.5 and 210.12(A). Disposal: AFCI/GFCI combo. Refrigerator: AFCI required per 210.12(A). All 120V dwelling circuits require AFCI.

**Accuracy:** 3/5 - Incorrectly exempted dishwasher, disposal, and refrigerator from AFCI
**Completeness:** 4/5 - Provided reasoning but based on misinterpretation
**Specific Errors:**
- Overly broad interpretation of 210.12(A) Exception 1 for dedicated appliance circuits
- Exception 1 has specific conditions that don't automatically apply to all dedicated appliance circuits in kitchens
- Refrigerator still requires AFCI protection per 210.12(A) as a 120V dwelling unit circuit
- This error could result in non-compliant installations

---

### 6. cec2022-032 (Score: 7/10)
**Question:** What circuit requirements exist for heat pump water heaters in new dwelling units?

**Agent Answer:** Discusses 422.13 (125% OCP/conductor sizing), 422.47 (temperature limits), 422.11(A). Mentions CALGreen but doesn't cite 408.2 as main California requirement.

**Expected Answer:** Per CEC 408.2, panelboards must have a reserved space for heat pump water heater branch circuit as part of California's decarbonization requirements.

**Accuracy:** 3/5 - Focused on general water heater requirements instead of California-specific 408.2
**Completeness:** 4/5 - Good general information but missed key requirement
**Specific Errors:**
- Did not emphasize CEC 408.2 as the primary California-specific requirement
- Focused on Article 422 general requirements instead of the reserved panelboard space mandate
- This is a California-unique electrification readiness requirement that was not highlighted

---

### 7. cec2022-035 (Score: 8/10)
**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Agent Answer:** Table includes California amendments (δ) that modify NEC. Cross-references specialized conductor types to their articles for overcurrent protection rules.

**Expected Answer:** CEC Table 240.4(G) provides overcurrent protection requirements for small conductors. Table exists in both CEC and NEC but California has modified values.

**Accuracy:** 4/5 - Correctly identified amendment concept but vague on specifics
**Completeness:** 4/5 - General explanation without specific modified values
**Specific Errors:**
- Did not specify what values are modified
- Did not mention small conductor overcurrent protection specifically

---

### 8. cec2022-001 (Score: 9/10)
**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Agent Answer:** Ampacity: 25 amperes at 75°C (Table 310.16). Overcurrent Protection Limit: 20A maximum (Section 240.4(D))...

**Expected Answer:** 20 amperes

**Accuracy:** 4/5 - Stated 25A ampacity but expected answer emphasizes 20A practical limit
**Completeness:** 5/5 - Excellent context provided
**Specific Errors:**
- Question wording is ambiguous - raw ampacity is 25A but practical limit is 20A
- Expected answer focuses on 20A; agent provided both values

---

### 9. cec2022-003 (Score: 9/10)
**Question:** Where is GFCI protection required in a residential kitchen?

**Agent Answer:** All 125V-250V receptacles serving countertop surfaces per 210.8(A)(6).

**Expected Answer:** Countertop surfaces per 210.8(A)(6). Dishwashers NOT explicitly required under 210.8(A)(6).

**Accuracy:** 5/5 - Correct on main requirement
**Completeness:** 4/5 - Did not mention dishwasher exemption clarification
**Specific Errors:**
- Did not explicitly clarify that dishwashers are NOT required to have GFCI under 210.8(A)(6)

---

### 10. cec2022-014 (Score: 9/10)
**Question:** Two 12 AWG conductors on single breaker terminal not marked for two - violation?

**Agent Answer:** Yes, violation per 408.41.

**Expected Answer:** Yes, violation per 110.14(A).

**Accuracy:** 5/5 - Correct conclusion
**Completeness:** 4/5 - Different code section cited
**Specific Errors:**
- Cited 408.41 instead of 110.14(A) - both are applicable but 110.14(A) is more directly relevant

---

### 11. cec2022-021 (Score: 9/10)
**Question:** Panel load calculation - is 200A adequate?

**Agent Answer:** 24,050 VA ÷ 240V = 100.2A. 200A adequate.

**Expected Answer:** 24,775 VA ÷ 240V = 103.2A. 200A adequate.

**Accuracy:** 4/5 - Slight difference in total VA (24,050 vs 24,775)
**Completeness:** 5/5 - Full calculation shown
**Specific Errors:**
- Minor calculation difference of ~725 VA, likely due to demand factor application
- Correct conclusion reached

---

### 12. cec2022-025 (Score: 9/10)
**Question:** Max 10 AWG THHN conductors in 1¼" RMC?

**Agent Answer:** 28 conductors (rounds down from 28.91)

**Expected Answer:** 28-29 conductors. Per Note 7, can round up to 29 when decimal ≥0.8.

**Accuracy:** 4/5 - Used conservative rounding
**Completeness:** 5/5 - Full calculation shown
**Specific Errors:**
- Rounded down to 28 instead of applying Note 7 which allows 29

---

### 13. cec2022-033 (Score: 9/10)
**Question:** Electric cooktop readiness in new homes?

**Agent Answer:** Per 422.3(A)(2) and California Energy Code 150.0(u), dedicated circuits required.

**Expected Answer:** CEC 408.2 requires reserved panelboard space.

**Accuracy:** 4/5 - Correct concept but different code path
**Completeness:** 5/5 - Practical requirements covered
**Specific Errors:**
- Cited 422.3(A)(2) instead of 408.2 - both valid but 408.2 is the primary reference

---

### 14. cec2022-050 (Score: 9/10)
**Question:** Size conductors, EGC, GEC for 200A residential service?

**Agent Answer:** Service: 2/0 AWG (Table 310.12(A)). EGC: 6 AWG. GEC: 4 AWG.

**Expected Answer:** Service: 3/0 AWG (Table 310.16). EGC: 6 AWG. GEC: 4 AWG.

**Accuracy:** 4/5 - Table 310.12(A) allows 2/0 for dwelling services; 310.16 requires 3/0
**Completeness:** 5/5 - All three conductors sized
**Specific Errors:**
- Different table reference - 310.12(A) vs 310.16
- Both are valid approaches; 310.12(A) has special dwelling service allowances

---

## Pattern Analysis

### Most Common Error Types:
1. **Temperature/derating factor selection** (cec2022-027) - Critical calculation error
2. **AFCI exception interpretation** (cec2022-023) - Code interpretation error
3. **Working space requirements** (cec2022-013) - Confused width vs depth
4. **California-specific code citations** (cec2022-032, cec2022-038) - Missed unique CEC provisions
5. **Table lookup limitations** (cec2022-048) - Search/tool failure

### Recommendations for Improvement:
1. Strengthen temperature correction factor lookup for 60°C conductors
2. Review AFCI exception conditions more carefully
3. Distinguish between working space width (30") and depth (36")
4. Better indexing of California-specific amendments and tables
5. Ensure fixture wire types are fully indexed in table tools
