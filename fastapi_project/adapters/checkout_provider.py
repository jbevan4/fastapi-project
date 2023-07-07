from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC
from fastapi_project.domain.order import Provider


class Checkout(ThirdPartyProviderABC):
    name = Provider.checkout

    def create_payment(self, order):
        return super().create_payment(order)
