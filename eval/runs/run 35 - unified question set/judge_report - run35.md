# LLM-as-Judge Report - Run 35

**Date:** 2025-12-11
**Run Description:** First unified question set evaluation (53 questions)
**Judge:** Claude Code (manual evaluation)

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | 53 |
| Perfect Scores (10/10) | 43 |
| Partial Scores | 3 |
| Wrong Answers | 7 |
| Total Score | 482/530 |
| **Overall Accuracy** | **90.9%** |

## Scoring Rubric

- **Accuracy (0-5):** Does the answer match the expected answer?
- **Completeness (0-5):** Does the answer include all required code references and details?
- **Total Score:** Accuracy + Completeness (0-10)

---

## Detailed Scores

| ID | Category | Score | Notes |
|----|----------|-------|-------|
| cec2022-001 | table_lookup | 9/10 | Gave 25A ampacity (correct) but expected answer wanted 20A (OCP limit) |
| cec2022-002 | table_lookup | 10/10 | Correct: 6 AWG copper |
| cec2022-003 | knowledge_simple | 10/10 | Correct: GFCI for countertop per 210.8(A)(6) |
| cec2022-004 | knowledge_simple | 10/10 | Correct: Yes AFCI per 210.12(A) |
| cec2022-005 | table_lookup | 10/10 | Correct: 4/0 AWG aluminum |
| cec2022-006 | knowledge_simple | 10/10 | Correct: 36 inches (3 feet) |
| cec2022-007 | knowledge_simple | 10/10 | Correct: Two 20A circuits |
| cec2022-008 | knowledge_simple | 10/10 | Correct: Yes per 230.67 |
| cec2022-009 | multi_article | 10/10 | Correct: Both copper and aluminum options |
| cec2022-010 | multi_article | 10/10 | Correct: MWBC requirements covered |
| cec2022-011 | knowledge | 10/10 | Correct: All GFCI locations listed |
| cec2022-012 | knowledge | **2/10** | **WRONG:** Said surge NOT required; Expected YES per 230.67 |
| cec2022-013 | edge_cases | 10/10 | Correct: Multiple violations identified |
| cec2022-014 | edge_cases | 10/10 | Correct: Violation per 110.14(A) |
| cec2022-015 | grounding_bonding | 10/10 | Correct: Separation of neutral/ground |
| cec2022-016 | grounding_bonding | 10/10 | Correct: MBJ vs SBJ distinction |
| cec2022-017 | load_calculations | 10/10 | Correct: Two circuits, can serve dining |
| cec2022-018 | load_calculations | 10/10 | Correct: 19.7A calculation |
| cec2022-019 | why_questions | 10/10 | Correct: AFCI prevents arc faults |
| cec2022-020 | why_questions | 10/10 | Correct: Torque per 110.14(D) |
| cec2022-021 | panel_load_calculation | 10/10 | Correct: 200A panel adequate |
| cec2022-022 | clearance_violations | 10/10 | Correct: Depth and obstruction violations |
| cec2022-023 | gfci_afci_compliance | **6/10** | **PARTIAL:** Incorrectly exempted refrigerator from AFCI |
| cec2022-024 | subpanel_violations | 10/10 | Correct: All violations identified |
| cec2022-025 | conduit_fill | 10/10 | Correct: 28 conductors |
| cec2022-026 | voltage_drop | 10/10 | Correct: 2.37% meets 3% limit |
| cec2022-027 | derating_calculation | 10/10 | Correct: 11.36A calculation |
| cec2022-028 | grounding_electrode_conductor | 10/10 | Correct: 2/0 AWG copper GEC |
| cec2022-029 | panelboard_requirements | 10/10 | Correct: All appliances per 408.2 |
| cec2022-030 | ev_charging | 10/10 | Correct: Article 625 and CALGreen |
| cec2022-031 | solar_pv | 10/10 | Correct: PV requirements covered |
| cec2022-032 | heat_pump | 10/10 | Correct: Circuit requirements |
| cec2022-033 | electrification | 10/10 | Correct: Cooktop readiness per 408.2 |
| cec2022-034 | electrification | 10/10 | Correct: Dryer circuit requirements |
| cec2022-035 | overcurrent | **5/10** | **PARTIAL:** Said Table 240.4(G) has no CA-specific content; Expected says it's California-only |
| cec2022-036 | surge_protection | 10/10 | Correct: Table 242.3 is CA-specific |
| cec2022-037 | motor_control | 10/10 | Correct: Table 430.72(B) details |
| cec2022-038 | medium_voltage | **7/10** | **PARTIAL:** Mentioned some tables but expected 18 tables (311.60(C)(67)-(86)) |
| cec2022-039 | conductor_ampacity | 10/10 | Correct: 230A at 75°C |
| cec2022-040 | grounding | 10/10 | Correct: 6 AWG copper / 4 AWG aluminum |
| cec2022-041 | grounding | 10/10 | Correct: 4 AWG copper / 2 AWG aluminum |
| cec2022-042 | ampacity_adjustment | 10/10 | Correct: 0.88 correction factor |
| cec2022-043 | ampacity_adjustment | 10/10 | Correct: 0.70 (70%) bundling factor |
| cec2022-044 | working_space | **3/10** | **WRONG:** Did not provide 1.2m (4 ft) answer; discussed wrong topic |
| cec2022-045 | enclosure | 9/10 | Mostly correct enclosure types |
| cec2022-046 | lighting_load | 10/10 | Correct: 1.3 VA/sq ft |
| cec2022-047 | flexible_cord | 10/10 | Correct: 25A flexible cord |
| cec2022-048 | fixture_wire | **2/10** | **WRONG:** Said SF-2 not in table; Expected 200°C |
| cec2022-049 | adjusted_ampacity | 10/10 | Correct: 30.8A calculation |
| cec2022-050 | service_sizing | **7/10** | **PARTIAL:** Said 2/0 AWG service conductors; Expected 3/0 AWG |
| cec2022-051 | commercial_load | **2/10** | **WRONG:** Used 14 VA/sq ft (70,000 VA); Expected 1.3 VA/sq ft (6,500 VA) |
| cec2022-052 | motor_circuit | 10/10 | Correct: 10A max |
| cec2022-053 | dwelling_load | 10/10 | Correct: 7,200 VA |

