# Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры.
counter = 0
for n in range(100, 999+1):
    a=n//100%10
    b=n//10%10
    c=n%10
    # count=0
    if a==b or b==c or b==c:
        print(n, end=" ")
        # counter=120
        counter+=1
print("количество чисел", counter)
# Подсказала счетчику сколько чисел

