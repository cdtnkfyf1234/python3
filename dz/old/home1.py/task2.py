number1=int(input("input number: "))
number2=int(input("input number: "))
print("vybor")
print("1: sum: ")
print("2: difference: ")
print("3: arithmetic: ")
print("4: mult: ")
choice=int(input("vas vybor"))
if choice==1:
    print(number1+number2)
elif choice==2:
    print(number1-number2) 
elif choice==3:
    print((number1+number2)/2) 
elif choice==4: 
    print(number1*number2)        

