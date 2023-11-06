import random
class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return 0

    def deposit(self, amount):
        self.balance += amount
        return amount

    def get_balance(self):
        return self.balance


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, balance, pin):
        account = Account(account_number, balance, pin)
        self.accounts[account_number] = account

    def login(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            return self.accounts[account_number]
        else:
            return None

    def display_menu(self):
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

    def main_menu(self):
        while True:
            print("Welcome to the ATM")
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")

            account = self.login(account_number, pin)

            if account:
                while True:
                    self.display_menu()
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        balance = account.get_balance()
                        print(f"Your balance: ${balance:.2f}")
                    elif choice == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        withdrawn = account.withdraw(amount)
                        if withdrawn:
                            print(f"Withdrew: ${withdrawn:.2f}")
                        else:
                            print("Insufficient funds")
                    elif choice == '3':
                        amount = float(input("Enter the amount to deposit: "))
                        deposited = account.deposit(amount)
                        print(f"Deposited: ${deposited:.2f}")
                    elif choice == '4':
                        print("Thank you for using the ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
            else:
                print("Invalid account number or PIN. Please try again.")


if __name__ == "__main__":
    atm = ATM()
    accounts_db = {}
    try:
        with open("accounts_db.txt", "r") as file:
            for line in file:
                account_data = line.strip().split(',')
                account_number, balance, pin = account_data
                accounts_db[account_number] = Account(account_number, float(balance), pin)
    except FileNotFoundError:
        pass

    while True:
        print("Welcome to the ATM")
        choice = input("Are you a new user? (yes/no): ")
        if choice.lower() == "yes":
            account_number = str(random.randint(100000, 999999))
            pin = str(random.randint(1000, 9999))
            print(f"Your new account number is: {account_number}")
            print(f"Your new PIN is: {pin}")
            deposit_amount = float(input("Please deposit 1000 Rs to activate your account: "))
            if deposit_amount == 1000:
                account = Account(account_number, 1000.0, pin)
                accounts_db[account_number] = account
                print("Your account has been activated.")
            else:
                print("Invalid deposit amount. Your account has not been created.")

        elif choice.lower() == "no":
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")

            account = accounts_db.get(account_number)  

            if account and account.pin == pin:
                print("Welcome to your account!")
                while True:
                    atm.display_menu()
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        balance = account.get_balance()
                        print(f"Your balance: ${balance:.2f}")
                    elif choice == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        withdrawn = account.withdraw(amount)
                        if withdrawn:
                            print(f"Withdrew: ${withdrawn:.2f}")
                        else:
                            print("Insufficient funds")
                    elif choice == '3':
                        amount = float(input("Enter the amount to deposit: "))
                        deposited = account.deposit(amount)
                        print(f"Deposited: ${deposited:.2f}")
                    elif choice == '4':
                        print("Thank you for using the ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
            else:
                print("Invalid account number or PIN. Please try again.")
    with open("accounts_db.txt", "w") as file:
        for account_number, acc in accounts_db.items():
            file.write(f"{account_number},{acc.get_balance():.2f},{acc.pin}\n")