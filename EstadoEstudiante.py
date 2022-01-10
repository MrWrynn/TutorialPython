# Determinar si un estudiante se encuentra aprobado, aplazado o reprobado
# Función que determina el estado de un estudiante
# Entradas: nota
# Salidas: estado
# Restricciones: nota entre 0 y 10
def estado(nota):
        if ((nota >= 0) and (nota <= 100)):
                if (nota >= 70):
                        return "Aprobado"
                if (nota < 60):
                        return "Reprobado"
                if ((nota >= 60) and (nota < 70)):
                        return "Aplazado"
        else:
            return "La nota no esta dentro de los parametros aceptados"
                
