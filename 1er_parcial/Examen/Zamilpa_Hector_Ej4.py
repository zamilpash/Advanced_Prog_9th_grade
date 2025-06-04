#  EJERCICIO 4: ESTADISTICAS DE DATOS MECATRONICOS

"""
Crear una lista con 15 lecturas de corriente de un sisitema mecatrónico. 
Calcula la media, mediana, valor minimo y maximo usando funciones. 
Muestra los resultados en pantala fomrato claro. Comenta el codigo y explica que se insterpresta en cada resultado.
"""

def mostrar_cabecera():
    print("=" * 70)
    print("------- Estadísticas de datos mecatrónicos--------")
    print("=" * 70)

mostrar_cabecera()

#Librerias random(simular las lecturas) statistics(para calcular medida y moda)
import random
import statistics

# 15 lecturas de corriente usando números aleatorios entre 0 y 10
lecturas_corriente = [round(random.uniform(0, 10), 2) for _ in range(15)]


# Función para calcular y mostrar estadísticas
def mostrar_estadisticas(lecturas):
    print("Lecturas de corriente (Amperes):")
    print(lecturas)

    # Calcular estadísticas
    media = statistics.mean(lecturas)
    mediana = statistics.median(lecturas)
    valor_min = min(lecturas)
    valor_max = max(lecturas)

    # Mostrar resultados con formato
    print("\n Estadísticas del sistema:")
    print(f" Media:   {media:.2f} A  -> Corriente promedio consumida por el sistema.")
    print(f" Mediana: {mediana:.2f} A  -> Valor central de las lecturas")
    print(f" Mínimo:  {valor_min:.2f} A  -> Lectura más baja registrada.")
    print(f" Máximo:  {valor_max:.2f} A  -> Lectura más alta registrada.")


# Ejecutar la función
mostrar_estadisticas(lecturas_corriente)