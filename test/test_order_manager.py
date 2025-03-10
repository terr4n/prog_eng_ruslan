import unittest
from online_sales.order_manager import OrderManager

class TestOrderManager(unittest.TestCase):
    def setUp(self):
        self.order_manager = OrderManager()

    def test_create_order_success(self):
        self.order_manager.create_order(order_id=100, user_id=1, items=[{"product_id": 1, "qty": 2}])
        order = self.order_manager.get_order(100)
        self.assertEqual(order["status"], "in_progress")
        self.assertEqual(order["user_id"], 1)
        self.assertEqual(len(order["items"]), 1)

    def test_create_order_duplicate(self):
        self.order_manager.create_order(order_id=101, user_id=1, items=[])
        with self.assertRaises(ValueError):
            self.order_manager.create_order(order_id=101, user_id=2, items=[])

    def test_update_order_status(self):
        self.order_manager.create_order(order_id=102, user_id=1, items=[])
        self.order_manager.update_order_status(102, "shipped")
        order = self.order_manager.get_order(102)
        self.assertEqual(order["status"], "shipped")

    def test_cancel_order(self):
        self.order_manager.create_order(order_id=103, user_id=1, items=[])
        self.order_manager.cancel_order(103)
        order = self.order_manager.get_order(103)
        self.assertEqual(order["status"], "cancelled")

    def test_get_non_existing_order(self):
        with self.assertRaises(ValueError):
            self.order_manager.get_order(999)

if __name__ == "__main__":
    unittest.main()
