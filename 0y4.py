# Descripción: Dado un numero entero, verifique que todos sus digitos se encuentre entre 0 y 4
# Restricciones: el número es un entero positivo
# Entrada: un númeor entero positivo.
# Salida: True si los dígitos del numeor se encuaentran entre 0 y 4, False so no se cumple la condición

def busqueda(n):
    if (type(n == int) and (n >= 0)):
        return operacion(n)
    else: return "ERROR"

def operacion(n):
    if n == 0:
        return True
    elif (n % 10) <= 4 and (n % 10) >= 0:               
        return operacion(n // 10)
    else: return False
    
