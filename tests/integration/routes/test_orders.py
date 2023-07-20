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
