from fastapi_project.domain.order import Order
from fastapi_project.repositories.order.base import OrderRepository
from typing import List


class InMemoryOrderRepository(OrderRepository):
    def __init__(self: "InMemoryOrderRepository") -> None:
        self.orders: List[Order] = []

    def add(self: "InMemoryOrderRepository", order: Order) -> None:
        self.orders.append(order)

    def update(self: "InMemoryOrderRepository", order: Order) -> Order:
        for i, o in enumerate(self.orders):
            if o.id == order.id:
                self.orders[i] = order
                return
        raise ValueError(f"No order found with id: {order.id}")