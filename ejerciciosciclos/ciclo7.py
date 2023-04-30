num=0
n=float("inf")
print("Escriba numero: ") 
while num<n:
    j=(num+n)/2
    sum= j*(j+1)/2
    if sum>n:
        n=j
    else:
        num=j+1