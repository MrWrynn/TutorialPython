# Descripción: Se quiere contar la cantidad de veces que un número se repite en un numero dado
# Restricciones: El digito y el numero tienen que ser enteros postivios
# Entradas: un digito y un numero
# Salidas: la cantidad de veces que se repite el digito en el numero

def aparece(num, digito):
    if (type(num == int) and type(digito == 0) and (num >= 0) and (digito >= 0) and (digito <= 9)):
        return aparece_digito(num, digito)
    else:
        return "Error"

def aparece_digito(num, digito):
    if(num == 0):
        return 0
    elif ((num % 10) == digito):
        return 1 + aparece_digito(num // 10, digito)
    else:
        return aparece_digito(num // 10, digito)
