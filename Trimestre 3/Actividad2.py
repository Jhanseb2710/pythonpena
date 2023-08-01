from os import strerror

try:
    file=open("c:\\Jhan\\ datospersonales.txt","wt")
    nombres=str(input("Ingrese sus nombres: "))
    apellidos=str(input("Ingrese sus apellidos: "))
    documentos=str(input("Ingrese su documento de identidad: "))
    direccion=str(input("Ingrese su direccion: "))
    ciudad=str(input("Ingrese su ciudad de residencia: "))
    telefono=str(input("Ingrese su telefono: "))
    email=str(input("Ingrese su correo elecronico: "))
    
    for i in range(1):
        file.write(nombres + "\n")
        file.write(apellidos + "\n")
        file.write(documentos + "\n")
        file.write(direccion + "\n")
        file.write(ciudad + "\n")
        file.write(telefono + "\n")
        file.write(email + "\n")

    file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))