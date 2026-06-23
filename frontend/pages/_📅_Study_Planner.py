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

from backend.agents.study_planner import (
    generate_study_plan
)

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Study Planner",
    layout="wide"
)

apply_theme()

# ============================================
# HEADER
# ============================================

st.title("📅 AI Study Planner")

st.caption(
    "Generate personalized AI-powered study schedules"
)

# ============================================
# INPUTS
# ============================================

goal = st.text_input(
    "Target Goal",
    placeholder="Example: Prepare for CDS Exam"
)

study_hours = st.slider(
    "Daily Study Hours",
    1,
    12,
    4
)

# ============================================
# GENERATE PLAN
# ============================================

if st.button("🚀 Generate Study Plan"):

    with st.spinner(
        "Creating intelligent study roadmap..."
    ):

        plan = generate_study_plan(
            goal,
            study_hours
        )

        st.markdown("---")

        st.markdown(
            f"""
<div class="hero-card">

<h2>🧠 Personalized Study Plan</h2>

<pre style="
white-space: pre-wrap;
font-size: 1rem;
color: white;
">
{plan}
</pre>

</div>
""",
            unsafe_allow_html=True
        )