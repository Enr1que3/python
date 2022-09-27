class Alumno:
    nombre=None
    nota=None
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        if nota>=60:
            print(nombre,"Aprobado con",nota)
        else:
            print(nombre,"Reprobado con",nota)
    
a=Alumno("Enrique",50)


