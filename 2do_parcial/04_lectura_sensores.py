import pymysql
import random
import time
from datetime import datetime

# Configuración de conexión a la base de datos
config = {
    'host': 'localhost',
    'user': 'Usuario_nuevo',
    'password': 'Test987654321',
    'database': 'Sistema_monitoreo'
}

# Crear tabla si no existe
def crear_tabla_lecturas():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS Lecturas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tipo_sensor VARCHAR(30) NOT NULL,
            valor FLOAT(10) NOT NULL,
            fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        cursor.execute(sql)
        conn.commit()
        conn.close()
        print("Tabla Lecturas creada")
    except Exception as e:
        print(f"Error al crear tabla: {e}")

# Generar datos aleatorios según el tipo de sensor
def generar_datos_sensor(tipo_sensor):
    if tipo_sensor == "Temperatura":
        return round(random.uniform(20.0, 80.0), 2)
    elif tipo_sensor == "Presion":
        return round(random.uniform(50.0, 200.0), 2)
    elif tipo_sensor == "Humedad":
        return round(random.uniform(30.0, 90.0), 2)
    elif tipo_sensor == "CO2":
        return round(random.uniform(400.0, 1500.0), 2)
    elif tipo_sensor == "Luz":
        return round(random.uniform(0.0, 1023.0), 2)
    else:
        return round(random.uniform(0, 100), 2)

# Insertar una lectura en la base de datos
def insertar_dato_sensor(tipo_sensor):
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        valor = generar_datos_sensor(tipo_sensor)
        sql = "INSERT INTO Lecturas (tipo_sensor, valor) VALUES (%s, %s)"
        cursor.execute(sql, (tipo_sensor, valor))
        conn.commit()
        conn.close()
        print(f"Insertado: {tipo_sensor} = {valor}")
    except Exception as e:
        print(f"Error al insertar dato: {e}")

# Función que genera múltiples lecturas
def simular_datos_sensores(sensores):
    for sensor in sensores:
        for _ in range(10):
            insertar_dato_sensor(sensor)
            time.sleep(0.2)


def limpiar_tabla_lecturas():
    try:
        # Realizamos conexión a la DB
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        # Comando para borrar todos los datos de la tabla
        cursor.execute("DELETE FROM Lecturas")

        # Reinicia el contador de AUTO_INCREMENT
        cursor.execute("ALTER TABLE Lecturas AUTO_INCREMENT = 1")

        conn.commit()
        conn.close()
        print("Tabla Lecturas vaciada correctamente.")

    except Exception as e:
        print(f"Error al limpiar la tabla: {e}")



# Código principal
if __name__ == '__main__':
    crear_tabla_lecturas()  # Crear la tabla una vez
    limpiar_tabla_lecturas()
    sensores = ["Temperatura", "Presion", "Humedad", "CO2", "Luz"]
    simular_datos_sensores(sensores)  # Insertar datos simulados
