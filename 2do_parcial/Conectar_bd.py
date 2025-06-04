# Conceptos básicos de Bases de datos con MySql
import pymysql

# Crear conexión usando un diccionario
config = {
    'host' : 'localhost',            # creamos el servidor
    'user' : 'test1',                # Creamos un usuario
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




if __name__ == '__main__':
    print("===== Creando Sistemas ====")

    test_conection()
    