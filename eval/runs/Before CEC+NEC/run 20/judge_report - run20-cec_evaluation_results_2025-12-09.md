# Judge Report - run20-cec_evaluation_results_2025-12-09

## Metadata
| Field | Value |
|-------|-------|
| **Model Evaluated** | qwen/qwen3-32b |
| **Source File** | run20-cec_evaluation_results_2025-12-09.md |
| **Judge** | Claude Code (Opus 4.5) |
| **Method** | LLM-as-Judge |
| **Timestamp** | 2025-12-09 |
| **Key Change** | No mandatory exception search enforcement |

---

## Summary
| Metric | Value |
|--------|-------|
| **Total Questions** | 30 |
| **Total Score** | 285 / 300 |
| **Percentage** | 95.0% |
| **Avg Accuracy** | 4.77 / 5 |
| **Avg Completeness** | 4.73 / 5 |

---

## Score Distribution
| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 22 |
| High (8-9/10) | 7 |
| Low (5-7/10) | 1 |
| Very Low (0-4/10) | 0 |

---

## Comparison with Run 19

| Metric | Run 19 | Run 20 | Change |
|--------|--------|--------|--------|
| **Total Score** | 278/300 (92.7%) | 285/300 (95.0%) | **+7 (+2.3%)** |
| **Perfect Scores** | 22 | 22 | Same |
| **Exception Search Used** | 30/30 (forced) | 1/30 (voluntary) | -29 |
| **cec_lookup_table Used** | 7/30 | 10/30 | +3 |
| **Avg Duration** | 18.6s | 11.6s | **-7.0s (37% faster)** |

### Hypothesis Validated
**Removing mandatory exception search IMPROVED scores:**
- cec-007: Run 19 = 6/10, Run 20 = **10/10** (+4)
- cec-008: Run 19 = 5/10, Run 20 = **10/10** (+5)
- Overall: +7 points improvement

### Speed Improvement
Agent is **37% faster** (11.6s vs 18.6s per question) by not forcing unnecessary exception searches.

---

## All Evaluations

| ID | Question | Accuracy | Completeness | Total |
|----|----------|----------|--------------|-------|
| cec-001 | Panelboard space requirements | 5/5 | 5/5 | 10/10 |
| cec-002 | EV charging infrastructure | 5/5 | 5/5 | 10/10 |
| cec-003 | Solar PV requirements | 5/5 | 5/5 | 10/10 |
| cec-004 | Heat pump water heater circuits | 5/5 | 5/5 | 10/10 |
| cec-005 | Electric cooktop readiness | 5/5 | 5/5 | 10/10 |
| cec-006 | Electric clothes dryer circuits | 5/5 | 5/5 | 10/10 |
| cec-007 | CEC Table 240.4(G) | 5/5 | 5/5 | 10/10 |
| cec-008 | CEC Table 242.3 | 5/5 | 5/5 | 10/10 |
| cec-009 | CEC Table 430.72(B) | 5/5 | 5/5 | 10/10 |
| cec-010 | Medium voltage cable tables | 5/5 | 5/5 | 10/10 |
| cec-011 | 4/0 AWG copper ampacity | 5/5 | 5/5 | 10/10 |
| cec-012 | EGC for 200A circuit | 5/5 | 5/5 | 10/10 |
| cec-013 | GEC for 3/0 service | 4/5 | 4/5 | 8/10 |
| cec-014 | Temperature correction factor | 5/5 | 5/5 | 10/10 |
| cec-015 | Ampacity adjustment factor | 5/5 | 5/5 | 10/10 |
| cec-016 | Working space depth | 5/5 | 5/5 | 10/10 |
| cec-017 | Enclosure types | 5/5 | 4/5 | 9/10 |
| cec-018 | Lighting load VA/sqft | 5/5 | 5/5 | 10/10 |
| cec-019 | Flexible cord ampacity | 5/5 | 5/5 | 10/10 |
| cec-020 | SF-2 wire temperature | 5/5 | 5/5 | 10/10 |
| cec-021 | Adjusted ampacity calc | 5/5 | 5/5 | 10/10 |
| cec-022 | 200A service sizing | 4/5 | 4/5 | 8/10 |
| cec-023 | Office lighting load | 5/5 | 5/5 | 10/10 |
| cec-024 | Motor control OCP | 5/5 | 5/5 | 10/10 |
| cec-025 | Dwelling lighting load | 5/5 | 5/5 | 10/10 |
| cec-026 | Kitchen GFCI comparison | 3/5 | 4/5 | 7/10 |
| cec-027 | Panelboard comparison | 5/5 | 5/5 | 10/10 |
| cec-028 | EV charging comparison | 5/5 | 5/5 | 10/10 |
| cec-029 | AFCI comparison | 5/5 | 4/5 | 9/10 |
| cec-030 | Solar PV comparison | 4/5 | 5/5 | 9/10 |

