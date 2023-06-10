from Cliente import *
class Producto:
    def __init__(self,id,nombre,tipo,descripcion,precio):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__precio = precio
    
    def getProducto (self):
        return f"{self.__id} {self.__nombre} {self.__tipo} {self.__descripcion} {self.__precio}"
    
    #def descuentoProducto (self,precio):
        self.__precio = precio
        precio = self.__precio * 0.03
        return f"El precio con descuento para un individual es: {precio} "