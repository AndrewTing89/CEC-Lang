# ChatGPT 5.1 (GPT-4.1) Wrong Answer Analysis

**Judge:** Claude Code (Claude Opus 4.5)
**Method:** LLM-as-Judge
**Overall Score:** 94.6% (246/260)

---

## Executive Summary

**Questions with Errors:** 2 of 26 answered (2 questions were not asked)

**Key Error Pattern:** The model demonstrates exceptional overall performance but shows critical failures in:
1. Basic table lookup (confusing temperature columns)
2. Reading comprehension (missing conduit size specification)
3. Load calculation methodology (ignoring demand factors)

**Most Critical Error:** Question baseline-001 - Stated 25A instead of 20A for 12 AWG at 75°C. This is a fundamental table lookup error that could lead to dangerous overcurrent protection sizing and fire hazards.

**Strengths:**
- Excellent understanding of complex code concepts (AFCI/GFCI requirements, grounding/bonding, multiwire branch circuits)
- Strong calculation methodology when applied correctly (derating, voltage drop)
- Thorough explanations with proper code references
- Comprehensive answers that often exceed minimum requirements
- 24 out of 26 questions scored perfectly (10/10)

---

## Detailed Error Analysis (2 of 26)

### 1. baseline-001: Table Lookup - 12 AWG Ampacity (Score: 4/10)

**Question:** What is the ampacity of 12 AWG copper conductor at 75°C termination?

**Model's Answer:** "At 75°C, 12 AWG copper has an ampacity of 25 amperes per NEC Table 310.16 (75°C column). Note: In most branch-circuit applications, 240.4(D) still limits 12 AWG copper to a 20A OCPD, even though its 75°C ampacity is 25A."

**Correct Answer:** 20 amperes

**What the Model Did Wrong:**
The model stated 25 amperes instead of the correct 20 amperes for 12 AWG copper at 75°C. The model confused the 75°C column (20A) with the 90°C column (25A) in Table 310.16. Ironically, the model then correctly references that 240.4(D) limits 12 AWG to 20A OCPD, demonstrating it knows the correct practical limitation but failed on the fundamental table lookup.

**Root Cause:**
Table column misidentification. The model appears to have looked up the 90°C ampacity (25A) and incorrectly labeled it as the 75°C value. This suggests either:
- Confusion about which temperature column to use
- Training data that incorrectly associated 12 AWG with 25A at 75°C
- Possible conflation with the fact that THHN is rated 90°C

**Impact:** Critical safety error. If an electrician sized overcurrent protection based on this answer, they could install a 25A breaker on 12 AWG conductors rated for 20A at 75°C terminations (the standard for most equipment). This creates a fire hazard.

**Score Breakdown:**
- Accuracy: 0/5 (completely wrong core answer)
- Completeness: 4/5 (provided helpful context about 240.4(D), but core answer wrong)

---

### 2. inspection-001: Load Calculation - Service Sizing (Score: 5/10)

**Question:** Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized. Show your work.

**Model's Answer:**
Calculated total load: 28,775 VA (120A at 240V)
Used full 12,000 VA for the electric range
Conclusion: 200A service is adequately sized

**Correct Answer:**
Total load: 24,775 VA (103.2A at 240V)
Range should use 8,000 VA demand from Table 220.55
Conclusion: 200A service is adequately sized with 48% safety margin

**What the Model Did Wrong:**
The model used the full nameplate rating (12,000 VA) for the electric range instead of applying the Table 220.55 demand factor (8,000 VA for one range ≤12 kW). This resulted in a 4,000 VA overcalculation (28,775 VA vs. 24,775 VA) and an amperage error of 16.8A (120A vs. 103.2A).

The model explicitly acknowledged Table 220.55 exists but chose to ignore it: "You have a single 12 kW electric range on a 40A breaker. Under 220.55 (ranges), for one range ≤12 kW or less, a common, conservative treatment for service calcs is: Use full nameplate: 12,000 VA (If you were using the table in a more optimized design context, you might apply its demand value, but using full nameplate is accepted and errs on the safe side.)"

**Root Cause:**
Misunderstanding of NEC load calculation methodology. The model incorrectly believed that using "full nameplate" is acceptable for service load calculations. However, NEC Article 220 explicitly requires using Table 220.55 demand factors for range loads in standard residential load calculations. The "conservative" approach the model cited is not code-compliant for this type of calculation.

**Impact:**
Moderate but significant. While the final conclusion (200A is adequate) is correct in both cases, the overcalculation would lead to:
- Oversized service conductors (waste of materials and cost)
- Incorrect documentation of actual service load
- Failure to follow standard NEC load calculation procedures
- In marginal cases, this error pattern could lead to undersizing when loads are subtracted rather than added

**Score Breakdown:**
- Accuracy: 1/5 (methodology partially correct but critical error in range demand factor)
- Completeness: 4/5 (showed most calculation steps but skipped Table 220.55 lookup)

---

