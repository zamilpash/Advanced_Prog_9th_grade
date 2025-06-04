"""
# Aplicacion de ciclo While
print("--- Simulación de control de temperatura")
temp_actual = 22
temp_objetivo = 40.0
pot_calentador = 0

# Simulación del aumento de temperatura
time = 0

while temp_actual < temp_objetivo:
    diferencia = temp_objetivo - temp_actual
    pot_calentador = min(100, diferencia * 10)

    incremento = pot_calentador * 0.05 
    temp_actual += incremento

    time += 1

    print(f" Tiempo : {time}s | Temperatura: {temp_actual:.2f}°C | Potencia: {pot_calentador:.2f}W")

    if time >= 20:
        print("Tiempo limite alcanzado")
        break


    print(f"Temperatura final: {temp_actual:.2f}°C")
"""


#Ciclo whiel con validacion de entrada

print("\n Sistema de control de velocidad")

velocidad_valida = False

while not velocidad_valida:
    try:
        velocidad = float(input("Ingrese velocidad deseada (0 - 100%): \n"))
        if 0 <= velocidad <= 100:
            velocidad_valida = True
            print(f"Velocidad configurada: {velocidad}%")
        else:
            print("Error: La velocidad debe estar entre 0 - 100% ")

    except ValueError:
        print("Error: Ingrese un valor númerico válido")
