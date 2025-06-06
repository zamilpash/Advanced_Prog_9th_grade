import pymysql

# Configuración correcta para conectarse a la base de datos ya existente
config = {
    'host': 'localhost',
    'user': 'Usuario_nuevo',
    'password': 'Test987654321',
    'database': 'Sistema_monitoreo'  
}

# Función para verificar si un usuario y contraseña existen en la tabla 'usuarios'
def verificar_usuario(usuario, password):
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        sql = """SELECT usuario, password FROM Operadores WHERE 
        usuario = %s AND password = %s"""
        cursor.execute(sql, (usuario, password))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return True, resultado[0], resultado[1]
        else:
            return False, None, None

    except Exception as e:
        print(f"Error en login: {e}")
        return False, None, None

# Función para pedir credenciales al usuario e intentar iniciar sesión
def hacer_login():
    print("Por favor ingresa tus credenciales:")
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    exito, usuario, password = verificar_usuario(usuario, password)

    if exito:
        print(f" Bienvenido, {usuario}")
        return True, usuario, password
    else:
        print(" Usuario o contraseña incorrectos")
        return False, None, None

# Función principal que llama al login
def main():
    exito, usuario, password = hacer_login()
    if exito:
        print(f"Sesión iniciada correctamente como {usuario}")
    else:
        print("No se pudo iniciar sesión.")

# Ejecutar si este archivo es el principal
if __name__ == '__main__':

    main()  
