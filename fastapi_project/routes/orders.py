from fastapi import APIRouter, Depends

from fastapi_project.adapters.third_party_provider_selector import (
    ThirdPartyProviderSelector,
)
from fastapi_project.config import Config
from fastapi_project.domain.order import Order, OrderIn
from fastapi_project.domain.order_factory import OrderFactory
from fastapi_project.repositories.factory import OrderRepositoryFactory
from fastapi_project.repositories.order.in_memory import InMemoryOrderRepository
from fastapi_project.usecases.create_order import CreateOrder

router = APIRouter()


def get_order_repo() -> InMemoryOrderRepository:
    factory = OrderRepositoryFactory()
    return factory.create_repository(Config.REPOSITORY_TYPE)


def get_third_party_provider_selector() -> ThirdPartyProviderSelector:
    return ThirdPartyProviderSelector()


def get_order_factory() -> OrderFactory:
    return OrderFactory()


def get_create_order_use_case(
    order_repo: InMemoryOrderRepository = Depends(get_order_repo),
    provider_selector: ThirdPartyProviderSelector = Depends(
        get_third_party_provider_selector
    ),
    order_factory: OrderFactory = Depends(get_order_factory),
) -> CreateOrder:
    return CreateOrder(
        order_repo=order_repo,
        provider_selector=provider_selector,
        order_factory=order_factory,
    )


@router.post("/orders/")
async def create_order_route(
    order_in: OrderIn, create_order: CreateOrder = Depends(get_create_order_use_case)
) -> Order:
    return create_order.execute(order_in=order_in)
