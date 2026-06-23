from backend.database.db import SessionLocal

from backend.database.models import (
    ChatHistory,
    QuizScore,
    WeakTopic
)


# ============================================
# SAVE CHAT
# ============================================

def save_chat(role, message):

    db = SessionLocal()

    chat = ChatHistory(
        role=role,
        message=message
    )

    db.add(chat)

    db.commit()

    db.close()


# ============================================
# SAVE QUIZ SCORE
# ============================================

def save_quiz_score(
    topic,
    score,
    difficulty
):

    db = SessionLocal()

    quiz = QuizScore(
        topic=topic,
        score=score,
        difficulty=difficulty
    )

    db.add(quiz)

    db.commit()

    db.close()


# ============================================
# SAVE WEAK TOPIC
# ============================================

def save_weak_topic(
    topic,
    weakness_score
):

    db = SessionLocal()

    weak = WeakTopic(
        topic=topic,
        weakness_score=weakness_score
    )

    db.add(weak)

    db.commit()

    db.close()


# ============================================
# GET CHAT HISTORY
# ============================================

def get_chat_history():

    db = SessionLocal()

    chats = db.query(
        ChatHistory
    ).all()

    db.close()

    return chats


# ============================================
# GET WEAK TOPICS
# ============================================

def get_weak_topics():

    db = SessionLocal()

    topics = db.query(
        WeakTopic
    ).all()

    db.close()

    return topics
# ============================================
# GET RECENT CHATS
# ============================================

def get_recent_chats(limit=5):

    db = SessionLocal()

    chats = (
        db.query(ChatHistory)
        .order_by(ChatHistory.timestamp.desc())
        .limit(limit)
        .all()
    )

    db.close()

    return chats