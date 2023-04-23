number=int(input("number: "))
a=number%1000%100%10
b=number%1000%100//10
c=number%1000//100
d=number//1000
print(a)
print(b)
print(c)
print(d)
Number=a*1000+b*100+c*10+d
print(Number)
