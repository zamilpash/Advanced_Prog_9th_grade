import time 
import os
import random
import statistics as stats
from math import sin, cos, radians
"""

while True:
    print("Opciones del Juego")
    print("Piedra, Papel o Tijeras")

    opciones = ["Piedra", "Papel", "Tijeras"]
    eleccion = input("Elige una opcion: ") 




# Ejemplo de converion

angulo = 30
magnitud = 10
angulo_rad = radians(angulo)
comp_x = magnitud * cos(angulo_rad)
comp_y = magnitud * sin(angulo_rad)

print(f"Componente x del vector {comp_x}")
print(f"Componente y del vector {comp_y}")
"""

datos_sensor = [22.9, 22.0, 21, 23, 99, 77, 44, 32, 34, 54]
print("\n")
print(f"Media: {stats.mean(datos_sensor):.2f}")
print(f"Desviación estandar: {stats.stdev(datos_sensor):.4f}")
print("\n")