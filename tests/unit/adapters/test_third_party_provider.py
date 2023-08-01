from decimal import Decimal

import pytest
from fastapi_project.adapters.checkout_provider import Checkout
from fastapi_project.adapters.stripe_provider import Stripe
from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC
from fastapi_project.domain.order.order import Country, OrderIn, Status
from fastapi_project.domain.order.order_factory import OrderFactory


@pytest.mark.parametrize("provider_class", [(Checkout), (Stripe)])
def test_create_payment(
    provider_class: ThirdPartyProviderABC,
) -> None:
    provider: ThirdPartyProviderABC = provider_class()
    order = OrderFactory.make_order(
        order_in=OrderIn(amount=Decimal(10), country_of_origin=Country.australia)
    )

    updated_order = provider.create_payment(order)
    assert updated_order.provider == provider.name
    assert order.id == updated_order.id
    assert updated_order.status == Status.charged
