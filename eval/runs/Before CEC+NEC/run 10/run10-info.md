# Run 10 - Evaluation Info

## Date
2025-12-09

## What's Being Tested

### 1. LLM Provider: Google Gemini 2.5 Pro
- **Previous runs (1-9):** Groq API with Qwen3 32B / Llama 3.3 70B
- **This run:** Google Gemini 2.5 Pro (`gemini-2.5-pro`)
- **Why:** Testing Gemini's reasoning and tool-calling capabilities for electrical code questions

### 2. True Hybrid Search (BM25 + k-NN)
- **Previous runs (1-9):** Pure k-NN vector search only
- **This run:** True hybrid search combining:
  - **BM25 (keyword search):** Exact matching for section numbers ("310.16"), electrical terms ("GFCI", "AWG")
  - **k-NN (vector search):** Semantic similarity for natural language queries
  - **Weighting:** 50/50 balanced for general search, BM25-heavy for exception search
- **Implementation:** OpenSearch neural-search plugin with `hybrid_search_pipeline`

## Technical Changes

### Search Pipeline
Created OpenSearch search pipeline for score normalization:
```json
{
  "normalization-processor": {
    "normalization": {"technique": "min_max"},
    "combination": {"technique": "arithmetic_mean", "parameters": {"weights": [0.5, 0.5]}}
  }
}
```

### Code Changes
- `core/opensearch_hybrid_client.py`: Updated `hybrid_search()` and `exception_search()` to use `hybrid` query type
- `core/agent.py`: Switched from `ChatGroq` to `ChatGoogleGenerativeAI`

## Expected Improvements
1. **Better exact matches:** Section references like "240.4(D)" and "310.16" should rank higher
2. **Improved exception search:** Keywords like "shall not apply", "not required" matched exactly via BM25
3. **Maintained semantic understanding:** Natural language queries still work via vector search

## Question Sets
- **CEC Evaluation:** 30 California-specific questions
- **Core Evaluation:** 28 general electrical code questions

## Comparison Baseline
Compare results to Run 9 (or earlier) to measure:
- Pass rate improvement
- Response quality for section-specific queries
- Exception finding accuracy
