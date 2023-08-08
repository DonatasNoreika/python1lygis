import unittest
from kmi_skaiciavimas import kmi


class TestSkaiciavimas(unittest.TestCase):
    def test_kmi(self):
        self.assertEqual(23.5, kmi(78, 1.82))
        self.assertEqual(20.5, kmi(50, 1.56))
        self.assertEqual(27.7, kmi(100, 1.90))
        with self.assertRaises(ValueError):
            kmi(20, 1.40)
        with self.assertRaises(ValueError):
            kmi(240, 1.40)
        with self.assertRaises(ValueError):
            kmi(80, 0.40)
        with self.assertRaises(ValueError):
            kmi(80, 3.40)
