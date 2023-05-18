contactos = {}
salir = False
 
while (not salir):
    nombre=input("Introduzca un nombre: ")
    numero=int(input("Introduzca un numero de telefono: "))
    if(nombre not in contactos):
        contactos[nombre] = numero
        print('Añadido el contacto')
    else:
        print('El nombre esta repetido')
    respuesta = input("¿Quieres salir? (SI/N0): ")
 
    if(respuesta == "SI"):
        salir = True

print(contactos)