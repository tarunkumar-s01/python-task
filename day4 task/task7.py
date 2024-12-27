lists=[]
for i in range(4):
    value=input("enter your  question : ").split()
    lists.append(value)

print("questions given by user giver below")
for i in range(len(lists)):
    print(i,'.',*lists[i])