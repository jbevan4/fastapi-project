from decimal import Decimal
import pytest
from sqlmodel import Session
from fastapi_project.domain.order_factory import OrderFactory
from fastapi_project.repositories.database import init_db, get_session
from fastapi_project.domain.order import Country, Order, OrderIn
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository


@pytest.fixture
def test_db() -> Session:
    init_db()
    with get_session() as session:
        yield session


def test_add_order(test_db: Session) -> None:
    order_in = OrderIn(amount=Decimal(10), country_of_origin=Country.australia)
    order: Order = OrderFactory.make_order(order_in=order_in)
    repository = SQLiteOrderRepository(test_db)
    repository.add(order=order)
