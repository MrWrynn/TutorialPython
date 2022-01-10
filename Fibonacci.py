def fib(n):
    if (type(n == int) and (n >= 0)):
        return fibo(n)
    else: return "ERROR"

def fibo(n):
    if n < 2:
        return n
    else: return fib(n-1) + fib(n-2)
                                     
        
