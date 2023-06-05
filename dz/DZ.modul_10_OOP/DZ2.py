# Реализуйте класс «Книга»
class Book:
    def __init__(self, name="", year="", publisher="", genre="", autor="", prise=""):
        self.name=name
        self.year=year
        self.publisher=publisher
        self.genre=genre
        self.autor=autor
        self.prise=prise
        
    def set_name(self, name):
        self.name = name
    def set_year(self, year):
        self.year = year
    def set_publisher(self, publisher):
        self.publisher = publisher
    def set_genre(self, genre):
        self.genre = genre
    def set_author(self, autor):
        self.autor = autor
    def set_price(self, prise):
        self.prise = prise

    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def get_publisher(self):
        return self.publisher
    def get_genre(self):
        return self.genre
    def get_autor(self):
        return self.autor
    def get_prise(self):
        return self.prise 

    def display_book_info(self):
        print(f"Book name {self.name},"
          f"\nYear {self.year},"
          f"\nPublisher {self.publisher},"
          f"\nGenre {self.genre},"
          f"\nAuthor {self.autor},"
          f"\nPrise {self.prise}")


    def input_book_info(self):
        self.set_name(input("Enter book name: "))
        self.set_year(input("Enter year of publication: "))
        self.set_publisher(input("Enter publisher: "))
        self.set_genre(input("Enter genre: "))
        self.set_author(input("Enter author: "))
        self.set_price(input("Enter price: "))

    def __str__(self):
        return f"Book name {self.name}, "\
          f"\nPublisher {self.publisher}, "\
          f"\nGenre {self.genre}, "\
          f"\nAuthor {self.autor}, "\
          f"\nPrise {self.prise}"


my_book = Book("Кафе на краю світу", "2005", "Книгарня_Є", "роман", "Джон П. Стрелекі", "166")
print(f"Book name {my_book.name},"
          f"\nYear {my_book.year},"
          f"\nPublisher {my_book.publisher},"
          f"\nGenre {my_book.genre},"
          f"\nAuthor {my_book.autor},"
          f"\nPrise {my_book.prise}")
print()
# my_book2 = Book()
# my_book2.input_book_info()
# my_book2.display_book_info()

print(my_book)
