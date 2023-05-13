def fib (e):
    if e == 0:
        return 0
    elif e == 1:
        return 1
    else:
        return fib (e-2) + fib (e-1)

for x in range (50):
    print (fib(x))