import uuid
from datetime import datetime
from enum import Enum

from sqlmodel import Field, Relationship, SQLModel


class OperationType(str, Enum):
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"


class Wallet(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(default=None, nullable=False, index=True)
    balance: int = Field(default=0)
    created_at: datetime = Field()
    transactions: list["Transaction"] = Relationship(back_populates="wallet")


class Transaction(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    wallet_id: uuid.UUID = Field(foreign_key="wallet.id")
    wallet: "Wallet" = Relationship(back_populates="transactions")
    operation: OperationType = Field()
    amount: int = Field()
    timestamp: datetime = Field()


Transaction.update_forward_refs()
