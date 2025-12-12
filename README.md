# CEC Lang

**Inspector-Grade California Electrical Code Agent with Zero Hallucination Architecture**

An agentic RAG system built for safety-critical electrical code questions. CEC Lang combines deterministic table lookups, hybrid search, and multi-layer enforcement to achieve **96% accuracy with zero calculation errors** — outperforming raw GPT-4o, Claude Sonnet 4.5, and Gemini 2.5 Pro on complex NEC/CEC questions.

<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-96%25-brightgreen" alt="Accuracy"/>
  <img src="https://img.shields.io/badge/Calculation%20Errors-0-blue" alt="Zero Calculation Errors"/>
  <img src="https://img.shields.io/badge/CEC%20Tables-202-orange" alt="202 Tables"/>
  <img src="https://img.shields.io/badge/Python-3.10+-yellow" alt="Python"/>
</p>

---

## Background

Built for **Skyler Robotics** to power automated residential electrical panel installation. The robot needs a reliable knowledge base for inspection decisions — where hallucinated values could cause code violations or safety hazards.

While computer vision development continues, CEC Lang evolved into an **educational tool for electricians and inspectors**, with architecture designed for downstream automation tasks like:
- Automated permit review
- Real-time inspection assistance
- Code compliance verification
- Load calculation validation

---

## Why Not Just Use ChatGPT?

**Every baseline LLM makes calculation errors on electrical code questions.** This matters when wrong answers can cause fires.

### Baseline LLM Comparison (28 NEC Questions)

| Model | Score | Calculation Errors | Critical Mistakes |
|-------|------:|:------------------:|-------------------|
| **CEC Lang Agent** | **96.79%** | **0** | None |
| Claude Sonnet 4.5 | 96.92% | 2 | Wrong service conductor size |
| ChatGPT 5.1 (GPT-4.1) | 94.62% | 3 | Confused ampacity with OCP limit |
| Gemini 2.5 Pro | 93.93% | 3 | Table lookup errors |
| GPT-4o | 92.50% | 4 | Unit confusion (mm² vs in²) |

**Example: Conduit Fill Calculation**
> "Maximum 10 AWG THHN conductors in 1.25" RMC?"

| Model | Answer | Correct? |
|-------|--------|:--------:|
| CEC Lang | 28 conductors | Yes |
| GPT-4o | **144 conductors** | No (used mm² instead of in²) |
| Gemini | 18 conductors | No |

CEC Lang achieves **zero calculation errors** through deterministic table lookups and mandatory Python REPL usage — not LLM text generation.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           USER QUESTION                                  │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ANTI-HALLUCINATION LAYER                              │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ Iteration 1: MUST use tools (cannot answer from memory)          │    │
│  │ Iteration 2+: Process tool results, extract hints               │    │
│  │ Verification: Enforce required tools based on question type     │    │
│  │ Reflection: Self-verify completeness before final answer        │    │
│  └─────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
    ┌───────────────────┐ ┌─────────────────┐ ┌─────────────────────┐
    │   HYBRID SEARCH   │ │  TABLE LOOKUPS  │ │  PYTHON CALCULATOR  │
    │                   │ │  (Deterministic)│ │                     │
    │ ┌───────────────┐ │ │                 │ │  No mental math     │
    │ │ BM25 Keyword  │ │ │  202 CEC Tables │ │  Verified results   │
    │ │ (exact match) │ │ │  • Ampacity     │ │  Step-by-step       │
    │ └───────────────┘ │ │  • Grounding    │ │                     │
    │ ┌───────────────┐ │ │  • Conduit Fill │ │  Example:           │
    │ │ k-NN Vector   │ │ │  • Working Space│ │  30A × 0.82 × 0.80  │
    │ │ (semantic)    │ │ │  • Derating     │ │  = 19.68A ✓         │
    │ └───────────────┘ │ │                 │ │                     │
    │                   │ │  JSON data →    │ │                     │
    │  CEC 2022 Index   │ │  Exact values   │ │                     │
    │  NEC 2023 Index   │ │  + Footnotes    │ │                     │
    └───────────────────┘ └─────────────────┘ └─────────────────────┘
                    │               │               │
                    └───────────────┼───────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         CROSS-REFERENCE ENFORCEMENT                      │
