from pydantic import BaseModel


class Balance(BaseModel):
    deposit: float

    def __eq__(self, other):
        return self.deposit == other.deposit