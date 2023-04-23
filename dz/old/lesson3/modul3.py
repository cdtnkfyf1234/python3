number=int(input("input number"))
a=number//1000
b=number%1000//100
c=number%1000%100//10
d=number%1000%100%10
print(a)
print(b)
print(c)
print(d)
mult=a*b*c*d
print(mult)