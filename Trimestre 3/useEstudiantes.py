from Estudiantes import *
import csv
from statistics import median, mode
estudiantes=[]
with open("C:\\Users\\Familia Fonseca\\Desktop\\pythonpena\\pythonpena\\Trimestre 3\\Pruebas Saber-2019.csv") as csvarchivo:
    csvReader=csv.reader(csvarchivo)
    for row in csvReader:
        print(row[7],row[4],row[-6],row[-2])
        break

def sumacsv(ruta):
    columna27 = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna27 = row[-6]
                if valor_columna27.isdigit():
                    columna27.append(int(valor_columna27))
    suma27 = sum(columna27)
    return suma27

def mayorcsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna = row[-6]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return max(lista)

def menorcsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna = row[-6]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return min(lista)

def promediocsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna = row[-6]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return sum(lista) / len(lista)

def parescsv(ruta):
    pares = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna = row[-6]
                if valor_columna.isdigit():
                    numero = int(valor_columna)
                    if numero % 2 == 0:
                        pares.append(numero)
    return pares

def imparescsv(ruta):
    impares = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna = row[-6]
                if valor_columna.isdigit():
                    numero = int(valor_columna)
                    if numero % 2 != 0:
                        impares.append(numero)
    return impares

def mediacsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna = row[-6]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return sum(lista) / len(lista)

def modacsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        next(csvReader)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna = row[-6]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return mode(lista)

def medianacsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 28:
                valor_columna = row[-6]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return median(lista)

ruta = "C:\\Users\\Familia Fonseca\\Desktop\\pythonpena\\pythonpena\\Trimestre 3\\Pruebas Saber-2019.csv"

resultadoSuma = sumacsv(ruta)
print(".suma de los valores en la columna Resultado ICFES:", resultadoSuma)

mayorValor = mayorcsv(ruta)
print(".mayor valor en la columna Resultado ICFES:", mayorValor)

menorValor = menorcsv(ruta)
print(".menor valor en la columna Resultado ICFES:", menorValor)

promedio = promediocsv(ruta)
print(".promedio de los valores en la columna Resultado ICFES:", promedio)

numeros_pares = parescsv(ruta)
print(".pares en la columna Resultado ICFES:", numeros_pares)

numeros_impares = imparescsv(ruta)
print(".impares en la columna Resultado ICFES:", numeros_impares)

media = mediacsv(ruta)
print(".media de la columna Resultado ICFES:", media)

mediana= medianacsv(ruta)
print(".mediana de la columna Resultados ICFES:",mediana)

moda= modacsv(ruta)
print(".moda de la columna Resultados ICFES:", moda)

def resultadostxt():
    resultSum=resultadoSuma
    resultMay=mayorValor
    resultmen=menorValor
    resultProm=promedio
    resultPar=numeros_pares
    resultImp=numeros_impares
    resultmedia=media
    resultmediana=mediana
    resultmoda=moda

    with open("C:\\Users\\Familia Fonseca\\Desktop\\pythonpena\\pythonpena\\Trimestre 3\\resultados.txt","w") as n:
        n.write(f".suma de los valores en la columna Resultado ICFES:{resultSum}\n")
        n.write(f".mayor valor en la columna Resultado ICFES:{resultMay}\n")
        n.write(f".menor valor en la columna Resultado ICFES:{resultmen}\n")
        n.write(f".promedio de los valores en la columna Resultado ICFES:{resultProm}\n")
        n.write(f".pares en la columna Resultado ICFES:{resultPar}\n")
        n.write(f".impares en la columna Resultado ICFES:{resultImp}\n")
        n.write(f".media de la columna Resultado ICFES:{resultmedia}\n")
        n.write(f".mediana de la columna Resultado ICFES:{resultmediana}\n")
        n.write(f".moda de la columna Resultado ICFES:{resultmoda}\n")

a1=(resultadostxt())