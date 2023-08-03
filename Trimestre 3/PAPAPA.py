try:
    papapa=open("C:\\Users\\Familia Fonseca\\Documents\\PA PA PA.txt","r",encoding= "utf-8")
    cont=1
    linea=papapa.readline()
    c=1
    while linea!="":
        print(f"{c} {linea}")
        linea=papapa.readline()
        c+=1
except IOError as e:
    print(e,"......")