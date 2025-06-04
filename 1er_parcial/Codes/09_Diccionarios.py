# Diccionarios en Ingenierías

print("\n === Diccionarios en aplicaciones Mecatrónicas ===")

# Configuracion de un controlador para un motor DC

config_motor = {
    "Id": "M01",
    "Tipo": "BLDC",
    "Voltaje_nom": 24.0,
    "Corriente_max": 10.0,
    "Vel_max": 5000,
    # Dicionario dentro de otro diccionario
    "Limites": {
        "Temperatura": 85,
        "Aceleracion": 2000
    } 
}
"""
print(type(config_motor))

# Indexado de diccionarios
print(f"Motor ID: {config_motor['Id']}")
print(f"Tipo: {config_motor['Tipo']}")
print(f"Voltaje Nominal: {config_motor['Voltaje_nom']}")


# Indexado de diccionarios dentro de diccionario
print(f"Temperatura limite: {config_motor['Limites']['Temperatura']}")


# Modificar diccionarios 
config_motor ["Vel_max"] = 6000
"""
# Agregar nuevos parametros
#config_motor['Eficiencia'] = 0.95

# print(config_motor)


# Obtener clave-valor

items = config_motor.items()
print("\nPares Clave-Valor (primeros 3):")
for i, (clave, valor) in enumerate(list(items)[:3]):
    print(f"{clave}: {valor}")
