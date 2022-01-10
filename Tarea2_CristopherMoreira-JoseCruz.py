#Tarea 2 de Introducción a la programación
#Cristopher Eduardo Moreira Quirós | Carné:2021055902
#Jose Eduardo Cruz Vargas | Carné:2021050675

#Ejercicio 1
def lista_split(num):
    if (isinstance(num, int)):
        return lista_split_aux(num, [], [])
    else:
        print("El numero deber ser entero")

def lista_split_aux(num, lista_0_4, lista_0_5):
    lista_0_4.sort()
    lista_0_5.sort()
    if (num==0):
        return lista_0_4, lista_0_5
    else:
        digito=num%10

        if (digito <= 4):
            lista_0_4.append(digito)
        else:
            lista_0_5.append(digito)

        return lista_split_aux(num//10, lista_0_4, lista_0_5)


print(lista_split(1023456789))

#Ejercicio 2
def splitColaAux(lista,result):
    if 0 in lista:
        partir = lista.index(0)
        result += [lista[:partir]]
        lista = lista[partir + 1:]
        return splitColaAux(lista, result)
    else: return result + [lista]

def splitCola(lista):
    if isinstance(lista,list):
        print(splitColaAux(lista,[]))
    else: print("error")
splitCola( [2,0,46,78,9,0,87,65])


#Ejercicio 3

def cambie_todos(num):
    if isinstance(num, int):
        rep=crear_lista(num, [])
        return cambie_todos_aux(num,0,rep,0)
    else:
        return "Error"

def crear_lista(num, lista):
    if num==0:
        return repetidos(lista)
    else:
        dig=num%10
        return crear_lista(num//10,[dig] + lista)

def repetidos(lista):
    listarepetidos=[]
    for i in range(1,10):
        if lista.count(i)>1:
            listarepetidos.append(i)
    return listarepetidos

def cambie_todos_aux(num,exponente,rep,resultado):
    dig = num%10
    if num !=0:
        if dig in rep:
            valorA=dig*0
            return cambie_todos_aux(num//10,exponente+1,rep,resultado+valorA)
        else:
            valorB=dig*(10**exponente)
            return cambie_todos_aux(num//10,exponente+1,rep,resultado+valorB)
    else:
        return resultado


print(cambie_todos(1223445))


#Ejercicio 4
def sumalistacola(lista,result):
    if lista == []:
        return result
    else:
        result += lista[0]
        del lista[0]
        return sumalistacola(lista,result)

def coincideColaAux(lista,result):
    if lista==[]:
        return result
    else:
        if lista[-1]==sumalistacola(lista[0:len(lista)-1],0):
            result +=1
        else: result = result
        del lista[-1]
        return coincideColaAux(lista,result)
def coincideCola(lista):
    if isinstance(lista,list):
        if coincideColaAux(lista,0) > 0:
            print("coincide")
        else: print("no coincide")
    else: print("error")
coincideCola([2,4,3,9,14])


#Ejercico 5

def divida(dig, num):
    if (isinstance(dig, int) and isinstance(num, int)):
        return divida_aux(dig, num, 0, 0, 0, 0)
    else:
        print("El numero deber ser entero")


def divida_aux(dig, num, nMenores, nMayores, resultadoMenor, resultadoMayor):
    if (num == 0):
        return resultadoMenor, resultadoMayor
    else:
        digito = num % 10
        if (digito <= dig):
            resultadoMenor = resultadoMenor + digito * 10 ** nMenores
            nMenores = nMenores + 1
        else:
            resultadoMayor = resultadoMayor + digito * 10 ** nMayores
            nMayores = nMayores + 1

        return divida_aux(dig, num // 10, nMenores, nMayores, resultadoMenor, resultadoMayor)


print(divida(5, 123456789))


#Ejercicio 6
def SumatoriaAux(maxValue,n,result):
    if n > maxValue:
        return result
    else:
        result+= 2*(n**3)+3*(n**2)+1
        return SumatoriaAux(maxValue,n+1,result)
def SumatoriaCola(MaxValue):
    if isinstance(MaxValue,int) and MaxValue>0:
        print(SumatoriaAux(MaxValue,1,0))
    else: print("error")
SumatoriaCola(8)
