from sqlmodel import Session
from fastapi_project.domain.order import Order
from fastapi_project.repositories.order.base import OrderRepository


class SQLiteOrderRepository(OrderRepository):
    def __init__(self: "SQLiteOrderRepository", session: Session) -> None:
        self.session = session

    def add(self: "SQLiteOrderRepository", order: Order) -> None:
        self.session.add(order)
        self.session.commit()

    def update(self: "SQLiteOrderRepository", order: Order) -> Order:
        pass
