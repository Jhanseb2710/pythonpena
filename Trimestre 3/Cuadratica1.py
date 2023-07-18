from math import sqrt

a= int(input("Ingresar numero: "))
b= int(input("Ingresar numero: "))
c= int(input("Ingresar numero: "))

cuadratica1= (b**2)-(4*a*c)
cuadratica2= (-b)
cuadratica3= (2*a)
raiz= sqrt(cuadratica1)

suma= ((cuadratica2 + raiz)/cuadratica3)
resta= ((cuadratica2 - raiz)/cuadratica3)

print (suma,resta)