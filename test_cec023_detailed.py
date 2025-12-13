import sys
sys.path.insert(0, r"C:\Users\Andrews Razer Laptop\Desktop\CEC Lang")
from core.agent import CECAgent
import json

question = "New residential construction. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI."

agent = CECAgent(enable_reflection=True)
results = []

for i in range(7):
    print(f'\n===== RUN {i+1}/7 =====')
    agent.clear_memory()
    result = agent.ask(question, force_nec_comparison=False)
    answer = result.get('answer', '')

    # Check if AFCI is mentioned for refrigerator (the one often missed)
    afci_for_fridge = 'refrigerator' in answer.lower() and 'afci' in answer.lower()
    # Check for 'not required' which would be wrong
    has_not_required = 'not required' in answer.lower() or 'standard breaker' in answer.lower()

    correct = afci_for_fridge and not has_not_required
    results.append({
        'run': i+1,
        'correct': correct,
        'answer': answer,
        'afci_for_fridge': afci_for_fridge,
        'has_not_required': has_not_required
    })
    print(f'Run {i+1}: {"CORRECT" if correct else "WRONG"} - AFCI for fridge: {afci_for_fridge}, "not required" present: {has_not_required}')

# Save detailed results
with open('test_cec023_detailed_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f'\n\n===== FINAL SUMMARY =====')
print(f'Summary: {sum(1 for r in results if r["correct"])}/7 correct')
print(f'\nAccuracy: {sum(1 for r in results if r["correct"])/7*100:.1f}%')
print('\nDetailed Results:')
for r in results:
    print(f'\n  Run {r["run"]}: {"✓ CORRECT" if r["correct"] else "✗ WRONG"}')
    print(f'    Answer: {r["answer"][:400]}...')
