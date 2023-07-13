from fastapi_project.domain.order import Order


class OrderFactory:
    @staticmethod
    def make_order(**kwargs: dict) -> Order:
        return Order(**kwargs)
