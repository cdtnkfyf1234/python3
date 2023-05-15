# Напишите функцию, которая проверяет является ли число палиндромом.
def polindrom(x):
    comp = ''.join(reversed(str(x)))
    return str(x) == str(comp)
 
 
num = 789987
if polindrom(num):
    print('Число ', num, '- полиндром.')
else:
    print('Число ', num, '- не полиндром.')