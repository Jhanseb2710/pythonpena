numeros = (21,45,27,54,63,27,27,4,3,2,1,21,80,54,27)
num = int(input("Dame un numero: "))
 
contador= 0
for i in numeros:
    if num == i:
        contador = contador + 1
 
print ("Hay ",contador," repeticion/es")