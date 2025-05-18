# Tuplas
# Permiten indexado pero no se pueden modificar, van entre parentesís

print("Tuplas para ingeniería \n")

origen = (0, 0, 0)
home = (150, 0, 200)
punto_trabajo = (200, 120, 50)

print(type(origen))
print(f"\n Coordenada z del punto de trabajo: {punto_trabajo[2]}")


# Coordenadas desempaquetadas
x, y, z = punto_trabajo
