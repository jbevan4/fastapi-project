from sqlite3 import Connection
from fastapi_project.domain.order import Order
from fastapi_project.repositories.order.base import OrderRepository


class SQLiteOrderRepository(OrderRepository):
    def __init__(
        self: "SQLiteOrderRepository", db_path: str, db_client: Connection
    ) -> None:
        self.db_path = db_path
        self.db_client = db_client

    def add(self: "SQLiteOrderRepository", order: Order) -> None:
        with self.db_client:
            cursor = self.db_client.cursor()
            cursor.execute(
                "INSERT INTO orders "
                "("
                "id,"
                "amount,"
                "country_of_origin,"
                "created_at,"
                "provider_id,"
                "provider,"
                "status,"
                "tax_amount"
                ")"
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    str(order.id),
                    order.amount,
                    order.country_of_origin.value,
                    order.created_at,
                    str(order.provider_id) if order.provider_id else None,
                    order.provider.value if order.provider else None,
                    order.status.value,
                    order.tax_amount,
                ),
            )

    def update(self: "SQLiteOrderRepository", order: Order) -> Order:
        with self.db_client:
            cursor = self.db_client.cursor()
            cursor.execute(
                "UPDATE orders "
                "SET amount = ?,country_of_origin = ?,created_at = ?,provider_id = ?,"
                "provider = ?,status = ?,tax_amount = ?"
                "WHERE id = ?",
                (
                    order.amount,
                    order.country_of_origin.value,
                    order.created_at,
                    str(order.provider_id) if order.provider_id else None,
                    order.provider.value if order.provider else None,
                    order.status.value,
                    order.tax_amount,
                    str(order.id),
                ),
            )
        return order
