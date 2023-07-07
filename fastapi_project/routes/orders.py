from fastapi import APIRouter
from ..domain import OrderCreate
from ..usecases import create_order

router = APIRouter()


@router.post("/orders/")
async def create_order_route(order: OrderCreate):
    return create_order(order)
