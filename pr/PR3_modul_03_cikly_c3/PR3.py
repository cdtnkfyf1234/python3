# пользователь вводит с кклавиатуры две границы диапазона и число.Если число попадает в диапазон....
a=int(input("a= "))
b=int(input("b= "))
i=int(input("i= "))
while not a<i<b:
    print("ввести число еще раз")
for i in range(a, b):
    print(a, "!",i,"!", b, end=" 3")
