# Пользователь вводит с клавиатуры числа. Если число больше нуля, то нужно вывести надпись.....
n=int(input("n= "))
if n>0 and n!=7:
    print("Number is positive")
if n<0:
    print("Number is negative")
elif n==0:
    print("Number is equal to zero")
elif n==7:
    print("Good bye!")