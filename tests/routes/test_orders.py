from decimal import Decimal
from unittest.mock import MagicMock
from fastapi_project.domain.order import Country, OrderIn
from fastapi_project.routes.orders import create_order_route
import pytest


@pytest.mark.asyncio
async def test_create_order_route_success() -> None:
    create_order_mock = MagicMock()
    order_in = OrderIn(amount=Decimal(10), country_of_origin=Country.australia)
    create_order_mock.execute.return_value = {}

    # Use asyncio.run to run the asynchronous function and await the result
    response = await create_order_route(
        order_in=order_in, create_order=create_order_mock
    )

    assert response == create_order_mock.execute.return_value
    create_order_mock.execute.assert_called_once_with(**order_in.dict())
