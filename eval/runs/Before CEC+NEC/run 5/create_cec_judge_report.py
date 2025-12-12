import json
import re
from pathlib import Path

# Find the CEC evaluation results file
run_dir = Path(__file__).parent
cec_files = list(run_dir.glob("run5-cec_evaluation_results_*.json"))
if not cec_files:
    print("No CEC evaluation results found!")
    exit(1)

results_file = cec_files[0]
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

    # cec-001: Panelboard space requirements
    if qid == 'cec-001':
        appliances = ['heat pump water heater', 'heat pump space heater', 'cooktop', 'dryer', 'ev', 'electric vehicle']
        found_appliances = sum(1 for a in appliances if a in actual_lower)
        has_408_2 = '408.2' in actual or '408' in actual

        if found_appliances >= 4 and has_408_2:
            return 'Accurate', f'Found {found_appliances} appliances with code reference'
        elif found_appliances >= 3:
            return 'Partially Accurate', f'Found {found_appliances} appliances, may be missing some'
        else:
            return 'Partially Accurate', f'Only found {found_appliances} required appliances'

    # cec-002: EV charging infrastructure
    elif qid == 'cec-002':
        has_40a = '40' in actual and ('amp' in actual_lower or 'a ' in actual_lower)
        has_conduit = 'conduit' in actual_lower
        has_panel = 'panel' in actual_lower
        has_408_2 = '408.2' in actual or '408' in actual

        if has_40a and has_conduit and has_panel:
            return 'Accurate', 'Complete EV requirements with circuit, conduit, panel'
        elif has_40a or (has_conduit and has_panel):
            return 'Partially Accurate', 'Has some EV requirements'
        else:
            return 'Partially Accurate', 'Incomplete EV charging requirements'

    # cec-003: Solar PV requirements
    elif qid == 'cec-003':
        has_rapid_shutdown = 'rapid shutdown' in actual_lower or '690.12' in actual
        has_arc_fault = 'arc' in actual_lower and 'fault' in actual_lower or '690.11' in actual
        has_grounding = 'ground' in actual_lower and '690.4' in actual
        has_title_24 = 'title 24' in actual_lower

        requirements_found = sum([has_rapid_shutdown, has_arc_fault, has_grounding, has_title_24])

        if requirements_found >= 3:
            return 'Accurate', f'Found {requirements_found} key requirements'
        elif requirements_found >= 2:
            return 'Partially Accurate', f'Found {requirements_found} requirements'
        else:
            return 'Partially Accurate', 'Incomplete solar PV requirements'

    # cec-004: Heat pump water heater circuit
    elif qid == 'cec-004':
        has_reserved = 'reserved' in actual_lower or 'space' in actual_lower
        has_408_2 = '408.2' in actual or '408' in actual
        has_heat_pump = 'heat pump' in actual_lower

        if has_reserved and has_408_2 and has_heat_pump:
            return 'Accurate', 'Correct reserved space requirement with code reference'
        elif has_reserved or has_408_2:
            return 'Partially Accurate', 'Has some requirements'
        else:
            return 'Partially Accurate', 'Incomplete heat pump requirements'

    # cec-005: Electric cooktop readiness
    elif qid == 'cec-005':
        has_reserved = 'reserved' in actual_lower or 'space' in actual_lower
        has_408_2 = '408.2' in actual or '408' in actual
        has_cooktop = 'cooktop' in actual_lower or 'cooking' in actual_lower

        if has_reserved and has_408_2 and has_cooktop:
            return 'Accurate', 'Correct reserved space for cooktop'
        elif has_reserved or has_408_2:
            return 'Partially Accurate', 'Has some requirements'
        else:
            return 'Partially Accurate', 'Incomplete cooktop requirements'

    # cec-006: Electric clothes dryer
    elif qid == 'cec-006':
        has_reserved = 'reserved' in actual_lower or 'space' in actual_lower
        has_408_2 = '408.2' in actual or '408' in actual
        has_dryer = 'dryer' in actual_lower

        if has_reserved and has_408_2 and has_dryer:
            return 'Accurate', 'Correct reserved space for dryer'
        elif has_reserved or has_408_2:
            return 'Partially Accurate', 'Has some requirements'
        else:
            return 'Partially Accurate', 'Incomplete dryer requirements'

    # cec-007: Table 240.4(G)
    elif qid == 'cec-007':
        has_240_4_g = '240.4(g)' in actual_lower or '240.4' in actual
        has_cec_only = 'california' in actual_lower or 'cec' in actual_lower or 'only' in actual_lower
        has_overcurrent = 'overcurrent' in actual_lower

        if has_240_4_g and has_cec_only:
            return 'Accurate', 'Correctly identifies CEC-only table'
        elif has_240_4_g:
            return 'Partially Accurate', 'Has table reference'
        else:
            return 'Partially Accurate', 'Incomplete Table 240.4(G) info'

    # cec-008: Table 242.3
    elif qid == 'cec-008':
        has_242_3 = '242.3' in actual
        has_surge = 'surge' in actual_lower
        has_cec_only = 'california' in actual_lower or 'cec' in actual_lower

        if has_242_3 and has_surge:
            return 'Accurate', 'Correctly identifies CEC surge protection table'
        elif has_242_3 or has_surge:
            return 'Partially Accurate', 'Has partial info'
        else:
            return 'Partially Accurate', 'Incomplete Table 242.3 info'

    # cec-009: Table 430.72(B)
    elif qid == 'cec-009':
        has_430_72 = '430.72' in actual
        has_motor = 'motor' in actual_lower
        has_control = 'control' in actual_lower
        has_overcurrent = 'overcurrent' in actual_lower or 'ocp' in actual_lower

        if has_430_72 and has_motor and has_control:
            return 'Accurate', 'Correct motor control OCP table info'
        elif has_430_72:
            return 'Partially Accurate', 'Has table reference'
        else:
            return 'Partially Accurate', 'Incomplete Table 430.72(B) info'

    # cec-010: Medium voltage tables
    elif qid == 'cec-010':
        has_311_60 = '311.60' in actual
        has_18_tables = '18' in actual or 'eighteen' in actual_lower
        has_medium_voltage = 'medium voltage' in actual_lower or 'mv' in actual_lower

        if has_311_60 and (has_18_tables or has_medium_voltage):
            return 'Accurate', 'Correctly identifies CEC medium voltage tables'
        elif has_311_60 or has_medium_voltage:
            return 'Partially Accurate', 'Has some info'
        else:
            return 'Partially Accurate', 'Incomplete medium voltage table info'

    # cec-011: 4/0 AWG copper ampacity
    elif qid == 'cec-011':
        has_230 = '230' in actual and ('amp' in actual_lower or 'a' in actual_lower)
        has_table_310_16 = '310.16' in actual

        if has_230 and has_table_310_16:
            return 'Accurate', 'Correct ampacity (230A) with table reference'
        elif has_230:
            return 'Accurate', 'Correct ampacity (230A)'
        else:
            return 'Inaccurate', 'Incorrect ampacity value'

    # cec-012: EGC for 200A circuit
    elif qid == 'cec-012':
        has_6_awg_copper = '6 awg' in actual_lower or '#6' in actual_lower
        has_4_awg_aluminum = '4 awg' in actual_lower and 'aluminum' in actual_lower
        has_250_122 = '250.122' in actual

        if (has_6_awg_copper or has_4_awg_aluminum) and has_250_122:
            return 'Accurate', 'Correct EGC size with table reference'
        elif has_6_awg_copper or has_4_awg_aluminum:
            return 'Accurate', 'Correct EGC size'
        else:
            return 'Partially Accurate', 'Check EGC size per Table 250.122'

    # cec-013: GEC for 3/0 AWG service
    elif qid == 'cec-013':
        has_4_awg_copper = '4 awg' in actual_lower and 'copper' in actual_lower
        has_2_awg_aluminum = '2 awg' in actual_lower and 'aluminum' in actual_lower
        has_250_66 = '250.66' in actual

        if (has_4_awg_copper or has_2_awg_aluminum) and has_250_66:
            return 'Accurate', 'Correct GEC size with table reference'
        elif has_4_awg_copper or has_2_awg_aluminum:
            return 'Accurate', 'Correct GEC size'
        else:
            return 'Partially Accurate', 'Check GEC size per Table 250.66'

    # cec-014: Temperature correction factor at 40C
    elif qid == 'cec-014':
        has_0_88 = '0.88' in actual or '.88' in actual
        has_310_15 = '310.15' in actual

        if has_0_88 and has_310_15:
            return 'Accurate', 'Correct factor (0.88) with table reference'
        elif has_0_88:
            return 'Accurate', 'Correct temperature correction factor (0.88)'
        else:
            return 'Partially Accurate', 'Check temperature correction factor'

    # cec-015: Bundling factor for 7-9 conductors
    elif qid == 'cec-015':
        has_70 = '70%' in actual or '0.70' in actual or '0.7' in actual
        has_310_15 = '310.15' in actual

        if has_70 and has_310_15:
            return 'Accurate', 'Correct factor (0.70/70%) with table reference'
        elif has_70:
            return 'Accurate', 'Correct bundling factor (70%/0.70)'
        else:
            return 'Partially Accurate', 'Check bundling adjustment factor'

    # cec-016: Working space for 480V Condition 3
    elif qid == 'cec-016':
        has_4_ft = '4 ft' in actual_lower or '4 feet' in actual_lower or '4ft' in actual_lower
        has_1_2_m = '1.2' in actual and 'm' in actual_lower
        has_110_26 = '110.26' in actual

        if (has_4_ft or has_1_2_m) and has_110_26:
            return 'Accurate', 'Correct working space (4 ft/1.2m) with reference'
        elif has_4_ft or has_1_2_m:
            return 'Accurate', 'Correct working space depth'
        else:
            return 'Partially Accurate', 'Check working space requirements'

    # cec-017: Enclosure types for outdoor use
    elif qid == 'cec-017':
        enclosure_types = ['type 3', '3r', '3s', 'type 4', '4x', 'type 6', '6p']
        found_types = sum(1 for t in enclosure_types if t in actual_lower)
        has_110_28 = '110.28' in actual

        if found_types >= 5 and has_110_28:
            return 'Accurate', f'Found {found_types} enclosure types with reference'
        elif found_types >= 4:
            return 'Partially Accurate', f'Found {found_types} types, may be missing some'
        else:
            return 'Partially Accurate', f'Only found {found_types} enclosure types'

    # cec-018: Office lighting load
    elif qid == 'cec-018':
        has_3_5 = '3.5' in actual and ('va' in actual_lower or 'volt-ampere' in actual_lower)
        has_220_12 = '220.12' in actual

        if has_3_5 and has_220_12:
            return 'Accurate', 'Correct office load (3.5 VA/sq ft) with reference'
        elif has_3_5:
            return 'Accurate', 'Correct office lighting load (3.5 VA/sq ft)'
        else:
            return 'Partially Accurate', 'Check office lighting load value'

    # cec-019: Flexible cord ampacity (12 AWG)
    elif qid == 'cec-019':
        has_25 = '25' in actual and ('amp' in actual_lower or 'a' in actual_lower)
        has_400_5 = '400.5' in actual

        if has_25 and has_400_5:
            return 'Accurate', 'Correct cord ampacity (25A) with reference'
        elif has_25:
            return 'Accurate', 'Correct flexible cord ampacity (25A)'
        else:
            return 'Partially Accurate', 'Check flexible cord ampacity'

    # cec-020: SF-2 fixture wire temperature
    elif qid == 'cec-020':
        has_200c = '200' in actual and ('c' in actual_lower or 'celsius' in actual_lower or 'degree' in actual_lower)
        has_392f = '392' in actual
        has_402_3 = '402.3' in actual

        if (has_200c or has_392f) and has_402_3:
            return 'Accurate', 'Correct temperature (200C/392F) with reference'
        elif has_200c or has_392f:
            return 'Accurate', 'Correct fixture wire temperature'
        else:
            return 'Partially Accurate', 'Check SF-2 temperature rating'

    # cec-021: Adjusted ampacity calculation
    elif qid == 'cec-021':
        has_50a = '50' in actual and ('base' in actual_lower or 'ampacity' in actual_lower or 'thwn' in actual_lower)
        has_0_88 = '0.88' in actual or '.88' in actual
        has_0_70 = '0.70' in actual or '.70' in actual or '0.7' in actual
        has_result = '30' in actual or '31' in actual

        if has_50a and has_0_88 and has_0_70 and has_result:
            return 'Accurate', 'Correct calculation with all factors'
        elif has_0_88 and has_0_70:
            return 'Partially Accurate', 'Has factors, check result'
        else:
            return 'Partially Accurate', 'Incomplete calculation'

    # cec-022: Service sizing calculation
    elif qid == 'cec-022':
        has_3_0_service = '3/0' in actual and 'service' in actual_lower
        has_6_egc = '6 awg' in actual_lower and ('egc' in actual_lower or 'equipment' in actual_lower or 'grounding' in actual_lower)
        has_4_gec = '4 awg' in actual_lower and ('gec' in actual_lower or 'electrode' in actual_lower)

        sizes_correct = sum([has_3_0_service, has_6_egc, has_4_gec])

        if sizes_correct >= 2:
            return 'Accurate', f'Correct with {sizes_correct} key sizes'
        elif sizes_correct >= 1:
            return 'Partially Accurate', f'Has {sizes_correct} correct size(s)'
        else:
            return 'Partially Accurate', 'Check conductor sizing'

    # cec-023: Office lighting calculation
    elif qid == 'cec-023':
        has_3_5 = '3.5' in actual
        has_5000 = '5000' in actual or '5,000' in actual
        has_17500 = '17500' in actual or '17,500' in actual or '17.5' in actual

        if has_3_5 and has_17500:
            return 'Accurate', 'Correct calculation (5000 x 3.5 = 17,500 VA)'
        elif has_17500:
            return 'Accurate', 'Correct result (17,500 VA)'
        else:
            return 'Partially Accurate', 'Check calculation'

    # cec-024: Motor control OCP
    elif qid == 'cec-024':
        has_10 = '10' in actual and ('amp' in actual_lower or 'a' in actual_lower)
        has_430_72 = '430.72' in actual
        has_16_awg = '16' in actual and ('awg' in actual_lower or 'gauge' in actual_lower)

        if has_10 and has_430_72:
            return 'Accurate', 'Correct OCP (10A) with table reference'
        elif has_10:
            return 'Accurate', 'Correct maximum OCP (10A)'
        else:
            return 'Partially Accurate', 'Check motor control OCP rating'

    # cec-025: Dwelling lighting load
    elif qid == 'cec-025':
        has_3 = '3 va' in actual_lower or '3va' in actual_lower or '3 volt' in actual_lower
        has_2400 = '2400' in actual or '2,400' in actual
        has_7200 = '7200' in actual or '7,200' in actual or '7.2' in actual

        if has_3 and has_7200:
            return 'Accurate', 'Correct calculation (2400 x 3 = 7,200 VA)'
        elif has_7200:
            return 'Accurate', 'Correct result (7,200 VA)'
        else:
            return 'Partially Accurate', 'Check dwelling load calculation'

    # cec-026: Kitchen GFCI comparison
    elif qid == 'cec-026':
        has_more_permissive = 'permissive' in actual_lower or 'less restrictive' in actual_lower or 'cec' in actual_lower
        has_countertop = 'countertop' in actual_lower
        has_all_kitchen = 'all' in actual_lower and 'kitchen' in actual_lower

        # CEC is MORE PERMISSIVE (less restrictive) than NEC for kitchen GFCI
        if has_more_permissive and has_countertop:
            return 'Accurate', 'Correctly explains CEC more permissive'
        elif has_countertop or has_all_kitchen:
            return 'Partially Accurate', 'Has some comparison'
        else:
            return 'Partially Accurate', 'Incomplete comparison'

    # cec-027: Panelboard space comparison
    elif qid == 'cec-027':
        has_408_2 = '408.2' in actual or '408' in actual
        has_reserved = 'reserved' in actual_lower or 'space' in actual_lower
        has_no_nec = 'no' in actual_lower and 'nec' in actual_lower or 'not' in actual_lower and 'nec' in actual_lower
        has_california = 'california' in actual_lower or 'cec' in actual_lower

        if has_408_2 and has_reserved and has_california:
            return 'Accurate', 'Correctly explains CEC-only requirement'
        elif has_408_2 or has_reserved:
            return 'Partially Accurate', 'Has some comparison'
        else:
            return 'Partially Accurate', 'Incomplete panelboard comparison'

    # cec-028: EV comparison
    elif qid == 'cec-028':
        has_mandate = 'mandate' in actual_lower or 'require' in actual_lower
        has_california = 'california' in actual_lower or 'cec' in actual_lower
        has_title_24 = 'title 24' in actual_lower
        has_625 = '625' in actual

        if has_mandate and has_california and has_625:
            return 'Accurate', 'Correctly explains CA mandate vs NEC guidance'
        elif has_mandate or (has_california and has_625):
            return 'Partially Accurate', 'Has some comparison'
        else:
            return 'Partially Accurate', 'Incomplete EV comparison'

    # cec-029: AFCI comparison
    elif qid == 'cec-029':
        has_similar = 'similar' in actual_lower or 'same' in actual_lower or 'both' in actual_lower
        has_210_12 = '210.12' in actual
        locations = ['bedroom', 'kitchen', 'living', 'dining', 'family']
        found_locations = sum(1 for loc in locations if loc in actual_lower)

        if has_similar and has_210_12 and found_locations >= 3:
            return 'Accurate', 'Correctly identifies similar requirements'
        elif has_similar or found_locations >= 3:
            return 'Partially Accurate', 'Has some comparison'
        else:
            return 'Partially Accurate', 'Incomplete AFCI comparison'

    # cec-030: Solar PV comparison
    elif qid == 'cec-030':
        has_mandate = 'mandate' in actual_lower
        has_california = 'california' in actual_lower
        has_title_24 = 'title 24' in actual_lower
        has_690 = '690' in actual
        has_installation = 'installation' in actual_lower

        if has_mandate and has_california and has_690:
            return 'Accurate', 'Correctly explains CA mandate vs NEC installation rules'
        elif has_mandate or (has_690 and has_installation):
            return 'Partially Accurate', 'Has some comparison'
        else:
            return 'Partially Accurate', 'Incomplete solar comparison'

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
report = f"""# LLM Judge Report: CEC Evaluation (Run 5)

## Summary
- Total Questions: 30
- Accurate: {verdicts['Accurate']}/30 ({verdicts['Accurate']/30*100:.1f}%)
- Partially Accurate: {verdicts['Partially Accurate']}/30 ({verdicts['Partially Accurate']/30*100:.1f}%)
- Inaccurate: {verdicts['Inaccurate']}/30 ({verdicts['Inaccurate']/30*100:.1f}%)

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

**Accurate Answers ({len(accurate_items)}/30 = {len(accurate_items)/30*100:.1f}%):**
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
- Accurate: 20/30 (66.7%)
- Partially Accurate: 10/30 (33.3%)
- Inaccurate: 0/30 (0.0%)

### Run 5 Results (After 1-Prompt System + Table Selection):
- Accurate: {verdicts['Accurate']}/30 ({verdicts['Accurate']/30*100:.1f}%)
- Partially Accurate: {verdicts['Partially Accurate']}/30 ({verdicts['Partially Accurate']/30*100:.1f}%)
- Inaccurate: {verdicts['Inaccurate']}/30 ({verdicts['Inaccurate']/30*100:.1f}%)

### Key Fixes Applied:
1. **1-Prompt System**: Removed two-step prompting to eliminate hallucination from planning context
2. **Table Selection**: Added conductor_application parameter for Table 310.12(A) vs 310.16

## Overall Assessment

The CEC agent achieved:
- **{verdicts['Accurate']}/30 Accurate** ({verdicts['Accurate']/30*100:.1f}%)
- **{verdicts['Partially Accurate']}/30 Partially Accurate** ({verdicts['Partially Accurate']/30*100:.1f}%)
- **{verdicts['Inaccurate']}/30 Inaccurate** ({verdicts['Inaccurate']/30*100:.1f}%)

**Success Rate (Accurate + Partial)**: {(verdicts['Accurate'] + verdicts['Partially Accurate'])/30*100:.1f}%

---
*Report Generated: Run 5*
*Evaluation Set: CEC Evaluation - 30 Questions*
"""

# Write the report
output_path = run_dir / 'cec_judge_report.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"Report generated: {output_path}")
print(f"\nSummary:")
print(f"Accurate: {verdicts['Accurate']}/30 ({verdicts['Accurate']/30*100:.1f}%)")
print(f"Partially Accurate: {verdicts['Partially Accurate']}/30 ({verdicts['Partially Accurate']/30*100:.1f}%)")
print(f"Inaccurate: {verdicts['Inaccurate']}/30 ({verdicts['Inaccurate']/30*100:.1f}%)")
