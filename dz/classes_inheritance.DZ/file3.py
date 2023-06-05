class Book():
    pass
class Textbook(Book):
    super().__init__()
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

my_textbook=Textbook("hhh", "uuu", "rrr", "jjj", "hhh")
print(my_textbook)