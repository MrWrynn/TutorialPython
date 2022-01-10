#

#Ejemplo 1
def multiplica(a, b):
    i=1

    #Ciclo exterior
    while i<=a:
        j=1
        #Ciclo interior
        while j<=b:
            print(i * j, "\t", end="")
            j+=1

        print("\n")
        i+=1


#multiplica(10,10)

def reconoce_negativo():
    while True:
        num = int(input("Introduzca un numero: "))

        if num < 0:
            print("El número es negativo. Fin del programa")
            break

#reconoce_negativo()

def factorial(num):
    resultado=1

    while num>=1:
        resultado=resultado*num
        num -= 1

    print("El resultado es: ",resultado)

#factorial(5)

def numeros_100():
    i=1
    while i<=100:
        j=1
        while j<=10:
            print(i, "\t", end="")
            j +=1
            i += 1
        print("\n")



#numeros_100()

def primos(a,b):
    while z




primos(2,12)