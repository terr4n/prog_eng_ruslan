class UserManager:
    def __init__(self):
        self.users = {}  # {user_id: {"name": ..., "email": ..., "orders": [...], ...}}

    def register_user(self, user_id, name, email):
        """Регистрация нового пользователя."""
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = {"name": name, "email": email, "orders": []}

    def get_user(self, user_id):
        """Получение информации о пользователе."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        return self.users[user_id]

    def add_order_to_user(self, user_id, order_id):
        """Привязка заказа к пользователю."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        self.users[user_id]["orders"].append(order_id)
