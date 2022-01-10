# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:00:49 2021

@author: Usuario
"""
import random as ran
import copy
import time

lista_palabra=[]
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
            lista_palabra.append(dato)
            dato_false=True
    return dato

# lista_palabras=[]
for b in range(2):
    palabra_sopa=datos('str','Ingrese la palabra '+str(b+1)+' para la sopa de letras: ')
    time.sleep(0.7)

# lista_palabra_y_orden={}
# for b in range(5):
#     palabra_sopa=input('Ingrese la palabra '+str(b+1)+' para la sopa de letras: ')
#     lista_palabra_y_orden[palabra_sopa]=[0,0]
# print(lista_palabra_y_orden)
orden_palabra=[]    

time.sleep(0.7) 
fila_ancho=datos('int', 'Ingrese la cantidad de filas que desea en la sopa de letras. ')
time.sleep(0.7)
columna_alto=datos('int','Ingrese la cantidad de columnas que desea en la sopa de letras. ')



sopa=[]

for i in range(columna_alto):
    sopa.append([])
    for j in range(fila_ancho):
        sopa[i].append('*')

s2=copy.deepcopy(sopa)

posiciones=['arriba','abajo','derecha','izquierda', 'diagonal_abajo_derecha','diagonal_abajo_izquierda','diagonal_arriba_derecha','diagonal_arriba_izquierda']
g=0
for j in lista_palabra:    
    # posicion_random=[]
    tamano_falso=False
    while not tamano_falso:
        if len(j)<=fila_ancho and len(j)<=columna_alto:
            numero_1=int(fila_ancho)
            numero_2=int(columna_alto)
            orden_palabra.append(ran.randrange(1,numero_1,1))
            orden_palabra.append(ran.randrange(1,numero_2,1))
            tamano_falso=True            
            posicion_valida=False
            while not posicion_valida:
                direccion_palabra=ran.choice(posiciones)
                try:
                    if direccion_palabra=='abajo':
                        if orden_palabra[g]+len(j)<=numero_1 and orden_palabra[g+1]+len(j)<=numero_2:
                            # posicion_actual=posicion_inicial
                            error=False
                            for caracter in j:
                                if s2[orden_palabra[g]][orden_palabra[g+1]]=='*' \
                                    or s2[orden_palabra[g]][orden_palabra[g+1]]==caracter:
                                        s2[orden_palabra[g]][orden_palabra[g+1]]=caracter
                                        # posicion_actual[1]+=1
                                        orden_palabra[g]+=1
                                        posicion_valida=True
                                        
                                else:
                                    error=True
                                    posicion_valida=False
                            if not error:
                                sopa=s2
                                posicion_valida=True
                                g=g+2
                except:
                    posicion_valida=False
                try:
                    if direccion_palabra=='arriba':
                        if orden_palabra[g]+len(j)<=numero_1 and orden_palabra[g+1]+len(j)<=numero_2:
                            # posicion_actual=posicion_inicial
                            error=False
                            for caracter in j:
                                if s2[orden_palabra[g]][orden_palabra[g+1]]=='*' \
                                    or s2[orden_palabra[g]][orden_palabra[g+1]]==caracter:
                                        s2[orden_palabra[g]][orden_palabra[g+1]]=caracter
                                        # posicion_actual[1]+=1
                                        orden_palabra[g]-=1
                                        posicion_valida=True
                                else:
                                    error=True
                                    posicion_valida=False
                            if not error:
                                sopa=s2
                                posicion_valida=True
                                g=g+2
                except:
                    posicion_valida=False
                try:
                    if direccion_palabra=='derecha':
                        if orden_palabra[g]+len(j)<=numero_1 and orden_palabra[g+1]+len(j)<=numero_2:
                            # posicion_actual=posicion_inicial
                            error=False
                            for caracter in j:
                                if s2[orden_palabra[b]][orden_palabra[b+1]]=='*' \
                                    or s2[orden_palabra[b]][orden_palabra[b+1]]==caracter:
                                        s2[orden_palabra[b]][orden_palabra[b+1]]=caracter
                                        # posicion_actual[1]+=1
                                        orden_palabra[b+1]+=1
                                        posicion_valida=True
                                else:
                                    error=True
                                    posicion_valida=False
                            if not error:
                                sopa=s2
                                posicion_valida=True
                                g=g+2
                except:
                    posicion_valida=False
                try:
                    if direccion_palabra=='izquierda':
                        if orden_palabra[g]+len(j)<=numero_1 and orden_palabra[g+1]+len(j)<=numero_2:
                            # posicion_actual=posicion_inicial
                            error=False
                            for caracter in j:
                                if s2[orden_palabra[g]][orden_palabra[g+1]]=='*' \
                                    or s2[orden_palabra[g]][orden_palabra[g+1]]==caracter:
                                        s2[orden_palabra[g]][orden_palabra[g+1]]=caracter
                                        # posicion_actual[1]+=1
                                        orden_palabra[g+1]-=1
                                        posicion_valida=True
                                else:
                                    error=True
                                    posicion_valida=False
                            if not error:
                                sopa=s2
                                posicion_valida=True
                                g=g+2
                except:
                    posicion_valida=False
                try:
                    if direccion_palabra=='diagonal_abajo_derecha':
                        if orden_palabra[g]+len(j)<=numero_1 and orden_palabra[g+1]+len(j)<=numero_2:
                            # posicion_actual=posicion_inicial
                            error=False
                            for caracter in j:
                                if s2[orden_palabra[g]][orden_palabra[g+1]]=='*' \
                                    or s2[orden_palabra[g]][orden_palabra[g+1]]==caracter:
                                        s2[orden_palabra[g]][orden_palabra[g+1]]=caracter
                                        orden_palabra[g+1]+=1
                                        orden_palabra[g]+=1
                                        posicion_valida=True
                                else:
                                    error=True
                                    posicion_valida=False
                            if not error:
                                sopa=s2
                                posicion_valida=True
                                g=g+2
                except:
                    posicion_valida=False
                try:
                    if direccion_palabra=='diagonal_abajo_izquierda':
                        if orden_palabra[g]+len(j)<=numero_1 and orden_palabra[g+1]+len(j)<=numero_2:
                            # posicion_actual=posicion_inicial
                            error=False
                            for caracter in j:
                                if s2[orden_palabra[g]][orden_palabra[g+1]]=='*' \
                                    or s2[orden_palabra[g]][orden_palabra[g+1]]==caracter:
                                        s2[orden_palabra[g]][orden_palabra[g+1]]=caracter
                                        orden_palabra[g+1]-=1
                                        orden_palabra[g]+=1
                                        posicion_valida=True
                                else:
                                    error=True
                                    posicion_valida=False
                            if not error:
                                sopa=s2
                                posicion_valida=True
                                g=g+2
                except:
                    posicion_valida=False
                try:
                    if direccion_palabra=='diagonal_arriba_derecha':
                        if orden_palabra[g]+len(j)<=numero_1 and orden_palabra[g+1]+len(j)<=numero_2:
                            # posicion_actual=posicion_inicial
                            error=False
                            for caracter in j:
                                if s2[orden_palabra[g]][orden_palabra[g+1]]=='*' \
                                    or s2[orden_palabra[g]][orden_palabra[g+1]]==caracter:
                                        s2[orden_palabra[g]][orden_palabra[g+1]]=caracter
                                        orden_palabra[g+1]+=1
                                        orden_palabra[g]-=1
                                        posicion_valida=True
                                else:
                                    error=True
                                    posicion_valida=False
                            if not error:
                                sopa=s2
                                posicion_valida=True
                                g=g+2
                except:
                    posicion_valida=False
                try:
                    if direccion_palabra=='diagonal_arriba_izquierda':
                        if orden_palabra[g]+len(j)<=numero_1 and orden_palabra[g+1]+len(j)<=numero_2:
                            # posicion_actual=posicion_inicial
                            error=False
                            for caracter in j:
                                if s2[orden_palabra[g]][orden_palabra[g+1]]=='*' \
                                    or s2[orden_palabra[g]][orden_palabra[g+1]]==caracter:
                                        s2[orden_palabra[g]][orden_palabra[g+1]]=caracter
                                        orden_palabra[g+1]-=1
                                        orden_palabra[g]-=1
                                        posicion_valida=True
                                else:
                                    error=True
                                    posicion_valida=False
                            if not error:
                                sopa=s2
                                posicion_valida=True
                                g=g+2
                except:
                    posicion_valida=False
                posicion_valida=True
        elif len(j)>fila_ancho and len(j)>columna_alto:
            time.sleep(0.7) 
            fila_ancho=datos('int', 'Ingrese la cantidad de filas que desea en la sopa de letras nuevamente. ')
            time.sleep(0.7)
            columna_alto=datos('int','Ingrese la cantidad de columnas que desea en la sopa de letras nuevamente. ')
            tamano_falso=False
        # posicion_random.append(ran.randrange(0,numero_1,1))
        # posicion_random.append(ran.randrange(0,numero_2,1))
    # print(posicion_random)                       
print(lista_palabra)
print(orden_palabra)                      
s3=copy.deepcopy(s2)
# sopa=[]
# s2=copy.deepcopy(sopa)
# posiciones=['arriba','abajo','derecha','izquierda', 'diagonal_abajo_derecha','diagonal_abajo_izquierda','diagonal_arriba_derecha','diagonal_arriba_izquierda']
alfa=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(columna_alto):
    for j in range(fila_ancho):
        if sopa[i][j]=='*':
            letra=ran.choice(alfa)
            sopa[i][j]=letra
    print('')



        
for i in range(columna_alto):
    for j in range(fila_ancho):
        print(sopa[i][j], end=' ')
    print('')

print('')
for i in range(columna_alto):
    for j in range(fila_ancho):
        print(s3[i][j], end=' ')
    print('')


presionar=input('Presione enter si desea ver la solución. ')