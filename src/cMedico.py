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
        if paciente.clasificacion == "naranja":  # como pasa el tiempo
            return "internado"
        elif paciente.clasificacion == "amarillo":  # como pasa el tiempo
            return (random.choice(estados))
        elif paciente.clasificacion == "verde" or paciente.clasificacion == "azul":  # como pasa el tiempo
            return "de alta"

        self.estado = True
        return


def derivar(paciente=Paciente):
    """clase medico"""
    paciente.clasificacion = 0
    # pass


def ir_a_casa():
    """clase medico"""
    # pass


def frenar_tiempo():
    """clase medico"""
    # pass
