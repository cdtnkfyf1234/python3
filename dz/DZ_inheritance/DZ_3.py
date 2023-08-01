class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return f"${self.dollars}.{self.cents}"

    def set_dollars(self, dollars):
        self.dollars = dollars

    def set_cents(self, cents):
        self.cents = cents

    def get_dollars(self):
        return self.dollars

    def get_cents(self):
        return self.cents

    def add(self, other):
        new_cents = self.cents + other.get_cents()
        new_dollars = self.dollars + other.get_dollars()
        if new_cents >= 100:
            new_cents -= 100
            new_dollars += 1
        return Money(new_dollars, new_cents)


money1 = Money(10, 50)
money2 = Money(5, 75)

print(money1.add(money2))


money1.set_dollars(20)
money1.set_cents(30)

print(money1)