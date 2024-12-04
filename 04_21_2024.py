import random  # import random for generating random account numbers
from shlex import join  # import "join" from "shlex" for generate account number


class BankAccount:
    def __init__(self, first_name, last_name, balance=0):  # initialize class BankAccount
        self.account_number = self.generate_account_number()
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    @staticmethod  # put "@staticmethod" for formatting
    def generate_account_number():  # generating bank account number using "random" module
        return join(str(random.randint(0, 9)) for _ in range(10))

    def deposit(self, amount):  # depositing funds into the created bank account
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):  # withdrawing funds from created bank account
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")

    def check_balance(self):  # check current balance of created bank account from past transactions
        print(f"Current balance: ${self.balance}")


class SavingsAccount(BankAccount):  # inherit attributes from BankAccount to SavingsAccount
    def __init__(self, first_name, last_name, balance=0, interest_rate=0.02):
        super().__init__(first_name, last_name, balance)
        self.interest_rate = interest_rate  # with added regular interest rate

    def calculate_interest(self):  # calculate the regular interest rate for a savings account
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest calculated: ${interest}. New balance: ${self.balance}")


class PremiumSavingsAccount(SavingsAccount):  # inherit attributes from SavingsAccount to PremiumSavingsAccount
    def __init__(self, first_name, last_name, balance=0, interest_rate=0.02, bonus_interest_rate=0.01):
        super().__init__(first_name, last_name, balance, interest_rate)
        self.bonus_interest_rate = bonus_interest_rate  # with added additional bonus interest rate

    def calculate_bonus_interest(self):  # calculate the bonus interest rate for a premium savings account
        bonus_interest = self.balance * self.bonus_interest_rate
        self.balance += bonus_interest
        print(f"Bonus interest calculated: ${bonus_interest}. New balance: ${self.balance}")


def main():
    accounts = []  # empty list to store created bank accounts
    while True:
        print("\nOnline Banking System Menu:")
        print("[1] Open an Account")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Balance Inquiry")
        print("[5] Calculate Interest (Savings Account)")
        print("[6] Calculate Bonus Interest (Premium Savings Account)")
        print("[7] Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            account_type = input("Enter account type: \n"
                                 "Type [1] for Savings \n"
                                 "Type [2] for Premium Savings \n"
                                 "> ")
            if account_type == '1':
                account = SavingsAccount(first_name, last_name)
            elif account_type == '2':
                account = PremiumSavingsAccount(first_name, last_name)
            else:
                print("Invalid account type")
                continue
            accounts.append(account)
            print(f"Account created successfully. Your account number is: {account.account_number}")

        elif choice in {'2', '3', '4', '5', '6'}:
            account_number = input("Enter account number: ")
            account = next((acc for acc in accounts if acc.account_number == account_number), None)
            if account:
                if choice == '2':
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                elif choice == '4':
                    account.check_balance()
                elif choice == '5' and isinstance(account, SavingsAccount):
                    account.calculate_interest()
                elif choice == '6' and isinstance(account, PremiumSavingsAccount):
                    account.calculate_bonus_interest()
                else:
                    print("Account not found. Please try again.")

        elif choice == '7':
            print("Exiting the program \n"
                  "...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
