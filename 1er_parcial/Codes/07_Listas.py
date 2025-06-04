temp_celsius = [22.5, 33.7, 88.9, 88.2, 12.2, 166.9, 81, 32]

"""
# Estructuras de datos 

# Listas 
print("---- Comprension de listas en aplicaciones de ingenierias----")

print(type(temp_celsius))

# Agregar elemento a la lista .append
temp_celsius.append(22.8)

# Número de elementos de la lista len()
print(len(temp_celsius))

# Indexar una lista (Ingresar y sacar el valor del elemento en especifico)
print(temp_celsius[4])

for i, valor in enumerate(temp_celsius):
    print(f"Valor de Temperatura {i}: {valor}°C")




temp_celsius[3] = 22
print(temp_celsius)

tempe_farenheith = [(temp * 1.8) + 32
                    for temp in temp_celsius
                    ]

print(f"Temperaturas Farenheith: ", temp_celsius, "°F")

temp_altas = [ temp for temp in temp_celsius
              if temp > 23.0:  
                print(f"Temperaturas por encima de 23°C:  {temp_altas}")]



ciclos_trabajo = [round(i/10, 1) for i in range (11)]
print(f"\n Secuencia de ciclos de trabajo PWM: {ciclos_trabajo}")

"""

# Listas de listas (Matrices)
matriz_distancias = [
    [ 120, 122, 123, 124, 125],
    [ 130, 132, 133, 134, 135],
    [ 200, 225, 250, 180, 123],
    [ 170, 171, 172, 173, 174]
]

# Acceso a los elementos en matrices
print("=== Acceso a matrices ===")
print(f"Todas las mediciones del primer renglon son : {matriz_distancias[0]}")
print(f" Medicion de posicion 3,3: {matriz_distancias[2][2]}")