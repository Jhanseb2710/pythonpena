import csv

with open("datos.csv",newline="") as archivo_csv:
    lector_csv=csv.reader(archivo_csv, delimiter=",", quotechar='"')
    for fila in lector_csv:
        print(fila)