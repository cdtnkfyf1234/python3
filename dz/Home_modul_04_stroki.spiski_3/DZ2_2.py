# В списке целых, заполненном случайными числами,определить минимальный и максимальный элементы,
a=int(input("a= "))
b=int(input("b= "))
S1=S2=S3=0
Min=Max=0
for x in range(a, b):
    if x>0:
        S1+=1
    elif x<0:
        S2+=1
    else:
        S3+=1
print(S1)
print(S2)
print(S3)


for i in range(a, b+1):
    if i < Min:
        Min=i
    elif i>Max:
        Max=i
print(Min)
print(Max)