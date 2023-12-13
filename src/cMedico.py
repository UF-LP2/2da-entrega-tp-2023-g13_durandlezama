""" imporar librerias"""
import random
from src.cPaciente import Paciente


class Medico:
    """clase medico"""

    def __init__(self, nombre: str, estado=True):
        self.nombre = nombre
        self.estado = estado

    def atender(self, paciente=Paciente):
        """funcion donde se atienden a los pacientes"""
        self.estado = False
        estados = ["internado", "de alta"]

        if paciente.color == "Naranja":  # como pasa el tiempo
            return "internado"
        elif paciente.color == "Amarillo":  # como pasa el tiempo
            return (random.choice(estados))
        elif paciente.color == "Verde" or paciente.color == "Azul":  # como pasa el tiempo
            return "de alta"

        self.estado = True
        return
