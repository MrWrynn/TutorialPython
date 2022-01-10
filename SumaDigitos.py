# Descripción: sumar los digitos de cualquier numero entero positivo
# Restriccion: el número es entero y positivo.
# Entrada: número entero positivo
# Salida: suma de los digitos del número

# Requisitos: programar la función de validacion (verifica las restricciones
# y la función para efectuar la suma de los dígitos).

def sum(n):
    if (type(n == int) and (n > 0)):
        return suma(n)
    else: print("El numero no es un entero o no es mayor a cero.")

def suma(n):
    if n < 1:
        return 0
    else:  return (n%10)+(suma(n // 10))                                                     

