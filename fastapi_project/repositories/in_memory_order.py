class InMemoryOrderRepository:
    def __init__(self):
        self.orders = []

    def add(self, order):
        self.orders.append(order)
