# Написать программу конвертер валют....
# n-сумма
while True:
    n=int(input("n= "))
    # x=str(input("введите валюту"))  
    print("vubor")
    print("1:, доллар")
    print("2:, евро")
    choise=int(input("vas vubor"))
    if choise==1:
        res=n*36
        print("res:",res, "грн:" )
    elif choise==2:
        res=n*40
        print("res:",res, "грн:" )
    else:
        print("неправильный ввод")
    print("продолжить работу?")
    print("1:, да")
    print("2:, нет")
    choise=int(input("vas vubor"))
    if choise==1:
        print("ok")
    if choise==2:
        break

    

