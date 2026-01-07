class Bank_account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"Deposite Amount is ${amount} & New balance is ${self.balance}")
        
    def debit(self, deduct):
        if(self.balance >= deduct):
            self.balance -=  deduct
            print(f"Debit Amount ${deduct} $ Current balance is ${self.balance}")
        else:
            print("Insufficient balance!")

account = Bank_account("Cherry", 1000)

account.deposite(500)
account.debit(500)
account.debit(5000)




