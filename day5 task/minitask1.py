class area_circle:
    pi=3.14
    def __init__(self):
        self.radius=0
    
    def accept_method(self):
        self.radius=int(input('enter a number:'))
    
    def area(self):
        result=self.radius*self.radius*area_circle.pi
        print(result)
    
def main():
    user=area_circle()
    user.accept_method()
    user.area()   
         
        
main()
        