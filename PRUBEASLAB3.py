# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:03:30 2021

@author: Manuel Gómez López
"""
import random as ran
import copy

sopa=[]
for i in range(10):
    sopa.append([])
    for j in range(11):
        sopa[i].append('*')
        
for i in range(10):
    for j in range(11):
        print(sopa[i][j], end=' ')
    print('')

s2=copy.deepcopy(sopa)
palabra={'GATO':[0,0],'SIRVIENTE':[0,0],'AZUL':[0,0],'ROJO':[0,0]}
posicion_inicial=[]
posicion_inicial.append(ran.randrange(1,10,1))
posicion_inicial.append(ran.randrange(1,11,1))
print(posicion_inicial)
direccion_1='abajo'
direccion_2='arriba'
direccion_3='derecha'
direccion_4='izquierda'
# if direccion_1=='abajo':
#     if posicion_inicial[1]+len(i)<=10:
#         posicion_actual=posicion_inicial
#         error=False
#         for caracter in i:
#             if s2[posicion_actual[0]][posicion_actual[1]]=='*' \
#                 or s2[posicion_actual[0]][posicion_actual[1]]==caracter:
#                 s2[posicion_actual[0]][posicion_actual[1]]=caracter
#                 posicion_actual[0]+=1
#             else:
#                 error=True
#         if not error:
#             sopa=s2

              
        
posiciones=['arriba','abajo','derecha','izquierda', 'diagonal_abajo_derecha','diagonal_abajo_izquierda','diagonal_arriba_derecha','diagonal_arriba_izquierda']
posicion_inicial=[ran.randrange(1,10,1),ran.randrange(1,11,1)]
# palabra='GATUBE'
for i in palabra:
    palabra[i]=[ran.randrange(1,10,1),ran.randrange(1,11,1)]
    if direccion_1=='abajo':
        if posicion_inicial[0]+len(palabra)<=10 and posicion_inicial[1]+len(palabra)<=11:
            posicion_actual=posicion_inicial
            error=False
            for caracter in palabra:
                if s2[posicion_actual[0]][posicion_actual[1]]=='*' \
                    or s2[posicion_actual[0]][posicion_actual[1]]==caracter:
                        s2[posicion_actual[0]][posicion_actual[1]]=caracter
                        # posicion_actual[1]+=1
                        posicion_actual[0]+=1
                else:
                    error=True
            if not error:
                sopa=s2
print(palabra)
# for i in palabra:
#     # ran.choice(posiciones)
#     print(ran.choice(posiciones))
#     if direccion_1=='abajo':
#         if posicion_inicial[1]+len(i)<=10:
#             posicion_actual=posicion_inicial
#             error=False
#             palabra_temporal=i
#             for caracter in palabra_temporal:
#                 if s2[posicion_actual[0]][posicion_actual[1]]=='*' or s2[posicion_actual[0]][posicion_actual[1]]==caracter:
#                     s2[posicion_actual[0]][posicion_actual[1]]=caracter
#                     posicion_actual[0]+=1
#                 else:
#                     error=True
#             if not error:
#                 sopa=s2

# dicc_prueba={'pene':[1,5], 'culo':[4,9],'dianexybonita':[10,10]}
# for x,y in  dicc_prueba.items():
#     print(str(y))
#     for z in y:
#         print(str(z))

for i in range(10):
    for j in range(11):
        print(sopa[i][j], end=' ')
    print('')
