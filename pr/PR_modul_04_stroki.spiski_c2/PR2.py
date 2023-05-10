<<<<<<< HEAD
n=int(input("count of number: "))
=======
n=int(input("Скільки елементів у списку: "))
>>>>>>> 9570e790ba41bbfa3f0bba5ac0559ef850ddf6e6
lst = []
for i in range(n):
    lst.append(int(input("number["+str(i)+"] = ")))
number = int(input("n= "))
count = lst.count(number)
print(count)