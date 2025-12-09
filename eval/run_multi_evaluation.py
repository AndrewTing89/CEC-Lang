"""
CEC Lang Multi-Run Evaluation Runner
Runs evaluation questions multiple times to average out LLM variance
Uses majority voting to determine final verdict per question
"""
import sys
import json
import time
import re
from datetime import datetime
from pathlib import Path
from collections import Counter

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()

from core.agent import CECAgent


def run_single_question(agent: CECAgent, question: str) -> dict:
    """Run a single question and return the result"""
    agent.chat_history = []  # Clear history for independent evaluation

    start = time.time()
    result = agent.ask(question)
    duration = time.time() - start

    answer = result.get('answer', '')
    tool_calls = result.get('tool_calls', [])

    # Determine pass/fail
    status = "PASS"
    if not answer or answer.startswith("Error:"):
        status = "FAIL"

    # Extract citations
    citations = re.findall(r'\b(\d{3}\.\d+(?:\([A-Z]\)(?:\(\d+\))?)?)\b', answer)
    citations = list(set(citations))

    # Check tool usage
    cec_tools_used = [tc['tool'] for tc in tool_calls if 'cec' in tc['tool'].lower()]
    nec_tools_used = [tc['tool'] for tc in tool_calls if 'nec' in tc['tool'].lower() and 'cec' not in tc['tool'].lower()]

    return {
        "status": status,
        "answer": answer,
        "tool_calls": tool_calls,
        "cec_tools_used": cec_tools_used,
        "nec_tools_used": nec_tools_used,
        "citations": citations,
        "duration_seconds": round(duration, 1),
        "cec_primary": len(cec_tools_used) > 0,
        "trace": result.get("trace", {})
    }


