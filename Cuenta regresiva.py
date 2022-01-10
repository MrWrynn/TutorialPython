# Hacer una función que escriba los numeros desde i hasta 1 en forma descendente
# Entradas: Un numero cualquiera mayor a 1
# Salida: La sucesion de los numeros

def cuenta_regresiva(i):
    if (type(i == int) and (i >= 1)):
        return cuentaregresiva(i)
    else: print("El número no es un entero mayor o igual a 1.")

def cuentaregresiva(i):
    if (i < 1):
        return 0
    else:
        print(i)
        cuentaregresiva(i-1)
  
