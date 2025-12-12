# Wrong Answers - run18-cec_evaluation_results_2025-12-09

**Model:** qwen/qwen3-32b (CEC Agent with NEC Comparison)
**Judge:** Claude Code (Opus 4.5)
**Overall Score:** 91.7% (275/300)

---

## Executive Summary
**Questions with Errors:** 8 of 30
**Perfect Scores:** 22

The model performed well overall with 22 perfect scores. The 8 imperfect responses fall into three categories:
1. **Critical Error (1):** Completely wrong conclusion on GFCI comparison
2. **Missed Target (2):** Didn't answer what the question asked about specific tables
3. **Minor Omissions (5):** Correct answers with small missing details

---

## Critical Error (1 question)

### 1. cec-026 (Score: 4/10)
**Question:** Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?

**Accuracy:** 1/5 - **WRONG CONCLUSION**
**Completeness:** 3/5 - Provides comparison details but arrives at wrong answer

**Expected Answer:**
> CEC 2022 is MORE PERMISSIVE than NEC 2023 for kitchen GFCI. CEC limits GFCI requirements to receptacles serving countertop surfaces and within 6 feet of the sink. NEC 2023 requires GFCI protection for ALL kitchen receptacles, including those for refrigerators and built-in microwaves.

**Agent's Conclusion:**
> CEC 2022 is more restrictive than NEC 2023 for kitchen GFCI requirements

**Specific Errors:**
- Got the comparison completely backwards
- Stated "No exceptions for common kitchen appliances on dedicated circuits" when CEC actually IS more permissive by limiting GFCI to countertop/sink-adjacent receptacles
- Misinterpreted the 6 ft spacing rule context
- This is a significant factual error that could mislead users about code requirements

**Root Cause:** The agent appears to have confused CEC's GFCI exceptions (which make it less restrictive) with additional requirements (which would make it more restrictive).

---

## Missed Target (2 questions)

### 2. cec-008 (Score: 4/10)
**Question:** What does CEC Table 242.3 specify for California installations?

**Accuracy:** 2/5 - Did not describe Table 242.3
**Completeness:** 2/5 - Missing the main point

**Expected Answer:**
> CEC Table 242.3 is a California-only table related to surge protection requirements. This table does not exist in the base NEC 2023.

**Agent's Response Focus:**
- Wind turbine surge protection (CEC 694.7(D))
- Dwelling unit SPD mandate (CEC 230.67)
- Did NOT describe Table 242.3 itself

**Specific Errors:**
- Never directly addressed what Table 242.3 contains
- Never stated it's a California-only table
- Discussed related surge protection requirements instead of the specific table
- Response appears to be about tangentially related content

**Root Cause:** The search tools may not have returned Table 242.3 directly, causing the agent to answer about related surge protection topics instead.

---

### 3. cec-007 (Score: 6/10)
**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Accuracy:** 3/5 - Discussed exceptions but not the table content
**Completeness:** 3/5 - Missing key information

**Expected Answer:**
> CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**Agent's Response Focus:**
- Exceptions to Table 240.4(G) (motor-starting currents, busway protection)
- How exceptions modify the table's application
- Did NOT describe the table itself

**Specific Errors:**
- Never clearly stated what Table 240.4(G) contains (overcurrent protection requirements)
- Never explicitly stated it's a California-only table not in NEC
- Focused on exceptions rather than base table content
- Title says "Exceptions and Limitations" rather than "What the table specifies"

**Root Cause:** The agent interpreted the question as asking about exceptions to the table rather than the table's content and California-unique nature.

---

## Minor Omissions (5 questions)

### 4. cec-002 (Score: 8/10)
**Question:** What are California's electrical requirements for EV charging infrastructure in new residential construction?

**Accuracy:** 4/5 - Correct concepts but missing specifics
**Completeness:** 4/5 - Covers main points

**Expected Answer Highlights:**
- Dedicated 40-amp minimum circuits
- Conduit to parking spaces
- Panel capacity for EV loads
- CEC Article 625 and Title 24 CALGreen

