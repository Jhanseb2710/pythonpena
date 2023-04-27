cantidad = float(input("¿Cantidad a invertir?: "))
intereses = float(input("¿Interes porcentual anual?: "))
años = int(input("¿Años?: "))
for i in range(años) :
    cantidad *= 1+ intereses/100
    print("Capital tras " + str(i+1) + "años: "+ str(round(cantidad,2)))