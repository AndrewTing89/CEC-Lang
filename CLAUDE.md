# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CEC Lang is a California Electrical Code (CEC 2022) and NEC 2023 question-answering agent built on LangChain with Groq API. It provides inspector-grade electrical code answers using hybrid search (OpenSearch + Google embeddings) and deterministic table lookups.

## Commands

### Run the Streamlit Web Interface
```bash
streamlit run interfaces/streamlit_app.py
```

### Run Evaluation
```bash
# Run CEC evaluation (10 California-specific questions)
python eval/run_evaluation.py --questions cec_evaluation_questions.json --output-dir "run N"

# Run core evaluation (30 general questions)
python eval/run_evaluation.py --questions core_evaluation_questions.json --output-dir "run N"

# Run multi-iteration evaluation (5 iterations for statistical confidence)
python eval/run_multi_evaluation.py --questions core_evaluation_questions.json --output-dir "run N" --iterations 5

# Limit questions for testing
python eval/run_evaluation.py --questions cec_evaluation_questions.json --limit 5
```

### Generate Judge Reports (LLM-as-Judge)
```bash
# After running evaluation, generate judge reports:
python eval/run N/create_core_judge_report.py
python eval/run N/create_cec_judge_report.py
```

## Architecture

### Core Agent Loop (`core/agent.py`)
The `CECAgent` class implements a custom iteration loop with enforcement checks:
1. **Anti-hallucination layer**: Forces tool usage on first response (never answers from memory)
2. **Verification layer**: Requires both search AND exception_search before final answer
3. **NEC comparison layer**: Optional enforcement when user requests California vs NEC comparison

The agent uses `retry_with_backoff` decorator for Groq API rate limit handling (TPM limits).

### Tool System (`core/tools.py`)
Tools are organized by code source:
- **CEC Tools (Primary)**: `cec_search`, `cec_exception_search`, `cec_lookup_*` - Use for California questions
- **NEC Tools (Reference)**: `nec_search`, `nec_exception_search`, `lookup_*` - Use for comparison
- **Table Tools**: Deterministic lookups from JSON data (no LLM involved)
- **Calculator**: Python REPL for electrical calculations

### Hybrid Search (`core/opensearch_hybrid_client.py`)
- Uses OpenSearch k-NN with Google `text-embedding-004` embeddings
- Two indices: `nec_2023_chunks` and `cec_2022_chunks`
- Singleton pattern via `get_hybrid_client()` and `get_cec_hybrid_client()`

### Table Data (`data/`)
- `CEC_2022/cec_tables_unified.json` - California-specific table data with amendments
- `NEC_2023/nec_tables_unified.json` - National code table data
- Table tools (`cec_table_tools.py`, `nec_table_tools.py`) provide deterministic lookups with footnote/cross-reference augmentation

## Key Design Decisions

1. **California-First**: CEC tools are primary; NEC tools are for comparison only
2. **Mandatory Exception Search**: Every answer requires checking for exceptions to the base rule
3. **Tool Result Augmentation**: Table lookups automatically inject footnotes and cross-references (e.g., 240.4(D) for small conductors)
4. **No Mental Math**: Agent forced to use `python_calculator` for all arithmetic
5. **Execution Trace**: Full trace captured in `result["trace"]` for debugging/evaluation

## Environment Variables

Required in `.env`:
- `GROQ_API_KEY` - Groq API key for LLM
- `GOOGLE_API_KEY` - Google API key for embeddings
- `OPENSEARCH_HOST` - OpenSearch host (default: localhost)
- `OPENSEARCH_PORT` - OpenSearch port (default: 9200)

## Evaluation Framework

The `eval/` directory contains:
- Question sets: `cec_evaluation_questions.json` (California-specific), `core_evaluation_questions.json` (general)
- Results stored in `eval/run N/` directories with JSON and Markdown outputs
- LLM-as-Judge scripts generate pass/fail verdicts with reasoning
