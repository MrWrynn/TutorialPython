def pares(n):
    if((n >= 0) and type(n == int)):
        return contar(n)
    else: return "ERROR"
def contar(n):
    if n == 0:
        return 0
    elif (n % 2) == 0:
        return 1 + contar(n //10)
    else:
        return contar(n // 10)
