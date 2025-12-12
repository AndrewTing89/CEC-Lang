# LLM-as-Judge Evaluation Report - Run 12

**Date:** 2025-12-09
**Model Evaluated:** Qwen3 32B (via Groq)
**Judge:** Claude Opus 4.5 (direct evaluation)

---

## Executive Summary

| Metric | Core (28 Q) | CEC (30 Q) | Combined (58 Q) |
|--------|-------------|------------|-----------------|
| **PASS** | 27 (96.4%) | 29 (96.7%) | 56 (96.6%) |
| **FAIL** | 1 (3.6%) | 1 (3.3%) | 2 (3.4%) |
| **Avg Score** | 8.9/10 | 9.3/10 | 9.1/10 |

### Overall Verdict: EXCELLENT

The CEC Lang Agent with Qwen3 32B demonstrates strong performance on both NEC/CEC code questions, achieving a **96.6% pass rate** with an average score of **9.1/10**.

---

## Scoring Criteria

Each answer evaluated on 0-10 scale:
- **Technical Accuracy**: Correctness of values, calculations, and code interpretations
- **Completeness**: Coverage of all question aspects
- **Code References**: Proper NEC/CEC section citations
- **Reasoning Quality**: Clarity and logic of explanation

**PASS** = Overall score >= 6/10
**FAIL** = Overall score < 6/10

---

## Core Evaluation Results (28 Questions)

### Failed Questions (1)

| ID | Question | Expected | Agent Answer | Issue | Score |
|----|----------|----------|--------------|-------|-------|
| **core-010** | Adjusted ampacity for 12 AWG THHN at 50°C, 6 conductors | 30A × 0.82 × 0.80 = 19.68A | 25A × 0.75 × 0.80 = 15A | Wrong base ampacity (used 75°C column instead of 90°C for THHN) and wrong temp factor | 5/10 |

### Passed Questions Summary (27)

| Category | Questions | Avg Score |
|----------|-----------|-----------|
| Baseline (1-8) | 8 | 9.6/10 |
| Core Technical (1-12) | 11 | 9.5/10 |
| Inspection (1-10) | 8 | 9.0/10 |

### Notable Strengths:
- **baseline-001**: Agent correctly stated 25A ampacity (the expected "20A" is actually the OCP limit, not ampacity)
- **baseline-005**: Excellent distinction between dwelling (2/0 AWG with 83% rule) vs non-dwelling (4/0 AWG) aluminum service sizing
- **inspection-007**: Conduit fill calculation (28 conductors max) perfectly executed
- **inspection-008**: Voltage drop calculation (2.84V, 2.37%) matches expected exactly

### Areas for Improvement:
- **core-010**: Must use 90°C column for THHN conductors when applying temperature correction, then limit to termination temperature
- **inspection-010**: Should use direct Table 250.66 lookup instead of ratio calculation for GEC sizing

---

## CEC Evaluation Results (30 Questions)

### Failed Questions (1)

| ID | Question | Expected | Agent Answer | Issue | Score |
|----|----------|----------|--------------|-------|-------|
| **cec-020** | SF-2 fixture wire max temp | 200°C | 180°C | Incorrect temperature rating from Table 402.3 | 4/10 |

### Passed Questions Summary (29)

| Category | Questions | Avg Score |
|----------|-----------|-----------|
| CA-Specific Requirements (1-10) | 10 | 9.6/10 |
| Table Lookups (11-20) | 9 | 9.4/10 |
| Calculations (21-25) | 5 | 9.6/10 |
| CEC vs NEC Comparisons (26-30) | 5 | 8.8/10 |

### Notable Strengths:
- **cec-001 through cec-006**: Perfect coverage of California electrification readiness requirements (408.2 panelboard spaces)
- **cec-010**: Correctly identified all 18 California-only medium voltage tables (311.60(C)(67)-(86))
- **cec-021**: Ampacity adjustment calculation (30.8A) executed perfectly
- **cec-023, cec-025**: Lighting load calculations correct (1.3 VA/sq ft for office, 3 VA/sq ft for dwelling)

### Areas for Improvement:
- **cec-017**: Enclosure types list incomplete (missed 3, 3R, 6P)
- **cec-020**: Table 402.3 lookup error - SF-2 is 200°C, not 180°C
- Comparison questions could more strongly emphasize California's mandatory requirements vs NEC's optional installation rules

---

## Detailed Pass/Fail by Question

### Core Evaluation
```
baseline-001  PASS (9/10)   baseline-002  PASS (10/10)
baseline-003  PASS (8/10)   baseline-004  PASS (10/10)
baseline-005  PASS (10/10)  baseline-006  PASS (10/10)
baseline-007  PASS (10/10)  baseline-008  PASS (10/10)
core-001      PASS (10/10)  core-002      PASS (10/10)
core-003      PASS (8/10)   core-004      PASS (10/10)
core-005      PASS (8/10)   core-006      PASS (9/10)
core-007      PASS (10/10)  core-008      PASS (10/10)
core-009      PASS (10/10)  core-010      FAIL (5/10) ***
core-011      PASS (10/10)  core-012      PASS (10/10)
inspection-001 PASS (8/10)  inspection-002 PASS (10/10)
inspection-005 PASS (7/10)  inspection-006 PASS (10/10)
inspection-007 PASS (10/10) inspection-008 PASS (10/10)
inspection-009 PASS (10/10) inspection-010 PASS (6/10)
```

### CEC Evaluation
```
cec-001  PASS (10/10)  cec-002  PASS (9/10)
cec-003  PASS (10/10)  cec-004  PASS (10/10)
cec-005  PASS (10/10)  cec-006  PASS (10/10)
cec-007  PASS (8/10)   cec-008  PASS (9/10)
cec-009  PASS (10/10)  cec-010  PASS (10/10)
cec-011  PASS (10/10)  cec-012  PASS (10/10)
cec-013  PASS (10/10)  cec-014  PASS (10/10)
cec-015  PASS (10/10)  cec-016  PASS (10/10)
cec-017  PASS (8/10)   cec-018  PASS (10/10)
cec-019  PASS (10/10)  cec-020  FAIL (4/10) ***
cec-021  PASS (10/10)  cec-022  PASS (8/10)
cec-023  PASS (10/10)  cec-024  PASS (9/10)
cec-025  PASS (10/10)  cec-026  PASS (9/10)
cec-027  PASS (10/10)  cec-028  PASS (8/10)
cec-029  PASS (9/10)   cec-030  PASS (8/10)
```

---

## Methodology

This LLM-as-Judge evaluation was performed by Claude Opus 4.5 directly reviewing each Q&A pair. Each response was evaluated against:

1. **Expected Answer** - Ground truth from the question bank
2. **Technical Accuracy** - Correctness of code values, calculations
3. **Completeness** - Coverage of all question aspects
4. **Code References** - Proper NEC/CEC section citations
5. **Reasoning Quality** - Clarity and logic of explanation

A **PASS** verdict requires an overall score >= 6/10.

---

## Conclusion

The CEC Lang Agent demonstrates production-ready performance for electrical code questions:

- **96.6% accuracy** across 58 diverse questions
- **Strong table lookup capability** with proper code references
- **Excellent calculation skills** for ampacity adjustments, voltage drop, conduit fill
- **Good California-specific knowledge** of CEC amendments and requirements

The two failures (core-010 and cec-020) represent edge cases in table interpretation that can be addressed with targeted improvements to the agent's reasoning about temperature ratings and ampacity column selection.
