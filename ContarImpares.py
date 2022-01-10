# Descripcion: se requiere determinar cuantos digitos imapres tiene un numero
# Restricciones: el número es un entero positivo mayor a 0
# Entradas: un número
# Salida: cantidad de numeros impares.

def impares(n):
    if (type(n == int) and (n > 0)):
        return contar(n)
    else: return "ERRROR"

def contar(n):
    if n == 0:
        return 0
    elif ((n % 2) != 0):
        return 1 + contar(n // 10)
    else:
        return contar(n // 10)
    
