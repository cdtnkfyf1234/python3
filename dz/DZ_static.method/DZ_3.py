# Создайте класс для перевода из метрической системы в английскую и наоборот
mydict={
    'mile':'1609 m',
    'yard':'0.9144 m',
    'foot':'30.48 cm',
    'inch':'2.54 m',
    'km':'1000 m',
    'm':'1 m',
    'cm':'0.01 m',
    'mm':'0.001 m',
}
 
def converter(arr):
    val=0
    v1=mydict[arr[1]].split(" ")
    v2=mydict[arr[3]].split(" ")
    if v1[1]!="m":
        v2=mydict[v1[1]]
        val=float(v2.split(" ")[0])
        val=val*float(v1[0])
    else:
        val=float(v1[0])/float(v2[0])
 
    val=val*float(arr[0])
    print('Результат равен '+str(val)+' '+arr[3])
    return 0
 
 
test=["5.3 km in cm","22.39 foot in m","10200 mm in yard","15.5 mile in km"]
 
for i in range(len(test)):
    converter(test[i].split(" "))