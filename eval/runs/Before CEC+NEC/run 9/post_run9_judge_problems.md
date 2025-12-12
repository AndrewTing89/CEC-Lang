# Post-Run 9 Deep Dive: Agent Evaluation Issues

**Date:** 2025-12-07
**Evaluation Run:** Run 9
**Analyst:** Claude Code

---

## Executive Summary

Despite achieving 100% "PASS" status on both CEC (30/30) and Core (28/28) question sets, detailed analysis reveals **significant accuracy and safety issues** in the agent's responses. This report documents 7 distinct problems identified through deep-dive investigation of the underlying data, tools, and agent behavior.

### Key Finding
**The table data is CORRECT in all cases.** Problems stem from:
- Missing dedicated lookup functions
- Bugs in existing lookup logic
- Stale content in semantic search index
- LLM misinterpretation and hallucination

### Issue Summary

| Issue | Question | Expected | Agent Answer | Root Cause | Severity |
|-------|----------|----------|--------------|------------|----------|
| Office Lighting | cec-018 | 1.3 VA/ft² | 3.5 VA/ft² | RAG returns stale data | Medium |
| Flexible Cord | cec-019 | 25A | 20A | Missing lookup function | Medium |
| Motor Control OCP | cec-024 | 10A | 20A | Missing lookup + wrong tool | Medium |
| GFCI Comparison | cec-026 | CEC permissive | CEC restrictive | Section conflation | Low |
| Subpanel Bonding | core-007 | Separate N/G | Bond N/G | **HALLUCINATION** | **CRITICAL** |
| THHN Ampacity | core-010 | 19.68A | 15.0A | Function default bug | Medium |
| GEC Sizing | inspection-010 | 2/0 AWG | 350 kcmil | Range matching bug | Medium |

---

## Detailed Investigation Results

---

### Issue 1: CEC-018 — Office Lighting Load

**Question:** "What is the general lighting load in VA per square foot for office buildings according to California code?"

| Aspect | Value |
|--------|-------|
| **Expected Answer** | 1.3 VA/ft² per CEC 2022 Table 220.12 |
| **Agent Answer** | 3.5 VA/ft² |
| **Data in JSON** | ✅ CORRECT: 1.3 VA/ft² |

#### Investigation Findings

**File:** `data/CEC_2022/cec_tables_unified.json`

```json
{
  "type_of_occupancy": "Office",
  "volt_amperes_per_m2": 14,
  "volt_amperes_per_ft2": 1.3,
  "footnote": "d"
}
```

The JSON table data is **correct and current** (1.3 VA/ft²).

#### Root Cause: RAG/Search Inconsistency

The agent used `cec_search` (semantic search) instead of `cec_lookup_table` (direct table access):

- **`cec_search`** queries `cec_chunks.jsonl` which contains outdated NEC 2020 values (3.5 VA/ft²)
- **`cec_lookup_table`** queries `cec_tables_unified.json` which has correct CEC 2022 values (1.3 VA/ft²)

**Evidence:** In cec-023 (commercial load calculation), the agent used `cec_lookup_table` and correctly calculated with 1.3 VA/ft². The inconsistency is due to tool selection, not data.

#### Recommended Fix

1. Update `cec_chunks.jsonl` with current CEC 2022 Table 220.12 values
2. Re-index the OpenSearch database
3. Add tool routing logic to prefer direct table lookups for questions about table values

---

### Issue 2: CEC-019 — Flexible Cord Ampacity

**Question:** "What is the ampacity of a 12 AWG flexible cord (Column B thermoset) according to California code?"

| Aspect | Value |
|--------|-------|
| **Expected Answer** | 25 amperes per Table 400.5(A)(1) |
| **Agent Answer** | 20 amperes |
| **Data in JSON** | ✅ CORRECT: 25A for Column B |

#### Investigation Findings

**File:** `data/CEC_2022/cec_tables_unified.json` (lines 16102-16106)

```json
{
  "size_awg": "12",
  "thermoset_tst": null,
  "column_a": 20,
  "column_b": 25,
  "types_hpd": 30
}
```

The data is correct:
- Column A (3-conductor): 20A
- Column B (2-conductor thermoset): **25A** ✓
- Types HPD: 30A

#### Root Cause: Missing Dedicated Lookup Function

**No `cec_lookup_flexible_cord_ampacity()` function exists** in `cec_table_tools.py`.

The agent used `cec_search`, which returned Table 400.5(A)(1) as unstructured text. The LLM then extracted the wrong column value (Column A: 20A instead of Column B: 25A).

#### Recommended Fix

Implement dedicated lookup function:

