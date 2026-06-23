import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)

import streamlit as st

from frontend.styles.theme import apply_theme

from backend.agents.manager import (
    process_agent_request
)

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Multi-Agent AI",
    layout="wide"
)

apply_theme()

# ============================================
# HEADER
# ============================================

st.title("🤖 Multi-Agent AI System")

st.caption(
    "Autonomous AI agents collaborate to assist learning"
)

# ============================================
# INPUT
# ============================================

user_input = st.text_area(
    "Ask Anything",
    placeholder=
    """
Examples:

Generate quiz on DBMS

Create flashcards for OS

Generate study plan for CDS

Create graph for Automata
"""
)

# ============================================
# PROCESS
# ============================================

if st.button("🚀 Run AI Agents"):

    with st.spinner(
        "AI agents collaborating..."
    ):

        result = process_agent_request(
            user_input
        )

        st.markdown("---")

        st.markdown(
            f"""
<div class="hero-card">

<h2>🧠 Agent Response</h2>

<pre style="
white-space: pre-wrap;
font-size: 1rem;
color: white;
">
{result}
</pre>

</div>
""",
            unsafe_allow_html=True
        )