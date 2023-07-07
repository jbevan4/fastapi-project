from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from uuid import UUID, uuid4


class Provider(str, Enum):
    stripe = "stripe"
    checkout = "checkout"


class Order:
    def __init__(
        self: "Order",
        timestamp: datetime,
        provider: Provider,
        original_amount: float,
        tax_amount: float,
        tax_percentage: float,
        provider_id: str,
    ) -> None:
        self.id = uuid4()
        self.timestamp = timestamp
        self.provider = provider
        self.original_amount = original_amount
        self.tax_amount = tax_amount
        self.tax_percentage = tax_percentage
        self.provider_id = provider_id


# Then define your Pydantic models in terms of this Order class
class OrderIn(BaseModel):
    provider: Provider
    original_amount: float
    tax_amount: float
    tax_percentage: float
    provider_id: str

    def to_order(self: "OrderIn") -> Order:
        return Order(
            self.timestamp,
            self.provider,
            self.original_amount,
            self.tax_amount,
            self.tax_percentage,
            self.provider_id,
        )


class OrderOut(BaseModel):
    id: UUID
    timestamp: datetime
    provider: Provider
    original_amount: float
    tax_amount: float
    tax_percentage: float
    provider_id: str

    @staticmethod
    def from_order(order: Order) -> "OrderOut":
        return OrderOut(
            id=order.id,
            timestamp=order.timestamp,
            provider=order.provider,
            original_amount=order.original_amount,
            tax_amount=order.tax_amount,
            tax_percentage=order.tax_percentage,
            provider_id=order.provider_id,
        )
