# Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
str=input("Введить строку: ")
num=[]
letter=[]
count_num=0
count_letter=0
for x in str:
    if x.isdigit():
        num.append(int(x))
        count_num+=int(x)
    else:
        letter.append(x)
        count_letter=len(str)-count_num
print(num)
print(letter)
print(count_num)
print(count_letter)


