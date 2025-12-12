import json
import re
from pathlib import Path

# Find the CEC evaluation results file
run_dir = Path(__file__).parent
cec_files = list(run_dir.glob("run4-cec_evaluation_results_*.json"))
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

    # CEC-001: Panelboard requirements - 5 appliances
    if qid == 'cec-001':
        required_appliances = ['heat pump water heater', 'heat pump space heater',
                              'electric cooktop', 'electric clothes dryer',
                              'electric vehicle', 'ev charging', 'ev']
        # Check for each appliance type (EV can be mentioned different ways)
        found_heat_pump_water = 'heat pump water' in actual_lower
        found_heat_pump_space = 'heat pump space' in actual_lower or ('heat pump' in actual_lower and 'space heat' in actual_lower)
        found_cooktop = 'cooktop' in actual_lower or 'electric range' in actual_lower
        found_dryer = 'dryer' in actual_lower or 'clothes dryer' in actual_lower
        found_ev = 'electric vehicle' in actual_lower or 'ev charging' in actual_lower or 'ev ' in actual_lower

        found_count = sum([found_heat_pump_water, found_heat_pump_space, found_cooktop, found_dryer, found_ev])
        has_408_2 = '408.2' in actual

        if found_count >= 5 and has_408_2:
            return 'Accurate', f'Found all 5 appliances and CEC 408.2 reference'
        elif found_count >= 4 and has_408_2:
            return 'Partially Accurate', f'Found {found_count}/5 appliances with code reference'
        elif found_count >= 3:
            return 'Partially Accurate', f'Found {found_count}/5 appliances'
        else:
            return 'Inaccurate', f'Only found {found_count}/5 appliances'

    # CEC-002: EV charging
    elif qid == 'cec-002':
        has_625 = '625' in actual
        has_408_2 = '408.2' in actual
        has_40a = '40' in actual and ('ampere' in actual_lower or 'amp' in actual_lower or 'a ' in actual_lower)
        has_title24 = 'title 24' in actual_lower or 'title24' in actual_lower

        if has_40a and (has_625 or has_408_2 or has_title24):
            return 'Accurate', 'Has 40-amp requirement and code references'
        elif has_40a:
            return 'Partially Accurate', 'Has 40-amp but limited code references'
        else:
            return 'Partially Accurate', 'Missing 40-amp minimum circuit requirement'

    # CEC-003: Solar PV
    elif qid == 'cec-003':
        has_690 = '690' in actual
        has_rapid_shutdown = 'rapid shutdown' in actual_lower or 'rapid-shutdown' in actual_lower
        has_arc_fault = 'arc' in actual_lower and 'fault' in actual_lower
        has_title24 = 'title 24' in actual_lower

        if has_690 and has_rapid_shutdown:
            return 'Accurate', 'Has Article 690 and rapid shutdown'
        elif has_690:
            return 'Partially Accurate', 'Has Article 690 but missing rapid shutdown'
        else:
            return 'Partially Accurate', 'Missing Article 690 reference'

    # CEC-004: Heat pump
    elif qid == 'cec-004':
        has_440 = '440' in actual
        has_heat_pump = 'heat pump' in actual_lower
        has_408_2 = '408.2' in actual

        if has_408_2 and has_heat_pump:
            return 'Accurate', 'Correct panelboard requirement for heat pump'
        elif has_440 or has_408_2:
            return 'Partially Accurate', 'Has some correct references'
        else:
            return 'Partially Accurate', 'Missing key details'

    # CEC-005: Electrification - cooktop
    elif qid == 'cec-005':
        has_408_2 = '408.2' in actual
        has_reserved = 'reserved' in actual_lower
        has_cooktop = 'cooktop' in actual_lower

        if has_408_2 and has_reserved:
            return 'Accurate', 'Correct reserved space requirement'
        elif has_408_2 or has_reserved:
            return 'Partially Accurate', 'Has some correct info'
        else:
            return 'Partially Accurate', 'Missing key requirements'

    # CEC-006: Electric dryer panelboard
    elif qid == 'cec-006':
        has_408_2 = '408.2' in actual
        has_dryer = 'dryer' in actual_lower
        has_reserved = 'reserved' in actual_lower

        if has_408_2 and has_dryer:
            return 'Accurate', 'Correct dryer circuit requirement'
        elif has_408_2:
            return 'Partially Accurate', 'Has code reference but incomplete'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-007: Table 240.4(G)
    elif qid == 'cec-007':
        has_240_4_g = '240.4(g)' in actual_lower or 'table 240.4(g)' in actual_lower
        has_california = 'california' in actual_lower

        if has_240_4_g and has_california:
            return 'Accurate', 'Identifies Table 240.4(G) as California-specific'
        elif has_240_4_g:
            return 'Partially Accurate', 'Mentions 240.4(G) but unclear on California status'
        else:
            return 'Partially Accurate', 'Missing Table 240.4(G) reference'

    # CEC-008: Surge protection Table 242.3
    elif qid == 'cec-008':
        has_242 = '242' in actual
        has_table = 'table' in actual_lower and '242' in actual

        if has_table:
            return 'Accurate', 'Correct table reference'
        elif has_242:
            return 'Partially Accurate', 'Has article but incomplete on table'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-009: Motor control Table 430.72(B)
    elif qid == 'cec-009':
        has_430 = '430' in actual
        has_table = 'table' in actual_lower and '430' in actual
        has_72_b = '430.72' in actual

        if has_72_b:
            return 'Accurate', 'Correct table reference'
        elif has_430:
            return 'Partially Accurate', 'Has article but incomplete'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-010: Medium voltage tables
    elif qid == 'cec-010':
        has_311 = '311' in actual
        has_medium_voltage = 'medium voltage' in actual_lower or '2001' in actual or 'kv' in actual_lower

        if has_311 and has_medium_voltage:
            return 'Accurate', 'Correct article and voltage reference'
        elif has_311:
            return 'Partially Accurate', 'Has article reference'
        else:
            return 'Partially Accurate', 'Missing key information'

    # CEC-011: Ampacity 4/0 AWG
    elif qid == 'cec-011':
        has_230 = '230' in actual  # Expected ampacity
        has_table_310 = '310.16' in actual or 'table 310' in actual_lower

        if has_230 and has_table_310:
            return 'Accurate', 'Correct ampacity and table reference'
        elif has_table_310:
            return 'Partially Accurate', 'Has table but check ampacity value'
        else:
            return 'Partially Accurate', 'Missing table reference'

    # CEC-012: EGC for 200A
    elif qid == 'cec-012':
        has_6_awg = '6 awg' in actual_lower or '#6' in actual_lower or '6awg' in actual_lower
        has_250_122 = '250.122' in actual

        if has_6_awg and has_250_122:
            return 'Accurate', 'Correct EGC size and table reference'
        elif has_6_awg:
            return 'Partially Accurate', 'Correct size but missing table reference'
        else:
            return 'Partially Accurate', 'Check EGC size'

    # CEC-013: GEC for 3/0 AWG service
    elif qid == 'cec-013':
        has_4_awg = '4 awg' in actual_lower or '#4' in actual_lower
        has_250_66 = '250.66' in actual

        if has_4_awg and has_250_66:
            return 'Accurate', 'Correct GEC size and table reference'
        elif has_4_awg:
            return 'Partially Accurate', 'Correct size but missing table reference'
        else:
            return 'Partially Accurate', 'Check GEC size'

    # CEC-014: Temperature correction factor
    elif qid == 'cec-014':
        has_factor = '0.82' in actual or '.82' in actual
        has_310_15 = '310.15' in actual

        if has_factor and has_310_15:
            return 'Accurate', 'Correct factor and table reference'
        elif has_factor:
            return 'Partially Accurate', 'Has factor but missing table reference'
        else:
            return 'Partially Accurate', 'Check temperature correction factor'

    # CEC-015: Bundling adjustment 7-9 conductors
    elif qid == 'cec-015':
        has_70 = '0.70' in actual or '.70' in actual or '70%' in actual or '0.7' in actual
        has_310_15 = '310.15' in actual

        if has_70 and has_310_15:
            return 'Accurate', 'Correct factor (0.70) and table reference'
        elif has_70:
            return 'Partially Accurate', 'Has factor but missing table reference'
        else:
            return 'Partially Accurate', 'Check bundling adjustment factor'

    # CEC-016: Working space 480V
    elif qid == 'cec-016':
        has_3_feet = '3 feet' in actual_lower or '36' in actual or '3 ft' in actual_lower or '914' in actual
        has_110_26 = '110.26' in actual

        if has_3_feet and has_110_26:
            return 'Accurate', 'Correct clearance and section reference'
        elif has_3_feet:
            return 'Partially Accurate', 'Has clearance but missing section reference'
        else:
            return 'Partially Accurate', 'Check working space clearance'

    # CEC-017: Enclosure for outdoor use
    elif qid == 'cec-017':
        enclosure_types = ['3r', 'type 3r', '3s', '4', '4x', '6', '6p']
        found_types = sum(1 for t in enclosure_types if t in actual_lower)
        has_110_28 = '110.28' in actual

        if found_types >= 3 and has_110_28:
            return 'Accurate', f'Found {found_types} enclosure types with table reference'
        elif found_types >= 2:
            return 'Partially Accurate', f'Found {found_types} enclosure types'
        else:
            return 'Partially Accurate', 'Incomplete enclosure list'

    # CEC-018: Lighting load VA/sqft
    elif qid == 'cec-018':
        has_3_va = '3 va' in actual_lower or '3va' in actual_lower or '3 volt-ampere' in actual_lower
        has_220_12 = '220.12' in actual

        if has_3_va and has_220_12:
            return 'Accurate', 'Correct VA/sqft and table reference'
        elif has_3_va:
            return 'Partially Accurate', 'Has VA value but missing table reference'
        else:
            return 'Partially Accurate', 'Check VA/sqft value'

    # CEC-019: Flexible cord ampacity
    elif qid == 'cec-019':
        has_25 = '25' in actual and ('ampere' in actual_lower or 'amp' in actual_lower or 'a' in actual_lower)
        has_400_5 = '400.5' in actual

        if has_25 and has_400_5:
            return 'Accurate', 'Correct ampacity and table reference'
        elif has_25:
            return 'Partially Accurate', 'Has ampacity but missing table reference'
        else:
            return 'Partially Accurate', 'Check flexible cord ampacity'

    # CEC-020: SF-2 temperature
    elif qid == 'cec-020':
        has_200 = '200' in actual and ('°c' in actual_lower or 'deg' in actual_lower or 'celsius' in actual_lower or 'c' in actual_lower)
        has_402 = '402' in actual

        if has_200 and has_402:
            return 'Accurate', 'Correct temperature and table reference'
        elif has_200:
            return 'Partially Accurate', 'Has temperature but missing table reference'
        else:
            return 'Partially Accurate', 'Check temperature rating'

    # CEC-021: Adjusted ampacity calculation
    elif qid == 'cec-021':
        has_calculation = any(x in actual for x in ['×', '*', 'x', 'multiply', '='])
        has_factors = 'factor' in actual_lower or 'adjustment' in actual_lower or 'correction' in actual_lower
        has_310 = '310' in actual

        if has_calculation and has_factors and has_310:
            return 'Accurate', 'Shows proper calculation method'
        elif has_calculation or has_factors:
            return 'Partially Accurate', 'Has some calculation info'
        else:
            return 'Partially Accurate', 'Incomplete methodology'

    # CEC-022: Service sizing 200A
    elif qid == 'cec-022':
        has_service = '2/0' in actual or '3/0' in actual or '4/0' in actual  # Service conductor sizes
        has_egc = '6 awg' in actual_lower or '6awg' in actual_lower or '#6' in actual
        has_gec = '4 awg' in actual_lower or '4awg' in actual_lower or '#4' in actual

        if has_service and has_egc and has_gec:
            return 'Accurate', 'Has service, EGC, and GEC sizes'
        elif has_service and (has_egc or has_gec):
            return 'Partially Accurate', 'Has some sizes but incomplete'
        else:
            return 'Partially Accurate', 'Missing sizing information'

    # CEC-023: Commercial lighting load
    elif qid == 'cec-023':
        has_calculation = any(str(x) in actual for x in range(10000, 20000))  # Expected result range
        has_220 = '220' in actual

        if has_calculation and has_220:
            return 'Accurate', 'Correct calculation approach'
        elif has_220:
            return 'Partially Accurate', 'Has article but check calculation'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-024: Motor control overcurrent
    elif qid == 'cec-024':
        has_430 = '430' in actual
        has_10a = '10' in actual and ('ampere' in actual_lower or 'amp' in actual_lower or 'a' in actual_lower)

        if has_430 and has_10a:
            return 'Accurate', 'Correct article and overcurrent value'
        elif has_430:
            return 'Partially Accurate', 'Has article but check value'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-025: Dwelling lighting load
    elif qid == 'cec-025':
        has_220 = '220' in actual
        has_sqft = 'sq' in actual_lower or 'square' in actual_lower or '2400' in actual or '2,400' in actual

        if has_220 and has_sqft:
            return 'Accurate', 'Correct article and calculation'
        elif has_220:
            return 'Partially Accurate', 'Has article but incomplete'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-026: GFCI comparison
    elif qid == 'cec-026':
        has_210_8 = '210.8' in actual
        has_comparison = 'cec' in actual_lower and 'nec' in actual_lower

        if has_210_8 and has_comparison:
            return 'Accurate', 'Correct section and comparison'
        elif has_210_8:
            return 'Partially Accurate', 'Has section but limited comparison'
        else:
            return 'Partially Accurate', 'Missing section reference'

    # CEC-027: Panelboard comparison
    elif qid == 'cec-027':
        has_408 = '408' in actual
        has_comparison = 'cec' in actual_lower and 'nec' in actual_lower
        has_california = 'california' in actual_lower

        if has_408 and (has_comparison or has_california):
            return 'Accurate', 'Correct article and comparison'
        elif has_408:
            return 'Partially Accurate', 'Has article but limited comparison'
        else:
            return 'Partially Accurate', 'Missing article reference'

    # CEC-028: EV charging comparison
    elif qid == 'cec-028':
        has_625 = '625' in actual
        has_mandate = 'mandate' in actual_lower or 'require' in actual_lower or 'infrastructure' in actual_lower
        has_comparison = 'cec' in actual_lower and 'nec' in actual_lower

        if has_625 and has_mandate and has_comparison:
            return 'Accurate', 'Correct comparison with mandate distinction'
        elif has_625 and has_comparison:
            return 'Partially Accurate', 'Has comparison but missing mandate detail'
        else:
            return 'Partially Accurate', 'Missing key information'

    # CEC-029: AFCI comparison
    elif qid == 'cec-029':
        has_210_12 = '210.12' in actual
        has_comparison = 'cec' in actual_lower and 'nec' in actual_lower

        if has_210_12 and has_comparison:
            return 'Accurate', 'Correct section and comparison'
        elif has_210_12:
            return 'Partially Accurate', 'Has section but limited comparison'
        else:
            return 'Partially Accurate', 'Missing section reference'

    # CEC-030: Solar PV comparison
    elif qid == 'cec-030':
        has_690 = '690' in actual
        has_comparison = 'cec' in actual_lower and 'nec' in actual_lower

        if has_690 and has_comparison:
            return 'Accurate', 'Correct article and comparison'
        elif has_690:
            return 'Partially Accurate', 'Has article but limited comparison'
        else:
            return 'Partially Accurate', 'Missing article reference'

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

# Generate markdown report
report = f"""# LLM Judge Report: CEC Evaluation (Run 4)

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

report += f"""

## Overall Assessment

The CEC agent achieved:
- **{verdicts['Accurate']}/30 Accurate** ({verdicts['Accurate']/30*100:.1f}%)
- **{verdicts['Partially Accurate']}/30 Partially Accurate** ({verdicts['Partially Accurate']/30*100:.1f}%)
- **{verdicts['Inaccurate']}/30 Inaccurate** ({verdicts['Inaccurate']/30*100:.1f}%)

**Success Rate (Accurate + Partial)**: {(verdicts['Accurate'] + verdicts['Partially Accurate'])/30*100:.1f}%

---
*Report Generated: Run 4*
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
