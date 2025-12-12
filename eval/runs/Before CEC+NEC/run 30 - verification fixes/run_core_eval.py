#!/usr/bin/env python3
"""
Core (NEC) Evaluation Script - Run 30 (Verification Fixes)
Tests CEC Lang agent on general NEC questions (28 questions).

CHANGES from Run 29:
- Enhanced Step 4 in system prompt for explicit tool citation
- Added correction factor verification (0.88, 0.70 must come from tools)
- Auto-retry on hallucination detection for calculations
- Normalized factor comparison (0.7 == 0.70)
"""

import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from core.agent import CECAgent


def parse_simple_text_questions(filepath: str) -> list:
    """Parse questions from simple-text.txt format."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by separator
    blocks = content.split('-' * 80)
    questions = []

    for block in blocks:
        block = block.strip()
        if not block or block.startswith('NEC 2023') or block.startswith('Total:') or block.startswith('='):
            continue

        # Parse question ID and text
        lines = block.split('\n')
        first_line = lines[0].strip()

        # Format: "baseline-001\tWhat is the ampacity..."
        if '\t' in first_line:
            parts = first_line.split('\t', 1)
            q_id = parts[0].strip()
            q_text = parts[1].strip() if len(parts) > 1 else ''
        else:
            # Try to extract ID from start
            match = re.match(r'^([a-z]+-\d+)\s+(.+)$', first_line)
            if match:
                q_id = match.group(1)
                q_text = match.group(2)
            else:
                continue

        if q_id and q_text:
            questions.append({
                'id': q_id,
                'question': q_text
            })

    return questions


def run_evaluation(questions: list, output_dir: str):
    """Run evaluation on questions and save results."""

    # Initialize agent
    agent = CECAgent()

    results = []
    total_questions = len(questions)

    print(f"\n{'='*60}")
    print(f"Core (NEC) Evaluation - Run 30 (Verification Fixes)")
    print(f"{'='*60}")
    print(f"CHANGES:")
    print(f"  - Enhanced Step 4 for explicit tool citation")
    print(f"  - Correction factor verification (must come from tools)")
    print(f"  - Auto-retry on calculation hallucination")
    print(f"  - Normalized factor comparison (0.7 == 0.70)")
    print(f"{'='*60}")
    print(f"Total questions: {total_questions}")
    print(f"NEC comparison: NOT FORCED")
    print(f"Memory clearing: ENABLED")
    print(f"Tool enforcement: ENABLED")
    print(f"{'='*60}\n")

    start_time = datetime.now()
    exception_search_count = 0
    nec_comparison_count = 0
    hallucination_retry_count = 0

    for i, q in enumerate(questions):
        question_id = q.get('id', f'q{i+1}')
        question_text = q.get('question', '')

        print(f"\n[{i+1}/{total_questions}] {question_id}")
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

            used_exception_search = any('exception_search' in t for t in tools_called)
            used_nec_comparison = 'compare_with_nec' in tools_called

            # Check for hallucination warning (indicates retry happened)
            had_hallucination_warning = 'hallucination_warning' in result.get('trace', {})
            if had_hallucination_warning:
                hallucination_retry_count += 1

            if used_exception_search:
                exception_search_count += 1
            if used_nec_comparison:
                nec_comparison_count += 1

            results.append({
                'id': question_id,
                'question': question_text,
                'answer': result.get('answer', ''),
                'trace': result.get('trace', {}),
                'tools_called': tools_called,
                'used_exception_search': used_exception_search,
                'nec_comparison_used': used_nec_comparison,
                'hallucination_warning': had_hallucination_warning,
                'duration_seconds': q_duration,
                'success': True,
                'error': None
            })

            status = "RETRY" if had_hallucination_warning else "OK"
            print(f"   [{status}] Duration: {q_duration:.1f}s | Tools: {len(tools_called)}")

        except Exception as e:
            print(f"   ERROR: {str(e)[:100]}")
            results.append({
                'id': question_id,
                'question': question_text,
                'answer': None,
                'trace': {},
                'tools_called': [],
                'used_exception_search': False,
                'nec_comparison_used': False,
                'hallucination_warning': False,
                'duration_seconds': 0,
                'success': False,
                'error': str(e)
            })

    total_duration = (datetime.now() - start_time).total_seconds()

    # Calculate statistics
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]

    summary = {
        'run_id': 'core-run30',
        'changes': 'Verification fixes: enhanced Step 4, correction factor check, auto-retry',
        'timestamp': datetime.now().isoformat(),
        'total_questions': total_questions,
        'successful': len(successful),
        'failed': len(failed),
        'success_rate': len(successful) / total_questions if total_questions > 0 else 0,
        'total_duration_seconds': total_duration,
        'avg_duration_seconds': total_duration / total_questions if total_questions > 0 else 0,
        'exception_search_count': exception_search_count,
        'nec_comparison_count': nec_comparison_count,
        'hallucination_retry_count': hallucination_retry_count,
        'nec_comparison_forced': False,
        'memory_clearing': True,
        'tool_enforcement': True,
        'notes': 'Enhanced prompt Step 4, correction factor verification, auto-retry on hallucination'
    }

    # Save results
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')

    # JSON output
    json_file = os.path.join(output_dir, f'core-run30_evaluation_results_{date_str}.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': summary,
            'results': results
        }, f, indent=2, ensure_ascii=False)

    # Markdown output
    md_file = os.path.join(output_dir, f'core-run30_evaluation_results_{date_str}.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# Core (NEC) Evaluation Results - Run 30 (Verification Fixes)\n\n")
        f.write(f"**Date:** {date_str}\n")
        f.write(f"**Changes:** Enhanced Step 4, correction factor verification, auto-retry on hallucination\n\n")
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
        f.write(f"| NEC Comparison Used | {nec_comparison_count}/{total_questions} |\n")
        f.write(f"| Hallucination Retries | {hallucination_retry_count}/{total_questions} |\n")
        f.write(f"| Memory Clearing | Enabled |\n")
        f.write(f"| Tool Enforcement | Enabled |\n\n")

        f.write(f"## Results by Question\n\n")
        for r in results:
            f.write(f"### {r['id']}\n\n")
            f.write(f"**Question:** {r['question']}\n\n")
            f.write(f"**Duration:** {r['duration_seconds']:.1f}s\n\n")
            f.write(f"**Tools Called:** {', '.join(r['tools_called']) if r['tools_called'] else 'None'}\n\n")
            if r.get('hallucination_warning'):
                f.write(f"**Note:** Hallucination detected, auto-retried\n\n")
            if r['success']:
                f.write(f"**Answer:**\n\n{r['answer']}\n\n")
            else:
                f.write(f"**Error:** {r['error']}\n\n")
            f.write(f"---\n\n")

    # Print summary
    print(f"\n{'='*60}")
    print(f"EVALUATION COMPLETE - Core Run 30")
    print(f"{'='*60}")
    print(f"Total: {total_questions} | Passed: {len(successful)} | Failed: {len(failed)}")
    print(f"Success Rate: {summary['success_rate']*100:.1f}%")
    print(f"Total Duration: {total_duration:.1f}s (avg {summary['avg_duration_seconds']:.1f}s/question)")
    print(f"Hallucination Retries: {hallucination_retry_count}/{total_questions}")
    print(f"\nOutput files:")
    print(f"  - {json_file}")
    print(f"  - {md_file}")
    print(f"{'='*60}\n")

    return summary, results


if __name__ == '__main__':
    # Paths
    script_dir = Path(__file__).parent
    questions_file = script_dir.parent.parent / 'standardized_llm-as-judge' / 'core_evaluation_simple-text.txt'
    output_dir = script_dir

    # Parse and run
    questions = parse_simple_text_questions(str(questions_file))
    print(f"Loaded {len(questions)} questions")

    summary, results = run_evaluation(questions, str(output_dir))
