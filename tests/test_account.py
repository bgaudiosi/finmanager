# -*- coding: utf-8 -*-
"""
test.test_account
~~~~~~~~~~~~~~~~~~~~~

Unit tests for Account class
"""
import unittest
from datetime import datetime, timedelta
from finmanager.account import Account
from finmanager.transaction import Transaction

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.start = datetime(year=2019, month=4, day=1)
        self.checking = Account("Checking Account", self.start)
        self.transactions = [
            Transaction(self.start + timedelta(days=1), 0.40, "one"),
            Transaction(self.start + timedelta(days=1), 70, "two"),
            Transaction(self.start + timedelta(days=1), -30, "one"),
            Transaction(self.start + timedelta(days=2), 250, "three"),
            Transaction(self.start + timedelta(days=2), -65.30, "one"),
            Transaction(self.start + timedelta(days=3), 5.30, "two"),
            Transaction(self.start + timedelta(days=4), -10, "four"),
            Transaction(self.start + timedelta(days=4), 22, "five")
        ]

    def test_string(self):
        self.assertEqual(str(self.checking), "Balance for Checking Account is $0.00")

    def test_transactions(self):
        for transaction in self.transactions:
            self.checking.process_transaction(transaction)

        self.assertEqual(self.checking.balance, 242.40)

    def test_balance_at(self):
        for transaction in self.transactions:
            self.checking.process_transaction(transaction)

        self.assertRaises(ValueError, self.checking.balance_at, self.start - timedelta(days=1))
        self.assertRaises(ValueError, self.checking.balance_at, datetime.now() + timedelta(days=1))
        self.assertEqual(self.checking.balance_at(self.start + timedelta(days=2)), 225.10)

class TestCreditCard(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
