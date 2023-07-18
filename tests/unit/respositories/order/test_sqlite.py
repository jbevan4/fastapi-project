from decimal import Decimal
import pytest
from unittest.mock import MagicMock
from fastapi_project.domain.order import Country, Order, OrderIn
from fastapi_project.domain.order_factory import OrderFactory
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository


@pytest.fixture
def db_client() -> MagicMock:
    # Create a mock SQLite client
    return MagicMock()


def test_add_order(db_client: MagicMock) -> None:
    repository = SQLiteOrderRepository(db_client=db_client, db_path="")
    order_in = OrderIn(country_of_origin=Country.usa, amount=Decimal(10))
    order: Order = OrderFactory.make_order(order_in=order_in)
    repository.add(order)

    cursor = db_client.cursor.return_value
    cursor.execute.assert_called_once_with(
        "INSERT INTO orders "
        "("
        "id,"
        "amount,"
        "country_of_origin,"
        "created_at,"
        "provider_id,"
        "provider,"
        "status,"
        "tax_amount,"
        "tax_percentage,"
        "final_amount_charged"
        ")"
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            str(order.id),
            order.amount,
            order.country_of_origin.value,
            order.created_at,
            order.provider_id,
            order.provider,
            order.status.value,
            order.tax_amount,
            order.tax_percentage,
            order.final_amount_charged,
        ),
    )
