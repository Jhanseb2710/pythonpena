from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt") 
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close() 
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno)) 