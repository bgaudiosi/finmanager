# -*- coding: utf-8 -*-
"""
pybudget.user
~~~~~~~~~~~~~

Contains information about a user
"""

from datetime import datetime

class User():
    def __init__(self, name: str,
                 accounts: list=[],
                 credit_cards: list=[], ,
                 loans: list=[],
                 recurring_expenses: list=[]):

        self.name = name
        self.accounts = accounts
        self.credit_cards = credit_cards
        self.loans = loans
        self.recurring_expenses = recurring_expenses

    def add_account(self, account):
        pass

    def add_credit_card(self, account):
        pass

    def add_loan(self):
        pass

    def add_recurring_expense(self):
        pass

    def add_transaction(self):
        pass

    def total_debts(self):
        pass

    def total_cash(self):
        pass

    def net_worth(self):
        pass
