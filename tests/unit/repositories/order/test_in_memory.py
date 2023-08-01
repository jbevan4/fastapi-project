import pytest
from fastapi_project.domain.order.order import Country, Order, Status
from fastapi_project.repositories.order.in_memory import InMemoryOrderRepository


@pytest.fixture
def order() -> Order:
    return Order(amount=10.0, country_of_origin=Country.australia)


def test_add_order(order: Order) -> None:
    repository = InMemoryOrderRepository()
    repository.add(order)
    retrieved_order = repository.orders[0]
    assert retrieved_order == order
    assert len(repository.orders) == 1


def test_update_order(order: Order) -> None:
    repository = InMemoryOrderRepository()
    repository.add(order)
    updated_order = order.copy(update={"status": Status.charged})
    repository.update(updated_order)
    retrieved_order = repository.orders[0]
    assert retrieved_order == updated_order


def test_update_order_errors_when_unable_to_find_the_original_order(
    order: Order,
) -> None:
    repository = InMemoryOrderRepository()
    with pytest.raises(ValueError, match=f"No order found with id: {order.id}"):
        repository.update(order)
