num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba otro numero: "))
rest = 0

if num2 < num1:
    rest = num1 - num2
    print(f"El  resultado de la resta es: {rest}")

else:
    resta = num2 -num1
    print(f"El resultado de la resta es: {rest}")
    
while rest !=0:
    if num1 < num2:
        rest = rest - num2
        print("El resultado de la resta es: ", rest)

    else:
        rest = rest - num2
        print("El resultado de la resta es:", rest)

    if rest <=0:
        print("No se puede restar mas: ")
        print("El residuo de la resta es: ", rest)
        break