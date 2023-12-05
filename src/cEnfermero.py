from datetime import datetime
import time
from src.cPaciente import Paciente
from src.cArbolSintomas import arbol_sintomas

colores = {
    1: "Rojo",
    2: "Naranja",
    3: "Amarillo",
    4: "Verde",
    5: "Azul"
}


class Enfermero:
    "clase enfermero"

    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno

    def clasificar(self, pac: Paciente):
        """ metodo para clasificar"""

        tree = arbol_sintomas()
        valor = 0

        for i in pac.sintomas:
            valor = valor + self.busqueda(i, tree)

        if valor >= 100:
            pac.color = colores.get(1)
            pac.max_time = 0
        elif valor < 100 and valor >= 75:
            pac.color = colores.get(2)
            pac.max_time = 10
        elif valor < 75 and valor >= 50:
            pac.color = colores.get(3)
            pac.max_time = 60
        elif valor < 50 and valor >= 30:
            pac.color = colores.get(4)
            pac.max_time = 120
        else:
            pac.color = colores.get(5)
            pac.max_time = 240

        pac.tiempo_ingreso = datetime.now()

        time.sleep(0.1)  # simulamos el que tarda en clasificar
        return valor

    def busqueda(self, sintomas: str, raiz) -> int:
        """ metodo para recorrer el arbol y encontrar los sintomas"""
        if raiz is None:
            return 0

        suma_actual = 0

        if raiz.name in sintomas:
            suma_actual = raiz.value

        suma_izquierda = self.busqueda(sintomas, raiz.left)
        suma_derecha = self.busqueda(sintomas, raiz.right)

        return suma_actual + suma_izquierda + suma_derecha
