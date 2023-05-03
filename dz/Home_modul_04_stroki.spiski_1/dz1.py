# Пользователь вводит с клавиатуры строку. Проверьте является ли введенная строка палиндромом
str1=input("Введіть текст: ")
str2=str1.lower()
print(str2)
str3=str2.replace(" ", "")
print(str3)
str4=str3[::-1]
print("str4: ", str3[::-1])
if str3==str4:
    print("паліндром")
elif str3!=str4:
    print("не паліндром")