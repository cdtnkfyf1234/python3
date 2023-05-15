import random
print("Введіть розмір списку: ")
n=int(input("n= "))
m=[]
def print_summ(m):
    my_sum=0
    for i in m:
        my_sum+=i
    return my_sum
for i in range(n):
    m.append(random.randint(-10, 10))
print(m)

print(print_summ(m))

