# Пользователь вводит с клавиатуры два числа. Нужно посчитать отдельно сумму четных, нечетных чисел.....c, d-считают количество четных и нечетных чисел.
a=int(input("a= "))
b=int(input("b= "))
even=0
odd=0
a0=a
sr=0
c=0
d=0
for i in range(a, b+1):
    if i%2!=0:
        even+=i 
        c+=1
    else: 
        odd+=i
        d+=1
    if i%9==0:
        print(i)
print(even)
print(odd)
sr1=even/c
sr2=odd/d
print(sr1)
print(sr2)
