import re


def parse_quiz(text):

    questions = []

    pattern = r"""
(Q\d+\..*?)
A\.\s(.*?)
B\.\s(.*?)
C\.\s(.*?)
D\.\s(.*?)
Answer:\s([A-D])
"""

    matches = re.findall(
        pattern,
        text,
        re.DOTALL | re.VERBOSE
    )

    for match in matches:

        questions.append({
            "question": match[0].strip(),
            "A": match[1].strip(),
            "B": match[2].strip(),
            "C": match[3].strip(),
            "D": match[4].strip(),
            "answer": match[5].strip()
        })

    return questions