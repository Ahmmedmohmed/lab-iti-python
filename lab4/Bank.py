class Account:
    def __init__(self, customer_name, total_money):
        self.customer_name = customer_name
        self.total_money = total_money
        self.transactions = []

    def deposit(self, amount , isendfrom=False):
        self.total_money += amount
        if isendfrom =false :
           self.transactions.append(f"Deposited: {amount}")
    return self.total_money

    def withdrawal(self, amount):
        if amount <= self.total_money:
            self.total_money -= amount
            self.transactions.append(f"Withdrew: {amount}")
        else:
            print("You do not have enough credit")
        return self.total_money

    def transfer(self, recipient_account, amount):
        if amount <= self.total_money:
            recipient_account.deposit(amount,True)
            self.total_money -= amount
            self.transactions.append(f"Transferred: {amount} to {recipient_account.customer_name}")
             recipient_accoun.transactions.append("send form {self.customer_name}")

            
        else:
            print("No money sent")

    def check_balance(self):
        return self.total_money

    def generate_statement(self):
        return f"Account Statement for {self.customer_name}:\n" + "\n".join(self.transactions)

    def earingmoany():

       return self. self.total_money * 0.10    


class Customer:
    def __init__(self, name, addres):
        self.name = name
        self.accounts = []
        self.account = []
        
        self.address = address

    def add_account(self, account):
        self.accounts.append(account)

    

class Bank:
    def __init__(self, name,):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
