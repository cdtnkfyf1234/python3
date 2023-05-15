# Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра
def func_count(x):
    res=0
    for i in range(len(str(x))):
        res+=1
    return res
print(func_count(3456890))    