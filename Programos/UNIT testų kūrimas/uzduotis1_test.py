import unittest
import datetime
from funkcijos import (skaiciu_suma,
                       saraso_suma,
                       didziausias_skaicius,
                       stringas_atbulai,
                       info_apie_sakini,
                       unikalus_sarasas,
                       ar_pirminis,
                       isrikiuoti_nuo_galo,
                       ar_keliamieji,
                       patikrinti_data)


class TestFunkcijos(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(45, skaiciu_suma(45, 5, -5))
        self.assertEqual(62, skaiciu_suma(60, 2, 0))
        self.assertEqual(50, skaiciu_suma(3, 3, 44))

    def test_saraso_suma(self):
        self.assertEqual(95, saraso_suma([4, 5, 78, 8]))
        self.assertEqual(-68, saraso_suma([-20, -50, 2]))
        self.assertEqual(202.70000000000005, saraso_suma([-1000, 2.5, 1200.200]))

    def test_didziausias_skaicius(self):
        self.assertEqual(78, didziausias_skaicius(5, 6, 78))
        self.assertEqual(55, didziausias_skaicius(-300, 5, 55))
        self.assertEqual(45.7, didziausias_skaicius(45.6, 45.7, 45.22))

    def test_stringas_atbulai(self):
        self.assertEqual("satanoD", stringas_atbulai("Donatas"))

    def test_info_apie_sakini(self):
        self.assertEqual((5, 2, 28, 3), info_apie_sakini("Code Academy programavimo mokykla 101"))

    def test_unikalus_sarasas(self):
        self.assertCountEqual([4, 5, 'Labas', 6, True, 10], unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))

    def test_ar_pirminis(self):
        self.assertTrue(ar_pirminis(7))
        self.assertFalse(ar_pirminis(8))
        self.assertTrue(ar_pirminis(113))

    def test_isrikiuoti_nuo_galo(self):
        self.assertEqual("keturi trys du Vienas", isrikiuoti_nuo_galo("Vienas du trys keturi"))

    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2000))
        self.assertTrue(ar_keliamieji(1996))
        self.assertFalse(ar_keliamieji(1994))
        self.assertFalse(ar_keliamieji(2100))

    def test_patikrinti_data(self):
        lukestis = (23, 283, 1231, 8619, 206877, 12412608, 744756468)
        rezultatas = patikrinti_data(sukaktis="2000-01-01 12:12:12", dabar=datetime.datetime(2023, 8, 8, 9, 0, 0))
        self.assertEqual(lukestis, rezultatas)

        lukestis2 = (32, 389, 1691, 11837, 284109, 17046528, 1022791668)
        rezultatas2 = patikrinti_data(sukaktis="1991-03-11 12:12:12", dabar=datetime.datetime(2023, 8, 8, 9, 0, 0))
        self.assertEqual(lukestis2, rezultatas2)
