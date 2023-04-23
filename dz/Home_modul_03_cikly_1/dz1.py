# Пользователь вводит с клавиатуры два числа (начало и конец диапазона)...
a=int(input("a= "))
b=int(input("b= "))
for i in range(a, b+1):
    if i%7==0:
        print(i, end=" ")