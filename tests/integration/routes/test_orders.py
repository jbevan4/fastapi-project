from datetime import datetime, timedelta
from decimal import Decimal
from http import HTTPStatus

import pytest
from config import Config
from fastapi.testclient import TestClient
from fastapi_project.domain.order import Country, Order, OrderIn, Status
from fastapi_project.repositories.database import get_session
from fastapi_project.repositories.types import RepositoryType
from main import app
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool


@pytest.fixture(autouse=True)
def config_fixture() -> None:
    original_value = Config.REPOSITORY_TYPE
    Config.REPOSITORY_TYPE = RepositoryType.SQLITE
    yield
    Config.REPOSITORY_TYPE = original_value


@pytest.fixture(name="session")
def session_fixture() -> Session:
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session) -> Session:
    def get_session_override() -> Session:
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_create_order_with_sqlite(session: Session, client: TestClient) -> None:
    order_in: OrderIn = OrderIn(amount=Decimal(10), country_of_origin=Country.uk)
    response = client.post("/orders/", content=order_in.json())
    response_data: dict = response.json()

    created_at = datetime.strptime(response_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
    max_created_at = datetime.utcnow() + timedelta(seconds=1)

    assert response.status_code == HTTPStatus.OK
    assert created_at <= max_created_at
    assert response_data.get("amount") == order_in.amount
    assert response_data.get("status") == Status.charged
    assert session.get(Order, response_data.get("id"))


# @pytest.fixture
# def test_client() -> TestClient:
#     app = FastAPI()
#     app.include_router(orders_router)
#     return TestClient(app)


# @pytest.fixture
# def sqlite_db() -> None:
#     Config.REPOSITORY_TYPE = RepositoryType.SQLITE
#     init_db()
#     yield
#     cleanup_db()


# @pytest.fixture
# def in_memory_db() -> None:
#     Config.REPOSITORY_TYPE = RepositoryType.IN_MEMORY
#     return


# def test_create_order_with_in_memory_db(
#     test_client: TestClient, in_memory_db  # noqa: ANN001
# ) -> None:
#     # IN_MEMORY is the default database provided
#     order_in: OrderIn = OrderIn(amount=Decimal(10), country_of_origin=Country.uk)
#     response = test_client.post("/orders/", content=order_in.json())
#     response_data = response.json()

#     now = datetime.utcnow()
#     created_at = datetime.strptime(response_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

#     assert now - timedelta(seconds=5) <= created_at <= now + timedelta(seconds=10)
#     assert response.status_code == HTTPStatus.OK
#     assert response_data.get("status") == Status.charged


# def test_create_order_with_sqlite_db(
#     test_client: TestClient, sqlite_db  # noqa: ANN001
# ) -> None:
#     order_in: OrderIn = OrderIn(amount=Decimal(10), country_of_origin=Country.uk)

#     response = test_client.post("/orders/", content=order_in.json())
#     response_data = response.json()

#     created_at = datetime.strptime(response_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
#     max_created_at = datetime.utcnow() + timedelta(seconds=1)

#     assert response.status_code == HTTPStatus.OK
#     assert created_at <= max_created_at
#     assert response_data.get("amount") == order_in.amount
#     assert response_data.get("status") == Status.charged
