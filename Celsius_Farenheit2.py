# Función que convierte celsius a farenheit y viceversa
def conversion_temperatura():
    conversion = float(input("Escriba 1 si quiere pasar a celsius y 2 si quiere pasar a farenheit: "))
    if conversion == 1:
        temperatura = float(input("Digite la temperatura a convertir: "))
        operacion = (temperatura - 32) * 5/9
        print (operacion)
    if conversion == 2:
        temperatura = float(input("Digite la temperatura a convertir: "))
        operacion = (temperatura * 9/5) + 32 
        print (operacion)
    else: return "Error"



        
    


    
