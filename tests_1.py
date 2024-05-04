import unittest
from utils import read_transactions, get_transaction_amount_rub

class TestUtils(unittest.TestCase):
    def test_read_transactions_empty(self):
        self.assertEqual(read_transactions("nonexistent_file.json"), [])

    def test_read_transactions_valid(self):
        transactions = read_transactions("data/operations.json")
        self.assertIsInstance(transactions, list)
        self.assertGreater(len(transactions), 0)

    def test_get_transaction_amount_rub(self):
        test_cases = [
            ({"amount": 100, "currency": "RUB"}, 100.0),
            ({"amount": 100, "currency": "USD"}, 95.0),  # Примерный курс
            ({"amount": 100, "currency": "EUR"}, 105.0),  # Примерный курс
        ]
        for transaction, expected_amount in test_cases:
            self.assertAlmostEqual(
                get_transaction_amount_rub(transaction), expected_amount, delta=5
            )
