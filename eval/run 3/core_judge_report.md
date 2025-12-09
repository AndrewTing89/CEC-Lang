# LLM Judge Report: Core Evaluation

## Summary
- Total Questions: 28
- Accurate: 11/28 (39.3%)
- Partially Accurate: 10/28 (35.7%)
- Inaccurate: 7/28 (25.0%)

## Scoring Criteria
- **Accurate**: Answer contains all key facts from expected answer
- **Partially Accurate**: Answer contains some but not all key facts
- **Inaccurate**: Answer is wrong or missing critical information
- Extra detail beyond expected answer is NOT penalized

## Results

| ID | Category | Verdict | Notes |
|----|----------|---------|-------|
| baseline-001 | table_lookup | Partially Accurate | Agent says 25A (table value), but expected answer is 20A (overcurrent protection limit per 240.4(D)). Agent mentions 240.4(D) but presents 25A as main answer instead of 20A. |
| baseline-002 | table_lookup | Inaccurate | Expected: 6 AWG copper. Agent: 4 AWG copper. Wrong conductor size selected. |
| baseline-003 | knowledge_simple | Partially Accurate | Correctly identifies countertop receptacles need GFCI. Missing explicit mention of dishwasher GFCI requirement. |
| baseline-004 | knowledge_simple | Accurate | Correctly states AFCI required for bedroom circuits per 210.12(A). |
| baseline-005 | table_lookup | Inaccurate | Expected: 4/0 AWG aluminum. Agent: 250 kcmil aluminum. Wrong size specified. |
| baseline-006 | knowledge_simple | Accurate | Correctly identifies 36 inches (900mm/3 feet) minimum depth. |
| baseline-007 | knowledge_simple | Accurate | Correctly states minimum of two 20A small appliance circuits required. |
| baseline-008 | knowledge_simple | Accurate | Correctly identifies surge protection is required per NEC 2023 Section 230.67(A). |
| core-001 | multi_article | Accurate | Correctly identifies 2/0 AWG copper OR 4/0 AWG aluminum. Provides detailed load calculation. |
| core-002 | multi_article | Partially Accurate | Correctly identifies common trip requirement and 20A max breaker. Missing specific mention that common trip is required for line-to-line AND line-to-neutral loads. Missing conductor grouping requirement per 210.4(D). |
| core-003 | nec_2023_updates | Partially Accurate | Lists most locations but missing "unfinished basements" and "utility rooms with sinks" as separate specific callouts. Has general categories but not all specific locations from expected answer. |
| core-004 | nec_2023_updates | Partially Accurate | Answers CEC 2022 instead of NEC 2023 as asked. Correctly identifies Type 1/Type 2 SPD and installation locations, but mixes up which code edition was asked about. |
| core-005 | edge_cases | Partially Accurate | Identifies insufficient front clearance (24" vs 36"). Missing critical violation: panels prohibited in clothes closets per 240.24(D). Missing "no storage in working space" violation. |
| core-006 | edge_cases | Accurate | Correctly identifies this as a violation per 110.14(A) and 110.3(B). |
| core-007 | grounding_bonding | Partially Accurate | Correctly mentions grounds and neutrals must be separated and need grounding electrode. Missing explicit statement "NO main bonding jumper in subpanel" and "neutral bar must be isolated (not bonded to enclosure)". |
| core-008 | grounding_bonding | Accurate | Correctly explains difference between MBJ (at service) and SBJ (at separately derived systems). Correct code references. |
| core-009 | load_calculations | Accurate | Correctly states minimum two 20A circuits required and they CAN serve dining room. Mentions they should serve dining/pantry/breakfast room. |
| core-010 | load_calculations | Accurate | Correctly calculates: 30A × 0.82 × 0.80 = 19.68A (approximately 20A). All factors applied correctly. |
| core-011 | why_questions | Accurate | Correctly explains AFCI prevents electrical fires from arc faults, detects series and parallel arcing. Good technical explanation. |
| core-012 | why_questions | Accurate | Correctly identifies requirements in 110.14(D) and 110.3(B). Explains why torque matters (prevents loose connections, high resistance, heat, arcing). |
| inspection-001 | panel_load_calculation | Partially Accurate | Final answer 115.42A is close to expected 103.2A. Methodology appears correct but slight differences in demand factor application. Correctly concludes 200A panel is adequate. |
| inspection-002 | clearance_violations | Partially Accurate | Correctly identifies depth violation (28" < 36" required, though agent says 30" required which is NEC not CEC). Identifies water heater obstruction. Uses NEC 2023 instead of CEC as context suggests residential California. |
| inspection-005 | gfci_afci_compliance | Inaccurate | Major errors: Says dishwasher, disposal, and refrigerator are exempt from GFCI/AFCI. Expected answer requires GFCI for dishwasher and AFCI for all circuits. Agent incorrectly applies exceptions. |
| inspection-006 | subpanel_violations | Accurate | Correctly identifies main violations: neutral bar should NOT be bonded to enclosure, should NOT have main bonding jumper. Correct configuration explained. |
| inspection-007 | conduit_fill | Partially Accurate | Agent calculates 28 conductors. Expected answer says 28 or 29 depending on rounding (0.91 > 0.8 rounds up to 29, but conservative is 28). Agent answer is acceptable. |
| inspection-008 | voltage_drop | Accurate | Correctly calculates 2.84V drop and 2.37%. Correctly concludes this meets 3% recommendation. |
| inspection-009 | derating_calculation | Inaccurate | Expected: 11.36A (20A × 0.71 × 0.80). Agent: 9.94A (20A × 0.71 × 0.70). Wrong bundling factor used (0.70 instead of 0.80). |
| inspection-010 | grounding_electrode_conductor | Inaccurate | Expected: 2/0 AWG copper for 1000 kcmil service. Agent: 1/0 AWG copper. Wrong size per Table 250.66. |

## Detailed Analysis

### Issues Found

#### 1. Table Lookup Errors (Critical)
- **baseline-002**: Specified 4 AWG instead of 6 AWG for 60A circuit
- **baseline-005**: Specified 250 kcmil instead of 4/0 AWG aluminum for 200A service
- **inspection-010**: Specified 1/0 AWG instead of 2/0 AWG copper GEC

These errors suggest the agent has difficulty accurately navigating NEC/CEC tables or may be using incorrect table values. These are critical errors that would result in undersized conductors.

#### 2. Calculation Errors
- **baseline-001**: Presented table ampacity (25A) instead of overcurrent protection limit (20A) as main answer
- **inspection-009**: Used wrong bundling factor (0.70 instead of 0.80), resulting in 9.94A instead of 11.36A

The bundling factor error is particularly concerning as it shows confusion about which adjustment factor table to use.

#### 3. Missing Critical Code Violations
- **core-005**: Failed to identify that panels are PROHIBITED in clothes closets per 240.24(D) - this is a major safety violation
- **inspection-005**: Incorrectly claimed dishwasher, disposal, and refrigerator are exempt from GFCI/AFCI requirements - complete misapplication of exceptions

These demonstrate the agent can miss critical safety-related code violations.

#### 4. Incomplete Answers
- **baseline-003**: Missed dishwasher GFCI requirement
- **core-002**: Missing conductor grouping requirement per 210.4(D)
- **core-003**: Missing specific locations like "unfinished basements" and "utility rooms with sinks"
- **core-005**: Missing "no storage in working space" violation per 110.26(B)
- **core-007**: Not explicit enough about "NO main bonding jumper" and neutral bar isolation

While these answers contained correct information, they were incomplete and could lead to code violations if followed without additional verification.

#### 5. Code Edition Confusion
- **core-004**: Answered with CEC 2022 when NEC 2023 was asked
- **inspection-002**: Mixed NEC and CEC requirements (30" vs 36" depth)

This suggests the agent sometimes loses track of which code edition is being referenced.

### Strengths

#### 1. Strong Performance Areas
- **Grounding/Bonding Theory**: Correctly explained MBJ vs SBJ concepts (core-008)
- **Voltage Drop Calculations**: Accurate calculation and interpretation (inspection-008)
- **Working Clearances**: Generally correct on depth requirements (baseline-006)
- **Code Reasoning**: Good explanations of WHY requirements exist (core-011, core-012)

#### 2. Correct Fundamental Concepts
- AFCI requirements for bedrooms (baseline-004, baseline-007)
- Surge protection requirements NEC 2023 (baseline-008)
- Subpanel grounding violations (inspection-006)
- Service conductor sizing for upgrades (core-001)
- Torque specifications importance (core-012)
- Small appliance circuit requirements (core-009)

#### 3. Detailed Responses
- Agent provides extensive detail and code references
- Shows work for calculations step-by-step
- Compares CEC 2022 vs NEC 2023 consistently
- Attempts to verify exceptions
- Explains the reasoning behind code requirements

### Patterns Observed

#### Systematic Issues
1. **Table Lookup Accuracy**: Multiple errors in conductor sizing from tables (3 errors out of relevant questions)
2. **Adjustment Factors**: Inconsistent application of bundling/derating factors
3. **Exception Application**: Overly broad or incorrect application of exceptions (inspection-005)
4. **Critical Violations**: Sometimes misses the most serious code violations (closet panel prohibition)

#### Good Practices
1. Consistently shows calculations step-by-step
2. Provides specific code section references
3. Compares CEC and NEC editions for context
4. Explains reasoning behind requirements
5. Attempts to identify applicable exceptions

## Recommendations

### For Agent Improvement
1. **Enhance Table Lookup Accuracy**: Implement stricter verification for conductor sizing tables. Consider adding a validation step that cross-references table lookups.
2. **Adjustment Factor Precision**: Create standardized calculation templates for derating/bundling. Clearly distinguish between Table 310.15(B)(1) and 310.15(C)(1).
3. **Exception Handling**: More conservative approach to applying exceptions; verify carefully against exact code language.
4. **Critical Violations First**: Prioritize identifying the most serious code violations (prohibition rules, safety violations).
5. **Code Edition Awareness**: Clearly track which code edition is being asked about and maintain that context throughout the response.
6. **Completeness Checks**: Implement a checklist approach for multi-part questions to ensure all required elements are addressed.

### For Evaluation Process
1. The agent performs best on conceptual/reasoning questions (why/how questions)
2. Struggles most with precise table lookups and specific numeric values
3. May benefit from additional training on NEC/CEC table navigation and interpretation
4. Strong foundation in grounding/bonding theory but needs improvement in application details
5. Good at explaining concepts but needs to be more thorough in identifying all applicable violations

## Score Distribution by Category

| Category | Questions | Accurate | Partial | Inaccurate | Success Rate |
|----------|-----------|----------|---------|------------|--------------|
| table_lookup | 3 | 1 | 1 | 1 | 66.7% |
| knowledge_simple | 5 | 4 | 1 | 0 | 100.0% |
| multi_article | 2 | 1 | 1 | 0 | 100.0% |
| nec_2023_updates | 2 | 1 | 1 | 0 | 100.0% |
| edge_cases | 2 | 1 | 1 | 0 | 100.0% |
| grounding_bonding | 2 | 1 | 1 | 0 | 100.0% |
| load_calculations | 2 | 2 | 0 | 0 | 100.0% |
| why_questions | 2 | 2 | 0 | 0 | 100.0% |
| panel_load_calculation | 1 | 0 | 1 | 0 | 100.0% |
| clearance_violations | 1 | 0 | 1 | 0 | 100.0% |
| gfci_afci_compliance | 1 | 0 | 0 | 1 | 0.0% |
| subpanel_violations | 1 | 1 | 0 | 0 | 100.0% |
| conduit_fill | 1 | 0 | 1 | 0 | 100.0% |
| voltage_drop | 1 | 1 | 0 | 0 | 100.0% |
| derating_calculation | 1 | 0 | 0 | 1 | 0.0% |
| grounding_electrode_conductor | 1 | 0 | 0 | 1 | 0.0% |

**Note**: Success Rate = (Accurate + Partially Accurate) / Total Questions per category

### Category Performance Insights

**Strong Categories (100% success rate)**:
- Knowledge/Simple Questions: The agent excels at straightforward code requirement questions
- Load Calculations: Demonstrates solid understanding of load calculation procedures
- Why Questions: Excellent at explaining the reasoning behind code requirements
- Grounding/Bonding: Good conceptual understanding of grounding principles

**Weak Categories**:
- GFCI/AFCI Compliance: Only 0% accurate (1 question with major exception misapplication)
- Derating Calculations: Only 0% accurate (wrong adjustment factor)
- Grounding Electrode Conductor: Only 0% accurate (wrong table lookup)

## Overall Assessment

The CEC agent demonstrates **solid foundational knowledge** with a **75.0% success rate** (accurate + partially accurate). However, **25.0% of answers contain critical errors** that could lead to code violations or safety issues.

### Agent Capabilities:
**What the agent does well:**
- Explaining code concepts and reasoning
- Basic load calculations
- Identifying common code requirements
- Providing detailed code references
- Comparing CEC and NEC editions

**What needs improvement:**
- Precise table lookups (critical for conductor sizing)
- Applying adjustment/correction factors accurately
- Identifying ALL applicable code violations
- Exception application (tends to over-apply or misapply)
- Maintaining code edition context

### Recommended Use Cases:
- **Appropriate**: Educational tool for learning code concepts, study aid for understanding why requirements exist, preliminary research
- **Caution Required**: Final code compliance verification, conductor sizing calculations, critical safety determinations
- **Not Recommended**: Sole source for inspection decisions, permit applications without human verification

**Key Takeaway**: The agent is better suited as a **study aid or conceptual guide** rather than a definitive code compliance tool. All answers should be verified by a qualified professional, especially for:
1. Conductor sizing from tables
2. Adjustment factor calculations
3. Critical safety violations
4. Exception applications

The agent shows promise but requires **human oversight** for professional electrical work.

---
*Report Generated: 2025-12-06*
*Evaluation Set: Core Evaluation - 28 Questions*
*Model: CEC Agent (Run 3)*
*Judge: LLM-based evaluation with human-defined criteria*
