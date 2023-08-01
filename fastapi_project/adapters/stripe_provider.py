from decimal import Decimal
from uuid import uuid4

from fastapi_project.adapters.third_party_provider import ThirdPartyProviderABC
from fastapi_project.domain.order.order import Order, Provider, Status


class Stripe(ThirdPartyProviderABC):
    name = Provider.stripe

    def create_payment(self: "Stripe", order: Order) -> Order:
        updated_order = order.copy(
            update={
                "provider_id": uuid4(),
                "provider": self.name,
                "status": Status.charged,
                "tax_amount": Decimal(15),
                "tax_percentage": Decimal(10),
                "final_amount_charged": Decimal(15) + order.amount,
            }
        )
        return updated_order
