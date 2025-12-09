"""
Judge LLM responses on NEC (National Electrical Code) questions.

This script compares responses from different LLMs (Gemini, Claude Sonnet)
against expected answers and generates a scoring report.

Uses an LLM (Claude) as the judge to evaluate technical accuracy.
"""

import json
import os
from pathlib import Path
from anthropic import Anthropic

# Expected answers for baseline questions (ground truth)
EXPECTED_ANSWERS = {
    "baseline-001": {
        "question": "What is the ampacity of 12 AWG copper conductor at 75C termination?",
        "expected": "25 amperes",
        "reference": "NEC Table 310.16 (or 310.15(B)(16))",
        "key_points": [
            "25 amperes is the correct ampacity",
            "Reference to NEC Table 310.16 or 310.15(B)(16)",
            "75C column specifically",
            "Bonus: mentioning 20A overcurrent protection limit per 240.4(D)"
        ]
    },
    "baseline-002": {
        "question": "What size copper conductor is required for a 60A circuit at 75C?",
        "expected": "6 AWG copper",
        "reference": "NEC Table 310.16",
        "key_points": [
            "6 AWG is the minimum size (65A ampacity)",
            "Reference to NEC Table 310.16",
            "Bonus: mentioning 4 AWG for continuous loads (125% rule)"
        ]
    },
    "baseline-003": {
        "question": "Where is GFCI protection required in a residential kitchen?",
        "expected": "All receptacles in kitchen (2023 NEC), or countertop receptacles and within 6 feet of sink (earlier codes)",
        "reference": "NEC 210.8(A)(6)",
        "key_points": [
            "All receptacles in kitchen per 2023 NEC",
            "Countertop receptacles",
            "Within 6 feet of sink",
            "Dishwasher receptacle",
            "Reference to NEC 210.8"
        ]
    },
    "baseline-004": {
        "question": "Is AFCI protection required for bedroom circuits in new residential construction?",
        "expected": "Yes",
        "reference": "NEC 210.12(A)",
        "key_points": [
            "Yes, AFCI is required",
            "All 120V, 15 and 20A circuits",
            "Reference to NEC 210.12",
            "Bonus: expanded to other rooms in recent codes"
        ]
    },
    "baseline-005": {
        "question": "Can aluminum conductors be used for a 200A service? If yes, what size?",
        "expected": "Yes, 4/0 AWG aluminum",
        "reference": "NEC Table 310.16, NEC 310.15(B)(7) or 310.12",
        "key_points": [
            "Yes, aluminum is permitted",
            "4/0 AWG (four-aught) aluminum",
            "Reference to dwelling unit service sizing rules",
            "Bonus: mentioning 83% rule for residential services"
        ]
    },
    "baseline-006": {
        "question": "What is the minimum depth of working clearance required in front of a 120/240V residential electrical panel?",
        "expected": "36 inches (3 feet)",
        "reference": "NEC 110.26(A)(1)",
        "key_points": [
            "36 inches or 3 feet",
            "Reference to NEC 110.26",
            "Bonus: mentioning 30 inch width requirement",
            "Bonus: mentioning 6.5 feet (78 inches) height requirement"
        ]
    },
    "baseline-007": {
        "question": "How many 20-ampere small appliance branch circuits are required for a kitchen?",
        "expected": "Minimum of two (2)",
        "reference": "NEC 210.11(C)(1) and 210.52(B)",
        "key_points": [
            "Minimum of two circuits",
            "20-ampere rating",
            "Reference to NEC 210.11(C)(1) or 210.52(B)",
            "Bonus: mentioning they serve countertop receptacles"
        ]
    },
    "baseline-008": {
        "question": "Is surge protection required for a new 200A residential service according to 2023 NEC?",
        "expected": "Yes",
        "reference": "NEC 230.67",
        "key_points": [
            "Yes, surge protection is required",
            "Reference to NEC 230.67",
            "Type 1 or Type 2 SPD",
            "Bonus: mentioning it applies to service replacement too"
        ]
    }
}


def load_qa_file(filepath):
    """Load Q&A pairs from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def judge_response(client, question_id, question, model_answer, expected_info):
    """Use Claude to judge a single response."""

    prompt = f"""You are an expert NEC (National Electrical Code) evaluator. Your task is to judge the accuracy of an LLM's response to an NEC question.

QUESTION: {question}

EXPECTED ANSWER: {expected_info['expected']}
NEC REFERENCE: {expected_info['reference']}
KEY POINTS TO LOOK FOR:
{chr(10).join(f"- {point}" for point in expected_info['key_points'])}

MODEL'S RESPONSE:
{model_answer}

Please evaluate the response and provide:
1. A score from 0-10 where:
   - 0-3: Incorrect or significantly wrong answer
   - 4-5: Partially correct but missing key information
   - 6-7: Mostly correct with minor issues
   - 8-9: Correct answer with good detail
   - 10: Perfect answer with all key points and proper references

