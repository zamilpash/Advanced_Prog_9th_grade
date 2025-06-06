# Importamos el módulo pymysql para conectarnos y manipular bases de datos MySQL desde Python
import pymysql

# Diccionario de configuración para conectarse a la base de datos
config = {
    'host' : 'localhost',             # Dirección del servidor (localhost si es local)
    'user' : 'Usuario_nuevo',         # Nombre de usuario creado en MySQL
    'password': 'Test987654321',      # Contraseña del usuario
    'database': 'Sistema_monitoreo'            # Nombre de la base de datos a usar
}

# Función para probar la conexión y crear la base de datos si no existe
def test_conection():
    try:
        # Intentamos conectarnos a MySQL usando la configuración
        conn = pymysql.connect(**config)
        print("!Conexión Exitosa¡")

        # Creamos un cursor para ejecutar comandos SQL
        cursor = conn.cursor()

        # SQL para crear la base de datos solo si no existe
        sql = "CREATE DATABASE IF NOT EXISTS Sistema_monitoreo"
        cursor.execute(sql)  # Ejecuta el comando SQL
        print("!Base de datos: 'Sistema_monitoreo' creada o ya existente¡")

        # Cerramos la conexión
        conn.close()

    except Exception as e:
        # Si hay error, lo mostramos
        print(f"Error al crear la base de datos {e}")

# Función para crear la tabla Usuarios dentro de la base de datos
def crear_tabla_user():
    try:
        # Conexión a la base de datos
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        # SQL para crear la tabla con sus columnas
        sql = """CREATE TABLE IF NOT EXISTS Operadores (
        id INT AUTO_INCREMENT PRIMARY KEY,        -- ID auto incremental
        nombre VARCHAR(50) NOT NULL,              -- Campo nombre obligatorio
        usuario VARCHAR(30) UNIQUE NOT NULL,      -- Campo usuario único y obligatorio
        password VARCHAR(30) NOT NULL,            -- Campo password obligatorio
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Fecha automática al crear
        )"""

        # Ejecutamos la consulta y guardamos cambios
        cursor.execute(sql)
        conn.commit()
        print("Tabla creada exitosamente")

        # Cerramos la conexión
        conn.close()

    except Exception as e:
        print(f"Error creando tabla: {e}")

# Función para insertar usuarios predefinidos en la tabla
def insertar_usuarios():
    try:
        # Conexión a la base de datos
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        # Lista de usuarios a insertar (nombre, usuario, password)
        usuarios = [
            ("Administrador", "admin", "1234"),
            ("Jose Altuve", "astroboy", "4321")
        ]

        # Recorremos cada usuario y lo insertamos
        for nombre, usuario, password in usuarios:
            sql = """INSERT INTO Operadores (nombre, usuario, password)
                    VALUES (%s, %s, %s)"""
            cursor.execute(sql, (nombre, usuario, password))

        # Guardamos los cambios
        conn.commit()
        print("Usuarios creados correctamente")

        # Cerramos la conexión
        conn.close()

    except Exception as e:
        print(f"Error insertando usuarios {e}")

# Función para mostrar todos los registros de la tabla Usuarios
def mostrar_usuarios():
    try:
        # Crear la conexión a la base de datos usando la configuración definida
        conn = pymysql.connect(**config)
        
        # Crear un cursor para ejecutar comandos SQL
        cursor = conn.cursor()

        # Definir la consulta SQL para obtener todos los registros de la tabla Usuarios
        sql = "SELECT * FROM Usuarios"
        
        # Ejecutar la consulta
        cursor.execute(sql)
        
        # Obtener todos los resultados de la consulta
        resultados = cursor.fetchall()  

        # Iterar sobre cada fila de resultados y mostrarla
        for fila in resultados:
            # fila es una tupla: (id, nombre, usuario, password, fecha_creacion)
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Usuario: {fila[2]}, Password: {fila[3]}, Fecha: {fila[4]}")

        # Cerrar la conexión a la base de datos
        conn.close()

    except Exception as e:
        # En caso de error, mostrar mensaje con la descripción del error
        print(f"Error mostrando usuarios: {e}")

# Bloque principal que se ejecuta al correr el archivo
if __name__ == '__main__':
    print("===== Creando Sistemas ====")

    # Llamamos a las funciones que necesitamos
    test_conection()         # Verifica conexión y crea DB si no existe
    crear_tabla_user()      # Crear tabla (descomentar si quieres volver a ejecutar)
    insertar_usuarios()     # Insertar usuarios (descomentar si quieres volver a insertar)
#    mostrar_usuarios()       # Mostrar todos los usuarios en consola
