
from sqlmodel import Session, SQLModel, create_engine

from fastapi_project.config import Config

engine = create_engine(Config.DATABASE_URL)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


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
