# Convertir de celsius a Farenheit
# Entrada: Grados Celsius
# Salida: Grados Farenheit
# Restricciones: números enteros o flotantes

def celsius_farenheit(celsius):
    if(type(celsius) == int or type(celsius) == float):
        # Invoca la función que calcula la conversión y regresa el resultado
        return calcular(celsius)
    else: return "Error: la entrada no es un entero o un flotante"

def calcular(celsius):
    return 9 / 5 * celsius + 32


def farenheit_celsius(farenheit):
    return (farenheit - 32) / 1.8


# Hacer una función que calcule la conversión de Farenheit a celsius y viceversa
# al indicar lo que se quiere calcular.

