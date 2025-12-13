# Wrong Answers Analysis - Run 42

**Date:** 2025-12-12
**Questions with Scores < 5/10:** 2

---

## cec2022-008 - Surge Protection Requirement

**Score:** 4/10 (Accuracy: 2, Completeness: 2)

**Question:** Is surge protection required for a new 200A residential service?

**Expected Answer:**
Yes, all services supplying dwelling units shall be provided with a surge-protective device (SPD) per 230.67.

**Agent Answer:**
Agent answered about **service conductor sizing** (2/0 AWG copper, 4/0 AWG aluminum from Table 310.12(A)) instead of surge protection requirements.

**Root Cause:**
The service conductor enforcement rule triggered on "200A service" keywords, forcing the agent to call `cec_lookup_conductor_size` instead of searching for surge protection requirements.

**Evidence:**
- Service Conductor Enforced: **Yes** (in results)
- Tools Called: `cec_search, cec_lookup_conductor_size`

**Fix Required:**
Modify enforcement rule to NOT trigger when question contains "surge" or "protection" keywords.

---

## cec2022-012 - Surge Protection Location

**Score:** 4/10 (Accuracy: 2, Completeness: 2)

**Question:** Is surge protection required for a new 200A residential service? If so, where can it be installed?

**Expected Answer:**
Yes, per 230.67. Type 1 or Type 2 SPD required. Must be installed integral to the service equipment or immediately adjacent. Exception allows installation at the first downstream panelboard.

**Agent Answer:**
Agent again answered about **service conductor sizing** (2/0 AWG copper, 4/0 AWG aluminum from Table 310.12(A)) instead of surge protection requirements and installation locations.

**Root Cause:**
Same as cec2022-008 - service conductor enforcement triggered incorrectly.

**Evidence:**
- Service Conductor Enforced: **Yes** (in results)
- Tools Called: `cec_search, cec_lookup_conductor_size`

**Fix Required:**
Same as above - refine enforcement rule.

---

## Summary

Both wrong answers share the same root cause: the service conductor enforcement rule added in Run 42 to fix cec2022-009 is triggering too aggressively. It detects "200A service" in the question and forces the agent to look up conductor sizing, even when the question is actually about surge protection.

### Proposed Fix

In `core/agent.py`, modify the service conductor enforcement rule (lines 763-778) to exclude surge protection questions:

```python
# Current rule (too broad):
if any(kw in q_lower for kw in ['service conductor', '200a service',
                                 'dwelling service', 'service entrance']):

# Proposed fix (add negative condition):
if any(kw in q_lower for kw in ['service conductor', '200a service',
                                 'dwelling service', 'service entrance']):
    # Don't enforce if question is about surge protection
    if not any(surge_kw in q_lower for surge_kw in ['surge', 'spd', '230.67', 'protection device']):
        # ... rest of enforcement logic
```

This ensures the enforcement only triggers for actual conductor sizing questions, not surge protection queries that happen to mention service amperage.
