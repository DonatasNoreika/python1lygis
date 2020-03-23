
from operator import attrgetter

# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų __repr__ metodas, kuris atvaizduotų vardą ir amžių

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"({self.vardas}, {self.amzius})")

# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# Įdėti sukurtus Zmogus objektus į naują sąrašą

z1 = Zmogus("Domas", 22)
z2 = Zmogus("Antanas", 30)
z3 = Zmogus("Jonas", 45)

sarasas = [z1, z2, z3]

# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą

# surusiuotas = sorted(sarasas, key=lambda e: e.vardas)
# print(surusiuotas)

# arba

surusiuotas = sorted(sarasas, key=attrgetter("vardas"))
print(surusiuotas)

# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą atbulai

surusiuotas = sorted(sarasas, key=attrgetter("vardas"), reverse=True)
print(surusiuotas)

# Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių

surusiuotas = sorted(sarasas, key=attrgetter("amzius"))
print(surusiuotas)

# Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių atbulai

surusiuotas = sorted(sarasas, key=attrgetter("amzius"), reverse=True)
print(surusiuotas)
