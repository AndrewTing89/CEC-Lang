"""
CEC Lang Agent - LangChain-based California Electrical Code Assistant
Uses Google Gemini 2.5 Pro for reasoning
Includes retry with backoff on rate limits/failures
"""
import os
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
from functools import wraps
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangChain imports
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage

# Local imports
from core.tools import get_all_tools


# ============================================================================
# RETRY DECORATOR (same model, with backoff)
# ============================================================================

def retry_with_backoff(max_retries: int = 5, initial_wait: float = 30.0, max_wait: float = 120.0):
    """
    Decorator that retries the same model with exponential backoff.

    On rate limit (429/413) or overload (503), waits and retries.
    Uses longer waits to respect Groq's TPM limits.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            last_error = None

            for attempt in range(max_retries):
                try:
                    return func(self, *args, **kwargs)

                except Exception as e:
                    last_error = e
                    error_str = str(e).lower()

                    # Rate limit or token limit - wait and retry
                    if any(x in error_str for x in ["rate_limit", "429", "rate limit", "tokens", "413", "quota", "resourceexhausted", "resource_exhausted"]):
                        # Exponential backoff: 30s, 60s, 120s, 120s, 120s
                        wait_time = min(initial_wait * (2 ** attempt), max_wait)
                        if self.verbose:
                            print(f"    [Rate limit] Waiting {wait_time:.0f}s before retry {attempt + 1}/{max_retries}...")
                        time.sleep(wait_time)
                        continue

                    # Model overloaded - wait and retry
                    if "overloaded" in error_str or "503" in error_str or "service unavailable" in error_str:
                        wait_time = min(initial_wait * (2 ** attempt), max_wait)
                        if self.verbose:
                            print(f"    [Overloaded] Waiting {wait_time:.0f}s before retry {attempt + 1}/{max_retries}...")
                        time.sleep(wait_time)
                        continue

                    # Connection/timeout errors - shorter retry
                    if "timeout" in error_str or "connection" in error_str:
                        wait_time = 5 * (attempt + 1)
                        if self.verbose:
                            print(f"    [Connection error] Retrying in {wait_time:.0f}s...")
                        time.sleep(wait_time)
                        continue

                    # Tool use failed (Groq bug: model outputs wrong format) - retry with short wait
                    if "tool_use_failed" in error_str or "failed_generation" in error_str:
                        wait_time = 2 * (attempt + 1)
                        if self.verbose:
                            print(f"    [Tool format error] Retrying in {wait_time:.0f}s ({attempt + 1}/{max_retries})...")
                        time.sleep(wait_time)
                        continue

                    # Unknown error - don't retry, raise immediately
                    raise

            # All retries exhausted
            if last_error:
                raise last_error
            raise RuntimeError("All retries exhausted")

        return wrapper
    return decorator


# ============================================================================
# SYSTEM PROMPT - Full version ported from Gemini Agent
# ============================================================================

SYSTEM_PROMPT = """# CALIFORNIA ELECTRICAL CODE AGENT

You are a California Electrical Code Agent providing CEC-accurate, inspector-grade answers based on CEC 2022.
California uses CEC (based on NEC with California amendments marked [CEC]). CEC is your PRIMARY source.

---

## CORE RULES (MANDATORY)

1. **ALWAYS call tools** - Never answer from memory for code facts
2. **CEC first** - Use cec_* tools for California questions
3. **Exception check** - Always call cec_exception_search after finding base rules
4. **No mental math** - Use python_calculator for all arithmetic
5. **Cite sources** - Every value needs a section/table citation

---

## STRUCTURED REASONING PROTOCOL (MANDATORY)

Before EVERY answer, complete this reasoning chain:

### STEP 1: DECOMPOSE
List ALL sub-questions in the user's question.
```
Example: "Size conductors, EGC, and GEC for 200A service"
→ [1] Service conductor size
→ [2] EGC size
→ [3] GEC size
```

