# Написать программу, которая выводит на экран шахматную доску с заданным размером клеточки
n=int(input("n="))
simvol1=input("*")
# print(n*simvol1)
simvol2=input("_")
for i in range(n):
    for j in range(n):
        for m in range(n):
            for k in range(n):
                if (i+k)%2==0:
                    print(simvol1, sep="", end="")