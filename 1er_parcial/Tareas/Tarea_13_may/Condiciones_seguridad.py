# Ejercicio 3
# Verificar condiciones de seguridad


nombre = input("Ingrese su nombre, operador: ")

# Ingresar límites
print("\n--- Definir límites de seguridad ---")
temp_min = float(input("Límite mínimo de temperatura: "))
temp_max = float(input("Límite máximo de temperatura: "))

vib_min = float(input("Límite mínimo de vibración: "))
vib_max = float(input("Límite máximo de vibración: "))

volt_min = float(input("Límite mínimo de voltaje: "))
volt_max = float(input("Límite máximo de voltaje: "))

# Ingresar valores actuales
print("\n--- Ingresar valores actuales del sistema ---")
temp = float(input("Temperatura actual: "))
vib = float(input("Vibración actual: "))
volt = float(input("Voltaje actual: "))

# Evaluar condiciones
fuera_rango = 0

if temp < temp_min or temp > temp_max:
    fuera_rango += 1

if vib < vib_min or vib > vib_max:
    fuera_rango += 1

if volt < volt_min or volt > volt_max:
    fuera_rango += 1

# Diagnóstico
print("\n--- Evaluación del Sistema ---")
if fuera_rango == 0:
    print("Estado: NORMAL (verde)")
    print("Acción: No hacer nada.")
elif fuera_rango == 1:
    print("Estado: CRÍTICO (amarillo)")
    print("Acción: Realizar un chequeo.")
else:
    print("Estado: PELIGRO (rojo)")
    print("Acción: Dar mantenimiento inmediato.")
