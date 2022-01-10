# Descripción: Dada un numero n, sumarlo n veces elevado a la 2.
# Restriccón: n es un numero entero positivo.
# Entrada: un numero n
# Salida: la suma de n**2 n veces.

def sumatoria(n):
    if (type(n == 0) and (n >= 0)):
        return operacion(n, 0)
    else: return "ERROR"

def operacion(n, c):
    if c == n:
        return 0
    else: return (n**2) + operacion(n, c + 1)
    
     
    
    