**Missing from Agent Response:**
- "40-amp minimum circuits" - not specifically mentioned
- "Conduit to parking spaces" - not mentioned
- Response covers CALGreen, GFCI, ventilation, cord lengths but misses these infrastructure specifics

---

### 5. cec-013 (Score: 8/10)
**Question:** What size grounding electrode conductor is required for a 3/0 AWG copper service conductor in California?

**Accuracy:** 4/5 - Correct for copper, missing aluminum
**Completeness:** 4/5 - Incomplete answer

**Expected Answer:**
> 4 AWG copper or 2 AWG aluminum GEC per CEC 2022 Table 250.66

**Agent Response:**
> 4 AWG copper (correct) - aluminum option not mentioned

**Missing:**
- 2 AWG aluminum option from Table 250.66

---

### 6. cec-017 (Score: 8/10)
**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice according to California code Table 110.28?

**Accuracy:** 4/5 - Mostly correct but different enclosure list
**Completeness:** 4/5 - Good coverage

**Expected Answer:**
> Type 3, 3R, 3S, 4, 4X, 6, or 6P

**Agent Response:**
> Type 3S, 3SX, 3X, 4, 4X, 6, 6P

**Differences:**
- Missing: Type 3, Type 3R
- Added: Type 3SX, Type 3X
- The basic Type 3 and 3R (raintight) were omitted while more specialized variants were included

---

### 7. cec-022 (Score: 9/10)
**Question:** Size the conductors, EGC, and GEC for a 200A residential service in California using copper conductors.

**Accuracy:** 4/5 - Different table reference for service conductor
**Completeness:** 5/5 - All components sized

**Expected Answer:**
> Service conductors: 3/0 AWG copper (per CEC Table 310.16)

**Agent Response:**
> Service conductor: 2/0 AWG copper (per Table 310.12(A))

**Analysis:**
- Both answers are technically valid depending on which table is used
- Table 310.16 (ampacity table) shows 200A requires 3/0 AWG at 75°C
- Table 310.12(A) (service entrance conductor minimum sizes) shows 2/0 for 200A service
- Expected answer uses ampacity table, agent uses service entrance minimums
- EGC (6 AWG) and GEC (4 AWG) were correct

---

### 8. cec-030 (Score: 8/10)
**Question:** Compare California's solar PV requirements with NEC 2023 Article 690.

**Accuracy:** 4/5 - Correct but mandate less prominent
**Completeness:** 4/5 - Technical details good, key distinction less clear

**Expected Answer Key Point:**
> California MANDATES solar PV on new single-family homes through Title 24 Part 6. CEC 690 follows NEC 690 for installation requirements. The key difference is California requires solar installation; NEC only covers how to install it safely.

**Agent Response:**
- Covers AC module exceptions, PV-powered signs, energy storage, system connections
- Title 24 mandate mentioned but not as the primary distinction
- Technical differences well covered but the fundamental "mandate vs rules" distinction is less clear

---

## Pattern Analysis

### Error Categories
| Category | Count | Questions |
|----------|-------|-----------|
| Wrong Conclusion | 1 | cec-026 |
| Missed Table Content | 2 | cec-007, cec-008 |
| Missing Specific Values | 2 | cec-002, cec-013 |
| Different Valid Interpretation | 2 | cec-017, cec-022 |
| Emphasis Issue | 1 | cec-030 |

### Recommendations
1. **GFCI Comparison (Critical):** Review the tool's understanding of CEC vs NEC GFCI scope - CEC is MORE permissive, not more restrictive
2. **Table Lookups:** When asked "what does Table X specify", ensure the response describes the table's content, not just related exceptions
3. **Aluminum Options:** Include aluminum conductor sizes when relevant (they're in the same tables)
4. **Key Distinctions:** For comparison questions, lead with the fundamental difference before diving into technical details

---

## Score Breakdown

| Score | Count | Percentage |
|-------|-------|------------|
| 10/10 | 22 | 73.3% |
| 9/10 | 1 | 3.3% |
| 8/10 | 4 | 13.3% |
| 6/10 | 1 | 3.3% |
| 4/10 | 2 | 6.7% |
