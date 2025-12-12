# Wrong/Partial Answers Analysis - Run 35

**Date:** 2025-12-11
**Total Wrong/Partial:** 10 questions

---

## 1. cec2022-012 - Surge Protection Requirement (2/10)

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected Answer:** Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**Agent Answer:** The California Electrical Code (CEC) 2022 **does not explicitly require surge protection** (surge protective devices or SPDs) for residential services.

**Analysis:** This is a critical error. CEC 2022 Section 230.67 explicitly requires SPDs for all dwelling unit services. This is particularly concerning because cec2022-008 (essentially the same question) was answered correctly. This inconsistency suggests a search result quality issue.

**Root Cause:** Search tool returned grounding-related results instead of Article 230.67.

**Fix Needed:** Improve search relevance for surge protection queries; ensure 230.67 is properly indexed.

---

## 2. cec2022-023 - Kitchen Circuit Protection (6/10)

**Question:** New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection.

**Expected Answer:**
- Countertop: AFCI/GFCI combination
- Dishwasher: AFCI/GFCI combination (per 422.5 and 210.12(A))
- Disposal: AFCI/GFCI combination
- Refrigerator: AFCI required per 210.12(A)

**Agent Answer:**
- Countertop: AFCI/GFCI (Correct)
- Dishwasher: GFCI only (Wrong - exempted AFCI)
- Disposal: GFCI only (Wrong - exempted AFCI)
- Refrigerator: Standard breaker (Wrong - AFCI required)

**Analysis:** Agent incorrectly claimed AFCI exemptions for motor circuits and refrigeration equipment. CEC 2022 Section 210.12(A) requires AFCI for ALL 120V dwelling unit circuits. The motor exemption applies to specific industrial applications, not residential appliances.

**Root Cause:** Misinterpretation of 210.12(A) exceptions.

**Fix Needed:** Update system prompt to clarify 210.12(A) scope for dwelling units.

---

## 3. cec2022-035 - Table 240.4(G) California Amendment (5/10)

**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected Answer:** CEC Table 240.4(G) is a California-only table that provides additional overcurrent protection requirements. This table does not exist in the base NEC 2023.

**Agent Answer:** CEC Table 240.4(G) does **not contain California-specific modifications** in its core content.

**Analysis:** The agent incorrectly stated the table has no California-specific content. The expected answer indicates this is a California-only table (marked with "N" for new California content).

**Root Cause:** Table lookup tool may not be flagging California-only tables properly.

**Fix Needed:** Enhance table metadata to clearly indicate California-specific vs NEC tables.

---

## 4. cec2022-038 - Medium Voltage Tables (7/10)

**Question:** What medium voltage cable tables exist that are California-specific?

**Expected Answer:** CEC has 18 medium voltage tables in the 311.60(C) series (Tables 311.60(C)(67) through 311.60(C)(86)) that are California-only.

**Agent Answer:** Mentioned Tables 311.60(C)(69), 311.60(C)(70), 311.60(C)(75), 311.60(C)(76) and some Article 392 tables, but did not provide the complete count of 18 California-specific tables.

**Analysis:** Partial answer - identified some tables but missed the full scope (18 tables from 311.60(C)(67) through (86)).

**Root Cause:** Search only returned partial results; table metadata incomplete for medium voltage tables.

**Fix Needed:** Index all 311.60(C) series tables with California-specific flags.

---

## 5. cec2022-044 - Working Space 480V Condition 3 (3/10)

**Question:** What is the minimum working space depth for a 480V panelboard under Condition 3?

**Expected Answer:** 1.2 m (4 ft) per CEC 2022 Table 110.26(A)(1)

**Agent Answer:** Provided information about 110.26(B) dedicated space and combustible materials, but did NOT answer the actual question about working space depth.

**Analysis:** Complete miss - the agent searched for 110.26(B) instead of looking up Table 110.26(A)(1) for the 480V/Condition 3 value. The working space tool should have been used but returned irrelevant results.

**Root Cause:** Working space lookup tool failed for this specific query (480V, Condition 3).

**Fix Needed:** Fix cec_lookup_working_space tool to handle 480V (301-600V range) and Condition 3 correctly.

---

## 6. cec2022-048 - SF-2 Fixture Wire Temperature (2/10)

**Question:** What is the maximum operating temperature for Type SF-2 silicone insulated fixture wire?

**Expected Answer:** 200°C (392°F) per CEC 2022 Table 402.3

