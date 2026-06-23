from backend.llm.models import (
    get_chat_model
)

llm = get_chat_model()


def generate_flashcards(
    topic,
    context=""
):

    prompt = f"""
Generate 5 flashcards
ONLY from this content:

{context}

Topic:
{topic}

FORMAT:

Q:
question

A:
answer
"""

    response = llm.invoke(
        prompt
    )

    return response.content