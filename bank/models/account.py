from pydantic import BaseModel
from orders.models.product import Product


class Account(BaseModel):
    address: str
    city: str
    state: str
    zipcode: str
    firstname: str
    lastname: str
    email: str
    account_number: str
    curr_balance: float

    def __eq__(self, other):
        return self.address == other.address and self.city == other.city and \
            self.state == other.state and self.zipcode == other.zipcode and self.firstname == other.firstname and \
                self.lastname == other.lastname and self.email == other.email and self.account_number == other.account_number and \
                    self.curr_balance == other.curr_balance 
                