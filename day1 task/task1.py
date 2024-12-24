a=int(input('enter a value : '))
b=int(input('enter b value : '))

a,b=b,a
print(f'value of a is {a}, value of b is {b}')

a1=int(input('enter a value : '))
b1=int(input('enter b value : '))

temp=a1
a1=b1
b1=temp

print(f'value of a1 is {a1}, value of b1 is {b1}')

amount=int(input('enter amount value : '))
tip=int(input('enter tip value : '))
val=int(input('how many people'))

calculate= tip/100
total = amount + (amount*calculate)
ans = total/val
print(ans)

val = input('enter value : ')
print(val,type(val))

