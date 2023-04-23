# Пользователь вводит с клавиатуры два числа (начало и конец диапазона)...
a=int(input("a= "))
b=int(input("b= "))
s=0
for i in range(a, b+1):
    print(i)
else:
    for  i in reversed(range(a, b+1)):
        print(i)
    else:
        for i in range(a, b+1):
            if i%7==0:
                print(i, "\n")
            if i%5==0:
                s=i+5
print("summa", s)
           