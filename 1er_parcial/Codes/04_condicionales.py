# Control basico de un sistema
# Se aplico una maquina de estado para controlar el sistema
# Se utilizo un sistema de control de temperatura para encender o apagar un calentador y un enfriador
temperature = 75.0

if temperature < 20.0:
    print("Calentando el sistema")
    estado_calentador = "Encendido"
    estado_calentador = True
elif temperature > 80.0:
    print("Enfriando el sistema")
    estado_calentador = "Apagado"
    estado_calentador = False
    activar_enfriamiento = True
    print("Activando enfriamiento")
else:
    print("Sistema en temperatura normal")


# Condicionales anidados

sistema_encendido = True
nivel_bateria = 15
modo_operacion = "APAGADO"

if sistema_encendido:
    if nivel_bateria < 20:
        modo_operacion = "NORMAL"
    else:
        modo_operacion = "ECO"
else:
    modo_operacion = "APAGADO"
