x=int(input('ingrese numero: ')) #int almacena un valor numerico no decimal sea positivo o negativo
y=int(input('ingrese numero: '))
z=int(input('ingrese numero: '))
#indentación
if x>y: #If ejecuta el codigo cuando se cumple una condicion
    if x>z:
        print(f'el mayor es: {x}')
    else: #Else solo se utiliza si no se cumple con la condicion de If
        print(f'el mayor es: {z}')
else:
    if y>z:
        print(f'el mayor es: {y}')
    else:
        print(f'el mayor es: {z}')
        
# Se escriben tres numeros y se diferencia quien es el mayor de estos numeros