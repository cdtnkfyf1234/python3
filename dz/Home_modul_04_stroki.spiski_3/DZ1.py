# Два списка целых заполняются случайными числами.Необходимо....
lst1=input("Введіть елементи першого списку: ")
lst2=input("Введіть елементи другого списку: ")
lst3=lst1+lst2
print([lst3])
Min1=Min2=0

# temp=[]
# [temp.append(x) for x in lst3 if x not in temp]
# print(temp)

lst3_set=set(lst3)
print(list(lst3_set))

c=[]
for i in lst1:
    if i in lst2 and i not in c:
        c.append(i)
        print(c)

new_lst=[i for i in lst1 if i not in lst2] + [i for i in lst2 if i not in lst1]
print(new_lst)

print(max(lst1))
print(max(lst2))
for x in lst1:
    if x < Min1:
       Min1=x
for x in lst2:
    if x < Min2:
       Min2=x
print(Min1)
print(Min2)
# Чомусь не показує мінімум

# a = sorted(lst1)
# b = sorted(lst2)
# lst4 = [a[0], a[-1], b[0], b[-1]]
# print(lst4)