"""
Extract Q&A pairs from ChatGPT HTML exports.
Works with 'Save page as HTML' browser output.
"""

import json
import re
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 not installed. Run: pip install beautifulsoup4")
    sys.exit(1)


def extract_qa_from_chatgpt_html(html_path: Path, model_name: str) -> dict:
    """Extract Q&A pairs from a ChatGPT HTML export."""

    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    qa_pairs = []

    # Find all conversation turns using data-turn attribute
    user_turns = soup.find_all('article', attrs={'data-turn': 'user'})
    assistant_turns = soup.find_all('article', attrs={'data-turn': 'assistant'})

    print(f"Found {len(user_turns)} user turns and {len(assistant_turns)} assistant turns")

    # Match user questions with assistant answers
    # Get all articles in order
    all_articles = soup.find_all('article')

    current_question = None
    question_idx = 0

    for article in all_articles:
        turn = article.get('data-turn', '')

        if turn == 'user':
            # Extract user question text
            text = article.get_text(separator=' ', strip=True)
            # Clean up the text
            text = re.sub(r'\s+', ' ', text).strip()
            if text and len(text) > 10:  # Skip very short texts
                current_question = text

        elif turn == 'assistant' and current_question:
            # Extract assistant answer
            text = article.get_text(separator='\n', strip=True)
            # Clean up
            text = re.sub(r'\n{3,}', '\n\n', text)

            if text and len(text) > 20:
                question_idx += 1

                # First, try to extract ID from the question text itself
                # Pattern: "baseline-001", "core-002", "inspection-005", etc.
                id_match = re.search(r'(baseline-\d{3}|core-\d{3}|inspection-\d{3})', current_question.lower())

                if id_match:
                    qid = id_match.group(1)
                    # Also clean the question text to remove the ID prefix
                    # Pattern like "You said: baseline-001 What is..."
                    clean_q = re.sub(r'^.*?(baseline-\d{3}|core-\d{3}|inspection-\d{3})\s*', '', current_question, flags=re.IGNORECASE)
                    current_question = clean_q.strip()
                else:
                    # Fallback: Determine ID based on question content
                    q_lower = current_question.lower()
                    if 'ampacity' in q_lower and '12 awg' in q_lower:
                        qid = 'baseline-001'
                    elif '60a circuit' in q_lower or '60 amp' in q_lower:
                        qid = 'baseline-002'
                    elif 'gfci' in q_lower and 'kitchen' in q_lower and 'list' not in q_lower:
                        qid = 'baseline-003'
                    elif 'afci' in q_lower and 'bedroom' in q_lower and 'why' not in q_lower:
                        qid = 'baseline-004'
                    elif 'aluminum' in q_lower and '200a' in q_lower:
                        qid = 'baseline-005'
                    elif 'working clearance' in q_lower or 'working space' in q_lower:
                        qid = 'baseline-006'
                    elif 'small appliance' in q_lower and 'how many' in q_lower and 'dining' not in q_lower:
                        qid = 'baseline-007'
                    elif 'surge' in q_lower and 'required' in q_lower and 'where' not in q_lower:
                        qid = 'baseline-008'
                    elif 'upgrade' in q_lower and '100a' in q_lower and '200a' in q_lower:
                        qid = 'core-001'
                    elif 'multiwire' in q_lower and '12/3' in q_lower:
                        qid = 'core-002'
                    elif 'gfci' in q_lower and 'list' in q_lower:
                        qid = 'core-003'
                    elif 'surge' in q_lower and 'where' in q_lower:
                        qid = 'core-004'
                    elif 'closet' in q_lower and '24 inch' in q_lower:
                        qid = 'core-005'
                    elif 'two' in q_lower and '12 awg' in q_lower and 'terminal' in q_lower:
                        qid = 'core-006'
                    elif 'detached garage' in q_lower and '4-wire' in q_lower:
                        qid = 'core-007'
                    elif 'main bonding jumper' in q_lower and 'system bonding' in q_lower:
                        qid = 'core-008'
                    elif 'small appliance' in q_lower and 'dining' in q_lower:
                        qid = 'core-009'
                    elif 'thhn' in q_lower and '50c' in q_lower:
                        qid = 'core-010'
                    elif 'afci' in q_lower and 'why' in q_lower:
                        qid = 'core-011'
                    elif 'torque' in q_lower:
                        qid = 'core-012'
                    elif 'calculate' in q_lower and 'service load' in q_lower:
                        qid = 'inspection-001'
                    elif 'countertop' in q_lower and 'protection' in q_lower:
                        qid = 'inspection-005'
                    elif 'subpanel' in q_lower and 'violation' in q_lower:
                        qid = 'inspection-006'
                    elif 'conduit' in q_lower and 'maximum number' in q_lower:
                        qid = 'inspection-007'
                    elif 'voltage drop' in q_lower:
                        qid = 'inspection-008'
                    elif 'attic' in q_lower and 'tw' in q_lower:
                        qid = 'inspection-009'
                    elif 'parallel' in q_lower and 'gec' in q_lower.lower():
                        qid = 'inspection-010'
                    else:
                        qid = f'qa-{question_idx:03d}'

                qa_pairs.append({
                    'id': qid,
                    'question': current_question,
                    'answer': f"ChatGPT said:\n{text}\nYou said:"
                })

                current_question = None

    return {
        'model': model_name,
        'source': html_path.name,
        'qa_pairs': qa_pairs
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_qa_from_html.py <html_file> <model_name>")
        print("Example: python extract_qa_from_html.py raw_gpt_4o.html 'GPT-4o'")
        sys.exit(1)

    html_path = Path(sys.argv[1])
    model_name = sys.argv[2]

    if not html_path.exists():
        print(f"Error: File not found: {html_path}")
        sys.exit(1)

    print(f"Extracting Q&A from: {html_path}")
    print(f"Model name: {model_name}")

    result = extract_qa_from_chatgpt_html(html_path, model_name)

    print(f"\nExtracted {len(result['qa_pairs'])} Q&A pairs")

    # Output filename
    output_path = html_path.parent / f"extracted_qa_{html_path.stem.replace('raw_', '')}.json"

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Saved to: {output_path}")

    # Print summary
    print("\nExtracted questions:")
    for qa in result['qa_pairs']:
        print(f"  {qa['id']}: {qa['question'][:60]}...")


if __name__ == '__main__':
    main()
