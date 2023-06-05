# Реализуйте класс «Автомобиль».

class Automobile:
    
    def __init__(self, model, year, manufacturer, engine_size, color, prise):  
        self.__model=model
        self.year=year
        self.manufacturer=manufacturer
        self.engine_size=engine_size
        self.color=color
        self.prise=prise

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        # if self.__model == "BMW":
        return self.__model
    def get_year(self):
        return self.year
    def get_manufacturer(self):
        return self.manufacturer
    def get_engine_size(self):
        return self.engine_size
    def get_color(self):
        return self.color
    def get_prise(self):
        return self.prise

automobile=Automobile("BMW", "2000", "Germany", "2979", "white", "2000000")

year = 2021
if year == 2020:
      model = "BMW"
else:
      model = "DDD"

automobile.set_model(model)
print(f"Модель машини {automobile.get_model()}," 
      f"\nрік випуску {automobile.year},"
      f"\nвиробник {automobile.manufacturer},"
      f"\nоб'єм двигуна {automobile.engine_size},"
      f"\nколір {automobile.color},"
      f"\nціна {automobile.prise}")

my_new_automobile=Automobile("audi", "2002", "Germany", "2730", "black", "1800000")
print(f"Модель машини {my_new_automobile.get_model()}," 
      f"\nрік випуску {my_new_automobile.year},"
      f"\nвиробник {my_new_automobile.manufacturer},"
      f"\nоб'єм двигуна {my_new_automobile.engine_size},"
      f"\nколір {my_new_automobile.color},"
      f"\nціна {my_new_automobile.prise}")

def change_model(self, new_model):
        self.model = new_model
def change_year(self, new_year):
        self.year = new_year
def change_manufacturer(self, new_manufacturer):
        self.manufacturer = new_manufacturer
def change_engine(self, new_engine):
        self.engine = new_engine
def change_color(self, new_color):
        self.color = new_color
def change_price(self, new_price):
        self.price = new_price








    


