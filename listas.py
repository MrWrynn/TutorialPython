def listanegativo(lista):
    for i in lista:
        if 0>i:
            cambio=lista.index(i)
            lista[cambio]=0
    print(lista)
entrada=[-3,-2,-1,1,2,3,4]
listanegativo(entrada)


def listadeimpares(listatotal):
   listaimpares=[]
   for i in listatotal:
        if i%2!=0:
            listaimpares.append(i)
   print(listatotal)
   print(listaimpares)

entrada=list(range(11))
listadeimpares(entrada)

def primo(num):
    suma=0
    for i in range(2,num):
        if num%i ==0:
            suma=suma+1
        else:
            suma=suma+0
    if suma==0:
        return num

def listadeprimos(num):
    lista=list(range(num+1))
    listaprimos=[]
    a=0
    for i in lista:
        listaprimos.append(primo(i))
    print(listaprimos)
listadeprimos(100)

matriz1=[[10,20,30],[0,0,0],[0,0,0]]


def matrizTriangularSuperior(matriz):
    del matriz [0][1]
    del matriz [0][1]
    del matriz [1][2]
    for i in matriz:
        for j in i:
            print(j,end="")
        print("")
matrizTriangularSuperior(matriz1)

def matrizTriangularInferior(matriz):
    del matriz [1][0]
    del matriz [2][0]
    del matriz [2][0]
    for i in matriz:
        for j in i:
            print(j,end="")
        print("")
matrizTriangularInferior(matriz1)

def matrizprima(matriz):
    suma1=(matriz[0][0])+(matriz[0][1])+(matriz[0][2])
    suma2 = (matriz[1][0]) + (matriz[1][1]) + (matriz[1][2])
    suma3 = (matriz[2][0]) + (matriz[2][1]) + (matriz[2][2])
    suma4 =(matriz[0][0])+(matriz[1][0])+(matriz[2][0])
    suma5 = (matriz[0][1]) + (matriz[1][1]) + (matriz[2][1])
    suma6 = (matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])
    if suma1==suma4:
        print("prima")
    elif suma1==suma5:
        print("prima")
    elif suma1==suma6:
        print("prima")
    elif suma2==suma4:
        print("prima")
    elif suma2==suma5:
        print("prima")
    elif suma2 == suma6:
        print("prima")
    elif suma3==suma4:
        print("prima")
    elif suma3==suma5:
        print("prima")
    elif suma3==suma6:
        print("prima")
    else:
        print("no prima")
matrizprima(matriz1)