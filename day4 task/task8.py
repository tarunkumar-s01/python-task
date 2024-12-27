
val=list(map(int,input().split()))
min,max,add=val[0],0,0
for i in val:
    if i>max:max=i
    if i<min:min=i
    add+=i
print(min,max,add)