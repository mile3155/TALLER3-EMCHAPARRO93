from animal_exotico import Animal_Exotico
from animal import Animal

class Boa(Animal_Exotico):
    peso_raton:float = 1.5

    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuesto:float):
        super().__init__(nombre, peso, edad, pais_origen, impuesto)
        self.__ratones_comidos = 0

    @staticmethod
    def hacer_sonido():
        return "¡Tsss!"

    def comer_raton(self, cantidad=1) -> None:
        self.__ratones_comidos += cantidad
        try:
            self.__ratones_comidos<10
            print(f"Boa ha comido:{self.__ratones_comidos}ratones")
        except ValueError as e:
            print(f"Demasiados Ratones!")
        self.comer(self.peso_raton*cantidad)

    @property
    def ratones_comidos(self) -> int:
        return self.__ratones_comidos

