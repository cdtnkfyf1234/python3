#  журнал, книга, друковане видання, підручник
class Printer_edition:
    def __init__(self, name="", publisher="", genre="", autor="", prise=""):
        self.name=name
        # self.year=year
        self.publisher=publisher
        self.genre=genre
        self.autor=autor
        self.prise=prise


    def set_name(self, name):
        self.name = name
    # def set_year(self, year):
    #     self.year = year
    def set_publisher(self, publisher):
        self.publisher = publisher
    def set_genre(self, genre):
        self.genre = genre
    def set_author(self, autor):
        self.autor = autor
    def set_price(self, prise):
        self.prise = prise


    def __str__(self):
            return f"Book name {self.name}, "\
          f"\nPublisher {self.publisher}, "\
          f"\nGenre {self.genre}, "\
          f"\nAuthor {self.autor}, "\
          f"\nPrise {self.prise}"


my_book=Printer_edition("jjj", "nnn", "hhh", "nnnn", "hhh")
print(my_book)
