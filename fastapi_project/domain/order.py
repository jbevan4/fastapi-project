from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field
from decimal import Decimal
import uuid


class Provider(str, Enum):
    stripe = "stripe"
    checkout = "checkout"


class Country(str, Enum):
    usa = "USA"
    india = "India"
    germany = "Germany"
    australia = "Australia"
    uk = "UK"


class Status(str, Enum):
    pending = "pending"
    failed = "failed"
    charged = "charged"


# Then define your Pydantic models in terms of this Order class
class OrderIn(BaseModel):
    amount: Decimal
    coutry_of_origin: Country


class Order(OrderIn):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="uuid")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    provider_id: uuid.UUID | None
    provider: Provider = Field(default=None)
    status: Status = Field(default=Status.pending)
    tax_amount: Decimal = Field(default=Decimal(0.0))
    tax_percentage: Decimal = Field(default=Decimal(0.0))
    final_amount_charged: Decimal = Field(default=Decimal(0.0))
