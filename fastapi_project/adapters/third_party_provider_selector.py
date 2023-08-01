from fastapi_project.adapters.checkout_provider import Checkout
from fastapi_project.adapters.stripe_provider import Stripe
from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC
from fastapi_project.domain.order.order import Country


class ThirdPartyProviderSelector:
    def __init__(self: "ThirdPartyProviderSelector") -> None:
        pass

    def get_provider(
        self: "ThirdPartyProviderSelector", country: Country
    ) -> ThirdPartyProviderABC:
        if country == country.australia:
            return Stripe()
        return Checkout()
