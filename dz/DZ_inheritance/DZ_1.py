# Создайте класс Device, который содержит информацию об устройстве.

class Device:
    pass

class CoffeeMachine:
    def __init__(self, r) -> None:
        self.__size = r
    def get_info(self):
        print('CoffeeMachine', self.__size)

class Blender(Device):
    def __init__(self) -> None:
        pass
    def get_info(self):
        # print('Blender', self.__size)
        print('Blender', self)

class MeatGrinder(Device):
    def __init__(self, size) -> None:
        Blender.__init__(self)
        CoffeeMachine.__init__(self, size)
    def get_info(self):
        Blender.get_info(self)
        CoffeeMachine.get_info(self)

MeatGrinder = MeatGrinder(1)
MeatGrinder.get_info()
print('MeatGrinder ', MeatGrinder)
print(MeatGrinder.mro())