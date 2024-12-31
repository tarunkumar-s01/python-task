class bank:
    def __init__(self):
        self.name=""
        self.amount=0
        self.address=''
        self.accountno=0
        
    def createaccount(self):
        self.name=input('enter name:')
        self.amount=int(input('enter amount:'))
        self.address=input('enter address:')
        self.accountno=input('enter accountno:')
        
    def display(self):
        print("--------your account details---------")
        print("name : ",self.name)
        print("amount : ",self.amount)
        print("address : ",self.address)
        print("balance : ",self.accountno)
       
    
    def deposit(self,add):
        self.add=add
        self.amount+=self.add
        print('deposit :',self.amount)
        
    def withdraw(self,sub):
        self.sub=sub
        self.amount-=self.sub
        print('withdraw :',self.amount)
        
    def balance(self):
        print('balance amount : ',self.amount)
        
def main():
    user=bank()
    print('create first account : ')
    user.createaccount()
    user.display()
    user.deposit(500)
    user.withdraw(1000)
    user.balance()
    
main()
