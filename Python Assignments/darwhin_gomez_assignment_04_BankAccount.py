## THis is Baccount Class
class BankAccount:
    def __init__(self, bankname, firstname, lastname, balance=0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

    def __str__(self):
        return f"Bank: {self.bankname}, Owner: {self.firstname} {self.lastname}, Balance: ${self.balance}"


# Testing BankAccount class
account1 = BankAccount("CUNY Banks ", "Arron", "Judge")
account2 = BankAccount("NYSPB", "Juan", "Soto", 540000)
print(account1)

account1.deposit(10000)

account1.withdrawal(5000)

account1.withdrawal(5160)

account1.deposit(15000000)

print(account2)
account2.deposit(1200000)
account2.deposit(1500000)
account2.withdrawal(154514)
account2.withdrawal(14748474)
