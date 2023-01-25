import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from bank.repositories.account import AccountRepository
from bank.services.account import AccountService

import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='bank',
    user='postgres',
    port='2023',
    password='password'
)
connection.set_session(autocommit=True)

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

class Balance(BaseModel):
    deposit: float

app = FastAPI()

account_repository = AccountRepository()
account_service = AccountService(account_repository)


@app.get('/api/accounts')
async def retrieve_products():
    responses = account_service.get_all_accounts()
    return responses

@app.get('/api/account/{account_number}')
async def retrieve_account_by_number(account_number):
    responses = account_service.get_account(account_number)
    return responses

@app.post("/account/")
async def create_account(account:Account):
    account_service.open_account(account=account)
    return {"Account": f"Account for {account.firstname} {account.lastname} has been added."}  
    
@app.put('/api/account/deposit/{account_number}')
async def update_balance(account_number, balance: Balance):
    responses = account_service.deposit(account_number, balance)
    return responses

@app.delete('/api/delete/{account_number}')
async def delete_account(account_number):
    account_service.close_account(account_number)
    return f"Account {account_number} has been deleted."


if __name__ == "__main__":
    uvicorn.run("app:app")