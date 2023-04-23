a=int(input("a= "))
b=int(input("b= "))
a+=1
if a>b:
        a,b=b,a
while a<b:
    if a%2!=0:
        print(a, end=" ")
    a+=1
   