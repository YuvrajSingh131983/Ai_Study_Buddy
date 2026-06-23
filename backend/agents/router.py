def route_agent(user_input):

    text = user_input.lower()

    # ============================================
    # QUIZ AGENT
    # ============================================

    if (
        "quiz" in text
        or "mcq" in text
        or "test" in text
    ):

        return "quiz"

    # ============================================
    # FLASHCARD AGENT
    # ============================================

    elif (
        "flashcard" in text
        or "revise" in text
        or "revision" in text
    ):

        return "flashcard"

    # ============================================
    # STUDY PLANNER AGENT
    # ============================================

    elif (
        "study plan" in text
        or "schedule" in text
        or "roadmap" in text
    ):

        return "planner"

    # ============================================
    # KNOWLEDGE GRAPH AGENT
    # ============================================

    elif (
        "graph" in text
        or "relationship" in text
        or "topic map" in text
    ):

        return "graph"

    # ============================================
    # DEFAULT TUTOR AGENT
    # ============================================

    else:

        return "tutor"