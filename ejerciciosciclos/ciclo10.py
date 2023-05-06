e = int (input("Ingrese un numero: "))
j = int (input("Ingrese un numero: "))
mod = 0
while e % j !=0:
    mod = e % j
    e = j
    j = mod
print (f"El maximo comun divisor es: {j}")