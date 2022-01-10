# Cristopher Eduardo Moreira Quirós
#FUNCIONES

# Ejercicio 1:
#Cree una función en Python que permita calcular la raíz enésima de un número
#cualquiera. Reciba como entrada el índice y el radicando. Adicionalmente, restrinja
#los valores de entrada a valores válidos
print("Ejercio 1")

def raiz(indice, radicando):
	resultado = pow(radicando, 1 / indice)
	print("El resultado de la raíz es: ", resultado)


raiz(3, 2)

# Ejercicio 2
#Escriba una función en Python que calcule e imprima el promedio de tres números
#recibidos como argumentos.
print("")
print("Ejercicio 2")


def promedio_3(num_1, num_2, num_3):
	resultado = (num_1 + num_2 + num_3) / 3
	print(resultado)


promedio_3(10, 10, 10)

# Ejercicio 3
#Escriba una función que determine si un número es múltiplo de otro.
print("")
print("Ejercicio 3")


def multiplo(num_1, num_2):
	resultado = num_1 % num_2
	if resultado == 0:
		print("El ", num_2, " es multiplo de ", num_1)
	else:
		print("El ", num_2, " no es multiplo de ", num_1)


multiplo(10, 5)

# Ejercicio 4
#Escriba una función que permita calcular el área de un rectángulo y de un triángulo.
#debe recibir como parámetros la base, la altura y la figura a la que le va a calcular el
#área (rectángulo o triángulo).
print("")
print("Ejercicio 4")


def area(base, altura, figura):
	if figura == "triangulo":
		resultado = base * altura / 2
		print("El area del triangulo es: ", resultado)
	elif figura == "rectangulo":
		resultado = base * altura
		print("El area del rectangulo es: ", resultado)
	else:
		print("Esa figura no es ni un triangulo ni un rectangulo")


area(10, 2, "triangulo")

# Ejercicio 5
#Escriba una función que permita verificar si una palabra es palíndromo o no
print("")
print("Ejercicio 5")


def palindromo(palabra):
	if palabra == palabra[::-1]:
		print("La palabra es un palindromo")
	else:
		print("La palabra no es un palindromo")


palindromo("Ana")
palindromo("hola")

# Ejercicio 6
#Escriba una función que permita convertir de km/h a mph (millas por hora).
print("")
print("Ejercicio 6")


def conversion(rapidez):
	resultado = rapidez / 1.609
	print("Su rapidez es de: ", resultado, "mph")


conversion(100)

# Ejercicio 7
#Escriba una función que permita calcular multas de tránsito por exceso de velocidad,
#de acuerdo a las siguientes reglas:
#	○ Tendrá una multa de 100 000 si excede por más de 10km/h la velocidad máxima.
#	○ La multa será de 200 000 si excede por más de 20km/h la velocidad máxima.
#	○ Tendrá una multa de 300 000 si excede por más de 30km/h la velocidad máxima.
#La función debe recibir la velocidad máxima permitida por la carretera y la velocidad a la
#que circulaba el infractor.

print("")
print("Ejercicio 7")


def multa(vel_max, rapidez):
	exceso = rapidez - vel_max
	if exceso >= 10 and exceso < 20:
		print("Su multa es de 100 000 colones")
	elif exceso >= 20 and exceso < 30:
		print("Su multa es de 200 000 colones")
	elif exceso >= 30:
		print("Su multa es de 300 000 colones")
	else:
		print("Usted no tiene multa")


multa(60, 69)


# Ejercicio 8
#Hacer una función que reciba un número de exactamente 5 dígitos y los sume.
print("")
print("Ejercicio 8")


def suma_digitos(numero):
	num = str(numero)
	if len(num) == 5:
		suma = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4])
		print("La suma de los digitos es de: ", suma)
	else:
		print("El número no es de 5 digitos")


suma_digitos(22222)