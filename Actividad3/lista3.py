import random
num = [random.randint(0, 15)]
i = 1
valores=[random.randint(0, 15)]
repetidos=[]
while i < 15:
    e = random.randint (0, 15)
    if e not in num:
        num.append(e)
        i+=1
for i in valores :
    if i not in repetidos:
        repetidos.append(i)

print(num)
print(repetidos)