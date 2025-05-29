# Control de velocidad de un motor.
""" 
Objetivo: Crea una clase llamada Motor con atributos como "velocidad, aceleración y estado".
Implementar métodos para encender, apagar, cambiar velocidad y mostrar el estado actual.
Simula el cambio de estado de un motor con diferentes valores y documenta el uso de la clase.
Aplica conceptos de programación orientada a objetos.
"""

class Motor:
    def __init__(self, velocidad, aceleracion, estado):
        self.velocidad = 0
        self.aceleracion = 0
        self.estado = "apagado"
        pass

    def encender(self):
        return print(" Motor esta encendido")
    
    def apagar(self):
        return print("El motor esta apagado")

    def cambiar_velocidad(self, velocidad):

        


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
