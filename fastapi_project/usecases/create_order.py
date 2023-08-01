from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC
from fastapi_project.adapters.third_party_provider_selector import (
    ThirdPartyProviderSelector,
)
from fastapi_project.domain.order.order import Order, OrderIn
from fastapi_project.domain.order.order_factory import OrderFactory
from fastapi_project.repositories.order.in_memory import InMemoryOrderRepository


class CreateOrder:
    def __init__(
        self: "CreateOrder",
        order_repo: InMemoryOrderRepository,
        provider_selector: ThirdPartyProviderSelector,
        order_factory: OrderFactory,
    ) -> None:
        self.order_repo = order_repo
        self.provider_selector = provider_selector
        self.order_factory = order_factory

    def execute(self: "CreateOrder", order_in: OrderIn) -> Order:
        order = self.order_factory.make_order(order_in=order_in)
        provider: ThirdPartyProviderABC = self.provider_selector.get_provider(
            order.country_of_origin
        )
        order.provider = provider.name
        self.order_repo.add(order)
        updated_order = provider.create_payment(order)
        self.order_repo.update(updated_order)
        return updated_order
