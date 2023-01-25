from bank.models.account import Account
from bank.models.balance import Balance
from bank.repositories.account import AccountRepository


class AccountService():
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def open_account(self, account: Account):
        return self.account_repository.insert(account)

    def get_account(self, account_number):
        return self.account_repository.get(account_number)

    def get_all_accounts(self):
        return self.account_repository.get_all()
        

    def deposit(self, account_number, balance: Balance):
        return self.account_repository.update(account_number, balance)

    def close_account(self, account_number):
        return self.account_repository.delete(account_number)