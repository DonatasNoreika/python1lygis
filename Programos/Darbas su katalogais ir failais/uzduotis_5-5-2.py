import pickle

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas

with open("darbuotojai.pkl", "rb") as pickle_in:
    naujas_sarasas = pickle.load(pickle_in)

vienas = naujas_sarasas[0]
du = naujas_sarasas[1]
trys = naujas_sarasas[2]

print(vienas.vardas, vienas.pavarde, vienas.atlyginimas)
print(du.vardas, du.pavarde, du.atlyginimas)
print(trys.vardas, trys.pavarde, trys.atlyginimas)