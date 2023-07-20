class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma} (siuntėjas - {self.siuntejas}, info - {self.info})"


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta, info):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta = isigyta
        self.info = info

    def __str__(self):
        return f"Išlaidos: {self.suma} (atsiskaitymo būdas - {self.atsiskaitymo_budas}, įsigyta - {self.isigyta}, info - {self.info})"


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def ivesti_pajamas(self):
        suma = float(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)

    def ivesti_islaidas(self):
        suma = float(input("Suma: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta = input("Įsigyta prekė/paslauga: ")
        info = input("Papildoma informacija: ")
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta, info)
        self.zurnalas.append(irasas)

    def ataskaita(self):
        print("-----------------")
        for irasas in self.zurnalas:
            print(irasas)

    def balansas(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        print("Balansas", suma)


biudzetas = Biudzetas()

while True:
    veiksmas = int(input("""
    1 - įvesti pajamas
    2 - įvesti išlaidas
    3 - balansas
    4 - ataskaita
    5 - išeiti
    """))
    match veiksmas:
        case 1:
            biudzetas.ivesti_pajamas()
        case 2:
            biudzetas.ivesti_islaidas()
        case 3:
            biudzetas.balansas()
        case 4:
            biudzetas.ataskaita()
        case 5:
            break