### 3. inspection-007: Conduit Fill - Reading Comprehension Error (Score: 0/10)

**Question:** A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.

**Model's Answer:**
Answered for 1-inch RMC instead of 1¼-inch
Calculation: 0.610 in² ÷ 0.0211 in² = 28.9 conductors → 28 conductors maximum
(The model used 0.610 in² which is actually the 40% fill for 1¼-inch, but labeled it as 1-inch)

**Correct Answer:**
For 1¼-inch RMC: 29 conductors maximum
40% fill area: 0.610 in² (Table 4)
Conductor area: 0.0211 in² (Table 5)
Calculation: 0.610 ÷ 0.0211 = 28.91 → 29 per Note 7 (round up when decimal ≥ 0.8)

**What the Model Did Wrong:**
The model answered for the wrong conduit size (1-inch instead of 1¼-inch as specified). Interestingly, the model used the correct 40% fill area for 1¼-inch RMC (0.610 in²) but labeled it as 1-inch. This is a reading comprehension failure - the model didn't carefully read the question specification.

Additionally, the model's final answer of 28 conductors appears to ignore NEC Chapter 9 Note 7, which states: "When the decimal is 0.8 or larger, round up to the next whole number." Since 28.91 has a decimal of 0.91 (>0.8), the correct answer should be 29 conductors, not 28.

**Root Cause:**
1. Reading comprehension failure - did not process "1¼-inch" correctly
2. Possible confusion between similar conduit sizes
3. Did not apply Note 7 rounding rule correctly

**Impact:**
Critical field installation error. If an electrician followed this answer, they would:
- Install the wrong size conduit (1-inch instead of 1¼-inch)
- Potentially violate conduit fill requirements
- Create a code violation that would fail inspection

**Score Breakdown:**
- Accuracy: 0/5 (answered wrong question entirely)
- Completeness: 0/5 (calculation methodology correct but for wrong conduit size)

---

## Error Pattern Summary

| Error Type | Count | Questions |
|------------|-------|-----------|
| Table column confusion | 1 | baseline-001 |
| Load calculation methodology | 1 | inspection-001 |
| Reading comprehension | 1 | inspection-007 |
| **Total questions with errors** | **2** | **out of 26** |

### Common Themes:

1. **Basic vs. Complex Performance Gap**: The model excels at complex multi-step code interpretation (grounding/bonding configurations, AFCI/GFCI requirements, multiwire branch circuits) but fails on simpler table lookups. This is counterintuitive and suggests the model may be over-relying on learned patterns rather than careful step-by-step reasoning for basic questions.

2. **Self-Contradiction**: In baseline-001, the model states 25A then correctly notes that 240.4(D) limits to 20A. This shows the model has the correct knowledge but failed to apply it to the primary answer.

3. **Selective Application of Standards**: In inspection-001, the model acknowledges Table 220.55 exists but chooses to ignore it in favor of a "conservative" approach that is not actually code-compliant.

4. **Attention to Detail**: The conduit size error (inspection-007) demonstrates that the model may not be carefully parsing input specifications in technical questions.

### Recommendations:

1. **Table Lookup Verification**: Implement a verification step for basic table lookups to ensure correct column/row identification
2. **Question Parsing**: Enhance reading comprehension to catch specific numerical values and units in questions
3. **Code Methodology Training**: Reinforce that NEC load calculations must follow prescribed methods (e.g., Table 220.55 is mandatory, not optional)
4. **Consistency Checking**: Add a step to check if final answer aligns with supporting information (e.g., if you say 240.4(D) limits to 20A, why is your answer 25A?)

---

## Questions Not Asked

Two questions from the evaluation set were not asked to the model:

1. **inspection-002**: Panel clearance violations in garage (scored 0/10 as not applicable)
2. **inspection-007**: The conduit fill question was asked but with wrong conduit size in the model's response

---

## Overall Assessment

ChatGPT 5.1 (GPT-4.1) demonstrates **excellent overall performance** with a 94.6% score, correctly answering 24 out of 26 questions with perfect scores. The model shows particular strength in:

- Complex code interpretation and synthesis
- Thorough explanations with proper references
- Multi-step reasoning for grounding/bonding configurations
- Comprehensive coverage of GFCI/AFCI requirements

However, the three critical errors reveal concerning weaknesses:

1. **Basic table lookups** - The 12 AWG ampacity error is inexcusable for a professional-grade code assistant
2. **Reading comprehension** - Missing the conduit size specification indicates potential attention problems
3. **Code methodology** - Choosing "conservative" over code-compliant approaches undermines trust

These errors, while few in number, are in fundamental areas where even junior electricians should not fail. The model's strong performance on complex questions makes these basic errors particularly concerning, as users may trust the model's answers on simple questions without verification.

**Verdict:** Suitable for advanced code interpretation and conceptual questions, but **requires verification** for basic table lookups and load calculations. Users should not rely on this model for exam preparation or field work without independent verification of answers.
