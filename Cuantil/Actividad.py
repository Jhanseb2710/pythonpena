import random
def llenarLista(rango):
    lista=[]
    tam = random.randint (200, 2500)
    lista=[random.randrange(rango) for i in range(tam)]
    return lista
l1=llenarLista(500)
print(l1)
