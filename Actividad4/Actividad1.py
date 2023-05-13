import random
x=0
mayor=0
menor=21
def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayorLista(lista):
    max=lista[0];
    for x in lista:
        if x > max:
            max=x
    return max

def menorLista(lista):
    min=lista[0];
    for x in lista:
        if x < min:
            min=x
    return min

def ordenar(lista):
    lista.sort()
    for lista in lista:
        print (lista)
        
def descender(lista):
    lista.sort(reverse=True)
    for lista in lista:
        print (lista)

from statistics import mode
def mediana (lista):
    media = len (lista) // 2
    lista.sort()
    if not len (lista) % 2:
        return (lista [media - 1] + lista[media]) / 2.0
    return lista[media]

l1=llenarLista(5,20)
print(l1)
print("La suma de la lista es: ", sumaLista(l1))
print("El promedio de la lista es: ", promedioLista(l1))
print("El mayor de la lista es: ", max(l1))
print("El menor de la lista es: ", min(l1))
print("El orden ascendente de la lista es: ", ordenar(l1))
print("El orden descendente de la lista es: ", descender(l1))
print("La  moda es: ", mode(l1))
print("La medana es: ", mediana(l1))