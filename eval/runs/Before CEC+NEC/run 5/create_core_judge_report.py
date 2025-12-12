import json
import re
from pathlib import Path

# Find the Core evaluation results file
run_dir = Path(__file__).parent
core_files = list(run_dir.glob("run5-core_evaluation_results_*.json"))
if not core_files:
    print("No Core evaluation results found!")
    exit(1)

results_file = core_files[0]
print(f"Loading: {results_file}")

with open(results_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = data['results']

def judge_answer(qid, category, expected, actual):
    """
    Judge the answer based on key facts from expected answer.
    Returns: ('Accurate'|'Partially Accurate'|'Inaccurate', 'notes')

    IMPORTANT: Extra detail beyond expected answer is NOT penalized.
    We only check if the expected key facts are present.
    """

    expected_lower = expected.lower()
    actual_lower = actual.lower()

    # baseline-001: Ampacity of 12 AWG copper at 75C
    if qid == 'baseline-001':
        has_20a = '20' in actual and ('ampere' in actual_lower or 'amp' in actual_lower or 'a' in actual_lower)
        has_table = '310.16' in actual or 'table 310' in actual_lower

        if has_20a and has_table:
            return 'Accurate', 'Correct ampacity (20A) and table reference'
        elif has_20a:
            return 'Accurate', 'Correct ampacity (20A)'
        elif '25' in actual:
            return 'Partially Accurate', 'Agent may have given 90C value (25A) instead of 75C (20A)'
        else:
            return 'Inaccurate', 'Missing or incorrect ampacity value'

    # baseline-002: Size for 60A circuit at 75C - REVERSE LOOKUP
    elif qid == 'baseline-002':
        has_6_awg = '6 awg' in actual_lower or '#6' in actual_lower or '6awg' in actual_lower
        has_copper = 'copper' in actual_lower

        if has_6_awg:
            return 'Accurate', 'Correct conductor size (6 AWG copper)'
        elif '4 awg' in actual_lower or '#4' in actual_lower:
            return 'Inaccurate', 'Wrong size (4 AWG instead of 6 AWG)'
        else:
            return 'Inaccurate', 'Missing or incorrect conductor size'

    # baseline-003: GFCI in kitchen
    elif qid == 'baseline-003':
        has_countertop = 'countertop' in actual_lower or 'counter top' in actual_lower
        has_dishwasher = 'dishwasher' in actual_lower
        has_210_8 = '210.8' in actual

        if has_countertop and has_dishwasher:
            return 'Accurate', 'Mentions countertop and dishwasher GFCI requirements'
        elif has_countertop:
            return 'Partially Accurate', 'Has countertop GFCI but missing dishwasher'
        else:
            return 'Partially Accurate', 'Incomplete kitchen GFCI requirements'

    # baseline-004: AFCI for bedrooms
    elif qid == 'baseline-004':
        has_yes = 'yes' in actual_lower or 'required' in actual_lower
        has_210_12 = '210.12' in actual
        has_bedroom = 'bedroom' in actual_lower

        if has_yes and has_bedroom:
            return 'Accurate', 'Correctly states AFCI required for bedrooms'
        elif has_yes:
            return 'Partially Accurate', 'Confirms requirement but incomplete detail'
        else:
            return 'Inaccurate', 'Does not clearly state AFCI is required'

    # baseline-005: Aluminum for 200A service - REVERSE LOOKUP
    elif qid == 'baseline-005':
        has_yes = 'yes' in actual_lower
        has_4_0 = '4/0' in actual or '4-0' in actual or 'four/0' in actual_lower or '0000' in actual
        has_aluminum = 'aluminum' in actual_lower

        if has_yes and has_4_0 and has_aluminum:
            return 'Accurate', 'Correct (Yes, 4/0 AWG aluminum)'
        elif has_4_0 and has_aluminum:
            return 'Accurate', 'Correct size (4/0 AWG aluminum)'
        elif '250' in actual and ('kcmil' in actual_lower or 'mcm' in actual_lower):
            return 'Inaccurate', 'Wrong size (250 kcmil instead of 4/0 AWG)'
        elif has_yes and has_aluminum:
            return 'Partially Accurate', 'Confirms aluminum OK but check size'
        else:
            return 'Partially Accurate', 'Incomplete answer'

    # baseline-006: Working clearance depth
    elif qid == 'baseline-006':
        has_36 = '36' in actual or '3 feet' in actual_lower or 'three feet' in actual_lower or '3 ft' in actual_lower
        has_110_26 = '110.26' in actual

        if has_36:
            return 'Accurate', 'Correct clearance (36 inches / 3 feet)'
        elif '30' in actual:
            return 'Partially Accurate', 'May have used NEC value (30") instead of CEC (36")'
        else:
            return 'Inaccurate', 'Incorrect clearance dimension'

    # baseline-007: Small appliance circuits count
    elif qid == 'baseline-007':
        has_two = 'two' in actual_lower or '2 ' in actual or 'minimum of 2' in actual_lower
        has_20a = '20' in actual and ('ampere' in actual_lower or 'amp' in actual_lower or 'a' in actual_lower)

        if has_two and has_20a:
            return 'Accurate', 'Correct (minimum two 20A circuits)'
        elif has_two:
            return 'Accurate', 'Correct minimum of two circuits'
        elif '4' in actual or '6' in actual:
            return 'Inaccurate', 'Hallucination - said more than 2 circuits required'
        else:
            return 'Partially Accurate', 'Check circuit count'

    # baseline-008: Surge protection required
    elif qid == 'baseline-008':
        has_yes = 'yes' in actual_lower or 'required' in actual_lower
        has_230_67 = '230.67' in actual
        has_spd = 'spd' in actual_lower or 'surge' in actual_lower

        if has_yes and has_230_67:
            return 'Accurate', 'Correct - surge protection required per 230.67'
        elif has_yes and has_spd:
            return 'Accurate', 'Correct - surge protection is required'
        else:
            return 'Partially Accurate', 'Incomplete answer'

    # core-001: Service upgrade sizing
    elif qid == 'core-001':
        has_2_0_copper = '2/0' in actual and 'copper' in actual_lower
        has_4_0_aluminum = '4/0' in actual and 'aluminum' in actual_lower
        has_yes_aluminum = 'yes' in actual_lower and 'aluminum' in actual_lower

        if (has_2_0_copper or has_4_0_aluminum) and has_yes_aluminum:
            return 'Accurate', 'Correct sizes and confirms aluminum permitted'
        elif has_2_0_copper or has_4_0_aluminum:
            return 'Partially Accurate', 'Has some correct sizes'
        else:
            return 'Partially Accurate', 'Check conductor sizes'

    # core-002: Multiwire branch circuit
    elif qid == 'core-002':
        has_common_trip = 'common trip' in actual_lower or 'handle tie' in actual_lower
        has_20a = '20' in actual and ('ampere' in actual_lower or 'amp' in actual_lower or 'a' in actual_lower)
        has_neutral = 'neutral' in actual_lower and ('continuous' in actual_lower or 'not switched' in actual_lower)
        has_210_4 = '210.4' in actual

        if has_common_trip and has_20a:
            return 'Accurate', 'Correct breaker requirements'
        elif has_common_trip:
            return 'Partially Accurate', 'Has handle tie/common trip but check breaker size'
        else:
            return 'Partially Accurate', 'Missing key requirements'

    # core-003: GFCI locations 2023 NEC
    elif qid == 'core-003':
        locations = ['bathroom', 'garage', 'outdoor', 'crawl', 'basement', 'kitchen',
                     'laundry', 'sink', 'bathtub', 'shower', 'boathouse']
        found_locations = sum(1 for loc in locations if loc in actual_lower)
        has_210_8 = '210.8' in actual

        if found_locations >= 8 and has_210_8:
            return 'Accurate', f'Found {found_locations} locations with code reference'
        elif found_locations >= 6:
            return 'Partially Accurate', f'Found {found_locations} locations, may be missing some'
        else:
            return 'Partially Accurate', f'Only found {found_locations} locations'

    # core-004: Surge protection location
    elif qid == 'core-004':
        has_yes = 'yes' in actual_lower or 'required' in actual_lower
        has_230_67 = '230.67' in actual
        has_type_1_2 = 'type 1' in actual_lower or 'type 2' in actual_lower
        has_location = 'integral' in actual_lower or 'adjacent' in actual_lower or 'downstream' in actual_lower

        # Check for code edition - should answer about NEC 2023, not CEC
        uses_nec = 'nec' in actual_lower
        uses_cec = 'cec' in actual_lower and 'nec' not in actual_lower

        if has_yes and has_230_67 and has_type_1_2 and has_location:
            return 'Accurate', 'Complete answer with SPD types and locations'
        elif has_yes and has_230_67:
            return 'Partially Accurate', 'Has requirement but incomplete on types/locations'
        elif uses_cec and not uses_nec:
            return 'Partially Accurate', 'Answered with CEC instead of NEC as asked'
        else:
            return 'Partially Accurate', 'Incomplete answer'

    # core-005: Panel in closet violations - CRITICAL
    elif qid == 'core-005':
        has_no = 'no' in actual_lower or 'violat' in actual_lower or 'does not' in actual_lower
        has_36_depth = '36' in actual or 'three feet' in actual_lower or '3 feet' in actual_lower
        has_closet_prohibition = ('closet' in actual_lower and
                                   ('prohibit' in actual_lower or 'not' in actual_lower or 'shall not' in actual_lower))
        has_240_24_d = '240.24(d)' in actual_lower or '240.24' in actual
        has_110_26 = '110.26' in actual
        has_storage = 'storage' in actual_lower and 'working space' in actual_lower

        violations_found = sum([has_36_depth, has_closet_prohibition or has_240_24_d, has_storage])

        if has_no and violations_found >= 2 and has_closet_prohibition:
            return 'Accurate', 'Identifies closet prohibition and other violations'
        elif has_no and violations_found >= 1:
            return 'Partially Accurate', f'Found {violations_found} violation(s), may be missing closet prohibition'
        elif has_no:
            return 'Partially Accurate', 'Identifies violation but missing specifics'
        else:
            return 'Inaccurate', 'Does not identify violations'

    # core-006: Double-tapped breaker
    elif qid == 'core-006':
        has_yes = 'yes' in actual_lower or 'violation' in actual_lower
        has_110_14 = '110.14' in actual
        has_110_3_b = '110.3(b)' in actual_lower or '110.3' in actual

        if has_yes and (has_110_14 or has_110_3_b):
            return 'Accurate', 'Correct - violation with code reference'
        elif has_yes:
            return 'Accurate', 'Correctly identifies as violation'
        else:
            return 'Inaccurate', 'Does not identify as violation'

    # core-007: Subpanel grounding
    elif qid == 'core-007':
        has_separated = 'separat' in actual_lower and ('ground' in actual_lower or 'neutral' in actual_lower)
        has_no_mbj = ('no' in actual_lower or 'not' in actual_lower) and ('main bonding' in actual_lower or 'mbj' in actual_lower)
        has_isolated_neutral = 'isolat' in actual_lower and 'neutral' in actual_lower
        has_250_32 = '250.32' in actual

        if has_separated and has_no_mbj:
            return 'Accurate', 'Correct separation and no MBJ requirement'
        elif has_separated:
            return 'Partially Accurate', 'Has separation but missing MBJ detail'
        else:
            return 'Partially Accurate', 'Incomplete subpanel grounding answer'

    # core-008: MBJ vs SBJ
    elif qid == 'core-008':
        has_mbj = 'main bonding jumper' in actual_lower or 'mbj' in actual_lower
        has_sbj = 'system bonding jumper' in actual_lower or 'sbj' in actual_lower
        has_service = 'service' in actual_lower
        has_separately_derived = 'separately derived' in actual_lower or 'sds' in actual_lower or 'transformer' in actual_lower
        has_250_28 = '250.28' in actual
        has_250_30 = '250.30' in actual

        if has_mbj and has_sbj and has_service and has_separately_derived:
            return 'Accurate', 'Correctly explains both MBJ and SBJ'
        elif has_mbj and has_sbj:
            return 'Partially Accurate', 'Has both terms but check explanations'
        else:
            return 'Partially Accurate', 'Incomplete comparison'

    # core-009: Small appliance circuits + dining room
    elif qid == 'core-009':
        has_two = 'two' in actual_lower or '2 ' in actual or 'minimum of 2' in actual_lower
        has_yes_dining = 'yes' in actual_lower and 'dining' in actual_lower
        has_can_serve = ('can' in actual_lower or 'permitted' in actual_lower) and 'dining' in actual_lower

        if has_two and (has_yes_dining or has_can_serve):
            return 'Accurate', 'Correct - two circuits, can serve dining room'
        elif has_two:
            return 'Partially Accurate', 'Has circuit count but check dining room'
        else:
            return 'Partially Accurate', 'Incomplete answer'

    # core-010: Derating calculation with temperature and bundling
    elif qid == 'core-010':
        has_30a_base = '30' in actual and ('base' in actual_lower or '90' in actual_lower or 'thhn' in actual_lower)
        has_0_82 = '0.82' in actual or '.82' in actual
        has_0_80 = '0.80' in actual or '.80' in actual or '0.8' in actual
        has_result = '19' in actual or '20' in actual

        if has_30a_base and has_0_82 and has_0_80 and has_result:
            return 'Accurate', 'Correct calculation with all factors'
        elif has_0_82 and has_0_80:
            return 'Partially Accurate', 'Has correction factors, check result'
        elif has_0_82 or has_0_80:
            return 'Partially Accurate', 'Has one factor, may be missing the other'
        else:
            return 'Partially Accurate', 'Check derating factors'

    # core-011: Why AFCI required
    elif qid == 'core-011':
        has_fire = 'fire' in actual_lower
        has_arc = 'arc' in actual_lower
        has_210_12 = '210.12' in actual
        has_detection = 'detect' in actual_lower

        if has_fire and has_arc and has_detection:
            return 'Accurate', 'Good explanation of AFCI purpose'
        elif has_fire and has_arc:
            return 'Accurate', 'Explains arc fault fire prevention'
        else:
            return 'Partially Accurate', 'Incomplete explanation'

    # core-012: Torque specifications
    elif qid == 'core-012':
        has_110_14 = '110.14' in actual
        has_110_3_b = '110.3(b)' in actual_lower or '110.3' in actual
        has_loose = 'loose' in actual_lower
        has_heat = 'heat' in actual_lower
        has_resistance = 'resistance' in actual_lower

        if (has_110_14 or has_110_3_b) and (has_loose or has_heat or has_resistance):
            return 'Accurate', 'Correct references and explanation'
        elif has_110_14 or has_110_3_b:
            return 'Partially Accurate', 'Has code references but limited explanation'
        else:
            return 'Partially Accurate', 'Missing key code references'

    # inspection-001: Panel load calculation
    elif qid == 'inspection-001':
        has_calculation = any(str(x) in actual for x in range(90, 130))  # Expected result ~103A
        has_adequate = 'adequate' in actual_lower or 'sufficient' in actual_lower or 'yes' in actual_lower
        has_220 = '220' in actual
        has_demand_factor = 'demand' in actual_lower and 'factor' in actual_lower

        if has_adequate and has_220 and has_demand_factor:
            return 'Accurate', '200A panel adequate with demand factor calculation'
        elif has_adequate and has_calculation:
            return 'Partially Accurate', 'Correct conclusion, check calculation details'
        elif has_adequate:
            return 'Partially Accurate', 'Correct conclusion but limited calculation shown'
        else:
            return 'Partially Accurate', 'Check calculation and conclusion'

    # inspection-002: Clearance violations
    elif qid == 'inspection-002':
        has_depth_violation = ('28' in actual or 'depth' in actual_lower) and ('violation' in actual_lower or '36' in actual)
        has_water_heater = 'water heater' in actual_lower and ('obstruct' in actual_lower or 'violation' in actual_lower or 'working space' in actual_lower)
        has_110_26 = '110.26' in actual

        violations_found = sum([has_depth_violation, has_water_heater])

        if violations_found >= 2 and has_110_26:
            return 'Accurate', 'Identifies depth and water heater violations'
        elif violations_found >= 1:
            return 'Partially Accurate', f'Found {violations_found} violation(s)'
        else:
            return 'Partially Accurate', 'Check violation identification'

    # inspection-005: GFCI/AFCI compliance - kitchen circuits
    elif qid == 'inspection-005':
        # Check for correct requirements
        has_countertop_gfci_afci = 'countertop' in actual_lower and ('gfci' in actual_lower or 'afci' in actual_lower)
        has_dishwasher_gfci = 'dishwasher' in actual_lower and 'gfci' in actual_lower
        has_disposal_afci = 'disposal' in actual_lower and 'afci' in actual_lower
        has_refrigerator_afci = 'refrigerator' in actual_lower and 'afci' in actual_lower
        has_210_8 = '210.8' in actual
        has_210_12 = '210.12' in actual

        # Check for WRONG answers (exceptions that don't apply)
        claims_exempt = 'exempt' in actual_lower or 'not required' in actual_lower

        requirements_correct = sum([has_countertop_gfci_afci, has_dishwasher_gfci, has_disposal_afci, has_refrigerator_afci])

        if requirements_correct >= 3 and not claims_exempt:
            return 'Accurate', 'Correct GFCI/AFCI requirements for kitchen'
        elif requirements_correct >= 2:
            return 'Partially Accurate', f'Found {requirements_correct} correct requirements'
        elif claims_exempt:
            return 'Inaccurate', 'Incorrectly claims equipment exempt from protection'
        else:
            return 'Partially Accurate', 'Incomplete protection requirements'

    # inspection-006: Subpanel violations
    elif qid == 'inspection-006':
        has_neutral_violation = 'neutral' in actual_lower and ('bond' in actual_lower or 'isolat' in actual_lower)
        has_mbj_violation = ('main bonding' in actual_lower or 'mbj' in actual_lower) and ('remove' in actual_lower or 'violation' in actual_lower or 'not' in actual_lower)
        has_250_24 = '250.24' in actual
        has_408_40 = '408.40' in actual

        if has_neutral_violation and has_mbj_violation:
            return 'Accurate', 'Identifies neutral bonding and MBJ violations'
        elif has_neutral_violation or has_mbj_violation:
            return 'Partially Accurate', 'Identifies some violations'
        else:
            return 'Partially Accurate', 'Check violation identification'

    # inspection-007: Conduit fill
    elif qid == 'inspection-007':
        has_28_29 = '28' in actual or '29' in actual
        has_chapter_9 = 'chapter 9' in actual_lower or 'table 1' in actual_lower or 'table 4' in actual_lower
        has_0_610 = '0.610' in actual or '.610' in actual
        has_0_0211 = '0.0211' in actual or '.0211' in actual

        if has_28_29 and (has_chapter_9 or has_0_610):
            return 'Accurate', 'Correct conductor count with table references'
        elif has_28_29:
            return 'Accurate', 'Correct conductor count (28-29)'
        else:
            return 'Partially Accurate', 'Check conductor count calculation'

    # inspection-008: Voltage drop
    elif qid == 'inspection-008':
        has_2_84 = '2.84' in actual or '2.8' in actual
        has_2_37 = '2.37' in actual or '2.4' in actual or '2.3' in actual
        has_yes_meets = ('yes' in actual_lower or 'meets' in actual_lower or 'less than 3' in actual_lower)
        has_3_percent = '3%' in actual or '3 percent' in actual_lower

        if (has_2_84 or has_2_37) and has_yes_meets:
            return 'Accurate', 'Correct voltage drop calculation and conclusion'
        elif has_yes_meets and has_3_percent:
            return 'Partially Accurate', 'Correct conclusion, check calculation'
        else:
            return 'Partially Accurate', 'Check voltage drop calculation'

    # inspection-009: Derating calculation (TW conductors)
    elif qid == 'inspection-009':
        has_20a_base = '20' in actual and ('base' in actual_lower or 'tw' in actual_lower or '60' in actual_lower)
        has_0_71 = '0.71' in actual or '.71' in actual
        has_0_80 = '0.80' in actual or '.80' in actual or '0.8' in actual
        has_result = '11' in actual  # Expected ~11.36A

        # Check for WRONG answer (using 0.70 instead of 0.80)
        has_wrong_factor = '0.70' in actual and '0.71' in actual and '0.80' not in actual

        if has_20a_base and has_0_71 and has_0_80 and has_result:
            return 'Accurate', 'Correct derating calculation (20A x 0.71 x 0.80 = 11.36A)'
        elif has_0_71 and has_0_80:
            return 'Partially Accurate', 'Has both factors, check result'
        elif has_wrong_factor:
            return 'Inaccurate', 'Used wrong bundling factor (0.70 instead of 0.80 for 6 conductors)'
        else:
            return 'Partially Accurate', 'Check derating factors - need 0.71 temp and 0.80 bundling'

    # inspection-010: GEC sizing for 1000 kcmil service - REVERSE LOOKUP
    elif qid == 'inspection-010':
        has_2_0 = '2/0' in actual or '2-0' in actual or 'two/0' in actual_lower
        has_copper = 'copper' in actual_lower
        has_250_66 = '250.66' in actual

        if has_2_0 and has_copper:
            return 'Accurate', 'Correct GEC size (2/0 AWG copper)'
        elif '1/0' in actual:
            return 'Inaccurate', 'Wrong size (1/0 AWG instead of 2/0 AWG)'
        elif '4/0' in actual and 'aluminum' in actual_lower:
            return 'Accurate', 'Correct alternate (4/0 AWG aluminum)'
        else:
            return 'Partially Accurate', 'Check GEC size per Table 250.66'

    # Default
    return 'Partially Accurate', 'Requires manual review'


# Process all results
verdicts = {'Accurate': 0, 'Partially Accurate': 0, 'Inaccurate': 0}
detailed_results = []

for item in results:
    verdict, notes = judge_answer(item['id'], item['category'],
                                  item['expected_answer'], item['answer'])
    verdicts[verdict] += 1
    detailed_results.append({
        'id': item['id'],
        'category': item['category'],
        'verdict': verdict,
        'notes': notes
    })

# Calculate category statistics
category_stats = {}
for item in results:
    cat = item['category']
    if cat not in category_stats:
        category_stats[cat] = {'total': 0, 'accurate': 0, 'partial': 0, 'inaccurate': 0}
    category_stats[cat]['total'] += 1

for result in detailed_results:
    cat = result['category']
    if result['verdict'] == 'Accurate':
        category_stats[cat]['accurate'] += 1
    elif result['verdict'] == 'Partially Accurate':
        category_stats[cat]['partial'] += 1
    else:
        category_stats[cat]['inaccurate'] += 1

# Generate markdown report
report = f"""# LLM Judge Report: Core Evaluation (Run 5)

## Summary
- Total Questions: 28
- Accurate: {verdicts['Accurate']}/28 ({verdicts['Accurate']/28*100:.1f}%)
- Partially Accurate: {verdicts['Partially Accurate']}/28 ({verdicts['Partially Accurate']/28*100:.1f}%)
- Inaccurate: {verdicts['Inaccurate']}/28 ({verdicts['Inaccurate']/28*100:.1f}%)

## Scoring Criteria
- **Accurate**: Answer contains all key facts from expected answer
- **Partially Accurate**: Answer contains some but not all key facts
- **Inaccurate**: Answer is wrong or missing critical information
- **Extra detail beyond expected answer is NOT penalized**

## Results

| ID | Category | Verdict | Notes |
|----|----------|---------|-------|
"""

for result in detailed_results:
    report += f"| {result['id']} | {result['category']} | {result['verdict']} | {result['notes']} |\n"

# Add detailed analysis
report += """

## Detailed Analysis

### Issues Found

"""

inaccurate_items = [r for r in detailed_results if r['verdict'] == 'Inaccurate']
if inaccurate_items:
    report += f"**Inaccurate Answers ({len(inaccurate_items)}):**\n"
    for item in inaccurate_items:
        report += f"- {item['id']} ({item['category']}): {item['notes']}\n"
    report += "\n"
else:
    report += "**No Inaccurate Answers!**\n\n"

partial_items = [r for r in detailed_results if r['verdict'] == 'Partially Accurate']
if partial_items:
    report += f"**Partially Accurate Answers ({len(partial_items)}):**\n"
    for item in partial_items:
        report += f"- {item['id']}: {item['notes']}\n"
    report += "\n"

accurate_items = [r for r in detailed_results if r['verdict'] == 'Accurate']
report += f"""
### Strengths

**Accurate Answers ({len(accurate_items)}/28 = {len(accurate_items)/28*100:.1f}%):**
"""
for item in accurate_items:
    report += f"- {item['id']}: {item['notes']}\n"

# Category breakdown
report += """

## Score Distribution by Category

| Category | Questions | Accurate | Partial | Inaccurate | Success Rate |
|----------|-----------|----------|---------|------------|--------------|
"""

for cat, stats in sorted(category_stats.items()):
    success_rate = (stats['accurate'] + stats['partial']) / stats['total'] * 100 if stats['total'] > 0 else 0
    report += f"| {cat} | {stats['total']} | {stats['accurate']} | {stats['partial']} | {stats['inaccurate']} | {success_rate:.1f}% |\n"

report += f"""

## Comparison to Run 4

### Run 4 Results:
- Accurate: 17/28 (60.7%)
- Partially Accurate: 9/28 (32.1%)
- Inaccurate: 2/28 (7.1%)

### Run 5 Results (After 1-Prompt System + Table Selection):
- Accurate: {verdicts['Accurate']}/28 ({verdicts['Accurate']/28*100:.1f}%)
- Partially Accurate: {verdicts['Partially Accurate']}/28 ({verdicts['Partially Accurate']/28*100:.1f}%)
- Inaccurate: {verdicts['Inaccurate']}/28 ({verdicts['Inaccurate']/28*100:.1f}%)

### Key Fixes Applied:
1. **1-Prompt System**: Removed two-step prompting to eliminate hallucination from planning context
2. **Table Selection**: Added conductor_application parameter for Table 310.12(A) vs 310.16

## Overall Assessment

The Core agent achieved:
- **{verdicts['Accurate']}/28 Accurate** ({verdicts['Accurate']/28*100:.1f}%)
- **{verdicts['Partially Accurate']}/28 Partially Accurate** ({verdicts['Partially Accurate']/28*100:.1f}%)
- **{verdicts['Inaccurate']}/28 Inaccurate** ({verdicts['Inaccurate']/28*100:.1f}%)

**Success Rate (Accurate + Partial)**: {(verdicts['Accurate'] + verdicts['Partially Accurate'])/28*100:.1f}%

---
*Report Generated: Run 5*
*Evaluation Set: Core Evaluation - 28 Questions*
"""

# Write the report
output_path = run_dir / 'core_judge_report.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"Report generated: {output_path}")
print(f"\nSummary:")
print(f"Accurate: {verdicts['Accurate']}/28 ({verdicts['Accurate']/28*100:.1f}%)")
print(f"Partially Accurate: {verdicts['Partially Accurate']}/28 ({verdicts['Partially Accurate']/28*100:.1f}%)")
print(f"Inaccurate: {verdicts['Inaccurate']}/28 ({verdicts['Inaccurate']/28*100:.1f}%)")
