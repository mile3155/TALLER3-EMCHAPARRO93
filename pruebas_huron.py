import unittest
from huron import Huron

class Pruebas_Huron(unittest.TestCase):
    def test_hacer_sonido(self):
        huron=Huron("Huron1", 2, 7, "Suecia",  95000)
        self.assertEqual(huron.hacer_sonido(),"¡Eek Eek!")

    def test_calcular_flete(self):
        huron=Huron("Huron1", 2, 7, "Suecia", 95000)
        self.assertEqual(huron.calcular_flete(),190000)

if  __name__=='__main__':
    unittest.main()