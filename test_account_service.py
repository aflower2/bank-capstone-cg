import unittest
from unittest.mock import Mock
from bank.models.balance import Balance
from bank.models.account import Account
from bank.repositories.account import AccountRepository
from bank.services.account import AccountService

class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.balance = Balance(100.00)
        self.account = Account()
        self.product_repository = Mock()
        self.orderRepository = Mock()
        self.orderService = OrderService(self.orderRepository, self.product_repository)

    def test_add_new_order(self):
        self.product_repository.get_by_id = Mock(return_value=self.product)
        self.orderRepository.insert = Mock(return_value=self.order)
        new_order = self.orderService.add_new(self.order)
        self.assertEqual(new_order, self.order)

    def test_get_one_order(self):
        self.orderRepository.get_by_number = Mock(return_value=self.order)
        get_order = self.orderService.get_one("000")
        self.assertEqual(get_order, self.order)


if __name__ == "__main__":
    unittest.main()