```python
def cec_lookup_flexible_cord_ampacity(
    self,
    conductor_size: str,
    column: str = "B",  # A, B, or HPD
    insulation_type: str = "thermoset"
) -> Dict[str, Any]:
    """
    Look up flexible cord ampacity from CEC Table 400.5(A)(1).
    Column A: 3+ conductors
    Column B: 2 conductors (thermoset)
    Types HPD: Heater cord types
    """
```

---

### Issue 3: CEC-024 — Motor Control Circuit OCP

**Question:** "What is the maximum overcurrent protection for a motor control circuit using 16 AWG copper conductors that extend beyond the enclosure in California?"

| Aspect | Value |
|--------|-------|
| **Expected Answer** | 10 amperes per Table 430.72(B) Column C |
| **Agent Answer** | 20 amperes (from 240.4(D)) |
| **Data in JSON** | ✅ CORRECT: 10A for Column C |

#### Investigation Findings

**File:** `data/CEC_2022/cec_tables_unified.json` (lines 26538-26659)

```json
{
  "conductor_size": "16",
  "column_a_copper": 10,
  "column_b_copper": 40,
  "column_c_copper": 10
}
```

Table 430.72(B) column definitions:
- Column A: Separate protection provided → 10A
- Column B: Conductors within enclosure → 40A
- Column C: **Conductors extend beyond enclosure** → **10A** ✓

#### Root Cause: Missing Tool + Wrong Tool Selection

**Problem 1:** No `cec_lookup_motor_control_ocp()` function exists.

**Problem 2:** Agent applied general overcurrent rules (240.4(D) → 20A for 16 AWG) instead of the specific Table 430.72(B).

The question explicitly stated "extending beyond the enclosure" which maps to Column C, but the agent didn't recognize this as a Table 430.72(B) lookup.

#### Recommended Fix

1. Implement dedicated lookup function:
```python
def cec_lookup_motor_control_ocp(
    self,
    conductor_size: str,
    installation_config: str  # "separate", "within_enclosure", "beyond_enclosure"
) -> Dict[str, Any]:
    """Look up motor control circuit OCP from CEC Table 430.72(B)."""
```

2. Add system prompt guidance to prefer specific tables (430.72(B)) over general rules (240.4(D)) for motor control circuits.

---

### Issue 4: CEC-026 — Kitchen GFCI Comparison

**Question:** "Compare the kitchen GFCI requirements between CEC 2022 and NEC 2023. Which code is more restrictive?"

| Aspect | Value |
|--------|-------|
| **Expected Answer** | CEC 2022 is MORE PERMISSIVE |
| **Agent Answer** | CEC 2022 is more RESTRICTIVE |
| **Knowledge Base** | ✅ CORRECT content |

#### Investigation Findings

The knowledge base contains correct content for both codes:

**CEC 210.8(A)(6):** "Kitchens — where the receptacles are installed to serve the **countertop surfaces**"

**NEC 210.8(A)(5):** "Kitchens" (no qualifier — ALL receptacles)

The key difference: CEC limits GFCI to countertop receptacles; NEC requires GFCI for ALL kitchen receptacles (including refrigerator, built-in microwave, etc.).

#### Root Cause: Section Conflation

The agent conflated two different sections:
- **210.8** (GFCI protection requirements)
- **210.52** (Receptacle spacing/placement requirements)

Both sections mention "kitchen, pantry, breakfast room, dining room" so the search returned both. The agent then mixed:
- 210.52(C)(2)(a): "1 receptacle per 9 sq ft" (spacing rule)
- 210.8(A)(6): "countertop surfaces" (GFCI rule)

#### Recommended Fix

Add system prompt guidance to explicitly distinguish:
- Section 210.8 = Protection requirements (GFCI/AFCI)
- Section 210.52 = Location/spacing requirements

---

### Issue 5: CORE-007 — Subpanel Bonding ⚠️ **SAFETY CRITICAL**

**Question:** "A detached garage is fed from the house panel with a 4-wire feeder. How should the grounding and bonding be configured in the garage subpanel?"

| Aspect | Value |
|--------|-------|
| **Expected Answer** | Neutral and ground must be **SEPARATED** |
| **Agent Answer** | "**Bond** the neutral and ground bars in the subpanel" |
| **Knowledge Base** | ✅ CORRECT — prohibits bonding |

#### ⚠️ THIS IS DANGEROUS MISINFORMATION ⚠️

The agent's advice would create:
- Ground loop hazards
- Improper fault clearing
- Potential shock hazards
- Code violations (automatic inspection failure)

#### Investigation Findings

**The knowledge base is CORRECT.**

