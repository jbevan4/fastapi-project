from fastapi_project.domain.order import Order


class ThirdPartyProviderAdapter:
    def __init__(self: "ThirdPartyProviderAdapter") -> None:
        pass

    def send_order(self: "ThirdPartyProviderAdapter", order: Order) -> None:
        pass
