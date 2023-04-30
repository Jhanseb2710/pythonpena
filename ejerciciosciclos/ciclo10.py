def euclides (num1, num2, iteracciones=1):
    if num1<num2:
        num1,num2=num2,num1
        resta=num1%num2
        if resta==0:
            return (num2,iteracciones)
        return euclides(num2,resta,iteracciones+1)
num1=12
num2=4
comunDivisor, iteracciones= euclides(num1,num2)
print("El maximo comun divisor de {} y {} es: {}".format(num1,num2,comunDivisor))
print("Se ha encontrado en {} iteracciones".format(iteracciones))