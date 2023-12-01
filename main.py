"""importo archivos necesarios"""
import random
from datetime import datetime
from src.cArbolSintomas import arbol_sintomas
from library.leer_archivos import leer_archivo
from library.leer_archivos import archivo_m
from library.leer_archivos import archivo_e
from src.cPaciente import Paciente
from src.cEnfermero import Enfermero


def main() -> None:
    enfermero = Enfermero("Maria Durand", 1522)
    paciente = Paciente("Saul", 20, ['nauseas y vomitos', 'dolor', 'desmayo'])

    enfermero.clasificar(paciente)

    lista_doc = archivo_m()
    lista_enf = archivo_e()
    lista_pac = leer_archivo()


if __name__ == "__main__":
    main()
