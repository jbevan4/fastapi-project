from fastapi_project.adapters.stripe_provider import Stripe
from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC


class ThirdPartyProviderSelector:
    def __init__(self: "ThirdPartyProviderSelector") -> None:
        pass

    def get_provider(self: "ThirdPartyProviderSelector") -> ThirdPartyProviderABC:
        return Stripe()