2. A brief explanation of your scoring (2-3 sentences)

3. List any factual errors found

Respond in this exact JSON format:
{{
    "score": <number 0-10>,
    "explanation": "<your explanation>",
    "errors": ["<error 1>", "<error 2>"] or []
}}"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )

    # Parse the JSON response
    response_text = response.content[0].text
    # Find JSON in response
    try:
        # Try to extract JSON from response
        import re
        json_match = re.search(r'\{[\s\S]*\}', response_text)
        if json_match:
            return json.loads(json_match.group())
    except:
        pass

    # Fallback if parsing fails
    return {
        "score": 0,
        "explanation": f"Failed to parse judge response: {response_text[:200]}",
        "errors": ["Parse error"]
    }


def judge_all_responses(qa_data, expected_answers, client):
    """Judge all responses from a model."""
    results = {
        "model": qa_data["model"],
        "source": qa_data["source"],
        "evaluations": [],
        "summary": {}
    }

    total_score = 0
    count = 0

    for qa in qa_data["qa_pairs"]:
        question_id = qa["id"]
        if question_id not in expected_answers:
            print(f"  Skipping {question_id} - no expected answer defined")
            continue

        print(f"  Judging {question_id}...")

        judgment = judge_response(
            client,
            question_id,
            qa["question"],
            qa["answer"],
            expected_answers[question_id]
        )

        evaluation = {
            "id": question_id,
            "question": qa["question"],
            "score": judgment["score"],
            "explanation": judgment["explanation"],
            "errors": judgment["errors"]
        }

        results["evaluations"].append(evaluation)
        total_score += judgment["score"]
        count += 1

    # Calculate summary
    if count > 0:
        results["summary"] = {
            "total_questions": count,
            "total_score": total_score,
            "max_possible": count * 10,
            "average_score": round(total_score / count, 2),
            "percentage": round((total_score / (count * 10)) * 100, 1)
        }

    return results


def generate_report(all_results):
    """Generate a comparison report."""
    report = []
    report.append("=" * 70)
    report.append("NEC LLM EVALUATION REPORT")
    report.append("=" * 70)
    report.append("")

    # Summary comparison
    report.append("SUMMARY COMPARISON")
    report.append("-" * 40)
    for result in all_results:
        model = result["model"]
        summary = result["summary"]
        report.append(f"\n{model}:")
        report.append(f"  Total Score: {summary['total_score']}/{summary['max_possible']}")
        report.append(f"  Average: {summary['average_score']}/10")
        report.append(f"  Percentage: {summary['percentage']}%")

    report.append("")
    report.append("=" * 70)
    report.append("DETAILED EVALUATIONS")
    report.append("=" * 70)

    # Get all question IDs
    all_questions = set()
    for result in all_results:
        for eval_item in result["evaluations"]:
            all_questions.add(eval_item["id"])

    for qid in sorted(all_questions):
        report.append(f"\n{qid}")
        report.append("-" * 40)

        for result in all_results:
            model = result["model"]
            for eval_item in result["evaluations"]:
                if eval_item["id"] == qid:
                    report.append(f"\n  {model}: {eval_item['score']}/10")
                    report.append(f"  {eval_item['explanation']}")
                    if eval_item["errors"]:
                        report.append(f"  Errors: {', '.join(eval_item['errors'])}")
                    break

    return "\n".join(report)


def main():
    eval_dir = Path(r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\eval')

    # Initialize Anthropic client
    client = Anthropic()

    all_results = []

    # Judge Gemini responses
    gemini_file = eval_dir / 'gemini_qa.json'
    if gemini_file.exists():
        print("\nJudging Gemini responses...")
        gemini_data = load_qa_file(gemini_file)
        gemini_results = judge_all_responses(gemini_data, EXPECTED_ANSWERS, client)
        all_results.append(gemini_results)

        # Save individual results
        with open(eval_dir / 'gemini_evaluation.json', 'w', encoding='utf-8') as f:
            json.dump(gemini_results, f, indent=2)
        print(f"  Saved to gemini_evaluation.json")

    # Judge Claude Sonnet responses
    claude_file = eval_dir / 'claude_sonnet_qa.json'
    if claude_file.exists():
        print("\nJudging Claude Sonnet responses...")
        claude_data = load_qa_file(claude_file)
        claude_results = judge_all_responses(claude_data, EXPECTED_ANSWERS, client)
        all_results.append(claude_results)

        # Save individual results
        with open(eval_dir / 'claude_sonnet_evaluation.json', 'w', encoding='utf-8') as f:
            json.dump(claude_results, f, indent=2)
        print(f"  Saved to claude_sonnet_evaluation.json")

    # Generate comparison report
    if all_results:
        report = generate_report(all_results)
        report_file = eval_dir / 'evaluation_report.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {report_file}")
        print("\n" + report)


if __name__ == '__main__':
    main()
