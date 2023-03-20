import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        """
        Darbuotojo objektas
        :param vardas: darbuotojo vardas
        :param valandos_ikainis: darbo valandos įkainis
        :param dirba_nuo: datą įvesti formatu: YYYY-MM-DD
        """
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d")

    def _kiek_dienu(self):
        skirtumas = datetime.datetime.today() - self.dirba_nuo
        return skirtumas.days

    def paskaiciuoti_atlyginima(self):
        return self._kiek_dienu() * 8 * self.valandos_ikainis


class NormalusDarbuotojas(Darbuotojas):
    def _kiek_dienu(self):
        return super()._kiek_dienu() // 7 * 5


darbuotojas1 = Darbuotojas("Jonas", 20, "2000-01-01")
darbuotojas2 = NormalusDarbuotojas("Petras", 20, "2000-01-01")
print(darbuotojas1.paskaiciuoti_atlyginima())
print(darbuotojas2.paskaiciuoti_atlyginima())
