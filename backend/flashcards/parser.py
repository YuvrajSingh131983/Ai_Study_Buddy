import re


def parse_flashcards(text):

    if not text:

        return []

    pattern = r"Q:\s*(.*?)\s*A:\s*(.*?)(?=Q:|$)"

    matches = re.findall(
        pattern,
        text,
        re.DOTALL
    )

    cards = []

    for q, a in matches:

        cards.append(
            {
                "question": q.strip(),
                "answer": a.strip()
            }
        )

    return cards