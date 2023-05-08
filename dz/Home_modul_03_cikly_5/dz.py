# Вывести на экран фигуры, заполненные звездочками.Диалог с пользователем реализовать при помощи меню.
print("Вывести на экран фигуры, заполненные звездочками")
print("Выберите задание: ")
choise=int(input("Ваш выбор: "))

if choise==2:
    for i in range(10):
        if ( i < 10 - 1) or ( i > 10 - 1):
            print(i*"*")

if choise==9:
    for i in reversed( range(10)):
        if ( i < 10 - 1) or ( i > 10 - 1):
            print(i*"*")
 
if choise==7:
    n=int(input("n= "))
    for i in range(n):
        print("*"*(i+1), ""*(n-2*i))
    for i in range(n,0,-1):
        print("*"*(i+1), ""*(n-2*i))


