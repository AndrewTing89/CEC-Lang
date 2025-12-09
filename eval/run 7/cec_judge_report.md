# LLM Judge Report: CEC Evaluation (Run 7 - Multi-Run)

## Summary
- Total Questions: 30
- Accurate: 22/30 (73.3%)
- Partially Accurate: 8/30 (26.7%)
- Inaccurate: 0/30 (0.0%)
- Runs per Question: 3
- Aggregation Method: Majority Voting

## Scoring Criteria
- **Accurate**: Answer contains all key facts from expected answer
- **Partially Accurate**: Answer contains some but not all key facts
- **Inaccurate**: Answer is wrong or missing critical information
- **Extra detail beyond expected answer is NOT penalized**

## Results

| ID | Category | Verdict | Consistency | Notes |
|----|----------|---------|-----------|-------|
| cec-001 | panelboard_requirements | Accurate | 100% | Found 5 appliances with code reference |
| cec-002 | ev_charging | Partially Accurate | 100% | Has some EV requirements |
| cec-003 | solar_pv | Partially Accurate | 100% | Incomplete solar PV requirements |
| cec-004 | heat_pump | Accurate | 100% | Correct reserved space requirement with code reference |
| cec-005 | electrification | Partially Accurate | 100% | Has some requirements |
| cec-006 | electrification | Accurate | 100% | Correct reserved space for dryer |
| cec-007 | overcurrent | Accurate | 100% | Correctly identifies CEC-only table |
| cec-008 | surge_protection | Partially Accurate | 100% | Has partial info |
| cec-009 | motor_control | Accurate | 100% | Correct motor control OCP table info |
| cec-010 | medium_voltage | Partially Accurate | 100% | Has some info |
| cec-011 | conductor_ampacity | Accurate | 100% | Correct ampacity (230A) with table reference |
| cec-012 | grounding | Accurate | 100% | Correct EGC size with table reference |
| cec-013 | grounding | Accurate | 100% | Correct GEC size with table reference |
| cec-014 | ampacity_adjustment | Accurate | 100% | Correct factor (0.88) with table reference |
| cec-015 | ampacity_adjustment | Accurate | 100% | Correct factor (0.70/70%) with table reference |
| cec-016 | working_space | Accurate | 100% | Correct working space (4 ft/1.2m) with reference |
| cec-017 | enclosure | Accurate | 100% | Found 6 enclosure types with reference |
| cec-018 | lighting_load | Accurate | 100% | Correct office load (1.3 VA/sq ft) with reference |
| cec-019 | flexible_cord | Partially Accurate | 100% | Check flexible cord ampacity |
| cec-020 | fixture_wire | Accurate | 100% | Correct temperature (200C/392F) with reference |
| cec-021 | adjusted_ampacity | Accurate | 100% | Correct calculation with all factors |
| cec-022 | service_sizing | Partially Accurate | 100% | Has 1 correct size(s) |
| cec-023 | commercial_load | Partially Accurate | 100% | Check calculation |
| cec-024 | motor_circuit | Accurate | 100% | Correct OCP (10A) with table reference |
| cec-025 | dwelling_load | Accurate | 100% | Correct calculation (2400 x 3 = 7,200 VA) |
| cec-026 | gfci | Accurate | 100% | Correctly explains CEC more permissive |
| cec-027 | panelboard | Accurate | 100% | Correctly explains CEC-only requirement |
| cec-028 | ev_charging | Accurate | 100% | Correctly explains CA mandate vs NEC guidance |
| cec-029 | afci | Accurate | 100% | Correctly identifies similar requirements |
| cec-030 | solar_pv | Accurate | 100% | Correctly explains CA mandate vs NEC installation rules |


## Detailed Analysis

### Issues Found

**No Inaccurate Answers!**

**Partially Accurate Answers (8):**
- cec-002: Has some EV requirements (Consistency: 100%)
- cec-003: Incomplete solar PV requirements (Consistency: 100%)
- cec-005: Has some requirements (Consistency: 100%)
- cec-008: Has partial info (Consistency: 100%)
- cec-010: Has some info (Consistency: 100%)
- cec-019: Check flexible cord ampacity (Consistency: 100%)
- cec-022: Has 1 correct size(s) (Consistency: 100%)
- cec-023: Check calculation (Consistency: 100%)


### Strengths

