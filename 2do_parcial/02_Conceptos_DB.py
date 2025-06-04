# Conceptos básicos de Bases de datos con MySql
import pymysql

# Crear conexión usando un diccionario
config = {
    'host' : 'localhost',            # creamos el servidor
    'user' : 'test1',             # Creamos un usuario
    'password': 'test123',            # Creamos una contraseña
    'database': 'Usuarios'
}

# Funcion para probar nuestra conexión

def test_conection():
    try:
        conn = pymysql.connect(**config)
        print(f"!Conexión Exitosa¡")
    

        cursor = conn.cursor()
        sql = "CREATE DATA BASE IF NOT EXISTS Usuarios"
        cursor.execute(sql)
        print("!Base de datos: 'Usuarios' creada¡")
        conn.close()


    except Exception as e:
        print(f"Error al crear la base de datos {e}")


# Crear tabla user
# el is simpre 
def crear_tabla_user():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        sql = """CREATE TABLE IF NOT EXISTS Usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        usuario VARCHAR(30) UNIQUE NOT NULL,
        password VARCHAR(30) NOT NULL,
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        conn.commit()

        cursor.execute(sql)
        print("Trabla creada exitosamente")

        conn.close()

    except Exception as e:
        print(f"Error creando tabla: {e}")


def insertar_usuarios():
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        usuarios = [
            ("Administrador", "admin", "1234"),
            ("Jose Altuve", "astroboy", "4321")
        ]

    except Exception as e:
        print(f"Error insertando usuarios {e}")


    for nombre, usuario, password in usuarios:
        sql = """INSERT INTO Users (nombre, usuario, password)
                VALUES (%s, %s, %s)"""
        
        cursor.execute(sql, nombre, usuario, password)
        print("Usuarios creados correctamente")
        conn.commit()





if __name__ == '__main__':
    print("===== Creando Sistemas ====")

    test_conection()
    crear_tabla_user()
    insertar_usuarios()