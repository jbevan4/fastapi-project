from abc import ABC, abstractmethod

from fastapi_project.domain.order.order import Order


class ThirdPartyProviderABC(ABC):
    name: str

    @abstractmethod
    def create_payment(
        self: "ThirdPartyProviderABC", order: Order
    ) -> Order:  # pragma: no cover
        pass
