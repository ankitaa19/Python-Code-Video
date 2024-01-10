class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

class Transaction:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def withdraw_cash(self):
        if self.amount > 0 and self.amount <= self.account.balance:
            self.account.balance -= self.amount
            return f"Withdrawal successful. Remaining balance: ${self.account.balance}"
        else:
            return "Withdrawal failed. Invalid amount or insufficient balance."

    def check_balance(self):
        return f"Current balance: ${self.account.balance}"

class User:
    def __init__(self, user_id, name, accounts):
        self.user_id = user_id
        self.name = name
        self.accounts = accounts

class ATMSimulation:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def authenticate_user(self, user_id, entered_pin):
        for user in self.users:
            if user.user_id == user_id:
                for account in user.accounts:
                    if account.verify_pin(entered_pin):
                        return user, account
        return None, None  #Authentication failed

    def perform_transaction(self, user, account, transaction_type, amount=None):
        if transaction_type == "withdraw":
            transaction = Transaction(account, amount)
            return transaction.withdraw_cash()
        elif transaction_type == "check_balance":
            transaction = Transaction(account, 0)
            return transaction.check_balance()
        else:
            return "Invalid transaction type."


account1 = Account(account_number=123456789, pin=1234, balance=1000)
account2 = Account(account_number=987654321, pin=4321, balance=500)

user1 = User(user_id=1, name="Ankita", accounts=[account1])
user2 = User(user_id=2, name="Sam", accounts=[account2])

atm_simulation = ATMSimulation()
atm_simulation.add_user(user1)
atm_simulation.add_user(user2)

#Athentication and transaction
user_id_to_authenticate = 1
entered_pin = 1234
user, account = atm_simulation.authenticate_user(user_id_to_authenticate, entered_pin)

if user and account:
    #Cash Withdraw
    withdrawal_amount = 200
    withdrawal_result = atm_simulation.perform_transaction(user, account, "withdraw", amount=withdrawal_amount)
    print(withdrawal_result)

    #Balance
    balance_result = atm_simulation.perform_transaction(user, account, "check_balance")
    print(balance_result)
else:
    print("User authentication failed. Please check user ID and PIN.")