"""importar clases"""
from src.cEnfermero import Enfermero
from src.cPaciente import Paciente


def test_clasificacion1():
    """test de rojo"""
    enfermero = Enfermero("Maria Durand", 1522)
    paciente = Paciente("Saul", 20, [
        "perdida de sangre externa", "dificultad para respirar", "inconsiente"])

    enfermero.clasificar(paciente)
    assert paciente.color == "Rojo"


def test_clasificacion2():
    """test de rojo"""
    enfermero = Enfermero("Maria Durand", 1522)
    paciente = Paciente("Saul", 20,  [
                        'dificultad para respirar', 'perdida de sangre externa', 'nauseas y vomitos'])

    enfermero.clasificar(paciente)
    assert paciente.color == "Rojo"


def test_clasificacion3():
    """test de rojo"""
    enfermero = Enfermero("Maria Durand", 1522)
    paciente = Paciente("Saul", 20, ['nauseas y vomitos', 'dolor', 'desmayo'])

    enfermero.clasificar(paciente)
    assert paciente.color == "Naranja"


def test_clasificacion4():
    """test de rojo"""
    enfermero = Enfermero("Maria Durand", 1522)
    paciente = Paciente(
        "Saul", 20, ['nauseas y vomitos', 'dolor', 'perdida de fuerza'])

    enfermero.clasificar(paciente)
    assert paciente.color == "Amarillo"


def test_clasificacion5():
    """test de rojo"""
    enfermero = Enfermero("Maria Durand", 1522)
    paciente = Paciente(
        "Saul", 20, ['picazon', 'no es urgente', 'no es urgente'])

    enfermero.clasificar(paciente)
    assert paciente.color == "Azul"
