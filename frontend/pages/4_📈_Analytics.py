import sys
import os

# ============================================
# FIX PYTHON PATH
# ============================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)

# ============================================
# IMPORTS
# ============================================

import streamlit as st
import pandas as pd
import plotly.express as px

from backend.database.operations import get_weak_topics

from frontend.styles.theme import apply_theme

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Analytics",
    layout="wide"
)

apply_theme()

# ============================================
# HEADER
# ============================================

st.title("📈 AI Learning Analytics")

st.caption(
    "Detailed study performance analysis"
)

# ============================================
# SAMPLE PERFORMANCE DATA
# ============================================

df = pd.DataFrame({
    "Topic": [
        "DFA",
        "OS",
        "DBMS",
        "CN",
        "AI"
    ],
    "Score": [
        82,
        75,
        91,
        69,
        88
    ]
})

# ============================================
# BAR CHART
# ============================================

fig = px.bar(
    df,
    x="Topic",
    y="Score",
    text="Score"
)

fig.update_layout(
    paper_bgcolor="#0F172A",
    plot_bgcolor="#0F172A",
    font_color="white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ============================================
# WEAK TOPICS FROM DATABASE
# ============================================

st.subheader("⚠️ Weak Topics")

weak_topics = get_weak_topics()

if weak_topics:

    for topic in weak_topics:

        st.warning(
            f"Weak Area: {topic.topic}"
        )

else:

    st.success(
        "No weak topics detected yet."
    )

# ============================================
# AI RECOMMENDATIONS
# ============================================

st.markdown("---")

st.subheader("🧠 AI Study Recommendations")

st.info(
    """
Focus more on:
- Computer Networks
- Operating Systems
- PDA and CFG concepts

Recommended:
- Solve more quizzes
- Practice diagrams
- Revise weak topics daily
"""
)