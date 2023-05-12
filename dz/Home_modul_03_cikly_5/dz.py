# Вывести на экран фигуры, заполненные звездочками.Диалог с пользователем реализовать при помощи меню.
print("Вывести на экран фигуры, заполненные звездочками")
print("Выберите задание: ")
choise=int(input("Ваш выбор: "))

if choise==1:
    for i in range(10):
        print(" " * (i+1), "*" * (10-i))

if choise==2:
     n=10
     for i in range(n):
            print("*" * i, (n-1) * " ")

if choise==3:
    n=10
    for i in range(n):
        print(" " * i, (n-2 * i)* "*", " " * i, sep='')

if choise==4:
    n=10
    for i in range(9, -1, -1):
        print(" " * i, "*" * (10-2*i), " " * i)

if choise==5:
    for i in range(5):
        print(" " * i, "*" * (10-2*i), " " * i)
    for i in range(4, -1, -1):
         print(" " * i, "*" * (10-2*i), " " * i)

if choise==6:
    for i in range(5):
            print("*" * i, " " * (10-2*i), "*" * i)
    for i in range(5, 1, -1):
         print("*" * i, " " * (10-2*i), "*" * i)

if choise==7:
    n=10
    for i in range(n):
        print("*"*(i+1), ""*(n-2*i))
    for i in range(n,0,-1):
        print("*"*(i+1), ""*(n-2*i))

if choise==8:
    n=10
    for i in range(n):
        print(" " * (n-i), "*" * (1+i))
    for i in range(9, -1, -1):
        print(" " * (n-i), "*" * (1+i))

if choise==9:
    for i in range(10):
        print("*" * (10-i), " " * (i+1))

if choise==10:
    for i in (range(10)):
        print(" " * (10-i), "*" * (i+1))






   