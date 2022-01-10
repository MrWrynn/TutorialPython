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
#splitCola( [2,0,46,78,9,0,87,65])

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
#coincideCola([2,4,3,9,14])

#6
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
#SumatoriaCola(8)
