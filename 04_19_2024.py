class BankAccount:
    def __init__ (self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into accout {self.account_number}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. Current balance: {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

def main():
    account1 = BankAccount("123456", "John Doe")
    while True:
        print("\n Banking System Menu:")
        print("[1] Deposit")
        print("[2] Withdraw")
        print("[3] Balance Inquiry")
        print("[4] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account1.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account1.withdraw(amount)
        elif choice == "3":
            account1.check_balance()
        elif choice == "4":
            print("Thank you for using your banking system! \n"
                  "Exiting now...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
