# GPT-4o Wrong Answer Analysis

**Judge:** Claude Code (Claude Opus 4.5)
**Method:** LLM-as-Judge
**Overall Score:** 92.5% (259/280)

---

## Executive Summary

**Questions with Errors:** 6 of 28

**Key Error Pattern:** GPT-4o consistently confuses the 60°C vs 90°C columns in NEC temperature correction tables (Table 310.15(B)(1)). In core-010, it used the 60°C factor (0.71) for 90°C-rated THHN wire. In inspection-009, it used a higher factor (0.82) for 60°C-rated TW wire. This suggests systematic confusion about matching insulation temperature ratings to the correct table column.

**Most Critical Error:** inspection-007 (Conduit Fill) - GPT-4o used metric values (mm²) instead of imperial values (in²) from NEC Chapter 9 tables, resulting in an answer of 144 conductors instead of the correct 28-29. This 5x overestimate would be physically impossible and represents a dangerous misunderstanding.

**Strengths:** Excellent on conceptual questions, code interpretation, GFCI/AFCI requirements, grounding/bonding theory, and providing comprehensive explanations with proper NEC citations.

---

## Detailed Error Analysis (6 of 28)

---

### 1. core-010: THHN Temperature Correction (Score: 7/10)

**Question:** A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?

**GPT-4o's Answer:** 17.04A (rounded to 17A)

**Correct Answer:** 19.68A (approximately 20A)

**What GPT-4o Did Wrong:**
- Base ampacity: 30A at 90°C ✓ (correct)
- Bundling factor: 0.80 for 6 conductors ✓ (correct)
- **Temperature correction: Used 0.71** ✗ (WRONG)

**Root Cause:** GPT-4o looked up the temperature correction factor from the **60°C column** of Table 310.15(B)(1) instead of the **90°C column**. THHN is 90°C rated insulation, so the correct factor for 50°C ambient is **0.82**, not 0.71.

**Correct Calculation:**
- 30A × 0.82 × 0.80 = 19.68A ≈ 20A

**GPT-4o's Calculation:**
- 30A × 0.71 × 0.80 = 17.04A

---

### 2. inspection-001: Service Load Calculation (Score: 9/10)

**Question:** Calculate service load for 200A panel with 12kW range, 5.5kW dryer, AC, water heater, 3000 sq ft.

**GPT-4o's Answer:** 113.3A (27,200 VA)

**Expected Answer:** 103.2A (24,775 VA)

**What GPT-4o Did Wrong:**
GPT-4o's breakdown:
- General lighting (demand factored): 5,100 VA ✓
- Small appliance + laundry: 4,500 VA ✓
- Range (demand load): 8,000 VA ✓
- Dryer: 5,000 VA ✓
- HVAC: 4,600 VA ✓
- **Total: 27,200 VA**

Expected breakdown:
- General lighting (demand factored): 6,675 VA (included small appliance/laundry in demand calculation)
- Range: 8,000 VA
- Dryer: 5,500 VA (not 5,000 VA)
- AC: 4,600 VA
- **Total: 24,775 VA**

**Root Cause:** Minor differences in how demand factors were applied:
1. GPT-4o used 5,000 VA for dryer (NEC 220.54 standard) vs actual 5,500 VA rating
2. Different approach to combining general lighting with small appliance loads for demand factor application

**Note:** Both answers correctly conclude 200A is adequate. The variance is within acceptable bounds for NEC calculations which can vary by interpretation.

---

### 3. inspection-005: Kitchen Circuit Protection (Score: 9/10)

**Question:** Kitchen installation - specify protection for countertop receptacles, dishwasher, garbage disposal, refrigerator.

**GPT-4o's Answer:**
- Garbage disposal: GFCI + AFCI (Combination) required

**Expected Answer:**
- Garbage disposal: GFCI **not specifically required**, AFCI required

**What GPT-4o Did Wrong:**
GPT-4o stated GFCI is required for garbage disposal, citing 210.8(A)(6). However, the expected answer indicates GFCI is not specifically required for disposals.

**Root Cause:** This is actually a nuanced interpretation issue:
- NEC 210.8(A)(6) requires GFCI for "kitchens" but the disposal is typically hardwired, not a receptacle
- If cord-and-plug connected, GFCI would be required
- If hardwired, GFCI is not explicitly required by 210.8(A)(6)

GPT-4o took the more conservative (safer) interpretation.

