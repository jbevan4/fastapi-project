import pytest
from fastapi_project.adapters.checkout_provider import Checkout
from fastapi_project.adapters.stripe_provider import Stripe
from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC
from fastapi_project.adapters.third_party_provider_selector import (
    ThirdPartyProviderSelector,
)
from fastapi_project.domain.order import Country, Provider


@pytest.mark.parametrize(
    "country, expected_provider, expected_provider_name",
    [
        (Country.australia, Stripe, Provider.stripe),
        (Country.germany, Checkout, Provider.checkout),
        (Country.india, Checkout, Provider.checkout),
        (Country.uk, Checkout, Provider.checkout),
        (Country.usa, Checkout, Provider.checkout),
    ],
)
def test_get_provider(
    country: Country,
    expected_provider: ThirdPartyProviderABC,
    expected_provider_name: Provider,
) -> None:
    provider_selector = ThirdPartyProviderSelector()
    provider = provider_selector.get_provider(country)
    assert isinstance(provider, expected_provider)
    assert provider.name == expected_provider_name
