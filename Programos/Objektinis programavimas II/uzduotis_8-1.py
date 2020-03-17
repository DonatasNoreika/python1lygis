

class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self._informacija()

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

    def _informacija(self):
        print("Metai:", self.metai, "Modelis:", self.modelis, "Tipas:", self.kuro_tipas)

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_automonomiškai(self):
        print("Važiuoja autonomiškai")

toyota = Automobilis(2015, "Toyota Avensis", "Dyzelinas")
tesla = Elektromobilis(2018, "Telsla Model S", "Elektra")

toyota.vaziuoti()
toyota.stoveti()
toyota.pildyti_degalu()
tesla.pildyti_degalu()
tesla.vaziuoti_automonomiškai()