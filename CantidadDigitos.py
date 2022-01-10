# Descripción: función que cuente los digitos de un número dado
# Entrada: un número entero positivo
# Salida: la cantidad de digitos del número
# Restricciones: tiene que ser un entero positivo

def digitos(n):
    if (type(n == int) and (n >= 0)):
        return can_digitos(n)
    else: print("El digito introducido no es entero o mayor a 0.")

def can_digitos(n):
    if (n < 1):
        return 0                                                               
    else: return 1 + can_digitos(n // 10)
