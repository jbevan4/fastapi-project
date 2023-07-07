from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class Provider(str, Enum):
    stripe = "stripe"
    checkout = "checkout"


class Order(BaseModel):
    id: UUID
    timestamp: datetime
    provider: Provider
    original_amount: float
    tax_amount: float
    tax_percentage: float
    provider_id: str
