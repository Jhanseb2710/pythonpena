
#[], {}, (), {()}
x=100
print(type(x)) #type especifica el espacio de nombres con la definicion de clase  
x='Soacha'
print(type(x)) 
lista=['python',100,[1,2,3,[]],'a']
print(type(lista))
print(len(lista)) #len devuelve el tamaño que tiene un objeto que se ingreso
print(lista[0])
print(lista[1])
print(lista[3])
print(lista[-4])

del lista[-2] #del borra la lista que uno escoge
print(lista)

"""
cuenta1=cuenta()
cuenta2=cuenta()
cuenta3=cuenta()
cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""