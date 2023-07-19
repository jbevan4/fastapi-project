from datetime import datetime, timedelta
from decimal import Decimal
from http import HTTPStatus

import pytest
from config import Config
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_project.domain.order import Country, OrderIn, Status
from fastapi_project.repositories.database import cleanup_db, init_db
from fastapi_project.repositories.types import RepositoryType
from fastapi_project.routes.orders import router as orders_router


@pytest.fixture
def test_client() -> TestClient:
    app = FastAPI()
    app.include_router(orders_router)
    return TestClient(app)


@pytest.fixture
def sqlite_db() -> None:
    Config.REPOSITORY_TYPE = RepositoryType.SQLITE
    init_db()
    yield
    cleanup_db()


@pytest.fixture
def in_memory_db() -> None:
    Config.REPOSITORY_TYPE = RepositoryType.IN_MEMORY
    return


def test_create_order_with_in_memory_db(test_client: TestClient, in_memory_db) -> None:
    # IN_MEMORY is the default database provided
    order_in: OrderIn = OrderIn(amount=Decimal(10), country_of_origin=Country.uk)
    response = test_client.post("/orders/", content=order_in.json())
    response_data = response.json()

    now = datetime.utcnow()
    created_at = datetime.strptime(response_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

    assert now - timedelta(seconds=5) <= created_at <= now + timedelta(seconds=10)
    assert response.status_code == HTTPStatus.OK
    assert response_data.get("status") == Status.charged


def test_create_order_with_sqlite_db(test_client: TestClient, sqlite_db) -> None:
    order_in: OrderIn = OrderIn(amount=Decimal(10), country_of_origin=Country.uk)

    response = test_client.post("/orders/", content=order_in.json())
    response_data = response.json()

    created_at = datetime.strptime(response_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
    max_created_at = datetime.utcnow() + timedelta(seconds=1)

    assert response.status_code == HTTPStatus.OK
    assert created_at <= max_created_at
    assert response_data.get("amount") == order_in.amount
    assert response_data.get("status") == Status.charged
