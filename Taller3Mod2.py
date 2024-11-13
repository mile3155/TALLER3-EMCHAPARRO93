##Taller 3 Modulo 2 - Edna Milena Chaparro Perez

from huron import Huron
from boa import Boa
from animal_exotico import Animal_Exotico
from animal import Animal
from ianimal import iAnimal

huron_1=Huron("Huron1", 2, 7, "Suecia",  95000)
huron_2=Huron("Huron2", 1.2,8, "Suecia", 95000)

print(huron_1.obtener_nombre()+" tiene el sonido:"+str(Huron.hacer_sonido(Animal)))
print(huron_2.obtener_nombre()+" tiene el sonido:"+str(Huron.hacer_sonido(Animal)))

print("El flete para un "+huron_1.obtener_nombre()+" es $"+str(huron_1.calcular_flete()))
print("El flete para un "+huron_2.obtener_nombre()+" es $"+str(huron_2.calcular_flete()))

boa_1=Boa("Boa1", 10, 26, "Mexico", 50000)
boa_2=Boa("Boa2", 15, 30, "Argentina", 50000)

print(boa_1.obtener_nombre()+" tiene el sonido:"+str(Boa.hacer_sonido()))
print(boa_2.obtener_nombre()+" tiene el sonido:"+str(Boa.hacer_sonido()))

print(boa_1.ratones_comidos)
print(boa_1.comer_raton(1))
print(boa_1.comer_raton(2))
print(boa_1.ratones_comidos)
print(boa_1.obtener_kilos_comidos())






