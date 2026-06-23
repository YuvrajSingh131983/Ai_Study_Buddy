from backend.agents.router import (
    route_agent
)

from backend.quizzes.generator import (
    generate_quiz
)

from backend.flashcards.generator import (
    generate_flashcards
)

from backend.agents.study_planner import (
    generate_study_plan
)

from backend.knowledge_graph.generator import (
    generate_topic_map
)


def process_agent_request(user_input):

    agent = route_agent(
        user_input
    )

    # ============================================
    # QUIZ AGENT
    # ============================================

    if agent == "quiz":

        return generate_quiz(
            topic=user_input,
            difficulty="Medium",
            num_questions=5
        )

    # ============================================
    # FLASHCARD AGENT
    # ============================================

    elif agent == "flashcard":

        return generate_flashcards(
            user_input
        )

    # ============================================
    # PLANNER AGENT
    # ============================================

    elif agent == "planner":

        return generate_study_plan(
            goal=user_input,
            study_hours=4
        )

    # ============================================
    # KNOWLEDGE GRAPH AGENT
    # ============================================

    elif agent == "graph":

        return generate_topic_map(
            user_input
        )

    # ============================================
    # DEFAULT
    # ============================================

    else:

        return (
            "Tutor Agent Activated:\n\n"
            "Please ask educational questions "
            "from your uploaded notes."
        )