# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот.
# def convert(x):
#      tf=(9/5)*x+32
# # return tf
# while True:
#  tc=input('t v celciax ')
#  if tc=='':
#      break 
#  else :
#      tc=int(tc)
#  tf=convert(tc)
#  print('t в цельсиях',tc,'т в фаренгейтах',tf)

# a = input().split("_")
# b = input().split("_")
# print(str( (int(a[0]) - 32) * (5 / 9)) )  
# print(str( (int(b[0]) * (9 / 5)) + 32) )

c = int(input("Введіть с: "))
def conv(c):
    return 9/5 * c +32
fahrenheit  = conv(c)
print(fahrenheit)

c = int (input ("Введіть с: ") )
f = c * 9/5 + 32
print (f)