class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid amount.")

account = BankAccount(100)
print("Initial Balance:", account.get_balance())
account.deposit(50)
print("Current Balance:", account.get_balance())
account.withdraw(30)
print("Current Balance:", account.get_balance())