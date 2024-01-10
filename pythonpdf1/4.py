class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print("Account {} created with initial balance ${}".format(account_number, initial_balance))
        else:
            print("Account {} already exists. Cannot create duplicate accounts.".format(account_number))

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print("Balance in account {}: ${}".format(account_number, self.accounts[account_number]))
        else:
            print("Account {} not found. Please check the account number.".format(account_number))

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print("${} deposited into account {}. New balance: ${}".format(amount, account_number, self.accounts[account_number]))
        else:
            print("Account {} not found. Please check the account number.".format(account_number))

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print("${} withdrawn from account {}. New balance: ${}".format(amount, account_number, self.accounts[account_number]))
            else:
                print("Insufficient funds in account {}. Cannot withdraw ${}.".format(account_number, amount))
        else:
            print("Account {} not found. Please check the account number.".format(account_number))


def main():
    bank = Bank()
    bank.create_account("123890", 1000)  # Create account with number "123890" and initial balance $1000

    while True:
        print("\nWhat would you like to do?")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter the amount to deposit: $"))
            bank.deposit(account_number, amount)

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter the amount to withdraw: $"))
            bank.withdraw(account_number, amount)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()