import streamlit as st

from backend.quizzes.generator import (
    generate_quiz
)

from frontend.styles.theme import (
    apply_theme
)
from backend.rag.context import (
    get_pdf_context
)

st.set_page_config(
    page_title="Quiz Generator",
    layout="wide"
)

apply_theme()

st.title("🧠 AI Quiz Generator")

topic = st.text_input(
    "Enter Topic",
    value="Pushdown Automata"
)
if "qa_chain" not in st.session_state or st.session_state.qa_chain is None:

    st.warning(
        "No knowledge base found — upload a PDF and click 'Build Fast Knowledge Base' in the sidebar."
    )

    context = ""

else:

    context = get_pdf_context(
        st.session_state.qa_chain,
        topic
    )

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

num_questions = st.slider(
    "Number of Questions",
    1,
    10,
    5
)

# ============================================
# GENERATE QUIZ
# ============================================

if st.button("🚀 Generate Quiz"):

    with st.spinner(
        "Generating Quiz..."
    ):

        quiz = generate_quiz(
             topic,
             difficulty,
             num_questions,
             context
             )

    if not quiz:

        st.error(
            "Failed to generate quiz."
        )

    else:

        st.success(
            "Quiz generated successfully."
        )

        st.markdown("---")

        score = 0

        for i, q in enumerate(quiz):

            st.markdown(
                f"""
<div class="hero-card">
<h2>Q{i+1}. {q['question']}</h2>
</div>
""",
                unsafe_allow_html=True
            )

            user_answer = st.radio(
                "Choose Answer",
                list(
                    q["options"].keys()
                ),
                format_func=lambda x:
                f"{x}. {q['options'][x]}",
                key=f"q_{i}"
            )

            if st.button(
                f"Check Answer {i+1}",
                key=f"btn_{i}"
            ):

                correct = q["answer"]

                if user_answer == correct:

                    st.success(
                        "Correct Answer!"
                    )

                    score += 1

                else:

                    st.error(
                        f"Wrong! Correct Answer: {correct}"
                    )

            st.markdown("---")