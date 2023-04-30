n=int(input("Ingrese un numero de cuatro cifras: "))
c4= n % 10
c3= int((n % 100) / 10)
c2= int((n % 1000) / 100)
c1= int((n - (n % 1000)) / 1000)
print (str(c4)+str(c3)+str(c2)+str(c1))
