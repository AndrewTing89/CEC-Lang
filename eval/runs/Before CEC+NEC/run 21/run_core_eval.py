#!/usr/bin/env python3
"""
Core (NEC) Evaluation Script - Run 1
Tests CEC Lang agent on general NEC questions (28 questions).

Note: These are NEC-focused questions, so NEC comparison is NOT forced.
The agent should use NEC tools directly for these questions.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from core.agent import CECAgent


def load_questions(questions_file: str) -> list:
    """Load evaluation questions from JSON file."""
    with open(questions_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('questions', data)


def run_evaluation(questions: list, output_dir: str, limit: int = None):
    """Run evaluation on questions and save results."""

    # Initialize agent (NEC comparison NOT forced for core questions)
    agent = CECAgent()

    results = []
    total_questions = len(questions) if limit is None else min(limit, len(questions))

    print(f"\n{'='*60}")
    print(f"Core (NEC) Evaluation - Run 1")
    print(f"Prompt version: v4 - no hardcoded values")
    print(f"{'='*60}")
    print(f"Total questions: {total_questions}")
    print(f"NEC comparison: NOT FORCED (these are NEC questions)")
    print(f"Exception search: VOLUNTARY (not forced)")
    print(f"{'='*60}\n")

    start_time = datetime.now()
    exception_search_count = 0

    for i, q in enumerate(questions[:total_questions]):
        question_id = q.get('id', f'q{i+1}')
        question_text = q.get('question', q.get('text', ''))

        print(f"\n[{i+1}/{total_questions}] {question_id}")
        print(f"Q: {question_text[:100]}...")

        try:
            q_start = datetime.now()
            # Do NOT force NEC comparison - these are NEC questions
            result = agent.ask(question_text, force_nec_comparison=False)
            q_duration = (datetime.now() - q_start).total_seconds()

            # Check tools called
            tools_called = []
            if result.get('trace', {}).get('tool_calls_with_outputs'):
                tools_called = [tc['tool'] for tc in result['trace']['tool_calls_with_outputs']]

            used_exception_search = any('exception_search' in t for t in tools_called)
            if used_exception_search:
                exception_search_count += 1

            results.append({
                'id': question_id,
                'question': question_text,
                'answer': result.get('answer', ''),
                'trace': result.get('trace', {}),
                'tools_called': tools_called,
                'used_exception_search': used_exception_search,
                'duration_seconds': q_duration,
                'success': True,
                'error': None
            })

            # Show brief status
            print(f"   Duration: {q_duration:.1f}s | Tools: {len(tools_called)} | Exception search: {'Yes' if used_exception_search else 'No'}")

        except Exception as e:
            print(f"   ERROR: {str(e)[:100]}")
            results.append({
                'id': question_id,
                'question': question_text,
                'answer': None,
                'trace': {},
                'tools_called': [],
                'used_exception_search': False,
                'duration_seconds': 0,
                'success': False,
                'error': str(e)
            })

    total_duration = (datetime.now() - start_time).total_seconds()

    # Calculate statistics
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]

    summary = {
        'run_id': 'core-run1',
        'prompt_version': 'v4 - no hardcoded values',
        'timestamp': datetime.now().isoformat(),
        'total_questions': total_questions,
        'successful': len(successful),
        'failed': len(failed),
        'success_rate': len(successful) / total_questions if total_questions > 0 else 0,
        'total_duration_seconds': total_duration,
        'avg_duration_seconds': total_duration / total_questions if total_questions > 0 else 0,
        'exception_search_count': exception_search_count,
        'nec_comparison_forced': False,
        'notes': 'Core NEC questions - agent uses NEC tools directly'
    }

    # Save results
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')

    # JSON output
    json_file = os.path.join(output_dir, f'core-run1_evaluation_results_{date_str}.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': summary,
            'results': results
        }, f, indent=2, ensure_ascii=False)

    # Markdown output
    md_file = os.path.join(output_dir, f'core-run1_evaluation_results_{date_str}.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# Core (NEC) Evaluation Results - Run 1\n\n")
        f.write(f"**Date:** {date_str}\n")
        f.write(f"**Prompt Version:** v4 - no hardcoded values\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total Questions | {total_questions} |\n")
        f.write(f"| Successful | {len(successful)} |\n")
        f.write(f"| Failed | {len(failed)} |\n")
        f.write(f"| Success Rate | {summary['success_rate']*100:.1f}% |\n")
        f.write(f"| Total Duration | {total_duration:.1f}s |\n")
        f.write(f"| Avg Duration | {summary['avg_duration_seconds']:.1f}s |\n")
        f.write(f"| Exception Search Used | {exception_search_count}/{total_questions} |\n")
        f.write(f"| NEC Comparison Forced | No |\n\n")

        f.write(f"## Results by Question\n\n")
        for r in results:
            f.write(f"### {r['id']}\n\n")
            f.write(f"**Question:** {r['question']}\n\n")
            f.write(f"**Duration:** {r['duration_seconds']:.1f}s | **Exception Search:** {'Yes' if r['used_exception_search'] else 'No'}\n\n")
            f.write(f"**Tools Called:** {', '.join(r['tools_called']) if r['tools_called'] else 'None'}\n\n")
            if r['success']:
                f.write(f"**Answer:**\n\n{r['answer']}\n\n")
            else:
                f.write(f"**Error:** {r['error']}\n\n")
            f.write(f"---\n\n")

    # Print summary
    print(f"\n{'='*60}")
    print(f"EVALUATION COMPLETE - Core Run 1")
    print(f"{'='*60}")
    print(f"Total: {total_questions} | Passed: {len(successful)} | Failed: {len(failed)}")
    print(f"Success Rate: {summary['success_rate']*100:.1f}%")
    print(f"Total Duration: {total_duration:.1f}s (avg {summary['avg_duration_seconds']:.1f}s/question)")
    print(f"Exception Search Used: {exception_search_count}/{total_questions}")
    print(f"\nOutput files:")
    print(f"  - {json_file}")
    print(f"  - {md_file}")
    print(f"{'='*60}\n")

    return summary, results


if __name__ == '__main__':
    # Paths
    script_dir = Path(__file__).parent
    questions_file = script_dir.parent.parent / 'standardized_llm-as-judge' / 'core_evaluation_questions.json'
    output_dir = script_dir

    # Load questions
    questions = load_questions(str(questions_file))

    # Run evaluation
    summary, results = run_evaluation(questions, str(output_dir))
