# Показать на экран все простые числа в диапазоне,указанном пользователем.
a=int(input("a= "))
b=int(input("b= "))
if(a>b):
    print()
for i in range(a, b):
    simple = True
    for j in range(2, i-1):
        if i%j==0:
           simple = False
           break
    if(simple == True):
        print(i, end=" ")
   
       