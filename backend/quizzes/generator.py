import re

from langchain_ollama import (
    ChatOllama
)

quiz_llm = ChatOllama(
    model="llama3:8b",
    temperature=0.2
)

# ============================================
# PDF-BASED QUIZ
# ============================================

def generate_quiz(
    topic,
    difficulty,
    num_questions,
    context=""
):

    prompt = f"""
Generate EXACTLY {num_questions} MCQs.

Use ONLY this study material:

{context}

Topic:
{topic}

Difficulty:
{difficulty}

STRICT FORMAT:

Q:
question

A:
option

B:
option

C:
option

D:
option

ANSWER:
A
"""

    response = quiz_llm.invoke(
        prompt
    )

    text = response.content

    questions = []

    pattern = re.findall(
        r"Q:\s*(.*?)\s*A:\s*(.*?)\s*B:\s*(.*?)\s*C:\s*(.*?)\s*D:\s*(.*?)\s*ANSWER:\s*([ABCD])",
        text,
        re.DOTALL
    )

    for match in pattern:

        question, a, b, c, d, ans = match

        questions.append(
            {
                "question": question.strip(),
                "options": {
                    "A": a.strip(),
                    "B": b.strip(),
                    "C": c.strip(),
                    "D": d.strip()
                },
                "answer": ans.strip()
            }
        )

    return questions[:num_questions]