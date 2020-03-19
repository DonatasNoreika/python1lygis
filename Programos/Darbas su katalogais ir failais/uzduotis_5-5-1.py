import pickle

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas


domas = Darbuotojas("Domas", "Rutkauskas", 900)
tomas = Darbuotojas("Tomas", "Rutkauskas", 1500)
ponas = Darbuotojas("Ponas", "Rutkauskas", 1200)

sarasas = []
sarasas.append(domas)
sarasas.append(tomas)
sarasas.append(ponas)

with open("darbuotojai.pkl", "wb") as pickle_out:
    pickle.dump(sarasas, pickle_out)


