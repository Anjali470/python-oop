class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Give valid amount"
        self.balance += amount
        return "Amount deposited successfully"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        return "Amount withdrawn successfully"

    def check_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        return 'balance updated successfully'

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            return "Insufficient Balance"
        self.balance -= amount
        return "Amount withdrawn successfully"

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            return "Insufficient Balance"
        self.balance -= amount
        return "Amount withdrawn successfully"

def main():
    print("---- Savings Account ----")
    sa = SavingsAccount(101, "John Doe", 5000, 4)

    sa.display_account_info()
    print(sa.deposit(1000))
    print(sa.withdraw(4500))  # should fail (min balance)
    print(sa.calculate_interest())
    print("Balance:", sa.check_balance())

    print("\n---- Current Account ----")
    ca = CurrentAccount(102, "Rahul", 2000, 5000)

    ca.display_account_info()
    print(ca.withdraw(6000))  # allowed (overdraft)
    print(ca.withdraw(2000))  # may exceed limit
    print("Balance:", ca.check_balance())


if __name__ == "__main__":
    main()

