from animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuesto:int):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuesto = impuesto

        self.kilos_comidos=0

    def calcular_flete(self):
        flete = (self._impuesto * self._peso)
        return flete