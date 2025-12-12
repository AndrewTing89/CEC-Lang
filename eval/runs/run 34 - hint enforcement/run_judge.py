#!/usr/bin/env python3
"""
LLM-as-Judge for Run 34 (Hint Enforcement)
Uses Claude to evaluate agent answers against expected answers.
"""

import json
import os
import re
import anthropic
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def load_expected_answers(filepath: str) -> dict:
    """Load expected answers from simple-text.txt format."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = content.split('-' * 80)
    expected = {}

    for block in blocks:
        block = block.strip()
        if not block or block.startswith('NEC 2023') or block.startswith('Total:') or block.startswith('='):
            continue

        lines = block.split('\n')
        first_line = lines[0].strip()

        if '\t' in first_line:
            parts = first_line.split('\t', 1)
            q_id = parts[0].strip()
            q_text = parts[1].strip() if len(parts) > 1 else ''
        else:
            match = re.match(r'^([a-z]+-\d+)\s+(.+)$', first_line)
            if match:
                q_id = match.group(1)
                q_text = match.group(2)
            else:
                continue

        # Find expected answer
        exp_answer = ""
        for i, line in enumerate(lines):
            if line.strip().startswith('Expected:'):
                exp_answer = line.strip()[9:].strip()
                # Continue reading if answer spans multiple lines
                for j in range(i+1, len(lines)):
                    if lines[j].strip() and not lines[j].startswith('Source:'):
                        exp_answer += " " + lines[j].strip()
                    else:
                        break
                break

        if q_id:
            expected[q_id] = {
                'question': q_text,
                'expected_answer': exp_answer
            }

    return expected


def judge_answer(client, question: str, agent_answer: str, expected_answer: str) -> dict:
    """Use Claude to judge the agent's answer."""

    prompt = f"""You are an expert electrical code judge evaluating an AI agent's answer about NEC/CEC electrical codes.

## Question
{question}

## Agent's Answer
{agent_answer}

## Expected Answer (Reference)
{expected_answer}

## Scoring Rubric

**Accuracy (0-5 points)**:
- 5: Completely accurate, all values and citations correct
- 4: Minor inaccuracies that don't affect the main answer
- 3: Some inaccuracies but core answer is correct
- 2: Significant inaccuracies
- 1: Mostly incorrect
- 0: Completely wrong

**Completeness (0-5 points)**:
- 5: Addresses all parts of question with full detail
- 4: Addresses all parts, minor details missing
- 3: Addresses most parts
- 2: Missing significant portions
- 1: Barely addresses the question
- 0: Does not address the question

## Instructions
1. Compare the agent's answer to the expected answer
2. Note that different valid approaches may exist (e.g., standard vs optional calculation methods)
3. Focus on whether the answer would help an electrician/inspector make the correct decision
4. Provide scores and brief justification

Respond in this exact JSON format:
{{
    "accuracy_score": <0-5>,
    "completeness_score": <0-5>,
    "total_score": <0-10>,
    "accuracy_notes": "<brief notes on accuracy>",
    "completeness_notes": "<brief notes on completeness>",
    "errors": ["<list of specific errors if any>"]
}}"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    # Parse JSON from response
    text = response.content[0].text
    # Find JSON block
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        return json.loads(json_match.group())
    else:
        return {
            "accuracy_score": 0,
            "completeness_score": 0,
            "total_score": 0,
            "accuracy_notes": "Failed to parse judge response",
            "completeness_notes": text,
            "errors": ["Parse error"]
        }


def run_judge(results_file: str, expected_file: str, output_dir: str):
    """Run judge on all results."""

    # Load data
    with open(results_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = data['results']
    expected = load_expected_answers(expected_file)

    # Initialize Anthropic client
    client = anthropic.Anthropic()

    judge_results = []
    total_score = 0
    max_score = 0

    print(f"\n{'='*60}")
    print(f"LLM-as-Judge - Run 34 (Hint Enforcement)")
    print(f"{'='*60}")
    print(f"Questions: {len(results)}")
    print(f"{'='*60}\n")

    for i, r in enumerate(results):
        q_id = r['id']
        question = r['question']
        agent_answer = r.get('answer', '')

        exp = expected.get(q_id, {})
        expected_answer = exp.get('expected_answer', 'No expected answer available')

        print(f"[{i+1}/{len(results)}] Judging {q_id}...", end=" ")

        try:
            judgment = judge_answer(client, question, agent_answer, expected_answer)

            judge_results.append({
                'id': q_id,
                'question': question[:100] + "...",
                'judgment': judgment,
                'reflection_used': r.get('reflection_used', False),
                'reflection_improved': r.get('reflection_improved', False),
                'hint_enforced': r.get('hint_enforced', False)
            })

            score = judgment.get('total_score', 0)
            total_score += score
            max_score += 10

            markers = []
            if r.get('reflection_improved'):
                markers.append("R+")
            elif r.get('reflection_used'):
                markers.append("R")
            if r.get('hint_enforced'):
                markers.append("H")

            marker_str = f" [{','.join(markers)}]" if markers else ""
            print(f"{score}/10{marker_str}")

        except Exception as e:
            print(f"ERROR: {e}")
            judge_results.append({
                'id': q_id,
                'question': question[:100] + "...",
                'judgment': {'error': str(e), 'total_score': 0},
                'reflection_used': r.get('reflection_used', False),
                'reflection_improved': r.get('reflection_improved', False),
                'hint_enforced': r.get('hint_enforced', False)
            })
            max_score += 10

    # Calculate stats
    perfect_scores = sum(1 for jr in judge_results if jr['judgment'].get('total_score', 0) == 10)
    high_scores = sum(1 for jr in judge_results if 8 <= jr['judgment'].get('total_score', 0) < 10)
    medium_scores = sum(1 for jr in judge_results if 5 <= jr['judgment'].get('total_score', 0) < 8)
    low_scores = sum(1 for jr in judge_results if jr['judgment'].get('total_score', 0) < 5)

    # Reflection stats
    reflection_improved_scores = [jr['judgment'].get('total_score', 0) for jr in judge_results if jr.get('reflection_improved')]

    # Hint enforcement stats
    hint_enforced_scores = [jr['judgment'].get('total_score', 0) for jr in judge_results if jr.get('hint_enforced')]

    summary = {
        'run_id': 'core-run34',
        'total_score': total_score,
        'max_score': max_score,
        'percentage': (total_score / max_score * 100) if max_score > 0 else 0,
        'perfect_scores': perfect_scores,
        'high_scores': high_scores,
        'medium_scores': medium_scores,
        'low_scores': low_scores,
        'reflection_improved_count': sum(1 for jr in judge_results if jr.get('reflection_improved')),
        'reflection_improved_avg_score': sum(reflection_improved_scores) / len(reflection_improved_scores) if reflection_improved_scores else 0,
        'hint_enforced_count': sum(1 for jr in judge_results if jr.get('hint_enforced')),
        'hint_enforced_avg_score': sum(hint_enforced_scores) / len(hint_enforced_scores) if hint_enforced_scores else 0
    }

    # Save results
    date_str = datetime.now().strftime('%Y-%m-%d')

    # JSON
    json_file = os.path.join(output_dir, f'judge_results_{date_str}.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({'summary': summary, 'results': judge_results}, f, indent=2)

    # Markdown report
    md_file = os.path.join(output_dir, f'judge_report - core-run34.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# Judge Report - Core Run 34 (Hint Enforcement)\n\n")
        f.write(f"**Date:** {date_str}\n")
        f.write(f"**Model:** qwen/qwen3-32b\n")
        f.write(f"**Judge:** Claude Sonnet 4\n\n")

        f.write(f"## Summary\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total Score | {total_score}/{max_score} ({summary['percentage']:.1f}%) |\n")
        f.write(f"| Perfect (10/10) | {perfect_scores} |\n")
        f.write(f"| High (8-9/10) | {high_scores} |\n")
        f.write(f"| Medium (5-7/10) | {medium_scores} |\n")
        f.write(f"| Low (<5/10) | {low_scores} |\n")
        f.write(f"| Reflection Improved | {summary['reflection_improved_count']} |\n")
        f.write(f"| Reflection Improved Avg Score | {summary['reflection_improved_avg_score']:.1f}/10 |\n")
        f.write(f"| Hint Enforced | {summary['hint_enforced_count']} |\n")
        f.write(f"| Hint Enforced Avg Score | {summary['hint_enforced_avg_score']:.1f}/10 |\n\n")

        f.write(f"## Scores by Question\n\n")
        f.write(f"| ID | Score | Markers | Notes |\n")
        f.write(f"|-----|-------|---------|-------|\n")
        for jr in judge_results:
            j = jr['judgment']
            score = j.get('total_score', 0)
            markers = []
            if jr.get('reflection_improved'):
                markers.append("R+")
            elif jr.get('reflection_used'):
                markers.append("R")
            if jr.get('hint_enforced'):
                markers.append("H")
            marker_str = ",".join(markers) if markers else "-"
            notes = j.get('accuracy_notes', '')[:50]
            f.write(f"| {jr['id']} | {score}/10 | {marker_str} | {notes}... |\n")

        f.write(f"\n## Questions with Errors\n\n")
        for jr in judge_results:
            j = jr['judgment']
            if j.get('total_score', 0) < 10:
                f.write(f"### {jr['id']} ({j.get('total_score', 0)}/10)\n\n")
                f.write(f"**Accuracy ({j.get('accuracy_score', 0)}/5):** {j.get('accuracy_notes', '')}\n\n")
                f.write(f"**Completeness ({j.get('completeness_score', 0)}/5):** {j.get('completeness_notes', '')}\n\n")
                if j.get('errors'):
                    f.write(f"**Errors:** {', '.join(j.get('errors', []))}\n\n")
                f.write(f"---\n\n")

    # Wrong answers file
    wrong_file = os.path.join(output_dir, f'wrong_answers - core-run34.md')
    with open(wrong_file, 'w', encoding='utf-8') as f:
        f.write(f"# Wrong Answers - Core Run 34\n\n")
        f.write(f"**Total Score:** {total_score}/{max_score} ({summary['percentage']:.1f}%)\n\n")

        for jr in judge_results:
            j = jr['judgment']
            if j.get('total_score', 0) < 10:
                markers = []
                if jr.get('reflection_improved'):
                    markers.append("Reflection Improved")
                elif jr.get('reflection_used'):
                    markers.append("Reflection Used")
                if jr.get('hint_enforced'):
                    markers.append("Hint Enforced")
                marker_str = ", ".join(markers) if markers else "None"

                f.write(f"## {jr['id']} - Score: {j.get('total_score', 0)}/10\n\n")
                f.write(f"**Features:** {marker_str}\n\n")
                f.write(f"**Accuracy:** {j.get('accuracy_score', 0)}/5 - {j.get('accuracy_notes', '')}\n\n")
                f.write(f"**Completeness:** {j.get('completeness_score', 0)}/5 - {j.get('completeness_notes', '')}\n\n")
                if j.get('errors'):
                    f.write(f"**Specific Errors:**\n")
                    for err in j.get('errors', []):
                        f.write(f"- {err}\n")
                f.write(f"\n---\n\n")

    # Print summary
    print(f"\n{'='*60}")
    print(f"JUDGE COMPLETE - Run 34")
    print(f"{'='*60}")
    print(f"Total Score: {total_score}/{max_score} ({summary['percentage']:.1f}%)")
    print(f"Perfect: {perfect_scores} | High: {high_scores} | Medium: {medium_scores} | Low: {low_scores}")
    print(f"Reflection Improved: {summary['reflection_improved_count']} questions (avg {summary['reflection_improved_avg_score']:.1f}/10)")
    print(f"Hint Enforced: {summary['hint_enforced_count']} questions (avg {summary['hint_enforced_avg_score']:.1f}/10)")
    print(f"\nOutput files:")
    print(f"  - {json_file}")
    print(f"  - {md_file}")
    print(f"  - {wrong_file}")
    print(f"{'='*60}\n")

    return summary


if __name__ == '__main__':
    script_dir = Path(__file__).parent
    results_file = script_dir / 'core-run34_evaluation_results_2025-12-11.json'
    expected_file = script_dir.parent.parent / 'standardized_llm-as-judge' / 'core_evaluation_simple-text.txt'

    run_judge(str(results_file), str(expected_file), str(script_dir))
