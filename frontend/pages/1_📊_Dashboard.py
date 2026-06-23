import streamlit as st
import plotly.express as px
import pandas as pd

from frontend.styles.theme import apply_theme

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

apply_theme()

# ============================================
# HEADER
# ============================================

st.title("📊 Learning Dashboard")

st.caption(
    "Track your study performance and AI learning progress"
)

# ============================================
# METRICS
# ============================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Study Hours",
    "128",
    "+12%"
)

col2.metric(
    "Quiz Accuracy",
    "91%",
    "+4%"
)

col3.metric(
    "Questions Asked",
    "542",
    "+32"
)

col4.metric(
    "Topics Mastered",
    "24",
    "+3"
)

st.markdown("---")

# ============================================
# CHARTS
# ============================================

df = pd.DataFrame({
    "Day": [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ],
    "Study Hours": [2, 3, 4, 2, 5, 6, 3]
})

fig = px.line(
    df,
    x="Day",
    y="Study Hours",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ============================================
# WEAK TOPICS
# ============================================

st.markdown("## ⚠️ Weak Topics")

weak_topics = [
    "CFG",
    "PDA",
    "Recursion",
    "Deadlock"
]

for topic in weak_topics:

    st.markdown(
        f"""
<div class="metric-card">
<h3>{topic}</h3>
<p>Needs more practice</p>
</div>
""",
        unsafe_allow_html=True
    )