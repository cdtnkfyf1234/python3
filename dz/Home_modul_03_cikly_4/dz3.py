# Показать на экран таблицу умножения в диапазоне,указанном пользователем.
# a=int(input("Введите число: "))
# for i in range(1, 11):
#    print(a, "*", i, "=", a*i)
for i in range(1, 11):
        for n in range(3, 6, 2):
            print(i, "*", n, "=", i*n, end="   ")  