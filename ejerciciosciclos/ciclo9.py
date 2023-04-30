def potencia(num, exp):
    cont=1
    elevado=1
    while cont<=exp:
        elevado=elevado*num
        cont=cont+1
    return elevado
print(potencia (5,9))