class Database:
    @staticmethod
    def load_accounts():
        accounts_db = {}
        with open("accounts_db.txt", "r") as file:
            for line in file:
                account_data = line.strip().split(',')
                account_number, balance, pin = account_data
                accounts_db[account_number] = (float(balance), pin)
        return accounts_db

    @staticmethod
    def save_accounts(accounts_db):
        with open("accounts_db.txt", "w") as file:
            for account_number, (balance, pin) in accounts_db.items():
                file.write(f"{account_number},{balance:.2f},{pin}\n")