CEC 250.32(B)(1) explicitly states:
> "Any installed grounded conductor **shall not be connected** to the equipment grounding conductor or to the grounding electrode(s)."

CEC 250.24(A)(5) states:
> "A grounded conductor shall not be connected to normally non-current-carrying metal parts of equipment... on the load side of the service disconnecting means."

CEC 408.40 states:
> "Equipment grounding conductors shall not be connected to a terminal bar provided for grounded conductors... unless... interconnection... is permitted or required by Article 250."

#### Root Cause: Pure Hallucination

This is a **pure hallucination**. The agent:
1. Correctly cited section 250.32(B)(1)
2. Then stated the **OPPOSITE** of what it says
3. Confused service equipment bonding (required) with subpanel bonding (prohibited)

The search tools returned correct content, but the LLM fabricated an answer that contradicts the source material.

#### Recommended Fix (HIGH PRIORITY)

1. **Add explicit system prompt guidance:**
```
CRITICAL GROUNDING RULES:
- SERVICE EQUIPMENT: Bond neutral to ground (main bonding jumper required)
- SUBPANELS/FEEDERS: Separate neutral from ground (NO bonding jumper)
- 4-wire feeders: Neutral isolated, ground bonded to enclosure
```

2. **Add validation layer** for safety-critical topics (grounding, bonding, fault protection)

3. **Consider hardcoded rules** for common dangerous misconfigurations

---

### Issue 6: CORE-010 — THHN Ampacity Calculation

**Question:** "A panel has six 12 AWG THHN current-carrying conductors in a single conduit in a 50°C ambient temperature location. What is the adjusted ampacity?"

| Aspect | Value |
|--------|-------|
| **Expected Calculation** | 30A × 0.82 × 0.80 = 19.68A |
| **Agent Calculation** | 25A × 0.75 × 0.80 = 15.0A |
| **Data in JSON** | ✅ CORRECT for both values |

#### Investigation Findings

**Table 310.16 Data (correct):**
- 12 AWG at 75°C: 25A
- 12 AWG at 90°C: 30A

**Table 310.15(B)(1) Data (correct):**
- 50°C ambient, 75°C conductor: 0.75
- 50°C ambient, 90°C conductor: 0.82

THHN is a **90°C rated conductor**, so the correct calculation uses:
- Base: 30A (90°C column)
- Temp correction: 0.82 (90°C at 50°C)
- Bundling: 0.80 (6 conductors)
- Result: 30 × 0.82 × 0.80 = **19.68A**

#### Root Cause: Function Default Bug

**File:** `core/cec_table_tools.py` (line 160)

```python
def lookup_conductor_ampacity(self, conductor_size: str,
                             temperature_rating: str = "75°C",  # ← PROBLEM
                             conductor_type: str = "copper") -> Dict[str, Any]:
```

The function:
1. **Defaults to 75°C** instead of requiring explicit temperature rating
2. **Has no insulation_type parameter** to auto-detect that THHN = 90°C
3. Returns wrong ampacity when agent doesn't explicitly specify "90°C"

#### Recommended Fix

Option A — Add insulation type parameter:
```python
def lookup_conductor_ampacity(
    self,
    conductor_size: str,
    insulation_type: str = None,  # THHN, TW, XHHW, etc.
    temperature_rating: str = None,  # Only if insulation_type not provided
    conductor_type: str = "copper"
) -> Dict[str, Any]:
    # Map insulation types to temperature ratings
    INSULATION_TEMP_MAP = {
        "THHN": "90°C", "THWN-2": "90°C", "XHHW-2": "90°C",
        "TW": "60°C", "THW": "75°C", "THWN": "75°C"
    }
```

Option B — Remove default, require explicit:
```python
def lookup_conductor_ampacity(
    self,
    conductor_size: str,
    temperature_rating: str,  # Required, no default
    conductor_type: str = "copper"
) -> Dict[str, Any]:
```

---

### Issue 7: INSPECTION-010 — GEC Sizing

**Question:** "A commercial data center has a main service with four parallel sets of 250 kcmil copper conductors per phase (total equivalent: 1000 kcmil per phase). Using NEC Table 250.66, determine the minimum size copper grounding electrode conductor (GEC) required."

| Aspect | Value |
|--------|-------|
| **Expected Answer** | 2/0 AWG copper |
| **Agent Answer** | 350 kcmil copper |
| **Data in JSON** | ✅ CORRECT: 2/0 AWG |

#### Investigation Findings

**File:** `data/CEC_2022/cec_tables_unified.json`

Table 250.66 row for 1000 kcmil:
```json
{
  "largest_conductor_copper": "Over 600 through 1100",
  "largest_conductor_aluminum": "Over 900 through 1750",
  "grounding_conductor_copper": "2/0",
  "grounding_conductor_aluminum": "4/0"
}
```

