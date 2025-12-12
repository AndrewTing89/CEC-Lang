"""
NEC Comparison Toggle Test
Tests the force_nec_comparison feature by running the same questions twice:
1. With NEC comparison OFF (default)
2. With NEC comparison ON (checkbox enabled)

Compares tool calls, answers, and timing between the two modes.
"""
import sys
import json
import time
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
load_dotenv()

from core.agent import CECAgent


# Test questions - California-specific that don't inherently ask for NEC comparison
TEST_QUESTIONS = [
    {
        "id": "cec-001",
        "question": "What are the panelboard space requirements for single-family dwellings in California? What appliances must have reserved circuit breaker spaces?",
        "type": "CA policy"
    },
    {
        "id": "cec-011",
        "question": "What is the ampacity of 4/0 AWG copper conductor at 75C according to California electrical code?",
        "type": "Table lookup"
    },
    {
        "id": "cec-018",
        "question": "What is the general lighting load in VA per square foot for office buildings according to California code?",
        "type": "Table lookup"
    },
    {
        "id": "cec-021",
        "question": "Calculate the adjusted ampacity for 8 AWG THWN copper conductors with 7 conductors in a raceway at 40C ambient temperature in California.",
        "type": "Calculation"
    }
]


def run_single_test(agent: CECAgent, question: str, force_nec_comparison: bool) -> dict:
    """Run a single question and capture results."""
    agent.chat_history = []  # Clear history for independent test

    start = time.time()
    result = agent.ask(question, force_nec_comparison=force_nec_comparison)
    duration = time.time() - start

    # Extract tool names
    tool_names = [tc.get('tool', 'unknown') for tc in result.get('tool_calls', [])]

    # Check if compare_with_nec was called
    has_nec_comparison = 'compare_with_nec' in tool_names

    return {
        "answer": result.get('answer', ''),
        "tool_calls": result.get('tool_calls', []),
        "tool_names": tool_names,
        "duration_seconds": round(duration, 1),
        "iterations": result.get('iterations', 0),
        "has_nec_comparison": has_nec_comparison
    }


def run_comparison_test():
    """Run the full comparison test."""
    output_dir = Path(__file__).parent
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")

    print("\n" + "=" * 70)
    print("NEC COMPARISON TOGGLE TEST")
    print("=" * 70)
    print(f"Testing {len(TEST_QUESTIONS)} questions in 2 modes (OFF / ON)")
    print("=" * 70 + "\n")

    # Initialize agent
    print("Initializing CEC Agent...")
    agent = CECAgent(verbose=True)
    print(f"Agent ready: {agent.model_name}\n")

    results = []

    for i, q in enumerate(TEST_QUESTIONS, 1):
        qid = q['id']
        question = q['question']
        qtype = q['type']

        print("\n" + "-" * 70)
        print(f"[{i}/{len(TEST_QUESTIONS)}] {qid} ({qtype})")
        print(f"Question: {question[:80]}...")
        print("-" * 70)

        # Run with NEC comparison OFF
        print("\n>>> Mode: NEC Comparison OFF")
        result_off = run_single_test(agent, question, force_nec_comparison=False)
        print(f"    Duration: {result_off['duration_seconds']}s")
        print(f"    Tools: {', '.join(result_off['tool_names'])}")
        print(f"    compare_with_nec called: {result_off['has_nec_comparison']}")

        # Brief pause to avoid rate limits
        time.sleep(2)

        # Run with NEC comparison ON
        print("\n>>> Mode: NEC Comparison ON")
        result_on = run_single_test(agent, question, force_nec_comparison=True)
        print(f"    Duration: {result_on['duration_seconds']}s")
        print(f"    Tools: {', '.join(result_on['tool_names'])}")
        print(f"    compare_with_nec called: {result_on['has_nec_comparison']}")

        # Analyze differences
        time_diff = result_on['duration_seconds'] - result_off['duration_seconds']
        tools_added = set(result_on['tool_names']) - set(result_off['tool_names'])

        # Verification checks
        check_nec_only_when_on = (not result_off['has_nec_comparison']) and result_on['has_nec_comparison']

        print(f"\n    --- Analysis ---")
        print(f"    Time difference: {time_diff:+.1f}s")
        print(f"    Tools added when ON: {tools_added if tools_added else 'None'}")
        print(f"    VERIFY: compare_with_nec only when ON: {'PASS' if check_nec_only_when_on else 'FAIL'}")

        results.append({
            "id": qid,
            "question": question,
            "type": qtype,
            "off": {
                "answer": result_off['answer'],
                "tool_names": result_off['tool_names'],
                "duration_seconds": result_off['duration_seconds'],
                "iterations": result_off['iterations'],
                "has_nec_comparison": result_off['has_nec_comparison']
            },
            "on": {
                "answer": result_on['answer'],
                "tool_names": result_on['tool_names'],
                "duration_seconds": result_on['duration_seconds'],
                "iterations": result_on['iterations'],
                "has_nec_comparison": result_on['has_nec_comparison']
            },
            "analysis": {
                "time_difference_seconds": round(time_diff, 1),
                "tools_added": list(tools_added),
                "nec_comparison_only_when_on": check_nec_only_when_on
            }
        })

        # Pause between questions
        time.sleep(2)

    # Generate summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    total_time_off = sum(r['off']['duration_seconds'] for r in results)
    total_time_on = sum(r['on']['duration_seconds'] for r in results)
    avg_time_diff = (total_time_on - total_time_off) / len(results)

    pass_count = sum(1 for r in results if r['analysis']['nec_comparison_only_when_on'])

    print(f"\nTotal questions: {len(results)}")
    print(f"PASS (compare_with_nec only when ON): {pass_count}/{len(results)}")
    print(f"\nTotal time OFF: {total_time_off:.1f}s")
    print(f"Total time ON:  {total_time_on:.1f}s")
    print(f"Average additional time: {avg_time_diff:+.1f}s per question")

    # Save JSON results
    json_output = {
        "metadata": {
            "timestamp": timestamp,
            "model": agent.model_name,
            "total_questions": len(results),
            "pass_count": pass_count,
            "total_time_off_seconds": round(total_time_off, 1),
            "total_time_on_seconds": round(total_time_on, 1),
            "avg_time_difference_seconds": round(avg_time_diff, 1)
        },
        "results": results
    }

    json_path = output_dir / f"nec_comparison_test_results_{timestamp}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_output, f, indent=2, ensure_ascii=False)
    print(f"\nJSON saved: {json_path}")

    # Generate markdown report
    md_content = generate_markdown_report(json_output)
    md_path = output_dir / f"nec_comparison_test_report_{timestamp}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Markdown saved: {md_path}")

    print("\n" + "=" * 70)
    print("TEST COMPLETE")
    print("=" * 70 + "\n")

    return json_output


