# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум....
a=int(input("a= "))
b=int(input("b="))
s=0 
Min=0
Max=0
for i in range(a, b):
    s+=i
    for x in range(a, b+1):
        if x<Min:
            Min=x
        elif x>Max:
            Max=x
        elif x==7:
            print("Good bye!")
            break
print(s)
print(Max)
print(Min)

