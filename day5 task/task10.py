class menu:
    def __init__(self):
        self.menu=['idli','dosa','biriyani']
        update=[]
    
    
    def display(self):
        print('Display the menu')
        print('your menu :' ,*self.menu)
        
    def add(self):
        print('Add your item')
        self.item=input()
        self.menu.append(self.item)
        self.menu=self.menu
        print('added menu :',*self.menu)
        
    def update(self):
        print('update my menu')
        print(*self.menu)
        self.item=input('enter your item to update : ')
        self.item1=input('enter your new item : ')

        if self.item in self.menu:
            x=self.menu.index(self.item)
            self.menu[x]=self.item1
            print('updated menu :',*self.menu)

        else:
            print('your item is not existing')
            
            
    def delete(self):
        self.item=input('enter your item to delete : ')
        self.menu.remove(self.item)
        print('your new menu :',*self.menu)
    
    

def main():
    value=menu()
    print('1.display \n 2.add \n 3.update \n 4.delete \n 5.exit')
    num=int(input('enter a number : '))
    if(num==1):
        value.display()
        main()
    elif(num==2):
        value.add()
        main()
    elif(num==3):
        value.update()
        
    elif(num==4):
        value.delete()
        main()
    elif(num==5):
        exit()
    else:
        print('please do enter correct option')
        main()
        
        
if __name__=='__main__':
    main()