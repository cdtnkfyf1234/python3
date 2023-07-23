# К уже реализованному классу «Дробь» добавьте ста-тический метод, который при вызове возвращает коли-чество созданных объектов класса «Дробь»
class Drob(object):
    """ Дробь вида a/b"""
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
        self.normalize()

    @staticmethod
    def nod(x, y):      
        res = x % y
        while res > 1:
            x, y = y, res
            res = x % y
        return y

    def normalize(self):
        """ Приводит дробь вида 4/6 к 2/3"""
        k = Drob.nod(self.a, self.b)      
        self.a //= k
        self.b //= k

    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

d1 = Drob(4, 6)
print(d1)              

z = Drob.nod(123, 21)   
print(z)    