---

### 4. inspection-007: Conduit Fill Calculation (Score: 4/10) - CRITICAL ERROR

**Question:** Maximum number of 10 AWG THHN conductors in 1¼-inch RMC?

**GPT-4o's Answer:** 144 conductors

**Correct Answer:** 28-29 conductors

**What GPT-4o Did Wrong:**
GPT-4o used **metric (mm²) values** from Chapter 9 tables instead of **imperial (in²) values**:

| Value | GPT-4o Used (mm²) | Correct (in²) |
|-------|-------------------|---------------|
| 1¼" RMC 40% fill area | 526 mm² | 0.610 in² |
| 10 AWG THHN area | 3.63 mm² | 0.0211 in² |

**GPT-4o's Calculation:**
- 526 mm² ÷ 3.63 mm² = 144.9 → 144 conductors

**Correct Calculation:**
- 0.610 in² ÷ 0.0211 in² = 28.91 → 29 conductors (or 28 conservative)

**Root Cause:** GPT-4o retrieved values from the metric columns of NEC Chapter 9 Tables 4 and 5 instead of the imperial columns. This resulted in a **5x overestimate** (144 vs 29).

**Impact:** This is a dangerous error. Installing 144 conductors in a 1¼" conduit would be:
- Physically impossible
- A massive code violation
- A serious fire hazard if attempted

---

### 5. inspection-009: TW Conductor Derating (Score: 7/10)

**Question:** Six 12 AWG TW (60°C rated) conductors in attic at 110°F (43°C). Calculate adjusted ampacity.

**GPT-4o's Answer:** 13.12A (rounded to 13A)

**Correct Answer:** 11.36A (approximately 11.4A)

**What GPT-4o Did Wrong:**
- Base ampacity: 20A at 60°C ✓ (correct)
- Bundling factor: 0.80 for 6 conductors ✓ (correct)
- **Temperature correction: Used 0.82** ✗ (WRONG)

**Root Cause:** GPT-4o used the wrong temperature correction factor. For **60°C insulation (TW)** at 43°C ambient, the correct factor from Table 310.15(B)(1) is **0.71**, not 0.82.

Interestingly, this is the **opposite error** from core-010:
- In core-010 (THHN 90°C), GPT-4o used the 60°C column factor (0.71) instead of 90°C (0.82)
- In inspection-009 (TW 60°C), GPT-4o used 0.82 instead of 0.71

**Correct Calculation:**
- 20A × 0.71 × 0.80 = 11.36A

**GPT-4o's Calculation:**
- 20A × 0.82 × 0.80 = 13.12A

---

### 6. inspection-010: GEC Sizing (Score: 9/10)

**Question:** GEC size for service with 4 × 250 kcmil copper per phase (1000 kcmil equivalent)?

**GPT-4o's Answer:** 3/0 AWG copper

**Correct Answer:** 2/0 AWG copper

**What GPT-4o Did Wrong:**
GPT-4o stated "Over 600 kcmil copper" requires 3/0 AWG GEC.

Per Table 250.66, the row for "Over 600 through 1100 kcmil" copper service conductors requires **2/0 AWG copper** GEC, not 3/0.

**Root Cause:** GPT-4o may have:
1. Misread Table 250.66
2. Used the aluminum column instead of copper
3. Rounded up conservatively (though 2/0 is the code minimum)

**Impact:** One wire size oversized is conservative (not a safety issue), but represents unnecessary material cost and may not fit in some electrode connections.

---

## Error Pattern Summary

| Error Type | Questions | Pattern |
|------------|-----------|---------|
| Temperature correction factor confusion | core-010, inspection-009 | Mixing up 60°C vs 90°C columns |
| Unit confusion (metric vs imperial) | inspection-007 | Used mm² instead of in² |
| Table lookup errors | inspection-010 | One row off in Table 250.66 |
| Demand calculation variance | inspection-001 | Minor interpretation differences |
| Conservative interpretation | inspection-005 | Erred on side of more protection |

## Recommendations for GPT-4o Users

1. **Always verify NEC table lookups** - especially temperature correction factors
2. **Check units** - NEC tables have both metric and imperial columns
3. **Double-check conduit fill calculations** - errors can be orders of magnitude off
4. **For calculations involving insulation ratings**, verify you're using the column that matches the insulation temperature rating (60°C, 75°C, or 90°C)
