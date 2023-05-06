import random
lista = []
cuadrado = []
moda = []
sum = 0
prom = 0
mayor = 0
menor = 101
cont = 0
tama = random.randint (10, 20)
print (tama)
for i in range (tama):
    num = random.randrange(100)
    lista.append (num)
    sum += num
    e = num 
    if e > mayor:
        mayor = e
    if e < menor:
        menor = e
        prom = sum/tama
    def mediana (lista):
        media = len (lista) // 2
        lista.sort()
        if not len (lista) % 2:
            return (lista [media - 1] + lista[media]) / 2.0
        return lista[media]
print (lista)
print (f"La suma es: {sum}")
print (f"El promedio es: {prom}")
print (f"El mayor es: {mayor}")
print (f"El menor es: {menor}")
print (mediana(lista))