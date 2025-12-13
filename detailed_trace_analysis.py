"""
Deep dive analysis of cec2022-045 inconsistency
Captures full LLM reasoning and tool outputs
"""
import sys
import json
sys.path.insert(0, r"C:\Users\Andrews Razer Laptop\Desktop\CEC Lang")
from core.agent import CECAgent

question = "What type of enclosure is suitable for outdoor use with rain, sleet, and ice per Table 110.28?"

agent = CECAgent(enable_reflection=True)

print("="*80)
print("DETAILED TRACE CAPTURE FOR CEC2022-045")
print("="*80)
print(f"\nQuestion: {question}")
print("\nExpected: Full list (Type 3, 3R, 3S, 3X, 3RX, 3SX, 4, 4X, 6, 6P)")
print("Common Wrong: Only Type 3S, 3SX (focusing on 'Sleet*' row)")
print("\n" + "="*80)

# Run 10 tests to get better statistical sample
results = []
for i in range(10):
    print(f"\n{'='*80}")
    print(f"RUN {i+1}/10")
    print(f"{'='*80}")

    agent.clear_memory()
    result = agent.ask(question, force_nec_comparison=False)

    answer = result.get('answer', '')
    trace = result.get('trace', {})

    # Check correctness - must have Type 3, 3R, and 4 to be correct
    has_type_3 = 'type 3,' in answer.lower() or 'type 3\n' in answer.lower() or '- type 3' in answer.lower()
    has_type_3r = '3r' in answer.lower()
    has_type_4 = 'type 4' in answer.lower()
    is_correct = has_type_3 and has_type_3r and has_type_4

    # Check if answer mentions only 3S/3SX (wrong pattern)
    only_3s_3sx = ('type 3s' in answer.lower() and 'type 3sx' in answer.lower()
                   and not has_type_3r and not has_type_4)

    # Get full tool outputs (not truncated)
    tool_outputs_full = []
    for tc in trace.get('tool_calls_with_outputs', []):
        tool_outputs_full.append({
            'tool': tc.get('tool'),
            'output': tc.get('output', '')  # Full output, no truncation
        })

    # Get full LLM reasoning for each iteration
    iterations_full = []
    for it in trace.get('iterations', []):
        iterations_full.append({
            'iteration': it.get('iteration'),
            'phase': it.get('phase'),
            'llm_content': it.get('llm_content', ''),  # Full reasoning
            'tools_called': [t.get('tool') for t in it.get('tools_called', [])]
        })

    result_data = {
        'run': i+1,
        'correct': is_correct,
        'only_3s_3sx_pattern': only_3s_3sx,
        'answer_full': answer,
        'tool_outputs': tool_outputs_full,
        'iterations': iterations_full,
        'reflection_used': trace.get('reflection_used'),
        'reflection_improved': trace.get('reflection_improved')
    }
    results.append(result_data)

    status = "CORRECT" if is_correct else "WRONG (3S/3SX only)" if only_3s_3sx else "WRONG (other)"
    print(f"\nStatus: {status}")
    print(f"Answer mentions Type 3: {has_type_3}")
    print(f"Answer mentions 3R: {has_type_3r}")
    print(f"Answer mentions Type 4: {has_type_4}")
    print(f"\nAnswer snippet (first 300 chars):")
    print(answer[:300])

# Save full detailed results
output_file = r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\cec045_detailed_analysis.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\n" + "="*80)
print("ANALYSIS SUMMARY")
print("="*80)

correct_runs = [r for r in results if r['correct']]
wrong_3s_only = [r for r in results if r['only_3s_3sx_pattern']]
wrong_other = [r for r in results if not r['correct'] and not r['only_3s_3sx_pattern']]

print(f"\nTotal runs: {len(results)}")
print(f"Correct runs: {len(correct_runs)}/{len(results)} ({100*len(correct_runs)/len(results):.1f}%)")
print(f"Wrong (3S/3SX only): {len(wrong_3s_only)}/{len(results)} ({100*len(wrong_3s_only)/len(results):.1f}%)")
print(f"Wrong (other): {len(wrong_other)}/{len(results)} ({100*len(wrong_other)/len(results):.1f}%)")

# Analyze tool output consistency
print("\n" + "="*80)
print("TOOL OUTPUT ANALYSIS")
print("="*80)

if len(results) > 0 and len(results[0]['tool_outputs']) > 0:
    first_output = results[0]['tool_outputs'][0]['output']

    print("\nChecking if all runs received identical tool output...")
    all_identical = True
    for r in results[1:]:
        if len(r['tool_outputs']) > 0:
            if r['tool_outputs'][0]['output'] != first_output:
                all_identical = False
                print(f"  Run {r['run']}: DIFFERENT tool output")

    if all_identical:
        print("  All runs received IDENTICAL tool output")
        print("\n  Tool output includes both rows:")
        if 'Rain, snow, and sleet' in first_output:
            print("    - 'Rain, snow, and sleet' row: YES")
        if 'Sleet*' in first_output:
            print("    - 'Sleet*' row: YES")

# Analyze LLM reasoning patterns
print("\n" + "="*80)
print("LLM REASONING PATTERN ANALYSIS")
print("="*80)

if correct_runs:
    print(f"\n--- CORRECT RUNS ({len(correct_runs)} total) ---")
    for r in correct_runs[:3]:  # Show first 3 correct runs
        print(f"\nRun {r['run']}:")
        # Find the final answer iteration
        for it in r['iterations']:
            if it['phase'] != 'reflection' and len(it['tools_called']) == 0:
                content = it['llm_content']
                # Look for key phrases
                if 'rain, snow, and sleet' in content.lower():
                    print(f"  Mentions 'Rain, snow, and sleet' row: YES")
                if 'sleet*' in content.lower():
                    print(f"  Mentions 'Sleet*' row: YES")
                # Show snippet
                print(f"  Reasoning snippet: {content[:400]}")
                break

if wrong_3s_only:
    print(f"\n--- WRONG RUNS (3S/3SX only) ({len(wrong_3s_only)} total) ---")
    for r in wrong_3s_only[:3]:  # Show first 3 wrong runs
        print(f"\nRun {r['run']}:")
        # Find the final answer iteration
        for it in r['iterations']:
            if it['phase'] != 'reflection' and len(it['tools_called']) == 0:
                content = it['llm_content']
                # Look for key phrases
                if 'rain, snow, and sleet' in content.lower():
                    print(f"  Mentions 'Rain, snow, and sleet' row: YES")
                else:
                    print(f"  Mentions 'Rain, snow, and sleet' row: NO")
                if 'sleet*' in content.lower():
                    print(f"  Mentions 'Sleet*' row: YES")
                    # Check if it focuses only on Sleet*
                    if 'sleet*' in content.lower() and 'rain, snow' not in content.lower():
                        print(f"  PROBLEM: Focuses on 'Sleet*' without 'Rain, snow, and sleet'")
                # Show snippet
                print(f"  Reasoning snippet: {content[:400]}")
                break

print("\n" + "="*80)
print(f"Full detailed results saved to: {output_file}")
print("="*80)
