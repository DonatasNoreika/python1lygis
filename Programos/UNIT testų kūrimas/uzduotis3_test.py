import unittest
from uzduotis3 import kmi
class TestSkaiciavimas(unittest.TestCase):
    def test_kmi(self):
        self.assertEqual(kmi(78, 1.82), 23.54788069073783)
        self.assertEqual(kmi(50, 1.56), 20.5456936226167)
        self.assertEqual(kmi(100, 1.90), 27.70083102493075)
        with self.assertRaises(ValueError):
            kmi(20, 1.40)
        with self.assertRaises(ValueError):
            kmi(240, 1.40)
        with self.assertRaises(ValueError):
            kmi(80, 0.40)
        with self.assertRaises(ValueError):
            kmi(80, 3.40)