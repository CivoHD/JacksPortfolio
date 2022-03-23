import random
import sys

class ATM():
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Numbe: {self.account_number}")
        print(f"Avilable balance: £{self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: £", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is £{self.balance}")
            print("Try with an lesser amount\n")
        else:
            self.balance = self.balance - self.amount
            print(f"£{amount} withdrawal was succesful!")
            print("Current account balance £", self.balance)
    
    def check_balance(self):
        print("Avavilable balance: £", self.balance)
        print()

    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)

        while True:
            try:
                option = int(input("Enter 1 | 2 | 3 | 4 | 5: "))
            except:
                print("Error: Enter 1 | 2 | 3 | 4 | 5: ")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(£): "))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(£): "))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: £{self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                    sys.exit()


print("*******WELCOME TO BANK OF BHUTAN*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account creted successfully.....\n")

atm = ATM(name, account_number)

while True:
    trans = input("Do you want to do any transaction? | Y | N |: ")
    if trans == "y".lower():
        atm.transaction()
    elif trans == "n".lower():
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong input command Enter 'y' or 'n'")

  
                    

