# Descripción: formar un nuevo número con los digitos pares de otro número.
# Restricciones: el número es un entero positivo.
# Entrada: un número
# Salida: un número formado por los digitos pares de otro número

def formar(n):
    if (type(n == int) and (n > 0)):
        return nuevo(n,0)
    else: return "ERROR"

def nuevo(n, pot):
    if n == 0:
        return 0
    elif (n % 2) == 0:
        return (n % 10) * (10**pot) + nuevo(n // 10, pot+1)
    else: return nuevo(n // 10, pot)
    
    
