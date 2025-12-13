import sys
import json
import os
sys.path.insert(0, r"C:\Users\Andrews Razer Laptop\Desktop\CEC Lang")
from core.agent import CECAgent

question = "Calculate the general lighting load for a 5,000 square foot office building."

agent = CECAgent(enable_reflection=True)
results = []

for i in range(5):
    print(f"\n{'='*60}")
    print(f"RUN {i+1}")
    print(f"{'='*60}")

    agent.clear_memory()
    result = agent.ask(question, force_nec_comparison=False)

    answer = result.get('answer', '')
    trace = result.get('trace', {})

    # Check correctness
    uses_1_3 = '1.3' in answer or '6,500' in answer or '6500' in answer
    uses_14 = '14 va' in answer.lower() or '70,000' in answer or '70000' in answer or '× 14' in answer
    correct = uses_1_3 and not uses_14

    # Get tool outputs - CRITICAL: capture the actual table data returned
    tool_outputs = []
    for tc in trace.get('tool_calls_with_outputs', []):
        tool_outputs.append({
            'tool': tc.get('tool'),
            'input': tc.get('input'),
            'output': str(tc.get('output', ''))[:1500]  # Get more of the output
        })

    # Get iteration details with LLM reasoning
    iterations = []
    for it in trace.get('iterations', []):
        iterations.append({
            'iteration': it.get('iteration'),
            'phase': it.get('phase'),
            'llm_content': str(it.get('llm_content', ''))[:800] if it.get('llm_content') else None,
            'tools_called': [t.get('tool') for t in it.get('tools_called', [])]
        })

    result_data = {
        'run': i+1,
        'correct': correct,
        'uses_1_3': uses_1_3,
        'uses_14': uses_14,
        'answer_snippet': answer[:500],
        'tool_outputs': tool_outputs,
        'iterations': iterations,
        'reflection_used': trace.get('reflection_used'),
        'reflection_improved': trace.get('reflection_improved')
    }
    results.append(result_data)

    print(f"CORRECT: {correct} (uses 1.3: {uses_1_3}, uses 14: {uses_14})")
    print(f"Answer snippet: {answer[:300]}")

# Analyze patterns
print("\n" + "="*60)
print("PATTERN ANALYSIS")
print("="*60)

correct_runs = [r for r in results if r['correct']]
wrong_runs = [r for r in results if not r['correct']]

print(f"\nCorrect runs: {len(correct_runs)}/5")
print(f"Wrong runs: {len(wrong_runs)}/5")

if correct_runs:
    print("\n--- CORRECT RUN PATTERNS ---")
    for r in correct_runs:
        print(f"\nRun {r['run']}:")
        print(f"  Tools used: {[t['tool'] for t in r['tool_outputs']]}")
        # Check what the tool returned
        for t in r['tool_outputs']:
            if 'office' in t['output'].lower() or '220.12' in t['output']:
                print(f"  Tool output contains '1.3': {'1.3' in t['output']}")
                print(f"  Tool output contains '14': {'14' in t['output'] and 'va' in t['output'].lower()}")
                print(f"  Tool output snippet: {t['output'][:400]}")

if wrong_runs:
    print("\n--- WRONG RUN PATTERNS ---")
    for r in wrong_runs:
        print(f"\nRun {r['run']}:")
        print(f"  Tools used: {[t['tool'] for t in r['tool_outputs']]}")
        for t in r['tool_outputs']:
            if 'office' in t['output'].lower() or '220.12' in t['output']:
                print(f"  Tool output contains '1.3': {'1.3' in t['output']}")
                print(f"  Tool output contains '14': {'14' in t['output']}")
                print(f"  Tool output snippet: {t['output'][:400]}")

# Save detailed results
output_path = r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\cec051_trace_analysis.json'
try:
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, default=str, ensure_ascii=False)
    print(f"\nDetailed results saved to {output_path}")
except Exception as e:
    print(f"\nError saving JSON: {e}")
    print("Attempting alternative save...")
    alt_path = os.path.join(os.getcwd(), 'cec051_trace_analysis.json')
    with open(alt_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, default=str, ensure_ascii=False)
    print(f"Saved to {alt_path}")
