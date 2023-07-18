import pytest
from unittest.mock import MagicMock
from fastapi_project.domain.order import Order
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository


@pytest.fixture
def db_client() -> MagicMock:
    # Create a mock SQLite client
    return MagicMock()


def test_add_order(db_client: MagicMock) -> None:
    pytest.skip()
    repository = SQLiteOrderRepository(db_path="", db_client=db_client)

    # Create a test order
    order = Order(
        id="12345678-1234-5678-1234-567812345678",
        amount=10.0,
        country_of_origin="USA",
        created_at="2022-01-01 12:00:00",
        provider_id=None,
        provider=None,
        status="pending",
        tax_amount=0.0,
    )

    # Call the add method
    repository.add(order)

    # Assert that the appropriate method was called on the db_client
    db_client.execute.assert_called_once_with(
        "INSERT INTO orders (id, amount, country_of_origin, created_at, provider_id, provider, status, tax_amount) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            "12345678-1234-5678-1234-567812345678",
            10.0,
            "USA",
            "2022-01-01 12:00:00",
            None,
            None,
            "pending",
            0.0,
        ),
    )
