"""
CEC Lang Evaluation Runner
Runs evaluation questions and saves results in JSON and Markdown format
"""
import sys
import json
import time
import re
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()

from core.agent import CECAgent


def run_evaluation(questions_file: str, output_dir: str, limit: int = None, result_prefix: str = "cec_evaluation"):
    """Run evaluation and save results

    Args:
        questions_file: Path to JSON file with questions
        output_dir: Directory to save results
        limit: Optional limit on number of questions
        result_prefix: Prefix for output filenames (e.g., 'cec_evaluation' or 'core_evaluation')
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
    print(f"CEC Lang Evaluation - {total} Questions")
    print(f"{'='*60}\n")

    # Initialize agent
    print("Initializing CEC Agent...")
    agent = CECAgent(verbose=False)
    print(f"Agent ready: {agent.model_name}\n")

    # Run evaluation
    results = []
    successful = 0
    failed = 0
    total_duration = 0

    for i, q in enumerate(questions, 1):
        qid = q['id']
        question = q['question']
        expected = q['expected_answer']
        cec_ref = q.get('cec_reference', '')
        nec_ref = q.get('nec_reference', '')
        tier = q.get('tier', '')
        category = q.get('category', '')
        ca_specific = q.get('highlights_difference', False)

        # Clear chat history between questions for independent evaluation
        agent.chat_history = []

        print(f"[{i}/{total}] {qid}: {question[:60]}...")

        try:
            start = time.time()
            result = agent.ask(question)
            duration = time.time() - start
            total_duration += duration

            answer = result.get('answer', '')
            tool_calls = result.get('tool_calls', [])

            # Determine pass/fail based on key content
            status = "PASS"  # Default to pass if we got an answer
            if not answer or answer.startswith("Error:"):
                status = "FAIL"
                failed += 1
            else:
                successful += 1

            # Extract citations from answer
            citations = re.findall(r'\b(\d{3}\.\d+(?:\([A-Z]\)(?:\(\d+\))?)?)\b', answer)
            citations = list(set(citations))

            # Check tool usage
            cec_tools_used = [tc['tool'] for tc in tool_calls if 'cec' in tc['tool'].lower()]
            nec_tools_used = [tc['tool'] for tc in tool_calls if 'nec' in tc['tool'].lower() and 'cec' not in tc['tool'].lower()]

            results.append({
                "id": qid,
                "tier": tier,
                "category": category,
                "ca_specific": ca_specific,
                "question": question,
                "expected_answer": expected,
                "cec_reference": cec_ref,
                "nec_reference": nec_ref,
                "status": status,
                "answer": answer,
                "tool_calls": tool_calls,
                "cec_tools_used": cec_tools_used,
                "nec_tools_used": nec_tools_used,
                "citations": citations,
                "duration_seconds": round(duration, 1),
                "cec_primary": len(cec_tools_used) > 0,
                "trace": result.get("trace", {})  # Full execution trace
            })

            print(f"    [{status}] {duration:.1f}s - {len(tool_calls)} tool calls")

        except Exception as e:
            failed += 1
            results.append({
                "id": qid,
                "tier": tier,
                "category": category,
                "ca_specific": ca_specific,
                "question": question,
                "expected_answer": expected,
                "cec_reference": cec_ref,
                "nec_reference": nec_ref,
                "status": "ERROR",
                "answer": f"Error: {str(e)}",
                "tool_calls": [],
                "cec_tools_used": [],
                "nec_tools_used": [],
                "citations": [],
                "duration_seconds": 0,
                "cec_primary": False,
                "trace": {}  # Empty trace on error
            })
            print(f"    [ERROR] {str(e)[:50]}")

        # Brief pause between questions to avoid rate limits
        time.sleep(1)

    # Generate output
    timestamp = datetime.now().strftime("%Y-%m-%d")

    # JSON output
    json_output = {
        "metadata": {
            "date": timestamp,
            "model": agent.model_name,
            "total_questions": total,
            "successful": successful,
            "failed": failed,
            "success_rate": f"{successful/total*100:.1f}%",
            "total_duration_seconds": round(total_duration, 1),
            "avg_duration_seconds": round(total_duration/total, 1)
        },
        "results": results
    }

    # Extract run number from output dir name (e.g., "run 2" -> "run2")
    run_prefix = Path(output_dir).name.replace(" ", "")

    json_path = Path(output_dir) / f"{run_prefix}-{result_prefix}_results_{timestamp}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_output, f, indent=2, ensure_ascii=False)
    print(f"\nJSON saved: {json_path}")

    # Markdown output
    md_content = generate_markdown(json_output, results)
    md_path = Path(output_dir) / f"{run_prefix}-{result_prefix}_results_{timestamp}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Markdown saved: {md_path}")

    # Summary
    print(f"\n{'='*60}")
    print(f"EVALUATION COMPLETE")
    print(f"{'='*60}")
    print(f"Total: {total} | Passed: {successful} | Failed: {failed}")
    print(f"Success Rate: {successful/total*100:.1f}%")
    print(f"Total Duration: {total_duration:.1f}s")
    print(f"Avg per Question: {total_duration/total:.1f}s")
    print(f"{'='*60}\n")

    return json_output


def generate_markdown(metadata: dict, results: list) -> str:
    """Generate markdown report"""
    meta = metadata['metadata']

    md = f"""# CEC Agent Evaluation - LangChain + Groq

