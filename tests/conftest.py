import pytest
from fastapi_project.repositories.database import init_db, get_session


@pytest.fixture(scope="session")
def db_session() -> None:
    init_db()
    with get_session() as session:
        yield session
