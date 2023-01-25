from bank.models.account import Account
from bank.models.balance import Balance
import psycopg2

connection = psycopg2.connect(
        host="localhost",
        database="bank",
        user="postgres",
        password="password123",
    )
connection.set_session(autocommit=True)

class AccountRepository():

    def insert(self, account: Account):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM Address ORDER BY id DESC LIMIT 1;")
            result = cursor.fetchall()
            result_id = result[0][0] + 1
            cursor.execute("INSERT INTO Address(id,address,city,state,zipcode) VALUES (%s, %s, %s, %s, %s) RETURNING id", (result_id, account.address, account.city, account.state, account.zipcode))
            connection.commit()
            cursor.execute("INSERT INTO Customer(id,firstname,lastname,address_id,email_address) VALUES (%s, %s, %s, %s, %s) RETURNING id", (result_id, account.firstname, account.lastname, result_id, account.email))
            connection.commit()   
            cursor.execute("INSERT INTO Account(id,account_number,customer_id,curr_balance) VALUES (%s, %s, %s, %s) RETURNING id", (result_id, account.account_number, result_id, account.curr_balance))
            connection.commit()
        return {"Account": f"Account for {account.firstname} {account.lastname} has been added."}  

    def get_all(self):
        with connection.cursor() as cursor:
            cursor.execute('SELECT address, city, state, zipcode, firstname, lastname, customer.email_address, account.account_number, account.curr_balance FROM Account INNER JOIN Customer ON Account.customer_id = Customer.id INNER JOIN Address ON Customer.address_id = Address.id;')
            result = cursor.fetchall()
            response_dict = {}
            for i in range(len(result)):
                response = {"Address": result[i][0], "City": result[i][1], "State": result[i][2], "Zip Code": result[i][3], "First Name": result[i][4], "Last Name": result[i][5], "Email Address": result[i][6], "Account Number": result[i][7], "Current Balance": result[i][8]}
                response_dict[i] = response
        return response_dict
    
    def get(self, account_number):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT address, city, state, zipcode, firstname, lastname, customer.email_address, account.account_number, account.curr_balance FROM Account INNER JOIN Customer ON Account.customer_id = Customer.id INNER JOIN Address ON Customer.address_id = Address.id WHERE account_number = '{account_number}';")
            result = cursor.fetchall()
            results = result[0]
            response = {"Address": results[0], "City": results[1], "State": results[2], "Zip Code": results[3], "First Name": results[4], "Last Name": results[5], "Email Address": results[6], "Account Number": results[7], "Current Balance": results[8]}
        return response

    def update(self, account_number, balance: Balance):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT curr_balance FROM Account where account_number = '{account_number}';")
            result = cursor.fetchall()
            new_balance = float(result[0][0]) + balance.deposit
            cursor.execute(f"UPDATE Account SET curr_balance = '{new_balance}' WHERE account_number = '{account_number}';")
            connection.commit()
        return f"Account {account_number} has a new balance of {new_balance}."

    def delete(self, account_number):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT id FROM Account WHERE account_number = '{account_number}';")
            result = cursor.fetchall()
            result_id = result[0][0]
            cursor.execute(f"DELETE FROM Account WHERE id = '{result_id}';")
            cursor.execute(f"DELETE FROM Customer WHERE id = '{result_id}';")
            cursor.execute(f"DELETE FROM Address WHERE id = '{result_id}';")
            connection.commit()
        return f"Account {account_number} has been deleted."