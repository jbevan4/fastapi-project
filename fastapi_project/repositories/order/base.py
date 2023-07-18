from abc import ABC, abstractmethod
from fastapi_project.domain.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def add(self: "OrderRepository", order: Order) -> None:  # pragma: no cover
        pass

    @abstractmethod
    def update(self: "OrderRepository", order: Order) -> Order:  # pragma: no cover
        pass
