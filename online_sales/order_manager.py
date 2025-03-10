class OrderManager:
    def __init__(self):
        self.orders = {}  # Словарь: {order_id: {"items": [...], "status": ..., "user_id": ...}}

    def create_order(self, order_id, user_id, items):
        """Создаёт новый заказ."""
        if order_id in self.orders:
            raise ValueError("Order with this ID already exists.")
        self.orders[order_id] = {
            "items": items,
            "status": "in_progress",
            "user_id": user_id
        }

    def update_order_status(self, order_id, new_status):
        """Обновляет статус заказа."""
        if order_id not in self.orders:
            raise ValueError("Order not found.")
        self.orders[order_id]["status"] = new_status

    def get_order(self, order_id):
        """Получение данных о заказе."""
        if order_id not in self.orders:
            raise ValueError("Order not found.")
        return self.orders[order_id]

    def cancel_order(self, order_id):
        """Отмена заказа."""
        if order_id not in self.orders:
            raise ValueError("Order not found.")
        self.orders[order_id]["status"] = "cancelled"
