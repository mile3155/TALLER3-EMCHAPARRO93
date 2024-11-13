import unittest
from boa import Boa

class Pruebas_Boa(unittest.TestCase):
    def test_hacer_sonido(self):
        boa=Boa("Boa2", 15, 30, "Argentina", 50000)
        self.assertEqual(boa.hacer_sonido(),"¡Tsss!")

    def test_calcular_flete(self):
        boa=Boa("Boa2", 15, 30, "Argentina", 50000)
        self.assertEqual(boa.calcular_flete(),750000)

    def test_comer_raton(self):
        boa = Boa("Boa2", 15, 30, "Argentina", 50000)
        boa.comer_raton(15)
        self.assertEqual(boa.ratones_comidos,15)

if  __name__=='__main__':
    unittest.main()