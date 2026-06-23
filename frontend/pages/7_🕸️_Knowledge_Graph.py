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
import networkx as nx

from pyvis.network import Network

from frontend.styles.theme import apply_theme

from backend.knowledge_graph.generator import (
    generate_topic_map,
    parse_topic_map
)

from backend.rag.context import (
    get_pdf_context
)

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Knowledge Graph",
    layout="wide"
)

apply_theme()

# ============================================
# HEADER
# ============================================

st.title("🕸️ AI Knowledge Graph")

st.caption(
    "Visualize topic relationships using AI"
)

# ============================================
# INPUT
# ============================================

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Automata"
)

# ============================================
# GENERATE GRAPH
# ============================================

context = ""

if "qa_chain" in st.session_state and st.session_state.qa_chain is not None:

    context = get_pdf_context(
        st.session_state.qa_chain,
        topic
    )

if st.button("🚀 Generate Knowledge Graph"):

    with st.spinner(
        "Generating topic relationships..."
    ):

        raw_map = generate_topic_map(
            topic,
            context
        )

        edges = parse_topic_map(
            raw_map
        )

        if not edges:

            st.error(
                "Failed to generate graph."
            )

        else:

            G = nx.Graph()

            for source, target in edges:

                G.add_edge(
                    source,
                    target
                )

            net = Network(
                height="700px",
                width="100%",
                bgcolor="#0F172A",
                font_color="white"
            )

            net.from_nx(G)

            net.repulsion(
                node_distance=220,
                central_gravity=0.3,
                spring_length=200
            )

            output_path = "knowledge_graph.html"

            net.save_graph(
                output_path
            )

            with open(
                output_path,
                "r",
                encoding="utf-8"
            ) as f:

                html = f.read()

            st.components.v1.html(
                html,
                height=700
            )

            st.success(
                "Knowledge graph generated."
            )