**Agent Answer:** The referenced Table 402.3 in CEC 2022 does **not include an entry for Type SF-2 silicone insulated fixture wire**.

**Analysis:** The agent could not find SF-2 in the table data. This is a data gap in the cec_tables_unified.json file - the SF-2 fixture wire type is missing from Table 402.3.

**Root Cause:** Table 402.3 data is incomplete in the JSON file.

**Fix Needed:** Add SF-2 (and other missing fixture wire types) to Table 402.3 in cec_tables_unified.json.

---

## 7. cec2022-050 - Service Conductor Sizing (7/10)

**Question:** Size the conductors, EGC, and GEC for a 200A residential service using copper conductors.

**Expected Answer:** Service conductors: 3/0 AWG copper minimum (200A at 75°C per CEC Table 310.16)

**Agent Answer:** Service conductors: 2/0 AWG copper (per Table 310.12(A) dwelling-specific)

**Analysis:** Both answers can be considered correct depending on interpretation:
- Table 310.12(A) (dwelling-specific): 2/0 AWG copper for 200A dwelling services
- Table 310.16 (general): 3/0 AWG copper for 200A at 75°C

The expected answer uses the more conservative general approach. The agent used the dwelling-specific table which is technically correct for dwelling services.

**Root Cause:** Ambiguity in which table to use for dwelling service sizing.

**Fix Needed:** Consider accepting both answers or clarifying that dwelling-specific tables should be noted as alternatives.

---

## 8. cec2022-051 - Office Lighting Load (2/10)

**Question:** Calculate the general lighting load for a 5,000 square foot office building.

**Expected Answer:** Per CEC Table 220.12, office buildings require 1.3 VA per square foot. General lighting load = 5,000 sq ft x 1.3 VA/sq ft = 6,500 VA

**Agent Answer:** Unit load for office: 14 VA/sq ft (from Table 220.12). Total lighting load: 5,000 sq ft × 14 VA/sq ft = 70,000 VA

**Analysis:** Major error - the agent used 14 VA/m² (which is the metric conversion) instead of 1.3 VA/sq ft. The Table 220.12 data may have been returned in metric units or the agent misread the value.

**Root Cause:** Table 220.12 data or lookup returned wrong unit (VA/m² vs VA/ft²).

**Fix Needed:** Ensure Table 220.12 clearly returns values in VA/sq ft and agent uses correct units.

---

## 9. cec2022-001 - 12 AWG Ampacity (9/10)

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Expected Answer:** 20 amperes

**Agent Answer:** 25 amperes at 75°C (Table 310.16) with note about 240.4(D) 20A OCP limit.

**Analysis:** The agent provided the TABLE value (25A) which is technically the ampacity, but the expected answer wanted the PRACTICAL value limited by 240.4(D) which is 20A. The agent did mention 240.4(D) in the answer.

**Root Cause:** Question ambiguity - "ampacity" technically means table value (25A), but practical use is 20A.

**Fix Needed:** Consider accepting both 25A (table ampacity) and 20A (practical limit) as correct.

---

## 10. cec2022-045 - Enclosure Types (9/10)

**Question:** What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?

**Expected Answer:** Type 3, 3R, 3S, 4, 4X, 6, or 6P enclosures

**Agent Answer:** Type 3S, 3SX, 3X, 4, 4X, 6, 6P (missed Type 3 and 3R)

**Analysis:** Minor omission - the agent provided most correct enclosure types but missed Type 3 and 3R which are also suitable for rain exposure.

**Root Cause:** Table 110.28 lookup may have filtered out some enclosure types.

**Fix Needed:** Ensure complete enclosure type list is returned for outdoor weather queries.

---

## Summary of Root Causes

| Issue | Count | Priority |
|-------|-------|----------|
| Search/tool returning wrong results | 3 | High |
| Missing table data | 2 | High |
| Unit conversion errors | 1 | High |
| Code interpretation errors | 2 | Medium |
| Question ambiguity | 2 | Low |

## Recommended Fixes (Priority Order)

1. **High:** Fix surge protection search to reliably return 230.67
2. **High:** Add SF-2 fixture wire to Table 402.3 data
3. **High:** Fix working space tool for 480V/Condition 3
4. **High:** Fix Table 220.12 unit handling (VA/sq ft vs VA/m²)
5. **Medium:** Clarify 210.12(A) AFCI scope for dwelling units
6. **Medium:** Enhance California-specific table identification
7. **Low:** Accept alternative correct answers for ambiguous questions
