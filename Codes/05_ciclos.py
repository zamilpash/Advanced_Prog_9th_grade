"""

for var in secuencia:
    # Hacer algo ...

Donde var es la variable de ciclo o variable de control y secuencia la secuencia de valores que deberá iterarse. 
Es necesario remarcar la importancia de los dos puntos al final de esta primera línea y en indentar el bloque de código subsecuente que definirá el cuerpo del ciclo for.

# Ciclo FOR con rangos numericos
print("---Monitoreo de sensores")

for sensor_id in range (1,6):               # Se puede colocar 3 numeros, primer numero es el en el que empieza, segundo donde termina y el tercero es el paso que avanza 
    print(f"Leyendo sensor {sensor_id} ...")
    lectura_sensor = sensor_id * 10
    print(f"Valor {lectura_sensor} unidades")

# Usar for para iterar datos
lecturas_temp = [22.5, 33.4, 33.2, 22, 99.4, 100.5]
print("--- Analisis de temperatura \n")

for i, temperatura in enumerate(lecturas_temp):             # Cuando tiene 2 variables se usa enumerate, asígna una posición a cada valor de la lista
    print(f"Lectura {i + 1}: {temperatura} °C ")
    if temperatura > 26.0:
        print("!Temperatura elevada¡")


# Ciclo for con cadenas y diccionarios
comando = "M300S1500"

print("\ --- Análisis de comando ---")
for caracter in comando:
    if caracter == "M":    
        print("Identicador de motor detectado")
    elif caracter == "S":
        print("Se ha dectectado una velocidad")
    elif caracter.isdigit():                                # .isdigit identifica si es un digito
        print(f"Valor numerico : {caracter}")
"""

# Ciclo for con diccionarios
parametros_robot = {
    "velocidad_max" : 1000,
    "aceleracion": 250,
    "presicion" : 0.01,
    "carga_max" : 5.0
}

print("\n --- Parámetros del robot")
for parametro, valor in parametros_robot.items():
    print(f"{parametro.replace(_old:'_', _new:' ').title()}: {valor}")