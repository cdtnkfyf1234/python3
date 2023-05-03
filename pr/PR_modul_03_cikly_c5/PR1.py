# Пользователь вводит число. Определить количество цифр в этом числе, посчитать их сумму
n=int(input("n= "))
count=0
sum=0
sr=0

print("1: Определить количество цифр")
print("2: Посчитать сумму цифр")
print("3: Вывести среднеарифметическое")
print("4: Посчитать количество нулей")
choise= int(input("Ваш выбор"))
if choise==1:
    # while n>0:
   d=len(str(n))
   print(d)

elif choise==2:
    for i in range((n+1)%10):
        
        n//10
        sum+=int(i)
        # n//10
    print("sum: ", sum)

if choise==3:
    for i in range((n+1)%10):
        n//10
    sum+=int(i)
    d=len(str(n))    
    # for j in range(n):
    sr=sum/d
print(sr)

if choise==4:
    digit=len(str(n))
    # for i in range(n):
    #     if i%10==0:
    #         i//10
    #         count+=1
print(str(n).count("0"))
