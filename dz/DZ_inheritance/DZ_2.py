class Ship():
    def __init__(self, make, year, draft, loading):
        self.make=make
        self.year=year
        self.draft=draft
        self.loading=loading
    def desciption_name(self):
        desc=str(self.year) + " " + self.make + " " + self.draft
        return desc.title()
# class Sail():
#     def __init__(self) -> None:
#         pass
        
class Frigate(Ship):
    def __init__(self, make, year, draft, loading, sail):
        super().__init__(make, year, draft, loading)
        self.sail = sail
    def description_sail(self):
        print("This Frigate has a big sail")

class Destroyer(Ship):
    def __init__(self, make, year, draft, loading, engine):
        super().__init__(make, year, draft, loading)
        self.engine=engine
    def desciption_name(self):
        return super().desciption_name()
    
class Cruiser(Ship):
    def __init__(self, make, year, draft, loading, weapons):
        super().__init__(make, year, draft, loading)
        self.weapons=weapons
    def desciption_name(self):
        return super().desciption_name()


Dream = Frigate("sailboat", "2017", "3000", "40000", "800*600")
print(Dream.desciption_name)