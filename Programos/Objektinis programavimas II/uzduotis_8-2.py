import datetime

class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo


    def _kiek_dirba_valandu(self):
        nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y, %m, %d, %H, %M, %S")
        dabar = datetime.datetime.today()
        skirtumas = dabar - nuo_kada_dirba
        return skirtumas.days * 8

    def paskaiciuoti_atlyginima(self):
        atlyginimas = self.valandos_ikainis * self._kiek_dirba_valandu()
        print (self.vardas + " uždirbo " + str(atlyginimas))

class NormalusDarbuotojas(Darbuotojas):
    def _kiek_dirba_valandu(self):
        nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y, %m, %d, %H, %M, %S")
        dabar = datetime.datetime.today()
        skirtumas = dabar - nuo_kada_dirba
        return (skirtumas.days * 8) / 7 * 5


donatas = Darbuotojas("Donatas", 10, "2019, 03, 12, 12, 00, 00")
donatas_normalus = NormalusDarbuotojas("Donatas", 10, "2019, 03, 12, 12, 00, 00")
donatas.paskaiciuoti_atlyginima()
donatas_normalus.paskaiciuoti_atlyginima()
