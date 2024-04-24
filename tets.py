from clases import Materia, Profesor, Alumno
import unittest

class TestClases(unittest.TestCase):
    def test_materia(self):
        materia_1 = Materia(nombre="Programacion", profesores="Marcos", alumnos= None)
        self.assertEqual(materia_1.__nombre__, "Programacion")
        self.assertEqual(materia_1.__profesores__, "Marcos")

    def test_ver_alumnos_de_materia(self):  # quiero que muestre la lista de alumnos
        alumno_1 = Alumno("Rigoni", 62143, ["Calculo 1", "Algebra"])
        alumno_2 = Alumno("Valen", 62145, ["Calculo 1", "Electrotecnia"])
        alumnos = [alumno_1,alumno_2]
        materia_1 = Materia(nombre="Calculo 3", profesores="Artal", alumnos=alumnos)
        self.assertEqual(materia_1.obtener_profesores(), "Artal")
        self.assertEqual(materia_1.obtener_alumnos(), alumnos)

    def test_profesor(self):
        profesor_1 = Profesor("Marcos", "Titular", 3456)
        self.assertEqual(profesor_1.__nombre__, "Marcos")
        self.assertEqual(profesor_1.__cargo__, "Titular")
        self.assertEqual(profesor_1.__legajo__, 3456)

    def test_obtener_profesores(self):
        profesor_1 = Profesor("Marcos", "Titular", 3456)
        self.assertEqual(profesor_1.obtener_legajo(), 3456)
        self.assertEqual(profesor_1.obtener_cargo(), "Titular")
        self.assertEqual(profesor_1.obtener_nombre(), "Marcos")

    def test_cambiar_cargo(self):
        profesor_1 = Profesor("Marcos", "Titular", 3456)
        profesor_1.cambiar_cargo("Remplazante")
        self.assertEqual(profesor_1.__cargo__, "Remplazante")

    def test_alumno(self):
        alumno_1 = Alumno("rigoni", 62143, ["Calculo 1", "Algebra"])
        self.assertEqual(alumno_1.__nombre__, "rigoni")
        self.assertEqual(alumno_1.__legajo__, 62143)
        self.assertEqual(alumno_1.__materias__, ["Calculo 1", "Algebra"])
        
    def test_matricularse(self):
        alumno_1 = Alumno("rigoni", 62143, ["Calculo 1", "Algebra"])
        alumno_1.matricularse("Electrotecnia")
        self.assertEqual(alumno_1.__materias__, ["Calculo 1", "Algebra", "Electrotecnia"]) 

    
unittest.main()