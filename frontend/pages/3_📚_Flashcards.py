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

# ============================================
# IMPORTS
# ============================================

import streamlit as st

from frontend.styles.theme import (
    apply_theme
)

from backend.flashcards.generator import (
    generate_flashcards
)

from backend.flashcards.parser import (
    parse_flashcards
)

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Flashcards",
    layout="wide"
)

apply_theme()

# ============================================
# HEADER
# ============================================

st.title("📚 AI Flashcards")

st.caption(
    "Generate AI-powered revision flashcards"
)

# ============================================
# INPUT
# ============================================

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Operating System"
)

# ============================================
# GENERATE FLASHCARDS
# ============================================

if st.button(
    "🚀 Generate Flashcards"
):

    if not topic:

        st.warning(
            "Please enter a topic."
        )

    else:

        with st.spinner(
            "Generating flashcards..."
        ):

            raw_cards = generate_flashcards(
                topic
            )

            cards = []

            if raw_cards:

                cards = parse_flashcards(
                    raw_cards
                )

            if not cards:

                st.error(
                    "Failed to generate flashcards."
                )

            else:

                st.session_state.flashcards = (
                    cards
                )

                st.success(
                    "Flashcards generated successfully."
                )

# ============================================
# DISPLAY FLASHCARDS
# ============================================

if "flashcards" in st.session_state:

    st.markdown("---")

    for i, card in enumerate(
        st.session_state.flashcards
    ):

        with st.expander(
            f"🧠 Flashcard {i+1}"
        ):

            st.markdown(
                f"""
<div class="activity-card">

<h3>❓ Question</h3>

<p>{card['question']}</p>

<hr>

<h3>✅ Answer</h3>

<p>{card['answer']}</p>

</div>
""",
                unsafe_allow_html=True
            )