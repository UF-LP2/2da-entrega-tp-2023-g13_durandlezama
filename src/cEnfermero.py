from datetime import datetime
from src.cPaciente import Paciente
from src.cArbolSintomas import arbol_sintomas
from src.cArbolSintomas import Node


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

    def recorrer_arbol(self, sintomas: list[str], raiz: Node) -> Node:
        """Función para recorrer el arbol"""
        while raiz is not None:
            if self.color(raiz):
                return raiz
            else:
                found = False
                for x in sintomas:
                    if x == raiz.nombre:
                        raiz = raiz.left
                        found = True
                        sintomas.remove(x)
                        break
            if not found:
                raiz = raiz.right
        return None  # Si no se encuentra ninguna clasificación adecuada, devuelve None

    def clasificar(self, paciente: Paciente):
        """ metodo para clasficar a los pacientes"""
        raiz = arbol_sintomas()
        nodo = self.recorrer_arbol(paciente.sintomas, raiz)
        paciente.clasificacion = nodo.nombre
        paciente.tiempo_ingreso = datetime.now()
        paciente.set_tiempo_max()
