class Printer_edition:
    pass
class Magazine(Printer_edition):
    def set_name(self,name1):
        name1=="kkkk"
        self.set_name1=name1
    def set_publisher(self, publisher1): 
        publisher1=="oooo"
        self.set_publisher1=publisher1
    def showinfo(self):
        print()
magazine=Magazine("iii", "jjj", "ggg", "yyy", "hhh")
magazine.showinfo()
print(magazine)