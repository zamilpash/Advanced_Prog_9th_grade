# Ejercicio #1
# Calculadora de Presion, Momento y Potencia.

while True:
        print("\nCalculadora de Parámetros Mecánicos")
        print("1. Calcular Fuerza")
        print("2. Calcular Momento de Torsión")
        print("3. Calcular Potencia Mecánica ")
        print("4. Salir")

        parametro = input("Selecciona una opción: ")

        if parametro == '1':
            try:
                masa = float(input("Introduce la masa (en kg): "))
                aceleracion = float(input("Introduce la aceleración (en m/s²): "))
                if masa < 0 or aceleracion < 0:
                    print("La masa y la aceleración deben ser valores no negativos.")
                else:
                    fuerza = masa * aceleracion
                    print(f"La fuerza es: {fuerza:.2f} N")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número.")

        if parametro == '2':
            try:
                fuerza = float(input("Introduce la fuerza (en N): "))
                distancia = float(input("Introduce la distancia (en metros): "))
                if distancia < 0:
                    print("La distancia debe ser un valor no negativo.")
                else:
                    momento =  fuerza * distancia
                    print(f"El momento de torsión es: {momento:.2f} Nm")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número.")

        if parametro == '3':
            try:
                trabajo = float(input("Introduce el Trabajo (en J): "))
                tiempo = float(input("Introduce el tiempo (en s): "))
                potencia = trabajo * tiempo
                print(f"La potencia mecánica es: {potencia:.2f} W")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número.")

        if parametro == '4':
            print("Saliendo de la calculadora.")
            break

        if parametro != '1' and parametro != '2' and parametro != '3' and parametro != '4':
            print("Opción inválida. Por favor, selecciona una opción del menú.")