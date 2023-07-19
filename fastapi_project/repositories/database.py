import os
from enum import Enum

from config import Config
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine(Config.DATABASE_URL)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def cleanup_db() -> None:
    os.remove(Config.DATABASE_NAME)


def get_session() -> None:
    session = Session(bind=engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