### STEP 2: SEARCH PLAN
For each sub-question, identify which tool(s) to call:
```
→ [1] cec_lookup_conductor_size (conductor_application="service")
→ [2] cec_lookup_grounding_conductor("equipment", "200")
→ [3] cec_lookup_grounding_conductor("electrode", service_conductor_size)
```

### STEP 3: EXECUTE
Call tools in order. For each tool call, briefly state:
- What you're looking for
- Why this tool

### STEP 4: VERIFY RESULTS
After tool calls, check:
- Did I get a result for EACH sub-question?
- If any missing, search again with different terms
- For California-specific topics, also search "Title 24", "CALGreen", "California mandate"

### STEP 5: SYNTHESIZE
Combine all results into coherent answer with citations.

### STEP 6: COMPLETENESS CHECK
Before submitting, verify:
□ Did I address ALL parts of the question?
□ Does answer include SPECIFIC values (not "refer to table")?
□ Are all values from tool results (not memory)?
□ Did I cite section numbers for all requirements?
□ For lists: Did I COUNT and enumerate ALL items?
□ For California topics: Did I check Title 24/CALGreen?

---

## SEARCH STRATEGIES BY QUESTION TYPE

### California-Specific Questions (EV, Solar, Electrification)
ALWAYS search for:
1. Primary CEC article (625 for EV, 690 for solar, etc.)
2. Title 24 / CALGreen terms: "California mandate", "Title 24 Part 6", "CALGreen"
3. CEC 408.2 (panelboard spaces for electrification)
4. Exception search on base rule

### Multi-Component Questions (Sizing service + EGC + GEC)
1. List ALL components at start
2. Look up EACH component separately
3. Verify you got a value for EVERY component
4. Present as structured checklist in answer:
   ```
   ✓ Service conductor: 3/0 AWG copper (Table 310.12(A))
   ✓ EGC: 6 AWG copper (Table 250.122)
   ✓ GEC: 4 AWG copper (Table 250.66)
   ```

### Enumeration Questions ("List all", "How many", "What types")
1. Use limit=15+ in searches
2. Explicitly COUNT items found
3. State count in answer: "There are X items: [list]"
4. If expected count mentioned, verify you found all
5. For table columns, VERIFY column matches question

### Multi-Step Calculations (Derating, Load Calc)
1. Identify ALL factors needed
2. Look up EACH factor from correct table
3. Show calculation with ALL factors applied:
   ```
   Adjusted = Base × Factor1 × Factor2
   = 30A × 0.82 (temp) × 0.80 (bundling)
   = 19.68A
   ```

---

## TOOL REFERENCE

### CEC Tools (PRIMARY)

| Tool | Use For |
|------|---------|
| cec_search(query, limit) | Find CEC rules, sections |
| cec_exception_search(base_rule, context) | Find exceptions (MANDATORY) |
| compare_with_nec(section, query) | CEC vs NEC comparison |
| cec_lookup_conductor_ampacity(size, temp, material) | Ampacity of known size |
| cec_lookup_conductor_size(ampacity, temp, type, application) | Size for required ampacity |
| cec_lookup_grounding_conductor(type, ampacity_or_size) | EGC/GEC sizing |
| cec_lookup_ampacity_adjustment(type, ambient_temp, rating, num_conductors) | Derating factors |
| cec_lookup_working_space(voltage, condition) | Clearance requirements |

### Key Parameters

**conductor_application** for sizing:
- "general" → Table 310.16 (branch circuits, feeders)
- "service" → Table 310.12(A) (dwelling services) - USE FOR SERVICE QUESTIONS

**lookup_type** for grounding:
- "equipment" → Table 250.122 (EGC)
- "electrode" → Table 250.66 (GEC)

### NEC Tools (for comparison only)
Use lookup_* equivalents to get NEC comparison values.

---

## TOOL CALL SEQUENCE

