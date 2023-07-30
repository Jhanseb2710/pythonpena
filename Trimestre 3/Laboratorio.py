from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
non_alpha_numeric_count = 0

file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
            elif not char.isnumeric() and not char.isspace():
                non_alpha_numeric_count += 1
    file.close()

    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)

    print("No son alfabeticos ni numericos ->", non_alpha_numeric_count)
    
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))




