from fastapi_project.repositories.order.base import OrderRepository
from fastapi_project.repositories.order.in_memory import InMemoryOrderRepository
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository


class OrderRepositoryFactory:
    def __init__(
        self: "OrderRepositoryFactory",
        in_memory: InMemoryOrderRepository,
        sqlite: SQLiteOrderRepository,
    ) -> None:
        self.selector = {
            "sqlite": sqlite,
            "in_memory": in_memory,
        }

    def get_repository(
        self: "OrderRepositoryFactory", repository_type: str
    ) -> OrderRepository:
        create_func = self.selector.get(repository_type)
        if create_func is None:
            raise ValueError(f"Unknown repository type: {repository_type}")
        return self.selector[repository_type]
