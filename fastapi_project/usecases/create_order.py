from .domain.order import Order, Provider
from .adapters.third_party_provider import ThirdPartyProviderAdapter
from .repositories.in_memory_order_repository import InMemoryOrderRepository

class CreateOrder:
    def __init__(self, order_repo: InMemoryOrderRepository, provider_adapter: ThirdPartyProviderAdapter):
        self.order_repo = order_repo
        self.provider_adapter = provider_adapter

    def execute(self, provider: Provider, original_amount: float, tax_amount: float, tax_percentage: float, provider_id: str):
        order = Order(provider, original_amount, tax_amount, tax_percentage, provider_id)
        self.order_repo.add(order)
        self.provider_adapter.send_order(order)
        return order
