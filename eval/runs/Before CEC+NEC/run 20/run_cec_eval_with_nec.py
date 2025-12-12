"""
CEC Evaluation with NEC Comparison Enabled - Run 20 (no mandatory exception search)
Runs 30 CEC questions from cec_evaluation_simple-text.txt with force_nec_comparison=True
Testing removal of mandatory exception search enforcement.
"""
import sys
import json
import time
import re
from datetime import datetime
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
load_dotenv()

from core.agent import CECAgent


# Category mapping based on question IDs
CATEGORY_MAP = {
    "cec-001": ("california_specific", "panelboard_requirements"),
    "cec-002": ("california_specific", "ev_charging"),
    "cec-003": ("california_specific", "solar_pv"),
    "cec-004": ("california_specific", "heat_pump"),
    "cec-005": ("california_specific", "electrification"),
    "cec-006": ("california_specific", "electrification"),
    "cec-007": ("california_specific", "overcurrent"),
    "cec-008": ("california_specific", "surge_protection"),
    "cec-009": ("california_specific", "motor_control"),
    "cec-010": ("california_specific", "medium_voltage"),
    "cec-011": ("delta_tables", "conductor_ampacity"),
    "cec-012": ("delta_tables", "grounding"),
    "cec-013": ("delta_tables", "grounding"),
    "cec-014": ("delta_tables", "ampacity_adjustment"),
    "cec-015": ("delta_tables", "ampacity_adjustment"),
    "cec-016": ("delta_tables", "working_space"),
    "cec-017": ("delta_tables", "enclosure"),
    "cec-018": ("delta_tables", "lighting_load"),
    "cec-019": ("delta_tables", "flexible_cord"),
    "cec-020": ("delta_tables", "fixture_wire"),
    "cec-021": ("calculation", "adjusted_ampacity"),
    "cec-022": ("calculation", "service_sizing"),
    "cec-023": ("calculation", "commercial_load"),
    "cec-024": ("calculation", "motor_circuit"),
    "cec-025": ("calculation", "dwelling_load"),
    "cec-026": ("comparison", "gfci"),
    "cec-027": ("comparison", "panelboard"),
    "cec-028": ("comparison", "ev_charging"),
    "cec-029": ("comparison", "afci"),
    "cec-030": ("comparison", "solar_pv"),
}

# NEC reference mapping
NEC_REF_MAP = {
    "cec-001": "N/A - CEC only requirement",
    "cec-002": "NEC 625 (general installation only)",
    "cec-003": "NEC 690 (installation rules only, no mandate)",
    "cec-004": "N/A - CEC only",
    "cec-005": "N/A - CEC only",
    "cec-006": "N/A - CEC only",
    "cec-007": "N/A - CEC only table",
    "cec-008": "N/A - CEC only table",
    "cec-009": "N/A - CEC only table",
    "cec-010": "N/A - CEC only tables",
    "cec-011": "NEC Table 310.16",
    "cec-012": "NEC Table 250.122",
    "cec-013": "NEC Table 250.66",
    "cec-014": "NEC Table 310.15(B)(1)",
    "cec-015": "NEC Table 310.15(C)(1)",
    "cec-016": "NEC Table 110.26(A)(1)",
    "cec-017": "NEC Table 110.28",
    "cec-018": "NEC Table 220.12",
    "cec-019": "NEC Table 400.5(A)(1)",
    "cec-020": "NEC Table 402.3",
    "cec-021": "NEC Tables 310.16, 310.15(B), 310.15(C)",
    "cec-022": "NEC Tables 310.16, 250.122, 250.66",
    "cec-023": "NEC Table 220.12",
    "cec-024": "N/A - CEC only table",
    "cec-025": "NEC Table 220.12",
    "cec-026": "NEC 210.8(A)",
    "cec-027": "NEC 408 (no equivalent requirement)",
    "cec-028": "NEC 625",
    "cec-029": "NEC 210.12",
    "cec-030": "NEC 690",
}

