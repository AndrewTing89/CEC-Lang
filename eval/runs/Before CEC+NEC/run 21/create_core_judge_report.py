#!/usr/bin/env python3
"""
LLM-as-Judge Report Generator for Core (NEC) Evaluation
Scores each answer against expected answers using Gemini as judge.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

# Load rubric
RUBRIC = """
## Scoring Rubric (0-5 scale for each dimension)

### Accuracy (0-5)
- 5: All facts correct, proper code citations
- 4: Minor inaccuracies that don't affect conclusion
- 3: Some errors but core answer correct
- 2: Significant errors affecting reliability
- 1: Mostly incorrect
- 0: Completely wrong or fabricated

### Completeness (0-5)
- 5: Covers all aspects of expected answer
- 4: Missing minor details
- 3: Covers main points, missing some important details
- 2: Partial answer, significant gaps
- 1: Very incomplete
- 0: Does not address the question
"""


def load_expected_answers(filepath: str) -> dict:
    """Load expected answers from simple-text file."""
    expected = {}
    current_id = None
    current_expected = None

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith('baseline-') or line.startswith('core-') or line.startswith('inspection-'):
            parts = line.split('\t', 1)
            if len(parts) >= 1:
                current_id = parts[0]
        elif line.startswith('EXPECTED ANSWER:'):
            current_expected = line.replace('EXPECTED ANSWER:', '').strip()
            if current_id:
                expected[current_id] = current_expected
                current_id = None

    return expected


def judge_answer(question: str, expected: str, actual: str) -> dict:
    """Use Gemini to judge an answer against expected."""

    prompt = f"""You are an expert electrical code reviewer acting as a judge.

Compare the ACTUAL ANSWER against the EXPECTED ANSWER for this question.

QUESTION: {question}

EXPECTED ANSWER: {expected}

ACTUAL ANSWER: {actual}

{RUBRIC}

Score the actual answer on:
1. Accuracy (0-5): Is the information correct?
2. Completeness (0-5): Does it cover all expected points?

Respond in this exact JSON format:
{{
    "accuracy": <0-5>,
    "completeness": <0-5>,
    "total": <sum of above>,
    "reasoning": "<brief explanation of scores>"
}}

Be strict but fair. Only give 5/5 for truly excellent answers that match or exceed expected.
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Extract JSON from response
        if '```json' in text:
            text = text.split('```json')[1].split('```')[0]
        elif '```' in text:
            text = text.split('```')[1].split('```')[0]

        result = json.loads(text)
        return result
    except Exception as e:
        print(f"    Judge error: {str(e)[:50]}")
        return {
            "accuracy": 0,
            "completeness": 0,
            "total": 0,
            "reasoning": f"Judge error: {str(e)}"
        }


