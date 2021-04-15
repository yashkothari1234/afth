class Atm:
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber = input("Enter card number")
        self.pinNumber = input("Enter pin number")
        
    def CashWithdrawal():
        deposit=int(input("Enter amount to deposit"))
        initialAmount = deposit
        amountToBeWithdrawn = int(input("Enter amount to be withdrawn"))
        balance = initialAmount-amountToBeWithdrawn
        print("Balance :")
        print(balance)

    CashWithdrawal()


       


    
 
    