│                                                                          │
│   Table 310.16 returns: "30A for 12 AWG at 90°C"                        │
│   + Footnote: "See 240.4(D) for OCP limits"                             │
│                                                                          │
│   Agent MUST search 240.4(D) before final answer                        │
│   → Discovers: "12 AWG limited to 20A overcurrent protection"           │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          INSPECTOR-GRADE OUTPUT                          │
│                                                                          │
│   Answer: 20A maximum (Table 310.16 shows 25A @ 75°C, but 240.4(D)      │
│           limits overcurrent protection to 20A for 12 AWG)              │
│                                                                          │
│   + Full execution trace for audit                                       │
│   + All tool calls with inputs/outputs                                   │
│   + Code section citations                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

### Enforcement Flow (What Makes It Different)

```
ITERATION 1: Anti-Hallucination Check
├─ LLM tries: "The ampacity is 20 amperes"
├─ Check: No tool calls detected
└─ REJECT → "ERROR: You MUST call search tools before answering"

ITERATION 2: Forced Tool Usage
├─ LLM calls: cec_lookup_conductor_ampacity("12 AWG", "75°C", "copper")
├─ Tool returns: "25 amperes per Table 310.16"
│                + Footnote: "See 240.4(D) for OCP limits"
├─ Hint extracted: "240.4(D)" → queued for follow-up
└─ Continue...

ITERATION 3: Cross-Reference Lookup (from footnote)
├─ LLM calls: cec_lookup_table("Table 240.4(D)")
├─ Tool returns: "12 AWG copper → 20A max overcurrent protection"
├─ Agent recognizes: Base ampacity (25A) vs OCP limit (20A)
└─ Continue...

ITERATION 4: Synthesis
├─ Agent reasoning: "Table 310.16 shows 25A ampacity, but Table 240.4(D)
│                    limits overcurrent protection to 20A for 12 AWG.
│                    The limiting rule (20A) governs."
└─ Continue...

ITERATION 5: Reflection Phase
├─ Self-check: "Did I answer completely? Are values cited?"
├─ Verification: Required tools called ✓ Cross-references resolved ✓
└─ Return: "25A ampacity per Table 310.16, limited to 20A OCP per 240.4(D)"
```

---

## Key Features

### 1. Deterministic Table Lookups (Zero Guessing)

```python
# LLM Memory (unreliable)
"I think 12 AWG is rated for... 20 amps? Or was it 25?"

# CEC Lang (deterministic)
cec_lookup_conductor_ampacity(
    conductor_size="12 AWG",
    temperature_rating="75°C",
    material="copper"
)
→ Returns: {"ampacity": 25, "table": "310.16", "notes": ["See 240.4(D)"]}
```

**202 CEC Tables** unified in JSON format with:
- Ampacity (Table 310.16, 310.12)
- Grounding conductors (Tables 250.66, 250.122)
- Conduit fill (Chapter 9)
- Working space (Table 110.26)
- Temperature/bundling adjustment factors
- Motor control circuit protection

### 2. California-First Architecture

CEC Lang understands that **CEC 2022 = NEC 2023 + California amendments**:

| Requirement | NEC 2023 | CEC 2022 |
|-------------|----------|----------|
| Panelboard reserved spaces | Not required | Required for heat pumps, EV, cooktops, dryers |
| Surge protection | Required | Required + additional locations |
| Medium voltage tables | 0 tables | 20 California-specific tables |
| Working clearance | 36" (Condition 1) | 30" (some conditions) |

### 3. No Mental Math Policy

The agent is **forbidden from doing arithmetic** in text generation:

```python
# ❌ LLM text generation (error-prone)
"30 × 0.82 × 0.80 = approximately 19.7 amps"

# ✓ Python REPL (verified)
base = 30
temp_factor = 0.82
bundling = 0.80
result = base * temp_factor * bundling
# Output: 19.68 (exact)
```

### 4. Hybrid Search (BM25 + Vector)

| Search Type | Strength | Example |
|-------------|----------|---------|
| BM25 (Keyword) | Exact section matching | "310.16" finds Table 310.16 |
| k-NN (Vector) | Semantic understanding | "wire size for stove" → conductor ampacity |
| Combined | Best of both | Legal language + paraphrased queries |

Two indices: `cec_2022_chunks` and `nec_2023_chunks` for California vs national comparison.

### 5. Full Execution Trace (Audit Trail)