For California Questions:
1. cec_search → base rules
2. cec_exception_search → exceptions (MANDATORY)
3. cec_lookup_* → table values
4. python_calculator → calculations

---

## CRITICAL RULES

### Forward vs Reverse Lookups
- "What is ampacity of 12 AWG?" → cec_lookup_conductor_ampacity (forward)
- "What size for 60A?" → cec_lookup_conductor_size (reverse)

### Table Selection
- SERVICE conductors → conductor_application="service" (Table 310.12(A))
- GENERAL conductors → conductor_application="general" (Table 310.16)

### Cross-References
When tool returns cross_references or applicable_notes mentioning other sections:
- You MUST search for those sections
- Example: Table 310.16 note → "See 240.4(D)" → Search 240.4(D)

### Derating Order
1. Base ampacity from table
2. Temperature correction (Table 310.15(B)(1))
3. Bundling adjustment (Table 310.15(C)(1))
4. Apply BOTH factors: Base × Temp × Bundling

---

## OUTPUT FORMAT

```markdown
## [Answer Title - CEC 2022]

[Direct answer to question with specific values]
[All calculations with intermediate steps]
[All citations: CEC 2022 Section X.X, Table X.X]

✓ Source: CEC 2022
```

---

## EXAMPLES

### Example 1: Multi-Component Sizing

**Question:** "Size the conductors, EGC, and GEC for a 200A residential service in California using copper."

**Reasoning:**
DECOMPOSE: [1] Service conductor [2] EGC [3] GEC
SEARCH PLAN:
- [1] cec_lookup_conductor_size(200, "75°C", "copper", "service")
- [2] cec_lookup_grounding_conductor("equipment", "200")
- [3] cec_lookup_grounding_conductor("electrode", "3/0") after getting service size

**Answer:**
## Service Sizing (CEC 2022)

✓ **Service conductor**: 3/0 AWG copper (CEC Table 310.12(A))
✓ **EGC**: 6 AWG copper (CEC Table 250.122 for 200A)
✓ **GEC**: 4 AWG copper (CEC Table 250.66 for 3/0 service conductor)

✓ Source: CEC 2022

---

### Example 2: California-Specific (EV Charging)

**Question:** "What are California's EV charging requirements for new residential construction?"

**Reasoning:**
DECOMPOSE: [1] CEC electrical requirements [2] Title 24/CALGreen mandates [3] Panelboard requirements
SEARCH PLAN:
- cec_search("EV charging Article 625", limit=10)
- cec_search("CALGreen EV charging mandate", limit=10)
- cec_search("408.2 panelboard EV", limit=10)

**Answer:**
## California EV Charging Requirements (CEC 2022)

1. **Panelboard Space** (CEC 408.2): Reserved circuit breaker space for EV charging
2. **CALGreen/Title 24**: Mandates EV-ready infrastructure including:
   - Dedicated 40-amp minimum circuits
   - Conduit to parking spaces
   - Panel capacity for EV loads
3. **Article 625**: Dedicated branch circuits, GFCI protection, weatherproof enclosures

✓ Source: CEC 2022

---

### Example 3: Enumeration

**Question:** "What medium voltage tables does California have that are not in NEC?"

**Reasoning:**
DECOMPOSE: [1] Find MV tables in CEC [2] Count them [3] Identify table range
SEARCH PLAN: cec_search("medium voltage Table 311.60", limit=15)

**Answer:**
## Medium Voltage Tables (CEC 2022)

CEC has **18** medium voltage tables in the 311.60(C) series:
- Tables 311.60(C)(67) through 311.60(C)(86)
- These provide ampacity for MV cables (2001-35kV)

✓ Source: CEC 2022

---

### Example 4: Table Column Selection

**Question:** "What is the ampacity of 12 AWG flexible cord (Column B thermoset)?"

**Reasoning:**
DECOMPOSE: [1] Flexible cord ampacity [2] Correct table [3] Correct column
SEARCH PLAN: cec_search("Table 400.5 flexible cord ampacity", limit=10)
NOTE: Question specifies "Column B thermoset" - must use Column B value

**Answer:**
## Flexible Cord Ampacity (CEC 2022)

12 AWG flexible cord, **Column B (thermoset)**: **25 amperes**
Per CEC 2022 Table 400.5(A)(1)

✓ Source: CEC 2022

---

### Example 5: Multi-Step Calculation

**Question:** "Calculate adjusted ampacity for 8 AWG THWN copper with 7 conductors at 40°C ambient."

**Reasoning:**
DECOMPOSE: [1] Base ampacity [2] Temp correction [3] Bundling factor [4] Final calculation
SEARCH PLAN:
- cec_lookup_conductor_ampacity("8 AWG", "75°C", "copper")
- cec_lookup_ampacity_adjustment("temperature", 40, "75°C")
- cec_lookup_ampacity_adjustment("bundling", num_conductors=7)

**Answer:**
## Adjusted Ampacity Calculation (CEC 2022)

1. **Base ampacity**: 50A (CEC Table 310.16, 8 AWG @ 75°C)
2. **Temp correction**: 0.88 (CEC Table 310.15(B)(1), 40°C ambient)
3. **Bundling factor**: 0.70 (CEC Table 310.15(C)(1), 7-9 conductors)

**Calculation:**
```
Adjusted = 50A × 0.88 × 0.70 = 30.8A
```

**Final Answer: 30.8 amperes**

✓ Source: CEC 2022

---

### Example 6: Commercial Load Calculation

**Question:** "Calculate general lighting load for a 10,000 sq ft warehouse."

**Reasoning:**
DECOMPOSE: [1] VA per sq ft for WAREHOUSE from Table 220.12 [2] Calculation
SEARCH PLAN: cec_search("Table 220.12 lighting load warehouse", limit=10)
IMPORTANT: Always look up the ACTUAL value from the table - do not assume or use memorized values.

**Answer:**
## Commercial Lighting Load (CEC 2022)

Per CEC Table 220.12:
- **Warehouse/storage**: 0.25 VA per square foot

**Calculation:**
```
10,000 sq ft × 0.25 VA/sq ft = 2,500 VA (2.5 kVA)
```

✓ Source: CEC 2022

---

