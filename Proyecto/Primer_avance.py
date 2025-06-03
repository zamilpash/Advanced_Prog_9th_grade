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
    for _ in range(29):         # Se usa el _ para no tener variable de iteración, ya que en este caso no es necesario.
        lecturas_celsius = random.uniform(15, 50)
        sensor_temp.append(lecturas_celsius)

    # Sensor 2, mide Humedad en Porcentaje
    sensor_humedad = []
    for _ in range(29):         # Se usa el _ para no tener variable de iteración, ya que en este caso no es necesario.
        lecturas_humedad = random.uniform(0, 60)
        sensor_humedad.append(lecturas_humedad)

    # Sensor 3, mide el Peso en Gramos.
    sensor_peso = []
    for _ in range(29):         # Se usa el _ para no tener variable de iteración, ya que en este caso no es necesario.
        lecturas_peso = random.uniform(10, 250)
        sensor_peso.append(lecturas_peso)

    # Sensor 4, mide la Vibración de la tolva en Hz.
    sensor_vibracion = []
    for _ in range(29):         # Se usa el _ para no tener variable de iteración, ya que en este caso no es necesario.
        lecturas_vibracion = random.uniform(0, 150)
        sensor_vibracion.append(lecturas_vibracion)

    
    # Sensor 5, mide la Velocidad de llenado en Envases por minutos (10 - 40)
    sensor_velocidad = []
    for _ in range(29):         # Se usa el _ para no tener variable de iteración, ya que en este caso no es necesario.
        lecturas_velocidad = random.uniform(10, 40)
        sensor_velocidad.append(lecturas_velocidad)

#Detectar valores y enviar alertas

    # Detectar lecturas fuera del rango permitido para Temperaturas (20°C a 40°C)
    for temp in sensor_temp:
        if temp < 20:
            print(f"\nTemperatura debajo del rango: {temp:.2f}")
        
        elif temp > 40:
            print(f"\nTemperatura demasiado alta: {temp:.2f}")

        else:
            print(f"\nTemperatura dentro del rango permitido: {temp:.2f} °C")


    # Detectar lecturas fuera del rango permitido para Humedad (0% a 50°C)
    for hume in sensor_humedad:
        if hume < 0:
            print(f"\nHumedad debajo del rango: {hume:.2f}")
        
        elif temp > 50:
            print(f"\nHumedad demasiado alta: {hume:.2f}")

        else:
            print(f"\nHumedad dentro del rango permitido: {hume:.2f} °C")


    # Detectar lecturas fuera del rango permitido para el Peso (0g a 260g)
    for peso in sensor_peso:
        if peso < 20:
            print(f"\nPeso debajo del rango: {peso:.2f}")
        
        elif peso > 40:
            print(f"\nPeso demasiado alta: {peso:.2f}")

        else:
            print(f"\nPeso dentro del rango permitido: {peso:.2f} °C")


    # Detectar lecturas fuera del rango permitido para Vibración (0 Hz - 150 Hz)
    for vibracion in sensor_vibracion:
        if vibracion < 0:
            print(f"\nVibración debajo del rango: {vibracion:.2f}")
        
        elif vibracion > 160:
            print(f"\nVibración demasiado alta: {vibracion:.2f}")

        else:
            print(f"\nVibración dentro del rango permitido: {vibracion:.2f} °C")
        

    # Detectar lecturas fuera del rango permitido para Velocidad de llenado (0 - 100)
    for velocidad in sensor_velocidad:
        if velocidad < 20:
            print(f"\nVelocidad de envasado debajo del rango: {velocidad:.2f}")
        
        elif velocidad > 40:
            print(f"\nVelocidad de envasado demasiado alta: {velocidad:.2f}")

        else:
            print(f"\nVelocidad de envasado dentro del rango permitido: {velocidad:.2f} °C")


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