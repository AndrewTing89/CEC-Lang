#!/usr/bin/env python3
"""Re-run problematic questions after fixes to verify they work."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.stdout.reconfigure(encoding='utf-8')

from datetime import datetime
from core.agent import CECAgent
import json

# Questions to re-run
QUESTIONS = [
    {
        "id": "core-004",
        "question": "Is surge protection required for a new 200A residential service? If so, where can it be installed?"
    },
    {
        "id": "inspection-005",
        "question": "New residential construction, 2023 NEC. Kitchen installation has: (1) four countertop receptacles on two 20A circuits, (2) dishwasher on dedicated 15A circuit, (3) garbage disposal on dedicated 15A circuit, (4) refrigerator on dedicated 20A circuit. For each circuit, specify the required protection: standard breaker, GFCI, AFCI, or combination AFCI/GFCI. Provide NEC references."
    },
    {
        "id": "inspection-008",
        "question": "A 120V single-phase branch circuit supplies a continuous load of 22 amperes. The circuit uses 12 AWG copper conductors with a resistance of 1.29 ohms per 1,000 feet. The one-way distance from the panel to the load is 50 feet. Calculate the voltage drop in volts and as a percentage. Does this meet NEC recommendations (3% maximum for branch circuits)?"
    }
]

def main():
    print("=" * 60)
    print("Re-running Fixed Questions")
    print("=" * 60)

    # Initialize agent
    agent = CECAgent()
    print(f"[OK] Agent initialized")

    results = []

    for q in QUESTIONS:
        print(f"\n{'='*60}")
        print(f"[{q['id']}] {q['question'][:80]}...")
        print("="*60)

        # Clear memory before each question
        agent.clear_memory()

        start = datetime.now()
        try:
            result = agent.ask(q['question'], force_nec_comparison=False)
            duration = (datetime.now() - start).total_seconds()

            print(f"\n[OK] Duration: {duration:.1f}s")
            print(f"[OK] Tools: {result.get('tools_called', [])}")
            print(f"\n--- ANSWER ---")
            print(result['answer'][:2000])

            results.append({
                "id": q['id'],
                "question": q['question'],
                "answer": result['answer'],
                "tools_called": result.get('tools_called', []),
                "trace": result.get('trace', {}),
                "duration": duration,
                "success": True
            })

        except Exception as e:
            print(f"[ERROR] {e}")
            results.append({
                "id": q['id'],
                "question": q['question'],
                "error": str(e),
                "success": False
            })

    # Save results
    output_file = os.path.join(os.path.dirname(__file__), "rerun_results.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"results": results}, f, indent=2, ensure_ascii=False)

    print(f"\n\n{'='*60}")
    print(f"Results saved to: {output_file}")
    print("="*60)

if __name__ == "__main__":
    main()
