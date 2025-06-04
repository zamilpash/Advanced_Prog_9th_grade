# Programación Orientada a Objetos en Python.
"""
class Persona:
    def __init__(self, nombre, edad, direccion):                       # Metodo o funcion init es el constructor, estarán los atributos. Self se utiliza para conectar a 
        self.nombre = nombre                                           # Atributos de una persona.
        self.edad = edad
        self.direccion = direccion
        pass 


# Darle valores a su atributos.
persona_1 = Persona("Ana", 22, "Alameda #2, Colonia Centro")


print(type(Persona))
print(f"Nombre: {persona_1.nombre} \n Edad: {persona_1.edad}")

print(persona_1.direccion)


# Manipulacion de metodos
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        pass
    
    # Metodo para calcular area
    def calcular_area(self):                                
        area = 3.1416 * (self.radio) ** 2
        
        return area 
    
    # Metodo para calcular perimetro
    def calcular_perimetro(self):
        perimetro = 2 * 3.1416 * self.radio
        return perimetro


circulo_1 = (Circulo(5))                                            # circulo_1 es un 
print(f"Area: {circulo_1.calcular_area():.2f}")                     # Mandar llamar un metodo, siempre se usa () al final
print(f"Perimetro: {circulo_1.calcular_perimetro():.2f}")



# Crea una clase estudiante que almacene el nombre, matricula, promedio y con un metodo que lo apruebe si es mayor o igual a 7


class Estudiante:
    def __init__(self, nombre, matricula, promedio):
        self.nombre = nombre
        self.matricula = matricula
        self.promedio = promedio
        pass

    def aprobar(self):
        if self.promedio >= 7:
            return print("Estudiante aprobado!!")

        else:
            return print("Estudiante no aprobado :c ")
            
         
    
estudiante = Estudiante("Jose", 1111111, 9)

estudiante.aprobar()



# Herencia: Puedes crear clases hijas que heredan atributos de clases padres.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
    def encender (self):
        print(f"El vehículo {self.marca} {self.modelo} esta encendido")


# Clase derivada
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)                 # El metodo super hereda todos los atributos de la clase padre.
        self.puertas = puertas


auto = Automovil("Toyota", "Civic", 4)
auto.encender()
print(f"Este auto tiene {auto.puertas} puertas")




class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "Hace un sonido"
    


class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacer_sonido(self):
        return "Ladra"
    

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacer_sonido(self):
        return "Maulla"
        

perro = Perro("Max", 5)
gato = Gato("Gatito", 3)


print(f"{perro.nombre} {perro.hacer_sonido()}")
print(f"{gato.nombre} {gato.hacer_sonido()}")

"""

# Crear una clase base "Empleado" con atributos nombre y salario, con un metodo que se llame info.
# 2 clases derivadas Gerentes con atributo bono_adicional y Asistente con atributo no_tiene_bono_adicional


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        return f"Empleado: {self.nombre} | Salario {self.salario}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono 

    def bono(self):
        return f"Gerentes: {self.salario + self.bono}"
    

class Asistente(Empleado):
    pass
    

gerente = Gerente("Arturo", 50000, 10000)
asistente = Asistente("Ana", 30000)


print(gerente.mostrar_info())

print(asistente.mostrar_info())
