# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:49:13 2021

@author: Usuario
"""
def data(tipo_dato,mensaje):
    val_a = False
    while not val_a:
        dato = input(mensaje)
        if tipo_dato == "int":
            try:
                dato = int(dato)
                val_a = True
            except ValueError:
                print("El valor introducido no corresponde a un entero")
                val_a = False
                continue
        elif tipo_dato == "bateria":
            try:
                dato = float(dato)
            except ValueError:
                print("El valor introducido no corresponde a un numero real")
                val_a = False
                continue
        elif tipo_dato == "menu":
            try:
                dato = int(dato)
                if 1 <= dato <= 3:
                    val_a = True
                else:
                    print("El valor introducido no es una opcion establecido, intentelo nuevamente")
                    val_a = False
                    continue
            except ValueError:
                print("El valor introducido no corresponde a un numero real")
                val_a = False
                continue               
        elif tipo_dato == "code":
            try:
                dato = str(dato)
                val_a = True
            except ValueError:
                print("El valor introducido no corresponde a una cadena de texto")
                val_a = False
                continue    
        elif tipo_dato == "llave":
            try:
                dato = int(dato)
                if 0 <= dato <= 27:
                    val_a = True
                else:
                    print("El valor introducido se sale de los parametros, intentelo nuevamente")
                    val_a = False
                    continue
            except ValueError:
                print("El valor introducido no corresponde a un numero real")
                val_a = False
                continue                   

    return dato

val_asig = False
while not val_asig :
    print("Bienvenido al sistema codificacion")
    print("Digite el numero 1 para codificar el mensaje")
    print("Digite el numero 2 para decodificar el mensaje")
    print("Digita el numero 3 para salir del programa")
    val_menu = input("Introduzca el numero para acceder a la opcion de interes: ")
    try:
        val_menu = int(val_menu)
    except:
        print("El valor introducido no es valido, vuelva a intentarlo ")
        val_asig = False
    else:
        if val_menu > 3 or val_menu < 1:
            print("El numero ingresado no corresponde a ninguna opcion valida, intentelo nuevamente")
        else:
            val_asig = True
    if val_menu == 1:
        new_code = "QWERTYUIOPASDFGHJKLÑZXCVBNMQWERTYUIOPASDFGHJKLÑZXCVBNMqwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnm"
        men = data("code", "Digite el mensaje a codificar: ")
        lla = data("llave", "Ingrese la llave deseada, debe ser un valor entre 0 y 27 : ")
        for i in men:
            if i == " ":
                i = " "
            else:
                pos_i = new_code.find(i)
                cam_letra = new_code[pos_i + lla]
                men = men.replace(i, cam_letra)
        men = men.upper()
        print("Su mensaje ya codificado es: ", men)
        val_asig = False
    elif val_menu == 2:
        
        codi = data("code", "digite el codigo a decodificar: ")
    
    elif val_menu == 3:
        print("Ha sido un gusto servirle")
        val_asig = True
        
                