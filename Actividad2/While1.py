# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1
cont=0 #cont se le suma un valor constante
sum=0 #sum es la suma de los elementos
menor=1000000 #menor evalua si el valor de la izquierda es menor o igual al de la derecha
mayor=0 #mayor evalua si el valor de la derecha es mayor o igual al de la izquierda
while num!=0:
    num=int(input('ingrese numero: '))
    cont=cont+1
    sum=sum+num
    if num>mayor:
        mayor=num
    if num<menor and num!=0: #and opera hasta que se cumpla la operacion booleana
        menor=num

print(f'fueron ingresados {cont-1} numeros') #f imprime un mensaje por pantalla utilizando una cadena de formato
print(f'La suma es: {sum}')
print(f'El promedio es: {sum/(cont-1)}')
print(f'El mayor es: {mayor}')
print(f'El menor es: {menor}')