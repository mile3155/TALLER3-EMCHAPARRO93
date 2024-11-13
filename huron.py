from animal_exotico import Animal_Exotico
from animal import Animal

class Huron(Animal_Exotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuesto):
        super().__init__(nombre, peso, edad, pais_origen, impuesto)
        self._pais_origen = pais_origen
        self._impuesto = impuesto

    def hacer_sonido(Animal):
        return "¡Eek Eek!"