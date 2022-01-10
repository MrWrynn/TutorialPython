# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:14:31 2021

@author: Manuel Gómez López
"""

import random as ran
import copy
import time

lista_palabra_y_orden={}
def datos(tipo_dato,mensaje):
    dato_false=False
    while not dato_false:
        dato=input(mensaje)
        if tipo_dato=="int":
            try:
                dato=int(dato)
                dato_false=True
            except:
                print("Dato inválido, ingréselo nuevamente.")
                continue
        elif tipo_dato=="float":
            try:   
                dato=float(dato)
                dato_false=True
            except:
                print("Dato inválido, ingréselo nuevamente.")
                continue
        elif tipo_dato=='str':
            lista_palabra_y_orden[dato]=[0,0]
            dato_false=True
    return dato

# lista_palabras=[]
for b in range(5):
    palabra_sopa=datos('str','Ingrese la palabra '+str(b+1)+' para la sopa de letras: ')
    time.sleep(0.7)

# lista_palabra_y_orden={}
# for b in range(5):
#     palabra_sopa=input('Ingrese la palabra '+str(b+1)+' para la sopa de letras: ')
#     lista_palabra_y_orden[palabra_sopa]=[0,0]
# print(lista_palabra_y_orden)
    

time.sleep(0.7) 
fila_ancho=datos('int', 'Ingrese la cantidad de filas que desea en la sopa de letras. ')
time.sleep(0.7)
columna_alto=datos('int','Ingrese la cantidad de columnas que desea en la sopa de letras. ')


for j in lista_palabra_y_orden:    
    # posicion_random=[]
    tamano_falso=False
    while not tamano_falso:
        if len(j)<=fila_ancho and len(j)<=columna_alto:
            numero_1=int(fila_ancho)
            numero_2=int(columna_alto)
            lista_palabra_y_orden[j]=[ran.randrange(1,numero_1,1),ran.randrange(1,numero_2,1)]
            tamano_falso=True
        elif len(j)>fila_ancho and len(j)>columna_alto:
            time.sleep(0.7) 
            fila_ancho=datos('int', 'Ingrese la cantidad de filas que desea en la sopa de letras nuevamente. ')
            time.sleep(0.7)
            columna_alto=datos('int','Ingrese la cantidad de columnas que desea en la sopa de letras nuevamente. ')
            tamano_falso=False
        # posicion_random.append(ran.randrange(0,numero_1,1))
        # posicion_random.append(ran.randrange(0,numero_2,1))
    # print(posicion_random)                       
print(lista_palabra_y_orden)                      

sopa=[]
s2=copy.deepcopy(sopa)
posiciones=['arriba','abajo','derecha','izquierda', 'diagonal_abajo_derecha','diagonal_abajo_izquierda','diagonal_arriba_derecha','diagonal_arriba_izquierda']



for i in range(columna_alto):
    sopa.append([])
    for j in range(fila_ancho):
        sopa[i].append('*')
        
for i in range(columna_alto):
    for j in range(fila_ancho):
        print(sopa[i][j], end=' ')
    print('')
