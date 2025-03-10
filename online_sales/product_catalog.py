class ProductCatalog:
    def __init__(self):
        self.products = {}  # Словарь: {product_id: {"name": ..., "price": ..., "stock": ...}}

    def add_product(self, product_id, name, price, stock=0):
        """Добавляет новый товар в каталог."""
        if product_id in self.products:
            raise ValueError("Product with this ID already exists.")
        self.products[product_id] = {
            "name": name,
            "price": price,
            "stock": stock
        }

    def edit_product(self, product_id, **kwargs):
        """Редактирует свойства товара."""
        if product_id not in self.products:
            raise ValueError("Product not found.")
        for key, value in kwargs.items():
            if key in self.products[product_id]:
                self.products[product_id][key] = value

    def remove_product(self, product_id):
        """Удаляет товар из каталога."""
        if product_id not in self.products:
            raise ValueError("Product not found.")
        del self.products[product_id]

    def get_product(self, product_id):
        """Возвращает информацию о товаре."""
        if product_id not in self.products:
            raise ValueError("Product not found.")
        return self.products[product_id]
