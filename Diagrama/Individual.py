from Cliente import *
from Productos import *
class Individual(Cliente):
    def __init__(self,id,nombre,tipo,descripcion,email,telefono,direccion):
        super().__init__(id,nombre,tipo,descripcion)
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__email = email
        self.__telefono = telefono
        self.__direccion = direccion
        self.__productos = []
        #self.__precio= precio
        
    def getDatos(self):
        return f"{self.__id},{self.__nombre},{self.__tipo},{self.__descripcion},{self.__email},{self.__telefono},{self.__direccion}" 
    
    def setId (self,id):
        self.__id = id
        return f"Su nuevo id es: {self.__id}"
    
    def agregarProducto (self,producto):
        self.__productos.append(producto)

    def componerProducto(self,id,nombre,tipo,descripcion,precio):
        ob3 = Producto(id,nombre,tipo,descripcion,precio)
        self.__productos.append(ob3)    

    def descuentoProducto (self,precio):
        self.__precio = precio
        descuento = self.__precio * 0.35
        precio = self.__precio - descuento
        return f"El precio con descuento para un individual es: {precio} "
    
    def getProductosList(self):
        return self.__productos