# CEC reference mapping
CEC_REF_MAP = {
    "cec-001": "CEC 408.2",
    "cec-002": "CEC 408.2, Title 24",
    "cec-003": "CEC 690, Title 24 Part 6",
    "cec-004": "CEC 408.2",
    "cec-005": "CEC 408.2",
    "cec-006": "CEC 408.2",
    "cec-007": "CEC 240.4(G), Table 240.4(G)",
    "cec-008": "CEC 242.3, Table 242.3",
    "cec-009": "CEC 430.72(B), Table 430.72(B)",
    "cec-010": "CEC 311.60(C), Tables 311.60(C)(67-86)",
    "cec-011": "CEC Table 310.16",
    "cec-012": "CEC Table 250.122",
    "cec-013": "CEC Table 250.66",
    "cec-014": "CEC Table 310.15(B)(1)(1)",
    "cec-015": "CEC Table 310.15(C)(1)",
    "cec-016": "CEC Table 110.26(A)(1)",
    "cec-017": "CEC Table 110.28",
    "cec-018": "CEC Table 220.12",
    "cec-019": "CEC Table 400.5(A)(1)",
    "cec-020": "CEC Table 402.3",
    "cec-021": "CEC Tables 310.16, 310.15(B)(1)(1), 310.15(C)(1)",
    "cec-022": "CEC Tables 310.16, 250.122, 250.66",
    "cec-023": "CEC Table 220.12",
    "cec-024": "CEC Table 430.72(B)",
    "cec-025": "CEC Table 220.12",
    "cec-026": "CEC 210.8(A)",
    "cec-027": "CEC 408.2",
    "cec-028": "CEC 408.2, Title 24",
    "cec-029": "CEC 210.12",
    "cec-030": "CEC 690, Title 24 Part 6",
}


def parse_simple_text_questions(filepath: Path) -> list:
    """Parse cec_evaluation_simple-text.txt into structured questions."""
    content = filepath.read_text(encoding='utf-8')
    blocks = content.split('-' * 80)

    questions = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        if block.startswith("CEC 2022 Evaluation"):
            cec_match = re.search(r'(cec-001\t.+)', block, re.DOTALL)
            if cec_match:
                block = cec_match.group(1)
            else:
                continue

        if block.startswith("Total:"):
            continue

        lines = block.split('\n')
        first_line = lines[0].strip()

        if '\t' in first_line:
            parts = first_line.split('\t', 1)
            qid = parts[0].strip()
            question = parts[1].strip() if len(parts) > 1 else ""
        else:
            match = re.match(r'^(cec-\d+)\s+(.+)$', first_line)
            if match:
                qid = match.group(1)
                question = match.group(2)
            else:
                continue

        expected = ""
        for i, line in enumerate(lines):
            if line.startswith("EXPECTED ANSWER:"):
                expected = line.replace("EXPECTED ANSWER:", "").strip()
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if not next_line or next_line.startswith("---"):
                        break
                    expected += " " + next_line
                break

        tier, category = CATEGORY_MAP.get(qid, ("california_specific", "general"))
        ca_specific = tier in ("california_specific", "comparison") or qid.startswith("cec-0")

        questions.append({
            "id": qid,
            "tier": tier,
            "category": category,
            "ca_specific": ca_specific,
            "question": question,
            "expected_answer": expected.strip(),
            "cec_reference": CEC_REF_MAP.get(qid, "CEC 2022"),
            "nec_reference": NEC_REF_MAP.get(qid, "NEC 2023"),
        })

    return questions


def extract_citations(answer: str) -> list:
    """Extract section citations from answer text."""
    patterns = [
        r'\b(\d{3}\.\d+(?:\([A-Za-z0-9]+\))?(?:\([A-Za-z0-9]+\))?)\b',
        r'\b(\d{3}\.\d+)\b'
    ]
    citations = set()
    for pattern in patterns:
        matches = re.findall(pattern, answer)
        for m in matches:
            clean = m.strip('.,;:')
            if clean:
                citations.add(clean)
    return sorted(list(citations))


