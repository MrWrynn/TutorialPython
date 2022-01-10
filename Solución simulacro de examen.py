# 1. Escriba una funcioon recursiva en pila llamada diferencia, que reciba dos numeros enteros y obtenga como
# resultado dos numeros, el primero compuesto por los digitos del primer numero que no pertenecen al segundo
# numero y el segundo formado por los elementos del segundo numero que no pertenecen al primer numero.
def diferencia(num1, num2):
	if num1 == num2:
		return 0, 0
	else:
		return int(diferencia_num1(num1, num2)), int(diferencia_num2(num2, num1))


def diferencia_num1(num_original, resta):
	if num_original == 0:
		return ""
	if str(num_original % 10) in list(str(resta)):
		return diferencia_num1(num_original // 10, resta)
	else:
		return diferencia_num1(num_original // 10, resta) + str(num_original % 10)


def diferencia_num2(num_original, resta):
	if num_original == 0:
		return ""
	if str(num_original % 10) in list(str(resta)):
		return diferencia_num1(num_original // 10, resta)
	else:
		return diferencia_num1(num_original // 10, resta) + str(num_original % 10)


# 2. Escriba una funcion recursiva en pila que reste un digito especico a todos los digitos de otro numero.
# si la resta es negativa se debe colocar un cero.
def restard(dig, num):
	if num == 0:
		return ""
	if num % 10 - dig > 0:
		return restard(dig, num // 10) + str(num % 10 - dig)
	else:
		return restard(dig, num // 10) + "0"


# 3. Escribir una funcion recursiva, denominada contar(lista), que reciba como argumento una lista compuesta por
# elementos y sublistas y obtenga como resultado la cantidad de todos los elementos de la lista y de todas sus
# sublistas.
def contar(lista):
	if len(lista)==0:
		return 0
	return sub_dividir(lista)

def sub_dividir(lista):
	if len(lista)==0:
		return 0
	if type(lista[0])==list:
		# Sumamos los elementos de lista[0] al final
		lista=lista+lista[0]
		# Eliminamos el primer elemento (que era una lista) porque ya añadimos sus elementos al final de la lista
		lista=lista[1:]
		return sub_dividir(lista)
	else:
		return 1+sub_dividir(lista[1:])
