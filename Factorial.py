# Descripción: Función que calcula el valor de la multiplicación de un numero n hasta 1
# Restricciones: n tiene que ser un numero mayor o igual a 1
# Entrada: Un numero entero
# Salida: El factorial de un número dado

def factorial(n):
    if (type(n == int) and (n >= 1)):
        return (fact(n))
    else: print("El valor insertado no es un numero entero o mayor a 1.")

def fact(n):
    if n < 1:
        return 1
    else: return n * fact(n-1)
