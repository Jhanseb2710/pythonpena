class Persona:
    listaCursos = []
    def _init_(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__curso = []


    def addCursos(self, curso):
        self.__curso += [curso]

        for i in self.__curso:
            if i not in Persona.listaCursos:
                Persona.listaCursos.append(i)


    def getCursos(self):
        return self.__curso
                 

    def getDocumento(self):
        return self.__documento
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDocumento(self, documento):
        self.__documento = documento
        
    def getValues(self):
        return f"{self._nombre}, {self._documento}"
    
    def buscarCurso(self, curso):
        if curso in self.__curso:
            return f"El curso {curso} esta en la lista."
        else:
            return False
        
    def deleteCurso(self, cursoo):
        if cursoo in self.__curso:
            self.__curso.remove(cursoo)
      
        
    
    def updateCurso(self, curso, nuevocurso):
        if curso in self.__curso:
            for i in range(len(self.__curso)):
                if self.__curso[i] == curso:
                    self.__curso[i] = nuevocurso