import math as m
import tkinter as tk
def CalcularArea():
        area = 0
        valor = input("Ingrese el valor del radio: ")
        radio = int(valor)
        if radio > 0:
            area = (radio ** 2) * m.pi
            print("El valor del área es: ", area)
        else:
            print("El valor del radio no es mayor a cero.")
