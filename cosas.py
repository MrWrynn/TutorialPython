prueba=[2,0,46,78,9,0,87,65]
def split(lista):
    if 0 in lista:
        regreso=lista[0:lista.index(0)]
        del lista[0:lista.index(0)+1]
        return (regreso,split(lista))
    else:
        return lista
#print(split(prueba))
####

def cambiatodos(num):
    if isinstance(num,int) and num > 0:
        rep=repetidos(num)
        print(cambiatodosaux(num,0,rep))
    else: print("error")

def contador(num,comparador):
    suma=0
    dig = num%10
    if num !=0:
        if dig == comparador:
            return 1 + contador(num//10,comparador)
        else:
            return contador(num//10,comparador)
    else:
        return 0

def repetidos(num):
    listarepetidos=[]
    for i in range(1,10):
        if contador(num,i) > 1:
            listarepetidos.append(i)
    return listarepetidos


def cambiatodosaux(num,exponente,rep):
    dig = num%10
    if num !=0:
        if dig in rep:
            return (dig*0) + cambiatodosaux(num//10,exponente+1,rep)
        else:
            return dig*(10**exponente)+ cambiatodosaux(num//10,exponente+1,rep)
    else: return 0

cambiatodos(13365439925)

# función coincide lista

listacoincide=[2,4,3,9,14]

def sumalista(lista):
    if lista == []:
        return 0
    else:
        valor = lista[0]
        del lista[0]
        return valor + sumalista(lista)

def coincideaux(lista):
    i=0
    if lista != []:
        if lista[-1] == sumalista(lista[0:(len(lista)-1)]):
            i=i+1
        else: i=i
        del lista[-1]
        return coincideaux(lista)+i
    else:
        return 0

def coincide(lista):
    if coincideaux(lista)==0:
        print("no coincide")
    else:
        print("coincide")

coincide(listacoincide)
#ejercicio 6

def naturalaux(lista,i):
    if len(lista) > i:
        if lista[i-1] > lista[i]:
            nuevalista=lista[0:i]
            del lista[0:i]
            i=1
            return [nuevalista] + naturalaux(lista,i)
        else:
            i=i+1
            return naturalaux(lista,i)
    else: return [lista]
listanatural=[3,4,5,1,2,3,4,7,3,2,1,6,7,9,0,10,32]

def natural(lista):
    listaaimprimir=naturalaux(lista,1)
    print(listaaimprimir)
#natural(listanatural)

#ejercicio 7
matriz=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

#for i in matriz[0]:
   # prueba.append(i)
#print(prueba)

def laterales(matriz):
    bordederecho=[]
    bordeizquierdo=[]
    for i in matriz[0]:
        bordeizquierdo.append(i)
    for i in matriz[-1]:
        bordederecho.append(i)
    return bordeizquierdo + bordederecho

def superiorinferior(matriz):
    if len(matriz) > 2:
        elementosuperior=matriz[1][0]
        elementoinferior=matriz[1][-1]
        del matriz[1]
        return [elementosuperior]+[elementoinferior]+superiorinferior(matriz)
    else: return []



def borde(matriz):
    listaborde=(laterales(matriz)+superiorinferior(matriz))
    print(listaborde)
#borde(matriz)

#8

def mayor(num,dig,expomayor):
    if num==0:
        return 0
    else:
        if num%10 >= dig:
           return (num%10)*(10**expomayor)+mayor(num//10,dig,expomayor+1)
        else:
            return mayor(num // 10, dig, expomayor)

def menor(num,dig,expomenor):
    if num==0:
        return 0
    else:
        if dig>(num%10):
           return (num%10)*(10**expomenor)+menor(num//10,dig,expomenor+1)
        else:
            return menor(num // 10, dig, expomenor)

def divida(num,dig):
    if isinstance(num,int) and num>0 and isinstance(dig,int) and dig>0:
        print(menor(num,dig,0))
        print(mayor(num,dig,0))
    else: print("error")
#divida(113355887,5)

#ejercico 9

def sumatoriaaux(MaxValue,n):
    if MaxValue >= n:
        return (2*n+n**(1/2))/(n**3+n**(1/2)) + sumatoriaaux(MaxValue,(n+1))
    else: return 0

def Sumatoria(MaxValue):
    if isinstance(MaxValue,int):
        print(sumatoriaaux(MaxValue,1))
    else: print("error")
#Sumatoria(5)

#ejercico 10
def TriangularSuperiorAux(matriz,j):
    if len(matriz) == 1:
        return 0
    else:
         if matriz[1][:j].count(0)!=j:
            del matriz[1]
            return 1+TriangularSuperiorAux(matriz,j+1)
         else:
            del matriz[1]
            return TriangularSuperiorAux(matriz,j+1)

def TriangularSuperior(matriz):
    i=0
    for a in range(0,len(matriz)):
        if matriz[0]== [] or len(matriz) > len(matriz[a]):
            i=i+1
    if i != 0:
        print("error")
    else:
        if TriangularSuperiorAux(matriz,1) == 0:
                print("true")
        else: print("false")

matriztriangular=[[1,9,8,2], [0,0,2,5],[0,0,0,6],[0,0,0,1]]
#TriangularSuperior(matriztriangular)

#fibonacci

def fibonacciaux(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciaux(n-1) + fibonacciaux(n-2)

def fibonacci(n):
    if n >=0:
        print(fibonacciaux(n))
    else:
        print("error")

#fibonacci(9)

#12

def NumAux(num,i):
     if 100>=i:
         for j in range(1,102):
             if i*j == num:
                 pareja=[i,j]
                 return [pareja] + NumAux(num,i+1)
             elif j > 100:
                 return NumAux(num,i+1)
     else:
         return []
def multi(num):
    if isinstance(num,int) and num > 0:
        lista=NumAux(num,1)
        inicio=((len(lista)//2))
        final=len(lista)
        if len(lista)%2 ==0:
            del lista[inicio:final]
        else:
            del lista[inicio+1:final]
        print(lista)
    else: print("error")

multi(120)
