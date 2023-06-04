class equipo:
    pass
    def __init__(self,nombre,posicion):
        self.nombre=nombre
        self.posicion=posicion
    def descripcion(self):
        return "{} es un jugador de posicion {}".format(self.nombre,self.posicion)
class jugador1 (equipo):
    def rendimiento(self,rendimiento):
        return "{} su rendimiento en el partido fue de {}".format(self.nombre,rendimiento)
class jugador2 (equipo):
    def rendimiento(self,rendimiento):
        return "{} su rendimiento en el partido fue de {}".format(self.nombre,rendimiento) 
nuevo_jugador= jugador1 ("Kevin Mier", "arquero")
print(nuevo_jugador.descripcion())
print(nuevo_jugador.rendimiento("9.6"))