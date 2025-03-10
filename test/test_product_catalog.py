import unittest
from online_sales.product_catalog import ProductCatalog

class TestProductCatalog(unittest.TestCase):
    def setUp(self):
        """Инициализация перед каждым тестом."""
        self.catalog = ProductCatalog()

    def test_add_product_success(self):
        """Проверяем, что товар корректно добавляется."""
        self.catalog.add_product(product_id=1, name="Test Product", price=100.0, stock=10)
        product = self.catalog.get_product(1)
        self.assertEqual(product["name"], "Test Product")
        self.assertEqual(product["price"], 100.0)
        self.assertEqual(product["stock"], 10)

    def test_add_product_duplicate_id(self):
        """Проверяем, что при добавлении дубликата возникает ошибка."""
        self.catalog.add_product(product_id=1, name="Test", price=50)
        with self.assertRaises(ValueError):
            self.catalog.add_product(product_id=1, name="Duplicate", price=70)

    def test_edit_product_success(self):
        """Проверяем успешное редактирование товара."""
        self.catalog.add_product(product_id=2, name="Old Name", price=20)
        self.catalog.edit_product(2, name="New Name", price=30)
        updated_product = self.catalog.get_product(2)
        self.assertEqual(updated_product["name"], "New Name")
        self.assertEqual(updated_product["price"], 30)

    def test_remove_product_success(self):
        """Проверяем успешное удаление товара."""
        self.catalog.add_product(product_id=3, name="Removable", price=10)
        self.catalog.remove_product(3)
        with self.assertRaises(ValueError):
            self.catalog.get_product(3)

    def test_get_non_existing_product(self):
        """Проверяем, что при запросе несуществующего товара возникает ошибка."""
        with self.assertRaises(ValueError):
            self.catalog.get_product(999)

if __name__ == "__main__":
    unittest.main()
