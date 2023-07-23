# Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
GCD = gcd(a, b)
print("НОД: ")
print(GCD)