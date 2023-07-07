import unittest

from fastapi_project.domain.order import Order, Provider


class TestOrder(unittest.TestCase):
    def test_order_creation(self: "TestOrder"):
        order = Order(Provider.STRIPE, 100.0, 5.0, 5.0, "stripe_123")
        assert order.provider == Provider.STRIPE
        assert order.original_amount == 100.0
        assert order.tax_amount == 5.0
        assert order.tax_percentage == 5.0
        assert order.provider_id == "stripe_123"