def generate_markdown_report(data: dict) -> str:
    """Generate a markdown report from test results."""
    meta = data['metadata']
    results = data['results']

    md = f"""# NEC Comparison Toggle Test Report

**Date:** {meta['timestamp']}
**Model:** {meta['model']}

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | {meta['total_questions']} |
| PASS (compare_with_nec only when ON) | {meta['pass_count']}/{meta['total_questions']} |
| Total Time (OFF mode) | {meta['total_time_off_seconds']}s |
| Total Time (ON mode) | {meta['total_time_on_seconds']}s |
| Average Additional Time | {meta['avg_time_difference_seconds']:+.1f}s |

---

## Test Results

"""

    for r in results:
        nec_check = "PASS" if r['analysis']['nec_comparison_only_when_on'] else "FAIL"

        md += f"""### {r['id']} - {r['type']}

**Question:** {r['question']}

#### Mode: NEC Comparison OFF

- **Duration:** {r['off']['duration_seconds']}s
- **Iterations:** {r['off']['iterations']}
- **Tools:** {', '.join(r['off']['tool_names'])}
- **compare_with_nec called:** {'Yes' if r['off']['has_nec_comparison'] else 'No'}

<details>
<summary>Answer (OFF mode)</summary>

{r['off']['answer']}

</details>

#### Mode: NEC Comparison ON

- **Duration:** {r['on']['duration_seconds']}s
- **Iterations:** {r['on']['iterations']}
- **Tools:** {', '.join(r['on']['tool_names'])}
- **compare_with_nec called:** {'Yes' if r['on']['has_nec_comparison'] else 'No'}

<details>
<summary>Answer (ON mode)</summary>

{r['on']['answer']}

</details>

#### Analysis

- **Time Difference:** {r['analysis']['time_difference_seconds']:+.1f}s
- **Tools Added:** {', '.join(r['analysis']['tools_added']) if r['analysis']['tools_added'] else 'None'}
- **Verification (compare_with_nec only when ON):** {nec_check}

---

"""

    md += f"""## Conclusion

The NEC comparison toggle {'is working as expected' if meta['pass_count'] == meta['total_questions'] else 'has some issues'}.

- When OFF: Agent uses only CEC tools
- When ON: Agent additionally calls `compare_with_nec` to show differences from NEC 2023
- Average overhead: {meta['avg_time_difference_seconds']:+.1f}s per question

"""

    return md


if __name__ == "__main__":
    run_comparison_test()
