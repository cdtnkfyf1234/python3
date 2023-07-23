# Написать игру «Быки и коровы». 
from  random import choice              
z = '0123456789'                        
x = choice(z)                           
print(x)                      
for i in range(3):                     
    x += choice(z)                    
print(x)
x = choice(z[1:10])                         
for i in range(3):                          
    z = ''.join(z.split(x[i]))              
    x += choice(z)                          
    print(z)
print(x)
print('Загадано число:', x)
y = input("Введите четырёхзначное число: ") 
b = 0; c = 0                                
for i in range(4):                      
    if x[i] == y[i]:                        
        b += 1                           
    elif y[i] in x:                         
        c += 1                              
print(y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы')