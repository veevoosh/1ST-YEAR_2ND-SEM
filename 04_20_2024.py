import uuid

class BankAccount:
    def __init__(self, first_name, last_name, password, balance=0):
        self.account_number = str(uuid.uuid4())[:6]
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. Current balance: {self.balance}")

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. Current balance: {self.balance}")

        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

    def change_password(self):
        old_password = input("Please enter your old password to begin creating a new password: ")

        if old_password == self.password:
            new_password = input("Enter your new password: ")
            self.password = new_password
            print("Change password complete!")

        else:
            print("Invalid input! Please try again.")


def main():

    global account

    while True:
        print("\n Banking System Menu:")
        print("[1] Open an Account")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Balance Inquiry")
        print("[5] Change Password")
        print("[6] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            password = input("Enter a password: ")
            account = BankAccount(first_name, last_name, password)
            print(f"Account opened successfully! Your account number is {account.account_number}")

        elif choice == "2":
            user_password = input("Please enter your password to start this transaction: ")

            if user_password == account.password:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

            else:
                print("Incorrect password. Please try again.")
                main()

        elif choice == "3":
            user_password = input("Please enter your password to start this transaction: ")

            if user_password == account.password:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)

            else:
                print("Incorrect password. Please try again.")
                main()

        elif choice == "4":
            user_password = input("Please enter your password to start this transaction: ")

            if user_password == account.password:
                account.check_balance()

            else:
                print("Incorrect password. Please try again.")
                main()

        elif choice == "5":
            account.change_password()

        elif choice == "6":
            print("Thank you for using our banking system! \n"
                  "Exiting now...")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
