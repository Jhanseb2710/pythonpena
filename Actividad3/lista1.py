import random
lista = []
listaascendente = []
listadescendente = []
reverse = 0
cuadrado = []
n = 0
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
    from statistics import mode
    def mediana (lista):
        media = len (lista) // 2
        lista.sort()
        if not len (lista) % 2:
            return (lista [media - 1] + lista[media]) / 2.0
        return lista[media]
listaascendente.sort ()
print (lista)
print (f"La suma es: {sum}")
print (f"El promedio es: {prom}")
print (f"El mayor es: {mayor}")
print (f"El menor es: {menor}")
print ("La moda es: ", mode(lista))
print ("La mediana es: ", mediana(lista))
print ("Orden ascendente: ", lista)