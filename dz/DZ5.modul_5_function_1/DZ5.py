# Напишите функцию, которая возвращает произве-дение чисел в указанном диапазоне. Границы диапазона
def my_mult(a, b):
    if a>b:
        a, b=b, a

    res=1
    for i in range(a, b+1):
        res*=i
    return res


print(my_mult(int(input("a= ")), (int(input("b= ")))))

