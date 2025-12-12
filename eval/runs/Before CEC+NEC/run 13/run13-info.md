# Run 13 - Agent Improvement Implementation

**Date:** 2025-12-09
**Baseline:** Run 12 (96.6% pass rate, 9.1/10 average)
**Goal:** Fix 2 FAILs (core-010, cec-020) and improve 12 partial-credit questions

---

## Changes Implemented

### Solution 1: Unified Ampacity Decision Tree Tool

**Problem:** Agent had to make 3-4 separate tool calls + manual math for ampacity calculations, causing errors.

**Implementation:**
- Added `calculate_derated_ampacity()` method to `CECTableTools` class
- Added `cec_derated_ampacity` tool wrapper
- Automatically chains: insulation type -> temp rating -> base ampacity -> corrections

**Files Modified:**
- `core/cec_table_tools.py` - New method
- `core/tools.py` - Tool registration

**Expected Impact:** Fix core-010, cec-021 errors

---

### Solution 3A: Enhanced Table Returns with Adjacent Values

**Problem:** Agent misread table values without sanity checking

**Implementation:**
- Modified `lookup_conductor_ampacity()` to include adjacent row values
- Returns `smaller_size` and `larger_size` with their ampacities for verification

**Files Modified:**
- `core/cec_table_tools.py` - Enhanced return structure

**Expected Impact:** Better verification of table lookups

---

### Solution 3B: Routing Guidance for Numeric Table Answers

**Problem:** Agent searched and calculated instead of using lookup tools

**Implementation:**
- Added "NUMERIC ANSWERS FROM TABLES" section to system prompt
- Lists which tool to use for each type of numeric answer
- Explicit instruction: "NEVER calculate or estimate table values"

**Files Modified:**
- `core/agent.py` - System prompt update

**Expected Impact:** Fix cec-020 type errors

---

### Solution 5A: Rule Hierarchy System Prompt

**Problem:** Agent conflated base rules, limiting rules, and exceptions

**Implementation:**
- Added comprehensive "RULE HIERARCHY (MANDATORY)" section to system prompt
- Defines 4 levels: Base Rules -> Adjustment Rules -> Limiting Rules -> Exceptions
- Includes application flow and cross-reference guidance

**Files Modified:**
- `core/agent.py` - System prompt update

**Expected Impact:** Fix core-010, inspection-010 (12 AWG OCP limit issues)

---

### Solution 5B: Find Limiting Rules Tool

**Problem:** Agent didn't check for rules that constrain base rule application (e.g., 240.4(D))

**Implementation:**
- Added `find_limiting_rules()` method to `CECKnowledgeTools` class
- Added `cec_find_limiting_rules` tool wrapper
- Uses mapping + semantic search approach:
  - Known mappings (e.g., Table 310.16 + 12 AWG -> 240.4(D))
  - Semantic search for "shall not exceed", "maximum", "limited to"

**Files Modified:**
- `core/cec_knowledge_tools.py` - New method
- `core/tools.py` - Tool registration
- `core/agent.py` - Tool reference in prompt

**Expected Impact:** Proper application of limiting rules like 240.4(D)

---

### Solution 2: Fix Default Search Limits

**Problem:** Default limit=5 was too low; compare_with_nec was hardcoded to limit=3

**Implementation:**
- Changed default `limit` from 5 to 10 in:
  - `hybrid_search()` in opensearch_hybrid_client.py
  - `exception_search()` in opensearch_hybrid_client.py
- Made `compare_with_nec()` limit configurable (default 5, was hardcoded 3)

**Files Modified:**
- `core/opensearch_hybrid_client.py` - Default limits
- `core/tools.py` - compare_with_nec parameter

**Expected Impact:** Better completeness for enumeration questions (baseline-003, core-003, cec-017)

---

## Files Modified Summary

| File | Changes |
|------|---------|
| `core/agent.py` | Rule Hierarchy prompt, Numeric Table routing, Tool references |
| `core/tools.py` | 2 new tools (cec_derated_ampacity, cec_find_limiting_rules), compare_with_nec fix |
| `core/cec_table_tools.py` | calculate_derated_ampacity(), adjacent values in lookup |
| `core/cec_knowledge_tools.py` | find_limiting_rules() method |
| `core/opensearch_hybrid_client.py` | Default limits 5->10 |

---

## Tool Count

**Total tools:** 23 (was 21)

**New tools added:**
1. `cec_derated_ampacity` - Complete ampacity calculation with all derating factors
2. `cec_find_limiting_rules` - Find constraining/overriding rules

---

## Expected Results

| Metric | Run 12 | Expected Run 13 |
|--------|--------|-----------------|
| Pass Rate | 96.6% | ~98-100% |
| Average Score | 9.1/10 | ~9.5/10 |
| FAILs | 2 | 0 |

**Key questions expected to improve:**
- core-010 (ampacity derating) - was FAIL
- cec-020 (table lookup) - was FAIL
- inspection-010 (GEC sizing)
- baseline-003, core-003, cec-017 (enumeration completeness)
