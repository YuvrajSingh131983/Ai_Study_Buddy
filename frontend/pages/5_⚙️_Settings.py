import streamlit as st

from frontend.styles.theme import apply_theme

st.set_page_config(
    page_title="Settings",
    layout="wide"
)

apply_theme()

st.title("⚙️ Settings")

model = st.selectbox(
    "LLM Model",
    [
        "llama3:8b",
        "phi3",
        "mistral"
    ]
)

vision_model = st.selectbox(
    "Vision Model",
    [
        "llava",
        "minicpm-v"
    ]
)

theme = st.selectbox(
    "Theme",
    [
        "Dark",
        "Light"
    ]
)

if st.button("💾 Save Settings"):

    st.success("Settings saved successfully.")