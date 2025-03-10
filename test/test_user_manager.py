import unittest
from online_sales.user_manager import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    def test_register_user_success(self):
        self.user_manager.register_user(user_id=1, name="John Doe", email="john@example.com")
        user = self.user_manager.get_user(1)
        self.assertEqual(user["name"], "John Doe")
        self.assertEqual(user["email"], "john@example.com")
        self.assertEqual(user["orders"], [])

    def test_register_existing_user(self):
        self.user_manager.register_user(user_id=2, name="Jane Smith", email="jane@example.com")
        with self.assertRaises(ValueError):
            self.user_manager.register_user(user_id=2, name="Jane Duplicate", email="dup@example.com")

    def test_add_order_to_user(self):
        self.user_manager.register_user(user_id=3, name="Bob", email="bob@example.com")
        self.user_manager.add_order_to_user(user_id=3, order_id=101)
        user = self.user_manager.get_user(3)
        self.assertIn(101, user["orders"])

    def test_get_non_existing_user(self):
        with self.assertRaises(ValueError):
            self.user_manager.get_user(999)

if __name__ == "__main__":
    unittest.main()
