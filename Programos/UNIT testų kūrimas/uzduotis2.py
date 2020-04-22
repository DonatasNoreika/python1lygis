class StringTriukai():
    def __init__(self, sakinys):
        self.sakinys = sakinys

    def pirmas_zodis(self):
        zodziai = self.sakinys.split()
        return zodziai[0]

    def paskutinis_zodis(self):
        zodziai = self.sakinys.split()
        return zodziai[-1]

    def atbulai(self):
        return self.sakinys[::-1]

    def nuo_galo(self):
        zodziai = self.sakinys.split()
        atvirksciai = zodziai[::-1]
        return " ".join(atvirksciai)

    def didziosiomis(self):
        return self.sakinys.upper()

    def mazosiomis(self):
        return self.sakinys.lower()

    def info(self):
        zodziai = len(self.sakinys.split())
        skaiciai = sum(c.isdigit() for c in self.sakinys)
        didziosios = sum(c.isupper() for c in self.sakinys)
        mazosios = sum(c.islower() for c in self.sakinys)
        return (f"Žodžių kiekis: {zodziai}, Skaičių kiekis: {skaiciai}, Didžiųjų raidžių: {didziosios}, Mažųjų raidžių: {mazosios}")


sakinys = StringTriukai("Laba diena, Lietuva")

print(sakinys.pirmas_zodis())
print(sakinys.paskutinis_zodis())
print(sakinys.atbulai())
print(sakinys.nuo_galo())
print(sakinys.didziosiomis())
print(sakinys.mazosiomis())
print(sakinys.info())
