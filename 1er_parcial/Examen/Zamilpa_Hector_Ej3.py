# Gestion de sensores con diccionarios

"""
Usar un diccionario para almacenar la configuración de varios sensores (tipo, unidad, valor mínimo y máximo). 
Solicita al ususairo que ingrese un valor y verifica si está en el rango permitido para ese sensor. 
Incluye manejo de excepciones por si se ingresa una clave incorrecta o un valor inválido.
"""
sensores = {
    "Sensor_1": {
        "Tipo": "Infrarrojo",
        "Unidad": 11,
        "Val_max": 250,
        "Val_min": 25
    },
    "Sensor_2": {
        "Tipo": "Temperatura",
        "Unidad": 13,
        "Val_max": 35,
        "Val_min": 15
    },
    "Sensor_3": {
        "Tipo": "Humedad",
        "Unidad": 15,
        "Val_max": 65,
        "Val_min": 20
    },
    "Sensor_4": {
        "Tipo": "Presión",
        "Unidad": 17,
        "Val_max": 500,
        "Val_min": 100
    }
}

# --- Verificación de Valores de Sensores ---

while True:

    print("\n--- Verificación de Valores de Sensores ---")    
    print("1. Sensor 1")
    print("2. Sensor 2")
    print("3. Sensor 3 ")
    print("4. Sensor 4")
    print("5. Salir")
    
    opcion = input("¿Qué sensor quieres verificar? (ej. Sensor_1, Sensor_2, etc. o 'salir' para terminar): ")

    if opcion.lower() == 'salir':
        print("Saliendo del programa.")
        break

    try:
        # Verificar si la clave del sensor existe en nuestro diccionario 'sensores'
        if opcion not in sensores:
            raise KeyError(f"Error: El sensor '{opcion}' no se encuentra en la configuración. Por favor, elige uno de la lista.")

        sensor_seleccionado = sensores[opcion]
        min_val = sensor_seleccionado["Val_min"]
        max_val = sensor_seleccionado["Val_max"]
        unidad = sensor_seleccionado["Unidad"]

        print(f"\nHas seleccionado: **{opcion}** (Tipo: **{sensor_seleccionado['Tipo']}**)")
        print(f"Rango permitido: **{min_val}** a **{max_val}** (Unidad: **{unidad}**)")

        valor_str = input(f"Ingresa un valor para {opcion}: ").strip()

        try:
            # Intentar convertir el valor a un número (entero o flotante)
            if '.' in valor_str:
                valor_ingresado = float(valor_str)
            else:
                valor_ingresado = int(valor_str)

            # Verificar si el valor está en el rango permitido
            if min_val <= valor_ingresado <= max_val:
                print(f" El valor **{valor_ingresado}** está **dentro** del rango permitido para {opcion}.")
            else:
                print(f" El valor **{valor_ingresado}** está **FUERA** del rango permitido ({min_val}-{max_val}) para {opcion}.")

        except ValueError:
            print(f"Error: El valor ingresado '**{valor_str}**' no es un número válido. Por favor, intenta de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al procesar el valor: {e}")

    except KeyError as e:
        print(e) # Imprime el mensaje de error que creamos en el raise KeyError
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    print("-" * 40) # Un separador para mejor legibilidad entre cada verificación