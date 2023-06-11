from Cliente import *
from Productos import *
from Individual import *
from Empresa import *

# Se instancian objetos de la clase Cliente
persona = Cliente(10,"Normal","individual","hola")
persona2 = Cliente(20,"Normal","empresa","hola")

# Al objeto persona se le añade los metodos getDatos para visualizar todos los datos y el setId para modificar el Id
print (persona.getDatos())
print (persona.setId(11))
print (persona.getDatos())

# Se instancian 2 objetos ob1 y ob2 de la clase Producto 
ob1 = Producto(1,"Arroz","Grano","Grasas",1000)
ob2 = Producto(2,"Lenteja","Grano","Engorda",2000)

# A los dos objetos previamente instanciados se le asignan el metodo getProducto que viene de la clase Producto, estos 
# dos prints nos retornaran el valor de cada uno de los objetos
print(ob1.getProducto())
print(ob2.getProducto())

# Al objeto persona instanciado de la clase Cliente se le agrega el metodo agregarProducto con el parametro de 
# un producto, en este caso le pasaremos el objeto ob1 y ob2 creado desde la clase Producto para que lo añada en la lista de 
# productos del objeto al que se le esta pasando el metodo, lo que sucedera va a ser que se va añadir ob1 y ob2 a la 
# lista producto como ya lo habiamos dicho y nos mostrara es la direccion de memoria ya que por el momento ob1 y ob2 son 
# simplemente dos objetos
persona.agregarProducto(ob1)
persona.agregarProducto(ob2)

for producto in persona.getProductos():
    print (f"AGREGACION {producto.getProducto()}")

persona2.componerProducto(2,"Arroz","Grano","Grasas",2000)
persona2.componerProducto(3,"Arroz","Grano","Grasas",2000)
for producto in persona2.getProductos():
    print (f"COMPOSICION {producto.getProducto()}")

persona3 = Individual(27, "Jhan", "Individual", "empresario", "jhsbtian962016@gmail.com", 3133033390, "Cll 62D 75I 53")

print(persona3.getDatos())
print(isinstance(persona3,Individual))
producto = Producto(4, "Agua", "Bebida", "Lite", 1300)
persona3.agregarProducto(producto)
for i in persona3.getProductosList():
    print (f"Instanciado de Individual {i.getProducto()}")
print(persona3.descuentoProducto(1300))

empresa = Empresa("OTI","Empresa","Maderas",345789632, 5465)

print(empresa.getDatos())
print(isinstance(empresa,Empresa))
producto = Producto(1014, "Mueble", "Madera", "objeto", 45000)
empresa.agregarProducto(producto)
for i in empresa.getProductosList():
    print (f"Instanciado de Individual {i.getProducto()}")
print(empresa.descuentoProducto2())