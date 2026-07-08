class Atm():
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    
                        
    def menu(self):
        user_input=input("""" 
        Hi can i help you
        1.press 1 to create pin
        2.press 2 to change pin
        3.press 3 to check balance
        4.press 4 to withdraw
        5.Anything else to exit
        """)
        if int(user_input)>=6:
            print("You press wrong button ")
            print("Please press correct button")
            self.menu()

        if user_input=='1':
            #cerate pin
            self.create_pin()
        elif user_input=='2':
            #change pin
            self.change_pin()
        elif user_input=='3':
            #check balance
            self.check_balance()
        elif user_input=='4':
            #withdraw
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin=input('enter your pin')
        self.pin=user_pin

        user_balance=int(input('enter your balance'))
        self.balance=user_balance

        print('pin created successfully')
        self.menu()
    def change_pin(self):
        old_pin=input("enter your old pin")
        if old_pin==self.pin:
           new_pin=input("enter new pin")
           self.pin=new_pin
           print('pin change successfully')
           
        else:
            print("wrong pin")
        self.menu()


    def check_balance(self):
        user_pin=input('enter your pin')
        if user_pin==self.pin:
            print("your balance is ",self.balance)
        else:
            print("wrong pin and chl nikl")
        self.menu()


    def withdraw(self):
        user_pin=input('enter your pin')
        if user_pin==self.pin:
           amount=int(input('enter the amount'))
           if amount <= self.balance:
               self.balance=self.balance-amount
               print('withdraw successfully')
           else:
                print("gareeb gareeb")
        else:
            print('chor chor')
        self.menu()
obj=Atm()