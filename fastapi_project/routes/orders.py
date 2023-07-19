from config import Config
from fastapi import APIRouter, Depends
from sqlmodel import Session

from fastapi_project.adapters.third_party_provider_selector import (
    ThirdPartyProviderSelector,
)
from fastapi_project.domain.order import Order, OrderIn
from fastapi_project.domain.order_factory import OrderFactory
from fastapi_project.repositories.database import get_session
from fastapi_project.repositories.factory import OrderRepositoryFactory
from fastapi_project.repositories.order.base import OrderRepository
from fastapi_project.usecases.create_order import CreateOrder

router = APIRouter()


def get_order_repository(
    session: Session = Depends(get_session),
) -> OrderRepository:
    return OrderRepositoryFactory(session=session).get_repository(
        Config.REPOSITORY_TYPE
    )


def get_create_order_use_case(
    order_repo: OrderRepository = Depends(get_order_repository),
) -> CreateOrder:
    return CreateOrder(
        order_repo=order_repo,
        provider_selector=ThirdPartyProviderSelector(),
        order_factory=OrderFactory(),
    )


@router.post("/orders/")
async def create_order_route(
    order_in: OrderIn, create_order: CreateOrder = Depends(get_create_order_use_case)
) -> Order:
    return create_order.execute(order_in=order_in)