---

## Score Distribution by Category

| Category | Questions | Avg Score |
|----------|-----------|-----------|
| table_lookup | 3 | 9.7/10 |
| knowledge_simple | 5 | 10.0/10 |
| knowledge | 2 | 6.0/10 |
| multi_article | 2 | 10.0/10 |
| edge_cases | 2 | 10.0/10 |
| grounding_bonding | 2 | 10.0/10 |
| load_calculations | 2 | 10.0/10 |
| why_questions | 2 | 10.0/10 |
| panel_load_calculation | 1 | 10.0/10 |
| clearance_violations | 1 | 10.0/10 |
| gfci_afci_compliance | 1 | 6.0/10 |
| subpanel_violations | 1 | 10.0/10 |
| conduit_fill | 1 | 10.0/10 |
| voltage_drop | 1 | 10.0/10 |
| derating_calculation | 1 | 10.0/10 |
| grounding_electrode_conductor | 1 | 10.0/10 |
| panelboard_requirements | 1 | 10.0/10 |
| ev_charging | 1 | 10.0/10 |
| solar_pv | 1 | 10.0/10 |
| heat_pump | 1 | 10.0/10 |
| electrification | 2 | 10.0/10 |
| overcurrent | 1 | 5.0/10 |
| surge_protection | 1 | 10.0/10 |
| motor_control | 1 | 10.0/10 |
| medium_voltage | 1 | 7.0/10 |
| conductor_ampacity | 1 | 10.0/10 |
| grounding | 2 | 10.0/10 |
| ampacity_adjustment | 2 | 10.0/10 |
| working_space | 1 | 3.0/10 |
| enclosure | 1 | 9.0/10 |
| lighting_load | 1 | 10.0/10 |
| flexible_cord | 1 | 10.0/10 |
| fixture_wire | 1 | 2.0/10 |
| adjusted_ampacity | 1 | 10.0/10 |
| service_sizing | 1 | 7.0/10 |
| commercial_load | 1 | 2.0/10 |
| motor_circuit | 1 | 10.0/10 |
| dwelling_load | 1 | 10.0/10 |

---

## Key Findings

### Strengths
1. **Core electrical calculations:** Ampacity adjustments, derating, voltage drop - all correct
2. **Grounding and bonding:** Excellent understanding of MBJ/SBJ, subpanel configuration
3. **GFCI/AFCI locations:** Comprehensive coverage of protection requirements
4. **California-specific requirements:** Good on electrification readiness (408.2)
5. **Multi-article synthesis:** Strong performance on complex scenarios

### Weaknesses
1. **Surge protection inconsistency:** cec2022-012 incorrectly stated surge protection NOT required (contradicts cec2022-008 where it was correct)
2. **Table data gaps:** SF-2 fixture wire (402.3) and some medium voltage tables not found
3. **Working space depth:** Failed to provide correct answer for 480V Condition 3 (1.2m/4ft)
4. **Office lighting load:** Used wrong unit value (14 VA/sq ft instead of 1.3 VA/sq ft)
5. **Service conductor sizing:** Used Table 310.12(A) instead of Table 310.16 for general sizing

---

## Comparison with Previous Runs

| Run | Questions | Score | Notes |
|-----|-----------|-------|-------|
| Run 35 | 53 | 90.9% | First unified evaluation |

---

## Recommendations for Improvement

1. **Fix surge protection tool response:** The search sometimes returns no requirement when 230.67 clearly mandates it
2. **Add SF-2 to Table 402.3 data:** The fixture wire table is missing this entry
3. **Working space tool improvement:** 480V Condition 3 lookup returned wrong section
4. **Office lighting load fix:** Ensure Table 220.12 returns 1.3 VA/sq ft (not 14 VA/m²)
5. **Service conductor guidance:** Clarify when to use Table 310.12(A) vs 310.16
