import random
a=0
suma=0
suma2=0
tam=random.randint(20,30)
#lista=[random.randrange(0,5) for i in range(tam)]
nota=[round(random.random()*5,1) for i in range (tam)]
print(nota)

for e in range (tam):
    for j in range (e+1, tam ):
        if nota [e] > nota[j]:
            ayuda=nota[e]
            nota[e]=nota[j]
            nota[j]=ayuda

lista=["aprobo" if e >=3.0 else "reprobo" for e in nota]
aprueba=[e for e in nota if e >= 3.0]
print (f"Aprobo {aprueba}")
reprueba=[j for j in nota if j < 3.0]
print (f"Reprobo {reprueba}")
for n in aprueba:
    suma = suma + n
print("La suma de los aprobados es: ", suma)
prom=suma / len(aprueba)
print ("El promedio de los aprobados es: ", prom)
    
lista2=["Bajo" if a<=1.0 else "Malo"for a in nota] 
Bajo=[a for a in nota if a<=1.0]
print (f"Bajo {Bajo}")
Malo=[a for a in nota if a>1.0 and a<=2.0]
print (f"Malo {Malo}")
lista3=["Regular" if a<=3.0 else "Bueno"for a in nota] 
Regular=[a for a in nota if a>2.0 and a<=3.0]
print (f"Regular {Regular}")
Bueno=[a for a in nota if a>3.0 and a<=4.0]
print (f"Bueno {Bueno}")
Superior=[a for a in nota if a>4.0 and a<=5.0]
print (f"Superior {Superior}")

for g in reprueba:
    suma2 = suma2 + g
print("La suma de los reprobados es: ", suma2)
prom2=suma2 / len(reprueba)
print ("El promedio de los reprobados es: ", prom2)