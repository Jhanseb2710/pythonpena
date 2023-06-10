from Productos import *
class Cliente:
    def __init__(self,id,nombre,tipo,descripcion):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__productos = []
        
    def getDatos (self):
        return f"Su id es: {self.__id},su nombre es {self.__nombre}, su tipo es {self.__tipo}, su descripcion es {self.__descripcion}"
    
    def setId (self,id):
        self.__id = id
        return f"Su nuevo id es: {self.__id}"
    
    def agregarProducto (self,producto):
        self.__productos.append(producto)
        
    def componerProducto(self,id,nombre,tipo,descripcion,precio):
        ob3 = Producto(id,nombre,tipo,descripcion,precio)
        self.__productos.append(ob3)     

    def getProductos(self):
        return self.__productos