from datetime import datetime, timedelta
from decimal import Decimal
from http import HTTPStatus

import pytest
from config import Config
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_project.domain.order import Country, OrderIn, Status
from fastapi_project.repositories.database import cleanup_db, init_db
from fastapi_project.routes.orders import router as orders_router


@pytest.fixture
def test_client() -> None:
    app = FastAPI()
    app.include_router(orders_router)
    init_db()
    yield TestClient(app)
    cleanup_db()


def test_create_order_with_in_memory_db(test_client: TestClient) -> None:
    Config.REPOSITORY_TYPE = "in_memory"
    order_in: OrderIn = OrderIn(amount=Decimal(10), country_of_origin=Country.uk)
    response = test_client.post("/orders/", content=order_in.json())
    response_data = response.json()

    now = datetime.utcnow()
    created_at = datetime.strptime(response_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

    assert now - timedelta(seconds=5) <= created_at <= now + timedelta(seconds=10)
    assert response.status_code == HTTPStatus.OK
    assert response_data.get("status") == Status.charged


def test_create_order_with_sqlite_db(test_client: TestClient) -> None:
    Config.REPOSITORY_TYPE = "sqlite"
    order_in: OrderIn = OrderIn(amount=Decimal(10), country_of_origin=Country.uk)

    response = test_client.post("/orders/", content=order_in.json())
    response_data = response.json()

    now = datetime.utcnow()
    created_at = datetime.strptime(response_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

    assert now - timedelta(seconds=5) <= created_at <= now + timedelta(seconds=10)
    assert response.status_code == HTTPStatus.OK
    assert response_data.get("status") == Status.charged
