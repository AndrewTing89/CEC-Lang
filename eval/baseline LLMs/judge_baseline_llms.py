"""
Judge baseline LLM responses on NEC questions.
Evaluates completeness and accuracy against expected answers.
"""

import json
import os
from pathlib import Path
from datetime import datetime

# Try to import Groq for judging (using your existing setup)
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False
    print("Warning: Groq not available, will use rule-based scoring")


def load_expected_answers(filepath):
    """Load expected answers from core_evaluation_questions.json"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create lookup by ID and by question text (for fuzzy matching)
    by_id = {}
    by_question = {}

    for q in data['questions']:
        by_id[q['id']] = q
        # Normalize question for matching
        normalized = q['question'].lower().strip()[:100]
        by_question[normalized] = q

    return by_id, by_question, data['questions']


def load_qa_file(filepath):
    """Load Q&A pairs from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_expected_answer(qa, expected_by_id, expected_by_question):
    """Find the matching expected answer for a Q&A pair."""
    # First try exact ID match
    if qa['id'] in expected_by_id:
        return expected_by_id[qa['id']]

    # Try matching by question content
    normalized = qa['question'].lower().strip()[:100]
    if normalized in expected_by_question:
        return expected_by_question[normalized]

    # Try partial match
    for norm_q, expected in expected_by_question.items():
        if norm_q[:50] in normalized or normalized[:50] in norm_q:
            return expected

    return None


