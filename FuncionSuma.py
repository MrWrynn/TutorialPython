# Hacer una función que reciba un entero positivo de exactamente 3 dígitos
# y suma el valor de los digitos
# Entradas: numero
# Salida: suma
# Restricciones: numero >= 0, numero tiene al menos tres digitos
def suma(numero):
    if ((numero >= 100) and (numero <= 999)):
        unidad = numero %10
        diez = (numero // 10) %10
        cien = numero // 100
        return cien + diez + unidad
    else:
        return "Error"
