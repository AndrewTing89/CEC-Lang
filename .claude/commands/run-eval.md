# Run Evaluation Workflow

You are executing the CEC 2022 evaluation workflow. Follow these steps exactly.

## Arguments
- `$ARGUMENTS` = optional run description (e.g., "prompt improvements")

## Step 1: Determine Next Run Number

Scan `eval/runs/` for existing run folders and find the highest number:
```
eval/runs/run 1/
eval/runs/run 27 - robustness fixes/
```
Extract the number from each folder name (ignore the description suffix). The next run is highest + 1.

## Step 2: Ask for Run Description

If `$ARGUMENTS` is empty, ask the user:
> What's the description for this run? (e.g., "prompt improvements", "tool fixes")

## Step 3: Create Run Folder and Copy Snapshots

Create the new run folder:
```
eval/runs/run {N} - {description}/
```

Create a `snapshots/` subfolder for system file backups:
```
eval/runs/run {N} - {description}/snapshots/
```

**IMMEDIATELY copy these files as snapshots** (before doing anything else):

Using bash `cp` command, copy ALL core system files:
- `core/agent.py` → `snapshots/agent.py.txt`
- `core/tools.py` → `snapshots/tools.py.txt`
- `core/cec_knowledge_tools.py` → `snapshots/cec_knowledge_tools.py.txt`
- `core/cec_table_tools.py` → `snapshots/cec_table_tools.py.txt`
- `core/nec_knowledge_tools.py` → `snapshots/nec_knowledge_tools.py.txt`
- `core/nec_table_tools.py` → `snapshots/nec_table_tools.py.txt`
- `core/opensearch_hybrid_client.py` → `snapshots/opensearch_hybrid_client.py.txt`

Use `.txt` extension so they're easy to read/diff without execution. These are for rollback reference.

**Verify the snapshots folder and files exist before proceeding.**

## Step 4: Generate Evaluation Script

Create a single `run_eval.py` in the run folder with:
- Run ID: `run{N}`
- Questions source: `eval/standardized_llm-as-judge/CEC2022_eval_questions.json`
- Output to the run folder
- Include run description in the script header

Use a previous run's script as a template but update:
- Run number references
- Description/notes
- File output names
- Use the unified question set (53 questions)

## Step 5: Run Evaluation

Execute:
```bash
cd "C:\Users\Andrews Razer Laptop\Desktop\CEC Lang"
python "eval/runs/run {N} - {description}/run_eval.py"
```

Wait for completion. This takes ~30 minutes for 53 questions.

## Step 6: Summary

After the eval completes, report:
- Run folder location
- Files created (JSON + MD)
- Number of questions evaluated
- Suggest running `/judge-eval {N}` to analyze results

## Important Notes

- The unified question set has 53 questions (28 core + 25 CEC)
- Each eval clears agent memory between questions
- If an eval fails mid-run, the partial results are still saved
- Do NOT run multiple evals in parallel (Groq API rate limits)

