import base64

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

from backend.config.settings import VISION_MODEL


def analyze_diagram(image_bytes, user_query):

    vision_model = ChatOllama(
        model=VISION_MODEL,
        temperature=0.2
    )

    image_base64 = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": f"""
You are AI Study Buddy Vision Assistant.

Analyze the given educational diagram carefully.

User Query:
{user_query}

Instructions:
1. Explain step-by-step.
2. Identify labels and components.
3. Explain flow if present.
4. Keep explanation educational.
"""
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        ]
    )

    response = vision_model.invoke([message])

    return response.content