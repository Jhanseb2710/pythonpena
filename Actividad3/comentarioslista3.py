import random
lista=[]
cuadrado=[]
tam=random.randint(5,10) #genera un entero entre a y b, donde a debe ser menor o igual que b
print(tam)
for i in range(tam):
    num=random.randrange(100) #genera un entero entre los valores generados por range, admitiendo entre uno y tres argumentos
    lista.append(num) #agrega un elemento de cualquier tipo al finalizar una lista
print(lista)

for i in range(len(lista)):
    cuadrado.append(lista[i]**2)
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)
print(sum(lista))