The data is correct: 1000 kcmil falls in "Over 600 through 1100" → GEC is **2/0 AWG copper**.

#### Root Cause: Range Matching Bug

**File:** `core/cec_table_tools.py` — `lookup_gec_size()` function

The function uses substring matching:
```python
if size_normalized in row_value or row_value == size_normalized:
```

But row values are ranges like "Over 600 through 1100". The string "1000" doesn't substring-match this range string, so the matching fails.

**The fix already exists:** The codebase has `parse_range_value()` utility which correctly handles ranges. It's used in `lookup_temperature_correction()` and `lookup_bundling_adjustment()` but NOT in `lookup_gec_size()`.

#### Recommended Fix

Update `lookup_gec_size()` to use existing range matching utility:

```python
# CURRENT (broken):
if size_normalized in row_value or row_value == size_normalized:

# FIXED:
from core.nec_table_tools import parse_range_value
matches, _ = parse_range_value(row_value, int(size_normalized))
if matches:
    # Return the GEC size
```

---

## Root Cause Categories

### Category 1: Missing Dedicated Lookup Functions

| Issue | Missing Function | Table |
|-------|-----------------|-------|
| cec-019 | `lookup_flexible_cord_ampacity()` | 400.5(A)(1) |
| cec-024 | `lookup_motor_control_ocp()` | 430.72(B) |

**Pattern:** JSON data exists and is correct, but no structured lookup was implemented. Agent falls back to semantic search, which returns unstructured text that the LLM misinterprets.

### Category 2: Lookup Function Bugs

| Issue | Function | Bug |
|-------|----------|-----|
| core-010 | `lookup_conductor_ampacity()` | Wrong default (75°C) |
| inspection-010 | `lookup_gec_size()` | Substring instead of range matching |

**Pattern:** Functions exist but have implementation flaws.

### Category 3: RAG/Search Inconsistency

| Issue | Problem |
|-------|---------|
| cec-018 | `cec_chunks.jsonl` contains outdated values |

**Pattern:** Direct table lookups work; semantic search returns stale content.

### Category 4: LLM Interpretation Errors

| Issue | Error Type |
|-------|------------|
| cec-026 | Conflated similar sections (210.8 vs 210.52) |
| core-007 | **HALLUCINATED** opposite of correct rule |

**Pattern:** Content is correct, but LLM misinterprets or fabricates information.

---

## Recommended Priority Order for Fixes

### 🔴 HIGH PRIORITY (Safety-Critical)

1. **core-007: Subpanel Bonding Hallucination**
   - Add explicit system prompt rules for service vs. subpanel grounding
   - Add validation layer for grounding/bonding topics
   - Consider hardcoded safety rules

### 🟡 MEDIUM PRIORITY (Accuracy)

2. **inspection-010: GEC Sizing**
   - Fix `lookup_gec_size()` to use `parse_range_value()`
   - ~10 lines of code change

3. **core-010: THHN Ampacity**
   - Add insulation_type parameter to `lookup_conductor_ampacity()`
   - Or remove dangerous 75°C default

4. **cec-019: Flexible Cord Ampacity**
   - Implement `cec_lookup_flexible_cord_ampacity()` function
   - Register in tools.py

5. **cec-024: Motor Control OCP**
   - Implement `cec_lookup_motor_control_ocp()` function
   - Add system prompt guidance for specific vs. general rules

### 🟢 LOWER PRIORITY (Consistency)

6. **cec-018: Office Lighting Load**
   - Update `cec_chunks.jsonl` with current Table 220.12 values
   - Re-index OpenSearch

7. **cec-026: GFCI Comparison**
   - Add system prompt guidance distinguishing 210.8 from 210.52

---

## Files Requiring Changes

| File | Changes Needed |
|------|----------------|
| `core/cec_table_tools.py` | Fix `lookup_gec_size()`, fix `lookup_conductor_ampacity()`, add new lookup functions |
| `core/tools.py` | Register new lookup functions |
| `core/agent.py` | Add safety-critical guidance to system prompt |
| `data/CEC_2022/cec_chunks.jsonl` | Update Table 220.12 values |

---

## Conclusion

The CEC Lang agent's underlying data is accurate, but tool implementation gaps and LLM interpretation errors cause significant accuracy issues. Most critically, the subpanel bonding hallucination (core-007) represents a **safety hazard** that should be addressed immediately.

The evaluation system's 100% PASS rate is misleading — it validates that the agent responded, not that the response was correct. A more rigorous evaluation framework with answer validation would catch these issues.
