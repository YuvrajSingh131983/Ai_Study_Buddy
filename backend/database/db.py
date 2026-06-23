import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


def _get_database_url():
    env_url = os.getenv("DATABASE_URL")
    if env_url:
        return env_url

    db_file = os.getenv("DATABASE_FILE", "student_memory.db")
    db_path = Path(db_file)

    if not db_path.is_absolute():
        db_path = Path.cwd() / db_path

    if not os.access(db_path.parent, os.W_OK):
        tmp_dir = Path(
            os.getenv("TMPDIR")
            or os.getenv("TEMP")
            or os.getenv("TMP")
            or "/tmp"
        )
        db_path = tmp_dir / db_path.name

    db_path.parent.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{db_path.as_posix()}"


DATABASE_URL = _get_database_url()

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def init_db():
    from backend.database.models import Base as ModelsBase

    ModelsBase.metadata.create_all(bind=engine)
