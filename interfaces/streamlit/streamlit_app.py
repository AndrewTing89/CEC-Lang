"""
CEC Inspector Assistant - Streamlit Web Interface
California Electrical Code (CEC 2022) with NEC 2023 comparison support
"""
import streamlit as st
import sys
from pathlib import Path
import json
from datetime import datetime
import os
from io import BytesIO

# Voice input
from audio_recorder_streamlit import audio_recorder
from groq import Groq

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.agent import CECAgent

# Agent version for cache invalidation
AGENT_VERSION = "v1.0"

# Initialize session state for page persistence
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Chatbot'

if 'show_tool_calls' not in st.session_state:
    st.session_state.show_tool_calls = False

if 'force_nec_comparison' not in st.session_state:
    st.session_state.force_nec_comparison = False

if 'conversation_messages' not in st.session_state:
    st.session_state.conversation_messages = []

if 'last_audio_bytes' not in st.session_state:
    st.session_state.last_audio_bytes = None

if 'voice_transcription' not in st.session_state:
    st.session_state.voice_transcription = ""


# Page configuration
st.set_page_config(
    page_title="CEC Inspector Assistant",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Red/White Theme
st.markdown("""
<style>
    /* Global white background with black text */
    .main {
        background-color: white;
        color: black;
    }
    .stApp {
        background-color: white;
        color: black;
    }

    /* Remove excessive top padding */
    .block-container {
        padding-top: 1rem !important;
    }

    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #8B0000;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #333;
        margin-bottom: 2rem;
    }
    .citation-verified {
        color: #28a745;
        font-weight: bold;
    }
    .citation-unverified {
        color: #dc3545;
        font-weight: bold;
    }
    .stExpander {
        border: 1px solid #ddd;
        border-radius: 5px;
        background-color: white;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: white;
        color: black !important;
    }
    section[data-testid="stSidebar"] * {
        color: black !important;
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: black !important;
    }
    section[data-testid="stSidebar"] p {
        color: black !important;
    }
    section[data-testid="stSidebar"] label {
        color: black !important;
    }
    section[data-testid="stSidebar"] h3 {
        color: #8B0000 !important;
    }

    /* Button accent color - dark red */
    .stButton>button {
        background-color: #8B0000;
        color: white !important;
    }
    .stButton>button:hover {
        background-color: #A52A2A;
        color: white !important;
    }

    /* Sidebar button text - ensure white on red background */
    section[data-testid="stSidebar"] .stButton>button {
        color: white !important;
    }
    section[data-testid="stSidebar"] .stButton>button p {
        color: white !important;
    }
    section[data-testid="stSidebar"] .stButton>button span {
        color: white !important;
    }

    /* Radio buttons and selectbox accent */
    .stRadio>label, .stSelectbox>label {
        color: black !important;
    }
    .stRadio div[role="radiogroup"] label {
        color: black !important;
    }
    /* Radio button options in sidebar - force all text black */
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p {
        color: black !important;
    }
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label span {
        color: black !important;
    }
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] div {
        color: black !important;
    }

    /* Selectbox dropdown text */
    section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        color: black !important;
    }
    section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
        color: black !important;
        background-color: white !important;
    }
    section[data-testid="stSidebar"] .stSelectbox input {
        color: black !important;
    }
    /* Selectbox selected value */
    section[data-testid="stSidebar"] [role="combobox"] {
        color: black !important;
        background-color: white !important;
    }

    /* Text input and textarea */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: white;
        color: black !important;
        border-color: #ddd;
    }

    /* Placeholder text color - faded gray */
    .stTextArea>div>div>textarea::placeholder {
        color: #999 !important;
        opacity: 1 !important;
    }

    /* Remove extra spacing on text area */
    .stTextArea {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    /* Hide "Made with Streamlit" footer */
    footer {
        display: none !important;
    }

    /* Hide Streamlit header/toolbar */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    .stApp > header {
        display: none !important;
    }
    div[data-testid="stToolbar"] {
        display: none !important;
    }

    /* Metric containers */
    div[data-testid="stMetricValue"] {
        color: #8B0000 !important;
        font-weight: bold !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #8B0000 !important;
        font-weight: bold !important;
    }

    /* Info boxes */
    .stAlert {
        color: black !important;
    }

    /* Links */
    section[data-testid="stSidebar"] a {
        color: #8B0000 !important;
    }

    /* Sidebar horizontal rules (separator lines) */
    section[data-testid="stSidebar"] hr {
        border-top: 1px solid black !important;
        border-bottom: none !important;
        margin: 1rem 0 !important;
    }

    /* Chat message styling */
    .stChatMessage {
        background-color: white !important;
        color: black !important;
    }
    .stChatMessage p {
        color: black !important;
    }
    .stChatMessage div {
        color: black !important;
    }
    .stChatMessage [data-testid="stMarkdownContainer"] {
        color: black !important;
    }
    .stChatMessage [data-testid="stMarkdownContainer"] * {
        color: black !important;
    }

    /* Code element styling for readability */
    .stChatMessage code {
        background-color: #f5f5f5 !important;
        color: black !important;
        padding: 2px 6px !important;
        border-radius: 3px !important;
    }
    .stChatMessage pre {
        background-color: #f5f5f5 !important;
    }
    .stChatMessage pre code {
        background-color: #f5f5f5 !important;
        color: black !important;
    }

    /* Chat input styling - white background with minimal border */
    [data-testid="stChatInput"] {
        background-color: white !important;
    }
    [data-testid="stChatInput"] > div {
        background-color: white !important;
    }
    /* Make all elements white EXCEPT the button */
    [data-testid="stChatInput"] > div > div {
        background-color: white !important;
    }
    [data-testid="stChatInput"] textarea {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ddd !important;
    }
    [data-testid="stChatInput"] textarea:focus,
    [data-testid="stChatInput"] textarea:focus-visible,
    [data-testid="stChatInput"] textarea:active {
        border: 1px solid #ddd !important;
        box-shadow: none !important;
        outline: none !important;
    }
    /* Aggressive focus removal for all parent containers */
    [data-testid="stChatInput"],
    [data-testid="stChatInput"]:focus-within,
    [data-testid="stChatInput"]:focus,
    [data-testid="stChatInput"]:active,
    [data-testid="stChatInput"] > div,
    [data-testid="stChatInput"] > div:focus-within,
    [data-testid="stChatInput"] > div > div,
    [data-testid="stChatInput"] > div > div:focus-within {
        outline: none !important;
        box-shadow: none !important;
        border: none !important;
    }
    /* Remove any Streamlit default focus rings */
    [data-testid="stChatInput"] [data-baseweb="base-input"],
    [data-testid="stChatInput"] [data-baseweb="base-input"]:focus-within,
    [data-testid="stChatInput"] [data-baseweb="base-input"]:focus {
        outline: none !important;
        box-shadow: none !important;
        border: none !important;
    }
    /* Force no ring on wrapper */
    div:has(> [data-testid="stChatInput"]):focus-within {
        outline: none !important;
        box-shadow: none !important;
    }
    [data-testid="stChatInput"] textarea::placeholder {
        color: #999 !important;
    }
    /* Chat input submit button */
    [data-testid="stChatInput"] button {
        background-color: #8B0000 !important;
        color: white !important;
    }
    [data-testid="stChatInput"] button:hover {
        background-color: #A52A2A !important;
    }
    /* Bottom chat input container area */
    .stChatFloatingInputContainer {
        background-color: white !important;
        border-top: 2px solid #8B0000 !important;
    }

    /* Target all bottom container elements to force white background */
    [data-testid="stBottom"] {
        background-color: white !important;
    }
    [data-testid="stBottom"] > div {
        background-color: white !important;
    }
    section[data-testid="stBottom"] {
        background-color: white !important;
    }
    .stBottom {
        background-color: white !important;
    }

    /* About page styling */
    .about-h2 {
        color: #8B0000;
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .about-h3 {
        color: #8B0000;
        font-size: 1.4rem;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    .about-content {
        line-height: 1.8;
        color: black;
    }
    .about-divider {
        border-top: 2px solid #ddd;
        margin: 2rem 0;
    }
    .feature-box {
        background-color: #fafafa;
        border-left: 4px solid #8B0000;
        padding: 15px 20px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .about-content ul {
        margin-left: 1.5rem;
    }
    .about-content li {
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

@st.cache_resource
def get_inspection_system(version: str = AGENT_VERSION):
    """Initialize and cache CEC agent"""
    return CECAgent(verbose=False)


def transcribe_audio(audio_bytes: bytes) -> str:
    """
    Transcribe audio bytes to text using Groq's Whisper API.

    Args:
        audio_bytes: Raw audio data from the recorder

    Returns:
        Transcribed text string
    """
    client = Groq()  # Uses GROQ_API_KEY from environment

    # Create a file-like object from the bytes
    audio_file = BytesIO(audio_bytes)
    audio_file.name = "recording.wav"

    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-large-v3-turbo",
        response_format="text",
        language="en"
    )

    return transcription.strip()


def adapt_agent_result(cec_result):
    """
    Transform CECAgent output to streamlit-compatible format

    Args:
        cec_result: Result from CECAgent.ask()

    Returns:
        Dict with standardized format for streamlit display
    """
    # Build simplified execution trace from iterations
    execution_trace = []
    iterations = cec_result.get('iterations', 0)
    duration_ms = cec_result.get('duration_seconds', 0) * 1000

    # Create simplified trace entry for each iteration
    for i in range(iterations):
        execution_trace.append({
            'step_number': i + 1,
            'step_type': 'iteration',
            'duration_ms': duration_ms / iterations if iterations > 0 else 0
        })

    return {
        'answer': cec_result['answer'],
        'tool_calls': cec_result.get('tool_calls', []),
        'metadata': {
            'total_tokens': 0,  # Placeholder - CECAgent doesn't track tokens
            'tool_calls': cec_result.get('tool_calls', []),
            'model': cec_result.get('model', 'Unknown')
        },
        'execution_trace': execution_trace,
        'execution_summary': {
            'total_steps': iterations,
            'total_tokens': 0,
            'total_duration_ms': duration_ms
        }
    }


@st.cache_data
def load_cec_questions():
    """
    Load and parse CEC evaluation questions

    Returns:
        dict: Questions data organized by tier
    """
    json_path = Path(__file__).parent.parent / "eval" / "standardized_llm-as-judge" / "cec_evaluation_questions.json"

    with open(json_path, 'r') as f:
        data = json.load(f)

    # Organize questions by tier
    all_questions = data['questions']
    questions_by_tier = {
        'california_specific': [q for q in all_questions if q['tier'] == 'california_specific'],
        'delta_table': [q for q in all_questions if q['tier'] == 'delta_table'],
        'calculation': [q for q in all_questions if q['tier'] == 'calculation'],
        'comparison': [q for q in all_questions if q['tier'] == 'comparison']
    }

    return {
        'metadata': {
            'version': data.get('version', 'Unknown'),
            'created': data.get('created', 'Unknown'),
            'description': data.get('description', ''),
            'total_questions': len(all_questions)
        },
        'all_questions': all_questions,
        'by_tier': questions_by_tier
    }


@st.cache_data
def load_nec_questions():
    """
    Load and parse NEC/Core evaluation questions

    Returns:
        dict: Questions data organized by tier
    """
    json_path = Path(__file__).parent.parent / "eval" / "standardized_llm-as-judge" / "core_evaluation_questions.json"

    with open(json_path, 'r') as f:
        data = json.load(f)

    # Organize questions by tier
    all_questions = data['questions']
    questions_by_tier = {
        'baseline': [q for q in all_questions if q['tier'] == 'baseline'],
        'core': [q for q in all_questions if q['tier'] == 'core'],
        'inspection': [q for q in all_questions if q['tier'] == 'inspection']
    }

    return {
        'metadata': {
            'version': data.get('version', 'Unknown'),
            'created': data.get('created', 'Unknown'),
            'description': data.get('description', ''),
            'total_questions': len(all_questions)
        },
        'all_questions': all_questions,
        'by_tier': questions_by_tier
    }


def render_execution_flow(result: dict):
    """
    Render execution flow as a collapsible section

    Args:
        result: The adapted result dictionary
    """
    execution_trace = result.get('execution_trace', [])
    execution_summary = result.get('execution_summary', {})
    all_tool_calls = result.get('tool_calls', [])

    if not execution_trace and not all_tool_calls:
        return

    with st.expander("🔍 Execution Flow", expanded=False):
        # Summary section
        st.markdown(f"""
        **Summary:** {execution_summary.get('total_steps', 0)} iterations |
        {execution_summary.get('total_duration_ms', 0):.0f}ms total |
        {len(all_tool_calls)} tool calls
        """)

        st.markdown("---")

        # Show tool calls
        if all_tool_calls:
            for idx, tc in enumerate(all_tool_calls, 1):
                tool_name = tc.get('tool', 'unknown')
                tool_input = tc.get('input', {})

                # Format input nicely
                input_str = ", ".join([f"{k}={v}" for k, v in tool_input.items() if k != 'limit'])
                if len(input_str) > 80:
                    input_str = input_str[:80] + "..."

                st.markdown(f"""
                **Tool {idx}:** `{tool_name}`
                Parameters: {input_str if input_str else "none"}
                """)


# ============================================================================
# PAGE RENDERING FUNCTIONS
# ============================================================================

def render_cec_question_bank():
    """Render the CEC Question Bank page with California-specific test questions"""
    st.markdown('<div class="main-header">📚 CEC Question Bank</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">30 verified test questions for California Electrical Code evaluation</div>', unsafe_allow_html=True)

    # Load questions
    questions_data = load_cec_questions()
    metadata = questions_data['metadata']
    by_tier = questions_data['by_tier']

    # Tier descriptions
    tier_info = {
        'california_specific': {
            'emoji': '🟢',
            'title': 'California-Specific Requirements',
            'description': 'CEC-only requirements (electrification, EV, solar)',
            'color': '#8B0000'
        },
        'delta_table': {
            'emoji': '🟡',
            'title': 'CEC Table Lookups',
            'description': 'California-amended tables and unique CEC tables',
            'color': '#A52A2A'
        },
        'calculation': {
            'emoji': '🟠',
            'title': 'Calculation Questions',
            'description': 'Multi-step calculations using CEC tables',
            'color': '#8B0000'
        },
        'comparison': {
            'emoji': '🔴',
            'title': 'CEC vs NEC Comparison',
            'description': 'Comparing California code with national NEC',
            'color': '#A52A2A'
        }
    }

    # Display questions by tier
    for tier_key in ['california_specific', 'delta_table', 'calculation', 'comparison']:
        tier_questions = by_tier[tier_key]
        tier_meta = tier_info[tier_key]

        st.markdown(f"""
        <div style="background-color: {tier_meta['color']}; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <p style="color: white; font-size: 1.5rem; font-weight: bold; margin: 0;">
                {tier_meta['emoji']} {tier_meta['title']} ({len(tier_questions)})
            </p>
            <p style="color: white; font-size: 0.9rem; margin: 5px 0 0 0;">
                {tier_meta['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Display each question in this tier
        for i, q in enumerate(tier_questions, 1):
            question_text = q['question']
            question_id = q['id']

            # Create expander for each question
            with st.expander(f"**Q{i}: [{question_id}]** {question_text[:80]}{'...' if len(question_text) > 80 else ''}"):
                # Difficulty
                st.markdown(f"**Difficulty:** {q['difficulty']}/5")
                st.markdown("")

                # Full question
                st.markdown("**📋 Question:**")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{question_text}", unsafe_allow_html=True)
                st.markdown("")

                # CEC Reference
                st.markdown("**📖 CEC Reference:**")
                st.markdown(f"- {q['cec_reference']}")
                st.markdown("")

                # Expected answer
                st.markdown("**✅ Expected Answer:**")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{q['expected_answer']}", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem;">
        <p>💡 <strong>Tip:</strong> Use these questions to test your CEC Inspector Assistant on the Chatbot page.</p>
        <p>These questions focus on California-specific electrical code requirements and amendments.</p>
    </div>
    """, unsafe_allow_html=True)


def render_nec_question_bank():
    """Render the NEC/Core Question Bank page with general NEC test questions"""
    st.markdown('<div class="main-header">📚 NEC Question Bank</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">28 verified test questions for general NEC 2023 evaluation</div>', unsafe_allow_html=True)

    # Load questions
    questions_data = load_nec_questions()
    metadata = questions_data['metadata']
    by_tier = questions_data['by_tier']

    # Tier descriptions
    tier_info = {
        'baseline': {
            'emoji': '🟢',
            'title': 'Baseline Questions',
            'description': 'Simple, direct NEC lookups (Difficulty 1-2)',
            'color': '#8B0000'
        },
        'core': {
            'emoji': '🟡',
            'title': 'Core Questions',
            'description': 'Complex, multi-step reasoning (Difficulty 3-4)',
            'color': '#A52A2A'
        },
        'inspection': {
            'emoji': '🔴',
            'title': 'Inspection Questions',
            'description': 'Real-world inspection scenarios (Difficulty 4-5)',
            'color': '#8B0000'
        }
    }

    # Display questions by tier
    for tier_key in ['baseline', 'core', 'inspection']:
        tier_questions = by_tier[tier_key]
        tier_meta = tier_info[tier_key]

        st.markdown(f"""
        <div style="background-color: {tier_meta['color']}; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <p style="color: white; font-size: 1.5rem; font-weight: bold; margin: 0;">
                {tier_meta['emoji']} {tier_meta['title']} ({len(tier_questions)})
            </p>
            <p style="color: white; font-size: 0.9rem; margin: 5px 0 0 0;">
                {tier_meta['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Display each question in this tier
        for i, q in enumerate(tier_questions, 1):
            question_text = q['question']
            question_id = q['id']

            # Create expander for each question
            with st.expander(f"**Q{i}: [{question_id}]** {question_text[:80]}{'...' if len(question_text) > 80 else ''}"):
                # Difficulty
                st.markdown(f"**Difficulty:** {q['difficulty']}/5")
                st.markdown("")

                # Full question
                st.markdown("**📋 Question:**")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{question_text}", unsafe_allow_html=True)
                st.markdown("")

                # NEC Reference
                st.markdown("**📖 NEC Reference:**")
                nec_ref = q.get('nec_reference', 'N/A')
                st.markdown(f"- {nec_ref}")
                st.markdown("")

                # Expected answer
                st.markdown("**✅ Expected Answer:**")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{q['expected_answer']}", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem;">
        <p>💡 <strong>Tip:</strong> Use these questions to test your CEC Inspector Assistant on the Chatbot page.</p>
        <p>These questions cover general NEC 2023 code requirements (not California-specific).</p>
    </div>
    """, unsafe_allow_html=True)


def render_about_page():
    """Render the About CEC Agent page with styled content"""

    # Main header matching other pages
    st.markdown('<div class="main-header">📖 About CEC Agent</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">AI-powered California Electrical Code assistant with verified citations</div>', unsafe_allow_html=True)

    # Render the content
    st.markdown('<div class="about-content">', unsafe_allow_html=True)

    st.markdown('<h2 class="about-h2">What is CEC Agent?</h2>', unsafe_allow_html=True)
    st.markdown("""
    **CEC Agent** is an AI-powered assistant for the California Electrical Code (CEC 2022) with NEC 2023 comparison support.
    It helps electricians, inspectors, engineers, and students get fast, accurate answers about California electrical
    code requirements with verified citations and calculations.

    Unlike general AI tools that can give incorrect information, CEC Agent is specifically designed to provide
    accurate, trustworthy electrical code guidance you can rely on for professional work in California.
    """)

    st.markdown('<hr class="about-divider">', unsafe_allow_html=True)

    st.markdown('<h2 class="about-h2">California Code (CEC) vs National Code (NEC)</h2>', unsafe_allow_html=True)
    st.markdown("""
    California uses the California Electrical Code (CEC), which is based on the National Electrical Code (NEC)
    but includes California-specific amendments and additions marked with [California Amendment].

    **Key California Differences:**
    - **Electrification Requirements** - Reserved panel spaces for heat pumps, electric cooktops, electric dryers
    - **EV Charging Infrastructure** - Mandatory EV-ready circuits in new construction
    - **Solar PV Mandates** - Required solar installation on new single-family homes (Title 24)
    - **California-Only Tables** - 18+ unique tables not found in the base NEC
    - **Amended Tables** - California modifications to standard NEC tables

    CEC Agent understands both codes and can explain California-specific requirements and how they differ from NEC.
    """)

    st.markdown('<hr class="about-divider">', unsafe_allow_html=True)

    st.markdown('<h2 class="about-h2">The Problem with Standard AI</h2>', unsafe_allow_html=True)
    st.markdown("""
    When you ask regular AI assistants about electrical code:

    - **They hallucinate** - Make up code section numbers that don't exist
    - **They guess table values** - Provide incorrect ampacity ratings or correction factors from memory
    - **They miss exceptions** - Give you general rules without checking for important exceptions
    - **They show bad math** - Do mental calculations that can be wrong instead of showing verified work

    **This is dangerous for electrical work.** You need accurate information you can trust for safety and code compliance.
    """)

    st.markdown('<hr class="about-divider">', unsafe_allow_html=True)

    st.markdown('<h2 class="about-h2">How CEC Agent Solves This</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="about-h3">Anti-Hallucination Features</h3>', unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
    <strong>1. Verified Source Requirement</strong>
    <ul>
    <li>Every code citation must come from the actual CEC/NEC database</li>
    <li>The AI cannot cite sections from memory - it must search and verify first</li>
    <li>You get real section numbers with exact text, not made-up references</li>
    </ul>
    </div>

    <div class="feature-box">
    <strong>2. Deterministic Table Lookups</strong>
    <ul>
    <li>All table values are looked up from official CEC/NEC tables stored as structured data</li>
    <li>No guessing allowed - if a value isn't in the tables, the system says so</li>
    <li>100% accurate table values every time</li>
    </ul>
    </div>

    <div class="feature-box">
    <strong>3. Mandatory Exception Checking</strong>
    <ul>
    <li>Before answering, the system searches for exceptions that might apply</li>
    <li>Prevents giving you general rules when specific exceptions exist</li>
    <li>Ensures complete, contextually accurate answers</li>
    </ul>
    </div>

    <div class="feature-box">
    <strong>4. Transparent Calculations</strong>
    <ul>
    <li>All math is executed step-by-step with Python code</li>
    <li>Every calculation shows the formula, table lookups, and intermediate steps</li>
    <li>You can verify the work yourself</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="about-divider">', unsafe_allow_html=True)

    st.markdown('<h2 class="about-h2">Who is it for?</h2>', unsafe_allow_html=True)
    st.markdown("""
    - **Electricians** - Get quick answers while on the job site in California
    - **Electrical Inspectors** - Verify CEC compliance for installations
    - **Engineers** - Check California requirements during design and planning
    - **Students** - Learn California electrical code with clear explanations
    - **Contractors** - Plan projects with accurate load calculations per CEC
    """)

    st.markdown('<hr class="about-divider">', unsafe_allow_html=True)

    st.markdown('<h2 class="about-h2">What can it do?</h2>', unsafe_allow_html=True)
    st.markdown("""
    1. **Answer CEC Questions with Citations**
       - "What are California's panelboard space requirements for new homes?"
       - Returns verified CEC section references with California amendments

    2. **Compare CEC with NEC**
       - "How do California's GFCI requirements differ from NEC 2023?"
       - Shows California-specific differences and amendments

    3. **Perform California Code Calculations**
       - Ampacity calculations with CEC table values
       - Service conductor sizing per California amendments
       - Load calculations for California buildings
       - Working space clearance verification

    4. **Look Up CEC Table Values**
       - California-amended tables (Table 310.16, 250.122, etc.)
       - California-only tables (18 medium voltage tables, motor control tables, etc.)
       - All standard NEC tables for comparison

    5. **Find Exceptions**
       - Contextual exception searching
       - Identifies California-specific exceptions
       - Prevents incorrect citations
    """)

    st.markdown('<hr class="about-divider">', unsafe_allow_html=True)

    st.markdown('<h2 class="about-h2">Get Started</h2>', unsafe_allow_html=True)
    st.markdown("""
    Ready to get accurate CEC 2022 answers? Simply ask your California electrical code question and CEC Agent will:

    1. Understand what you're asking
    2. Search the relevant CEC sections and tables
    3. Perform any necessary calculations
    4. Provide a clear answer with exact citations

    Whether you're on a California job site, reviewing plans, or studying for an exam, CEC Agent gives you
    fast, reliable electrical code guidance specific to California requirements.
    """)

    st.markdown('</div>', unsafe_allow_html=True)


def render_chatbot_page():
    """Render the main CEC Inspector chatbot page"""
    include_metadata = True  # Always show metadata

    # Main content
    st.markdown('<div class="main-header">⚡ California Electrical Code Assistant</div>', unsafe_allow_html=True)

    # Display welcome message if no conversation yet
    if len(st.session_state.conversation_messages) == 0:
        st.markdown("""
        <div style="color: #999; padding: 40px 20px; line-height: 1.6;">
            <p style="margin-bottom: 1rem;">
                <strong>CEC Agent</strong> is an AI-powered assistant for the California Electrical Code (CEC 2022)
                with NEC 2023 comparison support. It helps electricians, inspectors, engineers, and students get fast,
                accurate answers about California electrical code requirements with verified citations and calculations.
            </p>
            <p style="margin-top: 1rem;">
                Unlike general AI tools that can give incorrect information, CEC Agent is specifically designed
                to provide accurate, trustworthy California electrical code guidance you can rely on for professional work.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Display chat messages using native Streamlit chat components
    for msg in st.session_state.conversation_messages:
        if msg["role"] == "user":
            # User message
            with st.chat_message("user"):
                st.markdown(msg["content"])
        else:
            # Assistant message
            with st.chat_message("assistant"):
                result = msg["result"]

                # Answer
                st.markdown(result['answer'], unsafe_allow_html=False)

                # Tool calls if enabled
                if st.session_state.show_tool_calls and result.get('tool_calls'):
                    with st.expander(f"🔧 Tool calls ({len(result['tool_calls'])})"):
                        for tc in result['tool_calls']:
                            st.markdown(f"**{tc['tool']}**")
                            st.code(str(tc['input']), language="json")

                # Execution flow (collapsible)
                render_execution_flow(result)

                # Metadata if enabled
                if include_metadata and result.get('metadata'):
                    metadata = result['metadata']
                    response_time_ms = result.get('execution_summary', {}).get('total_duration_ms', 0)
                    tool_calls_count = len(metadata.get('tool_calls', []))
                    model = metadata.get('model', 'Unknown')

                    st.markdown(f"""
                    <div style="margin: 5px 0 15px 0; font-size: 0.9rem; color: black;">
                        <span style="color: #8B0000; font-weight: bold;">Model:</span> {model} &nbsp;|&nbsp;
                        <span style="color: #8B0000; font-weight: bold;">Time:</span> {response_time_ms:.0f}ms &nbsp;|&nbsp;
                        <span style="color: #8B0000; font-weight: bold;">Tools:</span> {tool_calls_count}
                    </div>
                    """, unsafe_allow_html=True)

    # Unified input row: [mic] [text input] [send]
    st.markdown("""
    <style>
    /* Style the audio recorder button - white background, red icon */
    iframe[title="audio_recorder_streamlit.audio_recorder"] {
        background-color: white !important;
        border-radius: 8px !important;
    }
    /* Target the recorder container */
    [data-testid="column"]:first-child {
        background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Handle voice transcription first (before rendering input)
    prompt = None

    # Create the input container
    with st.container():
        input_col1, input_col2, input_col3 = st.columns([0.5, 10, 1.2])

        # Mic button (small, red theme)
        with input_col1:
            audio_bytes = audio_recorder(
                text="",
                recording_color="#ff4444",
                neutral_color="#8B0000",
                icon_size="lg",
                pause_threshold=2.0,
                key="voice_recorder"
            )

        # Text input field - use session state key directly for dynamic updates
        with input_col2:
            if "user_question_input" not in st.session_state:
                st.session_state.user_question_input = ""
            user_input = st.text_input(
                "Question",
                placeholder="Ask about CEC 2022 or NEC 2023 electrical codes...",
                label_visibility="collapsed",
                key="user_question_input"
            )

        # Send button
        with input_col3:
            send_clicked = st.button("Ask", type="primary", use_container_width=True)

    # Handle new voice recording
    if audio_bytes and audio_bytes != st.session_state.last_audio_bytes:
        st.session_state.last_audio_bytes = audio_bytes
        with st.spinner("Transcribing..."):
            try:
                transcribed_text = transcribe_audio(audio_bytes)
                if transcribed_text:
                    st.session_state.user_question_input = transcribed_text  # Populate text field directly
                    st.rerun()
            except Exception as e:
                st.error(f"Transcription error: {str(e)}")

    # Process input when send is clicked
    if send_clicked and user_input.strip():
        prompt = user_input.strip()
        st.session_state.user_question_input = ""  # Clear input after sending

    if prompt:
        # Add user message to conversation
        st.session_state.conversation_messages.append({
            "role": "user",
            "content": prompt
        })

        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(prompt)

        # Process and display assistant response
        with st.chat_message("assistant"):
            spinner_text = "🤖 Analyzing California Electrical Code..."
            with st.spinner(spinner_text):
                try:
                    # Get agent and perform analysis
                    agent = get_inspection_system(version=AGENT_VERSION)
                    cec_result = agent.ask(prompt, force_nec_comparison=st.session_state.force_nec_comparison)

                    # Adapt result to streamlit format
                    result = adapt_agent_result(cec_result)

                    # Display answer
                    answer = result.get('answer', '').strip()
                    if not answer:
                        st.warning("⚠️ The assistant did not provide a response. Please try rephrasing your question with more specific details.")
                    else:
                        st.markdown(answer, unsafe_allow_html=False)

                    # Tool calls if enabled
                    if st.session_state.show_tool_calls and result.get('tool_calls'):
                        with st.expander(f"🔧 Tool calls ({len(result['tool_calls'])})"):
                            for tc in result['tool_calls']:
                                st.markdown(f"**{tc['tool']}**")
                                st.code(str(tc['input']), language="json")

                    # Execution flow (collapsible)
                    render_execution_flow(result)

                    # Display metadata if enabled
                    if include_metadata and result.get('metadata'):
                        metadata = result['metadata']
                        response_time_ms = result.get('execution_summary', {}).get('total_duration_ms', 0)
                        tool_calls_count = len(metadata.get('tool_calls', []))
                        model = metadata.get('model', 'Unknown')

                        st.markdown(f"""
                        <div style="margin: 5px 0 15px 0; font-size: 0.9rem; color: black;">
                            <span style="color: #8B0000; font-weight: bold;">Model:</span> {model} &nbsp;|&nbsp;
                            <span style="color: #8B0000; font-weight: bold;">Time:</span> {response_time_ms:.0f}ms &nbsp;|&nbsp;
                            <span style="color: #8B0000; font-weight: bold;">Tools:</span> {tool_calls_count}
                        </div>
                        """, unsafe_allow_html=True)

                    # Add assistant response to conversation
                    st.session_state.conversation_messages.append({
                        "role": "assistant",
                        "result": result
                    })

                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")
                    st.exception(e)
                    # Remove the user message if there was an error
                    st.session_state.conversation_messages.pop()


# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    # Read query parameter to determine page
    query_params = st.query_params
    page_param = query_params.get("page", "chatbot")

    # Update session state based on query parameter
    if page_param == "cec-questions":
        st.session_state.current_page = "CEC Questions"
    elif page_param == "nec-questions":
        st.session_state.current_page = "NEC Questions"
    elif page_param == "about":
        st.session_state.current_page = "About"
    else:
        st.session_state.current_page = "Chatbot"

    # Company/Project name at the top
    st.markdown('<p style="font-size: 2.5rem; font-weight: bold; color: black; margin-bottom: 1rem; text-align: center; border: 2px solid black; padding: 10px; border-radius: 8px;">CEC Lang</p>', unsafe_allow_html=True)

    # Page navigation at the top - clickable button-style links
    st.markdown("### 📑 Navigation")
    st.markdown("""
    <style>
        .nav-button,
        .nav-button:link,
        .nav-button:visited,
        .nav-button:active {
            text-decoration: none !important;
            color: white !important;
            background-color: #8B0000;
            font-size: 1.05rem;
            display: block;
            margin: 10px 0;
            padding: 12px 16px;
            border-radius: 8px;
            text-align: center;
            border: 2px solid #8B0000;
            transition: all 0.3s ease;
        }
        .nav-button:hover {
            background-color: #A52A2A;
            border-color: #A52A2A;
            color: white !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
    </style>
    <div style="margin: 10px 0;">
        <a href="?page=chatbot" class="nav-button">
            💬 Assistant
        </a>
        <a href="?page=cec-questions" class="nav-button">
            📚 CEC Questions
        </a>
        <a href="?page=nec-questions" class="nav-button">
            📘 NEC Questions
        </a>
        <a href="?page=about" class="nav-button">
            📖 About
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Settings section (shown on Chatbot page only)
    if st.session_state.current_page == "Chatbot":
        st.markdown("---")
        st.markdown("### ⚙️ Settings")

        st.session_state.show_tool_calls = st.checkbox(
            "Show tool calls",
            value=st.session_state.show_tool_calls,
            help="Display which tools the agent called during execution"
        )

        st.session_state.force_nec_comparison = st.checkbox(
            "Include NEC comparison",
            value=st.session_state.force_nec_comparison,
            help="Compare California code with national NEC 2023 (adds time)"
        )

    # About section (shown on all pages except About)
    if st.session_state.current_page != "About":
        st.markdown("---")
        st.markdown("### 📊 About")
        if st.session_state.current_page == "Chatbot":
            st.markdown("""
            **CEC Inspector Assistant**

            **Powered by:**
            - 📚 CEC 2022 + NEC 2023 Knowledge Base
            - 🔍 Hybrid Search (BM25 + Vector)
            - 🛠️ Proprietary Custom Tools

            **Anti-Hallucination Features:**
            - **Verified Sources:** All citations from actual CEC/NEC database
            - **Table Lookups:** California-amended and CEC-only tables
            - **Exception Checking:** Automatically searches for exceptions
            - **Transparent Calculations:** Step-by-step Python code
            """)
        elif st.session_state.current_page == "CEC Questions":
            st.markdown("""
            **CEC Question Bank**

            **30 Verified Test Questions**

            Organized by category:
            - 🟢 California-Specific (10)
            - 🟡 Delta Tables (10)
            - 🟠 Calculations (5)
            - 🔴 Comparisons (5)

            Use these to validate CEC Agent performance on California code.
            """)
        elif st.session_state.current_page == "NEC Questions":
            st.markdown("""
            **NEC Question Bank**

            **28 Verified Test Questions**

            Organized by tier:
            - 🟢 Baseline (8): Simple lookups
            - 🟡 Core (12): Complex reasoning
            - 🔴 Inspection (8): Real scenarios

            Use these to validate CEC Agent performance on general NEC.
            """)

        st.markdown("---")

    # Show clear conversation button only on Chatbot page
    if st.session_state.current_page == "Chatbot":
        # Clear conversation button
        st.markdown("### 💬 Conversation")
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            st.session_state.conversation_messages = []
            agent = get_inspection_system(version=AGENT_VERSION)
            agent.clear_memory()
            st.rerun()


# ============================================================================
# MAIN CONTENT - CONDITIONAL PAGE RENDERING
# ============================================================================

if st.session_state.current_page == "Chatbot":
    render_chatbot_page()
elif st.session_state.current_page == "CEC Questions":
    render_cec_question_bank()
elif st.session_state.current_page == "NEC Questions":
    render_nec_question_bank()
else:  # About page
    render_about_page()
