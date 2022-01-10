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

def prueba(num,lista):
    if num in lista:
        print("True")

    else:
        print("False")

lista=[1,2,3,4,5,6]

prueba(5,lista)

