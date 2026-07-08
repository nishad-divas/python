class BankAccount:


    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    
    def Withdraw(self,other):
        if other <= self.balance:
            self.balance=self.balance-other
            print('withdwar successfully')
        else:
            print("gareeb gareeb")
        
        return self.balance
    

    def Deposite(self,other):
        self.balance=self.balance+other
        print('deposite successfully')
        return self.balance
    
    def BankFees(self):
        self.balance=self.baklance-self.balance*.05
    
    def Display(self):
        print("Account Number :",self.accountNumber)
        print("account owner name: ",self.name)
        print('account balance :',self.balance)

new_account=BankAccount(2178514584,"divas",2800)
new_account.Withdraw(700)
new_account.Deposite(1000)
new_account.Display()