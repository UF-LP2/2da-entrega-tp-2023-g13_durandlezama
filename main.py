"""importo archivos necesarios"""
import random
from datetime import datetime
from src.cGuardia import Guardia
from src.cPaciente import Paciente
from src.cEnfermero import Enfermero
from src.cArbolSintomas import arbol_sintomas


def main() -> None:
    """desarrollo del main"""

    # esto es donde probe el valor que tiraba y lo tira bien
    enfermero = Enfermero("Maria", "5/12")
    saul = Paciente("Saul", 55, ["sudoracion", "fiebre", "nauseas y vomitos"])
    raiz = arbol_sintomas()
    aux = enfermero.busqueda(saul.sintomas, raiz, 0)

    lista = []

    guardia_sm = Guardia("Triage", 1000, lista)
    guardia_sm.leer_archivo()

    horario = datetime.now()

    while guardia_sm.lista_archivo:

        if horario.hour >= 23 and horario.hour <= 6:
            print(" hay un enfermo en la guardia")
        elif horario.hour >= 6 and horario.hour <= 10:
            print(" hay dos enfermeros en la guardia")
        elif horario.hour >= 10 and horario.hour <= 16:
            print(" hay cinco enfermeros en la guardia")
        elif horario.hour >= 16 and horario.hour <= 23:
            print(" hay tres enfermeros en la guardia")

        pac_llegados = random.randint(
            0, len(guardia_sm.lista_archivo))

        for c in range(pac_llegados):
            enfermero.clasificar(guardia_sm.lista_archivo[c])
            lista.append(guardia_sm.lista_archivo[c])

        del guardia_sm.lista_archivo[:pac_llegados-1]

        guardia_sm.lista_pacientes = guardia_sm.armar_lista(lista)
        guardia_sm.llamar()


if __name__ == "__main__":
    main()
