"""
Clase cuenta: para manejar los datos de una cuenta de banco
Atributos:
-cedula: string
-nombre: string
-salo: real
Metodos:
-get_saldo()
-get_cedula()
-hacerDebito(monto)
e: monto a debitar
s: saldo actualizado o un mensaje de error
r: monto > 0
-hacerCredito(monto)
e: monto a creditar
s: saldo actualizado o un mensaje de error
r: monto > 0
"""

class Cuenta:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.saldo = 0
    def get_saldo(self):
        return self.saldo
    def get_cedula(self):
        return self.cedula
    def get_nombre(self):
        return self.nombre
    def hacerDebito(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
        else:
            return "ERROR"
    def hacerCredito(self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            return "ERROR"
