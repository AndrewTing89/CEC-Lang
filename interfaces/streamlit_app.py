"""
CEC Lang Streamlit Interface
California Electrical Code Assistant powered by LangChain + Groq
"""
import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.agent import CECAgent

# Page configuration
st.set_page_config(
    page_title="CEC Inspector Assistant",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
    }
    .tool-call {
        background-color: #f0f2f6;
        padding: 0.5rem;
        border-radius: 0.25rem;
        margin: 0.25rem 0;
        font-size: 0.85rem;
    }
    .main-header {
        text-align: center;
        padding: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    st.session_state.agent = None

if "show_tool_calls" not in st.session_state:
    st.session_state.show_tool_calls = False


@st.cache_resource
def get_agent():
    """Initialize and cache the CEC agent"""
    try:
        return CECAgent(verbose=False)
    except Exception as e:
        st.error(f"Failed to initialize agent: {e}")
        return None


# Sidebar
with st.sidebar:
    st.title("⚡ CEC Inspector")
    st.markdown("---")

    st.markdown("### Settings")
    st.session_state.show_tool_calls = st.checkbox(
        "Show tool calls",
        value=st.session_state.show_tool_calls,
        help="Display which tools the agent called"
    )

    st.markdown("---")

    st.markdown("### About")
    st.markdown("""
    **CEC Lang** is a California Electrical Code assistant powered by:
    - **LangChain** for agent orchestration
    - **Groq API** with Llama 3.3 70B
    - **LangSmith** for tracing

    **Primary Source:** CEC 2022 (California)
    **Reference:** NEC 2023 (National)
    """)

    st.markdown("---")

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        if st.session_state.agent:
            st.session_state.agent.clear_memory()
        st.rerun()

    st.markdown("---")

    st.markdown("### Example Questions")
    examples = [
        "What is the ampacity of 12 AWG copper at 75°C?",
        "What working space is required for a 480V panel?",
        "What size equipment grounding conductor for a 100A circuit?",
        "Are there exceptions to GFCI requirements in kitchens?",
    ]
    for ex in examples:
        if st.button(ex, key=f"ex_{ex[:20]}"):
            st.session_state.pending_question = ex


# Main content
st.markdown("<h1 class='main-header'>⚡ California Electrical Code Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Ask questions about CEC 2022 and NEC 2023 electrical codes</p>", unsafe_allow_html=True)

# Initialize agent
agent = get_agent()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        # Show tool calls if enabled
        if message["role"] == "assistant" and st.session_state.show_tool_calls:
            if "tool_calls" in message and message["tool_calls"]:
                with st.expander(f"🔧 Tool calls ({len(message['tool_calls'])})"):
                    for tc in message["tool_calls"]:
                        st.markdown(f"**{tc['tool']}**")
                        st.code(str(tc['input']), language="json")

# Handle pending question from example buttons
if "pending_question" in st.session_state:
    question = st.session_state.pending_question
    del st.session_state.pending_question

    # Add user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Searching electrical codes..."):
            if agent:
                result = agent.ask(question)
                answer = result["answer"]
                tool_calls = result.get("tool_calls", [])
            else:
                answer = "Error: Agent not initialized. Please check your API keys."
                tool_calls = []

        st.markdown(answer)

        if st.session_state.show_tool_calls and tool_calls:
            with st.expander(f"🔧 Tool calls ({len(tool_calls)})"):
                for tc in tool_calls:
                    st.markdown(f"**{tc['tool']}**")
                    st.code(str(tc['input']), language="json")

    # Save to session
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "tool_calls": tool_calls
    })

    st.rerun()

# Chat input
if prompt := st.chat_input("Ask about CEC/NEC electrical codes..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Searching electrical codes..."):
            if agent:
                result = agent.ask(prompt)
                answer = result["answer"]
                tool_calls = result.get("tool_calls", [])
            else:
                answer = "Error: Agent not initialized. Please check your API keys."
                tool_calls = []

        st.markdown(answer)

        if st.session_state.show_tool_calls and tool_calls:
            with st.expander(f"🔧 Tool calls ({len(tool_calls)})"):
                for tc in tool_calls:
                    st.markdown(f"**{tc['tool']}**")
                    st.code(str(tc['input']), language="json")

    # Save to session
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "tool_calls": tool_calls
    })


# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 0.8rem;'>"
    "CEC Lang | Powered by LangChain + Groq | LangSmith Tracing Enabled"
    "</p>",
    unsafe_allow_html=True
)
