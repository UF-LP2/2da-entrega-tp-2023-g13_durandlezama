"""importar clases"""
import pytest
from src.cEnfermero import Enfermero
from src.cPaciente import Paciente


def test_clasificacion1():
    """test de rojo"""
    enfermero = Enfermero("Maria Durand", 1522)
    paciente = Paciente("Saul", 20, [
        "perdida de sangre externa", "dificultad para respirar", "inconsiente"])

    enfermero.clasificar(paciente)
    assert paciente.color == "Rojo"