Every answer includes:
```json
{
  "answer": "...",
  "iterations": 5,
  "tools_called": [
    {"tool": "cec_lookup_conductor_ampacity", "input": {...}, "output": "..."},
    {"tool": "cec_search", "input": {...}, "output": "..."}
  ],
  "reflection_used": true,
  "reflection_improved": true,
  "response_time_seconds": 8.3
}
```

Inspectors can verify **exactly which code section** was consulted for every value.

---

## Evaluation Results

### Latest Run (Run 37 — December 2025)

| Metric | Value |
|--------|-------|
| **Total Score** | 509 / 530 (96.0%) |
| **Perfect Scores (10/10)** | 47 / 53 questions |
| **Avg Accuracy** | 4.77 / 5 |
| **Avg Completeness** | 4.83 / 5 |
| **Avg Response Time** | 8.8 seconds |
| **Calculation Errors** | 0 |

### Score Distribution

| Score Range | Count |
|-------------|-------|
| Perfect (10/10) | 47 |
| High (8-9/10) | 5 |
| Medium (5-7/10) | 1 |
| Low (0-4/10) | 0 |

### Categories Tested (53 Questions)

- Table lookups (ampacity, grounding, conduit fill)
- Multi-step calculations (derating, voltage drop, load)
- Code interpretation (GFCI/AFCI requirements, violations)
- California-specific (Title 24, CALGreen, electrification)
- Emerging tech (EV charging, solar PV, heat pumps)
- Inspection scenarios (panel violations, bonding errors)

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| **LLM** | Qwen 3 32B (via Groq) |
| **Framework** | LangChain 0.3+ |
| **Vector Search** | OpenSearch k-NN |
| **Embeddings** | Google text-embedding-004 |
| **Hybrid Search** | BM25 + k-NN (50/50 weighting) |
| **UI** | Streamlit |
| **Tables** | 202 CEC tables in unified JSON |

---

## Quick Start

### Prerequisites

- Python 3.10+
- OpenSearch instance with CEC/NEC indices
- Groq API key (for Qwen LLM)
- Google API key (for embeddings)

### Installation

```bash
git clone https://github.com/AndrewTing89/CEC-Lang.git
cd CEC-Lang
pip install -r requirements.txt
```

### Configuration

Create `.env` file:
```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
OPENSEARCH_HOST=localhost
OPENSEARCH_PORT=9200
```

### Run the Web Interface

```bash
streamlit run interfaces/streamlit_app.py
```

---

## Project Structure

```
CEC-Lang/
├── core/
│   ├── agent.py                    # Custom agent loop with enforcement (1,500+ LOC)
│   ├── tools.py                    # Tool registry (CEC primary, NEC reference)
│   ├── opensearch_hybrid_client.py # Hybrid BM25 + k-NN search
│   ├── cec_knowledge_tools.py      # CEC-specific search tools
│   ├── cec_table_tools.py          # Deterministic table lookups
│   ├── nec_knowledge_tools.py      # NEC reference search
│   └── nec_table_tools.py          # NEC table lookups
│
├── data/
│   ├── CEC_2022/
│   │   └── cec_tables_unified.json # 202 California tables
│   └── NEC_2023/
│       └── nec_tables_unified.json # National code tables
│
├── interfaces/
│   └── streamlit_app.py            # Web UI
│
├── eval/
│   ├── runs/                       # 37+ evaluation runs
│   ├── baseline LLMs/              # GPT-4o, Claude, Gemini comparisons
│   └── standardized_llm-as-judge/  # Evaluation framework
│
└── CLAUDE.md                       # Developer documentation
```

---

## Evaluation Commands

```bash
# Run full evaluation (53 questions)
python eval/standardized_llm-as-judge/run_eval.py

# Generate judge report
python eval/standardized_llm-as-judge/create_judge_report.py

# Analyze wrong answers
python eval/standardized_llm-as-judge/create_wrong_answers_report.py
```

---

## Roadmap

- [ ] Municipal/city code integration (LA, SF, Oakland amendments to CEC)
- [ ] Voice interface for hands-free inspection assistance
- [ ] Integration with permit management systems
- [ ] Computer vision integration for panel photo analysis
- [ ] Mobile app for field inspectors

---

## Contributing

This project was built for Skyler Robotics. For questions or collaboration inquiries, open an issue or reach out directly.

---

## License

MIT License — See [LICENSE](LICENSE) for details.

---

<p align="center">
  <strong>Built for robots. Evolved for electricians. Designed for safety.</strong>
</p>
