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
nuevo_jugador1= jugador1 ("Kevin Mier", "arquero")
nuevo_jugador2= jugador2 ("Dorlan Pabon", "mediocampista")
print(nuevo_jugador1.descripcion())
print(nuevo_jugador1.rendimiento("9.6"))
print(nuevo_jugador2.descripcion())
print(nuevo_jugador2.rendimiento("8.8"))