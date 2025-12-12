"""
Re-run specific questions and patch results into run 22 files.
Questions: baseline-001, inspection-007, inspection-009
"""

import json
import sys
import os
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from core.agent import CECAgent

# Questions to re-run
QUESTIONS_TO_RERUN = {
    "baseline-001": "What is the ampacity of a 12 AWG copper conductor with 75°C rated insulation (such as THWN) according to NEC Table 310.16?",
    "inspection-007": "A 1¼-inch rigid metal conduit (RMC) needs to accommodate multiple 10 AWG THHN conductors for a commercial installation. Using NEC Chapter 9 Tables, determine the maximum number of 10 AWG THHN conductors that can be installed in this conduit. Show your calculation.",
    "inspection-009": "A conduit in an attic contains six 12 AWG TW (Type TW, 60°C rated) copper conductors, all current-carrying. The attic ambient temperature reaches 110°F (43°C). Calculate the adjusted ampacity of these conductors after applying both temperature correction and bundling adjustment factors. Show all steps."
}

def run_questions():
    """Run the 3 questions and return results."""
    print("Initializing CECAgent...")
    agent = CECAgent()

    results = []
    for qid, question in QUESTIONS_TO_RERUN.items():
        print(f"\n{'='*60}")
        print(f"Running: {qid}")
        print(f"Question: {question[:80]}...")

        start_time = datetime.now()
        try:
            result = agent.ask(question, force_nec_comparison=True)
            duration = (datetime.now() - start_time).total_seconds()

            # Extract tool calls
            trace = result.get("trace", {})
            tool_calls = trace.get("tool_calls_with_outputs", [])
            tools_called = [tc.get("tool", "unknown") for tc in tool_calls]

            results.append({
                "id": qid,
                "question": question,
                "answer": result.get("answer", ""),
                "success": True,
                "error": None,
                "duration_seconds": duration,
                "tools_called": tools_called,
                "nec_comparison_used": "compare_with_nec" in tools_called,
                "trace": trace
            })
            print(f"SUCCESS - {duration:.1f}s")
            print(f"Tools: {tools_called}")

        except Exception as e:
            duration = (datetime.now() - start_time).total_seconds()
            results.append({
                "id": qid,
                "question": question,
                "answer": None,
                "success": False,
                "error": str(e),
                "duration_seconds": duration,
                "tools_called": [],
                "nec_comparison_used": False,
                "trace": {}
            })
            print(f"ERROR: {e}")

    return results

def patch_json_file(new_results, json_path):
    """Patch the JSON file with new results."""
    print(f"\nPatching JSON: {json_path}")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create lookup of new results by ID
    new_by_id = {r["id"]: r for r in new_results}

    # Check if baseline-001 exists in original
    existing_ids = {r["id"] for r in data["results"]}

    # Update existing or add new
    updated_results = []
    for r in data["results"]:
        if r["id"] in new_by_id:
            print(f"  Replacing: {r['id']}")
            updated_results.append(new_by_id[r["id"]])
            del new_by_id[r["id"]]
        else:
            updated_results.append(r)

    # Add any remaining new results (like baseline-001 if it was missing)
    for qid, r in new_by_id.items():
        print(f"  Adding: {qid}")
        # Insert at correct position
        if qid == "baseline-001":
            updated_results.insert(0, r)  # First
        else:
            updated_results.append(r)

    # Sort by ID to maintain order
    def sort_key(r):
        qid = r["id"]
        if qid.startswith("baseline-"):
            return (0, int(qid.split("-")[1]))
        elif qid.startswith("core-"):
            return (1, int(qid.split("-")[1]))
        elif qid.startswith("inspection-"):
            return (2, int(qid.split("-")[1]))
        return (3, 0)

    updated_results.sort(key=sort_key)
    data["results"] = updated_results

    # Update summary
    data["summary"]["total_questions"] = len(updated_results)
    data["summary"]["successful"] = sum(1 for r in updated_results if r["success"])
    data["summary"]["failed"] = sum(1 for r in updated_results if not r["success"])
    data["summary"]["total_duration_seconds"] = sum(r["duration_seconds"] for r in updated_results)

    # Save
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"  Saved {len(updated_results)} results")

def patch_md_file(new_results, md_path):
    """Regenerate the MD file from the JSON."""
    print(f"\nRegenerating MD: {md_path}")

    # Read the updated JSON
    json_path = md_path.replace('.md', '.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Generate markdown
    lines = []
    lines.append(f"# Core Evaluation Results - Run 22 (Patched)")
    lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"\n## Summary")
    lines.append(f"- Total Questions: {data['summary']['total_questions']}")
    lines.append(f"- Successful: {data['summary']['successful']}")
    lines.append(f"- Failed: {data['summary']['failed']}")
    lines.append(f"- Total Duration: {data['summary']['total_duration_seconds']:.1f}s")
    lines.append(f"\n---\n")

    for r in data["results"]:
        lines.append(f"### {r['id']}")
        lines.append(f"\n**Question:** {r['question']}")
        lines.append(f"\n**Duration:** {r['duration_seconds']:.1f}s | **NEC Comparison:** {'Yes' if r.get('nec_comparison_used') else 'No'}")
        lines.append(f"\n**Tools Called:** {', '.join(r.get('tools_called', []))}")
        lines.append(f"\n**Answer:**\n")
        lines.append(r.get('answer', 'No answer') or 'No answer')
        lines.append(f"\n\n---\n")

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"  Saved markdown")

def main():
    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "core-run22_evaluation_results_2025-12-10.json")
    md_path = os.path.join(base_dir, "core-run22_evaluation_results_2025-12-10.md")

    # Run the 3 questions
    print("="*60)
    print("RE-RUNNING FAILED QUESTIONS")
    print("="*60)
    new_results = run_questions()

    # Patch files
    patch_json_file(new_results, json_path)
    patch_md_file(new_results, md_path)

    print("\n" + "="*60)
    print("COMPLETE")
    print("="*60)

    # Summary of changes
    for r in new_results:
        status = "SUCCESS" if r["success"] else "FAILED"
        print(f"{r['id']}: {status} - Tools: {r['tools_called']}")

if __name__ == "__main__":
    main()
