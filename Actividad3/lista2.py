import random
lista1 = []
lista2 = []
cuadrado = []
suma1 = 0
suma2 = 0
promedio = 0
mayor = 0
menor = 101
par1 = 0
impar1 = 0
par2 = 0
impar2 = 0
tam = random.randint (10, 21)
for i in range (tam):
    num = random.randrange (100)
    lista1.append(num)
    suma1 += num
    n = num
    if n > mayor :
        mayor = n
    if n < menor:
        menor = n
    promedio1 = suma1/tam
    if i % 2 == 0:
            par1 += 1
    else :
        impar1 +=1
for i in range (tam):
    num = random.randrange (100)
    lista2.append (num)
    suma2 += num
    n = num
    if n > mayor :
        mayor = n
    if n < menor :
        menor = n
    promedio2 = suma2/tam
    if i % 2 == 0:
        par2 += 1
    else :
        impar2 +=1
promedio = suma1+suma2/tam
                    
print (lista1)
print (lista2)
print (f"El menor de las dos filas es: {menor}")
print (f"El mayor de las dos filas es: {mayor}")
print (f"La suma de los numeros de la lista1 es: {suma1}")
print (f"La suma de los numeros de la lista2 es: {suma2}")
if suma1 > suma2 :
    print ("La suma1 es mayor que suma2")
else:
    print ("La suma2 es mayor que suma1")
print (f"El promedio es: {promedio}")
print (f"El promedio de los numeros de la lista1 es: {promedio1}")
print (f"El promedio de los numeros de la lista2 es: {promedio2}")
if promedio1 > promedio2 :
    print ("El promedio1 es mayor que promedio2")
else:
    print ("El promedio2 es mayor que promedio1")
print ("El total de numeros pares es:", par1 )
print ("El total de numeros impares es: ", impar1)
print ("El total de numeros pares es: ", par2 )
print ("El total de numeros impares es: ", impar2)
if par1 > par2 :
    print ("El par1 es mayor que par2")
else:
    print ("son iguales")
