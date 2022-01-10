import math as ma
def entrada_dato(tipo_dato, mensaje):
    dato_valido = False
    while not dato_valido:
        dato = input(mensaje)
        if tipo_dato == "int":
            try:
                dato = int(dato)
            except ValueError:
                print("Error leyendo el dato, inténtelo de nuevo.")
                continue
        elif tipo_dato == "float":
            try:
                dato = float(dato)
            except ValueError:
                print("Error leyendo el dato, inténtelo de nuevo.")
                continue
    return dato

def coeficientes_coordenadas(x1, x2, y1, y2):
    global a
    global b
    global c
    m = (y2-y1)/(x2-x1)
    n = (y1-(m*x1))
    a = -m*(x2-x1)
    b = (x2-x1)
    c = -n*(x2-x1)
    return a, b, c     

def distancia(a, b, c, x0, y0):
    dist = (abs(a*x0 + b*y0 + c)/ ma.sqrt(a*2 + b*2)) 
    dist = dist * 30.9
    return dist

def calcular_gan(dist, tipo_proyecto, costo_est):
    if tipo_proyecto == "residencial":
        ganancia = 20000000 + 2000000 * ma.e**(-dist / 450) - costo_est
    elif tipo_proyecto == "comercial":
        ganancia = 50000000 + 10000000 * ma.e**(-dist / 450) - costo_est
    return ganancia

x1 = entrada_dato("float","Ingrese la coordenada de longitud del punto 1: ")
x2 = entrada_dato("float", "Ingrese la coordenada de longitud del punto 2: ")
y1 = entrada_dato("float", "Ingrese la coordenada de latitud del punto 1: ")
y2 = entrada_dato("flaot", "Ingrese la coordenada de latitud del punto 2: ")