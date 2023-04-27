for i in range(11): #for ejecuta un objeto en lista, conjunto, diccionario y ejecuta el bloque en codigo
    if i%3==0:
        print(f'{i} es multiplo de 3')
    else:
        print(i)

for j in range(1,11): #range representa una secuencia de numeros constante
    print(j)

for k in range(0,11,2):
    print(k)

for i in range(20,0,-2):
    print(i)
#El primer caso ejecuta los multiplos de 3, el segundo todos los numeros de 1 a 10, el tercero los pares de 0 a 10 y el cuarto los pares de 20 a 2 