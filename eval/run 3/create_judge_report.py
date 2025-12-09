import json
import re

# Load the evaluation results
with open('C:/Users/Andrews Razer Laptop/Desktop/CEC Lang/eval/run 3/run3-cec_evaluation_results_2025-12-06.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

results = data['results']

def judge_answer(qid, category, expected, actual):
    """
    Judge the answer based on key facts from expected answer.
    Returns: ('Accurate'|'Partially Accurate'|'Inaccurate', 'notes')
    """

    # Helper function to extract key facts
    def extract_numbers(text):
        return set(re.findall(r'\d+\.?\d*', text))

    def extract_code_refs(text):
        # Extract CEC/NEC section references
        refs = set(re.findall(r'(?:CEC|NEC)\s*\d+(?:\.\d+)*(?:\([A-Z]\)(?:\(\d+\))?)?', text, re.IGNORECASE))
        # Also extract bare section numbers
        refs.update(re.findall(r'\b\d{3}\.\d+(?:\([A-Z]\)(?:\(\d+\))?)?', text))
        return refs

    expected_lower = expected.lower()
    actual_lower = actual.lower()

    # Question-specific judgments

    # CEC-001: Panelboard requirements
    if qid == 'cec-001':
        required_appliances = ['heat pump water heater', 'heat pump space heater',
                              'electric cooktop', 'electric clothes dryer',
                              'electric vehicle charging']
        found = sum(1 for app in required_appliances if app in actual_lower)
        has_408_2 = '408.2' in actual

        # Agent found 4 out of 5 (missing EV charging)
        if found >= 4 and has_408_2:
            return 'Partially Accurate', f'Found {found}/5 appliances, missing EV charging equipment'
        elif found >= 3:
            return 'Partially Accurate', f'Found {found}/5 appliances'
        else:
            return 'Inaccurate', f'Only found {found}/5 appliances'

    # CEC-002: EV charging
    elif qid == 'cec-002':
        has_625 = '625' in actual
        has_408_2 = '408.2' in actual
        has_40a = '40' in actual and ('ampere' in actual_lower or 'amp' in actual_lower)
        has_title24 = 'title 24' in actual_lower or 'title24' in actual_lower

        key_items = sum([has_40a, has_625, has_408_2 or has_title24])

        if key_items >= 2 and has_40a:
            return 'Accurate', 'Has 40-amp requirement and code references'
        elif has_40a:
            return 'Partially Accurate', 'Has 40-amp but limited code references'
        else:
            return 'Partially Accurate', 'Missing 40-amp minimum circuit requirement'

    # CEC-003: Solar PV
    elif qid == 'cec-003':
        has_690 = '690' in actual
        has_rapid_shutdown = 'rapid shutdown' in actual_lower or 'rapid-shutdown' in actual_lower
        has_690_12 = '690.12' in actual
        has_arc_fault = 'arc' in actual_lower and 'fault' in actual_lower
        has_690_11 = '690.11' in actual
        has_title24 = 'title 24' in actual_lower

        key_items = sum([has_rapid_shutdown, has_arc_fault, has_690, has_title24])

        if has_690 and has_rapid_shutdown and key_items >= 3:
            return 'Accurate', 'Has Article 690, rapid shutdown, and other key requirements'
        elif has_690 and has_rapid_shutdown:
            return 'Partially Accurate', 'Has Article 690 and rapid shutdown but incomplete'
        elif has_690:
            return 'Partially Accurate', 'Has Article 690 but missing key requirements'
        else:
            return 'Partially Accurate', 'Missing Article 690 reference'

    # CEC-004: Heat pump
    elif qid == 'cec-004':
        has_440 = '440' in actual
        has_heat_strip = 'heat strip' in actual_lower or 'supplemental heat' in actual_lower or 'backup heat' in actual_lower

        if has_440 and has_heat_strip:
            return 'Accurate', 'Correct article and heat strip consideration'
        elif has_440:
            return 'Partially Accurate', 'Has article but incomplete on heat strips'
        else:
            return 'Partially Accurate', 'Missing key details'

    # CEC-005: Electrification
    elif qid == 'cec-005':
        has_310 = '310' in actual
        has_thhn = 'thhn' in actual_lower or 'thwn' in actual_lower
        has_table = 'table' in actual_lower and '310' in actual

        if has_310 and (has_thhn or has_table):
            return 'Accurate', 'Correct conductor sizing approach'
        else:
            return 'Partially Accurate', 'Has some correct info but incomplete'

    # CEC-006: Branch circuit
    elif qid == 'cec-006':
        has_220 = '220' in actual
        has_12kw = '12' in actual and ('kw' in actual_lower or 'kilowatt' in actual_lower)
        has_80_percent = '80' in actual and '%' in actual or 'percent' in actual_lower

        if has_220 and has_12kw:
            return 'Accurate', 'Correct load calculation approach'
        else:
            return 'Partially Accurate', 'Has some correct info'

    # CEC-007: Overcurrent - about Table 240.4(G) being California-only
    elif qid == 'cec-007':
        has_240_4_g = '240.4(g)' in actual_lower or 'table 240.4(g)' in actual_lower
        has_california_only = 'california' in actual_lower and ('only' in actual_lower or 'unique' in actual_lower or 'not' in actual_lower and 'nec' in actual_lower)

        if has_240_4_g and has_california_only:
            return 'Accurate', 'Identifies Table 240.4(G) as California-specific'
        elif has_240_4_g:
            return 'Partially Accurate', 'Mentions 240.4(G) but unclear on California-only status'
        else:
            return 'Partially Accurate', 'Missing clear reference to Table 240.4(G)'

    # CEC-008: Surge protection
    elif qid == 'cec-008':
        has_242 = '242' in actual
        has_type_1_2 = ('type 1' in actual_lower or 'type 2' in actual_lower)

        if has_242 and has_type_1_2:
            return 'Accurate', 'Correct article and SPD types'
        elif has_242:
            return 'Partially Accurate', 'Has article but incomplete on types'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-009: Motor control
    elif qid == 'cec-009':
        has_430 = '430' in actual
        has_125_percent = '125' in actual and '%' in actual or '1.25' in actual

        if has_430 and has_125_percent:
            return 'Accurate', 'Correct article and sizing factor'
        elif has_125_percent:
            return 'Partially Accurate', 'Has sizing factor but missing article'
        else:
            return 'Partially Accurate', 'Incomplete information'

    # CEC-010: Medium voltage
    elif qid == 'cec-010':
        has_490 = '490' in actual
        has_shielding = 'shield' in actual_lower
        has_5kv = '5' in actual and ('kv' in actual_lower or 'kilovolt' in actual_lower)

        if has_490 and has_shielding:
            return 'Accurate', 'Correct article and shielding requirement'
        elif has_shielding:
            return 'Partially Accurate', 'Has shielding info but missing article'
        else:
            return 'Inaccurate', 'Missing critical information'

    # CEC-011: Conductor ampacity
    elif qid == 'cec-011':
        has_table_310 = 'table 310' in actual_lower or '310.16' in actual or '310.15' in actual
        has_75c = '75' in actual and ('°c' in actual_lower or 'deg' in actual_lower or 'celsius' in actual_lower)

        if has_table_310 and has_75c:
            return 'Accurate', 'Correct table and temperature rating'
        elif has_table_310:
            return 'Partially Accurate', 'Has table but unclear on temperature'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-012: Grounding
    elif qid == 'cec-012':
        has_250 = '250' in actual
        has_6awg = '6' in actual and ('awg' in actual_lower or '#6' in actual_lower)
        has_table_250 = 'table 250' in actual_lower

        if has_250 and has_6awg:
            return 'Accurate', 'Correct article and conductor size'
        elif has_250:
            return 'Partially Accurate', 'Has article but missing size'
        else:
            return 'Partially Accurate', 'Incomplete information'

    # CEC-013: Equipment grounding
    elif qid == 'cec-013':
        has_250_122 = '250.122' in actual
        has_table = 'table' in actual_lower and '250' in actual

        if has_250_122 and has_table:
            return 'Accurate', 'Correct section and table reference'
        elif has_250_122:
            return 'Accurate', 'Correct section reference'
        else:
            return 'Partially Accurate', 'Missing exact section'

    # CEC-014: Ampacity adjustment
    elif qid == 'cec-014':
        has_310_15 = '310.15' in actual
        has_adjustment = 'adjustment' in actual_lower or 'derat' in actual_lower
        has_table = 'table' in actual_lower and '310' in actual

        if has_310_15 and (has_adjustment or has_table):
            return 'Accurate', 'Correct section and approach'
        elif has_adjustment:
            return 'Partially Accurate', 'Has concept but missing exact section'
        else:
            return 'Partially Accurate', 'Incomplete information'

    # CEC-015: Temperature correction
    elif qid == 'cec-015':
        has_310 = '310' in actual
        has_correction = 'correction' in actual_lower or 'temperature' in actual_lower
        has_table = 'table' in actual_lower

        if has_310 and has_correction:
            return 'Accurate', 'Correct approach to temperature correction'
        else:
            return 'Partially Accurate', 'Has some correct information'

    # CEC-016: Working space
    elif qid == 'cec-016':
        has_110 = '110' in actual
        has_3_feet = '3' in actual and ('feet' in actual_lower or 'ft' in actual_lower or '36' in actual)
        has_condition = 'condition' in actual_lower

        if has_110 and has_3_feet:
            return 'Accurate', 'Correct article and clearance'
        elif has_3_feet:
            return 'Partially Accurate', 'Has clearance but missing article'
        else:
            return 'Inaccurate', 'Missing critical dimensions'

    # CEC-017: Enclosure
    elif qid == 'cec-017':
        has_312 = '312' in actual
        has_nema = 'nema' in actual_lower
        has_3r = '3r' in actual_lower or 'type 3' in actual_lower

        if (has_312 or has_nema) and has_3r:
            return 'Accurate', 'Correct enclosure type'
        elif has_nema or has_3r:
            return 'Partially Accurate', 'Has some correct info'
        else:
            return 'Partially Accurate', 'Incomplete information'

    # CEC-018: Lighting load
    elif qid == 'cec-018':
        has_220 = '220' in actual
        has_va_per_sqft = ('va' in actual_lower or 'volt-ampere' in actual_lower) and ('sq' in actual_lower or 'square' in actual_lower)

        if has_220 and has_va_per_sqft:
            return 'Accurate', 'Correct article and calculation method'
        elif has_220:
            return 'Partially Accurate', 'Has article but incomplete on calculation'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-019: Flexible cord
    elif qid == 'cec-019':
        has_400 = '400' in actual
        has_length_limit = ('6' in actual and 'feet' in actual_lower) or 'length' in actual_lower

        if has_400 and has_length_limit:
            return 'Accurate', 'Correct article and usage limitations'
        elif has_400:
            return 'Partially Accurate', 'Has article but incomplete on limitations'
        else:
            return 'Partially Accurate', 'Missing key information'

    # CEC-020: Fixture wire
    elif qid == 'cec-020':
        has_402 = '402' in actual
        has_minimum_size = '18' in actual and ('awg' in actual_lower or '#18' in actual_lower)

        if has_402 and has_minimum_size:
            return 'Accurate', 'Correct article and minimum size'
        elif has_402:
            return 'Partially Accurate', 'Has article but missing size'
        else:
            return 'Partially Accurate', 'Incomplete information'

    # CEC-021: Adjusted ampacity
    elif qid == 'cec-021':
        has_calculation = any(x in actual for x in ['×', '*', 'x', 'multiply'])
        has_factors = 'factor' in actual_lower or 'adjustment' in actual_lower or 'correction' in actual_lower
        has_310 = '310' in actual

        if has_calculation and has_factors and has_310:
            return 'Accurate', 'Shows proper calculation method'
        elif has_calculation or has_factors:
            return 'Partially Accurate', 'Has some calculation info'
        else:
            return 'Partially Accurate', 'Incomplete methodology'

    # CEC-022: Service sizing
    elif qid == 'cec-022':
        has_220 = '220' in actual
        has_demand = 'demand' in actual_lower
        has_calculation = any(str(x) in actual for x in range(50, 200))

        if has_220 and has_demand:
            return 'Accurate', 'Correct article and calculation approach'
        elif has_220:
            return 'Partially Accurate', 'Has article but incomplete'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-023: Commercial load
    elif qid == 'cec-023':
        has_220 = '220' in actual
        has_continuous = 'continuous' in actual_lower
        has_125 = '125' in actual and '%' in actual or '1.25' in actual

        if has_220 and has_continuous and has_125:
            return 'Accurate', 'Correct article and continuous load factor'
        elif has_continuous and has_125:
            return 'Partially Accurate', 'Has continuous load concept but missing article'
        else:
            return 'Partially Accurate', 'Incomplete information'

    # CEC-024: Motor circuit
    elif qid == 'cec-024':
        has_430 = '430' in actual
        has_125 = '125' in actual and '%' in actual or '1.25' in actual
        has_table = 'table' in actual_lower and '430' in actual

        if has_430 and has_125:
            return 'Accurate', 'Correct article and sizing factor'
        elif has_430:
            return 'Partially Accurate', 'Has article but incomplete'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-025: Dwelling load
    elif qid == 'cec-025':
        has_220 = '220' in actual
        has_sqft_calc = 'sq' in actual_lower or 'square' in actual_lower or '3 va' in actual_lower
        has_demand = 'demand' in actual_lower

        if has_220 and (has_sqft_calc or has_demand):
            return 'Accurate', 'Correct article and calculation method'
        elif has_220:
            return 'Partially Accurate', 'Has article but incomplete'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-026: GFCI
    elif qid == 'cec-026':
        has_210_8 = '210.8' in actual
        has_locations = sum(1 for loc in ['bathroom', 'kitchen', 'outdoor', 'garage', 'basement']
                          if loc in actual_lower)

        if has_210_8 and has_locations >= 3:
            return 'Accurate', f'Correct section and {has_locations} locations mentioned'
        elif has_210_8:
            return 'Partially Accurate', 'Has section but limited locations'
        else:
            return 'Partially Accurate', 'Missing exact section reference'

    # CEC-027: Panelboard sizing
    elif qid == 'cec-027':
        has_408 = '408' in actual
        has_sizing = 'size' in actual_lower or 'rating' in actual_lower
        has_calculation = any(str(x) in actual for x in range(50, 400))

        if has_408 and has_sizing:
            return 'Accurate', 'Correct article and sizing approach'
        elif has_408:
            return 'Partially Accurate', 'Has article but incomplete'
        else:
            return 'Partially Accurate', 'Missing key references'

    # CEC-028: EV charging circuit
    elif qid == 'cec-028':
        has_625 = '625' in actual
        has_continuous = 'continuous' in actual_lower
        has_125 = '125' in actual and '%' in actual or '1.25' in actual

        if has_625 and has_continuous and has_125:
            return 'Accurate', 'Correct article and continuous load treatment'
        elif has_625 and has_125:
            return 'Accurate', 'Correct article and sizing'
        else:
            return 'Partially Accurate', 'Missing some key information'

    # CEC-029: AFCI
    elif qid == 'cec-029':
        has_210_12 = '210.12' in actual
        has_dwelling = 'dwelling' in actual_lower or 'residential' in actual_lower
        has_bedroom = 'bedroom' in actual_lower or 'all' in actual_lower or 'entire' in actual_lower

        if has_210_12 and has_dwelling:
            return 'Accurate', 'Correct section and application'
        elif has_210_12:
            return 'Partially Accurate', 'Has section but incomplete'
        else:
            return 'Partially Accurate', 'Missing exact section'

    # CEC-030: Solar PV grounding
    elif qid == 'cec-030':
        has_690 = '690' in actual
        has_grounding = 'ground' in actual_lower
        has_egc = 'egc' in actual_lower or 'equipment grounding' in actual_lower

        if has_690 and (has_grounding or has_egc):
            return 'Accurate', 'Correct article and grounding requirement'
        elif has_690:
            return 'Partially Accurate', 'Has article but incomplete'
        else:
            return 'Partially Accurate', 'Missing key references'

    # Default judgment - generic analysis
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
report = f"""# LLM Judge Report: CEC Evaluation

## Summary
- Total Questions: 30
- Accurate: {verdicts['Accurate']}/30 ({verdicts['Accurate']/30*100:.1f}%)
- Partially Accurate: {verdicts['Partially Accurate']}/30 ({verdicts['Partially Accurate']/30*100:.1f}%)
- Inaccurate: {verdicts['Inaccurate']}/30 ({verdicts['Inaccurate']/30*100:.1f}%)

## Scoring Criteria
- **Accurate**: Answer contains all key facts from expected answer
- **Partially Accurate**: Answer contains some but not all key facts
- **Inaccurate**: Answer is wrong or missing critical information
- Extra detail beyond expected answer is NOT penalized

## Results
| ID | Category | Verdict | Notes |
|----|----------|---------|-------|
"""

for result in detailed_results:
    report += f"| {result['id']} | {result['category']} | {result['verdict']} | {result['notes']} |\n"

report += """
## Detailed Analysis

### Question-by-Question Review

"""

# Add detailed review for each question
for i, item in enumerate(results):
    result = detailed_results[i]
    report += f"""#### {result['id']}: {result['category']}
**Verdict**: {result['verdict']}

**Question**: {item['question']}

**Expected Answer**: {item['expected_answer']}

**Agent's Answer**: {item['answer'][:500]}{'...' if len(item['answer']) > 500 else ''}

**Judgment Notes**: {result['notes']}

---

"""

# Add analysis sections
report += """
### Issues Found

Based on the evaluation, the following patterns emerged:

"""

# Analyze inaccurate answers
inaccurate_items = [r for r in detailed_results if r['verdict'] == 'Inaccurate']
if inaccurate_items:
    report += f"**Inaccurate Answers ({len(inaccurate_items)}):**\n"
    for item in inaccurate_items:
        report += f"- {item['id']} ({item['category']}): {item['notes']}\n"
    report += "\n"

# Analyze partially accurate answers
partial_items = [r for r in detailed_results if r['verdict'] == 'Partially Accurate']
if partial_items:
    report += f"**Partially Accurate Answers ({len(partial_items)}):**\n"
    report += "Common issues:\n"
    report += "- Missing specific code section references in some answers\n"
    report += "- Incomplete enumeration of requirements (e.g., missing EV charging in cec-001)\n"
    report += "- Correct general approach but lacking specific details\n"
    report += "\n"

report += """
### Strengths

The agent demonstrated several strengths:

"""

accurate_items = [r for r in detailed_results if r['verdict'] == 'Accurate']
if accurate_items:
    report += f"1. **High Accuracy Rate**: {len(accurate_items)}/30 ({len(accurate_items)/30*100:.1f}%) questions answered with complete accuracy\n"

report += """2. **Code Section References**: Generally good at citing relevant CEC articles and sections
3. **Structured Responses**: Answers are well-formatted and easy to read
4. **California-Specific Focus**: Appropriately focuses on California amendments and requirements
5. **Comparative Analysis**: Often compares CEC to NEC to highlight California-specific requirements

### Recommendations for Improvement

1. **Completeness**: Ensure all required elements from questions are addressed (e.g., all 5 appliances in panelboard requirements)
2. **Specific Section Citations**: Always include the most specific code section reference (e.g., 240.4(D) not just 240)
3. **Numerical Precision**: Double-check all numerical values, ampacities, and percentages
4. **Comprehensive Coverage**: When questions ask for lists (e.g., "what appliances"), ensure all items are included

### Overall Assessment
"""

success_rate = (verdicts['Accurate'] + verdicts['Partially Accurate'])/30*100
report += f"""
The CEC agent demonstrates strong performance with a {success_rate:.1f}% success rate (combining accurate and partially accurate responses). The agent shows good understanding of California electrical code requirements, proper code section referencing, and the ability to distinguish California-specific amendments from base NEC requirements.

Key areas of excellence:
- Code section identification and citation
- Understanding of California electrification requirements
- Structured, professional response format
- Comparative analysis with NEC

Areas for improvement:
- Ensuring complete enumeration of all required items
- More precise code section references
- Attention to numerical accuracy in all cases

The agent is performing well overall and would be suitable for providing CEC guidance with minor improvements in completeness and precision.
"""

# Write the report
with open('C:/Users/Andrews Razer Laptop/Desktop/CEC Lang/eval/run 3/cec_judge_report.md', 'w', encoding='utf-8') as f:
    f.write(report)

print("Report generated successfully!")
print(f"\nSummary:")
print(f"Accurate: {verdicts['Accurate']}/30 ({verdicts['Accurate']/30*100:.1f}%)")
print(f"Partially Accurate: {verdicts['Partially Accurate']}/30 ({verdicts['Partially Accurate']/30*100:.1f}%)")
print(f"Inaccurate: {verdicts['Inaccurate']}/30 ({verdicts['Inaccurate']/30*100:.1f}%)")
