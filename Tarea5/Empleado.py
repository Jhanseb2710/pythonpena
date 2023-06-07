class Empleado:
    def __init__(self, nombre, cargo, salario,incremento, extra):
        self.__nombre= nombre
        self.__cargo= cargo
        self.__salario= salario
        self.__incremento= incremento
        self.__extra= extra
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre
    
    def getCargo(self):
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo=cargo
    
    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario= salario
        
    def getIncremento(self):
        return self.__incremento
    def setIncremento(self, incremento):
        self.__incremento= incremento
        if self.__salario >= 1160000:
            self.__salario + 0.1612 
        else:
            self.__salario + 0.1312
            return self.__incremento
            
    def getExtra(self):
        return self.__extra
    def setExtra(self, extra):
        self.__extra=extra
        if extra <= 40:
            x=extra*4833
            self.__salario+ x
        else:
            return self.__salario
                    
p=Empleado ("Jhan", "Ingenierio", 1160000, 1160000, 30)
#q= Empleado ("Michell", "Contadora")
print(p.getNombre())
print(p.getCargo())
print(p.getSalario())
print(p.getIncremento())
print(p.getExtra())