**Accurate Answers (22/30 = 73.3%):**
- cec-001: Found 5 appliances with code reference
- cec-004: Correct reserved space requirement with code reference
- cec-006: Correct reserved space for dryer
- cec-007: Correctly identifies CEC-only table
- cec-009: Correct motor control OCP table info
- cec-011: Correct ampacity (230A) with table reference
- cec-012: Correct EGC size with table reference
- cec-013: Correct GEC size with table reference
- cec-014: Correct factor (0.88) with table reference
- cec-015: Correct factor (0.70/70%) with table reference
- cec-016: Correct working space (4 ft/1.2m) with reference
- cec-017: Found 6 enclosure types with reference
- cec-018: Correct office load (1.3 VA/sq ft) with reference
- cec-020: Correct temperature (200C/392F) with reference
- cec-021: Correct calculation with all factors
- cec-024: Correct OCP (10A) with table reference
- cec-025: Correct calculation (2400 x 3 = 7,200 VA)
- cec-026: Correctly explains CEC more permissive
- cec-027: Correctly explains CEC-only requirement
- cec-028: Correctly explains CA mandate vs NEC guidance
- cec-029: Correctly identifies similar requirements
- cec-030: Correctly explains CA mandate vs NEC installation rules


## Score Distribution by Category

| Category | Questions | Accurate | Partial | Inaccurate | Success Rate |
|----------|-----------|----------|---------|------------|--------------|
| adjusted_ampacity | 1 | 1 | 0 | 0 | 100.0% |
| afci | 1 | 1 | 0 | 0 | 100.0% |
| ampacity_adjustment | 2 | 2 | 0 | 0 | 100.0% |
| commercial_load | 1 | 0 | 1 | 0 | 100.0% |
| conductor_ampacity | 1 | 1 | 0 | 0 | 100.0% |
| dwelling_load | 1 | 1 | 0 | 0 | 100.0% |
| electrification | 2 | 1 | 1 | 0 | 100.0% |
| enclosure | 1 | 1 | 0 | 0 | 100.0% |
| ev_charging | 2 | 1 | 1 | 0 | 100.0% |
| fixture_wire | 1 | 1 | 0 | 0 | 100.0% |
| flexible_cord | 1 | 0 | 1 | 0 | 100.0% |
| gfci | 1 | 1 | 0 | 0 | 100.0% |
| grounding | 2 | 2 | 0 | 0 | 100.0% |
| heat_pump | 1 | 1 | 0 | 0 | 100.0% |
| lighting_load | 1 | 1 | 0 | 0 | 100.0% |
| medium_voltage | 1 | 0 | 1 | 0 | 100.0% |
| motor_circuit | 1 | 1 | 0 | 0 | 100.0% |
| motor_control | 1 | 1 | 0 | 0 | 100.0% |
| overcurrent | 1 | 1 | 0 | 0 | 100.0% |
| panelboard | 1 | 1 | 0 | 0 | 100.0% |
| panelboard_requirements | 1 | 1 | 0 | 0 | 100.0% |
| service_sizing | 1 | 0 | 1 | 0 | 100.0% |
| solar_pv | 2 | 1 | 1 | 0 | 100.0% |
| surge_protection | 1 | 0 | 1 | 0 | 100.0% |
| working_space | 1 | 1 | 0 | 0 | 100.0% |


## Consistency Analysis

| Consistency Level | Count | Percentage |
|-------------------|-------|------------|
| High (100%) | 30 | 100.0% |
| Medium (50-99%) | 0 | 0.0% |
| Low (<50%) | 0 | 0.0% |



## Comparison to Run 6

### Run 6 Results:
- Accurate: 22/30 (73.3%)
- Partially Accurate: 8/30 (26.7%)
- Inaccurate: 0/30 (0.0%)

### Run 7 Results (Multi-Run Averaged):
- Accurate: 22/30 (73.3%)
- Partially Accurate: 8/30 (26.7%)
- Inaccurate: 0/30 (0.0%)

## Overall Assessment

The CEC agent achieved:
- **22/30 Accurate** (73.3%)
- **8/30 Partially Accurate** (26.7%)
- **0/30 Inaccurate** (0.0%)

**Success Rate (Accurate + Partial)**: 100.0%

---
*Report Generated: Run 7 (Multi-Run Evaluation)*
*Evaluation Set: CEC Evaluation - 30 Questions*
