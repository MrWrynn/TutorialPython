#Ejercicio 5

def divida(dig, num):
    if (isinstance(dig, int) and isinstance(num, int)):
        return divida_aux(dig, num, 0, 0, 0, 0)
    else:
        print("El numero deber ser entero")

def divida_aux(dig, num, nMenores, nMayores, resultadoMenor, resultadoMayor):
    if (num==0):
        return resultadoMenor, resultadoMayor
    else:
        digito=num%10
        if (digito <= dig):
            resultadoMenor=resultadoMenor + digito*10**nMenores
            nMenores=nMenores+1
        else:
            resultadoMayor=resultadoMayor + digito*10**nMenores
            nMayores=nMayores+1

        return divida_aux(dig, num//10, nMenores, nMayores, resultadoMenor, resultadoMayor)

print(divida(5,12345678))


#Ejercicio 5
def divida(dig, num):
    if (isinstance(dig, int) and isinstance(num, int)):
        return divida_aux(dig, num, 0, 0, 0, 0)
    else:
        print("El numero deber ser entero")

def divida_aux(dig, num, nMenores, nMayores, resultadoMenor, resultadoMayor):
    if (num==0):
        return resultadoMenor, resultadoMayor
    else:
        digito=num%10
        if (digito <= dig):
            return divida_aux(dig, num // 10, nMenores + 1, nMayores, digito*10**nMenores + resultadoMenor, resultadoMayor)
        else:
            return divida_aux(dig, num//10, nMenores, nMayores+1, resultadoMenor, resultadoMayor + digito*10**nMayores)