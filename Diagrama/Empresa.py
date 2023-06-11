from Cliente import *

class Empresa(Cliente):
    def __init__(self,nombre,telefono,fax, precio):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__fax = fax
        self.__precio = precio
        
    def getDatos(self):
        return f"{self.__nombre},{self.__telefono},{self.__fax}"
    
    def agregarProducto (self,producto):
        self.__productos.append(producto)

    def componerProducto(self,id,nombre,tipo,descripcion,precio):
        ob4 = Producto(id,nombre,tipo,descripcion,precio)
        self.__productos.append(ob4) 
        
    def descuentoProducto (self,precio):
        self.__precio = precio
        descuento = self.__precio * 0.2
        precio= self.__precio - descuento
        return f"El precio con descuento para una empresa es: {precio} "
    
    def getProductosList(self):
        return self.__productos