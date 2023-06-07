class Cursos: 
    listaCursos=list() 
    def __int__(self, nombreCurso): 
        self.nombreCurso = nombreCurso 
    def menu(): 
        seleccionar = 0 
        while seleccionar != 5: 
            print("1. Mostrar los cursos") 
            print("2. Agregar cursos") 
            print("3. Cursos registrados del alumno") 
        seleccionar = int(input("Elige una opción: ")) 
    if seleccionar == 1: 
        mostrar() 
    if seleccionar == 2: 
        agregar() 
    if seleccionar == 3: 
        buscar() 
    listaCursos=list() 
    for cursos in listaCursos: 
        def mostrar(): 
            for cursos in listaCursos:
                cursos=cursos 
                print("Hay ", listaCursos.__len__(), " cursos registrados") 
        def agregarCurso(): 
            for curso in listaCursos: 
                if curso == Cursos(): 
                    curso.nombreCurso = input("Introduce el nombre del curso: ") 
                    listaCursos.append(curso) 
        def buscarCursos(): 
            for curso in listaCurso: 
                print("El nombre del curso es:", curso.nombreCurso)