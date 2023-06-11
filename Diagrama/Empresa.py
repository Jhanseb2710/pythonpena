from Cliente import *
from Productos import *
class Empresa(Cliente):
    def __init__(self,nombre,tipo,descripcion,telefono,fax):
        super().__init__(nombre,tipo,descripcion)
        self.__nombre = nombre
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__telefono = telefono
        self.__fax = fax
        self.__productos = []
        
    def getDatos(self):
        return f"{self.__nombre},{self.__tipo},{self.__descripcion},{self.__telefono},{self.__fax}"
    
    def agregarProducto (self,producto):
        self.__productos.append(producto)

    def componerProducto(self,id,nombre,tipo,descripcion,precio):
        ob4 = Producto(id,nombre,tipo,descripcion,precio)
        self.__productos.append(ob4) 
        
    def descuentoProducto2 (self,precio):
        self.__precio = precio
        descuento = self.__precio * 0.2
        precio= self.__precio - descuento
        return f"El precio con descuento para una empresa es: {precio} "
    
    def getProductosList(self):
        return self.__productos