# Funciones básicas en aplicaciones de Mecatrónica

"""
def nombre de la funcion (parametros):
    cuerpo de la funcion

"""

def mostrar_cabecera():
    print("=" * 50)
    print(" Sistema de control Mecatronico v1.0")
    print("=" * 50)


# Mandar llamar la funcion
#mostrar_cabecera()



# Funcion con parametros 
def fuerza (masa, aceleracion):
    """
    Calcula la fuerza segun la segunda ley de Newton
    Args:
        masa (float): Masa del objeto en kilogramos
        aceleracion (float): Aceleracion en m/s2

    Returns:
        float : Fuerza resultante en Newtons
    """

    fuerza = masa * aceleracion

    return fuerza

fuerza(2.5, 9.81) 


def configurar_motor (velocidad, aceleracion = 100, modo = "normal"):
    print(f" Configuracion motor:")
    print(f"- Velocidad: {velocidad} RPM")
    print(f"- Aceleracion: {aceleracion} m/s2")
    print(f"- Modo : {modo} \n")

    if modo == "normal":
        tiempo_estimado = velocidad / aceleracion
    elif modo == "eco":
        tiempo_estimado = velocidad / (aceleracion * 0.8)
    elif modo == "turbo":
        tiempo_estimado = velocidad / (aceleracion * 1.2)
        
    print(f" Tiempo estimado para alcanzar velocidad : {tiempo_estimado:.2f} s")



configurar_motor(1000)
configurar_motor(1500, 200)
configurar_motor(2000, 300, modo = "turbo")
