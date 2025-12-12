"""
Showcase Test: CEC vs NEC Comparison Feature

This script demonstrates the NEC comparison feature by running 3 questions
that highlight meaningful differences between CEC 2022 and NEC 2023.

Questions are written as pure CEC questions (no "compare" wording).
NEC comparison is triggered by force_nec_comparison=True (simulating frontend checkbox).
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from core.agent import CECAgent

# 3 Showcase questions that highlight CEC vs NEC differences
# Questions are worded as pure CEC questions - comparison triggered by flag
SHOWCASE_QUESTIONS = [
    {
        "id": "showcase-01",
        "question": "What are the panelboard space requirements for single-family dwellings in California?",
        "type": "CA policy",
        "expected_cec": "Reserved spaces required for heat pump water heaters, heat pump space heaters, electric cooktops, electric clothes dryers (Section 408.2(A))",
        "expected_nec_difference": "NEC has NO reserved space requirements for specific appliances",
        "why_good": "California-unique electrification mandate - NEC has no equivalent"
    },
    {
        "id": "showcase-02",
        "question": "What are the kitchen GFCI requirements in California?",
        "type": "GFCI",
        "expected_cec": "GFCI required for countertop surfaces and within 6 feet of sink (Section 210.8(A))",
        "expected_nec_difference": "NEC requires GFCI for ALL kitchen receptacles including refrigerators (more restrictive)",
        "why_good": "Shows California is MORE PERMISSIVE - bidirectional difference"
    },
    {
        "id": "showcase-03",
        "question": "What are the EV charging infrastructure requirements for new residential construction in California?",
        "type": "EV infrastructure",
        "expected_cec": "EV-ready infrastructure mandated: dedicated circuits, conduit, panel capacity (Title 24/CALGreen)",
        "expected_nec_difference": "NEC Article 625 only provides installation rules - no mandate",
        "why_good": "California as regulatory leader with proactive requirements"
    }
]


def run_showcase_test():
    """Run the 3 showcase questions with NEC comparison enabled."""
    print("=" * 70)
    print("SHOWCASE: CEC vs NEC Comparison Feature")
    print("=" * 70)
    print("\nThis test demonstrates meaningful differences between CEC 2022 and NEC 2023")
    print("NEC comparison is triggered by force_nec_comparison=True (frontend checkbox)\n")

    # Initialize agent
    agent = CECAgent()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    results = []

    for i, q in enumerate(SHOWCASE_QUESTIONS, 1):
        print(f"\n{'='*70}")
        print(f"Question {i}/3: {q['id']} - {q['type']}")
        print(f"{'='*70}")
        print(f"\nQ: {q['question']}")
        print(f"\nExpected CEC: {q['expected_cec']}")
        print(f"Expected NEC Difference: {q['expected_nec_difference']}")
        print(f"Why Good: {q['why_good']}")
        print(f"\nRunning with force_nec_comparison=True...")

        try:
            result = agent.ask(q['question'], force_nec_comparison=True)

            # Check if compare_with_nec was called
            tools_used = [c.get('tool') for c in result.get('tool_calls', [])]
            has_nec_comparison = 'compare_with_nec' in tools_used

            print(f"\n--- RESULT ---")
            print(f"Iterations: {result.get('iterations', 'N/A')}")
            print(f"Tools used: {tools_used}")
            print(f"compare_with_nec called: {'YES' if has_nec_comparison else 'NO'}")

            # Show answer (truncated)
            answer = result.get('answer', '')
            print(f"\n--- ANSWER (truncated) ---")
            print(answer[:1500] + "..." if len(answer) > 1500 else answer)

            # Check for NEC difference in answer
            answer_lower = answer.lower()
            mentions_nec = 'nec' in answer_lower
            mentions_difference = any(word in answer_lower for word in ['difference', 'unlike', 'does not', 'no such', 'not require', 'more restrictive', 'more permissive'])

            results.append({
                "id": q['id'],
                "type": q['type'],
                "question": q['question'],
                "answer": answer,
                "tools_used": tools_used,
                "has_nec_comparison": has_nec_comparison,
                "mentions_nec": mentions_nec,
                "mentions_difference": mentions_difference,
                "iterations": result.get('iterations', 0),
                "duration_seconds": result.get('duration', 0)
            })

            status = "PASS" if has_nec_comparison and mentions_nec else "FAIL"
            print(f"\nStatus: {status}")

        except Exception as e:
            print(f"\nERROR: {e}")
            results.append({
                "id": q['id'],
                "type": q['type'],
                "question": q['question'],
                "error": str(e)
            })

    # Generate summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")

    passed = sum(1 for r in results if r.get('has_nec_comparison') and r.get('mentions_nec'))
    print(f"\nQuestions with NEC comparison: {passed}/{len(results)}")

    for r in results:
        status = "PASS" if r.get('has_nec_comparison') and r.get('mentions_nec') else "FAIL"
        print(f"  {r['id']}: {status} (NEC comparison: {r.get('has_nec_comparison', 'N/A')}, Mentions NEC: {r.get('mentions_nec', 'N/A')})")

    # Save results
    output_dir = Path(__file__).parent

    # JSON results
    json_file = output_dir / f"showcase_results_{timestamp}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            "metadata": {
                "timestamp": timestamp,
                "total_questions": len(results),
                "passed": passed,
                "test_type": "showcase_nec_comparison"
            },
            "questions": SHOWCASE_QUESTIONS,
            "results": results
        }, f, indent=2)
    print(f"\nResults saved to: {json_file}")

    # Markdown report
    md_file = output_dir / f"showcase_report_{timestamp}.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write("# CEC vs NEC Comparison Showcase\n\n")
        f.write(f"**Date:** {timestamp}\n\n")
        f.write("## Summary\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total Questions | {len(results)} |\n")
        f.write(f"| Questions with NEC Comparison | {passed}/{len(results)} |\n\n")

        f.write("## Questions Tested\n\n")
        f.write("These questions demonstrate meaningful CEC vs NEC differences:\n\n")

        for r in results:
            q = next(q for q in SHOWCASE_QUESTIONS if q['id'] == r['id'])
            status = "PASS" if r.get('has_nec_comparison') and r.get('mentions_nec') else "NEEDS REVIEW"

            f.write(f"### {r['id']} - {r['type']}\n\n")
            f.write(f"**Question:** {r['question']}\n\n")
            f.write(f"**Expected CEC:** {q['expected_cec']}\n\n")
            f.write(f"**Expected NEC Difference:** {q['expected_nec_difference']}\n\n")
            f.write(f"**Why Good for Showcase:** {q['why_good']}\n\n")
            f.write(f"**Status:** {status}\n\n")

            if 'answer' in r:
                f.write("<details>\n<summary>Full Answer</summary>\n\n")
                f.write(r['answer'])
                f.write("\n\n</details>\n\n")

            f.write("---\n\n")

    print(f"Report saved to: {md_file}")

    return results


if __name__ == "__main__":
    run_showcase_test()
