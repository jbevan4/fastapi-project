from decimal import Decimal
from unittest.mock import MagicMock

import pytest
from fastapi_project.domain.order import Country, OrderIn
from fastapi_project.domain.order_factory import OrderFactory
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository


@pytest.fixture
def db_client() -> None:
    return MagicMock()


def test_add_order(db_client: MagicMock) -> None:
    repository = SQLiteOrderRepository(session=db_client)

    order_in = OrderIn(country_of_origin=Country.usa, amount=Decimal(10))
    order = OrderFactory.make_order(order_in=order_in)

    repository.add(order)

    db_client.add.assert_called_once_with(order)
