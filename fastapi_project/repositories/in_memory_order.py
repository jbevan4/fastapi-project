from fastapi_project.domain.order import Order


class InMemoryOrderRepository:
    def __init__(self: "InMemoryOrderRepository") -> None:
        self.orders = []

    def add(self: "InMemoryOrderRepository", order: Order) -> None:
        self.orders.append(order)
