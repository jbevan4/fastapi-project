from enum import Enum

from fastapi_project.repositories.order.base import OrderRepository
from fastapi_project.repositories.order.in_memory import InMemoryOrderRepository
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository


class RepositoryType(Enum):
    SQLITE = "sqlite"
    IN_MEMORY = "in_memory"


class OrderRepositoryFactory:
    def __init__(
        self: "OrderRepositoryFactory",
        in_memory: InMemoryOrderRepository,
        sqlite: SQLiteOrderRepository,
    ) -> None:
        self.selector = {
            RepositoryType.SQLITE: sqlite,
            RepositoryType.IN_MEMORY: in_memory,
        }

    def get_repository(
        self: "OrderRepositoryFactory", repository_type: RepositoryType
    ) -> OrderRepository:
        create_func = self.selector.get(repository_type)
        if create_func is None:
            raise ValueError(f"Unknown repository type: {repository_type}")
        return self.selector[repository_type]