def run_evaluation():
    """Run the full CEC evaluation with NEC comparison enabled."""
    output_dir = Path(__file__).parent
    questions_file = project_root / "eval" / "standardized_llm-as-judge" / "cec_evaluation_simple-text.txt"

    today = datetime.now().strftime("%Y-%m-%d")

    print("\n" + "=" * 70)
    print("CEC EVALUATION - RUN 20 (NO MANDATORY EXCEPTION SEARCH)")
    print("=" * 70)
    print(f"Date: {today}")
    print(f"Questions file: {questions_file}")
    print(f"Output dir: {output_dir}")
    print("NEC Comparison: ENABLED")
    print("\nKey Changes in This Run:")
    print("  - Removed mandatory exception search enforcement")
    print("  - Added cec_lookup_table, nec_lookup_table to search_tools")
    print("  - Relying on footnote augmentation for cross-references")
    print("=" * 70 + "\n")

    print("Parsing questions...")
    questions = parse_simple_text_questions(questions_file)
    print(f"Found {len(questions)} questions\n")

    print("Initializing CEC Agent...")
    agent = CECAgent(verbose=True)
    print(f"Agent ready: {agent.model_name}\n")

    results = []
    successful = 0
    failed = 0
    total_duration = 0.0

    for i, q in enumerate(questions, 1):
        qid = q['id']
        question = q['question']

        print("\n" + "-" * 70)
        print(f"[{i}/{len(questions)}] {qid} ({q['category']})")
        print(f"Question: {question[:80]}..." if len(question) > 80 else f"Question: {question}")
        print("-" * 70)

        agent.chat_history = []

        try:
            start = time.time()
            result = agent.ask(question, force_nec_comparison=True)
            duration = time.time() - start

            answer = result.get('answer', '')
            tool_calls = result.get('tool_calls', [])
            trace = result.get('trace', {})

            tool_names = [tc.get('tool', 'unknown') for tc in tool_calls]
            cec_tools = [t for t in tool_names if t.startswith('cec_') or t in ['python_calculator']]
            nec_tools = [t for t in tool_names if t.startswith('nec_') or t == 'compare_with_nec' or t.startswith('lookup_')]
            citations = extract_citations(answer)
            cec_primary = len(cec_tools) >= len(nec_tools)

            # Track if exception search was called voluntarily
            has_exception_search = any('exception' in t for t in tool_names)

            print(f"Duration: {duration:.1f}s")
            print(f"Tools: {', '.join(tool_names)}")
            print(f"Exception search called: {has_exception_search}")
            print(f"Citations: {len(citations)}")

            results.append({
                "id": qid,
                "tier": q['tier'],
                "category": q['category'],
                "ca_specific": q['ca_specific'],
                "question": question,
                "expected_answer": q['expected_answer'],
                "cec_reference": q['cec_reference'],
                "nec_reference": q['nec_reference'],
                "status": "PASS",
                "answer": answer,
                "tool_calls": tool_calls,
                "cec_tools_used": cec_tools,
                "nec_tools_used": nec_tools,
                "exception_search_called": has_exception_search,
                "citations": citations,
                "duration_seconds": round(duration, 1),
                "cec_primary": cec_primary,
                "trace": trace
            })

            successful += 1
            total_duration += duration

        except Exception as e:
            print(f"ERROR: {e}")
            results.append({
                "id": qid,
                "tier": q['tier'],
                "category": q['category'],
                "ca_specific": q['ca_specific'],
                "question": question,
                "expected_answer": q['expected_answer'],
                "cec_reference": q['cec_reference'],
                "nec_reference": q['nec_reference'],
                "status": "FAIL",
                "answer": f"Error: {str(e)}",
                "tool_calls": [],
                "cec_tools_used": [],
                "nec_tools_used": [],
                "exception_search_called": False,
                "citations": [],
                "duration_seconds": 0,
                "cec_primary": False,
                "trace": {}
            })
            failed += 1

        time.sleep(1)

    avg_duration = total_duration / len(questions) if questions else 0
    success_rate = (successful / len(questions) * 100) if questions else 0

    # Count how many questions called exception search voluntarily
    exception_search_count = sum(1 for r in results if r.get('exception_search_called', False))

    output = {
        "metadata": {
            "date": today,
            "model": agent.model_name,
            "run": 20,
            "prompt_version": "v3 - no mandatory exception search",
            "total_questions": len(questions),
            "successful": successful,
            "failed": failed,
            "success_rate": f"{success_rate:.1f}%",
            "total_duration_seconds": round(total_duration, 1),
            "avg_duration_seconds": round(avg_duration, 1),
            "nec_comparison": True,
            "exception_search_voluntary_count": exception_search_count
        },
        "results": results
    }

    json_path = output_dir / f"run20-cec_evaluation_results_{today}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nJSON saved: {json_path}")

    md_content = generate_markdown_report(output)
    md_path = output_dir / f"run20-cec_evaluation_results_{today}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Markdown saved: {md_path}")

    print("\n" + "=" * 70)
    print("EVALUATION COMPLETE")
    print("=" * 70)
    print(f"Total: {len(questions)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success Rate: {success_rate:.1f}%")
    print(f"Exception Search Called Voluntarily: {exception_search_count}/{len(questions)}")
    print(f"Total Duration: {total_duration:.1f}s")
    print(f"Avg Duration: {avg_duration:.1f}s")
    print("=" * 70 + "\n")

    return output


