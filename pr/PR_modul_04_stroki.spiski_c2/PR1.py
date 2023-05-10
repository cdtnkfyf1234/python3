<<<<<<< HEAD
# Есть некоторый текст. Реализуйте следующую функциональность
str=input("Введіть текст: ")
str=str.title()
print(str)
digit_count=0
punct_count=0
for i in str:
    if i.isdigit():
        digit_count+=1
        print(digit_count, sep="")
        print()
print(str.count("."))
print(str.count(","))
print(str.count("!"))
print(str.count("?"))

# for j in text:
#     if j== "." or "," or "!" or"?":
#         punct_count+=1
#         print(punct_count, end="")

=======
text=input("Введіть текст: ")

print(text.title())
print(text.count(","))
print(text.count("."))
print(text.count("!"))
print(text.count("?"))

for i in text:
    if i.isdigit():
        print(len(i), end="")
    

# print(text.count("!"))
>>>>>>> 9570e790ba41bbfa3f0bba5ac0559ef850ddf6e6
