import math
# Area de Círculo
# Funcion que calcula el area del circulo
#entrada: radio
#salida: area
def area(radio):
    if(type(radio) == int):
        if (radio > 0):
            return radio ** 2 * math.pi
        else:
            return "Error: el valor ingresado no es mayor a cero"
    else: return "Error: el tipo no es un valor entero."
