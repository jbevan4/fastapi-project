from contextlib import contextmanager
from sqlmodel import SQLModel, create_engine, Session
from fastapi_project.config import Config


engine = create_engine(Config.DATABASE_URL)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session() -> None:
    """Provide a transactional scope around a series of operations."""
    session = Session(bind=engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
