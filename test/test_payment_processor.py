import unittest
from online_sales.payment_processor import PaymentProcessor

class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PaymentProcessor()

    def test_process_payment_success(self):
        result = self.processor.process_payment(order_id=200, amount=100.0, payment_method="card")
        self.assertTrue(result)

    def test_process_payment_negative_amount(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment(order_id=201, amount=-50.0, payment_method="card")

    def test_refund_payment_success(self):
        result = self.processor.refund_payment(order_id=202, amount=30.0)
        self.assertTrue(result)

    def test_refund_payment_zero_amount(self):
        with self.assertRaises(ValueError):
            self.processor.refund_payment(order_id=203, amount=0)

if __name__ == "__main__":
    unittest.main()
