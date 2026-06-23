import sys
import os
import re

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# ============================================
# IMPORTS
# ============================================

import streamlit as st

from backend.database.db import init_db
from backend.database.operations import (
    get_chat_history,
    save_chat
)

from backend.rag.ingest import (
    load_pdf,
    split_documents
)

from backend.rag.vectorstore import (
    create_vectorstore
)

from backend.rag.retriever import (
    create_retriever
)

from backend.llm.chains import (
    build_qa_chain
)

from backend.vision.diagram_analyzer import (
    analyze_diagram
)

from frontend.styles.theme import (
    apply_theme
)

from frontend.components.dashboard_cards import (
    dashboard_cards
)

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🧠",
    layout="wide"
)

apply_theme()

init_db()

# ============================================
# SESSION STATE
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if "knowledge_ready" not in st.session_state:
    st.session_state.knowledge_ready = False

# ============================================
# CACHE FUNCTIONS
# ============================================

@st.cache_resource
def build_cached_qa(file_path):

    documents = load_pdf(file_path)

    chunks = split_documents(
        documents
    )

    vectorstore = create_vectorstore(
        chunks
    )

    retriever = create_retriever(
        vectorstore
    )

    qa_chain = build_qa_chain(
        retriever
    )

    return qa_chain

# ============================================
# HERO SECTION
# ============================================

st.markdown(
    """
<div class="hero-card">

<h1 style="
font-size:3rem;
font-weight:800;
margin-bottom:0.5rem;
">
🧠 AI Study Buddy
</h1>

<p style="
font-size:1.2rem;
color:#CBD5E1;
">
Fast AI-Powered Learning Platform
</p>

<hr>

<p style="
font-size:1rem;
color:#94A3B8;
">
RAG • Quizzes • Flashcards • Analytics • Knowledge Graphs
</p>

</div>
""",
    unsafe_allow_html=True
)

# ============================================
# DASHBOARD
# ============================================

dashboard_cards()

# ============================================
# SIDEBAR
# ============================================

with st.sidebar:

    st.markdown("# 🚀 AI Workspace")

    st.markdown("---")

    # ============================================
    # RECENT CHATS
    # ============================================

    st.subheader("🕘 Recent Chats")

    history = get_chat_history()

    for chat in history[-5:]:

        st.markdown(
            f"""
<div style="
padding:0.5rem;
margin-bottom:0.5rem;
background:rgba(255,255,255,0.05);
border-radius:10px;
font-size:0.8rem;
">
{chat.role}: {chat.message[:35]}
</div>
""",
            unsafe_allow_html=True
        )

    st.markdown("---")

    # ============================================
    # PDF UPLOAD
    # ============================================

    st.subheader("📚 Upload Notes")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        os.makedirs(
            "uploads",
            exist_ok=True
        )

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )

        st.success(
            "PDF Uploaded"
        )

        if st.button(
            "⚡ Build Fast Knowledge Base"
        ):

            with st.spinner(
                "Processing PDF..."
            ):

                qa_chain = build_cached_qa(
                    file_path
                )

                st.session_state.qa_chain = (
                    qa_chain
                )

                st.session_state.knowledge_ready = True

                st.success(
                    "Knowledge Base Ready"
                )

    st.markdown("---")

    # ============================================
    # DIAGRAM ANALYZER
    # ============================================

    st.subheader("📊 Diagram Analyzer")

    diagram_file = st.file_uploader(
        "Upload Diagram",
        type=["png", "jpg", "jpeg"]
    )

    diagram_query = st.text_input(
        "Diagram Question",
        value="Explain this diagram briefly."
    )

    if diagram_file and st.button(
        "⚡ Analyze"
    ):

        with st.spinner(
            "Analyzing..."
        ):

            result = analyze_diagram(
                diagram_file.getvalue(),
                diagram_query
            )

            st.write(result)

# ============================================
# QUICK ACTIONS
# ============================================

st.markdown("## 🚀 Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("📘 Explain DBMS"):

        st.session_state.quick_prompt = (
            "Explain DBMS normalization"
        )

with col2:

    if st.button("🧠 Explain OS"):

        st.session_state.quick_prompt = (
            "Explain CPU scheduling"
        )

with col3:

    if st.button("🌐 Explain CN"):

        st.session_state.quick_prompt = (
            "Explain TCP/IP model"
        )

# ============================================
# CHAT SECTION
# ============================================

st.markdown("## 💬 AI Tutor")

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if "dot_code" in message:

            st.graphviz_chart(
                message["dot_code"]
            )

# ============================================
# INPUT
# ============================================

prompt = st.chat_input(
    "Ask AI Study Buddy..."
)

# QUICK DEMO PROMPT

if (
    "quick_prompt"
    in st.session_state
):

    prompt = st.session_state.quick_prompt

    del st.session_state.quick_prompt

# ============================================
# HANDLE CHAT
# ============================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    save_chat(
        "user",
        prompt
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # ============================================
    # NO PDF
    # ============================================

    if not st.session_state.knowledge_ready:

        st.warning(
            "Upload PDF and build knowledge base first."
        )

    # ============================================
    # AI RESPONSE
    # ============================================

    else:

        with st.chat_message(
            "assistant"
        ):

            with st.spinner(
                "⚡ AI Thinking..."
            ):

                response = (
                    st.session_state.qa_chain.invoke(
                        {
                            "query": prompt
                        }
                    )
                )

                answer = response[
                    "result"
                ]

                st.markdown(answer)

                save_chat(
                    "assistant",
                    answer
                )

                dot_match = re.search(
                    r"```dot\n(.*?)\n```",
                    answer,
                    re.DOTALL
                )

                current_dot_code = None

                if dot_match:

                    current_dot_code = (
                        dot_match.group(1)
                    )

                    st.graphviz_chart(
                        current_dot_code
                    )

                history = {
                    "role": "assistant",
                    "content": answer
                }

                if current_dot_code:

                    history[
                        "dot_code"
                    ] = current_dot_code

                st.session_state.messages.append(
                    history
                )

# ============================================
# FOOTER
# ============================================

st.markdown("---")

st.markdown(
    """
<div style="
text-align:center;
padding:1rem;
color:#64748B;
font-size:0.9rem;
">

AI Study Buddy © 2026

Built with Streamlit • Ollama • LangChain • ChromaDB

</div>
""",
    unsafe_allow_html=True
)