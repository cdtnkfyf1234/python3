# Пользователь вводит с клавиатуры некоторый текст,после чего пользователь вводит список зарезервированных
text=input("Введіть текст: ")
words=input("Введіть список зарезервованих слів: ")
<<<<<<< HEAD
words=words.upper()
print(words.upper())
n=words
x=words.upper()
text1=text.replace("n", "x")
=======
words_upper=words.upper()
print(words_upper)
text1=text.replace(words, words_upper)
>>>>>>> 4890da4893b088b24b9c6937e5a1c0b179105afe

print(text1)
