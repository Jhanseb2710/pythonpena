import random
def generarLista(rango, tam):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista
def repetidos(lista):
    rep={}
    for i in lista:
        if i in rep:
            rep[i] +=1
        else:
            rep[i]=0
    print(len(rep))
        
l1=generarLista(100,20)
print(l1)
print("Los numeros repetidos en la lista son: ", repetidos(l1) )