**Now begin. Follow this system prompt exactly for every question.**
"""


# ============================================================================
# MAIN AGENT CLASS
# ============================================================================

class CECAgent:
    """
    LangGraph-based California Electrical Code Agent
    Uses Google Gemini 2.5 Pro for multi-step reasoning
    """

    def __init__(
        self,
        model_name: str = "gemini-2.5-pro",
        temperature: float = 0.0,
        verbose: bool = True
    ):
        """
        Initialize the CEC Agent

        Args:
            model_name: Groq model to use
            temperature: LLM temperature (0.0 for deterministic)
            verbose: Whether to print debug info
        """
        self.model_name = model_name
        self.temperature = temperature
        self.verbose = verbose

        # Get API key
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        if not self.google_api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")

        # Initialize LLM
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature,
            google_api_key=self.google_api_key,
            max_output_tokens=8192
        )

        # Get tools
        self.tools = get_all_tools()

        # Build tool lookup for fast execution
        self.tool_map = {tool.name: tool for tool in self.tools}

        # Table tools for footnote augmentation (lazy-initialized)
        self._cec_tables = None
        self._nec_tables = None

        # Bind tools to LLM for function calling
        self.llm_with_tools = self.llm.bind_tools(self.tools)

        # Conversation history (simple list)
        self.chat_history: List[Any] = []

        if verbose:
            print(f"[OK] CEC Agent initialized with {model_name}")
            print(f"[OK] Loaded {len(self.tools)} tools")
            print(f"[OK] Custom iteration loop with enforcement checks")

    @property
    def cec_tables(self):
        """Lazy-load CEC table tools on first access."""
        if self._cec_tables is None:
            from core.cec_table_tools import CECTableTools
            self._cec_tables = CECTableTools()
        return self._cec_tables

    @property
    def nec_tables(self):
        """Lazy-load NEC table tools on first access."""
        if self._nec_tables is None:
            from core.nec_table_tools import NECTableTools
            self._nec_tables = NECTableTools()
        return self._nec_tables

    def _execute_tool(self, tool_call: dict) -> str:
        """
        Execute a tool call and return result.

        Args:
            tool_call: Dict with 'name', 'args', and 'id'

        Returns:
            Tool execution result as string
        """
        tool_name = tool_call.get("name", "")
        tool_args = tool_call.get("args", {})

        if tool_name in self.tool_map:
            try:
                result = self.tool_map[tool_name].invoke(tool_args)
                return str(result)
            except Exception as e:
                return f"Error executing {tool_name}: {str(e)}"
        else:
            return f"Error: Tool '{tool_name}' not found"

    def _verify_required_tools(self, question: str, all_tool_calls: List,
                               force_nec_comparison: bool = False) -> tuple:
        """
        Check if required tools were called - simplified enforcement.

        ALL questions require:
        1. At least one search/lookup tool
        2. Exception search (cec_exception_search or nec_exception_search)

        Cross-reference handling (e.g., 240.4 for small conductors) is now handled
        via table footnotes. The lookup tools return applicable_notes and cross_references
        which the model is instructed to follow via the CROSS-REFERENCE RULE in the prompt.

        Args:
            question: The user's original question
            all_tool_calls: List of all tool calls made during the conversation

        Returns:
            Tuple of (is_complete: bool, missing_info: str or None)
        """
        tools_called = {tc.get("name", "") for tc in all_tool_calls}

        # ALL questions require at least one search/lookup
        search_tools = [
            "cec_search", "nec_search", "compare_with_nec",
            "cec_lookup_conductor_ampacity", "lookup_conductor_ampacity",
            "cec_lookup_ampacity_adjustment", "lookup_ampacity_adjustment",
            "cec_lookup_grounding_conductor", "lookup_grounding_conductor",
            "cec_lookup_working_space", "lookup_working_space",
            "search_tables", "get_table_info"
        ]
        has_search = any(t in tools_called for t in search_tools)

        # ALL questions require exception check
        exception_tools = ["cec_exception_search", "nec_exception_search"]
        has_exception = any(t in tools_called for t in exception_tools)

        if not has_search:
            return (False, "search")

        if not has_exception:
            return (False, "exception")

        # Check for NEC comparison if user requested it via checkbox
        if force_nec_comparison:
            has_nec_comparison = "compare_with_nec" in tools_called
            if not has_nec_comparison:
                return (False, "nec_comparison")

        return (True, None)

    def _augment_tool_result_with_footnotes(self, tool_call: dict, result_str: str) -> str:
        """
        Automatically inject footnote context into table lookup results.

        This generic approach detects ANY table lookup, extracts the table ID,
        loads footnotes from the table data, and appends cross-reference guidance.
        This ensures the agent sees all applicable code cross-references without
        requiring hardcoded knowledge of specific sections like 240.4(D).

        Args:
            tool_call: Dict with 'name', 'args', and 'id'
            result_str: The string result from tool execution

        Returns:
            Result string with footnotes appended (if applicable)
        """
        import re

        tool_name = tool_call.get("name", "")

        # Only augment table lookup tools
        table_lookup_tools = [
            # CEC tools
            "cec_lookup_conductor_ampacity",
            "cec_lookup_working_space",
            "cec_lookup_egc_size",
            "cec_lookup_gec_size",
            "cec_lookup_temperature_correction",
            "cec_lookup_ampacity_adjustment",
            "cec_get_table_data",
            # NEC tools
            "lookup_conductor_ampacity",
            "lookup_working_space",
            "lookup_egc_size",
            "lookup_gec_size",
            "lookup_temperature_correction",
            "lookup_ampacity_adjustment",
            "get_table_data",
        ]

        if tool_name not in table_lookup_tools:
            return result_str  # Not a table lookup, return unchanged

        # Extract table ID from result (e.g., "Table 310.16" or "CEC 2022 Table 310.16")
        match = re.search(r'Table\s+([\d\.]+(?:\([A-Za-z0-9]+\))*)', result_str)
        if not match:
            return result_str

        table_id = f"Table {match.group(1)}"

        # Determine which table source to use based on tool name
        try:
            if tool_name.startswith("cec_"):
                table_data = self.cec_tables.get_table_data(table_id)
            else:
                table_data = self.nec_tables.get_table_data(table_id)
        except Exception:
            return result_str  # Error getting table data, return unchanged

        if isinstance(table_data, dict) and "error" in table_data:
            return result_str

        # Build footnote context
        additions = []

        notes = table_data.get("notes", [])
        if notes:
            additions.append("\n\n[TABLE FOOTNOTES]")
            for note in notes:
                marker = note.get("marker") or note.get("number", "")
                text = note.get("text", "")
                if marker:
                    additions.append(f"  [{marker}] {text}")
                else:
                    additions.append(f"  - {text}")

        cross_refs = table_data.get("cross_references", [])
        if cross_refs:
            additions.append(f"\n[CROSS-REFERENCES TO CHECK]: {', '.join(cross_refs)}")
            additions.append("  >> You MUST search for these sections before answering.")

        if additions:
            return result_str + "\n".join(additions)
        return result_str

    @retry_with_backoff(max_retries=5, initial_wait=30.0, max_wait=120.0)
    def _invoke_llm_with_retry(self, messages: List[Any]) -> Any:
        """
        Call LLM with retry on rate limits.
        """
        return self.llm_with_tools.invoke(messages)

    def _run_agent_loop(self, question: str, max_iterations: int = 15,
                        force_nec_comparison: bool = False) -> dict:
        """
        Custom iteration loop with enforcement checks.

        This replaces LangGraph's create_react_agent with a loop we control.
        The model cannot return a final answer until:
        1. At least one search/lookup tool is called
        2. Exception search is called

        Args:
            question: User's question
            max_iterations: Maximum loop iterations (default: 15)

        Returns:
            Dict with answer, tool_calls, and iterations count
        """
        # Build initial messages with system prompt
        messages = [SystemMessage(content=SYSTEM_PROMPT)]
        messages.extend(self.chat_history)
        messages.append(HumanMessage(content=question))

        all_tool_calls = []
        iteration = 0
        last_response = None

        # Trace collection for full transparency
        trace = {
            "iterations": [],
            "tool_calls_with_outputs": []
        }

        while iteration < max_iterations:
            iteration += 1

            if self.verbose:
                print(f"  [Iteration {iteration}] Calling LLM...")

            # SINGLE-STEP APPROACH: Direct tool calling without separate planning step
            # The LLM will reason within its response after seeing tool outputs
            try:
                response = self._invoke_llm_with_retry(messages)  # WITH tools
            except Exception as e:
                if self.verbose:
                    print(f"  [Error] LLM call failed: {e}")
                return {
                    "answer": f"Error: {str(e)}",
                    "tool_calls": all_tool_calls,
                    "iterations": iteration,
                    "error": str(e),
                    "trace": trace
                }

            last_response = response
            has_tool_calls = bool(response.tool_calls) if hasattr(response, 'tool_calls') else False

            # Start tracking this iteration
            iter_trace = {
                "iteration": iteration,
                "llm_content": response.content,  # LLM response content (reasoning + answer combined)
                "tools_called": [],
                "enforcement_triggered": None
            }

            if self.verbose:
                print(f"  [Iteration {iteration}] Tool calls: {len(response.tool_calls) if has_tool_calls else 0}")

            # LAYER 2: ANTI-HALLUCINATION CHECK
            # If first iteration and no tools called, force tool usage
            if iteration == 1 and not has_tool_calls and not all_tool_calls:
                if self.verbose:
                    print("  [!] ANTI-HALLUCINATION: No tool calls in first response. Forcing search.")
                enforcement_msg = "ANTI-HALLUCINATION: Forced tool usage - model tried to answer without calling tools"
                iter_trace["enforcement_triggered"] = enforcement_msg
                trace["iterations"].append(iter_trace)
                messages.append(AIMessage(content=response.content or ""))
                messages.append(HumanMessage(
                    content="ERROR: You MUST call CEC/NEC search tools before answering. "
                           "You cannot answer from memory. Call cec_search NOW to retrieve verified code data."
                ))
                continue  # Force another iteration

            # Execute tool calls if present
            if has_tool_calls:
                messages.append(response)  # Add AI message with tool calls

                for tool_call in response.tool_calls:
                    tool_name = tool_call.get("name", "unknown")
                    tool_id = tool_call.get("id", "")

                    if self.verbose:
                        print(f"    -> Executing: {tool_name}")

                    # Execute tool
                    tool_result_raw = self._execute_tool(tool_call)

                    # Augment table lookup results with footnotes/cross-references
                    tool_result_augmented = self._augment_tool_result_with_footnotes(tool_call, tool_result_raw)

                    all_tool_calls.append(tool_call)

                    # Track detailed tool call with outputs for trace
                    detailed_call = {
                        "tool": tool_name,
                        "input": tool_call.get("args", {}),
                        "output": tool_result_raw,
                        "output_augmented": tool_result_augmented if tool_result_augmented != tool_result_raw else None
                    }
                    iter_trace["tools_called"].append(detailed_call)
                    trace["tool_calls_with_outputs"].append(detailed_call)

                    # Add tool result to messages
                    messages.append(ToolMessage(
                        content=tool_result_augmented,
                        tool_call_id=tool_id
                    ))

                # Save iteration trace and continue
                trace["iterations"].append(iter_trace)
                continue  # Get next response after tool execution

            # No tool calls - model wants to give final answer
            # LAYER 3: Verify required tools were called before allowing answer
            is_complete, missing_type = self._verify_required_tools(question, all_tool_calls, force_nec_comparison)

            if not is_complete:
                if self.verbose:
                    print(f"  [!] INCOMPLETE: Missing {missing_type}. Forcing additional search.")

                enforcement_msg = f"ENFORCEMENT: Missing {missing_type} - forced additional tool call"
                iter_trace["enforcement_triggered"] = enforcement_msg
                trace["iterations"].append(iter_trace)

                messages.append(AIMessage(content=response.content or ""))

                if missing_type == "search":
                    messages.append(HumanMessage(
                        content="INCOMPLETE: You must call cec_search or a lookup tool to verify your answer "
                               "against the code. Call the appropriate search tool NOW."
                    ))
                elif missing_type == "exception":
                    messages.append(HumanMessage(
                        content="INCOMPLETE: You must call cec_exception_search to check for exceptions "
                               "before providing your final answer. This is REQUIRED for every question.\n\n"
                               "Remember the CROSS-REFERENCE RULE from your instructions:\n"
                               "- If any tool returned cross_references or applicable_notes, you MUST follow them\n"
                               "- Search exceptions for the PRIMARY rule you found\n"
                               "- Search for any sections mentioned in footnotes/cross-references\n\n"
                               "Call cec_exception_search NOW with appropriate base_rule and context."
                    ))
                elif missing_type == "nec_comparison":
                    messages.append(HumanMessage(
                        content="INCOMPLETE: User requested NEC comparison. "
                               "Call compare_with_nec with the relevant CEC section "
                               "to show how California code differs from NEC 2023."
                    ))
                continue

            # All checks passed - return final answer
            if self.verbose:
                print(f"  [OK] Returning answer after {iteration} iterations, {len(all_tool_calls)} tool calls")

            # Add final iteration trace (no tools, just final answer)
            trace["iterations"].append(iter_trace)

            return {
                "answer": response.content or "No response generated",
                "tool_calls": all_tool_calls,
                "iterations": iteration,
                "trace": trace
            }

        # Max iterations reached
        if self.verbose:
            print(f"  [!] Max iterations ({max_iterations}) reached")

        return {
            "answer": last_response.content if last_response else "Max iterations reached",
            "tool_calls": all_tool_calls,
            "iterations": iteration,
            "max_iterations_reached": True,
            "trace": trace
        }

    def ask(self, question: str, force_nec_comparison: bool = False) -> Dict[str, Any]:
        """
        Ask the agent a question using custom iteration loop with enforcement.

        The loop ensures:
        1. At least one search/lookup tool is called
        2. Exception search is called
        3. Model cannot return answer until requirements are met
        4. If force_nec_comparison=True, compare_with_nec must be called

        Args:
            question: User's question about electrical codes
            force_nec_comparison: If True, require NEC comparison in response

        Returns:
            Dict with answer, tool_calls, and metadata
        """
        start_time = datetime.now()

        # If NEC comparison requested, append instruction to question
        if force_nec_comparison:
            question = question + "\n\n[INSTRUCTION: Include NEC 2023 comparison. Call compare_with_nec tool.]"

        try:
            # Run custom agent loop with enforcement
            result = self._run_agent_loop(question, force_nec_comparison=force_nec_comparison)

            answer = result.get("answer", "No response generated")
            tool_calls = result.get("tool_calls", [])

            # Format tool calls for output
            formatted_tool_calls = []
            for tc in tool_calls:
                formatted_tool_calls.append({
                    "tool": tc.get("name", "unknown"),
                    "input": tc.get("args", {}),
                    "output": ""
                })

            # Update chat history (keep last 6 messages = 3 exchanges)
            self.chat_history.append(HumanMessage(content=question))
            self.chat_history.append(AIMessage(content=answer))
            if len(self.chat_history) > 6:
                self.chat_history = self.chat_history[-6:]

            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            return {
                "answer": answer,
                "tool_calls": formatted_tool_calls,
                "duration_seconds": duration,
                "model": self.model_name,
                "timestamp": start_time.isoformat(),
                "iterations": result.get("iterations", 0),
                "trace": result.get("trace", {})  # Full execution trace
            }

        except Exception as e:
            import traceback
            error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
            if self.verbose:
                print(error_msg)
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            return {
                "answer": f"Error: {str(e)}",
                "tool_calls": [],
                "error": str(e),
                "model": self.model_name,
                "timestamp": start_time.isoformat(),
                "duration_seconds": duration,
                "trace": {}  # Empty trace on error
            }

    def clear_memory(self):
        """Clear conversation memory"""
        self.chat_history = []


# ============================================================================
# MODULE-LEVEL FUNCTIONS
# ============================================================================

_agent_instance = None


def get_agent() -> CECAgent:
    """Get or create singleton agent instance"""
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = CECAgent()
    return _agent_instance


if __name__ == "__main__":
    # Test the agent
    print("\n=== CEC Lang Agent Test ===\n")

    agent = CECAgent(verbose=True)

    # Test question
    question = "What is the ampacity of 12 AWG copper wire at 75°C?"
    print(f"Question: {question}\n")

    result = agent.ask(question)

    print(f"\nAnswer:\n{result['answer']}")
    print(f"\nTool calls: {len(result['tool_calls'])}")
    for tc in result['tool_calls']:
        print(f"  - {tc['tool']}: {tc['input']}")
    print(f"\nDuration: {result['duration_seconds']:.2f}s")
