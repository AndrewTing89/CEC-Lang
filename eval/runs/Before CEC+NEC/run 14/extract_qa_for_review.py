"""Extract Q&A pairs from Run 14 evaluation results for LLM review."""
import json
import os

def extract_qa(filepath):
    """Extract questions, expected answers, and agent answers."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results_data = data.get('results', [])
    results = []
    for item in results_data:
        qa = {
            'id': item.get('id', 'unknown'),
            'question': item.get('question', ''),
            'expected_answer': item.get('expected_answer', ''),
            'agent_answer': item.get('answer', ''),  # 'answer' is the key
            'status': item.get('status', ''),
            'cec_reference': item.get('cec_reference', ''),
        }
        results.append(qa)

    return results

def write_all_qa(results, name, outfile):
    """Write all Q&A pairs for review to file."""
    outfile.write(f"\n{'='*80}\n")
    outfile.write(f"  {name.upper()} - {len(results)} questions\n")
    outfile.write('='*80 + '\n')

    for r in results:
        outfile.write(f"\n{'-'*80}\n")
        outfile.write(f"ID: {r['id']}\n")
        outfile.write(f"{'-'*80}\n")
        outfile.write(f"QUESTION: {r['question']}\n")
        outfile.write(f"\nEXPECTED ANSWER: {r['expected_answer']}\n")
        outfile.write(f"\nAGENT ANSWER:\n{r['agent_answer'][:2000]}\n")
        outfile.write(f"\nSTATUS: {r['status']}\n")
        outfile.write(f"CEC REF: {r['cec_reference']}\n")

# Process all three evaluation files
base_dir = r"C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\eval\run 14"

files = [
    "run14-core_evaluation_results_2025-12-09.json",
    "run14-cec_evaluation_results_2025-12-09.json",
    "run14-inspection_results_2025-12-09.json"
]

output_path = os.path.join(base_dir, "qa_review.txt")
with open(output_path, 'w', encoding='utf-8') as outfile:
    all_results = {}
    for input_file in files:
        input_path = os.path.join(base_dir, input_file)
        if os.path.exists(input_path):
            results = extract_qa(input_path)
            name = input_file.split('_')[0].replace('run14-', '')
            all_results[name] = results
            write_all_qa(results, name, outfile)

    outfile.write("\n\nExtraction complete!\n")

print(f"Wrote to: {output_path}")
