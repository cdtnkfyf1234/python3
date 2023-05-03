# Написать программу, которая проверяет пользователя на знание таблицы умножения. Программа выводит на
a=int(input("Введіть число: "))
b=int(input("Введіть число: "))
answer=int(input("Введіть відповідь: "))
fail=0
right=0
total=0
if answer!=a*b:
    fail+=1
    right=0
    print("Невірна відповідь")
else:
    right+=1
    total+=1
    print("Правільно")

print(total)
