"""importar clases"""
from src.cEnfermero import Enfermero
from src.cPaciente import Paciente


def test_clasificacion():
    """ testeamos la funcion de clasificar"""
    maria = Enfermero("Maria", "1-2")

    saul = Paciente("saul", 20, [
                    "dificultad para respirar", "perida de sangre extrema", "inconsiente"])

    maria.clasificar(saul)

    assert saul.clasificacion == "rojo"
