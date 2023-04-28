inicio= int (input("Escriba un numero de inicio: "))
fin= int (input("Escriba un numero de fin: "))
incremento= int (input("Escriba un numero de incremento: "))
i=0
serie=0
for i in range (inicio, fin, incremento):
    serie= serie+1
    print(i)
    print(f"Serie {serie}")