n=int(input("Скільки елементів у списку: "))
lst = []
for i in range(n):
    lst.append(int(input("number["+str(i)+"] = ")))
number = int(input("n= "))
count = lst.count(number)
print(count)