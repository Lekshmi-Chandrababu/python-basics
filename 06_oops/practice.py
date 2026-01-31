# practice.py

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

acc = BankAccount("Lekshmi", 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.show_balance()
