# Вывести на экран фигуры, заполненные звездочками.Диалог с пользователем реализовать при помощи меню.
print("Вывести на экран фигуры, заполненные звездочками")
print("Выберите задание: ")
<<<<<<< HEAD
choise=int(input("Ваш выбор: "))

=======
choise=int(input("Ваш выбор"))
n = 10
>>>>>>> 4890da4893b088b24b9c6937e5a1c0b179105afe
if choise==2:
    for i in range(n):
        # if ( i < 10 - 1) or ( i > 10 - 1):
            print(" "*i, (n-2*i)*"*"," "*i,sep='')

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


