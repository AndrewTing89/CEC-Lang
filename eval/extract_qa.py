"""
Extract Q&A pairs from saved HTML files (Gemini and Claude conversations)
and save them as JSON for evaluation.
"""

import re
import json
from bs4 import BeautifulSoup
from pathlib import Path

def extract_gemini_qa(html_path):
    """Extract Q&A pairs from Gemini HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)

    # Clean text - remove special unicode
    text = text.encode('ascii', 'ignore').decode('ascii')

    qa_pairs = []

    # Find all question markers and extract Q&A
    # Pattern matches baseline-XXX, core-XXX, or inspection-XXX followed by question
    lines = text.split('\n')
    current_id = None
    current_question = None
    current_answer_lines = []

    # Pattern to match question IDs (baseline, core, inspection)
    id_pattern = r'^(baseline-\d+|core-\d+|inspection-\d+)[\s\t]+(.+)$'

    for i, line in enumerate(lines):
        # Check if line starts with a question ID
        match = re.match(id_pattern, line.strip())
        if match:
            # Save previous Q&A if exists
            if current_id and current_question:
                answer = '\n'.join(current_answer_lines).strip()
                qa_pairs.append({
                    'id': current_id,
                    'question': current_question,
                    'answer': answer
                })

            # Start new Q&A
            current_id = match.group(1)
            current_question = match.group(2)
            current_answer_lines = []
        elif current_id:
            # Add to current answer
            current_answer_lines.append(line)

    # Don't forget the last Q&A
    if current_id and current_question:
        answer = '\n'.join(current_answer_lines).strip()
        qa_pairs.append({
            'id': current_id,
            'question': current_question,
            'answer': answer
        })

    return qa_pairs


def extract_claude_qa(html_path):
    """Extract Q&A pairs from Claude HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)

    # Clean text - remove special unicode
    text = text.encode('ascii', 'ignore').decode('ascii')

    qa_pairs = []
    lines = text.split('\n')
    current_id = None
    current_question = None
    current_answer_lines = []

    # Pattern to match question IDs (baseline, core, inspection)
    id_pattern = r'^(baseline-\d+|core-\d+|inspection-\d+)[\s\t]+(.+)$'

    for line in lines:
        # Check if line starts with a question ID
        match = re.match(id_pattern, line.strip())
        if match:
            # Save previous Q&A if exists
            if current_id and current_question:
                answer = '\n'.join(current_answer_lines).strip()
                qa_pairs.append({
                    'id': current_id,
                    'question': current_question,
                    'answer': answer
                })

            # Start new Q&A
            current_id = match.group(1)
            current_question = match.group(2)
            current_answer_lines = []
        elif current_id:
            # Add to current answer
            current_answer_lines.append(line)

    # Don't forget the last Q&A
    if current_id and current_question:
        answer = '\n'.join(current_answer_lines).strip()
        qa_pairs.append({
            'id': current_id,
            'question': current_question,
            'answer': answer
        })

    return qa_pairs


def main():
    eval_dir = Path(r'C:\Users\Andrews Razer Laptop\Desktop\CEC Lang\eval')

    # Extract Gemini Q&A
    gemini_html = eval_dir / '_Gemini - direct access to Google AI.html'
    if gemini_html.exists():
        gemini_qa = extract_gemini_qa(gemini_html)
        output_path = eval_dir / 'gemini_qa.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'model': 'Gemini 2.5 Pro',
                'source': str(gemini_html.name),
                'qa_pairs': gemini_qa
            }, f, indent=2)
        print(f"Extracted {len(gemini_qa)} Q&A pairs from Gemini")
        print(f"Saved to: {output_path}")
    else:
        print(f"Gemini HTML not found: {gemini_html}")

    # Extract Claude Q&A
    claude_html = eval_dir / 'NEC LLM test - Anthropic - Sonnet 4.5 - Claude.html'
    if claude_html.exists():
        claude_qa = extract_claude_qa(claude_html)
        output_path = eval_dir / 'claude_sonnet_qa.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'model': 'Claude Sonnet 4.5',
                'source': str(claude_html.name),
                'qa_pairs': claude_qa
            }, f, indent=2)
        print(f"Extracted {len(claude_qa)} Q&A pairs from Claude Sonnet")
        print(f"Saved to: {output_path}")
    else:
        print(f"Claude HTML not found: {claude_html}")


if __name__ == '__main__':
    main()
