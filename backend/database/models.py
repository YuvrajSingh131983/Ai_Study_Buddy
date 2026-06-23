from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from backend.database.db import Base


# ============================================
# CHAT HISTORY
# ============================================

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    role = Column(String)

    message = Column(Text)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )


# ============================================
# QUIZ SCORES
# ============================================

class QuizScore(Base):

    __tablename__ = "quiz_scores"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    topic = Column(String)

    score = Column(Float)

    difficulty = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )


# ============================================
# WEAK TOPICS
# ============================================

class WeakTopic(Base):

    __tablename__ = "weak_topics"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    topic = Column(String)

    weakness_score = Column(Float)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )