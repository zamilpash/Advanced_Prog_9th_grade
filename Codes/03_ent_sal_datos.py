# Entrada y salida de datos
usuario = input("¿Cuál es tu nombre? \n")

print(f"Hola  {usuario} , bienvenido al resgitro de mantenimiento.")        # f significa estructura f string, permite concatenar variables y texto


# Entrada numerica con validacion basica
try :
    velocidad = float(input("Ingrese la velocidad de motor (rpm): \n"))
    print(f"La velocidad configurada: {velocidad} rpm")
except ValueError:
    print("Error: Debe ingresar un número válido para la velocidad válida.")


# Formato de Salida y multiples valores en una linea

temp = 25.5
presion = 14312120.123456789

print(f"Temperatura: {temp:.2f} °C, Presión: {presion/1000:.2f} Pa")                 # .2f significa que se mostrara con 2 decimales



# Ciclo For

for i in range(5):
    sensor = f"S{i+1}"
    valor = i * 10
    print(f"{sensor}: {valor}V ", end = "     |")