def run_multi_evaluation(questions_file: str, output_dir: str, num_runs: int = 3,
                         limit: int = None, result_prefix: str = "cec_evaluation"):
    """Run evaluation multiple times and aggregate results

    Args:
        questions_file: Path to JSON file with questions
        output_dir: Directory to save results
        num_runs: Number of times to run each question (default 3)
        limit: Optional limit on number of questions
        result_prefix: Prefix for output filenames
    """

    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Load questions
    with open(questions_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data['questions']
    if limit:
        questions = questions[:limit]
    total = len(questions)

    print(f"\n{'='*60}")
    print(f"CEC Lang Multi-Run Evaluation")
    print(f"Questions: {total} | Runs per question: {num_runs}")
    print(f"Total API calls: {total * num_runs}")
    print(f"{'='*60}\n")

    # Initialize agent
    print("Initializing CEC Agent...")
    agent = CECAgent(verbose=False)
    print(f"Agent ready: {agent.model_name}\n")

    # Store all runs per question
    all_runs = {}  # {qid: [run1_result, run2_result, run3_result]}

    # Run evaluation
    for i, q in enumerate(questions, 1):
        qid = q['id']
        question = q['question']

        print(f"[{i}/{total}] {qid}: {question[:50]}...")

        runs = []
        for run_num in range(1, num_runs + 1):
            print(f"  Run {run_num}/{num_runs}...", end=" ")

            try:
                result = run_single_question(agent, question)
                result['run_number'] = run_num
                runs.append(result)
                print(f"[{result['status']}] {result['duration_seconds']:.1f}s")

            except Exception as e:
                error_result = {
                    "run_number": run_num,
                    "status": "ERROR",
                    "answer": f"Error: {str(e)}",
                    "tool_calls": [],
                    "cec_tools_used": [],
                    "nec_tools_used": [],
                    "citations": [],
                    "duration_seconds": 0,
                    "cec_primary": False,
                    "trace": {}
                }
                runs.append(error_result)
                print(f"[ERROR] {str(e)[:40]}")

            # Brief pause between runs
            time.sleep(1)

        all_runs[qid] = {
            "question_data": q,
            "runs": runs
        }

        # Show consistency for this question
        statuses = [r['status'] for r in runs]
        consistency = max(Counter(statuses).values()) / len(runs) * 100
        print(f"  Consistency: {consistency:.0f}% ({Counter(statuses)})")
        print()

    # Aggregate results
    aggregated_results = aggregate_results(all_runs)

    # Generate output
    timestamp = datetime.now().strftime("%Y-%m-%d")
    run_prefix = Path(output_dir).name.replace(" ", "")

    # Save all runs (raw data)
    all_runs_path = Path(output_dir) / f"{run_prefix}-{result_prefix}_multi_results_{timestamp}.json"
    all_runs_output = {
        "metadata": {
            "date": timestamp,
            "model": agent.model_name,
            "total_questions": total,
            "runs_per_question": num_runs,
            "total_api_calls": total * num_runs
        },
        "all_runs": all_runs
    }
    with open(all_runs_path, 'w', encoding='utf-8') as f:
        json.dump(all_runs_output, f, indent=2, ensure_ascii=False)
    print(f"\nAll runs saved: {all_runs_path}")

    # Save aggregated results
    agg_path = Path(output_dir) / f"{run_prefix}-{result_prefix}_aggregated_{timestamp}.json"
    agg_output = {
        "metadata": {
            "date": timestamp,
            "model": agent.model_name,
            "total_questions": total,
            "runs_per_question": num_runs,
            "aggregation_method": "majority_voting"
        },
        "results": aggregated_results
    }
    with open(agg_path, 'w', encoding='utf-8') as f:
        json.dump(agg_output, f, indent=2, ensure_ascii=False)
    print(f"Aggregated results saved: {agg_path}")

    # Generate variance report
    variance_report = generate_variance_report(all_runs, aggregated_results, num_runs)
    variance_path = Path(output_dir) / f"{run_prefix}-{result_prefix}_variance_{timestamp}.md"
    with open(variance_path, 'w', encoding='utf-8') as f:
        f.write(variance_report)
    print(f"Variance report saved: {variance_path}")

    # Summary
    successful = sum(1 for r in aggregated_results if r['aggregated_status'] == 'PASS')
    failed = total - successful

    high_consistency = sum(1 for r in aggregated_results if r['consistency'] == 100)
    medium_consistency = sum(1 for r in aggregated_results if 50 < r['consistency'] < 100)
    low_consistency = sum(1 for r in aggregated_results if r['consistency'] <= 50)

    print(f"\n{'='*60}")
    print(f"MULTI-RUN EVALUATION COMPLETE")
    print(f"{'='*60}")
    print(f"Total Questions: {total}")
    print(f"Runs per Question: {num_runs}")
    print(f"Aggregated Pass Rate: {successful}/{total} ({successful/total*100:.1f}%)")
    print(f"\nConsistency Breakdown:")
    print(f"  High (100%): {high_consistency} questions")
    print(f"  Medium (50-99%): {medium_consistency} questions")
    print(f"  Low (<50%): {low_consistency} questions")
    print(f"{'='*60}\n")

    return agg_output


def aggregate_results(all_runs: dict) -> list:
    """Aggregate multiple runs into a single result per question using majority voting"""

    aggregated = []

    for qid, data in all_runs.items():
        q = data['question_data']
        runs = data['runs']

        # Majority vote on status
        statuses = [r['status'] for r in runs]
        status_counts = Counter(statuses)
        majority_status = status_counts.most_common(1)[0][0]
        consistency = status_counts.most_common(1)[0][1] / len(runs) * 100

        # Use the answer from the majority status runs
        majority_runs = [r for r in runs if r['status'] == majority_status]
        # Pick the first (or longest) answer from majority runs
        best_run = max(majority_runs, key=lambda r: len(r.get('answer', '')))

        # Aggregate tool usage across all runs
        all_cec_tools = set()
        all_nec_tools = set()
        all_citations = set()
        total_duration = 0

        for r in runs:
            all_cec_tools.update(r.get('cec_tools_used', []))
            all_nec_tools.update(r.get('nec_tools_used', []))
            all_citations.update(r.get('citations', []))
            total_duration += r.get('duration_seconds', 0)

        aggregated.append({
            "id": qid,
            "tier": q.get('tier', ''),
            "category": q.get('category', ''),
            "ca_specific": q.get('highlights_difference', False),
            "question": q['question'],
            "expected_answer": q['expected_answer'],
            "cec_reference": q.get('cec_reference', ''),
            "nec_reference": q.get('nec_reference', ''),
            "aggregated_status": majority_status,
            "consistency": consistency,
            "status_breakdown": dict(status_counts),
            "answer": best_run.get('answer', ''),
            "all_answers": [r.get('answer', '')[:500] for r in runs],  # Truncated for storage
            "cec_tools_used": list(all_cec_tools),
            "nec_tools_used": list(all_nec_tools),
            "citations": list(all_citations),
            "avg_duration_seconds": round(total_duration / len(runs), 1),
            "cec_primary": any(r.get('cec_primary', False) for r in runs)
        })

    return aggregated


def generate_variance_report(all_runs: dict, aggregated: list, num_runs: int) -> str:
    """Generate a markdown report analyzing variance across runs"""

    # Categorize by consistency
    high_consistency = [r for r in aggregated if r['consistency'] == 100]
    medium_consistency = [r for r in aggregated if 50 < r['consistency'] < 100]
    low_consistency = [r for r in aggregated if r['consistency'] <= 50]

    report = f"""# Multi-Run Variance Analysis Report

## Summary

| Metric | Value |
|--------|-------|
| Total Questions | {len(aggregated)} |
| Runs per Question | {num_runs} |
| High Consistency (100%) | {len(high_consistency)} |
| Medium Consistency (50-99%) | {len(medium_consistency)} |
| Low Consistency (<50%) | {len(low_consistency)} |

## Consistency Distribution

### High Consistency Questions ({len(high_consistency)})

These questions returned the same status across all {num_runs} runs - confident baseline.

| ID | Category | Status | Avg Duration |
|----|----------|--------|--------------|
"""

    for r in sorted(high_consistency, key=lambda x: x['id']):
        report += f"| {r['id']} | {r['category']} | {r['aggregated_status']} | {r['avg_duration_seconds']}s |\n"

    report += f"""

### Medium Consistency Questions ({len(medium_consistency)})

These questions had some variance - majority voting applied.

| ID | Category | Majority Status | Breakdown | Notes |
|----|----------|-----------------|-----------|-------|
"""

    for r in sorted(medium_consistency, key=lambda x: x['consistency']):
        breakdown = ', '.join(f"{k}:{v}" for k, v in r['status_breakdown'].items())
        report += f"| {r['id']} | {r['category']} | {r['aggregated_status']} | {breakdown} | {r['consistency']:.0f}% agreement |\n"

    report += f"""

### Low Consistency Questions ({len(low_consistency)})

These questions are highly unstable - needs investigation.

| ID | Category | Majority Status | Breakdown | Notes |
|----|----------|-----------------|-----------|-------|
"""

    for r in sorted(low_consistency, key=lambda x: x['consistency']):
        breakdown = ', '.join(f"{k}:{v}" for k, v in r['status_breakdown'].items())
        report += f"| {r['id']} | {r['category']} | {r['aggregated_status']} | {breakdown} | Only {r['consistency']:.0f}% agreement |\n"

    # Overall statistics
    pass_count = sum(1 for r in aggregated if r['aggregated_status'] == 'PASS')
    avg_consistency = sum(r['consistency'] for r in aggregated) / len(aggregated)

    report += f"""

## Overall Statistics

| Metric | Value |
|--------|-------|
| Pass Rate (Aggregated) | {pass_count}/{len(aggregated)} ({pass_count/len(aggregated)*100:.1f}%) |
| Average Consistency | {avg_consistency:.1f}% |
| Questions with 100% Consistency | {len(high_consistency)}/{len(aggregated)} ({len(high_consistency)/len(aggregated)*100:.1f}%) |

## Recommendations

"""

    if low_consistency:
        report += """### High-Variance Questions Need Investigation

The following questions showed significant variance and should be investigated for:
1. Ambiguous phrasing in the question
2. Multiple valid answers
3. Search result ordering sensitivity
4. Missing guidance in system prompt

"""
        for r in low_consistency:
            report += f"- **{r['id']}** ({r['category']}): {r['status_breakdown']}\n"
    else:
        report += "No questions showed critically low consistency.\n"

    report += f"""

---
*Report Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}*
*Runs per Question: {num_runs}*
"""

    return report


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run multi-pass CEC evaluation")
    parser.add_argument("--questions", type=str, default="cec_evaluation_questions.json",
                        help="Questions file (default: cec_evaluation_questions.json)")
    parser.add_argument("--runs", type=int, default=3,
                        help="Number of runs per question (default: 3)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limit number of questions")
    parser.add_argument("--output-dir", type=str, default="run 7",
                        help="Output directory name")
    args = parser.parse_args()

    # Determine questions file path
    questions_path = Path(args.questions)
    if not questions_path.is_absolute():
        questions_path = Path(__file__).parent / args.questions
    questions_file = str(questions_path)

    # Determine result prefix from questions filename
    questions_name = Path(args.questions).stem
    if questions_name.endswith("_questions"):
        result_prefix = questions_name[:-10]
    else:
        result_prefix = questions_name

    output_dir = Path(__file__).parent / args.output_dir

    run_multi_evaluation(
        questions_file,
        str(output_dir),
        num_runs=args.runs,
        limit=args.limit,
        result_prefix=result_prefix
    )
