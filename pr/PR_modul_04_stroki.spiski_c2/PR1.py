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