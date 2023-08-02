import csv

datos=[
    ["Jhan","Peña", "jhsbtian962016@gmail.com"],
    ["Maria","Fonseca", "mariacfonsecac9805@gmail.com"],
    ["Victor","Peña", "victorfernandobeltran2807@gmail.com"]
]

with open("datos.csv","w")as archivo:
    escritor=csv.writer(archivo)
    for fila in datos:
        escritor.writerow(fila)