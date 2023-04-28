n= int(input("Introduce un numero positivo: "))
i=2
for num in range (2, 1001):
    while n % i != 0:
        i += 1
if i == n:
    print(str(n) + " Es primo. ")
else: 
    print(str(n) + " No es primo. ")