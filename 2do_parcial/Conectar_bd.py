import pymysql

# Configuración de conexión sin especificar base de datos
config = {
    'host': 'localhost',
    'user': 'Usuario_nuevo',
    'password': 'Test987654321'
}

def crear_base_datos():
    try:
        conn = pymysql.connect(**config)
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS Usuarios")
            print(" Base de datos 'Usuarios' creada o ya existente")
        conn.close()
    except Exception as e:
        print(f" Error al crear la base de datos: {e}")

if __name__ == '__main__':
    print("===== CREAR BASE DE DATOS =====")
    crear_base_datos()
