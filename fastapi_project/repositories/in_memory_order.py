from fastapi_project.domain.order import Order
from typing import List


class InMemoryOrderRepository:
    def __init__(self: "InMemoryOrderRepository") -> None:
        self.orders: List[Order] = []

    def add(self: "InMemoryOrderRepository", order: Order) -> None:
        print(order)
        self.orders.append(order)

    def update(self: "InMemoryOrderRepository", order: Order) -> Order:
        print(order)
        for i, o in enumerate(self.orders):
            if o.id == order.id:
                self.orders[i] = order
                return
        raise ValueError(f"No order found with id: {order.id}")
