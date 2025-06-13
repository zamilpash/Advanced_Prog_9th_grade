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
        sql = """CREATE TABLE IF NOT EXISTS Lecturas_Sensores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tipo_sensor VARCHAR(30) NOT NULL,
            valor DECIMAL(10) NOT NULL,
            estado VARCHAR(30) NOT NULL,
            fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""

        # Verificación adicional
        cursor.execute("SHOW COLUMNS FROM Lecturas LIKE 'estado'")
        if not cursor.fetchone():
            print("¡Error: La columna 'estado' no se creó!")
        else:
            print("Tabla Lecturas creada correctamente con columna 'estado'")

        cursor.execute(sql)
        conn.commit()
        conn.close()
        print("Tabla Lecturas_sensores creada")
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
    elif tipo_sensor == "Vibracion":
        return round(random.uniform(400.0, 1500.0), 2)
    elif tipo_sensor == "Luz":
        return round(random.uniform(0.0, 1023.0), 2)
    else:
        return round(random.uniform(0, 100), 2)

# Obtener el estao del sensor
def estado_sensor():
    estado = ("Activo", "Inactivo")
    return random.choice(estado)


# Insertar una lectura en la base de datos
def insertar_dato_sensor(tipo_sensor):
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        valor = generar_datos_sensor(tipo_sensor)
        estado_actual = estado_sensor()
        sql = "INSERT INTO Lecturas_Sensores (tipo_sensor, valor, estado) VALUES (%s, %s, %s)"
        cursor.execute(sql, (tipo_sensor, valor, estado_actual))
        conn.commit()
        conn.close()
        print(f"Insertado: {tipo_sensor} = {valor}, Estado: {estado_actual}")
    except Exception as e:
        print(f"Error al insertar dato: {e}")

def simular_datos_sensores(sensores):
    for sensor in sensores:          # 1. Itera sobre cada tipo de sensor
        for _ in range(10):         # 2. Genera 10 lecturas por sensor
            insertar_dato_sensor(sensor)  # 3. Inserta cada lectura
            time.sleep(0.2)         # 4. Pausa entre lecturas

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
    crear_tabla_lecturas()  # Crear la tabla
    limpiar_tabla_lecturas()    # Limpiar tabla para no tener tantos datos
    sensores = ["Temperatura", "Presion", "Humedad", "Vibracion", "Luz"]
    simular_datos_sensores(sensores)  # Insertar datos simulados