# Напишите функцию для нахождения минимума в списке целых. Список передаётся в качестве параметра.
def func_minimum(*arg):
    print(f"мінімальне число: {min(arg)}") 
func_minimum(0, 4, -1, 9, 88)