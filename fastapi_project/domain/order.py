from datetime import datetime
from enum import Enum
from uuid import uuid4


class Provider(Enum):
    STRIPE = 1
    CHECKOUT = 2


class Order:
    def __init__(
        self: "Order",
        provider: Provider,
        original_amount: float,
        tax_amount: float,
        tax_percentage: float,
        provider_id: str,
    ) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.provider = provider
        self.original_amount = original_amount
        self.tax_amount = tax_amount
        self.tax_percentage = tax_percentage
        self.provider_id = provider_id
