class lists:
    def __init__(self):
        self.list1=[]
        self.max=0
        self.min=0
        self.addition=0
    
    def accept_method(self):
        self.list1=[]
        number=int(input('enter ur list size:'))
        
        for i in range(number):
            self.num=int(input())
            self.list1.append(self.num)
        
        print(self.list1)
        
    def maximum(self):
        self.max=0
        for i in self.list1:
            if i>self.max:
                self.max=i
        print(self.max)
    def minimum(self):
        self.min=self.list1[0]
        for i in self.list1:
            if i<self.min:
                self.min=i
        print(self.min)
    
    def add(self):
        self.addition=0
        for i in self.list1:
            self.addition+=i
        print(self.addition)
        
def main():
    result=lists()
    result.accept_method()
    result.maximum()
    result.minimum()
    result.add()

main()