def generate_report(results_file: str, expected_file: str, output_dir: str):
    """Generate judge report for evaluation results."""

    # Load data
    with open(results_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = data['results']
    expected_answers = load_expected_answers(expected_file)

    print(f"\n{'='*60}")
    print(f"LLM-as-Judge Report - Core Evaluation")
    print(f"{'='*60}")
    print(f"Questions: {len(results)}")
    print(f"Expected answers loaded: {len(expected_answers)}")
    print(f"{'='*60}\n")

    scores = []
    wrong_answers = []

    for i, r in enumerate(results):
        qid = r['id']
        question = r['question']
        actual = r.get('answer', '')
        expected = expected_answers.get(qid, 'No expected answer')

        print(f"[{i+1}/{len(results)}] Judging {qid}...")

        if not actual:
            judgment = {
                "accuracy": 0,
                "completeness": 0,
                "total": 0,
                "reasoning": "No answer provided"
            }
        else:
            judgment = judge_answer(question, expected, actual)

        scores.append({
            'id': qid,
            'question': question[:100],
            'expected': expected[:200],
            'actual': actual[:500] if actual else 'N/A',
            'accuracy': judgment.get('accuracy', 0),
            'completeness': judgment.get('completeness', 0),
            'total': judgment.get('total', 0),
            'reasoning': judgment.get('reasoning', '')
        })

        total = judgment.get('total', 0)
        print(f"    Score: {total}/10 (Acc: {judgment.get('accuracy', 0)}, Comp: {judgment.get('completeness', 0)})")

        # Track imperfect answers
        if total < 10:
            wrong_answers.append({
                'id': qid,
                'question': question,
                'expected': expected,
                'actual': actual,
                'score': total,
                'reasoning': judgment.get('reasoning', '')
            })

    # Calculate totals
    total_accuracy = sum(s['accuracy'] for s in scores)
    total_completeness = sum(s['completeness'] for s in scores)
    total_score = sum(s['total'] for s in scores)
    max_score = len(scores) * 10

    # Generate markdown report
    date_str = datetime.now().strftime('%Y-%m-%d')
    report_file = os.path.join(output_dir, f'judge_report_core-run1_{date_str}.md')

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"# LLM-as-Judge Report - Core Evaluation Run 1\n\n")
        f.write(f"**Date:** {date_str}\n")
        f.write(f"**Judge Model:** Gemini 2.0 Flash\n\n")

        f.write(f"## Summary\n\n")
        f.write(f"| Metric | Score |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total Score | **{total_score}/{max_score}** ({total_score/max_score*100:.1f}%) |\n")
        f.write(f"| Accuracy | {total_accuracy}/{len(scores)*5} |\n")
        f.write(f"| Completeness | {total_completeness}/{len(scores)*5} |\n")
        f.write(f"| Perfect Scores (10/10) | {len([s for s in scores if s['total'] == 10])} |\n")
        f.write(f"| Imperfect Scores (<10) | {len(wrong_answers)} |\n\n")

        f.write(f"## Score Distribution\n\n")
        f.write(f"| Score | Count |\n")
        f.write(f"|-------|-------|\n")
        for score_val in range(10, -1, -1):
            count = len([s for s in scores if s['total'] == score_val])
            if count > 0:
                f.write(f"| {score_val}/10 | {count} |\n")
        f.write(f"\n")

        f.write(f"## Scores by Question\n\n")
        f.write(f"| ID | Accuracy | Completeness | Total |\n")
        f.write(f"|----|----------|--------------|-------|\n")
        for s in scores:
            f.write(f"| {s['id']} | {s['accuracy']}/5 | {s['completeness']}/5 | **{s['total']}/10** |\n")
        f.write(f"\n")

        f.write(f"## Detailed Reasoning\n\n")
        for s in scores:
            f.write(f"### {s['id']} ({s['total']}/10)\n\n")
            f.write(f"**Reasoning:** {s['reasoning']}\n\n")
            f.write(f"---\n\n")

    # Generate wrong answers report
    wrong_file = os.path.join(output_dir, f'wrong_answers_core-run1_{date_str}.md')

    with open(wrong_file, 'w', encoding='utf-8') as f:
        f.write(f"# Imperfect Answers - Core Evaluation Run 1\n\n")
        f.write(f"**Date:** {date_str}\n")
        f.write(f"**Total Imperfect:** {len(wrong_answers)}/{len(scores)}\n\n")

        for wa in sorted(wrong_answers, key=lambda x: x['score']):
            f.write(f"## {wa['id']} (Score: {wa['score']}/10)\n\n")
            f.write(f"**Question:** {wa['question']}\n\n")
            f.write(f"**Expected:** {wa['expected']}\n\n")
            f.write(f"**Actual:** {wa['actual']}\n\n")
            f.write(f"**Reasoning:** {wa['reasoning']}\n\n")
            f.write(f"---\n\n")

    # Print summary
    print(f"\n{'='*60}")
    print(f"JUDGE REPORT COMPLETE")
    print(f"{'='*60}")
    print(f"Total Score: {total_score}/{max_score} ({total_score/max_score*100:.1f}%)")
    print(f"Perfect Scores: {len([s for s in scores if s['total'] == 10])}")
    print(f"Imperfect Scores: {len(wrong_answers)}")
    print(f"\nOutput files:")
    print(f"  - {report_file}")
    print(f"  - {wrong_file}")
    print(f"{'='*60}\n")

    return scores, wrong_answers


if __name__ == '__main__':
    script_dir = Path(__file__).parent

    # Find latest results file
    results_files = list(script_dir.glob('core-run1_evaluation_results_*.json'))
    if not results_files:
        print("No results file found!")
        sys.exit(1)

    results_file = max(results_files, key=lambda p: p.stat().st_mtime)
    expected_file = script_dir.parent.parent / 'standardized_llm-as-judge' / 'core_evaluation_simple-text.txt'

    print(f"Results file: {results_file}")
    print(f"Expected answers: {expected_file}")

    generate_report(str(results_file), str(expected_file), str(script_dir))
