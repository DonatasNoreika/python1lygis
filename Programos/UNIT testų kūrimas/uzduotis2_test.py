
import unittest
from uzduotis2 import StringTriukai

class TestUzduotis14_2(unittest.TestCase):

    def setUp(self):
        self.objektas = StringTriukai("Laba diena, Lietuva")

    def test_pirmas_zodis(self):
        self.assertEqual(self.objektas.pirmas_zodis(), "Laba")

    def test_paskutinis_zodis(self):
        self.assertEqual(self.objektas.paskutinis_zodis(), "Lietuva")

    def test_atbulai(self):
        self.assertEqual(self.objektas.atbulai(), "avuteiL ,aneid abaL")

    def test_nuo_galo(self):
        self.assertEqual(self.objektas.nuo_galo(), "Lietuva diena, Laba")

    def test_didziosiomis(self):
        self.assertEqual(self.objektas.didziosiomis(), "LABA DIENA, LIETUVA")

    def test_mazosiomis(self):
        self.assertEqual(self.objektas.mazosiomis(), "laba diena, lietuva")

    def test_info(self):
        lukestis = "Žodžių kiekis: 3, Skaičių kiekis: 0, Didžiųjų raidžių: 2, Mažųjų raidžių: 14"
        self.assertEqual(self.objektas.info(), lukestis)