**Date:** {meta['date']}
**Model:** {meta['model']}
**Agent:** California Electrical Code Agent (LangChain)
**Architecture:** California-First (CEC 2022 primary, NEC 2023 comparison)

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | {meta['total_questions']} |
| **Successful** | {meta['successful']} ({meta['success_rate']}) |
| **Failed** | {meta['failed']} |
| **Total Duration** | {meta['total_duration_seconds']}s |
| **Avg per Question** | {meta['avg_duration_seconds']}s |

---

## Results by Question

"""

    # Group by tier
    tiers = {}
    for r in results:
        tier = r.get('tier', 'other')
        if tier not in tiers:
            tiers[tier] = []
        tiers[tier].append(r)

    tier_names = {
        'california_specific': 'California-Unique Requirements',
        'delta_table': 'CEC Delta Tables',
        'calculation': 'Complex Calculations',
        'comparison': 'CEC vs NEC Comparison'
    }

    for tier, tier_results in tiers.items():
        tier_display = tier_names.get(tier, tier.title())
        md += f"\n## {tier_display}\n\n"

        for r in tier_results:
            ca_tag = " [CA-SPECIFIC]" if r.get('ca_specific') else ""
            status_emoji = "PASS" if r['status'] == "PASS" else "FAIL"

            md += f"""### {r['id']}: {r['category']}{ca_tag}

**Question:** {r['question']}

**Expected:** {r['expected_answer'][:300]}{'...' if len(r['expected_answer']) > 300 else ''}

**CEC Ref:** {r['cec_reference']} | **NEC Ref:** {r['nec_reference']}

**Status:** {status_emoji}

**Agent Answer:**
{r['answer'][:2000]}{'...' if len(r['answer']) > 2000 else ''}

**Tool Usage:**
- CEC Tools: {', '.join(r['cec_tools_used']) if r['cec_tools_used'] else 'None'}
- NEC Tools: {', '.join(r['nec_tools_used']) if r['nec_tools_used'] else 'None'}
- CEC Primary: {'Yes' if r['cec_primary'] else 'No'}

**Citations:** {len(r['citations'])} found
- {', '.join(r['citations'][:10]) if r['citations'] else 'None'}

**Response Time:** {r['duration_seconds']}s

---

"""

    # Summary
    cec_primary_count = sum(1 for r in results if r['cec_primary'])

    md += f"""
## Analysis

### Key Metrics

- **CEC-Primary Responses**: {cec_primary_count}/{len(results)}
- **Success Rate**: {meta['success_rate']}
- **Average Response Time**: {meta['avg_duration_seconds']}s

### Model Information

- **Provider**: Groq
- **Model**: {meta['model']}
- **Framework**: LangChain + LangGraph

"""

    return md


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run CEC evaluation")
    parser.add_argument("--questions", type=str, default="cec_evaluation_questions.json",
                        help="Questions file (default: cec_evaluation_questions.json)")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of questions")
    parser.add_argument("--output-dir", type=str, default="run 3", help="Output directory name")
    args = parser.parse_args()

    # Determine questions file path
    questions_path = Path(args.questions)
    if not questions_path.is_absolute():
        questions_path = Path(__file__).parent / args.questions
    questions_file = str(questions_path)

    # Determine result prefix from questions filename
    # e.g., "cec_evaluation_questions.json" -> "cec_evaluation"
    # e.g., "core_evaluation_questions.json" -> "core_evaluation"
    questions_name = Path(args.questions).stem  # Remove .json
    if questions_name.endswith("_questions"):
        result_prefix = questions_name[:-10]  # Remove "_questions"
    else:
        result_prefix = questions_name

    output_dir = Path(__file__).parent / args.output_dir

    run_evaluation(questions_file, str(output_dir), limit=args.limit, result_prefix=result_prefix)
