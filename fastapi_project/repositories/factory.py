from fastapi_project.repositories.database import get_session
from fastapi_project.repositories.order.base import OrderRepository
from fastapi_project.repositories.order.in_memory import InMemoryOrderRepository
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository


class OrderRepositoryFactory:
    def __init__(self: "OrderRepositoryFactory") -> None:
        self.selector = {
            "sqlite": self._create_sqlite_repository,
            "in_memory": self._create_in_memory_repository,
        }

    def create_repository(
        self: "OrderRepositoryFactory", repository_type: str
    ) -> OrderRepository:
        create_func = self.selector.get(repository_type)
        if create_func is None:
            raise ValueError(f"Unknown repository type: {repository_type}")
        return create_func()

    def _create_sqlite_repository(self: "OrderRepositoryFactory") -> OrderRepository:
        session = get_session()
        return SQLiteOrderRepository(session)

    def _create_in_memory_repository(self: "OrderRepositoryFactory") -> OrderRepository:
        return InMemoryOrderRepository()
