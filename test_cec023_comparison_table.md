# CEC-023 Response Comparison: What Each Run Said About the Refrigerator Circuit

## The Critical Test: Does the Agent Require AFCI for ALL Kitchen Circuits?

| Run | Pass/Fail | Refrigerator Protection Statement | Why It Failed/Passed |
|-----|-----------|-----------------------------------|---------------------|
| **1** | ❌ FAIL | "**Protection Required**: **CAFCI**<br>**Code Basis**: CAFCI: CEC 2022 **210.12(A)** applies.<br>**GFCI Exemption**: Refrigerators are not listed in 210.8 exceptions" | States "GFCI Exemption: **Refrigerators are not listed**" - the phrase triggers "not required" detection |
| **2** | ✅ PASS | "**Protection Required**: **AFCI Only**<br>**AFCI**: CEC 2022 Section 210.12(A) (universal AFCI requirement).<br>**GFCI Exemption**: No exception for refrigerators in CEC 2022" | Clear, direct statement with no "not required" language |
| **3** | ❌ FAIL | "**Protection Required**: **AFCI**<br>**GFCI**: **Not required** (no exception in 210.8 applies to refrigerators).<br>**AFCI**: CEC 210.12(A) requires AFCI" | Uses "**Not required**" for GFCI |
| **4** | ❌ FAIL | "**Protection Required**: **AFCI**<br>**AFCI**: CEC 2022 **210.12(A)** applies.<br>**GFCI**: Not required (no exception in code for refrigerators)" | Uses "Not required" for GFCI |
| **5** | ❌ FAIL | "**Protection:** **Standard breaker**<br>**AFCI:** CEC 210.12(B) exception applies to refrigerators on dedicated circuits<br>**GFCI:** Not required for hardwired appliances" | **MAJOR ERROR**: Claims false AFCI exception exists! Says "Standard breaker" only. This is factually wrong. |
| **6** | ❌ FAIL | "**Protection Required**: **AFCI Breaker Only**<br>**GFCI**: **Not required** (no explicit mandate for refrigerators in CEC 2022).<br>**AFCI**: CEC 2022 **210.12(A)**" | Uses "**Not required**" for GFCI |
| **7** | ❌ FAIL | "**Protection Required**: **AFCI only**<br>**GFCI**: **Not required**. Refrigerators are fixed appliances...<br>**AFCI**: CEC 210.12(A) applies" | Uses "**Not required**" for GFCI |

## Pattern Analysis

### What the Agent Got RIGHT (7/7 runs):
- ✅ Mentions AFCI requirement for refrigerator in **ALL** runs
- ✅ Cites CEC 210.12(A) correctly in 6/7 runs
- ✅ Understands the concept of universal AFCI requirement

### What the Agent Got WRONG:

#### Pattern 1: "Not Required" Language (Runs 1, 3, 4, 6, 7)
**Frequency**: 5 out of 7 runs (71%)

The agent correctly identifies AFCI requirement but then discusses GFCI exemptions using phrases like:
- "GFCI: Not required"
- "GFCI Exemption: Refrigerators are not listed"

**Why This Fails**: The test keyword search for "not required" catches these GFCI exemption discussions and incorrectly interprets them as saying protection is "not required" for the circuit.

**Verdict**: This is a **test design issue**, not necessarily an agent error. The agent is being technically accurate by explaining that GFCI is not required while AFCI is required.

---

#### Pattern 2: Hallucinated Exception (Run 5)
**Frequency**: 1 out of 7 runs (14%)

The agent incorrectly states:
> "**AFCI:** CEC 210.12(B) exception applies to refrigerators on dedicated circuits"

**Why This is Wrong**:
- CEC 2022 Section 210.12(B) does NOT provide an exception for refrigerators
- 210.12(A) mandates AFCI for ALL 120V, 15/20A dwelling circuits with no appliance exceptions
- This is a factual hallucination

**Verdict**: This is a **serious agent error** that represents a gap in code knowledge.

---

## Comparison: The ONE Correct Answer vs. Typical Wrong Answers

### ✅ Run 2 (CORRECT) - What Success Looks Like:
```
4. Refrigerator (Dedicated 20A Circuit)
- Protection Required: AFCI Only
- Citations:
  - AFCI: CEC 2022 Section 210.12(A) (universal AFCI requirement).
  - GFCI Exemption: No exception for refrigerators in CEC 2022 (unlike some NEC versions).
```

**Why This Passed**:
- Clear, unambiguous statement: "AFCI Only"
- Uses "Exemption" rather than "Not required" for GFCI
- Adds context about NEC differences without triggering keywords

---

### ❌ Run 3 (TYPICAL FAIL) - Common Pattern:
```
4. Refrigerator (20A Dedicated Circuit)
- Protection Required: AFCI
- Code Basis:
  - GFCI: Not required (no exception in 210.8 applies to refrigerators).
  - AFCI: CEC 210.12(A) requires AFCI for all 120V dwelling circuits.
```

**Why This Failed**:
- Uses "Not required" when discussing GFCI
- Technically accurate but triggers false positive in test

---

### ❌ Run 5 (CATASTROPHIC FAIL) - Hallucination:
```
4. Refrigerator (20A dedicated circuit):
- Protection: Standard breaker
- Source:
  - AFCI: CEC 210.12(B) exception applies to refrigerators on dedicated circuits (not general-purpose receptacles).
  - GFCI: Not required for hardwired appliances
```

**Why This is Dangerous**:
- Claims a code exception that **doesn't exist**
- Would result in failed inspection if followed
- Represents fundamental misunderstanding of 210.12(A) scope

---

## The Real Test: Semantic Understanding

Let's re-evaluate based on **semantic correctness** rather than keyword matching:

| Run | Keyword Test | Semantic Test | True Answer Quality |
|-----|--------------|---------------|---------------------|
| 1 | ❌ FAIL | ✅ PASS | Correct code requirements, awkward phrasing |
| 2 | ✅ PASS | ✅ PASS | Perfect answer |
| 3 | ❌ FAIL | ✅ PASS | Correct code requirements, explicit GFCI exemption |
| 4 | ❌ FAIL | ✅ PASS | Correct code requirements, explicit GFCI exemption |
| 5 | ❌ FAIL | ❌ FAIL | **WRONG** - claims false exception |
| 6 | ❌ FAIL | ✅ PASS | Correct code requirements, explicit GFCI exemption |
| 7 | ❌ FAIL | ✅ PASS | Correct code requirements, explicit GFCI exemption |

### Revised Accuracy:
- **Keyword-based Test**: 1/7 correct (14.3%)
- **Semantic Test**: 6/7 correct (85.7%)
- **Critical Errors**: 1/7 runs (14.3%) had a dangerous hallucination

## Conclusion

The agent has **85.7% semantic accuracy** but only **14.3% keyword accuracy** because:

1. **The test is too strict**: It fails answers that correctly require AFCI but mention "GFCI not required"
2. **Phrasing variation**: The agent uses different ways to express the same correct information
3. **One critical error**: Run 5's hallucinated exception is the real problem that needs fixing

**Recommended Action**: Fix the hallucination issue (likely related to 210.12(B) confusion) and create a smarter semantic test that understands:
- "AFCI required, GFCI not required" = CORRECT
- "Standard breaker only" = WRONG
- "AFCI exception exists" = WRONG
