from decimal import Decimal
from uuid import uuid4

from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC
from fastapi_project.domain.order.order import Order, Provider, Status


class Checkout(ThirdPartyProviderABC):
    name = Provider.checkout

    def create_payment(self: "Checkout", order: Order) -> Order:
        updated_order = order.copy(
            update={
                "provider_id": uuid4(),
                "provider": self.name,
                "status": Status.charged,
                "tax_amount": Decimal(10),
                "tax_percentage": Decimal(5),
                "final_amount_charged": Decimal(10) + order.amount,
            }
        )
        return updated_order
