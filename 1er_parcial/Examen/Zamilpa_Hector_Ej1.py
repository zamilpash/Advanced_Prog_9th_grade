# Análisis de sensores
"""
Simular la lectura de 10 valores de un sensor de temperatura usando una lista. Convierte los valores de grados Celsius a Fahrenheit utilizando una función modular. 
Identifica cuáles lecturas están fuera del rango permitido (entre 20°C y 80°C). Usa estructuras condicionales y comprension de listas
"""

import random

# Función para convertir de °C a °F
# Aplico directamente la formula para conversion.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Simular 10 lecturas de temperatura entre 20°C y 80°C
# Primero creo una lista vacia, después creo un for que se repita 10 veces.
# Se crea una variable donde se guardaran valores que vaya creando random.
# Se agregan las medidas generadas a la lista vacía.

temperaturas = []
for _ in range(9):
    lecturas_celsius = random.uniform(10, 50)
    temperaturas.append(lecturas_celsius)

# Convertir las lecturas a Fahrenheit
# Primero creo una lista vacia, donde se guardarán los valores convertidos en le funcion celsius_a_fahrenheit.
# Se crea una variable donde se guardaran valores convertidos.
# Se agregan las medidas generadas a la lista vacía.

lecturas_fahrenheit = []
for temp in temperaturas:
    temp_convertidos = celsius_a_fahrenheit(temp)
    lecturas_fahrenheit.append(temp_convertidos)
"""  
Se coloca una variable antes del for cuando usamos una comprensión de listas (o list comprehension),
que es una forma compacta de crear listas nuevas a partir de otras.
Esa "variable antes del for" es el valor que se agregará a la nueva lista. 
No es una variable especial, simplemente representa qué quieres incluir en la lista.
"""

# Le doy formanto a lo que se mostrará
# Mostrar las mediciones generadas.
print("\nTemperaturas en Celsius |    Temperaturas Fahrenheit")
print("-" * 30)

# Realizo un for iterando las dos listas, para mostrar sus datos uno por uno, 
# usando la clase zip que itera hasta el ultimo datos por si son difentes tamaños.
for c, f in zip(temperaturas, lecturas_fahrenheit):
    print(f"    {c:.2f} °C      =     {f:.2f} °F")


#  Detectar lecturas fuera del rango permitido (20°C a 40°C)
for temp in temperaturas:
    if temp < 20:
        print(f"\nTemperatura debajo del rango: {temp:.2f}")
    
    elif temp > 40:
        print(f"\nTemperatura demasiado alta: {temp:.2f}")

    else:
       print(f"\nTemperatura dentro del rango permitido: {temp:.2f} °C")
