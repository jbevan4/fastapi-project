import unittest
from fastapi_project.domain.order import Order, Provider

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        order = Order(Provider.STRIPE, 100.0, 5.0, 5.0, 'stripe_123')
        self.assertEqual(order.provider, Provider.STRIPE)
        self.assertEqual(order.original_amount, 100.0)
        self.assertEqual(order.tax_amount, 5.0)
        self.assertEqual(order.tax_percentage, 5.0)
        self.assertEqual(order.provider_id, 'stripe_123')
