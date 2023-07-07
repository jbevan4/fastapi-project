class InMemoryOrderRepository:
    def __init__(self: "InMemoryOrderRepository") -> None:
        self.orders = []

    def add(self: "InMemoryOrderRepository", order):
        self.orders.append(order)
