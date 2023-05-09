# В списке целых, заполненном случайными числами,определить минимальный и максимальный элементы,
s=input("Введіть список випадкових чисел: ")
s=lst=[]
sum1=0
sum2=0
i1=0
i2=0
i0=0
# print(max())
# print(min())
for i in lst: 
    if i<0:
        sum1+=i
        i1+=1
        print(sum1)
        print(i1)
    elif i==0:
        i0+=1
    else:
        sum2+=i
        i2+=1
    print(sum2)
    print(i2)