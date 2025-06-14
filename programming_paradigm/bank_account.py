
class BankAccount:
    def __init__(self, amount):
        self.balance = amount


    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True


    def display_balance(self):
        return f"Current Balance: ${self.balance}" 

