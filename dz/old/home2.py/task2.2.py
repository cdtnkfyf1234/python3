a=int(input("input: "))
b=int(input("input: "))
c=int(input("input: "))
print("vybor")
print("1: max: " )
print("2: min: ")
print("3: arithmetic: ")
choice=int(input("vas vybor"))
if choice==1:
    if a>b and a>c:
        print("a")
    elif b>a and b>c:
        print("b") 
    elif c>a and c>b:
        print("c")  
if choice==2:
    if a<b and a<c:
        print("a") 
    elif b<a and b<c:
        print("b")  
    else:
        print("c")     

if choice==3:
    print((a+b+c)/3)
