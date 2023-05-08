# Пользователь вводит с клавиатуры некоторый текст,после чего пользователь вводит список зарезервированных
text=input("Введіть текст: ")
words=input("Введіть список зарезервованих слів: ")
words_upper=words.upper()
print(words_upper)
text1=text.replace(words, words_upper)

print(text1)
