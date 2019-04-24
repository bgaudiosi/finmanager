# -*- coding: utf-8 -*-
"""
pybudget.transaction
~~~~~~~~~~~

Transaction Class
"""

from datetime import datetime

class Transaction():
    def __init__(self, date: datetime, amount: int, party: str, description: str=""):
        self.date = date
        self.amount = amount
        self.party = party
        self.description = description

    @classmethod
    def fromBOATransaction(cls):
        pass

    def __str__(self):
        string = (f"Date: {self.date.strftime('%Y-%m-%d')}\n"
                  f"Amount: ${self.amount:0.2f}\n"
                  f"Party: {self.party}")
        if self.description:
            string += "\n" + f"Description: {self.description}"
        return string

    def __repr___(self):
        return self.__str__()
