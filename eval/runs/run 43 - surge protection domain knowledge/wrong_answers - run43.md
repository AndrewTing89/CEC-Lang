# Wrong Answers Analysis - Run 43

**Date:** 2025-12-12
**Questions with Scores < 5/10:** 0

## Summary

**No questions scored below 5/10 in Run 43!**

The surge protection fix successfully resolved the two failing questions from Run 42:
- cec2022-008: 4/10 → 10/10
- cec2022-012: 4/10 → 10/10

---

## Partial Scores (8-9/10)

The following questions received partial scores. These are documented for future improvement but are not failures.

### cec2022-003 (9/10)
**Question:** Where is GFCI protection required in a residential kitchen?

**Expected:** All receptacles that serve the kitchen countertop surfaces shall have GFCI protection per 210.8(A)(6). Dishwashers are NOT explicitly required to have GFCI under 210.8(A)(6) in CEC 2022 (countertop surfaces only).

**Issue:** Answer expands to include both GFCI and AFCI requirements (accurate but over-comprehensive)

---

### cec2022-006 (8/10)
**Question:** What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?

**Expected:** 36 inches (3 feet)

**Issue:** Answer discusses 30-inch width and 3-foot depth in general working space context rather than giving the direct "36 inches" answer

---

### cec2022-013 (8/10)
**Question:** Panel in closet with 24 inches front clearance, water heater 18 inches to side

**Expected:** Identifies multiple violations including 36" depth requirement

**Issue:** Answer correctly identifies violations but mentions 30" instead of 36" for front clearance in one reference

---

### cec2022-021 (8/10)
**Question:** Residential panel load calculation

**Expected:** ~103A calculated load

**Issue:** Different demand factor application methodology results in ~119A. Same conclusion (200A adequate) but different calculation path.

---

### cec2022-022 (8/10)
**Question:** Garage panel clearance violations

**Expected:** Identifies 36" depth requirement violation

**Issue:** Identifies violations correctly but references 30" in some contexts

---

### cec2022-029 (8/10)
**Question:** Panelboard space requirements for single-family dwellings

**Expected:** CEC 408.2(A) requires reserved spaces for heat pump water heaters, heat pump space heaters, electric cooktops, and electric clothes dryers

**Issue:** Discusses panelboard requirements comprehensively but doesn't explicitly highlight the 408.2(A) reserved space requirements for specific appliances

---

### cec2022-035 (8/10)
**Question:** What does CEC Table 240.4(G) specify that is unique to California?

**Expected:** Table exists in both CEC and NEC but California has modified values

**Issue:** Correctly notes California amendments but doesn't emphasize the specific modified values

---

### cec2022-038 (8/10)
**Question:** California-specific medium voltage cable tables

**Expected:** 20 tables in 311.60(C) series (67-86)

**Issue:** Lists several tables but doesn't mention all 20 tables through 311.60(C)(86)

---

### cec2022-044 (8/10)
**Question:** Minimum working space depth for 480V panelboard under Condition 3

**Expected:** 1.2 m (4 ft)

**Issue:** Mentions 4 ft depth correctly but answer is more general about working space requirements

---

## Fix Verification

### cec2022-008 - FIXED
**Run 42:** Agent answered about service conductor sizing (2/0 AWG copper)
**Run 43:** Agent correctly answered about surge protection (230.67, SPD required)
**Enforcement:** Service Conductor Enforced = No (smart exclusion working)

### cec2022-012 - FIXED
**Run 42:** Agent answered about service conductor sizing (2/0 AWG copper)
**Run 43:** Agent correctly answered about surge protection location (230.67, integral/adjacent, Type 1/2 SPD)
**Enforcement:** Service Conductor Enforced = No (smart exclusion working)

---

## Conclusion

Run 43 has no failing questions. All 53 questions scored 8/10 or higher. The surge protection domain knowledge and smart exclusion fix successfully resolved the issues from Run 42 without introducing any regressions.
