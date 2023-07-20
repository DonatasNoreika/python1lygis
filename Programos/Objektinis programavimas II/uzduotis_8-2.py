import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo
        self.dirba_nuo_datetime = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d")

    def _kiek_nudirbo_dienu(self):
        skirtumas = datetime.datetime.today() - self.dirba_nuo_datetime
        return skirtumas.days

    def paskaiciuoti_atlyginima(self):
        return self._kiek_nudirbo_dienu() * 8 * self.valandos_ikainis


class NormalusDarbuotojas(Darbuotojas):
    def _kiek_nudirbo_dienu(self):
        return round(super()._kiek_nudirbo_dienu() / 7 * 5)


darbuotojas1 = Darbuotojas("Tomas", 20, "2000-12-12")
darbuotojas2 = NormalusDarbuotojas("Domas", 20, "2000-12-12")
print(darbuotojas1.paskaiciuoti_atlyginima())
print(darbuotojas2.paskaiciuoti_atlyginima())
