from perro import Perro

class Guarderia:
    def __init__(self, nombreguarderia: str, ubicacion: str):
        self.nombreguarderia = nombreguarderia
        self.ubicacion = ubicacion
        self.lista_hurones = []
        self.lista_boas = []
        self.__ratones_boa = 0

    def alimentar_boa(self,cantidad=1):
        self.__ratones_boa += cantidad