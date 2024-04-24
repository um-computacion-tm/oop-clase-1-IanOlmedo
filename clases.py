"""Tarea:
Agregar test para clase Materia y Profesor incluyendo test de constructor y demás metodos
La clase materia deberia tener un atributo __ alumnos __ equivalente a una lista de Alumnos. Empezando por los tests:
Implementar la clase Alumno
Agregar atributo __ alumno __ a clase Materia
Agregar metodo obtener_alumnos(self) que devuelva __ alumnos __"""



class Materia:
    def __init__(self, nombre, profesores, alumnos):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        return self.__alumnos__


class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__
    
    def cambiar_cargo(self, cargo):
        self.__cargo__ = cargo


class Alumno:
    def __init__(self, nombre, legajo, materias):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__materias__ = materias   #lista de materias en las que esta matriculado

    def obtener_nombre(self):
        return self.__nombre__
    
    def obtener_legajo(self):
        return self.__legajo__
    
    def obtener_materias(self):
        return self.__materias__
    
    def matricularse(self, materia):
        self.__materias__.append(materia)

    



    