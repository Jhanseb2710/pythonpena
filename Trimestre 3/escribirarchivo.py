import csv

datos=[
    ["Juan","Perez", 25],
    ["Maria","Gonzalez", 30],
    ["Pedro","Fernandez", 40]
]

with open("datos.csv","w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    for fila in datos:
        escritor_csv.writerow(fila)