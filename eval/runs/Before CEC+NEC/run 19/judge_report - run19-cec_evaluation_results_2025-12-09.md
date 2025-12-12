# LLM-as-Judge Report: Run 19 CEC Evaluation

## Metadata

| Field | Value |
|-------|-------|
| **Date** | 2025-12-09 |
| **Model Evaluated** | qwen/qwen3-32b (CEC Agent with NEC Comparison) |
| **Prompt Version** | v2 - table routing, completeness, comparison reasoning |
| **Judge** | Claude Code (Opus 4.5) |
| **Questions** | 30 |
| **Scoring** | Accuracy (0-5) + Completeness (0-5) = Total (0-10) |

## Prompt Improvements Tested

1. **Table Content Routing:** Added `cec_lookup_table` to tool reference + explicit routing rules
2. **Completeness Check:** Added copper/aluminum and all-types checklist items
3. **Comparison Reasoning:** Added "which is more restrictive" structured reasoning

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| **Total Score** | 278/300 |
| **Percentage** | 92.7% |
| **Perfect Scores (10/10)** | 22 |
| **Imperfect Scores** | 8 |
| **Average Score** | 9.27/10 |

## Comparison with Run 18

| Metric | Run 18 | Run 19 | Change |
|--------|--------|--------|--------|
| Total Score | 275/300 | 278/300 | **+3** |
| Percentage | 91.7% | 92.7% | **+1.0%** |
| Perfect Scores | 22 | 22 | Same |
| cec_lookup_table used | 0 | 7 | **+7** |

---

## Score Distribution

| Score | Count | Questions |
|-------|-------|-----------|
| 10/10 | 22 | cec-001, cec-003, cec-004, cec-005, cec-006, cec-009, cec-010, cec-011, cec-012, cec-014, cec-015, cec-016, cec-018, cec-019, cec-020, cec-021, cec-023, cec-024, cec-025, cec-027, cec-029 |
| 9/10 | 2 | cec-022, cec-028 |
| 8/10 | 4 | cec-002, cec-013, cec-017, cec-030 |
| 6/10 | 1 | cec-007 |
| 5/10 | 1 | cec-008, cec-026 |

---

## All Evaluations

| ID | Category | Accuracy | Completeness | Total | Notes |
|----|----------|----------|--------------|-------|-------|
| cec-001 | panelboard_requirements | 5 | 5 | 10 | Perfect - lists all 4 appliances |
| cec-002 | ev_charging | 4 | 4 | 8 | Missing "40-amp minimum" specifically |
| cec-003 | solar_pv | 5 | 5 | 10 | Title 24 mandate, rapid shutdown covered |
| cec-004 | heat_pump | 5 | 5 | 10 | Correct 408.2 reference |
| cec-005 | electrification | 5 | 5 | 10 | Correct 408.2 for cooktop |
| cec-006 | electrification | 5 | 5 | 10 | Correct 408.2 for dryer |
| cec-007 | overcurrent | 3 | 3 | 6 | Used cec_lookup_table but focused on exceptions |
| cec-008 | surge_protection | 2 | 3 | 5 | Did not describe table content clearly |
| cec-009 | motor_control | 5 | 5 | 10 | Good table content description |
| cec-010 | medium_voltage | 5 | 5 | 10 | Correctly identifies 18 tables |
| cec-011 | conductor_ampacity | 5 | 5 | 10 | Correct: 230A |
| cec-012 | grounding | 5 | 5 | 10 | Includes copper AND aluminum |
| cec-013 | grounding | 4 | 4 | 8 | Missing aluminum option |
| cec-014 | ampacity_adjustment | 5 | 5 | 10 | Correct: 0.88 |
| cec-015 | ampacity_adjustment | 5 | 5 | 10 | Correct: 0.70 |
| cec-016 | working_space | 5 | 5 | 10 | Correct: 1.2m (4 ft) |
| cec-017 | enclosure | 4 | 4 | 8 | Missing Type 3 and Type 3R |
| cec-018 | lighting_load | 5 | 5 | 10 | Correct: 1.3 VA/sq ft |
| cec-019 | flexible_cord | 5 | 5 | 10 | Correct: 25A |
| cec-020 | fixture_wire | 5 | 5 | 10 | Correct: 200°C |
| cec-021 | adjusted_ampacity | 5 | 5 | 10 | Correct calculation shown |
| cec-022 | service_sizing | 4 | 5 | 9 | Used Table 310.12(A) vs expected 310.16 |
| cec-023 | commercial_load | 5 | 5 | 10 | Correct: 6,500 VA |
| cec-024 | motor_circuit | 5 | 5 | 10 | Correct: 10A |
| cec-025 | dwelling_load | 5 | 5 | 10 | Correct: 7,200 VA |
| cec-026 | gfci | 2 | 3 | 5 | Wrong: said "Equally Restrictive" vs expected "CEC MORE PERMISSIVE" |
| cec-027 | panelboard | 5 | 5 | 10 | Perfect comparison |
| cec-028 | ev_charging | 4 | 5 | 9 | Good but mandate distinction less prominent |
| cec-029 | afci | 5 | 5 | 10 | Good AFCI comparison |
| cec-030 | solar_pv | 4 | 4 | 8 | Technical differences good, mandate less clear |

