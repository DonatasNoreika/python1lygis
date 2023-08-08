import unittest
from sakinys import Sakinys


class TestSakinys(unittest.TestCase):
    def setUp(self):
        self.objektas1 = Sakinys()
        self.objektas2 = Sakinys("Code Academy programavimo mokykla 101")

    def test_atbulai(self):
        self.assertEqual("101 alkykom omivamargorp ymedacA edoC", self.objektas2.atbulai())
        self.assertEqual("nohtyP fo neZ", self.objektas1.atbulai())

    def test_didziosiomis(self):
        self.assertEqual("CODE ACADEMY PROGRAMAVIMO MOKYKLA 101", self.objektas2.didziosiomis())

    def test_mazosiomis(self):
        self.assertEqual("code academy programavimo mokykla 101", self.objektas2.mazosiomis())

    def test_ieskoti(self):
        self.assertEqual(4, self.objektas2.ieskoti("a"))

    def test_pakeisti(self):
        self.assertEqual("Code Academy muzikos mokykla 101", self.objektas2.pakeisti("programavimo", "muzikos"))
        self.assertEqual("Code Academy programavimo universitetas 101", self.objektas2.pakeisti("mokykla", "universitetas"))

    def test_atspausdinti_zodi(self):
        self.assertEqual("programavimo", self.objektas2.atspausdinti_zodi(2))

    def test_info(self):
        self.assertEqual((5, 3, 2, 28), self.objektas2.info())
