import uuid


class Bank:
    def __init__(self, name):
        self.name = name

    def create_account(self, account_number, account_holder_name, password, initial_balance, account_type):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.password = password
        self.initial_balance = initial_balance
        self.account_type = account_type

    def close_account(self, account_number):
        self.account_number = account_number
        account_number = input("Enter account number to close: ")

        if account_number == self.account_number:
            print(f"Account {account_number} closed successfully.")

        else:
            print("Invalid input. Please enter a valid account number.")
            main()

    def approve_loan(self, account_number, loan_amount, interest_rate):
        self.account_number = account_number
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        account_number = input("Enter account number to approve loan: ")

        if account_number == self.account_number:
            loan_amount = int(input("Enter loan amount: "))
            interest_rate = int(input("Enter interest rate: "))
            print(
                f"Account {account_number} has been given a loan of {loan_amount} with an interest rate of {interest_rate} %.")

        else:
            print("Invalid input. Please enter a valid account number.")
            main()


class Account:
    def __init__(self, account_number, account_holder_name, password, initial_balance, account_type):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.password = password
        self.initial_balance = initial_balance
        self.account_type = account_type

    def deposit(self, amount):
        self.initial_balance += amount
        print(f"Deposited {amount} into account {self.account_number}. Current balance: {self.initial_balance}")

    def withdraw(self, amount):
        if amount <= self.initial_balance:
            self.initial_balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. Current balance: {self.initial_balance}")

        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.initial_balance}")


class Loan:
    def __init__(self, account_number, loan_amount, interest_rate):
        self.self = None
        self.account_number = account_number
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate

    def approve_loan(self):
        self.self = self


def main():
    global account, account_number, password, bank

    while True:
        print("\n Bank Management System Menu:")
        print("[1] Create Account")
        print("[2] Close Account")
        print("[3] Approve Loan")
        print("[4] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = str(uuid.uuid4())[:6]
            account_holder_name = input("Enter account holder name: ")
            password = input("Enter administration password: ")
            initial_balance = int(input("Enter initial balance: "))
            account_type = input("Enter account type: ")

            bank = Bank(name=None)
            bank.create_account(account_number, account_holder_name, password, initial_balance, account_type)

            print(f"Account created successfully! Account Number: {bank.account_number}")

        elif choice == "2":
            user_password = input("Please enter administration password to continue: ")

            if user_password == bank.password:
                bank.close_account(account_number)

            else:
                print("Incorrect password. Please try again.")
                main()

        elif choice == "3":
            user_password = input("Please enter administration password to continue: ")

            if user_password == bank.password:
                bank.approve_loan(account_number, loan_amount=None, interest_rate=None)

            else:
                print("Incorrect password. Please try again.")
                main()

        elif choice == "4":
            print("Exiting the program... \n"
                  "Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
