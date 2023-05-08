import random
num = [random.randint(0, 15)]
i = 1
while i < 15:
    e = random.randint (0, 15)
    if e not in num:
        num.append(e)
        i+=1
print (num)