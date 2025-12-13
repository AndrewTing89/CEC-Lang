#!/usr/bin/env python3
"""
CEC 2022 Unified Evaluation Script - Run 39
Tests CEC Lang agent on the unified question set (53 questions).

Run 39: AFCI GFCI enforcement and unit selection
Fixes implemented based on Run 38 wrong answer analysis:
1. DOMAIN KNOWLEDGE - Strengthened Circuit Protection with MANDATORY language
2. DOMAIN KNOWLEDGE - Added Unit Selection guidance for dual-unit tables
3. Code Enforcement - Added GFCI/AFCI cross-enforcement in _verify_required_tools()
4. Enforcement Handler - Added protection_type:afci/gfci message handler
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


def load_questions_from_json(filepath: str) -> list:
    """Load questions from the unified JSON question set."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for q in data.get('questions', []):
        questions.append({
            'id': q.get('id', ''),
            'question': q.get('question', ''),
            'original_id': q.get('original_id', ''),
            'tier': q.get('tier', ''),
            'category': q.get('category', '')
        })

    return questions


def run_evaluation(questions: list, output_dir: str):
    """Run evaluation on questions and save results."""

    # Initialize agent WITH REFLECTION ENABLED
    agent = CECAgent(enable_reflection=True)

    results = []
    total_questions = len(questions)

    print(f"\n{'='*60}")
    print(f"CEC 2022 Unified Evaluation - Run 39")
    print(f"{'='*60}")
    print(f"CHANGES (AFCI GFCI enforcement and unit selection):")
    print(f"  1. DOMAIN KNOWLEDGE - Strengthened Circuit Protection (MANDATORY)")
    print(f"  2. DOMAIN KNOWLEDGE - Unit Selection for dual-unit tables")
    print(f"  3. Code Enforcement - GFCI/AFCI cross-enforcement")
    print(f"  4. Enforcement Handler - protection_type message handler")
    print(f"{'='*60}")
    print(f"Total questions: {total_questions}")
    print(f"Reflection: ENABLED")
    print(f"Memory clearing: ENABLED")
    print(f"{'='*60}\n")

    start_time = datetime.now()
    reflection_used_count = 0
    reflection_improved_count = 0
    hint_enforcement_count = 0
    protection_enforcement_count = 0  # NEW: Track GFCI/AFCI enforcement

    # Track by category
    category_stats = {}

    for i, q in enumerate(questions):
        question_id = q.get('id', f'q{i+1}')
        question_text = q.get('question', '')
        category = q.get('category', 'unknown')

        print(f"\n[{i+1}/{total_questions}] {question_id} ({category})")
        print(f"Q: {question_text[:100]}...")

        try:
            q_start = datetime.now()

            # CRITICAL: Clear memory between questions to prevent context pollution
            agent.clear_memory()

            result = agent.ask(question_text, force_nec_comparison=False)
            q_duration = (datetime.now() - q_start).total_seconds()

            # Check tools called
            tools_called = []
            if result.get('trace', {}).get('tool_calls_with_outputs'):
                tools_called = [tc['tool'] for tc in result['trace']['tool_calls_with_outputs']]

            # Check reflection usage
            trace = result.get('trace', {})
            used_reflection = trace.get('reflection_used', False)
            reflection_improved = trace.get('reflection_improved', False)

            # Check enforcement types
            hint_enforced = False
            protection_enforced = False
            for iteration in trace.get('iterations', []):
                enforcement = str(iteration.get('enforcement_triggered', ''))
                if 'hint:' in enforcement:
                    hint_enforced = True
                if 'protection_type:' in enforcement:
                    protection_enforced = True

            if used_reflection:
                reflection_used_count += 1
            if reflection_improved:
                reflection_improved_count += 1
            if hint_enforced:
                hint_enforcement_count += 1
            if protection_enforced:
                protection_enforcement_count += 1

            # Track category stats
            if category not in category_stats:
                category_stats[category] = {'total': 0, 'success': 0}
            category_stats[category]['total'] += 1
            category_stats[category]['success'] += 1

            results.append({
                'id': question_id,
                'original_id': q.get('original_id', ''),
                'question': question_text,
                'category': category,
                'tier': q.get('tier', ''),
                'answer': result.get('answer', ''),
                'trace': trace,
                'tools_called': tools_called,
                'reflection_used': used_reflection,
                'reflection_improved': reflection_improved,
                'hint_enforced': hint_enforced,
                'protection_enforced': protection_enforced,
                'iterations': result.get('iterations', 0),
                'duration_seconds': q_duration,
                'success': True,
                'error': None
            })

            status_parts = [f"Duration: {q_duration:.1f}s", f"Tools: {len(tools_called)}", f"Iter: {result.get('iterations', 0)}"]
            if used_reflection:
                status_parts.append("Reflection: YES" + (" (improved)" if reflection_improved else ""))
            if hint_enforced:
                status_parts.append("Hint Enforced: YES")
            if protection_enforced:
                status_parts.append("Protection Enforced: YES")

            print(f"   [OK] {' | '.join(status_parts)}")

        except Exception as e:
            print(f"   ERROR: {str(e)[:100]}")

            # Track category stats for failures
            if category not in category_stats:
                category_stats[category] = {'total': 0, 'success': 0}
            category_stats[category]['total'] += 1

            results.append({
                'id': question_id,
                'original_id': q.get('original_id', ''),
                'question': question_text,
                'category': category,
                'tier': q.get('tier', ''),
                'answer': None,
                'trace': {},
                'tools_called': [],
                'reflection_used': False,
                'reflection_improved': False,
                'hint_enforced': False,
                'protection_enforced': False,
                'iterations': 0,
                'duration_seconds': 0,
                'success': False,
                'error': str(e)
            })

    total_duration = (datetime.now() - start_time).total_seconds()

    # Calculate statistics
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]

    summary = {
        'run_id': 'run39',
        'description': 'AFCI GFCI enforcement and unit selection',
        'timestamp': datetime.now().isoformat(),
        'total_questions': total_questions,
        'successful': len(successful),
        'failed': len(failed),
        'success_rate': len(successful) / total_questions if total_questions > 0 else 0,
        'total_duration_seconds': total_duration,
        'avg_duration_seconds': total_duration / total_questions if total_questions > 0 else 0,
        'reflection_used_count': reflection_used_count,
        'reflection_improved_count': reflection_improved_count,
        'hint_enforcement_count': hint_enforcement_count,
        'protection_enforcement_count': protection_enforcement_count,
        'category_stats': category_stats,
        'reflection_enabled': True,
        'memory_clearing': True,
        'notes': 'Run 39: GFCI/AFCI code enforcement, unit selection guidance, strengthened DOMAIN KNOWLEDGE'
    }

    # Save results
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')

    # JSON output
    json_file = os.path.join(output_dir, f'run39_evaluation_results_{date_str}.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': summary,
            'results': results
        }, f, indent=2, ensure_ascii=False)

    # Markdown output
    md_file = os.path.join(output_dir, f'run39_evaluation_results_{date_str}.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# CEC 2022 Unified Evaluation Results - Run 39\n\n")
        f.write(f"**Date:** {date_str}\n")
        f.write(f"**Description:** AFCI GFCI enforcement and unit selection\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total Questions | {total_questions} |\n")
        f.write(f"| Successful | {len(successful)} |\n")
        f.write(f"| Failed | {len(failed)} |\n")
        f.write(f"| Success Rate | {summary['success_rate']*100:.1f}% |\n")
        f.write(f"| Total Duration | {total_duration:.1f}s |\n")
        f.write(f"| Avg Duration | {summary['avg_duration_seconds']:.1f}s |\n")
        f.write(f"| Reflection Used | {reflection_used_count}/{total_questions} |\n")
        f.write(f"| Reflection Improved | {reflection_improved_count}/{total_questions} |\n")
        f.write(f"| Hint Enforcement | {hint_enforcement_count}/{total_questions} |\n")
        f.write(f"| Protection Enforcement | {protection_enforcement_count}/{total_questions} |\n\n")

        # Category breakdown
        f.write(f"## Results by Category\n\n")
        f.write(f"| Category | Total | Success | Rate |\n")
        f.write(f"|----------|-------|---------|------|\n")
        for cat, stats in sorted(category_stats.items()):
            rate = (stats['success'] / stats['total'] * 100) if stats['total'] > 0 else 0
            f.write(f"| {cat} | {stats['total']} | {stats['success']} | {rate:.0f}% |\n")
        f.write(f"\n")

        f.write(f"## Results by Question\n\n")
        for r in results:
            f.write(f"### {r['id']}\n\n")
            f.write(f"**Original ID:** {r.get('original_id', 'N/A')} | **Category:** {r.get('category', 'N/A')} | **Tier:** {r.get('tier', 'N/A')}\n\n")
            f.write(f"**Question:** {r['question']}\n\n")
            f.write(f"**Duration:** {r['duration_seconds']:.1f}s | **Iterations:** {r['iterations']}\n\n")
            f.write(f"**Tools Called:** {', '.join(r['tools_called']) if r['tools_called'] else 'None'}\n\n")
            f.write(f"**Reflection:** {'Yes' if r['reflection_used'] else 'No'}")
            if r['reflection_improved']:
                f.write(f" (improved answer)")
            f.write(f"\n\n")
            f.write(f"**Hint Enforced:** {'Yes' if r.get('hint_enforced') else 'No'}\n")
            f.write(f"**Protection Enforced:** {'Yes' if r.get('protection_enforced') else 'No'}\n\n")
            if r['success']:
                f.write(f"**Answer:**\n\n{r['answer']}\n\n")
            else:
                f.write(f"**Error:** {r['error']}\n\n")
            f.write(f"---\n\n")

    # Print summary
    print(f"\n{'='*60}")
    print(f"EVALUATION COMPLETE - Run 39 (AFCI GFCI enforcement and unit selection)")
    print(f"{'='*60}")
    print(f"Total: {total_questions} | Passed: {len(successful)} | Failed: {len(failed)}")
    print(f"Success Rate: {summary['success_rate']*100:.1f}%")
    print(f"Total Duration: {total_duration:.1f}s (avg {summary['avg_duration_seconds']:.1f}s/question)")
    print(f"Reflection Used: {reflection_used_count}/{total_questions}")
    print(f"Reflection Improved: {reflection_improved_count}/{total_questions}")
    print(f"Hint Enforcement: {hint_enforcement_count}/{total_questions}")
    print(f"Protection Enforcement: {protection_enforcement_count}/{total_questions}")
    print(f"\nCategory Breakdown:")
    for cat, stats in sorted(category_stats.items()):
        rate = (stats['success'] / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"  {cat}: {stats['success']}/{stats['total']} ({rate:.0f}%)")
    print(f"\nOutput files:")
    print(f"  - {json_file}")
    print(f"  - {md_file}")
    print(f"{'='*60}\n")

    return summary, results


if __name__ == '__main__':
    # Paths
    script_dir = Path(__file__).parent
    questions_file = script_dir.parent.parent / 'standardized_llm-as-judge' / 'CEC2022_eval_questions.json'
    output_dir = script_dir

    # Load and run
    questions = load_questions_from_json(str(questions_file))
    print(f"Loaded {len(questions)} questions from unified question set")

    summary, results = run_evaluation(questions, str(output_dir))
