from langchain_ollama import (
    ChatOllama
)

from backend.config.settings import (
    CHAT_MODEL
)

# ============================================
# CHAT MODEL
# ============================================

def get_chat_model():

    return ChatOllama(

        model=CHAT_MODEL,

        temperature=0.3,

        # IMPORTANT
        num_predict=1200,

        # Better long responses
        top_p=0.9,

        repeat_penalty=1.1
    )