def generate_markdown_report(data: dict) -> str:
    """Generate markdown report."""
    meta = data['metadata']
    results = data['results']

    md = f"""# CEC Agent Evaluation - Run 20 (No Mandatory Exception Search)

**Date:** {meta['date']}
**Model:** {meta['model']}
**Agent:** California Electrical Code Agent (LangChain)
**NEC Comparison:** ENABLED
**Prompt Version:** {meta.get('prompt_version', 'v3')}

## Key Changes in This Run

1. **Removed mandatory exception search enforcement** - Agent no longer forced to call exception search on every question
2. **Added missing tools to search_tools** - `cec_lookup_table`, `nec_lookup_table`, `cec_lookup_conductor_size`, `nec_lookup_conductor_size`
3. **Relying on footnote augmentation** - Table lookups automatically inject cross-references (e.g., 240.4(D))

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Questions** | {meta['total_questions']} |
| **Successful** | {meta['successful']} ({meta['success_rate']}) |
| **Failed** | {meta['failed']} |
| **Exception Search Called (Voluntary)** | {meta.get('exception_search_voluntary_count', 'N/A')}/{meta['total_questions']} |
| **Total Duration** | {meta['total_duration_seconds']}s |
| **Avg per Question** | {meta['avg_duration_seconds']}s |

---

## Results by Question

"""

    current_tier = None
    tier_names = {
        "california_specific": "California-Unique Requirements",
        "delta_tables": "CEC Delta Tables",
        "calculation": "Complex Calculations",
        "comparison": "CEC vs NEC Comparison"
    }

    for r in results:
        tier = r['tier']
        if tier != current_tier:
            current_tier = tier
            md += f"\n## {tier_names.get(tier, tier)}\n\n"

        ca_tag = " [CA-SPECIFIC]" if r['ca_specific'] else ""
        expected_short = r['expected_answer'][:200] + "..." if len(r['expected_answer']) > 200 else r['expected_answer']
        answer_short = r['answer'][:1500] + "..." if len(r['answer']) > 1500 else r['answer']

        md += f"""### {r['id']}: {r['category']}{ca_tag}

**Question:** {r['question']}

**Expected:** {expected_short}

**Status:** {r['status']}

**Agent Answer:**
{answer_short}

**Tool Usage:**
- CEC Tools: {', '.join(r['cec_tools_used']) if r['cec_tools_used'] else 'None'}
- NEC Tools: {', '.join(r['nec_tools_used']) if r['nec_tools_used'] else 'None'}
- Exception Search Called: {'Yes' if r.get('exception_search_called') else 'No'}

**Citations:** {len(r['citations'])} found

**Response Time:** {r['duration_seconds']}s

---

"""

    cec_primary_count = sum(1 for r in results if r['cec_primary'])
    nec_comparison_used = sum(1 for r in results if 'compare_with_nec' in r['nec_tools_used'])
    lookup_table_used = sum(1 for r in results if 'cec_lookup_table' in r['cec_tools_used'])
    exception_search_count = sum(1 for r in results if r.get('exception_search_called', False))

    md += f"""
## Analysis

### Key Metrics

- **CEC-Primary Responses**: {cec_primary_count}/{len(results)}
- **NEC Comparison Tool Used**: {nec_comparison_used}/{len(results)}
- **cec_lookup_table Used**: {lookup_table_used}/{len(results)}
- **Exception Search Called (Voluntary)**: {exception_search_count}/{len(results)}
- **Success Rate**: {meta['success_rate']}
- **Average Response Time**: {meta['avg_duration_seconds']}s

### Exception Search Analysis

With mandatory exception search removed, the agent now calls it voluntarily based on context.
This should result in:
- Fewer irrelevant exception results polluting answers
- Better answer quality for table description questions (cec-007, cec-008)
- Same quality for questions where exceptions are legitimately relevant

"""

    return md


if __name__ == "__main__":
    run_evaluation()
