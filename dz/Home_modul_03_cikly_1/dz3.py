# Пользователь вводит с клавиатуры два числа (начало и конец диапазона)....
a=int(input("a= "))
b=int(input("b= "))
for i in range(a, b+1):
    if i%3!=0 and i%5!=0:
        print(i)
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    else:
        if i%3==0:
            print("Fizz")
        if i%5==0:
            print("Buzz")

