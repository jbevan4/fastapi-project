from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi_project.adapters.third_party_provider import ThirdPartyProviderAdapter
from fastapi_project.domain.order import OrderIn, OrderOut
from fastapi_project.repositories.in_memory_order import InMemoryOrderRepository
from fastapi_project.usecases.create_order import CreateOrder


router = APIRouter()


def get_order_repo() -> InMemoryOrderRepository:
    return InMemoryOrderRepository()


def get_provider_adapter() -> ThirdPartyProviderAdapter:
    return ThirdPartyProviderAdapter()


def get_create_order_use_case(
    order_repo: InMemoryOrderRepository = Depends(get_order_repo),
    provider_adapter: ThirdPartyProviderAdapter = Depends(get_provider_adapter),
) -> CreateOrder:
    return CreateOrder(order_repo, provider_adapter)


@router.post("/orders/")
async def create_order_route(
    order: OrderIn, create_order: CreateOrder = Depends(get_create_order_use_case)
) -> OrderOut:
    return OrderOut.from_order(
        create_order.execute(
            order.provider,
            order.original_amount,
            order.tax_amount,
            order.tax_percentage,
            order.provider_id,
            timestamp=datetime.now(),
        )
    )
