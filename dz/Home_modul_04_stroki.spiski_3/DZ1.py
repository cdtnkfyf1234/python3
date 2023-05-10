# Два списка целых заполняются случайными числами.Необходимо....
lst1=input("Введіть елементи першого списку: ")
lst2=input("Введіть елементи другого списку: ")
lst3=lst1+lst2
print([lst3])

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
print(min(lst1))
print(min(lst2))

a = sorted(lst1)
b = sorted(lst2)
lst4 = [a[0], a[-1], b[0], b[-1]]
print(lst4)