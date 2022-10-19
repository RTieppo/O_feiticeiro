from random import randint
def dado_duplo():
    numero_aleatorio1 = int(randint(1,6))
    numero_aleatorio2 = int(randint(1,6))
    return numero_aleatorio1 + numero_aleatorio2

def dado_unico():
    numero_aleatorio1 = int(randint(1,6))
    return numero_aleatorio1