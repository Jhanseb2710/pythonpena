import random #Random contiene funciones relacionadas con valores aleatorios y antes de esta se debe importar la funcion
num=int(random.random()*10) #random.random genera un numero decimal entre 0 y 1, pero genera solo 0
print(num)
num1=random.randint(0,100) #genera un entero entre a y b, donde a debe ser menor o igual que b
print(num1) 
num2=random.randrange(10) #genera un entero entre los valores generados por range, admitiendo entre uno y tres argumentos
print(num2)