def judge_with_groq(question, model_answer, expected_info, client):
    """Use Groq LLM to judge a response."""
    prompt = f"""You are an expert NEC (National Electrical Code) evaluator. Judge this LLM response for ACCURACY and COMPLETENESS.

QUESTION: {question}

EXPECTED ANSWER: {expected_info['expected_answer']}
NEC REFERENCE: {expected_info['nec_reference']}

MODEL'S RESPONSE:
{model_answer[:3000]}

Evaluate on two criteria:

1. ACCURACY (0-5 points):
   - 0: Completely wrong or dangerous misinformation
   - 1: Mostly wrong with some correct elements
   - 2: Partially correct but significant errors
   - 3: Mostly correct with minor errors
   - 4: Correct answer with minor omissions
   - 5: Fully accurate, matches expected answer

2. COMPLETENESS (0-5 points):
   - 0: No relevant information provided
   - 1: Very incomplete, missing most key points
   - 2: Partially complete, missing important details
   - 3: Reasonably complete, covers main points
   - 4: Nearly complete, minor details missing
   - 5: Fully complete, all key points covered

Respond in this exact JSON format only:
{{"accuracy": <0-5>, "completeness": <0-5>, "accuracy_notes": "<brief explanation>", "completeness_notes": "<brief explanation>", "errors": ["<error1>", "<error2>"] or []}}"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.1
        )

        response_text = response.choices[0].message.content

        # Parse JSON from response
        import re
        json_match = re.search(r'\{[\s\S]*\}', response_text)
        if json_match:
            result = json.loads(json_match.group())
            result['total'] = result.get('accuracy', 0) + result.get('completeness', 0)
            return result
    except Exception as e:
        print(f"    Groq error: {e}")

    return None


def judge_rule_based(question, model_answer, expected_info):
    """Rule-based scoring as fallback."""
    expected = expected_info['expected_answer'].lower()
    answer = model_answer.lower()

    accuracy = 0
    completeness = 0
    errors = []

    # Check for key terms from expected answer
    key_terms = expected.split()
    key_terms = [t for t in key_terms if len(t) > 3]

    matches = sum(1 for term in key_terms if term in answer)
    match_ratio = matches / len(key_terms) if key_terms else 0

    # Accuracy based on key term matches
    if match_ratio >= 0.8:
        accuracy = 5
    elif match_ratio >= 0.6:
        accuracy = 4
    elif match_ratio >= 0.4:
        accuracy = 3
    elif match_ratio >= 0.2:
        accuracy = 2
    else:
        accuracy = 1

    # Check NEC reference
    nec_ref = expected_info.get('nec_reference', '')
    if nec_ref and nec_ref.lower() in answer:
        accuracy = min(5, accuracy + 1)

    # Completeness based on answer length and detail
    answer_len = len(answer)
    if answer_len > 1000:
        completeness = 5
    elif answer_len > 500:
        completeness = 4
    elif answer_len > 200:
        completeness = 3
    elif answer_len > 100:
        completeness = 2
    else:
        completeness = 1

    return {
        'accuracy': accuracy,
        'completeness': completeness,
        'accuracy_notes': f"Rule-based: {match_ratio:.0%} key term match",
        'completeness_notes': f"Answer length: {answer_len} chars",
        'errors': errors,
        'total': accuracy + completeness
    }


def evaluate_model(qa_data, expected_by_id, expected_by_question, groq_client=None):
    """Evaluate all responses from a model."""
    results = {
        'model': qa_data['model'],
        'source': qa_data['source'],
        'timestamp': datetime.now().isoformat(),
        'evaluations': [],
        'summary': {}
    }

    total_accuracy = 0
    total_completeness = 0
    total_score = 0
    count = 0
    matched = 0

    for qa in qa_data['qa_pairs']:
        expected = find_expected_answer(qa, expected_by_id, expected_by_question)

        if not expected:
            print(f"  Warning: No expected answer for {qa['id']}")
            continue

        matched += 1
        print(f"  Evaluating {qa['id']} (matched to {expected['id']})...")

        # Try Groq first, fallback to rule-based
        if groq_client:
            judgment = judge_with_groq(qa['question'], qa['answer'], expected, groq_client)

        if not groq_client or not judgment:
            judgment = judge_rule_based(qa['question'], qa['answer'], expected)

        evaluation = {
            'id': qa['id'],
            'matched_expected_id': expected['id'],
            'question': qa['question'][:100] + '...',
            'accuracy': judgment['accuracy'],
            'completeness': judgment['completeness'],
            'total': judgment['total'],
            'accuracy_notes': judgment.get('accuracy_notes', ''),
            'completeness_notes': judgment.get('completeness_notes', ''),
            'errors': judgment.get('errors', [])
        }

        results['evaluations'].append(evaluation)
        total_accuracy += judgment['accuracy']
        total_completeness += judgment['completeness']
        total_score += judgment['total']
        count += 1

    # Calculate summary
    if count > 0:
        results['summary'] = {
            'total_questions': count,
            'questions_matched': matched,
            'total_accuracy': total_accuracy,
            'total_completeness': total_completeness,
            'total_score': total_score,
            'max_possible': count * 10,
            'avg_accuracy': round(total_accuracy / count, 2),
            'avg_completeness': round(total_completeness / count, 2),
            'avg_total': round(total_score / count, 2),
            'percentage': round((total_score / (count * 10)) * 100, 1)
        }

    return results


def generate_report(all_results, output_path):
    """Generate a detailed comparison report."""
    lines = []
    lines.append("=" * 80)
    lines.append("NEC BASELINE LLM EVALUATION REPORT")
    lines.append("=" * 80)
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Summary comparison table
    lines.append("SUMMARY COMPARISON")
    lines.append("-" * 80)
    lines.append(f"{'Model':<25} {'Accuracy':>10} {'Complete':>10} {'Total':>10} {'Percent':>10}")
    lines.append("-" * 80)

    for result in all_results:
        model = result['model'][:24]
        summary = result['summary']
        lines.append(f"{model:<25} {summary['avg_accuracy']:>10.2f} {summary['avg_completeness']:>10.2f} {summary['avg_total']:>10.2f} {summary['percentage']:>9.1f}%")

    lines.append("-" * 80)
    lines.append("")

    # Score interpretation
    lines.append("SCORE INTERPRETATION")
    lines.append("-" * 40)
    lines.append("Accuracy (0-5): How correct is the answer?")
    lines.append("Completeness (0-5): How thorough is the answer?")
    lines.append("Total (0-10): Combined score")
    lines.append("Percentage: Total / Max possible * 100")
    lines.append("")

    # Detailed breakdown by tier
    lines.append("=" * 80)
    lines.append("SCORES BY QUESTION TIER")
    lines.append("=" * 80)

    for tier in ['baseline', 'core', 'inspection']:
        lines.append(f"\n{tier.upper()} QUESTIONS")
        lines.append("-" * 60)

        for result in all_results:
            tier_evals = [e for e in result['evaluations'] if e['id'].startswith(tier)]
            if tier_evals:
                avg_score = sum(e['total'] for e in tier_evals) / len(tier_evals)
                lines.append(f"  {result['model']}: {avg_score:.2f}/10 avg ({len(tier_evals)} questions)")

    # Detailed per-question comparison
    lines.append("")
    lines.append("=" * 80)
    lines.append("DETAILED QUESTION-BY-QUESTION COMPARISON")
    lines.append("=" * 80)

    # Get all unique question IDs
    all_ids = set()
    for result in all_results:
        for e in result['evaluations']:
            all_ids.add(e['id'])

    for qid in sorted(all_ids):
        lines.append(f"\n{qid}")
        lines.append("-" * 60)

        for result in all_results:
            for e in result['evaluations']:
                if e['id'] == qid:
                    lines.append(f"  {result['model']}:")
                    lines.append(f"    Accuracy: {e['accuracy']}/5 - {e.get('accuracy_notes', '')}")
                    lines.append(f"    Completeness: {e['completeness']}/5 - {e.get('completeness_notes', '')}")
                    lines.append(f"    Total: {e['total']}/10")
                    if e.get('errors'):
                        lines.append(f"    Errors: {', '.join(e['errors'])}")
                    break

    # Write report
    report_text = '\n'.join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_text)

    return report_text


def main():
    base_dir = Path(r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\eval')
    llm_dir = base_dir / 'baseline LLMs'

    # Load expected answers
    expected_path = base_dir / 'core_evaluation_questions.json'
    print(f"Loading expected answers from: {expected_path}")
    expected_by_id, expected_by_question, all_expected = load_expected_answers(expected_path)
    print(f"Loaded {len(all_expected)} expected answers")

    # Initialize Groq client if available
    groq_client = None
    if GROQ_AVAILABLE:
        api_key = os.environ.get('GROQ_API_KEY')
        if api_key:
            groq_client = Groq(api_key=api_key)
            print("Using Groq LLM for judging")
        else:
            print("GROQ_API_KEY not set, using rule-based scoring")

    all_results = []

    # Evaluate Gemini
    gemini_path = llm_dir / 'gemini_qa.json'
    if gemini_path.exists():
        print(f"\nEvaluating Gemini responses...")
        gemini_data = load_qa_file(gemini_path)
        gemini_results = evaluate_model(gemini_data, expected_by_id, expected_by_question, groq_client)
        all_results.append(gemini_results)

        # Save individual results
        with open(llm_dir / 'gemini_evaluation.json', 'w', encoding='utf-8') as f:
            json.dump(gemini_results, f, indent=2)
        print(f"  Saved to gemini_evaluation.json")

    # Evaluate Claude Sonnet
    claude_path = llm_dir / 'claude_sonnet_qa.json'
    if claude_path.exists():
        print(f"\nEvaluating Claude Sonnet responses...")
        claude_data = load_qa_file(claude_path)
        claude_results = evaluate_model(claude_data, expected_by_id, expected_by_question, groq_client)
        all_results.append(claude_results)

        # Save individual results
        with open(llm_dir / 'claude_sonnet_evaluation.json', 'w', encoding='utf-8') as f:
            json.dump(claude_results, f, indent=2)
        print(f"  Saved to claude_sonnet_evaluation.json")

    # Generate comparison report
    if all_results:
        report_path = llm_dir / 'evaluation_report.txt'
        report = generate_report(all_results, report_path)
        print(f"\nReport saved to: {report_path}")
        print("\n" + report)

        # Also save as JSON
        summary_path = llm_dir / 'evaluation_summary.json'
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'models': [r['model'] for r in all_results],
                'summaries': {r['model']: r['summary'] for r in all_results}
            }, f, indent=2)
        print(f"Summary saved to: {summary_path}")


if __name__ == '__main__':
    main()
