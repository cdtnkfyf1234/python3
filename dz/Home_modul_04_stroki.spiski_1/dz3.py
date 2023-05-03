# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.
str=input("Введіть текст: ")
count=0
print(str.count("."))
print(str.count("!"))
print(str.count("?"))
count=str.count(".")+str.count("!")+str.count("?")
print(count)
