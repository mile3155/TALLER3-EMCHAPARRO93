from abc import ABC, abstractmethod

class iAnimal(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):
        pass