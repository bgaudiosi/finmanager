# -*- coding: utf-8 -*-
"""
pybudget.account
~~~~~~~~~~~~~~~~

Implements the account class
"""
from datetime import datetime

class Account():
    def __init__(self, name: str, account_opened: datetime, transactions: list=[]):
        self.name = name
        self.account_opened = account_opened
        self.balance = 0
        self.transactions = []
        for transaction in transactions:
            self.process_transaction(transaction)

    def process_transaction(self, transaction):
        self.transactions.append(transaction)
        self.balance = round(self.balance + transaction.amount, 2)

    def account_age(self):
        return (datetime.now() - self.account_opened).days

    def balance_at(self, date):
        if date > datetime.now() or date < self.account_opened:
            raise ValueError(f"{date} cannot be before account opening date {self.account_opened} or after now.")

        old_balance = 0
        for transaction in self.transactions:
            if transaction.date <= date:
                old_balance += transaction.amount

        return round(old_balance, 2)

    def __str__(self):
        return f"Balance for {self.name} is ${round(self.balance, 2):.2f}"

    def __repr__(self):
        return self.__str__()

def CreditCard(Account):
    def __init__(self, name: str, account_opened: datetime,
                 credit_limit: float, closing_date: datetime,
                 transactions: list=[]):

        super(CreditCard, self).__init__(name, account_opened, balance=balance, transactions=transactions)
        self.credit_limit = credit_limit
        self.closing_date = closing_date

    def credit_utilization(self):
        return round(self.balance / self.credit_limit, 2)
