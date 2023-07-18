from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager


sqlite_file = "testing.db"
sqlite_url = f"sqlite:///{sqlite_file}"
engine = create_engine(sqlite_url)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session() -> Session:
    session = Session(engine)
    yield session
    session.close()
