n=int(input('ingrese numero: '))
i=1
while i<n:
    if i%7==0:
        print(f'{i} es multiplo de 7')
    else:
        print(i)
    i+=1
    
#Se escribe un numero y hasta ese numero se digita toda la lista, escogiendo los multiplos de 7