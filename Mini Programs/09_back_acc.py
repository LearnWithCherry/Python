
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient funds!")

    def save_account(self):
        with open('accounts.txt', 'a') as f:
            f.write(f"{self.name},{self.balance}\n")

acc = BankAccount(input("Enter account holder name: "))
while True:
    print("\n1. Deposit  2. Withdraw  3. Save & Exit")
    opt = input("Your choice: ")
    if opt == '1':
        acc.deposit(float(input("Amount: ")))
    elif opt == '2':
        acc.withdraw(float(input("Amount: ")))
    elif opt == '3':
        acc.save_account()
        break
    else:
        print("Invalid option!")
