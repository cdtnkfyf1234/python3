# Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
def func_simple(number):
    n=number
    counter=0
    for i in range(1, n+1):
        if n%i==0:
            counter+=1
        return "просте число"
        if counter==2:
            "не просте число"
        else:
            "не просте число"
func_simple(1, 2, 3, 5, 9, 0)
