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

        if paciente.color == "naranja":  # como pasa el tiempo
            return "internado"
        elif paciente.color == "amarillo":  # como pasa el tiempo
            return (random.choice(estados))
        elif paciente.color == "verde" or paciente.color == "azul":  # como pasa el tiempo
            return "de alta"

        self.estado = True
        return
