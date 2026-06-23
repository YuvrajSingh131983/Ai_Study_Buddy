import streamlit as st


def apply_theme():

    st.markdown(
        """
<style>

/* =========================================
MAIN APP
========================================= */

.stApp {

    background:
        linear-gradient(
            135deg,
            #0F172A,
            #111827,
            #1E293B
        );

    color: white;
}

/* =========================================
SIDEBAR
========================================= */

section[data-testid="stSidebar"] {

    background:
        rgba(15,23,42,0.95);

    border-right:
        1px solid rgba(255,255,255,0.08);
}

/* =========================================
HERO CARD
========================================= */

.hero-card {

    padding: 2rem;

    border-radius: 24px;

    background:
        linear-gradient(
            135deg,
            rgba(59,130,246,0.15),
            rgba(168,85,247,0.12)
        );

    border:
        1px solid rgba(255,255,255,0.08);

    margin-bottom: 1.5rem;

    backdrop-filter: blur(14px);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.3);
}

/* =========================================
ACTIVITY CARDS
========================================= */

.activity-card {

    padding: 1rem;

    border-radius: 18px;

    margin-bottom: 1rem;

    background:
        rgba(255,255,255,0.05);

    border:
        1px solid rgba(255,255,255,0.06);

    transition: 0.3s;
}

.activity-card:hover {

    transform: translateY(-3px);

    background:
        rgba(255,255,255,0.08);
}

/* =========================================
BUTTONS
========================================= */

.stButton button {

    width: 100%;

    border-radius: 14px;

    border: none;

    padding: 0.75rem;

    font-weight: 600;

    background:
        linear-gradient(
            90deg,
            #3B82F6,
            #8B5CF6
        );

    color: white;

    transition: 0.3s;
}

.stButton button:hover {

    transform: scale(1.02);

    opacity: 0.92;
}

/* =========================================
INPUTS
========================================= */

.stTextInput input,
.stTextArea textarea {

    border-radius: 14px !important;

    background:
        rgba(255,255,255,0.05) !important;

    color: white !important;

    border:
        1px solid rgba(255,255,255,0.08) !important;
}

/* =========================================
CHAT
========================================= */

.chat-wrapper {

    padding: 1rem;

    border-radius: 20px;

    background:
        rgba(255,255,255,0.03);

    border:
        1px solid rgba(255,255,255,0.05);
}

/* =========================================
SCROLLBAR
========================================= */

::-webkit-scrollbar {

    width: 8px;
}

::-webkit-scrollbar-thumb {

    background: #3B82F6;

    border-radius: 10px;
}

/* =========================================
LOADER
========================================= */

.loader {

    width: 48px;
    height: 48px;

    border:
        5px solid rgba(255,255,255,0.1);

    border-top:
        5px solid #3B82F6;

    border-radius: 50%;

    animation: spin 1s linear infinite;

    margin: auto;
}

@keyframes spin {

    100% {
        transform: rotate(360deg);
    }
}

</style>
""",
        unsafe_allow_html=True
    )