import math as math

def primos_linear(n: int):
    if n <= 1:
        print('numero invalido') 
    lista = []
    for num in range(2, n + 1):
        if eh_primo(num) == True:
            lista.append(num)
    
    return lista


def primos_rec(n:int, lista_aux: list = []):
    if n <= 1:
        print('numero invalido') 
    lista = lista_aux
    if n == 2:
        lista.append(n)
        lista.sort()
        return lista
    else:
        if eh_primo(n) == True:
            lista.append(n)
        return primos_rec(n-1, lista)



def eh_primo(n: int):
    aux = math.sqrt(n)
    for i in range(2, round(aux)+1):
        if n % i == 0:
            return False
            
    return True

