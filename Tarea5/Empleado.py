class Empleado:
    def __init__(self, nombre, cargo,extra, salario,incremento):
        self.__nombre= nombre
        self.__cargo= cargo
        self.__extra=extra
        self.__salario= salario
        self.__incremento= incremento
        

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre
    
    def getCargo(self):
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo=cargo
    
    def getExtra(self):
        return self.__extra
    def setExtra(self, extra):
        if extra <= 40:
            x=extra*4833
            self.__salario= self.__salario+ x
        else:
            return self.__salario
    
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
                    
p=Empleado ("Jhan", "Ingenierio", 30, 1160000, 1160000)
print(p.getNombre())
print(p.getCargo())
print(p.getExtra())
print(p.getSalario())
print(p.getIncremento())