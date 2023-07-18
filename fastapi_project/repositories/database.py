import os

from config import Config
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine(Config.DATABASE_URL)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def cleanup_db() -> None:
    os.remove(Config.DATABASE_NAME)


def get_session() -> Session:
    session = Session(bind=engine)
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
