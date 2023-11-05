from datetime import datetime
from src.cPaciente import Paciente
from src.cArbolSintomas import arbol_sintomas


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

    def recorrer_arbol(self, paciente: Paciente):
        """Función para clasificar a los pacientes"""
        raiz = arbol_sintomas()
        while raiz is not None:
            if self.color(raiz):
                return raiz
            else:
                found = False
                for x in paciente.sintomas:
                    if x == raiz.nombre:
                        raiz = raiz.left
                        found = True
                        break
                if not found:
                    raiz = raiz.right
        return None  # Si no se encuentra ninguna clasificación adecuada, devuelve None

    def clasificar(self, paciente: Paciente):
        """ metodo para clasficar a los pacientes"""
        nodo = self.recorrer_arbol(paciente)
        paciente.clasificacion = nodo.nombre
        paciente.tiempo_espera = datetime.now()
        paciente.set_tiempo_max()
