from langchain_ollama import ChatOllama

from backend.config.settings import (
    CHAT_MODEL
)

llm = ChatOllama(
    model=CHAT_MODEL,
    temperature=0.2
)


def generate_topic_map(topic, context=""):

    prompt = f"""
Generate topic relationships.
Study Material:
{context}

Topic:
{topic}

STRICT FORMAT:

Main Topic -> Subtopic
Subtopic -> Concept
Concept -> Detail

Generate 15 relationships.
"""

    response = llm.invoke(prompt)

    return response.content


def parse_topic_map(text):

    edges = []

    lines = text.split("\n")

    for line in lines:

        if "->" in line:

            parts = line.split("->")

            if len(parts) == 2:

                source = parts[0].strip()

                target = parts[1].strip()

                edges.append(
                    (
                        source,
                        target
                    )
                )

    return edges