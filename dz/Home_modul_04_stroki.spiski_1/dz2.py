# Пользователь вводит с клавиатуры некоторый текст,после чего пользователь вводит список зарезервированных
text=input("Введіть текст: ")
words=input("Введіть список зарезервованих слів: ")
words=words.upper()
print(words.upper())
text1=text.replace("words", "words.upper()")

print(text1)
