from abc import ABC, abstractmethod


class ThirdPartyProviderABC(ABC):
    @abstractmethod
    def create_payment(self, order):
        pass
