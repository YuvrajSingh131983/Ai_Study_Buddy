import streamlit as st


def dashboard_cards():

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            """
<div class="activity-card">

<h3>📚 Documents</h3>

<h1>12</h1>

<p>Knowledge Sources</p>

</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
<div class="activity-card">

<h3>🧠 AI Sessions</h3>

<h1>148</h1>

<p>Learning Conversations</p>

</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
<div class="activity-card">

<h3>🔥 Accuracy</h3>

<h1>91%</h1>

<p>Quiz Performance</p>

</div>
""",
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            """
<div class="activity-card">

<h3>⚡ Study Streak</h3>

<h1>16</h1>

<p>Consecutive Days</p>

</div>
""",
            unsafe_allow_html=True
        )