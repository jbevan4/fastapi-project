from sqlmodel import Session

from fastapi_project.repositories.order.base import OrderRepository
from fastapi_project.repositories.order.in_memory import InMemoryOrderRepository
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository
from fastapi_project.repositories.types import RepositoryType


class OrderRepositoryFactory:
    def __init__(self: "OrderRepositoryFactory", session: Session) -> None:
        self.selector = {
            RepositoryType.SQLITE: SQLiteOrderRepository,
            RepositoryType.IN_MEMORY: InMemoryOrderRepository,
        }
        self.session = session

    def get_repository(
        self: "OrderRepositoryFactory", repository_type: RepositoryType
    ) -> OrderRepository:
        repository_cls: OrderRepository = self.selector.get(repository_type)
        if repository_cls is None:
            raise ValueError(f"Unknown repository type: {repository_type}")

        return repository_cls(session=self.session)
