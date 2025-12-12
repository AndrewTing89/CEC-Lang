#!/usr/bin/env python3
"""
Variability Test - Run problematic questions multiple times to test LLM consistency.
Tests if errors are due to LLM variability or systematic issues.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from core.agent import CECAgent

# The 3 worst questions from Run 30
TEST_QUESTIONS = [
    {
        "id": "core-002",
        "question": "An electrician installed a multiwire branch circuit feeding kitchen receptacles using 12/3 cable. What are the NEC requirements for the circuit breaker and neutral termination?",
        "key_fact": "handle ties ARE permitted per 240.15(B)(1)"
    },
    {
        "id": "core-005",
        "question": "A panel is installed in a closet with 24 inches of clearance in front, and a water heater is 18 inches to the side. Does this meet NEC requirements?",
        "key_fact": "240.24(D) prohibits overcurrent devices in clothes closets"
    },
    {
        "id": "inspection-001",
        "question": "Residential panel inspection: 200A main breaker. Installed loads: (1) 12kW electric range on 40A breaker, (2) 5.5kW dryer on 30A breaker, (3) two 20A small appliance circuits, (4) one 20A laundry circuit, (5) 3000 sq ft living space with general lighting, (6) 4-ton central AC (19.2A at 240V, approximately 4600W). Calculate the service load per NEC Article 220 and determine if the 200A panel is adequately sized.",
        "key_fact": "Table 220.42: First 3000VA at 100%, remainder at 35%"
    }
]

ITERATIONS = 5

def run_variability_test():
    agent = CECAgent()
    results = {}

    print(f"\n{'='*60}")
    print(f"VARIABILITY TEST - {ITERATIONS} iterations per question")
    print(f"{'='*60}\n")

    for q in TEST_QUESTIONS:
        q_id = q["id"]
        results[q_id] = {
            "question": q["question"],
            "key_fact": q["key_fact"],
            "iterations": []
        }

        print(f"\n{'='*60}")
        print(f"Question: {q_id}")
        print(f"Key fact to check: {q['key_fact']}")
        print(f"{'='*60}")

        for i in range(ITERATIONS):
            print(f"\n  [Iteration {i+1}/{ITERATIONS}]")
            agent.clear_memory()

            try:
                result = agent.ask(q["question"], force_nec_comparison=False)
                answer = result.get("answer", "")

                # Check if key fact is mentioned
                answer_lower = answer.lower()

                if q_id == "core-002":
                    # Check if correctly states handle ties ARE permitted
                    mentions_permitted = "handle tie" in answer_lower and ("permitted" in answer_lower or "allowed" in answer_lower)
                    incorrectly_says_not = "not permitted" in answer_lower or "not allowed" in answer_lower
                    got_it_right = mentions_permitted and not incorrectly_says_not

                elif q_id == "core-005":
                    # Check if mentions clothes closet prohibition
                    mentions_closet = "240.24(d)" in answer_lower or "clothes closet" in answer_lower
                    got_it_right = mentions_closet

                elif q_id == "inspection-001":
                    # Check if uses correct demand factors (100%/35%)
                    uses_35 = "35%" in answer or "35 percent" in answer_lower
                    uses_wrong_40 = "40%" in answer or "40 percent" in answer_lower
                    got_it_right = uses_35 and not uses_wrong_40

                results[q_id]["iterations"].append({
                    "iteration": i + 1,
                    "got_key_fact": got_it_right,
                    "answer_preview": answer[:500]
                })

                status = "✓ CORRECT" if got_it_right else "✗ WRONG"
                print(f"    {status}")

            except Exception as e:
                print(f"    ERROR: {str(e)[:100]}")
                results[q_id]["iterations"].append({
                    "iteration": i + 1,
                    "got_key_fact": False,
                    "error": str(e)
                })

    # Summary
    print(f"\n\n{'='*60}")
    print("VARIABILITY TEST SUMMARY")
    print(f"{'='*60}\n")

    for q_id, data in results.items():
        correct = sum(1 for it in data["iterations"] if it.get("got_key_fact", False))
        total = len(data["iterations"])
        pct = (correct / total * 100) if total > 0 else 0

        print(f"{q_id}: {correct}/{total} correct ({pct:.0f}%)")
        print(f"  Key fact: {data['key_fact']}")
        print()

    # Save results
    output_file = Path(__file__).parent / f"variability_test_results_{datetime.now().strftime('%Y-%m-%d_%H%M')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {output_file}")

    return results

if __name__ == "__main__":
    run_variability_test()
