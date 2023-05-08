cant = 15
num = []
print(f"Ingrese {cant} de numeros ")
for i in range (cant):
    num = input(f"Ingrese un numero {i+1}: ")
    print(f"El numero que se ingreso fue el: {num}")
    print (f"El numero {num} es nuevo")
    print (f"El numero {num} ya se encuentra en el arreglo")