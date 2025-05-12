# Operadores aritmeticos

valor_1 = 8
valor_2 = 44
valor_3 = 11.88

# Sumar
suma = valor_1 + valor_2 + valor_3
# Resta
resta = valor_1 - valor_2 - valor_3
# Multiplicacion
multiplicacion = valor_1 * valor_2 * valor_3
# Division
division = valor_1 / valor_2 / valor_3
# Division entera
modulo = valor_1 % valor_2
# Area de un circulo
area_circulo = 3.1416 * (valor_1 ** 2)


# Operadores de comparacion
temperatura  = 75
temperatura_max = 80

if temperatura > temperatura_max:
    print("La temperatura es mayor a la maxima")



# Operadores logicos    
nivel_bateria = 50
nivel_carga = 80

if nivel_bateria < 20 and nivel_carga > 50:
    print("La bateria esta baja y la carga es alta")



# Operadores a nivel de bits
mascara_bits_binario = 0b1111
mascara_bits_hexadecimal = 0x0F
mascara_bits_decimal = 15
mascara_bits_octal = 0o17

registro_de_control = 0b10101010
registro_de_control = registro_de_control | mascara_bits_binario

# Cambio de un bit 
print(bin(registro_de_control))
print(int(mascara_bits_binario))
print(hex(mascara_bits_hexadecimal))