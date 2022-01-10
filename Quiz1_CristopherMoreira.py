#Quiz 1 Recursividad de cola | Introducción a la programación
#Cristopher Moreira Quirós | Carné: 2021095902


#Problema 1
#Escriba una funci´on (en recursividad de cola) llamada frecuencias(lista) que reciba una
#lista que contenga valores entre 0 y n − 1 (asuma que la lista est´a correcta), donde n es el
#tama˜no de la lista, y obtenga otra lista que indique en cada una de las posiciones la cantidad
#de veces que apareci´o ese d´ıgito (el que indica la posici´on) en la lista de entrada.
#   >>> frecuencias([1, 1, 2, 1, 4])
#   [0, 3, 1, 0, 1]
#Note que 0 aparece 0 veces, 1 aparece 3 veces, 2 aparece 1 vez, 3 aparece 0 veces, y 4 aparece 1 vez.
#   >>> frecuencias([1, 0, 2, 3, 5, 4])
#   [1, 1, 1, 1, 1, 1]

def frecuencias(lista):
    if isinstance(lista, list):
        return frecuencias_aux(lista, [], 0)
    else:
        return "ERROR"

def frecuencias_aux(lista, resultado, pos):
    rep = [contar_frecuencias(lista, 0, pos, 0)]
    if pos > len(lista)-1:
        return resultado
    else:
        return frecuencias_aux(lista, resultado + rep, pos + 1)

def contar_frecuencias(lista, resultado, pos, n):
    if n== len(lista):
        return resultado
    else:
        if lista[n] == pos:
            return contar_frecuencias(lista, resultado + 1, pos, n+1)
        else:
            return contar_frecuencias(lista, resultado, pos, n+1)

print(frecuencias([1,1,2,1,4]))


#Problema 2
#Escriba una funci´on en recursividad de cola llamada cambia(num), que reciba un n´umero
#entero y cambie los d´ıgitos que sean divisibles entre 4, por un cero.
#   >>> cambia(1488)
#   1000
#   >>> cambia(72571)
#   72571
def combina(num):
    if isinstance(num, int):
        return combina_aux(num, 0, 0)
    else:
        return "El número no es un entero."

def combina_aux(num, resultado, exp):
    digito=num%10
    if num == 0:
        return resultado
    elif digito%4 == 0:
        return combina_aux(num // 10, resultado + 0*(10**exp), exp+1)
    else:
        return combina_aux(num // 10, resultado + digito*(10**exp), exp + 1)

print(combina(1488))