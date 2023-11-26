from datetime import datetime
from src.cPaciente import Paciente
from src.cArbolSintomas import arbol_sintomas
import binarytree


class Enfermero:
    "clase enfermero"

    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno

    def color(self, nodo):
        """def color"""

        if nodo.nombre == "rojo" or nodo.nombre == "naranja" or nodo.nombre == "amarillo" or nodo.nombre == "verde" or nodo.nombre == "azul":
            return True
        else:
            return False

    def clasificar(self, paciente: Paciente):
        """ metodo para clasficar a los pacientes"""
        raiz = arbol_sintomas()
        nodo = self.busqueda(paciente.sintomas, raiz, 0)
        paciente.clasificacion = nodo.nombre
        paciente.tiempo_ingreso = datetime.now()
        paciente.set_tiempo_max()

    def busqueda(self, sintomas: str, raiz: binarytree, suma) -> int:
        """ metodo para recorrer el arbol y encontrar los sintomas"""

        if raiz is None:
            return 0

        suma_actual = 0
        if raiz.name in sintomas:
            suma_actual = raiz.value

        suma_izquierda = self.busqueda(sintomas, raiz.left, suma)
        suma_derecha = self.busqueda(sintomas, raiz.right, suma)

        return suma_actual + suma_izquierda + suma_derecha
