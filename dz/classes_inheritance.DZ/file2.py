# from Book import Printer_edition
class  Printer_edition():
    pass
class Book( Printer_edition):
   
    def __init__(self, name, publisher, genre, autor, prise):
        self.name=name
        self.publisher=publisher
        self.genre=genre
        self.autor=autor
        self.prise=prise     
        super().__init__(name, publisher, genre, autor, prise)
   
my_book=Book("jjj", "ggg", "fff", "yyy", "fff")
print(my_book)