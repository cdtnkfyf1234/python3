# Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.
def func_minimum(*arg):
    print(f"мінімальне число: {min(arg)}") 
func_minimum(0, 4, -1, 9, 88)
