# Función que suma los números del 1 hasta n, en donde n es cualquier numero
# entero mayor o igual a 1
# Restricciones: los números a sumar tienen que ser enteros
# Entrada: Número entero
# Salida: La suma de los numeros de 1 hasta n

def suma(numero):
    if (type(numero) == int) and (numero >= 1):
        return operacion(numero)
    else: print("El número no es entero o es menor que 1.")

def operacion(numero):
    if numero < 1: # condicion de parada
        return 0   # se ejecuta cuando se cumple la condicion de parada
    else: return numero + operacion(numero - 1)
