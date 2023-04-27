x,y=3,5
cont=1
while not(x%y==0 or y%x==0): #not invierte el resultado verdadero/falso de la siguiente expresion
    print(f'intento numero {cont}')
    x=int(input('ingrese numero: '))
    y=int(input('ingrese numero: '))
    cont+=1

print(f'{x} y {y} son factor')