import pytest
from fastapi_project.domain.order import Status, OrderIn, Country
from fastapi_project.domain.order_factory import OrderFactory
from fastapi_project.adapters.stripe_provider import Stripe
from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC
from fastapi_project.adapters.checkout_provider import Checkout
from decimal import Decimal


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
