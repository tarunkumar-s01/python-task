menu=['idli','dosa','biriyani']

def display():
    print('Display the menu')
    print('your menu :' ,*menu)

def add():
    print('Add your item')
    item=input()
    menu.append(item)
    print('added menu :',*menu)

def update():
    print('update my menu')
    print(*menu)
    item=input('enter your item to update : ')
    item1=input('enter your new item : ')

    if item in menu:
        
        x=menu.index(item)
        menu[x]=item1
        print('updated menu :',*menu)

    else:
        print('your item is not existing')
        update()
    

    
    
        
def delete():
    item=input('enter your item to delete : ')
    menu.remove(item)
    print('your new menu :',*menu)
    

def main():
    print('1.display \n 2.add \n 3.update \n 4.delete \n 5.exit')
    num=int(input('enter a number : '))
    if(num==1):
        display()
        main()
    elif(num==2):
        add()
        main()
    elif(num==3):
        update()
        main()
    elif(num==4):
        delete()
        main()
    elif(num==5):
        exit()
    else:
        print('please do enter correct option')
        main()
        
        
if __name__=='__main__':
    main()
    