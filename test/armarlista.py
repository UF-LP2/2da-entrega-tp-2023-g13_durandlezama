import pytest

from src.cGuardia import Guardia
from src.cPaciente import Paciente


def test_armadoLista():
    """ hola"""
    lista = []
    paciente1 = Paciente("paxiente 1", 12, lista)
    paciente2 = Paciente("paxiente 1", 12, lista)
    paciente3 = Paciente("paxiente 1", 12, lista)
    paciente4 = Paciente("paxiente 1", 12, lista)
    paciente5 = Paciente("paxiente 1", 12, lista)
    paciente6 = Paciente("paxiente 1", 12, lista)

    guardia = Guardia("Saul", 1999)

    resultado = []
    resultado = guardia.armar_lista(paciente1)
    resultado = resultado = guardia.armar_lista(paciente2)
    resultado = guardia.armar_lista(paciente3)
    resultado = guardia.armar_lista(paciente4)
    resultado = guardia.armar_lista(paciente5)
    resultado = guardia.armar_lista(paciente6)

    lista = [paciente6, paciente3, paciente4, paciente2, paciente1, paciente5]

    assert resultado == lista
