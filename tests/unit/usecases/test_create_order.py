from decimal import Decimal
from unittest.mock import MagicMock
from fastapi_project.domain.order import Country, OrderIn, Status, Provider
from fastapi_project.domain.order_factory import OrderFactory
from fastapi_project.usecases.create_order import CreateOrder
from uuid import uuid4


def test_create_order() -> None:
    amount, country_of_origin = Decimal(10), Country.germany
    order_in = OrderIn(amount=amount, country_of_origin=country_of_origin)
    order = OrderFactory().make_order(**order_in.dict())
    provider = MagicMock()
    in_memory_repository = MagicMock()
    provider_selector = MagicMock()
    order_factory = MagicMock()

    updated_order = order.copy(
        update={
            "provider_id": uuid4(),
            "provider": Provider.checkout,
            "status": Status.charged,
            "tax_amount": Decimal(10),
            "tax_percentage": Decimal(5),
            "final_amount_charged": Decimal(10) + order.amount,
        }
    )
    provider.create_payment.return_value = updated_order
    order_factory.make_order.return_value = order
    provider_selector.get_provider.return_value = provider
    create_order = CreateOrder(
        order_repo=in_memory_repository,
        provider_selector=provider_selector,
        order_factory=order_factory,
    )

    result = create_order.execute(**order_in.dict())

    order_factory.make_order.assert_called_with(**order_in.dict())
    provider_selector.get_provider.assert_called_with(Country.germany)
    in_memory_repository.add.assert_called_with(order)
    in_memory_repository.update.assert_called_with(updated_order)
    assert result == updated_order
