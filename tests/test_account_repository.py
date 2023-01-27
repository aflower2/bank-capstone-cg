import unittest

from bank.models.account import Account
from bank.models.balance import Balance
from bank.repositories.account import AccountRepository

class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self.repository = AccountRepository()
        self.inserted_account = Account(
                address="testaddy",city="la", state="ca",zipcode=123456,firstname="omar",lastname="mann",
                email="test@gmail.com",account_number=1, curr_balance=123)
        self.repository.insert(self.inserted_account)

    def tearDown(self):
        self.repository.delete(self.inserted_account.account_number)

    def test_get_by_number(self):
        get_account = self.repository.get(
            self.inserted_account.account_number)
        #elf.inserted_order.product = Account(id=self.inserted_product.id, product_number='', description='', unit_cost=0.0)
        print(get_account,"\n")
        print(get_account['Account Number'])
        
        self.assertEqual(get_account['Account Number'],'1')

if __name__ == "__main__":
    unittest.main()

          #self.assertEqual(get_account['Address'],'testaddy')

        #self.assertEqual(get_account['Current Balance'],123)

    #def test_get_all(self):

    #def update(self):
    