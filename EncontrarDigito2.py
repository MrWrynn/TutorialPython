# Descripción: se requiere determinar si un digito dado se encuentra en un
# numero entero positivo
# Restricciones: ambos numeros tienen que ser enteros positivos y el digito no
# ser mayor a 9
# Entradas: un digito y un número entero positivo
# Salida: verdadero (1) si el digito aparece, falso (0) si el numero no aparece

def validar(num, dig):
    if (type(num) == int) and (type(dig == int) and (num >= 0) and (dig >= 0) and (dig <= 9)):
        return buscarDigito(num, dig)
    else: return "Error"

def buscarDigito(num, dig):
    if(num == 0):
        return 0
    elif ((num % 10) == dig):
          return 1
    else: return buscarDigito(num // 10, dig)
