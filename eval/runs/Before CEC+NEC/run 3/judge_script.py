import json
import re

# Load the evaluation results
with open('C:/Users/Andrews Razer Laptop/Desktop/CEC Lang/eval/run 3/run3-cec_evaluation_results_2025-12-06.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

results = data['results']

# Storage for judgments
judgments = []

for item in results:
    qid = item['id']
    category = item['category']
    question = item['question']
    expected = item['expected_answer']
    actual = item['answer']

    # Print for manual review
    print(f"\n{'='*80}")
    print(f"ID: {qid}")
    print(f"Category: {category}")
    print(f"\nQuestion: {question}")
    print(f"\nExpected Answer:\n{expected}")
    print(f"\nActual Answer:\n{actual}")
    print(f"\n{'-'*80}")

    # Store for later processing
    judgments.append({
        'id': qid,
        'category': category,
        'question': question,
        'expected': expected,
        'actual': actual
    })

# Save judgments for later review
with open('C:/Users/Andrews Razer Laptop/Desktop/CEC Lang/eval/run 3/judgments_data.json', 'w', encoding='utf-8') as f:
    json.dump(judgments, f, indent=2, ensure_ascii=False)

print(f"\n\nTotal questions processed: {len(judgments)}")
