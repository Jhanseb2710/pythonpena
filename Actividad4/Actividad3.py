import random
def generarLista(rango, tam):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    valores=[]
    repetidos=0
    for i in valores :
        if i not in repetidos:
            repetidos.append(i)
    print (repetidos)
    return lista
l1=generarLista(100,20)
rep=(l1)
print(l1)
print(rep)

