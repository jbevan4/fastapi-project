from fastapi_project.domain.order.order import Order, OrderIn


class OrderFactory:
    @staticmethod
    def make_order(order_in: OrderIn) -> Order:
        return Order(**order_in.dict())