---

## Key Improvements from Run 19

### cec-001: Panelboard Space Requirements (Run 19: 8/10 → Run 20: 10/10)
**Improvement:** Now correctly lists all 4 appliances: heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers. Previously listed wrong appliances.

### cec-004, cec-005, cec-006: Electrification Requirements (Run 19: ~6/10 → Run 20: 10/10)
**Improvement:** All three now correctly identify CEC 408.2 reserved panelboard space requirements. Previously incorrectly stated "no California amendments."

### cec-007: Table 240.4(G) (Run 19: 6/10 → Run 20: 10/10)
**Improvement:** Without forced exception search, agent focuses on TABLE CONTENT (article references, conductor applications) rather than being polluted by low-relevance exception results.

### cec-008: Table 242.3 (Run 19: 5/10 → Run 20: 10/10)
**Improvement:** Agent now correctly describes this as "California-specific cross-reference table for overvoltage protection requirements" with detailed equipment-to-article mappings.

### cec-020: SF-2 Temperature (Run 19: 6/10 → Run 20: 10/10)
**Improvement:** Now correctly states 200°C per CEC Table 402.3. Previously stated incorrect 180°C.

---

## Detailed Results for Imperfect Scores

### cec-013 (Score: 8/10)
**Question:** What size GEC is required for a 3/0 AWG copper service conductor?
**Accuracy:** 4/5 - Correctly states 4 AWG copper
**Completeness:** 4/5 - Missing aluminum option (2 AWG)
**Notes:** Expected answer includes "4 AWG copper OR 2 AWG aluminum". Agent only mentions copper.

---

### cec-017 (Score: 9/10)
**Question:** Enclosure types for outdoor rain/sleet/ice
**Accuracy:** 5/5 - All types listed are valid
**Completeness:** 4/5 - Lists 3, 3S, 3SX, 3X, 4, 4X, 6, 6P (missing 3R from expected)
**Notes:** Minor difference in enclosure list. All types listed are correct for the conditions.

---

### cec-022 (Score: 8/10)
**Question:** 200A residential service sizing
**Accuracy:** 4/5 - Service conductor size discrepancy
**Completeness:** 4/5 - EGC and GEC correct
**Notes:** Agent says 2/0 AWG copper (CEC Table 310.12(A) for dwellings), expected says 3/0 AWG (Table 310.16). Agent's answer is actually correct for dwelling services per CEC's special table.

---

### cec-026 (Score: 7/10)
**Question:** Compare kitchen GFCI requirements CEC vs NEC
**Accuracy:** 3/5 - Gets restrictiveness direction wrong
**Completeness:** 4/5 - Good coverage of requirements
**Notes:**
- Expected: CEC is MORE PERMISSIVE (limits to countertops + 6ft from sink)
- Agent: Claims CEC is MORE RESTRICTIVE due to Title 24 CALGreen
- The agent's reasoning about CALGreen is valid but doesn't match the expected answer's focus on base code comparison

---

### cec-029 (Score: 9/10)
**Question:** Compare AFCI requirements CEC vs NEC
**Accuracy:** 5/5 - Correctly states requirements are similar
**Completeness:** 4/5 - Good detail but could list all room types more explicitly
**Notes:** Minor completeness issue only.

---

### cec-030 (Score: 9/10)
**Question:** Compare solar PV requirements
**Accuracy:** 4/5 - Focuses on AC module differences rather than the mandate
**Completeness:** 5/5 - Good technical detail
**Notes:** Expected answer emphasizes California MANDATES solar; agent focuses on technical differences in Article 690.

---

## Analysis

### What Changed?
1. **No forced exception search** → Agent answers based on retrieved content without pollution from low-relevance exception results
2. **Faster execution** → 37% reduction in response time
3. **Better tool selection** → cec_lookup_table used 10 times vs 7 times in run 19
4. **Voluntary exception search** → Only called when contextually relevant (1/30)

### Why It Worked
The mandatory exception search was:
1. **Redundant** - Footnote augmentation already injects cross-references like 240.4(D)
2. **Harmful** - Forced low-relevance (0.24-0.50 similarity) results that polluted answers

By removing it, the agent now:
1. Focuses on the most relevant tool results
2. Can synthesize cleaner answers without noise
3. Runs faster by skipping unnecessary searches

### Remaining Issue: cec-026 (GFCI Comparison)
The expected answer says CEC is MORE PERMISSIVE, but the agent argues CEC is MORE RESTRICTIVE due to Title 24 CALGreen. This is a nuanced disagreement:
- **Base code (210.8)**: CEC may be more permissive
- **With CALGreen**: California overall may be more restrictive

This may warrant reviewing the expected answer or adding nuance to handle both perspectives.
