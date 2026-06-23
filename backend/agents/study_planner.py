from langchain_ollama import ChatOllama

from backend.database.operations import (
    get_weak_topics
)

llm = ChatOllama(
    model="phi3",
    temperature=0.4
)


def generate_study_plan(
    goal,
    study_hours
):

    weak_topics = get_weak_topics()

    weak_topic_names = []

    for topic in weak_topics:

        weak_topic_names.append(
            topic.topic
        )

    weak_topics_text = ", ".join(
        weak_topic_names
    )

    prompt = f"""
Create a 7-day study plan.

Goal:
{goal}

Daily Study Hours:
{study_hours}

Weak Topics:
{weak_topics_text}

Requirements:
- Create day-wise schedule
- Include revision
- Include quizzes
- Include practice sessions
- Keep plan realistic
"""

    response = llm.invoke(prompt)

    return response.content