---

## Prompt Fix Impact Analysis

### Fix 1: Table Content Routing
**Target Questions:** cec-007, cec-008

| Question | Run 18 Score | Run 19 Score | Tool Used | Improvement |
|----------|--------------|--------------|-----------|-------------|
| cec-007 | 6/10 | 6/10 | cec_lookup_table | Tool routing fixed, but answer still focused on exceptions |
| cec-008 | 4/10 | 5/10 | cec_lookup_table | **+1** - Tool used correctly |

**Finding:** The routing rule successfully caused the agent to use `cec_lookup_table`, but the answer content still doesn't describe what the tables specify. The agent interprets the question as "what exceptions apply" rather than "what does the table contain."

### Fix 2: Completeness Check (Copper/Aluminum)
**Target Questions:** cec-013

| Question | Run 18 Score | Run 19 Score | Aluminum Included | Improvement |
|----------|--------------|--------------|-------------------|-------------|
| cec-012 | 10/10 | 10/10 | Yes | Already correct |
| cec-013 | 8/10 | 8/10 | No | No change - still missing aluminum |

**Finding:** cec-012 now explicitly includes both copper (6 AWG) AND aluminum (4 AWG). However, cec-013 still only mentions 4 AWG copper without the 2 AWG aluminum option.

### Fix 3: Comparison Reasoning ("Restrictive vs Permissive")
**Target Question:** cec-026

| Question | Run 18 Conclusion | Run 19 Conclusion | Expected | Improvement |
|----------|-------------------|-------------------|----------|-------------|
| cec-026 | "CEC is MORE RESTRICTIVE" (WRONG) | "Equally Restrictive" | "CEC is MORE PERMISSIVE" | Partial - no longer inverted |

**Finding:** The agent no longer makes the opposite error (saying CEC is more restrictive). However, it now concludes "Equally Restrictive" which is still incorrect. The structured reasoning was applied but the agent failed to identify that NEC's broader scope (all kitchen receptacles) makes it more restrictive.

---

## Remaining Issues

### Critical Errors (Score ≤ 6)
1. **cec-007 (6/10):** Answer describes exceptions to Table 240.4(G), not the table content itself
2. **cec-008 (5/10):** Answer discusses overcurrent protection, not surge protection table content
3. **cec-026 (5/10):** Wrong conclusion on restrictiveness comparison

### Minor Omissions (Score 8-9)
1. **cec-002 (8/10):** Missing "40-amp minimum circuits"
2. **cec-013 (8/10):** Missing "2 AWG aluminum" option
3. **cec-017 (8/10):** Missing Type 3 and Type 3R enclosures
4. **cec-022 (9/10):** Different table reference (valid interpretation)
5. **cec-028 (9/10):** Key mandate distinction not prominent
6. **cec-030 (8/10):** Technical details good, mandate less clear

---

## Recommendations for Run 20

### High Priority

1. **Table Content Questions (cec-007, cec-008):**
   - Add explicit instruction: "For 'What does Table X specify?' questions, describe the TABLE CONTENT (columns, rows, values) first, THEN discuss exceptions"
   - Current prompt gets agent to use right tool but not produce right answer format

2. **Comparison Scope Analysis (cec-026):**
   - Strengthen the comparison reasoning prompt with example:
     ```
     Example: If Code A applies to "all kitchen receptacles" and Code B applies to
     "only countertop receptacles", Code A is MORE RESTRICTIVE (broader scope).
     ```

### Medium Priority

3. **Material Completeness:**
   - Add explicit instruction: "When table shows both copper AND aluminum columns, you MUST report both values, e.g., '4 AWG copper OR 2 AWG aluminum'"

---

## Conclusion

Run 19 shows modest improvement (+1.0%) over Run 18. The prompt fixes successfully:
- ✅ Caused `cec_lookup_table` to be used for table questions (7/30 questions)
- ✅ Fixed cec-012 to include both copper and aluminum
- ✅ Prevented inverted comparison conclusion in cec-026

However, the fixes did not fully resolve:
- ❌ cec-007, cec-008: Agent uses right tool but still focuses on exceptions
- ❌ cec-013: Still missing aluminum option
- ❌ cec-026: Now says "Equally Restrictive" instead of "CEC is MORE PERMISSIVE"

The core issues require more explicit content formatting instructions, not just tool routing.
