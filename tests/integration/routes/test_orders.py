from datetime import datetime, timedelta
from decimal import Decimal
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi_project.routes.orders import router as orders_router
from fastapi_project.domain.order import Country, OrderIn, Status

app = FastAPI()
app.include_router(orders_router)

client = TestClient(app)


def test_create_order() -> None:
    order_in: OrderIn = OrderIn(amount=Decimal(10), country_of_origin=Country.uk)
    response = client.post("/orders/", data=order_in.json())
    response_data = response.json()

    now = datetime.utcnow()
    created_at = datetime.strptime(response_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

    assert now - timedelta(seconds=10) <= created_at <= now + timedelta(seconds=10)
    assert response.status_code == 200
    assert response_data.get("status") == Status.charged
