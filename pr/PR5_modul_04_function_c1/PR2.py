# Напишите функцию, которая принимает два числа в качестве параметра и отображает все нечетные числа
def funct_odd(a, b):
    for i in range(a,b):
        if i %2 !=0:
            print(i)

funct_odd(1,20)