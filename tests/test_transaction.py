# -*- coding: utf-8 -*-
"""
test.test_transaction
~~~~~~~~~~~~~~~~~~~~~

Unit tests for Transaction class
"""
import unittest
from datetime import datetime
from finmanager.transaction import Transaction

class TestTransactionMethods(unittest.TestCase):
    def setUp(self):
        self.transaction_1 = Transaction(datetime(year=2019, month=4, day=20), 100.11, "Ayy Lmao Inc.")

    def test_string(self):
        self.assertEqual(str(self.transaction_1), "Date: 2019-04-20\nAmount: $100.11\nParty: Ayy Lmao Inc.")

if __name__ == "__main__":
    unittest.main()
