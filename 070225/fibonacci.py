
# Duas funcoes com o mesmo proposito e diferentes abordagens

# a funcao fib(n) utiliza recursividade, 
# ao contrario da funcao fib_linear(n), que utiliza metodos lineares

def fib(numero: int):
    if numero < 0:
        print('Numero invalido')
    else:
        if numero == 0:
            return 0
        elif numero == 1:
            return 1
        else:
            return fib(numero - 2) + fib(numero - 1)
        


def fib_linear(numero:int):
    if numero < 0:
        print('Numero invalido')
    else:
        a = 0
        b = 1
        if numero == 0:
            return a
        elif numero == 1:
            return b
        else:
            for num in range(numero - 2):
                fibo = b + a
                a = b
                b = fibo
                
            return fibo