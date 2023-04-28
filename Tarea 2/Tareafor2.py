num = int(input("Escriba un numero positivo: "))
n = int(input("Desee hallar los multiplos: "))
cont = 0
for i in range (num):
    if i%n==0:
        print(f"{i} es multiplo de {n} ")
        cont = cont + 1
    else:
        print(i)
print("Hay :", cont, " multiplos de ", n)