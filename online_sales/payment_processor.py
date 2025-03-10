class PaymentProcessor:
    def process_payment(self, order_id, amount, payment_method):
        """
        Псевдо-обработка платежа.
        В реальном проекте — интеграция с платёжным шлюзом.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        # Допустим, всё прошло успешно:
        return True

    def refund_payment(self, order_id, amount):
        """
        Возврат средств.
        Аналогично, здесь был бы вызов API платёжной системы.
        """
        if amount <= 0:
            raise ValueError("Refund amount must be positive.")
        return True
