# encapsulation.py

class Account:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

acc = Account(1000)
acc.show_balance()
