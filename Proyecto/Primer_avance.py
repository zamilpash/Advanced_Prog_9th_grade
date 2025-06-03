# Programa que genere datos de 5 sensores con la librería Random
# Y que sean graficados.

import random
import matplotlib.pyplot as plt


# Simular 30 lecturas de temperatura entre 20°C y 40°C
# Primero creo una lista vacia para cada sensor, después creo un for que se repita 30 veces.
# Se crea una variable donde se guardaran valores que vaya creando random.
# Se agregan las medidas generadas a la lista vacía para posteriormente usarse esos datos para graficarse.

while True:

    print("Sistemas de medidición de una Célula de manufactura de llenado de Leguminosas")
    print("Se miden distintos valores:")
    # Sensor 1, mide Temperatura
    sensor_temp = []
    for _ in range(29):
        lecturas_celsius = random.uniform(15, 50)
        sensor_temp.append(lecturas_celsius)

    # Sensor 2, mide Humedad en 
    sensor_humedad = []
    for _ in range(29):
        lecturas_humedad = random.uniform(15, 50)
        sensor_humedad.append(lecturas_humedad)

    # Sensor 3, mide el Peso en Gramos.
    sensor_peso = []
    for _ in range(29):
        lecturas_peso = random.uniform(10, 250)
        sensor_peso.append(lecturas_peso)

    # Sensor 4, mide la Vibración de la tolva en Hz.
    sensor_vibracion = []
    for _ in range(29):
        lecturas_vibracion = random.uniform(50, 250)
        sensor_vibracion.append(lecturas_vibracion)

    
    # Sensor 5, mide la Velocidad de llenado en Envases por minutos
    sensor_velocidad = []
    for _ in range(29):
        lecturas_velocidad = random.uniform(50, 250)
        sensor_velocidad.append(lecturas_velocidad)


    # Crear la figura y los subplots
    plt.figure(figsize=(12, 10))

    # Sensor 1 - Temperatura
    plt.subplot(5, 1, 1)
    plt.plot(sensor_temp, color='red')
    plt.title("Temperatura (°C)")
    plt.ylabel("°C")
    plt.grid(True)

    # Sensor 2 - Humedad
    plt.subplot(5, 1, 2)
    plt.plot(sensor_humedad, color='blue')
    plt.title("Humedad (%)")
    plt.ylabel("%")
    plt.grid(True)

    # Sensor 3 - Peso
    plt.subplot(5, 1, 3)
    plt.plot(sensor_peso, color='green')
    plt.title("Peso (g)")
    plt.ylabel("g")
    plt.grid(True)

    # Sensor 4 - Vibración
    plt.subplot(5, 1, 4)
    plt.plot(sensor_vibracion, color='purple')
    plt.title("Vibración (Hz)")
    plt.ylabel("Hz")
    plt.grid(True)

    # Sensor 5 - Velocidad de llenado
    plt.subplot(5, 1, 5)
    plt.plot(sensor_velocidad, color='orange')
    plt.title("Velocidad de llenado (env/min)")
    plt.ylabel("Env/min")
    plt.xlabel("Lecturas")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

        