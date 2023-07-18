try:
    x= int(input("Ingrese un numero: "))
    y= int(input("Ingrese un numero: "))
    x/y
    print(x/y)
except ZeroDivisionError:
    print("Error")