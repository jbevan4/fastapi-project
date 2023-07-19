from decimal import Decimal
import pytest
from sqlmodel import Session
import os
from fastapi_project.domain.order_factory import OrderFactory
from sqlmodel import create_engine, SQLModel
from fastapi_project.domain.order import Country, Order, OrderIn
from fastapi_project.repositories.order.sqlite import SQLiteOrderRepository


@pytest.fixture
def test_db_session() -> Session:
    test_db_url = "sqlite:///test.db"
    test_engine = create_engine(test_db_url)
    SQLModel.metadata.create_all(test_engine)

    session = Session(test_engine)

    yield session

    session.close()
    os.remove("test.db")


def test_add_order(test_db_session: Session) -> None:
    order_in = OrderIn(amount=Decimal(10), country_of_origin=Country.australia)
    order: Order = OrderFactory.make_order(order_in=order_in)
    repository = SQLiteOrderRepository(test_db_session)
    repository.add(order=order)

    # Query the database for the order
    db_order = test_db_session.query(Order).first()

    # Assert that the order was added correctly
    assert db_order is not None, "Order was not added to the database"
    assert db_order.id == order.id, "Order ID did not match"
    assert db_order.amount == order.amount, "Order amount did not match"
    assert (
        db_order.country_of_origin == order.country_of_origin
    ), "Order country of origin did not match"
