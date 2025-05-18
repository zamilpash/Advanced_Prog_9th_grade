# Ejercicio 2
# Convertir unidades de Sistema metrico a Ingles y viceversa

while True:
    print("\n--- Conversor de Unidades entre sistemas---")
    print("1. Presión: kPa a psi")
    print("2. Presión: psi a kPa")
    print("3. Temperatura: °C a °F")
    print("4. Temperatura: °F a °C")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        try:
            kpa = float(input("Introduce la presión en kPa: "))
            psi = kpa * 0.145038
            print(f"{kpa} kPa = {psi:.2f} psi")
        except ValueError:
            print("Entrada inválida.")

    elif opcion == '2':
        try:
            psi = float(input("Introduce la presión en psi: "))
            kpa = psi / 0.145038
            print(f"{psi} psi = {kpa:.2f} kPa")
        except ValueError:
            print("Entrada inválida.")

    elif opcion == '3':
        try:
            celsius = float(input("Introduce la temperatura en °C: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} °C = {fahrenheit:.2f} °F")
        except ValueError:
            print("Entrada inválida.")

    elif opcion == '4':
        try:
            fahrenheit = float(input("Introduce la temperatura en °F: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit} °F = {celsius:.2f} °C")
        except ValueError:
            print("Entrada inválida.")

    elif opcion == '5':
        print("Saliendo del conversor.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
