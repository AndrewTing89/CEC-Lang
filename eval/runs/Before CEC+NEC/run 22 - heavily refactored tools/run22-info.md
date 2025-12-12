# Run 22 - Tool Refactoring

## Summary
Major tool audit and refactoring to improve LLM tool selection. Root cause analysis showed the LLM was using generic tools (`nec_lookup_table`) when specialized tools existed (`nec_lookup_conduit_fill`), causing wrong answers.

**Previous Run:** Run 21 (CEC: 95.0%, Core: 90.7%)

---

## Changes Since Run 21

### 1. Removed 2 Redundant Tools

| Tool Removed | Reason |
|--------------|--------|
| `get_table_info` | Redundant with `cec_lookup_table`/`nec_lookup_table` |
| `search_tables` | Used only 1x in 28 Core questions; `cec_search` covers this |

**Tool count:** 24 -> 22

### 2. Renamed 5 NEC Tools (Consistency)

Added `nec_` prefix to match CEC tool naming convention:

| Old Name | New Name |
|----------|----------|
| `lookup_conductor_ampacity` | `nec_lookup_conductor_ampacity` |
| `lookup_ampacity_adjustment` | `nec_lookup_ampacity_adjustment` |
| `lookup_grounding_conductor` | `nec_lookup_grounding_conductor` |
| `lookup_working_space` | `nec_lookup_working_space` |
| `lookup_conduit_fill` | `nec_lookup_conduit_fill` |

**Why:** Makes CEC vs NEC distinction obvious. LLM sees `cec_*` for California, `nec_*` for national.

### 3. Updated All 22 Tool Descriptions

Applied "USE THIS WHEN / DO NOT USE" pattern per OpenAI/Anthropic best practices.

#### Critical Fixes (targeting specific failures):

**`nec_lookup_conduit_fill`** (fixes inspection-007):
```
USE THIS TOOL WHEN:
- Question asks "how many conductors can fit in..."
- Question asks "maximum number of conductors..."
- Need conduit fill calculation per NEC
- Question mentions Chapter 9 Table 4 or Table 5

DO NOT use nec_lookup_table("4") - use THIS tool instead.
```

**`nec_lookup_ampacity_adjustment`** (fixes inspection-009):
```
USE THIS TOOL WHEN:
- Question asks about adjusted/derated ampacity per NEC
- Ambient temperature is NOT 30C (86F)
- More than 3 current-carrying conductors in raceway

IMPORTANT: After calling nec_lookup_conductor_ampacity for base ampacity,
you MUST call this tool for EACH adjustment factor needed.
DO NOT estimate or hallucinate factors - always look them up.
```

**`nec_lookup_table` / `cec_lookup_table`** (generic fallbacks):
```
WARNING: Use specialized tools when available:
- Conductor ampacity (310.16) -> use nec_lookup_conductor_ampacity
- Ampacity adjustment -> use nec_lookup_ampacity_adjustment
- Grounding (250.66/250.122) -> use nec_lookup_grounding_conductor
- Working space (110.26) -> use nec_lookup_working_space
- Conduit fill (Chapter 9) -> use nec_lookup_conduit_fill

Only use this tool for tables WITHOUT a specialized lookup function.
```

### 4. Updated agent.py References

- **SYSTEM_PROMPT (line 255):** `lookup_conductor_ampacity` -> `nec_lookup_conductor_ampacity`
- **search_tools list (lines 648-657):** Updated all renamed tools, added conduit_fill tools, removed deleted tools

---

## Final Tool List (22 tools)

### Search Tools (4)
- `cec_search` - Search CEC prose/rules
- `nec_search` - Search NEC prose/rules
- `cec_exception_search` - Find CEC exceptions
- `nec_exception_search` - Find NEC exceptions

### CEC Table Lookups (8)
- `cec_lookup_conductor_ampacity` - Base ampacity from 310.16
- `cec_lookup_conductor_size` - Reverse lookup (amps -> size)
- `cec_lookup_ampacity_adjustment` - Temp/bundling factors
- `cec_derated_ampacity` - All-in-one ampacity calculation
- `cec_lookup_grounding_conductor` - EGC/GEC sizing
- `cec_lookup_working_space` - Working clearances
- `cec_lookup_conduit_fill` - Conduit fill calculations
- `cec_lookup_table` - Generic fallback

### NEC Table Lookups (7)
- `nec_lookup_conductor_ampacity` - Base ampacity from 310.16
- `nec_lookup_conductor_size` - Reverse lookup (amps -> size)
- `nec_lookup_ampacity_adjustment` - Temp/bundling factors
- `nec_lookup_grounding_conductor` - EGC/GEC sizing
- `nec_lookup_working_space` - Working clearances
- `nec_lookup_conduit_fill` - Conduit fill calculations
- `nec_lookup_table` - Generic fallback

### Utility Tools (3)
- `compare_with_nec` - CEC vs NEC comparison
- `cec_find_limiting_rules` - Find overriding rules (like 240.4(D))
- `python_calculator` - Math calculations

---

## Expected Impact

| Issue | Previous Score | Expected Fix |
|-------|----------------|--------------|
| inspection-007 (conduit fill) | 7/10 | +3 points - will use `nec_lookup_conduit_fill` |
| inspection-009 (adjustment factors) | 6/10 | +4 points - will call `nec_lookup_ampacity_adjustment` |
| inspection-005 (AFCI) | 5/10 | +3-5 points - better search guidance |

**Projected Core score:** 254/280 (90.7%) -> 264-266/280 (94-95%)

---

## Files Modified

1. `core/tools.py` - All tool changes (remove, rename, descriptions)
2. `core/agent.py` - Updated SYSTEM_PROMPT and search_tools list

---

## Evaluation Plan

Run both question sets:
1. Core (NEC) - 28 questions
2. CEC - 30 questions

Generate LLM-as-Judge reports to measure impact.
