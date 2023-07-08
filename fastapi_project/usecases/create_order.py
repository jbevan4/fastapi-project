from fastapi_project.adapters.third_party_provider_selector import (
    ThirdPartyProviderSelector,
)
from fastapi_project.domain.order import Order
from fastapi_project.repositories.in_memory_order import InMemoryOrderRepository
from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC


class CreateOrder:
    def __init__(
        self: "CreateOrder",
        order_repo: InMemoryOrderRepository,
        provider_selector: ThirdPartyProviderSelector,
    ) -> None:
        self.order_repo = order_repo
        self.provider_selector = provider_selector

    def execute(self: "CreateOrder", **kwargs: dict) -> Order:
        order = Order(**kwargs)
        provider: ThirdPartyProviderABC = self.provider_selector.get_provider(
            order.country_of_origin
        )
        order.provider = provider.name
        self.order_repo.add(order)
        updated_order = provider.create_payment(order)
        self.order_repo.update(updated_order)
        return updated_order
