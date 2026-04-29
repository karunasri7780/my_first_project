"""s=input("enter a char:,")
if s==s[::-1]:
    print("its a palidrome function")
else:
    print("its not  a palidrome")"""
"""s=input("enter your character:,")
rev=""
for i in s:
    rev=i+rev

    if s==rev:
        print("its a palidrome function")
        break
    else:
        print("its not a palidrome")"""
"""n=int(input("enter the num"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n= n//10
    if rev==temp:
        print("its a palidrome")

    else:
        print("its not a palidrome ")"""
list=["python","mom", "dad"]
for i in list:
    if i==i[::-1]:
        print(i)